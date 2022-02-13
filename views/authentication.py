#Imports
import firebase_admin
import pyrebase
from firebase_admin import credentials, auth
from flask import Blueprint, abort, redirect, request, session
from google_auth_oauthlib.flow import Flow
from google.oauth2 import id_token
from pip._vendor import cachecontrol

from utils import access_secret

import settings
import requests
import google.auth.transport.requests

# main의 app에 대해 확장
bp = Blueprint('authentication', __name__, url_prefix='/')

#Connect to firebase
cred = credentials.Certificate(access_secret("FIREBASE_ADMIN_CONFIG"))
firebase = firebase_admin.initialize_app(cred)
pb = pyrebase.initialize_app(access_secret('FIREBASE_CONFIG'))

# google auth 인스턴스 생성
flow =Flow.from_client_config(
    client_config=access_secret('CLIENT_SECRET'),
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri=settings.BASE_URL+ ':8080'+ '/callback'
)

# Wrappers
def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()

    return wrapper


# Functions
def register(user_info:dict):
    try:
        auth.create_user(uid=user_info['sub'], email=user_info['email'], email_verified=user_info['email_verified'])
    except auth.UidAlreadyExistsError:
        print('User already Exists.')
    print('Register succeed.')

def signin(user_info:dict):
    try:
        auth.get_user(user_info['sub'])
    except auth.UserNotFoundError :
        print('user not found')
        print('Go into Register.')
        register(user_info)
    print('sign in succeed.')

# Routes
@bp.route("/authenticate")
def authenticate():
    return "Hello World <a href='/login'><button>Login</button></a>"

@bp.route('/login')
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state

    return redirect(authorization_url)

@bp.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    # 토큰의 무결성 검증
    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=access_secret('GOOGLE_OAUTH2_CLIENT_ID')
    )
    # 세션에 저장해서 url이 바뀌어도 로그인상태가 유지
    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")

    signin(id_info)
    return redirect("/")

@bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")
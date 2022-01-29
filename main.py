import pathlib
from flask import Flask, abort, redirect, render_template, request, session
from flask_assets import Environment, Bundle
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
import google.auth.transport.requests
from pip._vendor import cachecontrol
from get_data import get_index_data

import os
import requests

from secret_manager import access_secret
# 플라스크 앱 인스턴스 생성
app = Flask(__name__)
app.secret_key = access_secret('FLASK_KEY')
app.config['SESSION_TYPE'] = 'filesystem'
app.config['GOOGLE_OAUTH2_CLIENT_ID'] = access_secret('GOOGLE_OAUTH2_CLIENT_ID')
app.config['GOOGLE_OAUTH2_CLIENT_SECRET'] = access_secret('GOOGLE_OAUTH2_CLIENT_SECRET')

# SCSS 세팅
assets = Environment(app)
assets.url = app.static_url_path # =static/
scss = Bundle('scss/index.scss', filters='pyscss', output='all.css') # all.css 로 컴파일되서 assets.url(static/)에 저장됨
assets.register('scss_all', scss)

# Google oauth 설정
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")
flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://localhost:8080/callback"
)
def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()

    return wrapper

### Routes ###
@app.route('/', methods=['POST', 'GET'])
def index():
    firebase_config = access_secret('FIREBASE_CONFIG')

    return render_template('index.html',
        video_list=get_index_data(),
        config=firebase_config
    )

# 로그인 관련

@app.route("/login")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)


@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=access_secret('GOOGLE_OAUTH2_CLIENT_ID')
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/protected_area")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/auth")
def auth():
    return "Hello World <a href='/login'><button>Login</button></a>"


@app.route("/protected_area")
@login_is_required
def protected_area():
    return f"Hello {session['name']}! <br/> <a href='/logout'><button>Logout</button></a>"


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='127.0.0.1')
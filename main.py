from flask import Flask, render_template
from flask_assets import Environment, Bundle

import os
from settings import BASE_URL

from utils.secret_manager import access_secret
# 플라스크 앱 인스턴스 생성
app = Flask(__name__)
app.secret_key = access_secret('FLASK_KEY')
app.config['SESSION_TYPE'] = 'filesystem'
app.config['GOOGLE_OAUTH2_CLIENT_ID'] = access_secret('GOOGLE_OAUTH2_CLIENT_ID')
app.config['GOOGLE_OAUTH2_CLIENT_SECRET'] = access_secret('GOOGLE_OAUTH2_CLIENT_SECRET')

from views import home, authentication, detail, profile
app.register_blueprint(authentication.bp)
app.register_blueprint(home.bp)
app.register_blueprint(detail.bp)
app.register_blueprint(profile.bp)

# SCSS 세팅
assets = Environment(app)
assets.url = app.static_url_path # =static/
scss = Bundle('scss/main.scss', filters='pyscss', output='all.css') # all.css 로 컴파일되서 assets.url(static/)에 저장됨
assets.register('scss_all', scss)

# Google oauth 설정
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='localhost')    

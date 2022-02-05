from flask import Flask, render_template
from flask_assets import Environment, Bundle
from get_data import get_index_data

import os

from utils.secret_manager import access_secret
# 플라스크 앱 인스턴스 생성
app = Flask(__name__)
app.secret_key = access_secret('FLASK_KEY')
app.config['SESSION_TYPE'] = 'filesystem'
app.config['GOOGLE_OAUTH2_CLIENT_ID'] = access_secret('GOOGLE_OAUTH2_CLIENT_ID')
app.config['GOOGLE_OAUTH2_CLIENT_SECRET'] = access_secret('GOOGLE_OAUTH2_CLIENT_SECRET')
from views import authentication
app.register_blueprint(authentication.bp)

# SCSS 세팅
assets = Environment(app)
assets.url = app.static_url_path # =static/
scss = Bundle('scss/index.scss', filters='pyscss', output='all.css') # all.css 로 컴파일되서 assets.url(static/)에 저장됨
assets.register('scss_all', scss)

# Google oauth 설정
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"



### Routes ###
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html',
        video_list=get_index_data()
    )


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
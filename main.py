from flask import *
from flask_assets import Environment, Bundle
from oauth2client.contrib.flask_util import UserOAuth2


from get_data import get_index_data

import os


# 플라스크 앱 인스턴스 생성
app = Flask(__name__)
app.secret_key = '12343'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['GOOGLE_OAUTH2_CLIENT_ID'] = '670894580412-cl3vjkghu68hb2e79fq7tg9tptjqb84t.apps.googleusercontent.com'
app.config['GOOGLE_OAUTH2_CLIENT_SECRET'] = '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'
oauth2 = UserOAuth2(app)

# SCSS 세팅
assets = Environment(app)
assets.url = app.static_url_path # =static/
scss = Bundle('scss/index.scss', filters='pyscss', output='all.css') # all.css 로 컴파일되서 assets.url(static/)에 저장됨
assets.register('scss_all', scss)

## routes
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html', video_list=get_index_data())

@app.route('/test')
@oauth2.required
def test():
    if oauth2.has_credentials():
        print('login OK')
    else:
        print('login NO')
    return render_template('test.html')

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
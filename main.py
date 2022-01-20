from flask import *
from flask_assets import Environment, Bundle

from get_data import get_index_data


# 플라스크 앱 인스턴스 생성
app = Flask(__name__)

# SCSS 세팅
assets = Environment(app)
assets.url = app.static_url_path # =static/
scss = Bundle('scss/index.scss', filters='pyscss', output='all.css') # all.css 로 컴파일되서 assets.url(static/)에 저장됨
assets.register('scss_all', scss)

## routes
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html', video_list=get_index_data())

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080, debug=True)
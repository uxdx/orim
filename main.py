from flask import *

from get_data import get_index_data


# 플라스크 앱 인스턴스 생성
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html', video_list=get_index_data())

if __name__ == '__main__':
    app.run(debug=True)
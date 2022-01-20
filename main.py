import pyrebase
import json
from flask import *

# secrets.json 로딩
with open("secrets.json") as jsonFile:
    secrets = json.load(jsonFile)
    jsonFile.close()
config = secrets['config']
# 파이어베이스 인스턴스 생성
firebase = pyrebase.initialize_app(config)
# 데이터베이스 인스턴스 생성
db = firebase.database()
# 플라스크 앱 인스턴스 생성
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main():
    # # POST 요청이 접수된 경우
    # if request.method == 'POST':
    #     name = request.form['name'] # input의 name 부분
    #     db.child('todo').push(name) # 데이터베이스의 'todo' 하위분류에 name을 추가
    #     todo = db.child('todo').get() # 데이터베이스의 'todo' 부분을 get
    #     todo_list = todo.val() # 그 값의 dict형태
    #     print(todo_list.values())
    #     return render_template('index.html', todo=todo_list.values())


    video_list= dict()
    video = {
        "url" : "https://asd",
        "thumbnail" : "https:/asdfasdf",
    }
    for i in range(2):
        key = str(i)
        video_list[key] = video

    print(video_list)

    return render_template('index.html', video_list=video_list)

if __name__ == '__main__':
    app.run(debug=True)
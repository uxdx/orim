import pyrebase
import json

# secrets.json 로딩
with open("secrets.json") as jsonFile:
    secrets = json.load(jsonFile)
    jsonFile.close()
config = secrets['config']
# 파이어베이스 인스턴스 생성
firebase = pyrebase.initialize_app(config)
# 데이터베이스 인스턴스 생성
db = firebase.database()

def get_index_data() -> dict:
    videos = db.child('videos').get()
    videos_list = videos.val()

    return videos_list

if __name__ == '__main__':
    videos = db.child('videos').get()
    videos_list = videos.val()
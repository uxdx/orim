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
    video_list= dict()
    video = {
        "url" : "https://asd",
        "thumbnail" : "https:/asdfasdf",
    }
    for i in range(2):
        key = str(i)
        video_list[key] = video

    return video_list
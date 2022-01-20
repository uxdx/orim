from datetime import datetime
import datetime
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

def upload_video(title:str,uploadDate:datetime.datetime,url:str,thumbnail:str, like:int,view:int, category:str, channel_name:str):
    db.child('videos').push({
        'title':title,
        'uploadDate': uploadDate.__str__(),
        'url':url,
        'thumbnail': thumbnail,
        'like': like,
        'view': view,
        'category': category,
        'channel_name': channel_name
    })

def upload_video_from_dict(dic:dict):
    upload_video(dic['title'], dic['uploadDate'], dic['url'], dic['thumbnail'], dic['like'], dic['view'], dic['category'], dic['channel_name'])


if __name__ == '__main__':
    # upload_video_from_dict(sample_video)
    pass
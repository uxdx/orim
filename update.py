from datetime import datetime
import datetime
import pyrebase
import json

from secret_manager import access_secret

# secrets 로딩
config = access_secret()
# 파이어베이스 인스턴스 생성
firebase = pyrebase.initialize_app(config)
# 데이터베이스 인스턴스 생성
db = firebase.database()

def get_index_data() -> dict:
    videos = db.child('video').get()
    videos_list = videos.val()
    return videos_list

def update_data():
    key_list=['like','view']
    category=['Gaming','Music','Sports']
    data=get_index_data()
    for CTGR in category:
        for i in data[CTGR]:
            Information = youtube.videos().list(
                part='statistics',
                id=f'{i}',
            ).execute()
            response=[]
            if Information['items'][0]['statistics'].get('likeCount'):
                response.append(Information['items'][0]['statistics']['likeCount'])
            else:
                response.append("NULL")
            response.append(Information['items'][0]['statistics']['viewCount'])
            result=dict(zip(key_list,response))
            update_video_from_dict(result,CTGR,i)



def update_video(like:int, view:int, CTGR:str, videoId:str):
    db.child('video').child(CTGR).child(videoId).update({
        'like': like,
        'view': view,
    })

def update_video_from_dict(dic:dict, CTGR:str, videoId:str):
    update_video(dic['like'], dic['view'], CTGR, videoId)

if __name__ == '__main__':
    pass
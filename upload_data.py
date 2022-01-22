from datetime import datetime, timedelta
import datetime
import pyrebase
import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from secret_manager import access_secret

# secrets 로딩
config = access_secret()
# 파이어베이스 인스턴스 생성
firebase = pyrebase.initialize_app(config)
# 데이터베이스 인스턴스 생성
db = firebase.database()

#api 받아오기
DEVELOPER_KEY = ""
YOUTUBE_API_SERVICE_NAME="youtube"
YOUTUBE_API_VERSION="v3"
youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

def mostPopular():
    #카테고리 추가할 때 수정 필요
    category=[10, 17, 20]
    maxResults=5
    key_list=['title','uploadDate','videoId','url','thumbnail','like','view','category','channel_name','Ranking']
    result=[]

    for CTGR in category:
        Information = youtube.videos().list(
            part='snippet, statistics',
            chart='mostPopular',
            videoCategoryId=f'{CTGR}',
            regionCode='KR',
            maxResults=f'{maxResults}',
            ).execute()
        for i in range(maxResults):
            response=[]
            response.append(Information['items'][i]['snippet']['title'])
            time=Information['items'][i]['snippet']['publishedAt']
            time = time.replace("T"," ")
            time = time.replace("Z","")
            time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S') - timedelta(hours=-9)
            response.append(time)
            videoid=Information['items'][i]['id']
            response.append(videoid)
            response.append(f"https://www.youtube.com/embed/{videoid}")
            response.append(Information['items'][i]['snippet']['thumbnails']['medium']['url'])
            if Information['items'][i]['statistics'].get('likeCount'):
                response.append(Information['items'][i]['statistics']['likeCount'])
            else:
                response.append("NULL")
            response.append(Information['items'][i]['statistics']['viewCount'])
            #카테고리 추가할 때 수정 필요
            if CTGR==10:
                response.append('Music')
            elif CTGR==17:
                response.append('Sports')
            else:
                response.append('Gaming')
            response.append(Information['items'][i]['snippet']['channelTitle'])
            response.append(i+1)
            result.append(dict(zip(key_list,response)))
    return result

#메인 페이지 db
def upload_main_video(title:str, uploadDate:datetime.datetime ,videoId:str,url:str,thumbnail:str, like:int,view:int, category:str, channel_name:str,Ranking:int):
    db.child('mostPopular').child(category).child(Ranking).update({
        'title':title,
        'uploadDate': uploadDate.__str__(),
        'url':url,
        'thumbnail': thumbnail,
        'like': like,
        'view': view,
        'category': category,
        'channel_name': channel_name,
        'videoId': videoId
    })

#전체 db
def upload_video(title:str, uploadDate:datetime.datetime ,videoId:str,url:str,thumbnail:str, like:int,view:int, category:str, channel_name:str,Ranking:int):
    db.child('video').child(category).child(videoId).update({
        'title':title,
        'uploadDate': uploadDate.__str__(),
        'url':url,
        'thumbnail': thumbnail,
        'like': like,
        'view': view,
        'category': category,
        'channel_name': channel_name,
        'videoId': videoId
    })

def upload_video_from_dict(dic:dict):
    upload_main_video(dic['title'], dic['uploadDate'],dic['videoId'], dic['url'], dic['thumbnail'], dic['like'], dic['view'], dic['category'], dic['channel_name'],dic['Ranking'])
    upload_video(dic['title'], dic['uploadDate'],dic['videoId'], dic['url'], dic['thumbnail'], dic['like'], dic['view'], dic['category'], dic['channel_name'],dic['Ranking'])

def action():
    data=mostPopular()
    for i in data:
        upload_video_from_dict(i)

if __name__ == '__main__':
    # upload_video_from_dict(sample_video)
    pass
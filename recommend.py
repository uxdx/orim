from itertools import count
import pyrebase
import datetime
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime, timedelta
import datetime
import json
from upload_data import channel
from search import videoid_group
from upload_data import channel

with open("secrets.json") as jsonFile:
    secrets = json.load(jsonFile)
    jsonFile.close()
config = secrets['FIREBASE_CONFIG']
firebase = pyrebase.initialize_app(config)
db = firebase.database()

DEVELOPER_KEY = secrets['API_KEY']
YOUTUBE_API_SERVICE_NAME="youtube"
YOUTUBE_API_VERSION="v3"
youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

with open("category.json") as jsonFile:
    all_category = json.load(jsonFile)
    jsonFile.close()
category_dict=all_category['category']

def recommend(videoid:str, userid:str):
    time_data=datetime.datetime.now()
    time=time_data.strftime('%Y-%m-%d %H:%M:%S')
    amount=0
    db.child('recommend').child(videoid).update({
        userid:time
    })
    data=db.child('recommend').child(videoid).get()
    for i in data.val():
        if datetime.datetime.strptime(data.val()[i], '%Y-%m-%d %H:%M:%S')>=datetime.datetime.now()-timedelta(hours=-24):
            amount+=1
        else:
            db.child('recommend').child(videoid).child(i).remove()
    if amount>=5:
        Information = youtube.videos().list(
            part='snippet',
            id=videoid
            ).execute()
        publishedAt=Information['items'][i]['snippet']['publishedAt']
        publishedAt = publishedAt.replace("T"," ")
        publishedAt = publishedAt.replace("Z","")
        publishedAt = datetime.datetime.strptime(publishedAt, '%Y-%m-%d %H:%M:%S') - timedelta(hours=-9)
        channelId=Information['items'][0]['snippet']['channelId']
        categoryId=Information['items'][0]['snippet']['categoryId']
        db.child('video').child(videoid).update({
            'title':Information['items'][0]['snippet']['title'],
            'uploadDate': publishedAt.__str__(),
            'url':f'https://www.youtube.com/embed/{videoid}',
            'thumbnail': Information['items'][0]['snippet']['thumbnails']['high'],
            'category': category_dict[categoryId],
            # 카테고리 정보 가져와야 겠네
            'channel_name': Information['items'][0]['snippet']['channelTitle'],
            'videoId': videoid,
            'channelId': Information['items'][0]['snippet']['channelId'],
            'channelurl':f'https://www.youtube.com/channel/{channelId}',
            'Img_channel':channel(channelId)
        })


# 유튜브 api 검색 O/X는 db에 영상 유무
def youtube_search(keyword:str):
    Information = youtube.search().list(
    part='snippet',
    type='video',
    regionCode='KR',
    maxResults=5,
    q=f'{keyword}'
    ).execute()
    key_list=['title','uploadDate','videoId','thumbnail','channel_name','channelId','Img_channel','O/X']
    result=[]
    for i in range(5):
        response=[]
        response.append(Information['items'][i]['snippet']['title'])
        time=Information['items'][i]['snippet']['publishedAt']
        time = time.replace("T"," ")
        time = time.replace("Z","")
        time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S') - timedelta(hours=-9)
        response.append(time)
        videoid=Information['items'][i]['id']['videoId']
        response.append(videoid)
        response.append(Information['items'][i]['snippet']['thumbnails']['high']['url'])
        response.append(Information['items'][i]['snippet']['channelTitle'])
        response.append(Information['items'][i]['snippet']['channelId'])
        channelID=Information['items'][i]['snippet']['channelId']
        response.append(channel(channelID))
        if videoid_group(videoid):
            response.append('O')
        else:
            response.append('X')
        result.append(dict(zip(key_list,response)))
    return result
from itertools import count
import pyrebase
import datetime
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime, timedelta
import datetime
import json
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

def recommend(videoid:str):
    db.child('recommend').child('videoid').child().update({
    })

def youtube_search(keyword:str):
    Information = youtube.search().list(
    part='snippet',
    type='video',
    regionCode='KR',
    maxResults=5,
    q=f'{keyword}'
    ).execute()
    key_list=['title','uploadDate','videoId','thumbnail','channel_name','channelId','Img_channel']
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
        result.append(dict(zip(key_list,response)))
    return result
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime, timedelta
import datetime
import json
from initialize_firebase import ref_like, ref_mostPopular, ref_recommend, ref_User, ref_video

with open("secrets.json") as jsonFile:
    secrets = json.load(jsonFile)
    jsonFile.close()

DEVELOPER_KEY = secrets['API_KEY']
YOUTUBE_API_SERVICE_NAME="youtube"
YOUTUBE_API_VERSION="v3"
youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

with open("category.json") as jsonFile:
    all_category = json.load(jsonFile)
    jsonFile.close()
category_dict=all_category['category']

def mostPopular():
    maxResults=5
    key_list=['title','uploadDate','videoId','url','thumbnail','category','channel_name','Ranking','channelId','channelurl','Img_channel']
    result=[]
    rank=['A','B','C','D','E']

    for CTGR in category:
        Information = youtube.videos().list(
            part='snippet',
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
            response.append(Information['items'][i]['snippet']['thumbnails']['high']['url'])
            response.append(category_dict[Information['items'][i]['snippet']['categoryId']])
            response.append(Information['items'][i]['snippet']['channelTitle'])
            response.append(f"{CTGR}"+rank[i])
            response.append(Information['items'][i]['snippet']['channelId'])
            channelID=Information['items'][i]['snippet']['channelId']
            response.append(f'https://www.youtube.com/channel/{channelID}')
            response.append(channel(channelID))
            result.append(dict(zip(key_list,response)))
    return result

#메인 페이지 db
def upload_main_video(title:str, uploadDate:datetime.datetime ,videoId:str,url:str,thumbnail:str,category:str, channel_name:str,Ranking:int,channelId:str,channelurl:str,Img_channel:str):
    ref_mostPopular.child(category).child(Ranking).update({
        'title':title,
        'uploadDate': uploadDate.__str__(),
        'url':url,
        'thumbnail': thumbnail,
        'category': category,
        'channel_name': channel_name,
        'videoId': videoId,
        'channelId': channelId,
        'channelurl':channelurl,
        'Img_channel':Img_channel
    })

#전체 db
def upload_video(title:str, uploadDate:datetime.datetime ,videoId:str,url:str,thumbnail:str, category:str, channel_name:str, Ranking:int, channelId:str,channelurl:str,Img_channel:str):
    ref_video.child(videoId).update({
        'title':title,
        'uploadDate': uploadDate.__str__(),
        'url':url,
        'thumbnail': thumbnail,
        'category': category,
        'channel_name': channel_name,
        'videoId': videoId,
        'channelId': channelId,
        'channelurl':channelurl,
        'Img_channel':Img_channel
    })

def upload_video_from_dict(dic:dict):
    upload_main_video(dic['title'], dic['uploadDate'],dic['videoId'], dic['url'], dic['thumbnail'], dic['category'], dic['channel_name'], dic['Ranking'], dic['channelId'],dic['channelurl'],dic['Img_channel'])
    upload_video(dic['title'], dic['uploadDate'],dic['videoId'], dic['url'], dic['thumbnail'], dic['category'], dic['channel_name'], dic['Ranking'], dic['channelId'],dic['channelurl'],dic['Img_channel'])

def action():
    data=mostPopular()
    for i in data:
        upload_video_from_dict(i)

def channel(channelID:str):
    Information = youtube.channels().list(
                part='snippet',
                id =f'{channelID}'
                ).execute()
    channelurl=Information['items'][0]['snippet']['thumbnails']['default']['url']
    return channelurl


if __name__ == '__main__':
    pass
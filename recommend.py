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

# 스포츠 게임 음악 이외의 카테고리 올라오는 경우 생길수 있다.
with open("category.json") as jsonFile:
    all_category = json.load(jsonFile)
    jsonFile.close()
category_dict=all_category['category']

def videoid_group(videoid:str):
    snapshot = ref_video.order_by_child('videoId').equal_to(videoid).get()
    videoid_video=[]
    for val in snapshot.values():
        videoid_video.append(val)
    return videoid_video

# 추천하기 눌렸을때 추천 정보 저장, 24시간 이내 추천 정보가 5개 넘어갈 경우 db에 동영상 정보 저장
def recommend(videoid:str, userid:str):
    time_data=datetime.datetime.now()
    time=time_data.strftime('%Y-%m-%d %H:%M:%S')
    amount=0
    ref_recommend.child(videoid).update({
        userid:time
    })
    data=ref_recommend.child(videoid).get()
    for i in data:
        if datetime.datetime.strptime(data[i], '%Y-%m-%d %H:%M:%S')>=datetime.datetime.now()+timedelta(hours=-24):
            amount+=1
        else:
            ref_recommend.child(videoid).child(i).delete()
    if amount>=5:
        Information = youtube.videos().list(
            part='snippet',
            id=videoid
            ).execute()
        publishedAt=Information['items'][0]['snippet']['publishedAt']
        publishedAt = publishedAt.replace("T"," ")
        publishedAt = publishedAt.replace("Z","")
        publishedAt = datetime.datetime.strptime(publishedAt, '%Y-%m-%d %H:%M:%S') - timedelta(hours=-9)
        channelId=Information['items'][0]['snippet']['channelId']
        categoryId=Information['items'][0]['snippet']['categoryId']
        ref_video.child(videoid).update({
            'title':Information['items'][0]['snippet']['title'],
            'uploadDate': publishedAt.__str__(),
            'url':f'https://www.youtube.com/embed/{videoid}',
            'thumbnail': Information['items'][0]['snippet']['thumbnails']['high']['url'],
            'category': category_dict[categoryId],
            'channel_name': Information['items'][0]['snippet']['channelTitle'],
            'videoId': videoid,
            'channelId': Information['items'][0]['snippet']['channelId'],
            'channelurl':f'https://www.youtube.com/channel/{channelId}',
            'Img_channel':channel(channelId)
        })


# 유튜브 api 검색 O/X는 db에 영상 유무
# 유튜브에서 검색해서 추천하기
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

def channel(channelID:str):
    Information = youtube.channels().list(
                part='snippet',
                id =f'{channelID}'
                ).execute()
    channelurl=Information['items'][0]['snippet']['thumbnails']['default']['url']
    return channelurl
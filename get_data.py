import pyrebase
import json
from search import Recently_category_group, Recently_channel_group
from search_al import search_title, search_channel_name

with open("secrets.json") as jsonFile:
    secrets = json.load(jsonFile)
    jsonFile.close()
config = secrets['FIREBASE_CONFIG']
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# 메인 페이지용 함수
def get_index_data() -> dict:
    videos_Gaming = db.child('mostPopular').child('Gaming').get()
    videos_list = videos_Gaming.val()
    videos_Music = db.child('mostPopular').child('Music').get()
    videos_list2 = videos_Music.val()
    videos_Sports = db.child('mostPopular').child('Sports').get()
    videos_list3 = videos_Sports.val()
    videos_list.update(videos_list2)
    videos_list.update(videos_list3)
    return videos_list

# key 입력 받아서 영상 가져오는 함수
def get_video_by_vid(key:str=None):
    if key==None:
        video_list=[]
    else:
        data = db.child('video').child(key).get()
        video_list=data.val()
    return video_list

# 카테고리 모아보기 정확한 입력 필요 최근 업로드 순
def get_videos_by_category(category:str=None):
    if category==None:
        video_list=[]
    else:
        video_list=Recently_category_group(category)
    return video_list

# 채널 모아보기 정확한 입력 필요 최근 업로드 순
def get_videos_by_channel_name(channel:str=None):
    if channel==None:
        video_list=[]
    else:
        video_list=Recently_channel_group(channel)
    return video_list

# 검색어 입력 필요(데이터베이스에서 검색)
def get_videos_by_search_title(pattern:str=None):
    if pattern==None:
        video_list=[]
    else:
        video_list=search_title(pattern)
    return video_list

def get_videos_by_search_channel_name(pattern:str=None):
    if pattern==None:
        video_list=[]
    else:
        video_list=search_channel_name(pattern)
    return video_list

# if __name__ == '__main__':
#     print(get_index_data())

print(get_video_by_vid('lrzISkKt2wI'))
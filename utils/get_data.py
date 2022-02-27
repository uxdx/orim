import pyrebase

from utils.secret_manager import access_secret
from utils.search_al import search_title,search_channel_name

# secrets.json 로딩
config = access_secret('FIREBASE_CONFIG')
# 파이어베이스 인스턴스 생성
firebase = pyrebase.initialize_app(config)
# 데이터베이스 인스턴스 생성
db = firebase.database()

def get_index_videos():
    videos_Gaming=[]
    videos_Music=[]
    videos_Gaming=[]
    videos_Gaming = db.child('mostPopular').child('Gaming').get()
    videos_list = list(videos_Gaming.val().values())
    videos_Music = db.child('mostPopular').child('Music').get()
    videos_list2 = list(videos_Music.val().values())
    videos_Sports = db.child('mostPopular').child('Sports').get()
    videos_list3 = list(videos_Sports.val().values())
    
    return videos_list,videos_list2,videos_list3

def get_video_by_vid(key:str=None) -> dict:
    if key==None:
        video_list=[]
    else:
        data = db.child('video').child(key).get()
        video_list=data.val()
    return video_list

def get_videos_by_search_as_keyword(keyword:str) -> dict:
    """keyword를 통한 검색결과를 출력

    Parameters
    ----------
    keyword : str
        제목, 채널명 등

    Returns
    -------
    dict
        검색결과에 해당하는 2차원 dict
    """

    return dict()
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

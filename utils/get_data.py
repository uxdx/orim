import pyrebase

from utils.secret_manager import access_secret

# secrets.json 로딩
config = access_secret('FIREBASE_CONFIG')
# 파이어베이스 인스턴스 생성
firebase = pyrebase.initialize_app(config)
# 데이터베이스 인스턴스 생성
db = firebase.database()

def get_home_videos() -> dict:
    videos_Gaming = db.child('mostPopular').child('Gaming').get()
    videos_list = videos_Gaming.val()
    videos_Music = db.child('mostPopular').child('Music').get()
    videos_list2 = videos_Music.val()
    videos_Sports = db.child('mostPopular').child('Sports').get()
    videos_list3 = videos_Sports.val()
    videos_list.update(videos_list2)
    videos_list.update(videos_list3)
    return videos_list

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


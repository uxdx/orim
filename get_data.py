import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

with open("secrets.json") as jsonFile:
    secrets = json.load(jsonFile)
    jsonFile.close()

cred = credentials.Certificate(secrets['FIREBASE_ADMIN_CONFIG'])

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://jinho-337705-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# 메인 페이지용 함수
def get_index_data() -> dict:
    ref = db.reference('mostPopular')
    videos_Gaming = ref.child('Gaming').get()
    videos_Music = ref.child('Music').get()
    videos_Sports = ref.child('Sports').get()
    videos_list={'Gaming':videos_Gaming,'Music':videos_Music,'Sports':videos_Sports}
    return videos_list

# key 입력 받아서 영상 가져오는 함수
def get_video_by_vid(key:str=None):
    if key==None:
        video_list={}
    else:
        ref = db.reference('video')
        video_list=ref.child(key).get()
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

# 카테고리 영상 불러오기
def category_group(category:str):
    ref = db.reference('video')
    snapshot = ref.order_by_child('category').equal_to(category).get()
    category_video=[]
    for val in snapshot.values():
        category_video.append(val)
    return category_video

# 채널 영상 불러오기
def channel_group(channel:str):
    ref = db.reference('video')
    snapshot = ref.order_by_child('channel_name').equal_to(channel).get()
    channel_video=[]
    for val in snapshot.values():
        channel_video.append(val)
    return channel_video

# ex)제목으로 
# def title_group(title:str):
#     ref = db.reference('video')
#     snapshot = ref.order_by_child('title').equal_to(title).get()
#     title_video=[]
#     for val in snapshot.values():
#         title_video.append(val)
#     return title_video

def videoid_group(videoid:str):
    ref = db.reference('video')
    snapshot = ref.order_by_child('videoId').equal_to(videoid).get()
    videoid_video=[]
    for val in snapshot.values():
        videoid_video.append(val)
    return videoid_video

# 업로드 날짜 선->후
def Recently_uploadDate(videolist:list):
    a=dict()
    j=0
    for i in videolist:
        a[i['uploadDate']]=j
        j+=1
    b=sorted(a.items(),reverse=True)
    c=[]
    for i in b:
        c.append(i[1])
    d=[]
    for i in c:
        d.append(videolist[i])
    return d

# 업로드 날짜 후->선
def old_uploadDate(videolist:list):
    a=dict()
    j=0
    for i in videolist:
        a[i['uploadDate']]=j
        j+=1
    b=sorted(a.items(),reverse=False)
    c=[]
    for i in b:
        c.append(i[1])
    d=[]
    for i in c:
        d.append(videolist[i])
    return d

def Recently_category_group(category):
    data=category_group(category)
    video=Recently_uploadDate(data)
    return video

def Recently_channel_group(channel):
    data=channel_group(channel)
    video=Recently_uploadDate(data)
    return video

# 검색 알고리즘
def boyer_moore(pattern, text):
    M = len(pattern)
    N = len(text)
    i = 0
    while i <= N-M:
        j = M - 1
        while j >= 0:
            if pattern[j] != text[i+j]:
               move = find(pattern, text[i + M - 1])
               break
            j = j - 1
        if j == -1:
            return True
        else:
            i += move
    return False

def find(pattern, char):
    for i in range(len(pattern)-2, -1, -1):
        if pattern[i] == char:
            return len(pattern) -i -1
    return len(pattern)

# 검색 기능
def get_search_data():
    ref=db.reference('video')
    videos_list = ref.get()
    return videos_list

def search_title(pattern:str):
    data_dict=get_search_data()
    data_list=list(data_dict.values())
    search_result=[]
    for i in data_list:
        text=i['title']
        if boyer_moore(pattern, text):
            search_result.append(i)
    return search_result

def search_channel_name(pattern:str):
    data_dict=get_search_data()
    data_list=list(data_dict.values())
    search_result=[]
    for i in data_list:
        text=i['channel_name']
        if boyer_moore(pattern, text):
            search_result.append(i)
    return search_result

if __name__ == '__main__':
    print(get_index_data())
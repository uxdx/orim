from initialize_firebase import ref_like, ref_mostPopular, ref_recommend, ref_User, ref_video

# 메인 페이지용 함수
def get_index_data() -> dict:
    videos_Gaming = ref_mostPopular.child('Gaming').get()
    list_Gaming=videos_Gaming.values()
    for i in list_Gaming:
        i['uploadDate']=i['uploadDate'][0:10]
    videos_Music = ref_mostPopular.child('Music').get()
    list_Music=videos_Music.values()
    for i in list_Music:
        i['uploadDate']=i['uploadDate'][0:10]
    videos_Sports = ref_mostPopular.child('Sports').get()
    list_Sports=videos_Sports.values()
    for i in list_Sports:
        i['uploadDate']=i['uploadDate'][0:10]
    return list_Gaming, list_Music, list_Sports

# key 입력 받아서 영상 가져오는 함수
def get_video_by_vid(key:str=None):
    if key==None:
        video_list={}
    else:
        video_list=ref_video.child(key).get()
    return video_list

# 카테고리 모아보기 정확한 입력 필요 최근 업로드 순
def get_videos_by_category(category:str=None):
    if category==None:
        video_list=[]
    else:
        video_list=Recently_category_group(category)
        for i in video_list:
            i['uploadDate']=i['uploadDate'][0:10]
    return video_list

# 채널 모아보기 정확한 입력 필요 최근 업로드 순
def get_videos_by_channel_name(channel:str=None):
    if channel==None:
        video_list=[]
    else:
        video_list=Recently_channel_group(channel)
        for i in video_list:
            i['uploadDate']=i['uploadDate'][0:10]
    return video_list

# 검색어 입력 필요(데이터베이스에서 검색)
def get_videos_by_search_title(pattern:str=None):
    if pattern==None:
        video_list=[]
    else:
        video_list=search_title(pattern)
        for i in video_list:
            i['uploadDate']=i['uploadDate'][0:10]
    return video_list

def get_videos_by_search_channel_name(pattern:str=None):
    if pattern==None:
        video_list=[]
    else:
        video_list=search_channel_name(pattern)
        for i in video_list:
            i['uploadDate']=i['uploadDate'][0:10]
    return video_list

# 카테고리 영상 불러오기
def category_group(category:str):
    snapshot = ref_video.order_by_child('category').equal_to(category).get()
    category_video=[]
    for val in snapshot.values():
        category_video.append(val)
    for i in category_video:
        i['uploadDate']=i['uploadDate'][0:10]
    return category_video

# 채널 영상 불러오기
def channel_group(channel:str):
    snapshot = ref_video.order_by_child('channel_name').equal_to(channel).get()
    channel_video=[]
    for val in snapshot.values():
        channel_video.append(val)
    for i in channel_video:
        i['uploadDate']=i['uploadDate'][0:10]
    return channel_video

def videoid_group(videoid:str):
    snapshot = ref_video.order_by_child('videoId').equal_to(videoid).get()
    videoid_video=[]
    for val in snapshot.values():
        videoid_video.append(val)
    for i in videoid_video:
        i['uploadDate']=i['uploadDate'][0:10]
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
    videos_list = ref_video.get()
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
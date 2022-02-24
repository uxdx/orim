import json
from initialize_firebase import ref_like, ref_mostPopular, ref_recommend, ref_User, ref_video

# 좋아요 누를 때
def like_count(userid:str, videoid:str):
    ref_like.child('user').child(userid).update({
        videoid:1
    })
    ref_like.child('video').child(videoid).update({
        userid:1
    })

# video에 좋아요 누른 사람 숫자
# 유튜브 좋아요 x
def get_like_video(videoid:str):
    like = ref_like.child('video').child(videoid).get()
    like_count=len(like)
    return like_count

# user가 누른 좋아요 동영상
def get_like_user(userid:str):
    like = ref_like.child('user').child(userid).get()
    like_video=[]
    for i in like:
        like_video.append(i)
    return like_video

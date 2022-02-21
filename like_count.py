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

ref_like=db.reference('like')

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

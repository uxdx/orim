from itertools import count
import pyrebase
import datetime
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime, timedelta
import datetime
import json

with open("secrets.json") as jsonFile:
    secrets = json.load(jsonFile)
    jsonFile.close()
config = secrets['FIREBASE_CONFIG']
firebase = pyrebase.initialize_app(config)
db = firebase.database()

def like_count(userid:str, videoid:str):
    db.child('like').child('user').child(userid).update({
        videoid:1
    })
    db.child('like').child('video').child(videoid).update({
        userid:1
    })

def get_like_video(videoid:str):
    like = db.child('like').child('video').child(videoid).get()
    like_dic = like.val()
    like_count=0
    for i in like_dic:
        like_count+=1
    return like_count

def get_like_user(userid:str):
    like = db.child('like').child('user').child(userid).get()
    like_dic = like.val()
    like_video=[]
    for i in like_dic:
        like_video.append(i)
    return like_video

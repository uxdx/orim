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
ref_video=db.reference('video')
ref_User=db.reference('User')
ref_mostPopular=db.reference('mostPopular')
ref_recommend=db.reference('recommend')
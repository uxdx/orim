import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
from get_data import get_key_data

with open("secrets.json") as jsonFile:
    secrets = json.load(jsonFile)
    jsonFile.close()

cred = credentials.Certificate(secrets['FIREBASE_ADMIN_CONFIG'])

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://jinho-337705-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference('video')
# snapshot = ref.order_by_child('category').equal_to('Music').get()
# for key in snapshot:
#     print(key)

def category_group(category:str):
    snapshot = ref.order_by_child('category').equal_to(category).get()
    for key in snapshot:
        print(key)
    category_video=[]
    for key in snapshot:
        category_video.append(get_key_data(key))
    return category_video

def channel_group(channel:str):
    snapshot = ref.order_by_child('channel_name').equal_to(channel).get()
    for key in snapshot:
        print(key)
    category_video=[]
    for key in snapshot:
        category_video.append(get_key_data(key))
    return category_video
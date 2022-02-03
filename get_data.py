import pyrebase
import json

with open("secrets.json") as jsonFile:
    secrets = json.load(jsonFile)
    jsonFile.close()
config = secrets['FIREBASE_CONFIG']
firebase = pyrebase.initialize_app(config)
db = firebase.database()


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

def get_key_data(key:str) -> dict:
    data = db.child('video').child(key).get()
    video_list=data.val()
    return video_list


if __name__ == '__main__':
    print(get_index_data())

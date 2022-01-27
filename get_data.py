import os
import pyrebase

# secrets.json 로딩
config = os.environ.get('FIREBASE_CONFIG')
# 파이어베이스 인스턴스 생성
firebase = pyrebase.initialize_app(config)
# 데이터베이스 인스턴스 생성
db = firebase.database()

def get_index_data() -> dict:
    videos = db.child('video').child('Gaming').get()
    videos_list = videos.val()
    return videos_list

if __name__ == '__main__':
    print(get_index_data())

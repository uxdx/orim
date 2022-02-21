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

# 유저 정보 저장 수정 가능
def save_User_data(UserID:str, E_mail:str, Nickname:str, OX:str):
    ref = db.reference('User')
    ref.child(UserID).update({
        'UserID':UserID,
        'e-mail':E_mail,
        'Nickname':Nickname,
        'OX':OX
    })

# save_User('UserID','e-mail','Nickname','O')

# 유저 정보 불러오기
def get_User_data(UserID):
    ref = db.reference('User')
    User_data=ref.child(UserID).get()
    return User_data

# a=get_User_data('UserID')
# print(a)
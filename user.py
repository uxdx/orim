from initialize_firebase import ref_like, ref_mostPopular, ref_recommend, ref_User, ref_video

# 유저 정보 저장 수정 가능
def save_User_data(uid:str ,registered_date:str, email:str, name:str, email_verified:bool):
    ref_User.child(uid).update({
        'uid':uid,
        'email':email,
        'name':name,
        'email_verified':email_verified,
        'registered_date':registered_date
    })

# 유저 정보 불러오기
def get_User_data(uid:str):
    User_data=ref_User.child(uid).get()
    return User_data

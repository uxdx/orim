from firebase_admin import db
import pyrebase
import json

with open("secrets.json") as jsonFile:
    secrets = json.load(jsonFile)
    jsonFile.close()
config = secrets['config']
firebase = pyrebase.initialize_app(config)

ref =db.reference('https://jinho-337705-default-rtdb.asia-southeast1.firebasedatabase.app/')
print(ref.get())
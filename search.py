import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

with open("secrets.json") as jsonFile:
    secrets = json.load(jsonFile)
    jsonFile.close()


# Fetch the service account key JSON file contents
cred = credentials.Certificate(secrets['FIREBASE_ADMIN_CONFIG'])

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://jinho-337705-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('video')
snapshot = ref.order_by_key().get()
print(snapshot)
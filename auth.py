#Imports
import firebase_admin
import pyrebase
from firebase_admin import credentials, auth
from flask import Flask, request

from secret_manager import access_secret

#Connect to firebase
cred = credentials.Certificate(access_secret("FIREBASE_ADMIN"))
firebase = firebase_admin.initialize_app(cred)
pb = pyrebase.initialize_app(access_secret())

def register():
    auth.create_user()


if __name__ == "__main__":
    pass
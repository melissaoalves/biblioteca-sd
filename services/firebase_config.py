import firebase_admin
from firebase_admin import credentials, firestore, auth
from dotenv import load_dotenv
import os

cred = credentials.Certificate("services/firebase_credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

load_dotenv() 
config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": "",
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
}


import pyrebase
from dotenv import load_dotenv
import os

load_dotenv()

firebase_config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

def login_usuario(email, senha):
    try:
        user = auth.sign_in_with_email_and_password(email, senha)
        return True, "Login realizado com sucesso!"
    except Exception as e:
        return False, "Erro no login: Verifique seu e-mail e senha."

def registrar_usuario(email, senha):
    try:
        auth.create_user_with_email_and_password(email, senha)
        return True, "Usuário registrado com sucesso!"
    except Exception as e:
        return False, "Erro no registro: " + str(e)

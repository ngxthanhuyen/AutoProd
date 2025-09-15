from flask import Flask
from flask_mail import Mail
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

# Chargement des variables d'environnement depuis le fichier .env
load_dotenv()

# Classe singleton pour initialiser une seule fois l'app, mongo et mail
class ConfigSingleton:
    _instance = None

    def __init__(self):
        # Empêche l'instanciation directe de la classe
        raise RuntimeError("Utilisez instance()")

    @classmethod
    def instance(cls):
        # Vérifie si une instance existe déjà
        if cls._instance is None:
            # Création de l'application Flask
            app = Flask(__name__)
            # Configuration MongoDB
            mongo_host = os.getenv('MONGO_HOST', 'localhost')
            app.config['MONGO_URI'] = f"mongodb://{mongo_host}:27017/imageDB"
            # Configuration SMTP pour l'envoi d'e-mails
            app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
            app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
            app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
            app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
            app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
            app.config['MAIL_USE_TLS'] = False
            app.config['MAIL_USE_SSL'] = False

            # Enregistrement des objets nécessaires dans le singleton 
            cls._instance = {
                "app": app,
                "mongo": PyMongo(app),
                "mail": Mail(app)
            }
        # Retourne l'instance unique
        return cls._instance
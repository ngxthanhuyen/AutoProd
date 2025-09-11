import os 
class Config:
    MONGO_URI = os.environ.get("MONGO_URI", "mongodb://127.0.0.1:27017/image_db")

    # Configuration pour hMailServer local
    MAIL_SERVER = 'localhost'             # hMailServer local
    MAIL_PORT = 25                        # ou 587 si configuré
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'ed@monmail.com'    
    MAIL_PASSWORD = 'changeme'       
    MAIL_DEFAULT_SENDER = 'ed@monmail.com'

import os
from redmail import gmail

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    TEMPLATES_FOLDER = 'templates'
    DEBUG = False

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/emotion_dive'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    EMAIL_HOST = gmail.host
    EMAIL_PORT = gmail.port
    EMAIL_USERNAME = "emotiondive2022@gmail.com"
    EMAIL_PASSWORD = "etibcgyoykbklaio"

class TestConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/emotion_dive'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    EMAIL_HOST = gmail.host
    EMAIL_PORT = gmail.port
    EMAIL_USERNAME = "emotiondive2022@gmail.com"
    EMAIL_PASSWORD = "etibcgyoykbklaio"

class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/emotion_dive'
    EMAIL_HOST = gmail.host
    EMAIL_PORT = gmail.port
    EMAIL_USERNAME = "emotiondive2022@gmail.com"
    EMAIL_PASSWORD = "etibcgyoykbklaio"



config_by_name = dict(
    dev=DevConfig,
    test=TestConfig,
    prod=ProdConfig
)

key = Config.SECRET_KEY
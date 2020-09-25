# personal email account and db secrets not in repo
from flaskblog.config_secrets import Secrets


class Config:
    SECRET_KEY = Secrets.secret_key
    SQLALCHEMY_DATABASE_URI = Secrets.sqalchemy_database_uri
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = Secrets.username
    MAIL_PASSWORD = Secrets.password

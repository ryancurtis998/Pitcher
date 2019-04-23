import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ryan:12345@localhost/pitcher'

    MAIL_SERVER = 'smtp.googlemail.com'

    MAIL_PORT =   587

    MAIL_USE_TLS = True

    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")

    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    pass

class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ryan:12345@localhost/pitcher'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'super-secret-key'

    SQLALCHEMY_DATABASE_URI = (
        'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'store.db')
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = 'super-secret-key'

    GOOGLE_CLIENT_ID = '673865342919-i1kb9q06nnl0lgheaqnp034istdfacin.apps.googleusercontent.com'

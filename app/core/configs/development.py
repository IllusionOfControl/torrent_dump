from app.core.configs.base import BaseAppConfig, DATA_DIR
import os


class DevAppConfig(BaseAppConfig):
    DEBUG = True
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(DATA_DIR, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TORRENT_UPLOAD_PATH = os.path.join(DATA_DIR, "torrents")

from app.core.configs.base import BaseAppConfig
from tempfile import mkdtemp


class TestAppConfig(BaseAppConfig):
    DEBUG = True
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TORRENT_UPLOAD_PATH = mkdtemp

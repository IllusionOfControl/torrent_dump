from typing import Dict, Type
from app.core.configs.base import BaseAppConfig
from app.core.configs.development import DevAppConfig
from app.core.configs.test import TestAppConfig
import os


basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


environments: Dict[str, Type[BaseAppConfig]] = {
    "dev": DevAppConfig,
    "test": TestAppConfig,
    # AppEnvTypes.dev: DevAppConfig,
}


def get_application_config(env):
    return environments[env]


class Config:
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "..", "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TORRENT_UPLOAD_PATH = os.path.join(basedir, "..", "torrents")

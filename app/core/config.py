from typing import Dict, Type
from app.core.configs.base import BaseAppConfig
from app.core.configs.development import DevAppConfig
from app.core.configs.test import TestAppConfig
from app.core.configs.prod import ProdAppConfig
import os


environments: Dict[str, Type[BaseAppConfig]] = {
    "dev": DevAppConfig,
    "test": TestAppConfig,
    "prod": ProdAppConfig
}


def get_app_env():
    env = os.environ.get("APP_ENV", None)
    return env if env in environments else "prod"


def get_application_config(env):
    return environments[env]

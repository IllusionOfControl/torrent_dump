from flask import Flask
from flask_migrate import Migrate
from app.database import database
from app.core.config import get_application_config
from app.views import upload, torrents


migrate = Migrate()


def get_application(env="dev") -> Flask:
    application = Flask(__name__)

    config = get_application_config(env)
    application.config.from_object(config)

    database.init_app(application)
    migrate.init_app(application, database)

    # database.create_all(app=application)

    application.register_blueprint(upload.blueprint)
    application.register_blueprint(torrents.blueprint)

    return application


app = get_application()

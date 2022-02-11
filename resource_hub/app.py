from flask import Flask
from flask_smorest import Api
from flask_cors import CORS

from resource_hub.resources.models import Resource
from resource_hub.config import DevelopmentConfig as Config
from resource_hub.settings import INSTALLED_BLUEPRINTS, db, migrate


def create_app(base_config=None):
    flask_app = Flask(__name__)
    if base_config:
        flask_app.config.from_object(base_config)

    CORS(flask_app)
    db.init_app(flask_app)
    migrate.init_app(flask_app, db)

    return flask_app


def create_api(flask_app):
    smorest_api = Api(flask_app)
    return smorest_api


def register_blueprints(flask_app, blueprints):
    for blueprint in blueprints:
        flask_app.register_blueprint(blueprint)


app = create_app(base_config=Config())
api = create_api(app)
register_blueprints(api, INSTALLED_BLUEPRINTS)


# Demo API Endpoints
@app.route('/')
def hello():
    return 'Hello World'


@app.route('/status')
def status():
    return {'status': 'healthy'}

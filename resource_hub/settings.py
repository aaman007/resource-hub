from pathlib import Path

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from resource_hub.dummy.views import blp as dummy_blueprint

BASE_DIR = Path(__file__).resolve().parent.parent
db = SQLAlchemy()
migrate = Migrate()

INSTALLED_BLUEPRINTS = [
    dummy_blueprint
]

from pathlib import Path
from resource_hub.dummy.views import blp as dummy_blueprint

BASE_DIR = Path(__file__).resolve().parent.parent


INSTALLED_BLUEPRINTS = [
    dummy_blueprint
]

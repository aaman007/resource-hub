from flask.views import MethodView
from flask_smorest import Blueprint

from resource_hub.dummy.schemas import DummySchema

blp = Blueprint(
    'dummy', __name__, url_prefix='/dummy'
)


@blp.route('/')
class ListCreateView(MethodView):
    @blp.response(200, DummySchema(many=True))
    def get(self):
        return []

    @blp.response(201, DummySchema)
    def post(self):
        return {}


@blp.route('/<int:pk>/')
class RetrieveUpdateDestroyView(MethodView):
    @blp.response(200, DummySchema)
    def get(self, pk):
        return {}

    @blp.response(200, DummySchema)
    def put(self, pk):
        return {}

    @blp.response(200, DummySchema)
    def patch(self, pk):
        return {}

    @blp.response(204)
    def delete(self, pk):
        return None

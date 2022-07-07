from flask import Blueprint
from flask_restplus import Api

from main.controller.search import search_ns
from main.controller.user import user_ns


blueprint = Blueprint("api", __name__)
api = Api(
    blueprint,
    title="Faze Clan Movie Finder - APIs",
    description="Faze Clan Movie Finder backend API Documentation"
)
api.add_namespace(search_ns, '/search')
api.add_namespace(user_ns, '/user')


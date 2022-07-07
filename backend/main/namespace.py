from flask_restplus import Namespace

search_ns = Namespace("search",description="All functions for search.")

user_ns = Namespace("user",description="All functions for authentication and user info.")

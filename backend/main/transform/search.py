from flask_restplus import fields

from main.namespace import search_ns

class SearchObject:
    search_request = search_ns.model(
        "search_request", 
        {
            'name': fields.String,
            'desc': fields.String,
            'genre': fields.String,
            'actor': fields.String,
            'director': fields.String,
            #'username': fields.String,
        }
    )

    filter_request = search_ns.model(
        "filter_request",
        {
            "search_request": fields.Nested(search_request),
            "genre_filter": fields.String,
            "actor_filter": fields.String,
            "director_filter": fields.String,
            "order_by": fields.String
        }
    )
    
    search_single_movie = search_ns.model(
        "search_single_movie", 
        {
            'id': fields.Integer,
            'name': fields.String,
            'image': fields.String,
            'description': fields.String,
            'genres': fields.String,
            'rating': fields.String,
            'director': fields.String,
            'actor': fields.String,
        }
    )
    
    filter_single = search_ns.model(
        "filter_single",
        {
            'category': fields.String,
            'name': fields.String,
            'count': fields.Integer,
        }
    )

    search_response = search_ns.model(
        "search_response",
        {
            'filter_list': fields.List(fields.Nested(filter_single)),
            'movie_list': fields.List(fields.Nested(search_single_movie)),
        }
    )

    filter_response = search_ns.model(
        "filter_response",
        {
            'movie_list': fields.List(fields.Nested(search_single_movie))
        }
    )

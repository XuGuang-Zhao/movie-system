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

    search_response = search_ns.model(
        "search_response",
        {
            'movie_list':fields.List(fields.Nested(search_single_movie)),
        }
    )

from flask_restplus import fields
from main.namespace import user_ns

class UserObject:
    msg_response = user_ns.model("msg_response", {
        'message': fields.String,
    })
    
    
    login_request = user_ns.model("login_request", {
        'username': fields.String,
        'password': fields.String,
    })
    
    register_request = user_ns.model("register_request", {
        'username': fields.String,
        'password': fields.String,
        'gender': fields.String,
        'email': fields.String,
    })
    
    user_info_response = user_ns.model("user_info_response", {
        'user_id': fields.Integer,
        'username': fields.String,
        'email': fields.String,
        'gender': fields.String,
    })
    
    reset_pwd_request = user_ns.model("reset_pw_request", {
        'username': fields.String,
        'old_pwd': fields.String,
        'new_pwd': fields.String,
    })
    
    # This is for debugging
    view_request = user_ns.model("view_request", {
        'username': fields.String,
    })
    user_details = user_ns.model("user_details", {
            'user_id': fields.Integer,
            'username': fields.String,
            'password': fields.String,
            'email': fields.String,
            'gender': fields.String,
        }
    )
    
    user_id = user_ns.model("user_id", {
        'user_id': fields.Integer,
    })
    
    movie_wish = user_ns.model("movie_wish", {
        'movie_id': fields.Integer,
        'name': fields.String,
        'image': fields.String,
    })
    
    movie_ban = user_ns.model("movie_ban", {
        'movie_id': fields.Integer,
        'name': fields.String,
        'image': fields.String,
    })
    
    user_ban = user_ns.model("user_ban", {
        'banned_user_id': fields.Integer,
        'username': fields.String,
    })
    
    own_profile = user_ns.model("own_profile", {
        'user_id': fields.Integer,
        'movie_wish': fields.List(fields.Nested(movie_wish)),
        'movie_ban': fields.List(fields.Nested(movie_ban)),
        'user_ban': fields.List(fields.Nested(user_ban)),
    })
    
    other_profile = user_ns.model("other_profile", {
        'user_id': fields.Integer,
        'movie_wish': fields.List(fields.Nested(movie_wish)),
        'movie_ban': fields.List(fields.Nested(movie_ban)),
    })
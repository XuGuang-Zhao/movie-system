import datetime

from main import db


class Movies(db.Model):
    # this is a Movie table schema
    
    _tablename_ = 'movies'
    
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    image = db.Column(db.Text)
    description = db.Column(db.Text)
    genres = db.Column(db.Text)
    actor = db.Column(db.Text)
    director = db.Column(db.Text)
    rating = db.Column(db.Float)
    
    #reviews = db.relationship('Reviews', backref='movies')
#   recommendation = db.relationship('Recommendation', backref='movie')

#class Reviews(db.Model):
#    # this is a movie-review table schema
#    
#    _tablename_ = 'movie_reviews'
#    
#    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
#    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
#    #user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#    user_id = db.Column(db.Integer)
#    #user_gender = db.Column(db.String(1))
#    rating = db.Column(db.SmallInteger)
#    review_text = db.Column(db.Text)
#
#class Users(db.Model):
#    # this is a user table schema
#    
#    _tablename_ = 'users'
#    
#    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
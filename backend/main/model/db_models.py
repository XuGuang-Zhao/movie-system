import datetime

from main import db


class Movies(db.Model):
    # this is a Movie table schema
    
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    image = db.Column(db.Text)
    description = db.Column(db.Text)
    genres = db.Column(db.Text)
    actor = db.Column(db.Text)
    director = db.Column(db.Text)
    rating = db.Column(db.Float, default=0)

#    reviews = db.relationship('Reviews', backref='movies')
#   recommendation = db.relationship('Recommendation', backref='movie')

#class Reviews(db.Model):
    # this is a movie-review table schema
    
#    __tablename__ = 'movie_reviews'
    
#    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
#    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
#    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#    user_gender = db.Column(db.String(1))
#    rating = db.Column(db.SmallInteger)
#    review_text = db.Column(db.Text)

class Users(db.Model):
    # this is a user table schema
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    email = db.Column(db.Text, nullable=False)
    
    user_movie = db.relationship('UserMovieList', backref='users')
    #review = db.relationship('Reviews', backref='users')

class UserBanList(db.Model):
    # this is a user ban list table schema
    
    __tablename__ = 'user_ban'
    
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('Users', foreign_keys = [user_id])
    
    banned_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    banned_user = db.relationship('Users', foreign_keys = [banned_user_id])

class UserMovieList(db.Model):
    # this is a user movie list table schema
    
    __tablename__ = 'user_movie'
    
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category = db.Column(db.String(10), nullable=False) # can be wishlist or banned list, use 'Wish' or 'Ban'
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))

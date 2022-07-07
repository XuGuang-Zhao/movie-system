import traceback
from hashlib import md5
from sqlalchemy import and_
from main.model.db_models import Users, UserBanList, UserMovieList, Movies
from main import db
import random

# not implement yet
salt = 'asbfosfgnpiuddgposuisgdfpos'
def encrypt_pwd(password, salt=salt):
    """
    Use md5 algorthm to encrypt password for security.
    @:param 

    @:return 
    """
    return md5((password + salt).encode(encoding='UTF-8')).hexdigest()


def login(request):
    """
    @:param 

    @:return 
    """
    res = Users()
    user = Users.query.filter(Users.username==request.get('username', '')).first()
    if user is None:
        res.message = 'Username does not exist.'
        msg = 'fail'
    elif request.get('password', '') != user.password:    
#    elif encrypt_pwd(request.get('password', '')) != user.password:
        res.message = 'Password is incorrect.'
        msg = 'fail'
    else:
        user_info = Users.query.filter(Users.username==request.get('username', '')).first()
        res.user_id = user_info.id
        res.username = user_info.username
        res.email = user_info.email
        res.gender = user_info.gender
        msg = 'success'
    return res, msg

def register(request):
    """
    @:param 

    @:return 
    """
    res = Users()
    if not request.get('username', ''):
        res.message = 'Invaild username.'
        msg = 'fail'
    elif not request.get('password', ''):
        res.message = 'Invaild password.'
        msg = 'fail'
    elif not request.get('email', ''):
        res.message = 'Invaild email.'
        msg = 'fail'
    elif Users.query.filter(Users.username==request.get('username', '')).first() is not None:
        res.message = 'Username already exists.'
        msg = 'fail'
    elif Users.query.filter(Users.email==request.get('email', '')).first() is not None:
        res.message = 'Email already exists.'
        msg = 'fail'
    else:
        id = random.randint(0, 10000)
        while Users.query.filter(Users.id==id).first() is not None:
            id = random.randint(0, 10000)
        user = Users(
            id=id,
            username=request.get('username', ''),
            password=request.get('password', ''),
            #password=encrypt_pwd(request.get('password', '')),
            email=request.get('email',''),
            gender=request.get('gender', ''))
        try:
            db.session.add(user)
            db.session.commit()
            user_info = Users.query.filter(Users.username==request.get('username', '')).first()
            res.user_id = user_info.id
            res.username = user_info.username
            res.email = user_info.email
            res.gender = user_info.gender
            msg = 'success'
        except Exception as e:
            db.session.rollback()
            res.message = e
            msg = 'fail'
    return res, msg

def reset_pwd(request):    
    """
    @:param 

    @:return 
    """
    res = Users()
    user = Users.query.filter(Users.username==request.get('username', '')).first()
    if not request.get('username', ''):
        res.message = 'Invaild username.'
        msg = 'fail'
    elif request.get('old_pwd', '') == request.get('new_pwd', ''):
        res.message = 'New password is the same as the old one.'
        msg = 'fail'
    elif not request.get('new_pwd', ''):
        res.message = 'Invaild new password.'
        msg = 'fail'
    elif user is None:
        res.message = 'Username not exists.'
        msg = 'fail'
    elif user.password != request.get('old_pwd', ''):
        res.message = 'Incorrect old password.'
        msg = 'fail'
    else:
        user.password = request.get('new_pwd','')
        try:
            db.session.add(user)
            db.session.commit()
            res.message = 'Reset password successfully.'
            msg = 'success'
        except Exception as e:
            db.session.rollback()
            res.message = e
            msg = 'fail'
    return res, msg

def view(username):
    res = Users()
    user = Users.query.filter(Users.username==username).first()
    if user is None:
        res.message = 'Username does not exist.'
        msg = 'fail'
    else:
        res.user_id = user.id
        res.username = user.username
        res.email = user.email
        res.gender = user.gender
        res.password = user.password
        msg = 'success'
    return res, msg

def own_profile(user_id):
    own_profile = Users()
    own_profile.user_id = user_id.get('user_id')
    own_profile.movie_wish = UserMovieList.query \
                                .filter(UserMovieList.user_id == user_id.get('user_id'), UserMovieList.category == 'Wish') \
                                .join(Movies, UserMovieList.movie_id == Movies.id) \
                                .with_entities(UserMovieList.movie_id, Movies.name, Movies.image) \
                                .all()
    own_profile.movie_ban = UserMovieList.query \
                                .filter(UserMovieList.user_id == user_id.get('user_id'), UserMovieList.category == 'Ban') \
                                .join(Movies, UserMovieList.movie_id == Movies.id) \
                                .with_entities(UserMovieList.movie_id, Movies.name, Movies.image) \
                                .all()
    sub_stmt = UserBanList.query.filter(UserBanList.user_id == user_id.get('user_id')).with_entities(UserBanList.banned_user_id)
    own_profile.user_ban = UserBanList.query \
                            .filter(UserBanList.user_id == user_id.get('user_id')) \
                            .join(Users, UserBanList.banned_user_id == Users.id) \
                            .with_entities(UserBanList.banned_user_id, Users.username) \
                            .all()
    
    return own_profile, 'success'
    
def other_profile(user_id):
    other_profile = Users()
    other_profile.user_id = user_id.get('user_id')
    other_profile.movie_wish = UserMovieList.query \
                                .filter(UserMovieList.user_id == user_id.get('user_id'), UserMovieList.category == 'Wish') \
                                .join(Movies, UserMovieList.movie_id == Movies.id) \
                                .with_entities(UserMovieList.movie_id, Movies.name, Movies.image) \
                                .all()
    other_profile.movie_ban = UserMovieList.query \
                                .filter(UserMovieList.user_id == user_id.get('user_id'), UserMovieList.category == 'Ban') \
                                .join(Movies, UserMovieList.movie_id == Movies.id) \
                                .with_entities(UserMovieList.movie_id, Movies.name, Movies.image) \
                                .all()
    
    return other_profile, 'success'

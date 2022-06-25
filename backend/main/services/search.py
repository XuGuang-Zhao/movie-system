import traceback

from main.model.db_models import Movies#, Reviews
from main import db  # db is not required for queries, but is required for writes

# NOT COMPLETE YET

def search(name, 
           desc, 
           genre, 
           actor, 
           director, 
           #username
           ):
    # Query the movies that meets the requirement
    #reviews = Reviews.query(func.avg(rating).label('rating')) \
    #                 .group_by(movie_id)
    movies = Movies.query \
            .filter(Movies.name.like("%{}%".format(name))) \
            .order_by(Movies.rating.desc()) \
            .all()
    search_result = Movies()
    search_result.movie_list = movies
    return search_result

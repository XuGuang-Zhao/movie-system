import traceback
from sqlalchemy import and_
from main.model.db_models import Movies#, Reviews
from main import db  # db is not required for queries, but is required for writes

# NOT COMPLETE YET

def search(search_request, order_by='avg_rating'):
    """
    :param search_request: a dictionary in form of search_request
    :param order_by: the type of ordering (default by ratings now, maybe change to relevance later)

    :return: the search result
    """
    # Query the movies that meets the requirement
    # below section needs to be changed for name / other attribute search and ordering
    keywords = [name.lower() for name in search_request['name'].split()]
    kw_filter = [Movies.name.contains(kw) for kw in keywords]
    # kw_filter = [Movies.name.like("%{}%".format(kw)) for kw in keywords]

    filtered_movies = Movies.query \
            .filter(and_(*kw_filter), \
                Movies.description.contains(search_request.get('desc', '').lower()),\
                Movies.genres.contains(search_request.get('genre', '').lower()), \
                Movies.actor.contains(search_request.get('actor', '').lower()),\
                Movies.director.contains(search_request.get('director', '').lower()))\
            .order_by(Movies.rating.desc())\
            .all()
    search_result = Movies()
    filters = {}
    for movie in filtered_movies:
        if movie.genres:
            for g in movie.genres.split(','):
                filters[('Genre',g)] = filters.get(('Genre',g),0) + 1
        if movie.actor:
            for a in movie.actor.split(','):
                filters[('Actor',a)] = filters.get(('Actor',a),0) + 1
        if movie.director:
            for d in movie.director.split(','):
                filters[('Director',d)] = filters.get(('Director',d),0) + 1
    search_result.filter_list = sorted([{'category':c, 'name': n, 'count': v} for (c,n), v in filters.items()], key = lambda x: (x['category'], -x['count']))
    search_result.movie_list = filtered_movies
    # Only return the list of filters (based on the filtered movies) and the information of movies meet the requirements
    return search_result


def filter(filter_request):
    """
    :param filter_request: a dictionary in form of filter_request

    :return: the search result
    """
    # After searching, frontend get the list of filters and save it. 
    # If frontend sends a filter request, backend will return the information of movies which meet the requirements from previous search resquest and current filter request 
    
    # we may need to modify the structure of filter_request to make this simpler.
    keywords = [name.lower() for name in filter_request['search_request']['name'].split()]

    kw_filter = [Movies.name.contains(kw) for kw in keywords]
    # kw_filter = [Movies.name.like("%{}%".format(kw)) for kw in keywords]
    genre_filter = [Movies.genres.contains(filter_request['search_request'].get('genre', '').lower()),\
         Movies.genres.contains(filter_request.get('genre_filter', '').lower())]
    actor_filter = [Movies.actor.contains(filter_request['search_request'].get('actor', '').lower()),\
                Movies.actor.contains(filter_request.get('actor_filter', '').lower())] 
    director_filter = [Movies.director.contains(filter_request.get('director_filter', '').lower()),\
                Movies.director.contains(filter_request['search_request'].get('director', '').lower())]

    movies = Movies.query \
            .filter(and_(*kw_filter), \
                Movies.description.contains(filter_request['search_request'].get('desc', '').lower()),\
                and_(*genre_filter), \
                and_(*actor_filter),\
                and_(*director_filter))\
            .order_by(Movies.rating.desc())\
            .all()

    filter_result = Movies()
    filter_result.movie_list = movies
    return filter_result
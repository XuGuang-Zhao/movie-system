import traceback
from sqlalchemy import and_
from main.model.db_models import Movies#, Reviews
from main import db

# NOT COMPLETE YET
def split_keywords(keyword_string):
    """
    :param keyword_string: the string containing keywords for searching

    :return: a list of keywords

        keyword_string              keywords
    "short keyword"     -->     ["short", "keyword"]
    "'long keyword'"    -->     ["long keyword"]
    "time machine 'star wars' hello world" --> ["time", "machine", "star wars", "hello", "world"]
    """
    words = [word.lower() for word in keyword_string.split()]
    keywords = []
    i = 0
    while i < len(words):
        keyword = words[i]
        if keyword[0] == "\'":
            if keyword[-1] != "\'":
                keyword = keyword[1:]
                while i < len(words) - 1:
                    i += 1
                    keyword += " " + words[i]
                    if keyword[-1] == "\'":
                        keyword = keyword[:-1]
                        break
            else:
                keyword = keyword[1:-1]
        keywords.append(keyword)
        i += 1
    return keywords

def search(search_request):
    """
    :param search_request: a dictionary in form of search_request

    :return: the search result
    """
    # Query the movies that meets the requirement
    # below section needs to be changed for name / other attribute search and ordering

    keywords = split_keywords(search_request['name'])
    kw_filter = [Movies.name.contains(kw) for kw in keywords]
    # kw_filter = [Movies.name.like("%{}%".format(kw)) for kw in keywords]

    filtered_movies = Movies.query \
            .filter(and_(*kw_filter), 
                Movies.description.contains(search_request.get('desc', '').lower()),
                Movies.genres.contains(search_request.get('genre', '').lower()), 
                Movies.actor.contains(search_request.get('actor', '').lower()),
                Movies.director.contains(search_request.get('director', '').lower()))\
            .order_by(Movies.rating.desc(), Movies.name.asc())\
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

    :return: the filtered result
    """
    # After searching, frontend get the list of filters and save it. 
    # If frontend sends a filter request, backend will return the information of movies which meet the requirements from previous search resquest and current filter request 
    
    # we may need to modify the structure of filter_request to make this simpler.
    keywords = split_keywords(filter_request['search_request']['name'])
    kw_filter = [Movies.name.contains(kw) for kw in keywords]
    # kw_filter = [Movies.name.like("%{}%".format(kw)) for kw in keywords]
    desc_filter = [Movies.description.contains(filter_request['search_request'].get('desc', '').lower())]
    genre_filter = [Movies.genres.contains(filter_request['search_request'].get('genre', '').lower()),
        *[Movies.genres.contains(g.lower()) for g in filter_request.get('genre_filter', '').split(',') if g != '']]
    actor_filter = [Movies.actor.contains(filter_request['search_request'].get('actor', '').lower()),
        *[Movies.actor.contains(a.lower()) for a in filter_request.get('actor_filter', '').split(',') if a != '']]
    director_filter = [Movies.director.contains(filter_request['search_request'].get('director', '').lower()),
        *[Movies.director.contains(d.lower()) for d in filter_request.get('director_filter', '').split(',') if d != '']]

    movies = Movies.query\
            .filter(and_(*kw_filter), 
                and_(*desc_filter),
                and_(*genre_filter), 
                and_(*actor_filter),
                and_(*director_filter))

    ordering = filter_request['order_by']
    if ordering == 'avg_rating_desc':
        movies.order_by(Movies.rating.desc(), Movies.name.asc()).all()
    elif ordering == 'avg_rating_asc':
        movies.order_by(Movies.rating.asc(), Movies.name.asc()).all()
    elif ordering == 'alpha_asc':
        movies = movies.order_by(Movies.name.asc(), Movies.rating.desc()).all()
    elif ordering == 'alpha_desc':
        movies = movies.order_by(Movies.name.desc(), Movies.rating.desc()).all()
    
    filter_result = Movies()
    filter_result.movie_list = movies
    return filter_result
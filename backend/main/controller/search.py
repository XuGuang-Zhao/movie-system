from flask import request
from flask import json

from flask_restplus import Resource
from flask_restplus import marshal

from main.transform.search import SearchObject
from main.namespace import search_ns
from main.services import search


@search_ns.route("/search")
class Search(Resource):
    """
    @:parameter data via post
    @:return All movie information if search successfully.
    """

    @search_ns.expect(SearchObject.search_request)
    @search_ns.response(200, 'success', model=SearchObject.search_response)
    @search_ns.response(403, 'fail', model=SearchObject.search_response)
    def post(self):
        dict = json.loads(request.data)  # Parse request into a dictionary

        print(dict)

        # Execute the specific method, and get the returned dictionary
        response_dict = search.search(dict)

        status_code = 200 #if response_dict.message == 'success' else 403  # success or fail
        
        response_dict.filter_request = dict
        
        return marshal(response_dict, SearchObject.search_response), status_code

@search_ns.route("/filter")
class Filter(Resource):
    """
    @:parameter data via post
    @:return All movie information if search successfully.
    """

    @search_ns.expect(SearchObject.filter_request)
    @search_ns.response(200, 'success', model=SearchObject.filter_response)
    @search_ns.response(403, 'fail', model=SearchObject.filter_response)
    def post(self):
        dict = json.loads(request.data)  # Parse request into a dictionary

        print(dict)

        # Execute the specific method, and get the returned dictionary
        response_dict = search.filter(dict)

        status_code = 200 #if response_dict.message == 'success' else 403  # success or fail
        
        response_dict.filter_request = dict
        
        return marshal(response_dict, SearchObject.filter_response), status_code
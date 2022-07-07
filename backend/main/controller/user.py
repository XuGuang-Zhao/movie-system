from flask import request
from flask import json

from flask_restplus import Resource
from flask_restplus import marshal

from main.transform.user import UserObject
from main.namespace import user_ns
from main.services import user


@user_ns.route("/login")
class Login(Resource):
    """
    @:parameter data via post
    @:return That user's info if login successfully. Else return the error msg.
    """
    @user_ns.expect(UserObject.login_request)
    @user_ns.response(200, 'success', model=UserObject.user_info_response)
    @user_ns.response(403, 'fail', model=UserObject.msg_response)
    def post(self):
        dict = json.loads(request.data) 
        response_dict, msg = user.login(dict)
        if msg == 'success':
            status_code = 200 
            return marshal(response_dict, UserObject.user_info_response), status_code
        else:
            status_code = 403
            return marshal(response_dict, UserObject.msg_response), status_code
            
@user_ns.route("/register")
class Register(Resource):
    """
    @:parameter data via post
    @:return That user's info if register successfully. Else return the error msg.
    """

    @user_ns.expect(UserObject.register_request)
    @user_ns.response(200, 'success', model=UserObject.user_info_response)
    @user_ns.response(403, 'fail', model=UserObject.msg_response)
    def post(self):
        dict = json.loads(request.data) 
        response_dict, msg = user.register(dict)
        if msg == 'success':
            status_code = 200 
            return marshal(response_dict, UserObject.user_info_response), status_code
        else:
            status_code = 403
            return marshal(response_dict, UserObject.msg_response), status_code


@user_ns.route("/reset_password")
class Reset_pwd(Resource):
    """
    @:parameter data via post
    @:return message
    """

    @user_ns.expect(UserObject.reset_pwd_request)
    @user_ns.response(200, 'success', model=UserObject.msg_response)
    @user_ns.response(403, 'fail', model=UserObject.msg_response)
    def post(self):
        dict = json.loads(request.data) 
        response_dict, msg = user.reset_pwd(dict)
        status_code = 200 if msg == 'success' else 403
        return marshal(response_dict, UserObject.msg_response), status_code

# This is for debugging
@user_ns.route("/view")
class View(Resource):
    """
    @:parameter data via post
    @:return message
    """

    @user_ns.expect(UserObject.view_request)
    @user_ns.response(200, 'success', model=UserObject.user_details)
    @user_ns.response(403, 'fail', model=UserObject.msg_response)
    def post(self):
        dict = json.loads(request.data) 
        response_dict, msg = user.view(**dict)
        status_code = 200 
        if msg == 'success':
            status_code = 200 
            return marshal(response_dict, UserObject.user_details), status_code
        else:
            status_code = 403
            return marshal(response_dict, UserObject.msg_response), status_code

@user_ns.route("/own_profile")
class OwnProfile(Resource):
    @user_ns.expect(UserObject.user_id)
    @user_ns.response(200, 'success', model=UserObject.own_profile)
    @user_ns.response(403, 'fail', model=UserObject.msg_response)
    def post(self):
        dict = json.loads(request.data) 
        response_dict, msg = user.own_profile(dict)
        if msg == 'success':
            status_code = 200 
            return marshal(response_dict, UserObject.own_profile), status_code
        else:
            status_code = 403
            return marshal(response_dict, UserObject.msg_response), status_code

@user_ns.route("/other_profile")
class OtherProfile(Resource):
    """
    @:parameter data via post
    @:return That user's info if login successfully. Else return the error msg.
    """

    @user_ns.expect(UserObject.user_id)
    @user_ns.response(200, 'success', model=UserObject.other_profile)
    @user_ns.response(403, 'fail', model=UserObject.msg_response)
    def post(self):
        dict = json.loads(request.data) 
        response_dict, msg = user.other_profile(dict)
        if msg == 'success':
            status_code = 200 
            return marshal(response_dict, UserObject.other_profile), status_code
        else:
            status_code = 403
            return marshal(response_dict, UserObject.msg_response), status_code

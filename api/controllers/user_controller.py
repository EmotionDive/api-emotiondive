import json
from flask import Response, request
from flask_restful import Resource
from ..services.user_service import *

class Users(Resource):
    """
    Resource for general access to users of Emotion Dive
    """
    def get(self, username):
        user_obj = read_user(username)
        return user_obj
        
    def post(self, username):
        email = request.json["email"]
        age = request.json["age"]
        sex = request.json["sex"]
        civil_status = request.json["civil_status"]
        housing_situation = request.json["housing_situation"]
        active_account = request.json["active_account"]

        response_obj = create_user(username, email, age, sex, civil_status, housing_situation, active_account)
        return response_obj
        

    def delete(self, username):
        response_obj = delete_user(username)
        return response_obj
        
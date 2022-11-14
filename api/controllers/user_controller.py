from flask import request
from flask_restful import Resource
from ..services.user_service import *

class Users(Resource):
    """
    Resource for general access to users of Emotion Dive
    """
    def get(self, username):
        return read_user(username)
        
    def post(self, username):
        email = request.json["email"]
        name = request.json["name"]
        age = request.json["age"]
        sex = request.json["sex"]
        civil_status = request.json["civil_status"]
        housing_situation = request.json["housing_situation"]

        response_obj = create_user(
            username, 
            email, 
            name, 
            age, 
            sex, 
            civil_status, 
            housing_situation
        )
        return response_obj
        

    def delete(self, username):
        return delete_user(username)
        
class Username(Resource):
    """
    Resource to validate an username
    """
    def get(self, username):
        return validate_username(username)
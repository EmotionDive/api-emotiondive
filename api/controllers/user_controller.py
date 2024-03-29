from flask import request
from flask_restful import Resource
from ..services.user_service import *

class UserCreation(Resource):
    """
    Resource to create or delete users of the Emotion Dive DB
    """
    def post(self, username):
        email = request.json.get("email", None)
        name = request.json.get("name", None)
        age = request.json.get("age", None)
        sex = request.json.get("sex", None)
        civil_status = request.json.get("civil_status", None)
        housing_situation = request.json.get("housing_situation", None)

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
        
class UserUpdate(Resource):
    """
    Resource to update users info in Emotion Dive
    """
    def post(self, username):
        civil_status = request.json.get("civil_status", None)
        housing_situation = request.json.get("housing_situation", None)

        response_obj = update_user(
            username, 
            civil_status, 
            housing_situation
        )
        return response_obj
        
class UserInfo(Resource):
    """
    Resource to get user information
    """
    def get(self, email):
        return read_user(email)
        

class Username(Resource):
    """
    Resource to validate an username
    """
    def get(self, username):
        return validate_username(username)
import json
from flask import Response, request
from flask_restful import Resource
from api.resources.db.user_queries import *

class User(Resource):
    """
    Resource for general access to users of Emotion Dive
    """
    def get(self, username):
        user_data = get_user(username)
        user_obj = json.dumps(user_data)
        return Response(user_obj, mimetype="application/json", status=200)

    def post(self, username):
        ### In case we are dealing with raw data in the body of a POST request
        # username = request.get_data()
        # You don't need to specify encoding or decoding as UTF-8 it's default on python 3.X
        # user_obj = json.loads(username.decode()) 
        # return user_obj, 200
    
        ### In case that we are dealing with Form Data
        email = request.form.get("email")
        password = request.form.get("password")
        age = int(request.form.get("age"))
        sex = request.form.get("sex")
        civil_status = request.form.get("civil_status")
        housing_situation = int(request.form.get("housing_situation"))
        active_account = request.form.get("active_account")

        insert_user(username, email, password, age, sex, civil_status, housing_situation, active_account)
        return Response("User successfully created", mimetype="application/json", status=200)

    def delete(self, username):
        delete_user(username)
        return Response("User successfully deleted", mimetype="application/json", status=200)
        
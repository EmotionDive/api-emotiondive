import json
from flask import Response, request
from flask_restful import Resource
from api.controllers.db.user_queries import *
from ..services.user_service import *

class User(Resource):
    """
    Resource for general access to users of Emotion Dive
    """
    def get(self, username):
        user_data = get_user(username)
        user_obj = json.dumps(user_data)
        return Response(user_obj, mimetype="application/json", status=200)

    def post(self, username):
        email = request.form.get("email")
        password = request.form.get("password")
        age = int(request.form.get("age"))
        sex = request.form.get("sex")
        civil_status = request.form.get("civil_status")
        housing_situation = int(request.form.get("housing_situation"))
        active_account = request.form.get("active_account")

        response_obj = create_user(username, email, age, sex, civil_status, housing_situation, active_account)
        
        return response_obj, 200

    def delete(self, username):
        delete_user(username)
        return Response("User successfully deleted", mimetype="application/json", status=200)
        
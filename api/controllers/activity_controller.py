from flask import request
from flask_restful import Resource
from ..services.activity_service import *

class ActivitiesDescription(Resource):
    """
    Resource to get the data of two activities selected by the user
    """
    def post(self):
        competences = request.json["competences"]
        return get_competence_activities(competences)

class ActivitiesByUser(Resource):
    """
    Resource to get all the activities that an user completeted 100%
    """
    def get(self, username):
        return get_activities_by_user(username)
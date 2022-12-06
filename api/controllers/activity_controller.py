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
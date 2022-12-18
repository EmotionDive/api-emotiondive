from flask import request
from flask_restful import Resource
from ..services.competences_service import *

class Competences(Resource):
    """
    Resource to register and consult the selected comptences by the user
    """
    def get(self, username):
        return get_actual_competences(username)

    def post(self, username):
        competences = request.json["competences"]
        return register_competences(username, competences)

class RemainingCompetences(Resource):
    """
    Resource to get the remaining competences due the users' previous plans
    """
    def get(self, username):
        return get_undone_competences(username)
        
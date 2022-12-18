from flask import request
from flask_restful import Resource
from ..services.activity_service import *

class ActivitiesDescriptionByCompetence(Resource):
    """
    Resource to get the data of two activities selected by the user
    """
    def post(self):
        competences = request.json.get("competences", None)
        return get_competence_activities(competences)

class CompletedByUser(Resource):
    """
    Resource to get all the activities that an user completeted 100%
    """
    def get(self, username):
        return get_user_completed_activities(username)

class CompetenceCompletedByUser(Resource):
    """
    Resource to get all the competences which activities have been completed 100%
    """
    def post(self, username):
        competences = request.json.get("competences", None)
        test_flag = request.json.get("test_flag", None)

        if test_flag == None:
            return get_competences_finished(username, competences)
        else:
            return get_competences_finished(username, competences, test_flag)
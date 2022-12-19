from flask import request
from flask_restful import Resource
from ..services.test_service import *

class Tests(Resource):
    """
    Resource to save and get test results
    """
    def get(self, username):
        return get_statistics(username)

    def post(self, username):
        # answers = [5 for i in range(56)]
        answers = request.json.get("answers", None)
        return save_test_IE(answers, username)
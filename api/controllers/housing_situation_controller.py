from flask import request
from flask_restful import Resource
from ..services.housing_situation_service import *

class HousingSituationCatalog(Resource):
    """
    Resource to get the housing situation based on an ID
    """
    def get(self):
        response_obj = get_housing_situations()
        return response_obj
from flask import request
from flask_restful import Resource
from ..services.statics_IE import *

class statics_IECatalog(Resource):
    "Catalog to get the cognitive data of an user based on their ID"
    def get(self):
        answers = request.json["answers"]
        response_objIE = get_statics_IE(answers)
        return response_objIE
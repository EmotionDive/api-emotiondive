from flask import request
from flask_restful import Resource
from ..services.special_activity_service import *

class SpecialAcitvity(Resource):
    """
    Resource to write and read activity data of the user
    """
    def get(self, username, index=-1):
        if index != -1:
            return read_activity_info_specific(username, index)
        else:
            return read_activity_info(username)

    def post(self, username, index=-1):
        if index != -1:
            exito = request.json.get("exitos", None)
            fracaso = request.json.get("fracasos", None)
            return write_activity_info_specific(username, index, exito[0], fracaso[0])
        else:
            exitos = request.json.get("exitos", None)
            fracasos = request.json.get("fracasos", None)
            overwrite = request.json.get("overwrite", None)
            return write_activity_info(username, exitos, fracasos, overwrite)
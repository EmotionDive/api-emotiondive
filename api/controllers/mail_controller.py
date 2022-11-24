from flask import request
from flask_restful import Resource
from ..services.mail_service import *

class VerifyMail(Resource):
    """
    Resource to send a verfication mail
    """
    def get(self, email):
        return send_mail(email)
        
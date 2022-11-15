from flask import request
from flask_restful import Resource
from ..services.mail_service import *

class MailVerification(Resource):
    """
    Resource to verify an user's account
    """
    def get(self, username):
        return send_mail(username)
        
    def post(self, username):
        verification_code = request.json["code"]
        return verify_token(username, verification_code)
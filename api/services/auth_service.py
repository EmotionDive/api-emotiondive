import http.client
import json
from .. import db
from ..models.user import User
from ..models.test import Test

def get_auth_user(email):
    """
    Funtion to retrieve users by email from the Get Users Endpoint of the Auth0 Management API
    """
    AUTH0_DOMAIN = "dev-g4tx3izjk73lzxck.us.auth0.com"
    MGMT_API_TOKEN = ""
    conn = http.client.HTTPSConnection(AUTH0_DOMAIN)
    headers = { 
        'content-type': "application/json",
        'authorization': "Bearer " + MGMT_API_TOKEN 
    }
    conn.request("GET", "/api/v2/users-by-email?email=" + email, headers=headers)

    res = conn.getresponse()
    data = res.read().decode('utf-8')
    response_obj = json.loads(data)

    return response_obj

def get_auth_flags(email):
    """
    Funtion to return auth flags given an user conditions
    """
    auth_flags = {'is_registered' : False, 'is_active' : False, 'is_first_time' : False}

    try:
        ## Validation that the account is actually active on Emotion Dive
        user_query = User.query.filter_by(correo=email).first()
        if user_query is not None:
            auth_flags['is_registered'] = True
            if user_query.active_account == 'ACTIVE':
                auth_flags['is_active'] = True

            ## Validation for users' first time using Emotion Dive
            test_query = Test.query.filter_by(username_usuario=user_query.username).first()
            if test_query is None:
                auth_flags['is_first_time'] = True

        return auth_flags, 200
    except Exception as e:
        response_obj = {
            "status": "fail",
            "message": str(e)
        }
        return response_obj, 400
     


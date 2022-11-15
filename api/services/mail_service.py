import jwt
from flask import current_app
from .. import email, db
from ..models.user import User

def send_mail(username):
    try:
        user = User.query.get(username)
        verification_token = jwt.encode(
            {
                "email": user.correo,
                "active_account": user.active_account,
            }, current_app.config["SECRET_KEY"],
            algorithm="HS256"
        )
        email.send(
            subject="Verify your Emotion Dive account!",
            receivers=[user.correo],
            html_template="verify_email.html",
            body_params={
                "name": user.nombre,
                "username": username,
                "url": "http://localhost:3000/activeAccount?code=" + verification_token
            }
        )
        response_obj = {
            "status": "success",
            "message": "Verification mail sended successfully."
        }
        return response_obj, 200
    except Exception as e:
        response_obj = {
            "status": "fail",
            "message": str(e)
        }
        return response_obj, 400
    
def verify_token(username, mail_token):
    try:
        user = User.query.get(username)
        dec_token = jwt.decode(
            mail_token, 
            current_app.config["SECRET_KEY"],
            algorithms=["HS256"]
        )
        if dec_token['email'] == user.correo and dec_token['active_account'] == user.active_account:
            user.active_account = 'ACTIVE'
            db.session.commit()
            response_obj = {
                "status": "success",
                "message": "User email address verified successfully."
            }
            return response_obj, 200
        else:
            response_obj = {
                "status": "fail",
                "message": "User email address couldn't be verified due to the token."
            }
            return response_obj, 400
    except Exception as e:
        response_obj = {
            "status": "fail",
            "message": str(e)
        }
        return response_obj, 400
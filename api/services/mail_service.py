import jwt
from flask import current_app
from .. import email, db
from ..models.user import User

def send_mail(user_email):
    try:
        user = User.query.filter_by(correo=user_email).first()
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
                "username": user.username,
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
    
def verify_token(mail_token):
    try:
        
        dec_token = jwt.decode(
            mail_token, 
            current_app.config["SECRET_KEY"],
            algorithms=["HS256"]
        )
        user = User.query.filter_by(correo=dec_token['email']).first()
        if dec_token['active_account'] == user.active_account:
            aux_active_acount = user.active_account
            user.active_account = 'ACTIVE'
            db.session.commit()
            response_obj = {
                "status": "success",
                "token_mail": dec_token['email'],
                "received_token": dec_token['active_account'],
                "DB_token": aux_active_acount,
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
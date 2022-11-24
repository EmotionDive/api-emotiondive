import secrets
from .. import db
from ..models.user import User, user_schema

def create_user(
    username, 
    correo, 
    nombre,
    edad, 
    sexo, 
    estado_civil, 
    id_situacion_habitacional
):
    try:
        active_account = secrets.token_hex(16)
        new_user = User(username, 
            correo, 
            nombre, 
            edad, 
            sexo, 
            estado_civil, 
            id_situacion_habitacional, 
            active_account
        )
        db.session.add(new_user)
        db.session.commit()
        response_obj = {
            "status": "success",
            "message": "User successfully created."
        }
        return response_obj, 200
    except Exception as e:
        response_obj = {
            "status": "fail",
            "message": str(e)
        }
        return response_obj, 400

def read_user(email):
    try:
        user = User.query.filter_by(correo=email).first()
        return user_schema.dump(user), 200
    except Exception as e:
        response_obj = {
            "status": "fail",
            "message": str(e)
        }
        return response_obj, 400

def delete_user(username):
    try:
        user_obj = User.query.filter_by(username=username).one()
        db.session.delete(user_obj)
        db.session.commit()
        response_obj = {
            "status": "success",
            "message": "User successfully deleted."
        }
        return response_obj, 200
    except Exception as e:
        response_obj = {
            "status": "fail",
            "message": str(e)
        }
        return response_obj, 400

def validate_username(username):
    try:
        user = User.query.get(username)
        if user:
            response_obj = {
                "status": "success",
                "username_state": "occupied",
                "message": "Username state verified successfully."
            }
        else:
            response_obj = {
                "status": "success",
                "username_state": "available",
                "message": "Username state verified successfully."
            }
        return response_obj, 200
    except Exception as e:
        response_obj = {
            "status": "fail",
            "message": str(e)
        }
        return response_obj, 400
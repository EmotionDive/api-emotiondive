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
            "status": "Success",
            "message": "User successfully created."
        }
        return response_obj, 200
    except Exception as e:
        response_obj = {
            "status": "fail",
            "message": str(e)
        }
        return response_obj, 400

def read_user(username):
    try:
        user = User.query.get(username)
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
            "status": "Success",
            "message": "User successfully deleted."
        }
        return response_obj, 200
    except Exception as e:
        response_obj = {
            "status": "fail",
            "message": str(e)
        }
        return response_obj, 400
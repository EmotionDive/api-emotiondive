from .. import db
from ..models.user import User, user_schema, users_schema

def create_user(
    username, 
    correo, 
    edad, 
    sexo, 
    estado_civil, 
    id_situacion_habitacional, 
    active_account
):
    try:
        new_user = User(username, correo, edad, sexo, estado_civil, id_situacion_habitacional, active_account)
        db.session.add(new_user)
        db.session.commit()
        response_obj = {
            "status": "Success",
            "message": "User successfully created."
        }
        return response_obj, 201
    except Exception as e:
        response_obj = {
            "status": "fail",
            "message": "An error occurred."
        }
        return response_obj, 401

def read_user(username):
    try:
        user = User.query.get(username)
        return user_schema.dump(user), 200
    except Exception as e:
        response_obj = {
            "status": "fail",
            "message": "I am error"
        }
        return response_obj, 401

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
            "message": "An error occurred."
        }
        return response_obj, 401
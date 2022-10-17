from .. import db
from ..models.user_model import UserModel, user_schema, users_schema

def create_user(username, correo, edad, sexo, estado_civil, id_situacion_habitacional, active_account):
    new_user = UserModel(username, correo, edad, sexo, estado_civil, id_situacion_habitacional, active_account)
    db.session.add(new_user)
    db.session.commit()
    
    return user_schema.dump(new_user)


from .. import db, ma

class UserModel(db.Model):
    """ User Model to store user data """
    __tablename__ = "usuario"

    username = db.Column(db.String(512), nullable=False, primary_key=True)
    correo = db.Column(db.String(126), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    sexo = db.Column(db.String(12), nullable=False)
    estado_civil = db.Column(db.String(128), nullable=False)
    id_situacion_habitacional = db.Column(db.Integer, nullable=False)
    active_account = db.Column(db.String(3), nullable=False)

    def __init__(self, username, correo, edad, sexo, estado_civil, id_situacion_habitacional, active_account):
        self.username = username
        self.correo = correo
        self.edad = edad
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.id_situacion_habitacional = id_situacion_habitacional
        self.active_account = active_account
    
class UserSchema(ma.Schema):
    class Meta:
        fields = ('username', 'correo', 'edad', 'sexo', 'estado_civil', 'id_situacion_habitacional', 'active_account')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
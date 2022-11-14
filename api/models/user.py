from .. import db, ma
from .housing_situation import HousingSituation

class User(db.Model):
    """ User Model to store user data """
    __tablename__ = "usuario"

    username = db.Column(
        db.String(512), 
        nullable=False, 
        primary_key=True
    )
    correo = db.Column(db.String(128), unique=True, nullable=False)
    nombre = db.Column(db.String(128), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    sexo = db.Column(db.String(12), nullable=False)
    estado_civil = db.Column(db.String(128), nullable=False)
    id_situacion_habitacional = db.Column(
        db.Integer, 
        db.ForeignKey('situacion_habitacional.id_situacion_habitacional'), 
        nullable=False
    )
    situacion_habitacional = db.relationship("HousingSituation", backref=db.backref("situacion_habitacional", uselist=False))
    active_account = db.Column(db.String(32), nullable=False)

    def __init__(
        self, 
        username, 
        correo,
        nombre, 
        edad, 
        sexo, 
        estado_civil, 
        id_situacion_habitacional, 
        active_account
    ):
        self.username = username
        self.correo = correo
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.id_situacion_habitacional = id_situacion_habitacional
        self.active_account = active_account
    
class UserSchema(ma.Schema):
    class Meta:
        fields = (
            'username', 
            'correo', 
            'nombre',
            'edad', 
            'sexo', 
            'estado_civil', 
            'id_situacion_habitacional', 
            'active_account'
        )

user_schema = UserSchema()
users_schema = UserSchema(many=True)
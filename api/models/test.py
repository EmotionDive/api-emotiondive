from .. import db, ma
from .user import User

class Test(db.Model):
    """ Test Model to store user's test results """
    __tablename__ = "test"

    username_usuario = db.Column(
        db.String(512), 
        db.ForeignKey('usuario.username'),
        nullable=False, 
        primary_key=True
    )
    usuario = db.relationship("User", backref=db.backref("usuario", uselist=False))
    fecha = db.Column(
        db.DateTime, 
        nullable=False, 
        primary_key=True
    )
    autoconocimiento = db.Column(db.Integer, nullable=False)
    autoregulacion = db.Column(db.Integer, nullable=False)
    autoeficacia = db.Column(db.Integer, nullable=False)
    empatia = db.Column(db.Integer, nullable=False)

    def __init__(
        self, 
        username_usuario, 
        fecha, 
        autoconocimiento, 
        autoregulacion, 
        autoeficacia, 
        empatia
    ):
        self.username_usuario = username_usuario  
        self.fecha = fecha 
        self.autoconocimiento = autoconocimiento 
        self.autoregulacion = autoregulacion 
        self.autoeficacia = autoeficacia 
        self.empatia = empatia

class TestSchema(ma.Schema):
    class Meta:
        fields = (
            'username_usuario', 
            'fecha', 
            'autoconocimiento', 
            'autoregulacion', 
            'autoeficacia',
            'empatia'
        )

test_schema = TestSchema()
tests_schema = TestSchema(many=True)
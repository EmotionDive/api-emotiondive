from .. import db, ma


class Statics(db.Model):
    "Users IE statics to show in the front app"
    def __init__(
        self,
        username_usuario,
        calificacion_autoconocimiento,
        calificacion_autoregulacion,
        calificacion_autoeficacia,
        calificacion_empatia
        ):
        self.username_usuario = username_usuario
        self.calificacion_autoconocimiento = calificacion_autoconocimiento
        self.calificacion_autoregulacion = calificacion_autoregulacion
        self.calificacion_autoeficacia = calificacion_autoeficacia
        self.calificacion_empatia = calificacion_empatia

class StaticSchema(ma.Schema):
    class Meta:
        fields = (
          'username_usuario',
          'calificacion_autoconocimiento',
          'calificacion_autoregulacion',
          'calificacion_autoeficiencia',
          'calificacion_empatia'
        )

Static_schema = StaticSchema()
Statics_schema = StaticSchema(many=True)


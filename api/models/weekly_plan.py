from .. import db, ma 
from .user import User

class WeeklyPlan(db.Model):
    """ Weekly plan model to store data related to the users' weekly plan """
    __tablename__ = "plan_semanal"

    id_plan_semanal = db.Column(
        db.Integer, 
        nullable=False, 
        primary_key=True
    )
    username_usuario = db.Column(
        db.String(512), 
        db.ForeignKey('usuario.username'),
        nullable=False
    )
    usuario = db.relationship(
        "User", 
        backref=db.backref("usuario_plan", uselist=False)
    )
    fecha = db.Column(db.DateTime, nullable=False)

    def __init__(
        self, 
        id_plan_semanal,
        username_usuario,
        fecha
    ):
        self.id_plan_semanal = id_plan_semanal
        self.username_usuario = username_usuario
        self.fecha = fecha
    
class WeeklyPlanSchema(ma.Schema):
    class Meta:
        fields = (
            'id_plan_semanal',
            'username_usuario',
            'fecha'
        )

weekly_plan_schema = WeeklyPlanSchema()
weekly_plan_schema = WeeklyPlanSchema(many=True)
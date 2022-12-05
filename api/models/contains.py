from .. import db, ma 
from .user import User
from .weekly_plan import WeeklyPlan
from .activity import Activity

class Contains(db.Model):
    """ Conatains is the table about the content of the users' weekly plan """
    __tablename__ = "contiene"

    username_usuario = db.Column(
        db.String(512), 
        db.ForeignKey('usuario.username'),
        nullable=False,
        primary_key=True
    )
    usuario = db.relationship(
        "User", 
        backref=db.backref("usuario_plan_content", uselist=False)
    )
    id_actividad = db.Column(
        db.Integer, 
        db.ForeignKey('actividad.id_actividad'),
        nullable=False,
        primary_key=True
    )
    actividad = db.relationship(
        "Activity", 
        backref=db.backref("actividad", uselist=False)
    )
    id_plan_semanal = db.Column(
        db.String(512), 
        db.ForeignKey('plan_semanal.id_plan_semanal'),
        nullable=False
    )
    plan_semanal = db.relationship(
        "WeeklyPlan", 
        backref=db.backref("plan_semanal", uselist=False)
    )
    progreso = db.Column(db.Integer, nullable=False)

    def __init__(
        self, 
        username_usuario,
        id_actividad,
        id_plan_semanal,
        progreso

    ):
        self.id_plan_semanal = id_plan_semanal
        self.id_actividad = id_actividad
        self.username_usuario = username_usuario
        self.progreso = progreso
    
class ContainsSchema(ma.Schema):
    class Meta:
        fields = (
            'id_plan_semanal',
            'username_usuario',
            'id_actividad',
            'progreso'
        )

contains_schema = ContainsSchema()
multiple_contains_schema = ContainsSchema(many=True)
from .. import db, ma 
from .user import User
from .cognitive_competence import CognitiveCompetence

class CompetencesSelection(db.Model):
    """ Table about the competences selected by the user """
    __tablename__ = "competencia_cognitiva_selec"

    username_usuario = db.Column(
        db.String(512), 
        db.ForeignKey('usuario.username'),
        nullable=False,
        primary_key=True
    )
    usuario = db.relationship(
        "User", 
        backref=db.backref("usuario_selection", uselist=False)
    )
    id_competencia_cognitiva = db.Column(
        db.Integer, 
        db.ForeignKey('competencia_cognitiva.id_competencia_cognitiva'),
        nullable=False,
        primary_key=True
    )
    competencia_cognitiva = db.relationship(
        "CognitiveCompetence", 
        backref=db.backref("competencia_cognitiva", uselist=False)
    )
    fecha = db.Column(
        db.DateTime, 
        nullable=False, 
        primary_key=True
    )

    def __init__(
        self, 
        username_usuario,
        id_competencia_cognitiva,
        fecha
    ):
        self.username_usuario = username_usuario
        self.id_competencia_cognitiva = id_competencia_cognitiva
        self.fecha = fecha
    
class CompetencesSelectionSchema(ma.Schema):
    class Meta:
        fields = (
            'id_plan_semanal',
            'id_competencia_cognitiva',
            'fecha'
        )

competence_selection_schema = CompetencesSelectionSchema()
competences_selection_schema = CompetencesSelectionSchema(many=True)
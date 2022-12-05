from .. import db, ma 
from .cognitive_competence import CognitiveCompetence

class Activity(db.Model):
    """ Activity model to store activities data """
    __tablename__ = "actividad"

    id_actividad = db.Column(
        db.Integer, 
        nullable=False, 
        primary_key=True
    )
    nombre = db.Column(db.String(126), nullable=False)
    descripcion = db.Column(db.String(1024), nullable=False)
    instrucciones = db.Column(db.String(1024), nullable=False)
    beneficios = db.Column(db.String(1024), nullable=False)
    tiempo_estimado = db.Column(db.Time, nullable=False)
    id_competencia_cognitiva = db.Column(
        db.Integer, 
        db.ForeignKey('competencia_cognitiva.id_competencia_cognitiva'), 
        nullable=False
    )
    competencia_cognitiva = db.relationship(
        "CognitiveCompetence", 
        backref=db.backref("competencia_cognitiva", uselist=False)
    )
    advertencia_bandera = db.Column(db.String(64), nullable=False)
    offline_bandera = db.Column(db.String(64), nullable=False)

    def __init__(
        self, 
        id_actividad,
        nombre,
        descripcion,
        instrucciones,
        beneficios,
        tiempo_estimado,
        id_competencia_cognitiva,
        advertencia_bandera,
        offline_bandera
    ):
        self.id_actividad = id_actividad
        self.nombre = nombre
        self.descripcion = descripcion
        self.instrucciones = instrucciones
        self.beneficios = beneficios
        self.tiempo_estimado = tiempo_estimado
        self.id_competencia_cognitiva = id_competencia_cognitiva
        self.advertencia_bandera = advertencia_bandera
        self.offline_bandera = offline_bandera
    
class ActivitySchema(ma.Schema):
    class Meta:
        fields = (
            'id_actividad',
            'nombre',
            'descripcion', 
            'instrucciones', 
            'beneficios', 
            'tiempo_estimado', 
            'id_competencia_cognitiva',
            'advertencia_bandera',
            'offline_bandera',
        )

activity_schema = ActivitySchema()
activities_schema = ActivitySchema(many=True)
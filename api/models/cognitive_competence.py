from .. import db, ma 

class CognitiveCompetence(db.Model):
    """ Cognitive competencies model that'll work as the competences catalog """
    __tablename__ = "competencia_cognitiva"

    id_competencia_cognitiva = db.Column(
        db.Integer, 
        nullable=False, 
        primary_key=True
    )
    competencia = db.Column(db.String(1024), nullable=False)

    def __init__(
        self, 
        id_competencia_cognitiva,
        competencia
    ):
        self.id_competencia_cognitiva = id_competencia_cognitiva
        self.competencia = competencia

class CognitiveCompetenceSchema(ma.Schema):
    class Meta:
        fields = (
            'id_competencia_cognitiva',
            'competencia'
        )

cognitive_competence_schema = CognitiveCompetenceSchema()
cognitive_competences_schema = CognitiveCompetenceSchema(many=True)
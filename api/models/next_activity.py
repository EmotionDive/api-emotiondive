from .. import db, ma 
from .activity import Activity

class NextActivity(db.Model):
    """ Activity model to retrieve the activities following activity """
    __tablename__ = "actividad_siguiente"

    id_actividad = db.Column(
        db.Integer, 
        db.ForeignKey('actividad.id_actividad'), 
        nullable=False, 
        primary_key=True
    )

    id_actividad_siguiente = db.Column(
        db.Integer, 
        db.ForeignKey('actividad.id_actividad'), 
        nullable=False
    )

    actividad = db.relationship(
        "Activity", 
        backref=db.backref(
            "actividad_origen", 
            uselist=False, 
        ),
        foreign_keys=[id_actividad],
    )

    actividad_siguiente = db.relationship(
        "Activity", 
        backref=db.backref(
            "actividad_siguiente", 
            uselist=False, 
        ),
        foreign_keys=[id_actividad_siguiente],
    )

    def __init__(self, id_actividad, id_actividad_siguiente):
        self.id_actividad = id_actividad
        self.id_actividad_siguiente = id_actividad_siguiente

class NextActivitySchema(ma.Schema):
    class Meta:
        fields = (
            'id_actividad',
            'id_actividad_siguiente'
        )

next_activity_schema = NextActivitySchema()
next_activities_schema = NextActivitySchema(many=True)
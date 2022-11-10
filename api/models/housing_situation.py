from .. import db, ma

class HousingSituation(db.Model):
    """ Housing Situation Model for the housing situation options on sign up"""
    __tablename__ = "situacion_habitacional"

    id_situacion_habitacional = db.Column(db.Integer, nullable=False, primary_key=True)
    descripcion = db.Column(db.String(128), nullable=False)

    def __init__(self, id_situacion_habitacional, descripcion):
        self.id_situacion_habitacional = id_situacion_habitacional
        self.descripcion = descripcion
    
class HousingSituationSchema(ma.Schema):
    class Meta:
        fields = ('id_situacion_habitacional', 'descripcion')

housing_situation_schema = HousingSituationSchema()
housing_situations_schema = HousingSituationSchema(many=True)
from .. import db
from ..models.housing_situation import HousingSituation, housing_situation_schema, housing_situations_schema

def get_housing_situations():
    """
    Function to get the housing situation of an user based on an ID
    """
    try:
        hs_catalog = HousingSituation.query.all()
        return housing_situations_schema.dump(hs_catalog), 200
    except Exception as e:
        response_obj = {
            "status": "fail",
            "message": str(e)
        }
        return response_obj, 401
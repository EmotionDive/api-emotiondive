from .. import db
from ..models.cognitive_competence import (
    CognitiveCompetence,
    cognitive_competence_schema,
    cognitive_competences_schema
)
from ..models.activity import (
    Activity,
    activity_schema,
    activities_schema
)
from ..models.next_activity import (
    NextActivity,
    next_activity_schema,
    next_activities_schema
)

def get_competence_activities(competences):
    try:
        competence_activities = []
        for competence in competences:
            # We query the 'competencia_cognitiva' table to get the ID of the given ompetences
            competence_query = CognitiveCompetence.query.filter_by(competencia=competence).one()
            competence_id = competence_query.id_competencia_cognitiva

            # We query the "actividad" table to get all the activities that belong to the same competence
            activities_query = Activity.query.filter_by(id_competencia_cognitiva=competence_id).all()
            activities = activities_schema.dump(activities_query)

            activities_list = []

            for activity in activities:
                
                next_activity_query = NextActivity.query.get(activity['id_actividad'])
                
                if next_activity_query != None:
                    aux_activity_obj = {
                        "activity": activity,
                        "next_activity": next_activity_query.id_actividad_siguiente
                    }
                else:
                    aux_activity_obj = {
                        "activity": activity,
                        "next_activity": None
                    }
                
                activities_list.append(aux_activity_obj)

            aux_response_obj = {
                "competence": competence,
                "activities": activities_list
            }
            
            competence_activities.append(aux_response_obj)

        response_obj = {
            "status": "success",
            "competence_activities": competence_activities
        }
        return response_obj, 200
    
    except Exception as e:
        response_obj ={
            "Status" : "fail",
            "message" : str(e)
        } 
        return response_obj, 400
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

def get_competence_activities(competences):
    try:
        competence_activities = []
        for competence in competences:
            # We query the 'competencia_cognitiva' table to get the ID of the given ompetences
            competence_query = CognitiveCompetence.query.filter_by(competencia=competence).one()
            competence_id = competence_query.id_competencia_cognitiva

            # We query the "actividad" table to get all the activities that belong to the same competence
            activities_query = Activity.query.filter_by(id_competencia_cognitiva=competence_id).all()
            aux_obj = {competence: activities_schema.dump(activities_query)}
            
            competence_activities.append(aux_obj)

        response_obj = {
            "status": "success",
            "competence_activities": competence_activities,
            "message": "Competences successfully registered."
        }
        return response_obj, 200
    except Exception as e:
        response_obj ={
            "Status" : "fail",
            "message" : str(e)
        } 
        return response_obj, 400
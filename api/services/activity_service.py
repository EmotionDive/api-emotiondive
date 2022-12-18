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
from ..models.contains import (
    Contains,
    contains_schema,
    multiple_contains_schema
)

## Helper functions

def activities_by_competence(competence):
    try:
        # We query the 'competencia_cognitiva' table to get the ID of the given ompetences
        competence_query = CognitiveCompetence.query.filter_by(competencia=competence).one()
        competence_id = competence_query.id_competencia_cognitiva

        # We query the "actividad" table to get all the activities that belong to the same competence
        activities_query = Activity.query.filter_by(id_competencia_cognitiva=competence_id).all()
        activities = activities_schema.dump(activities_query)

        competence_activities = []

        for activity in activities:
            competence_activities.append(activity['id_actividad'])

        return competence_activities
    except Exception as e:
        print(str(e))
        return []

def activities_completed_by_user(username):
    try:
        activities_by_user_query = Contains.query.with_entities(
            Contains.id_actividad,
            Contains.progreso
        ).filter_by(
            username_usuario=username
        ).all()

        progress_by_user = multiple_contains_schema.dump(activities_by_user_query)
        activities_completed = []

        for activity_progress in progress_by_user:
            activities_query = Activity.query.with_entities(
                Activity.numero_realizaciones
            ).filter_by(
                id_actividad=activity_progress['id_actividad']
            ).one()

            if activities_query.numero_realizaciones == activity_progress['progreso']:
                activities_completed.append(activity_progress['id_actividad'])

        return activities_completed
    except Exception as e:
        print(str(e))
        return []


## Functions that return responses for the endpoints

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


def get_competences_finished(username, competences, test_flag=False):
    user_completed = activities_completed_by_user(username)
    competences_state = {}

    for competence in competences:
        competence_activities = activities_by_competence(competence)

        if set(user_completed) == set(competence_activities):
            competences_state[competence] = {
                "status": "complete"
            }
        else:
            competences_state[competence] = {
                "status": "incomplete"
            }

    if test_flag == True:
        response_obj = {
            "status": "success",
            "competences_state": competences_state,
            "test_ready_flag": all(value ==  "complete" for value in competences_state.values())
        }
    else:
        response_obj = {
            "status": "success",
            "competences_state": competences_state
        }
    
    return response_obj, 200

def get_user_completed_activities(username):
    try:
        response_obj = {
            "status": "success",
            "activities_by_user": activities_completed_by_user(username)
        }
        return response_obj, 200
    except Exception as e:
        response_obj ={
            "Status" : "fail",
            "message" : str(e)
        } 
        return response_obj, 400 
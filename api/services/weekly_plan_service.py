from .. import db
from datetime import datetime, timedelta
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
from ..models.weekly_plan import (
    WeeklyPlan,
    weekly_plan_schema,
    weekly_plans_schema
)
from ..models.contains import (
    Contains,
    contains_schema,
    multiple_contains_schema
)

def create_weekly_plan(username, activities):
    try:
        deadline = datetime.today() + timedelta(days=7)
        new_weekly_plan = WeeklyPlan(username_usuario=username, fecha_limit=deadline)
        db.session.add(new_weekly_plan)
        db.session.commit()

        plan_query = WeeklyPlan.query.filter_by(
            username_usuario=username
        ).order_by(
            WeeklyPlan.fecha_limit.desc()
        ).first()

        for activity_id in activities:
            new_plan_content = Contains(
                username_usuario=username, 
                id_plan_semanal=plan_query.id_plan_semanal, 
                id_actividad=activity_id, 
                progreso=0
            )
            db.session.add(new_plan_content)
            db.session.commit()

        response_obj = {
            "status": "success",
            "deadline": str(deadline),
            "message": "New weekly plan successfully created."
        }
        return response_obj, 200
    except Exception as e:
        response_obj ={
            "Status" : "fail",
            "message" : str(e)
        } 
        return response_obj, 400

def get_weekly_plan(username):
    # We query the 'plan_semanal' table and get the most recent plan of an user
    plan_query = WeeklyPlan.query.filter_by(
        username_usuario=username
    ).order_by(
        WeeklyPlan.fecha_limit.desc()
    ).first()

    # We query the 'contiene' table and get the associations of the weekly plan
    plan_content_query = Contains.query.filter_by(
        id_plan_semanal=plan_query.id_plan_semanal
    ).all()
    plan_content_list = multiple_contains_schema.dump(plan_content_query)

    activities_list = []

    for content in plan_content_list:
        activity_query = Activity.query.get(content['id_actividad'])
        activity_dict = activity_schema.dump(activity_query)

        competence_query = CognitiveCompetence.query.get(activity_dict['id_competencia_cognitiva'])
        competence_dict = cognitive_competence_schema.dump(competence_query)



        activity_obj = {
            "actividad": activity_dict, 
            "competence": competence_dict['competencia'],
            "progreso": content['progreso'],
            "done_flag": True if activity_dict['numero_realizaciones'] == content['progreso'] else False
        }
        activities_list.append(activity_obj)
    
    response_obj = {
        "status": "success",
        "deadline": str(plan_query.fecha_limit),
        "activities": activities_list
    }
    return response_obj, 200

def increase_activity_progress(username, activity_id):
    plan_query = WeeklyPlan.query.filter_by(
        username_usuario=username
    ).order_by(
        WeeklyPlan.fecha_limit.desc()
    ).first()

    plan_activity = Contains.query.get((
        username, 
        activity_id, 
        plan_query.id_plan_semanal
    ))
    plan_activity.progreso = plan_activity.progreso + 1
    db.session.commit()

    response_obj = {
        "status": "success",
        "message": "Activity progress saved."
    }
    return response_obj, 200
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
    pass
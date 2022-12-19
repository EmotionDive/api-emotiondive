from flask import request
from flask_restful import Resource
from ..services.weekly_plan_service import *

class WeeklyPlan(Resource):
    """
    Resource to manipulate the weekly plan of an user
    """
    def post(self, username):
        activities = request.json.get("activities", None)
        return create_weekly_plan(username, activities)
    
    def get(self, username):
        return get_weekly_plan(username)

class ActivityProgress(Resource):
    """
    Resource to update the activity progress within the weekly plan of an user
    """
    def post(self, username, activity_id):
        return increase_activity_progress(username, activity_id)

class ActivityRealization(Resource):
    """
    Resource to update and get activities' last realization during a weekly plan
    """
    def post(self, username, activity_id):
        return update_last_realization(username, activity_id)

    def get(self, username, activity_id):
        return get_last_realization(username, activity_id)


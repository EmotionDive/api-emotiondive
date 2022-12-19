from .. import db
from datetime import date
from ..models.user import User, user_schema
from ..models.competences_selection import (
    CompetencesSelection, 
    competences_selection_schema, 
    competence_selection_schema
)
from ..models.cognitive_competence import (
    CognitiveCompetence, 
    cognitive_competence_schema, 
    cognitive_competences_schema
)

def register_competences(username, competences):
    try:
        selection_date = date.today()
        for selected_competence in competences:
            competence = CognitiveCompetence.query.filter_by(competencia=selected_competence).one()
            new_competence_selected = CompetencesSelection(username, competence.id_competencia_cognitiva, selection_date)
            db.session.add(new_competence_selected)
            db.session.commit()
        response_obj = {
            "status": "success",
            "message": "Competences successfully registered."
        }
        return response_obj, 200
    except Exception as e:
        response_obj ={
            "Status" : "fail",
            "message" : str(e)
        } 
        return response_obj, 400

def get_actual_competences(username):
    try:
        selection_query = CompetencesSelection.query.filter_by(
            username_usuario=username
        ).order_by(
            CompetencesSelection.fecha.desc()
        ).limit(2)

        recent_selection = competences_selection_schema.dump(selection_query)
        competences = []
        for selected_competence in recent_selection:
            competence_query = CognitiveCompetence.query.get(selected_competence['id_competencia_cognitiva'])
            competences.append(competence_query.competencia)
        response_obj = {
            "status": "success",
            "selected_competences": competences,
        }
        return response_obj, 200
    except Exception as e:
        response_obj ={
            "Status" : "fail",
            "message" : str(e)
        } 
        return response_obj, 400

def get_undone_competences(username):
    try:
        # We get all the competences that the user has done and store them in a list
        selection_query = CompetencesSelection.query.filter_by(username_usuario=username).all()
        competences_finished = competences_selection_schema.dump(selection_query)

        done = []
        for competence in competences_finished:
            aux_query = CognitiveCompetence.query.get(competence['id_competencia_cognitiva'])
            done.append(aux_query.competencia)

        # We get all the competences available in the database
        competences_query =  CognitiveCompetence.query.all()
        existing_competences = cognitive_competences_schema.dump(competences_query)

        available = []
        for competence in existing_competences:
            available.append(competence['competencia'])

        # We return the competences that are not in 'done'
        response_obj = {
            "status": "success",
            "selected_competences": [elem for elem in available if elem not in done],
            "message": "Competences successfully registered."
        }
        return response_obj, 200
    except Exception as e:
        response_obj ={
            "Status" : "fail",
            "message" : str(e)
        } 
        return response_obj, 400

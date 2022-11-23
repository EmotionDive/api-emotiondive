from .. import db
from ..models.test import Test, test_schema, tests_schema
from datetime import date
from ..common.statistics_cases_utils import *
from ..common.skill_grade_utils import *

def save_test_IE(answers, username):
    """
    Function to save the grade of the cognitive competence based on the ID
    """
    try:
        test_date = date.today()
        answers_changed = get_grade(answers)
        final_grade_autoconocimiento = autoconocimiento_grade(answers_changed)
        final_grade_autoregulacion = autoregulacion_grade(answers_changed)
        final_grade_empatia = empatia_grade(answers_changed)
        final_grade_autoeficiencia = autoeficacia_grade(answers_changed)
        
        new_test = Test(
            username, 
            test_date, 
            final_grade_autoconocimiento, 
            final_grade_autoeficiencia, 
            final_grade_autoregulacion, 
            final_grade_empatia
        )
        db.session.add(new_test)
        db.session.commit()
        response_obj = {
            "status": "success",
            "message": "Test saved successfully."
        }
        return response_obj, 200

    except Exception as e:
        response_obj ={
            "Status" : "fail",
            "message" : str(e)
        } 
        return response_obj, 400

def get_statistics(username):
    """
    Function to retrieve the skills' proficiency and a message according to a range
    """
    try:    
        test_query = Test.query.filter_by(username_usuario=username).order_by(Test.fecha.desc()).limit(2)
        recent_tests = tests_schema.dump(test_query)
        skills = ['autoconocimiento', 'autoregulacion', 'autoeficacia', 'empatia']
        response_obj = []

        for test in recent_tests:
            aux_obj = {}

            aux_obj['date'] = test['fecha']
            for skill in skills:
                aux_obj[skill] = {}
                aux_obj[skill]['grade'] = test[skill]
                aux_obj[skill]['message'] = defining_grades_autoconocimiento(test[skill])
            
            response_obj.append(aux_obj)

        return response_obj, 200
    except Exception as e:
        response_obj ={
            "Status" : "fail",
            "message" : str(e)
        } 
        return response_obj, 400
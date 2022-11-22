from .. import db
from ..models.statistics_IE import *
from ..controllers import user_controller 
from ..models import test
from datetime import date


def defining_grades_autoconocimiento(final_grade_autoconocimiento):
    message_autoconocimiento = "lorem"
    "Caso autoconocimiento"
    if final_grade_autoconocimiento > 85:
        message_autoconocimiento = "Felicidades, esta subescala indica que tienes un gran nivel de autoconocimiento, eres una persona dinámica, abierta al trato con los demás, habla de que tienes un entorno familiar sano que es abierto a la expresión de emociones, perseverante en los objetivos que te propones, no solo eso, tienes un grado de habilidades metacognitivas, es decir que tus forma de aprender y mejorar estrategias de aprendizaje, son pan comido para ti!, sigue así."
    elif final_grade_autoconocimiento> 40 and final_grade_autoconocimiento<85:
        message_autoconocimiento ="Tienes una gran area de mejora en tu autoconocimiento y tus competencias metacognitivas, quizá tienes dificultad para el trato con las démas personas, algunas veces esta relacionada esta situación con tu entorno en el que te desenvuelves. Realiza las actividades de manera honesta, cuanto mas avances veras tu mejora, recuerda que todo es un proceso y tu continuas avanzando, por último tus competencias metacognitivas mejoraran a la par asi que recorramos juntos el camino."
    elif final_grade_autoconocimiento < 40:
        message_autoconocimiento ="El autoconocimiento es complejo, tienes dificultades para ser una persona dinámica, abierta al trato con otras personas, quizá tu entonrno dificulta la expresión de tus emociones, es un indicativo de una familia desestructurada, pero no te preocupes, todos tenemos desafios, se te apoyara en este viaje, por que queremos que estes bien, comencemos este viaje y mejoremos juntos!!. "
    return message_autoconocimiento

def defining_grades_autoregulacion(final_grade_autoregulacion):
    message_autoregulacion = "lorem"
    if final_grade_autoregulacion > 85:
        message_autoregulacion = "Increible!, esta subescala indica que tienes un gran control y manejo de tus emociones, ademas de controlar tus impulsos."
    elif final_grade_autoregulacion> 40 and final_grade_autoregulacion<85:
        message_autoregulacion ="Parece que tienes la oportunidad de mejorar en tu control y manejo emocional, quizá tengas problemas al controlar los impulsos que sientes, sin embargo, siempre podemos mejorar."
    elif final_grade_autoregulacion < 40:
        message_autoregulacion ="La autoregulación refleja el control y manejo emocional, tus resultados revelan que puede ser complicado para ti las reacciones ante los sucesos, no te desanimes, hagamos juntos este viaje y podras mejorar en tu control emocional."
    return message_autoregulacion

def defining_grades_autoeficiencia(final_grade_autoeficiencia):
    "Caso autoeficiencia"
    message_autoeficiencia = "lorem"
    if final_grade_autoeficiencia > 85:
        message_autoeficiencia = "La autoeficiencia se entiende como las expectativas que el sujeto desarrolla para conseguir objetivos personales y grupales. Tu calificación refleja una gran perseverancia y escrupulosidad, tienes una gran apertura mental para los aspectos intelectuales y culturales."
    elif final_grade_autoeficiencia> 40 and final_grade_autoeficiencia<85:
        message_autoeficiencia ="La autoeficiencia se entiende como las expectativas que el sujeto desarrolla para conseguir objetivos, tienes una buena autoregulación y eres capaz de autoinstruirte en distintos temas que son de tu interes, recuerda, siempre puedes mejorar, sigue así!"
    elif final_grade_autoeficiencia < 40:
        message_autoeficiencia ="La autoeficiencia se entiende como las expectativas que el sujeto desarrolla para conseguir objetivos, tus resultados muestran que te es complicado el autoregularte y autoinstruirte, pero haciendo uso de las actividades mejoraras la capacidad de autoregularte y autoinstruirte, trabaja duro y logremos juntos tus metas!."
    return message_autoeficiencia

def defining_grades_empatia(final_grade_empatia):
    "Caso empatia"
    message_empatia = "lorem"
    if final_grade_empatia > 85:
        message_empatia = "Felicidades! la calificación que has obtenido refleja que eres una persona que sabe entender y comprender las emociones y sentimientos de los demás. Indica que eres una persona extrovertida, cooperativa y coordial, con una buena actitud para el aprendizaje."
    elif final_grade_empatia> 40 and final_grade_empatia<85:
        message_empatia ="Tienes la capacidad de entender las emociones de las demas personas, comprenderlas, quizá tienes la capacidad de ser una persona extrovertida, cooperativa y coordial, aunque puede que llegues a presentar dificultades al momento de comprender las emociones que tienes con los demas o el colaborar con ciertas personas que salen de tu entorno."
    elif final_grade_empatia < 40:
        message_empatia ="Vaya, no te desanimes, todos empezamos desde un punto, tus resultados reflejan que te es muy complicado coomprender las emociones de otra persona, quizá no eres una persona muy cooperativa y coordial, sin embargo, te apoyaremos en este viaje y lograras desarrollar tu empatia!."
    return message_empatia

def get_grade(answers):
    "Changing the value of the answers based on the CIE grades"
    for x in range(len(answers)):
        if answers[x]== 1:
            answers[x] = 5
        elif answers[x]==2:
            answers[x] = 4
        elif answers[x]==4:
            answers[x] = 2
        elif answers[x]==1:
            answers[x] = 5   
    return(answers)

def autoconocimiento_grade(answers_changed):
    answers_autoconocimiento = []
    sum_grade=0
    "Appending the index of the questions to list of competence"
    answers_autoconocimiento.append(answers_changed[8])
    answers_autoconocimiento.append(answers_changed[16])
    answers_autoconocimiento.append(answers_changed[18])
    answers_autoconocimiento.append(answers_changed[20])
    answers_autoconocimiento.append(answers_changed[21])
    answers_autoconocimiento.append(answers_changed[22])
    answers_autoconocimiento.append(answers_changed[26])
    answers_autoconocimiento.append(answers_changed[33])
    answers_autoconocimiento.append(answers_changed[37])
    answers_autoconocimiento.append(answers_changed[41])
    answers_autoconocimiento.append(answers_changed[44])
    answers_autoconocimiento.append(answers_changed[45])
    answers_autoconocimiento.append(answers_changed[47])
    answers_autoconocimiento.append(answers_changed[49])
    answers_autoconocimiento.append(answers_changed[51])
    answers_autoconocimiento.append(answers_changed[52])
    for iteration in answers_autoconocimiento:
        sum_grade+= iteration
    final_grade = (100*sum_grade)/80
    return final_grade

def autoregulacion_grade(answers_changed):
    answers_autoregulacion = []
    sum_grade=0
    "Autoregulacion"
    answers_autoregulacion.append(answers_changed[3])
    answers_autoregulacion.append(answers_changed[12])
    answers_autoregulacion.append(answers_changed[19])
    answers_autoregulacion.append(answers_changed[23])
    answers_autoregulacion.append(answers_changed[24])
    answers_autoregulacion.append(answers_changed[28])
    answers_autoregulacion.append(answers_changed[29])
    answers_autoregulacion.append(answers_changed[38])
    answers_autoregulacion.append(answers_changed[42])
    answers_autoregulacion.append(answers_changed[53])
    answers_autoregulacion.append(answers_changed[55])
    for iteration in answers_autoregulacion:
        sum_grade+= iteration
    final_grade = (100*sum_grade)/55
    return final_grade

def autoeficiencia_grade(answers_changed):
    answers_autoeficiencia = []
    final_grade=0
    "Autoeficacia"
    answers_autoeficiencia.append(answers_changed[1])
    answers_autoeficiencia.append(answers_changed[4])
    answers_autoeficiencia.append(answers_changed[6])
    answers_autoeficiencia.append(answers_changed[9])
    answers_autoeficiencia.append(answers_changed[31])
    answers_autoeficiencia.append(answers_changed[35])
    answers_autoeficiencia.append(answers_changed[46])
    answers_autoeficiencia.append(answers_changed[48])
    answers_autoeficiencia.append(answers_changed[50])
    answers_autoeficiencia.append(answers_changed[54])
    for iteration in answers_autoeficiencia:
        final_grade+= iteration
    return final_grade

def empatia_grade(answers_changed):
    answers_empatia = []
    final_grade=0
    "Empatia"
    answers_empatia.append(answers_changed[5])
    answers_empatia.append(answers_changed[7])
    answers_empatia.append(answers_changed[10])
    answers_empatia.append(answers_changed[13])
    answers_empatia.append(answers_changed[14])
    answers_empatia.append(answers_changed[25])
    answers_empatia.append(answers_changed[30])
    answers_empatia.append(answers_changed[39])
    answers_empatia.append(answers_changed[43])
    for iteration in answers_empatia:
        final_grade+=iteration
    return final_grade


def get_statics_IE(answers, username):
    "Function to get the grade of the cognitive competence based on the ID"
    try:
        today = date.today()
        Date_test  = today.strftime("%d/%m/%Y")
        Statics_catalog = StaticSchema.query.all()
        answers_changed = get_grade(answers)
        final_grade_autoconocimiento = autoconocimiento_grade(answers_changed)
        final_grade_autoregulacion = autoregulacion_grade(answers_changed)
        final_grade_empatia = empatia_grade(answers_changed)
        final_grade_autoeficiencia = autoeficiencia_grade(answers_changed)
        message_autoconocimiento = defining_grades_autoconocimiento(final_grade_autoconocimiento)
        message_autoregulacion = defining_grades_autoregulacion(final_grade_autoregulacion)
        message_autoeficacia = defining_grades_autoeficiencia(final_grade_autoeficiencia)
        message_empatia = defining_grades_empatia(final_grade_empatia)
        new_test = Test(username, Date_test, final_grade_autoconocimiento, final_grade_autoeficiencia, final_grade_autoregulacion, final_grade_empatia, message_autoconocimiento,message_autoeficacia,message_autoregulacion,message_empatia)
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
        return response_obj, 401

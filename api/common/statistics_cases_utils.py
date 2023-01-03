def defining_grades_autoconocimiento(final_grade_autoconocimiento):
    ## Caso autoconocimiento
    message_autoconocimiento = "lorem"
    if final_grade_autoconocimiento > 85:
        message_autoconocimiento = "Felicidades, esta subescala indica que tienes un gran nivel de **autoconocimiento**, eres una persona dinámica, abierta al trato con los demás, habla de que tienes un entorno familiar sano que es abierto a la expresión de emociones, perseverante en los objetivos que te propones, no solo eso, tienes un grado de habilidades metacognitivas, es decir que tus forma de aprender y mejorar estrategias de aprendizaje, son pan comido para ti!, sigue así."
    elif final_grade_autoconocimiento> 40 and final_grade_autoconocimiento<85:
        message_autoconocimiento ="Tienes una gran area de mejora en tu **autoconocimiento** y tus competencias metacognitivas, quizá tienes dificultad para el trato con las démas personas, algunas veces esta relacionada esta situación con tu entorno en el que te desenvuelves. Realiza las actividades de manera honesta, cuanto mas avances veras tu mejora, recuerda que todo es un proceso y tu continuas avanzando, por último tus competencias metacognitivas mejoraran a la par asi que recorramos juntos el camino."
    elif final_grade_autoconocimiento < 40:
        message_autoconocimiento ="El **autoconocimiento es complejo**, tienes dificultades para ser una persona dinámica, abierta al trato con otras personas, quizá tu entonrno dificulta la expresión de tus emociones, es un indicativo de una familia desestructurada, pero no te preocupes, todos tenemos desafíos, se te apoyara en este viaje, por que queremos que estes bien, comencemos este viaje y mejoremos juntos!!. "
    return message_autoconocimiento

def defining_grades_autoregulacion(final_grade_autoregulacion):
    ## Caso autoregulacion 
    message_autoregulacion = "lorem"
    if final_grade_autoregulacion > 85:
        message_autoregulacion = "Increible!, la subescala de **autorregulación** indica que tienes un gran control y manejo de tus emociones, ademas de controlar tus impulsos."
    elif final_grade_autoregulacion> 40 and final_grade_autoregulacion<85:
        message_autoregulacion ="Parece que tienes la oportunidad de mejorar en tu control y manejo emocional (**autorregulación**), quizá tengas problemas al controlar los impulsos que sientes, sin embargo, siempre podemos mejorar."
    elif final_grade_autoregulacion < 40:
        message_autoregulacion ="La **autoregulación** refleja el control y manejo emocional, tus resultados revelan que puede ser complicado para ti las reacciones ante los sucesos, no te desanimes, hagamos juntos este viaje y podras mejorar en tu control emocional."
    return message_autoregulacion

def defining_grades_autoeficacia(final_grade_autoeficacia):
    ## Caso autoeficiencia
    message_autoeficacia = "lorem"
    if final_grade_autoeficacia > 85:
        message_autoeficacia = "La **autoeficiencia** se entiende como las expectativas que el sujeto desarrolla para conseguir objetivos personales y grupales. Tu calificación refleja una gran perseverancia y escrupulosidad, tienes una gran apertura mental para los aspectos intelectuales y culturales."
    elif final_grade_autoeficacia> 40 and final_grade_autoeficacia<85:
        message_autoeficacia ="La **autoeficiencia** se entiende como las expectativas que el sujeto desarrolla para conseguir objetivos, tienes una buena autoregulación y eres capaz de autoinstruirte en distintos temas que son de tu interes, recuerda, siempre puedes mejorar, sigue así!"
    elif final_grade_autoeficacia < 40:
        message_autoeficacia ="La **autoeficiencia** se entiende como las expectativas que el sujeto desarrolla para conseguir objetivos, tus resultados muestran que te es complicado el autoregularte y autoinstruirte, pero haciendo uso de las actividades mejoraras la capacidad de autoregularte y autoinstruirte, trabaja duro y logremos juntos tus metas!."
    return message_autoeficacia

def defining_grades_empatia(final_grade_empatia):
    ## Caso empatia
    message_empatia = "lorem"
    if final_grade_empatia > 85:
        message_empatia = "¡Muy bien en **Empatía**! La calificación que has obtenido refleja que eres una persona que sabe entender y comprender las emociones y sentimientos de los demás. Indica que eres una persona extrovertida, cooperativa y coordial, con una buena actitud para el aprendizaje."
    elif final_grade_empatia >= 40 and final_grade_empatia <=85:
        message_empatia ="Tienes la capacidad de entender las emociones de las demás personas, comprenderlas (**empatía**), quizá tienes la capacidad de ser una persona extrovertida, cooperativa y coordial, aunque puede que llegues a presentar dificultades al momento de comprender las emociones que tienes con los demás o el colaborar con ciertas personas que salen de tu entorno."
    elif final_grade_empatia < 40:
        message_empatia ="Vaya, no te desanimes, todos empezamos desde un punto, tus resultados reflejan que te es muy complicado coomprender las emociones de otra persona, quizá no eres una persona muy cooperativa y coordial, sin embargo, te apoyaremos en este viaje y lograras desarrollar tu **empatía**!."
    return message_empatia
def get_grade(answers):
    """
    Changing the value of the answers based on the CIE grades
    """
    for x in range(len(answers)):
        if answers[x]== 1:
            answers[x] = 5
        elif answers[x]==2:
            answers[x] = 4
        elif answers[x]==4:
            answers[x] = 2
        elif answers[x]==5:
            answers[x] = 1   
    return(answers)

def autoconocimiento_grade(answers_changed):
    ## Appending the index of the questions to list of competence
    answers_autoconocimiento = []
    sum_grade=0
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
    if final_grade <= 20:
        return 0
    else:
        return final_grade

def autoregulacion_grade(answers_changed):
    ## Autoregulacion
    answers_autoregulacion = []
    sum_grade=0
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
    if final_grade <= 20:
        return 0
    else:
        return final_grade

def autoeficacia_grade(answers_changed):
    ## Autoeficacia
    answers_autoeficacia = []
    final_grade=0
    answers_autoeficacia.append(answers_changed[1])
    answers_autoeficacia.append(answers_changed[4])
    answers_autoeficacia.append(answers_changed[6])
    answers_autoeficacia.append(answers_changed[9])
    answers_autoeficacia.append(answers_changed[31])
    answers_autoeficacia.append(answers_changed[35])
    answers_autoeficacia.append(answers_changed[46])
    answers_autoeficacia.append(answers_changed[48])
    answers_autoeficacia.append(answers_changed[50])
    answers_autoeficacia.append(answers_changed[54])
    for iteration in answers_autoeficacia:
        final_grade+= iteration
    final_grade = (100*final_grade)/50
    if final_grade <= 20:
        return 0
    else:
        return final_grade

def empatia_grade(answers_changed):
    ## Empatia
    answers_empatia = []
    final_grade=0
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
    final_grade = (100*final_grade)/45
    if final_grade <= 20:
        return 0
    else:
        return final_grade


DROP DATABASE IF EXISTS emotion_dive;
CREATE DATABASE emotion_dive;
USE emotion_dive;
CREATE TABLE situacion_habitacional
(
	id_situacion_habitacional INTEGER AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(128) NOT NULL
);

CREATE TABLE competencia_cognitiva
(
	id_competencia_cognitiva INTEGER AUTO_INCREMENT PRIMARY KEY,
    competencia VARCHAR(1024) NOT NULL
);

CREATE TABLE usuario 
(
    username VARCHAR(512) NOT NULL PRIMARY KEY,
    correo VARCHAR(128) NOT NULL,
    nombre VARCHAR(128) NOT NULL,
    edad INTEGER,
    sexo VARCHAR(12),
    estado_civil VARCHAR(128),
    id_situacion_habitacional INTEGER,
    active_account VARCHAR(32) NOT NULL,
    FOREIGN KEY (id_situacion_habitacional) 
    REFERENCES situacion_habitacional (id_situacion_habitacional),
    UNIQUE(correo)
);

CREATE TABLE test
(
	username_usuario VARCHAR(512) NOT NULL,
    fecha DATETIME NOT NULL,
    autoconocimiento INTEGER NOT NULL,
    autoregulacion INTEGER NOT NULL,
    autoeficacia INTEGER NOT NULL,
    empatia INTEGER NOT NULL,
    FOREIGN KEY (username_usuario) 
    REFERENCES usuario (username),
    PRIMARY KEY(username_usuario, fecha)
);

CREATE TABLE actividad
(
	id_actividad INTEGER AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(126) NOT NULL,
    descripcion VARCHAR(1024) NOT NULL,
    instrucciones VARCHAR(1024) NOT NULL,
    beneficios VARCHAR(1024) NOT NULL,
    numero_realizaciones INTEGER NOT NULL,
    tiempo_estimado TIME NOT NULL,
    id_competencia_cognitiva INTEGER NOT NULL,
    advertencia_bandera BOOLEAN NOT NULL,
    offline_bandera BOOLEAN NOT NULL,
    FOREIGN KEY (id_competencia_cognitiva) 
    REFERENCES competencia_cognitiva (id_competencia_cognitiva)
);

CREATE TABLE realiza
(
	username_usuario VARCHAR(512) NOT NULL,
	id_actividad INTEGER NOT NULL,
    FOREIGN KEY (username_usuario) 
    REFERENCES usuario (username),
    FOREIGN KEY (id_actividad) 
    REFERENCES actividad (id_actividad),
    PRIMARY KEY(username_usuario, id_actividad)
);

CREATE TABLE competencia_cognitiva_selec
(
	username_usuario VARCHAR(512) NOT NULL,
    id_competencia_cognitiva INTEGER NOT NULL,
    fecha DATETIME NOT NULL,
    FOREIGN KEY (username_usuario) 
    REFERENCES usuario (username),
    PRIMARY KEY(username_usuario, id_competencia_cognitiva)
);

CREATE TABLE plan_semanal
(
	id_plan_semanal INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
	username_usuario VARCHAR(512) NOT NULL,
    fecha_limit DATETIME NOT NULL,
    FOREIGN KEY (username_usuario) 
    REFERENCES usuario (username)
);

CREATE TABLE contiene
(
	username_usuario VARCHAR(512) NOT NULL,
    id_actividad INTEGER NOT NULL,
    id_plan_semanal INTEGER NOT NULL,
    progreso INTEGER NOT NULL,
    FOREIGN KEY (username_usuario) 
    REFERENCES usuario (username),
    FOREIGN KEY (id_actividad) 
    REFERENCES actividad (id_actividad),
	FOREIGN KEY (id_plan_semanal) 
    REFERENCES plan_semanal (id_plan_semanal),
    PRIMARY KEY(username_usuario, id_actividad)
    
);

CREATE TABLE actividad_siguiente
(
    id_actividad INTEGER NOT NULL PRIMARY KEY,
    id_actividad_siguiente INTEGER NOT NULL,
    FOREIGN KEY (id_actividad) 
    REFERENCES actividad (id_actividad),
    FOREIGN KEY (id_actividad_siguiente) 
    REFERENCES actividad (id_actividad)
);

## Inserts de catalogos

## Inserts para catalogo de situacion habitacional

INSERT 
INTO situacion_habitacional (id_situacion_habitacional, descripcion) 
VALUES (1, "Casa propia");

INSERT 
INTO situacion_habitacional (id_situacion_habitacional, descripcion) 
VALUES (2, "Casa prestada");

INSERT 
INTO situacion_habitacional (id_situacion_habitacional, descripcion) 
VALUES (3, "Departamento propio");

INSERT 
INTO situacion_habitacional (id_situacion_habitacional, descripcion) 
VALUES (4, "Departamento rentado");

## Inserts para catalogo de competencias cognitivas

INSERT 
INTO competencia_cognitiva (id_competencia_cognitiva, competencia) 
VALUES (1, "Empatia");

INSERT 
INTO competencia_cognitiva (id_competencia_cognitiva, competencia) 
VALUES (2, "Autoconocimiento");

INSERT 
INTO competencia_cognitiva (id_competencia_cognitiva, competencia) 
VALUES (3, "Autorregulacion");

INSERT 
INTO competencia_cognitiva (id_competencia_cognitiva, competencia) 
VALUES (4, "Autoeficacia");

## Inserts para catalogo de actividades

# Empatía
INSERT
INTO actividad
VALUES (1,"Empatía vs Antipatía y Simpatía", 
"Aprende a diferenciar entre los conceptos de empatía, simpatía y antipatía.\nSe te presentaran las definiciones de empatía, simpatía y antipatía y podrás conocer un poco más al respecto.",
"Debes de realizar esta actividad una vez durante un plan semanal.\nLa retroalimentación se dará al terminar la actividad, donde conocerás las definiciones de dichos conceptos.",
"Al completar esta actividad tendrás un mejor entendimiento de las diferencias entre empatía, simpatía y antipatía.",
1,
'00:10:00',
1,
FALSE,
TRUE
);

INSERT
INTO actividad
VALUES (2,"Empatía vs Antipatía y Simpatía 2", 
"Pondrás a prueba tu entendimiento respecto a los conceptos de empatía, simpatía y antipatía.\nSe te presentaran distintos escenarios donde deberás identificar si dicho escenario, muestra una actitud empática, simpática o antipática.",
"Debes de realizar esta actividad una vez durante un plan semanal.\nLa retroalimentación se dará según al ir avanzando a traves de los escenarios.",
"Al completar esta actividad habrás puesto a prueba tu capacidad para identificar comportamientos empáticos, simpáticos y antipáticos.",
1,
'00:15:00',
1,
FALSE,
TRUE
);

INSERT
INTO actividad
VALUES (3,"Conversaciones empáticas", 
"Aprende a mostrar empatía hacia otras personas mediante conversaciones basadas en distintos escenarios.\nSe te presentara un escenario con el cual se simulara una conversación y podrás elegir las respuesta que te parezca correcta dada la situación.",
"Debes de realizar esta actividad dos veces durante distintos planes semanales.\nLa retroalimentación se ira dando en la misma actividad a medida que progreses.",
"Al completar esta actividad tendrás un mejor entendimiento del rol que juega la empatía cuando interactuamos con otras personas.",
1,
'00:10:00',
1,
FALSE,
TRUE
);

INSERT
INTO actividad
VALUES (4,"Reconocimiento de entornos", 
"Reconoce las situaciones por las que pueden estar pasando distintas personas y las emociones que experimentan durante dichas situaciones.",
"Debes de realizar esta actividad dos veces en tu plan semanal y la retroalimentación se dará al terminar la actividad.",
"Al completar esta actividad podrás reconocer de mejor manera como situaciones ajenas a ti afectan a otras personas.",
2,
'00:15:00',
1,
FALSE,
TRUE
);

INSERT
INTO actividad
VALUES (5,"Comentarios empáticos", 
"Aprende a mostrar empatía hacia otras personas a traves de las redes sociales para comunicarte de una forma más efectiva.\nSe te presentaran distintos escenarios donde se simulara un publicación en línea y un comentario que carece de empatía, tu te encargaras de reescribir dicho comentario, de una manera en tu consideres más empática.",
"Debes de realizar esta actividad una vez durante un plan semanal.\nLa retroalimentación se dará una vez que completes la actividad, podrás ver un comentario para dicha situación donde se muestra empatía.",
"Al completar esta actividad tendrás un mejor entendimiento de como comunicarte empáticamente en escenarios que involucren interacción por medio de redes sociales.",
1,
'00:15:00',
1,
TRUE,
TRUE
);

INSERT 
INTO actividad_siguiente
VALUES (1,2);

INSERT 
INTO actividad_siguiente
VALUES (2,3);

INSERT 
INTO actividad_siguiente
VALUES (3,4);

INSERT 
INTO actividad_siguiente
VALUES (4,5);

# Autoconocimiento
INSERT
INTO actividad
VALUES (6,"Identificación de emociones faciales", 
"Interpreta las emociones que representan las imágenes en función de las 5 emociones que representa MATEA (Miedo, Alegría, Tristeza, Enojo y Afecto).\nEn cada una de ellas deberás de aprender a reconocer tus propias gesticulaciones con las presentadas, desarrollando tu capacidad de reconocer emociones en otros, con el propósito de posteriormente ser capaz de identificar tus propias emociones.",
"Se te presentaran 5 imágenes, cada una de ellas representa una emoción distinta, tu trabajo será identificar cual imagen representa la emoción correcta, recuerda que trabajaremos bajo la tabla de MATEA, la cual contempla 5 emociones (Miedo, Alegría, Tristeza, Enojo y Afecto).\nDeberás de realizar esta actividad 5 veces.",
"Al realizar este ejercicio con imágenes de rostros que representan el estado emocional, serás capaz de reconocer las emociones que presentan los demás en distintas situaciones del día a día.",
5,
'00:10:00',
2,
FALSE,
TRUE
);

INSERT
INTO actividad
VALUES (7,"Emociones en la vida diaria", 
"Descubre si eres capaz de distinguir que emociones comúnmente se desprenden en diferentes contextos.\nA partir de varias situaciones que se te plantearan, deberás elegir que emoción podría desprenderse ante esa situación (Miedo, Alegría, Tristeza, Enojo, Afecto).",
"Deberás de realizar esta actividad tres veces y se te retroalimentará en cada respuesta que des.",
"Podrás reconocer qué emociones normalmente se generan en situaciones comunes y, cuando te pasen en la vida real, razones qué es lo que estas sintiendo y tomes como experiencia lo que identificaste en esta actividad.",
3,
'00:10:00',
2,
FALSE,
TRUE
);

INSERT
INTO actividad
VALUES (8,"¿Asigno bien mis emociones?", 
"Averigua si eres capaz de identificar qué emociones sientes en este momento o sentiste en el pasado.\nTendrás que redactar algo que estés viviendo en estos momentos o algo que te impactó mucho en el pasado (alguna situación o problemática) y, con base en eso, elige qué emociones sentiste en ese momento y después responde cuál es la razón posible de que hayas sentido esa emoción.",
"Deberás de realizar esta actividad 5 veces.",
"Al realizar este ejercicio con situaciones propias lograrás ser más consciente de que existen esas emociones en ti y, sobre todo, razonarás el porqué sientes esas emociones.",
5,
'00:15:00',
2,
FALSE,
TRUE
);

INSERT
INTO actividad
VALUES (9,"Reconocimiento de emociones", 
"Identifica como tu muestras tus emociones y cuales son las similitudes y diferencias con la forma en la que otras personas muestran emociones.",
"Debes de realizar esta actividad una vez en tu plan semanal y sera una actividad totalmente autoreflexiva.",
"Al completar esta actividad podrás reconocer de mejor manera la forma en que muestras tus emociones.",
1,
'00:15:00',
2,
FALSE,
TRUE
);

INSERT
INTO actividad
VALUES (10,"¿Qué me gusta?", 
"Realmente ¿sabemos que nos gusta?, muchas veces olvidamos que nos gusta de nosotros mismos…\nLlevamos una vida tan a prisa que no nos cuestionamos acerca de lo que nos gusta, incluso lo que nos desagrada, cuestionarnos acerca de lo que nos agrada y desagrada de nosotros mismos, nos ayuda a realizar estrategias para mejorar, sin olvidar que también es importante aceptarnos por quienes somos.",
"Se te presentara una lista de opciones con respecto a lo que te gusta de ti, en donde deberás de seleccionar al menos una opción con respecto a algún atributo que posees, de igual manera deberás de seleccionar alguna opción que englobe algo que no te gusta de ti, por último define una estrategia que puedas realizar con tus acciones para mejorar en esos aspectos.\nDeberás de realizar esta actividad 2 veces.",
"Al realizar esta actividad desarrollaras la capacidad de reconocer tus virtudes, pero también cuestiones que quizá no sean de tu agrado, además de desarrollar estrategias para obtener resultados en aquello que consideras un área de oportunidad en ti.",
3,
'00:10:00',
2,
FALSE,
TRUE
);

INSERT 
INTO actividad_siguiente
VALUES (6,7);

INSERT 
INTO actividad_siguiente
VALUES (7,8);

INSERT 
INTO actividad_siguiente
VALUES (8,9);

INSERT 
INTO actividad_siguiente
VALUES (9,10);

# Autoregulación
INSERT
INTO actividad
VALUES (11,"¿Cómo me autorregulo?", 
"Descubre cómo analizas situaciones en tu entorno y cómo es que actúas frente a ellas.\nSe te presentarán varios ejemplos de situaciones que pueden ocurrir en tu vida diaria y deberás elegir cómo es que tu actuarías frente a dichas situaciones.",
"Deberás de realizar esta actividad una vez y se te retroalimentará en cada respuesta que des.",
"Al completar esta actividad podrás observar cómo es que te autoregulas en este punto y comprender mejor tu área de mejora.",
1,
'00:15:00',
3,
FALSE,
TRUE
);

INSERT
INTO actividad
VALUES (12,"Estrategias de Autorregulación", 
"Aprende cuáles son las diferentes estrategias de autorregulación que puedes usar a tu favor.\nSe te mostrarán 2 estrategias que pueden serte de utilidad para lograr autoregularte frente a diversas situaciones de tu vida diaria.",
"Deberás de realizar esta actividad 1 vez en tu plan semanal.",
"Al completar esta actividad conocerás cómo funcionan estas estrategias y cómo puedes aplicarlas.",
1,
'00:10:00',
3,
FALSE,
TRUE
);

INSERT
INTO actividad
VALUES (13,"Aprende a usar las estrategias", 
"Descubre cómo aplicar las estrategias de distracción y reevaluación en diversas situaciones.\nAhora que conoces las estrategias, se te plantearan situaciones para ambas estrategias y deberás elegir la acción que represente de mejor manera el uso de la estrategia.",
"Deberás de realizar esta actividad 2 veces en tu plan semanal y se te retroalimentará a medida que contestes.",
"Al completar esta actividad habrás identificado el cómo se usa cada estrategia en situaciones ejemplo.",
2,
'00:15:00',
3,
FALSE,
TRUE
);

INSERT
INTO actividad
VALUES (14,"Usa las estrategias en ti", 
"Analiza situaciones de tu vida diaria e identifica cómo es que podrías usar alguna de las estrategias a tu favor.\nDeberás redactar una situación que te haya sucedido en el pasado o en tu presente y posteriormente, elegir una de las estrategias y escribir cómo la aplicarías para regularte emocionalmente.",
"Deberás de realizar esta actividad 4 veces en tu plan semanal para ejercitar el uso de las estrategias.",
"Al completar esta actividad tendrás más comprensión de las estrategias y te será más fácil llevarlas a tu vida diaria en tus situaciones futuras.",
4,
'00:15:00',
3,
FALSE,
TRUE
);

INSERT
INTO actividad
VALUES (15,"Autorregulación a prueba", 
"Después de practicar tu autorregulación, llegó el momento de ponerte aprueba con diversas situaciones.\nSe te plantearan nuevas situaciones donde podrás seleccionar un modo de actuar usando cualquier de las dos estrategias.",
"Deberás de realizar 2 veces esta actividad y en cada ocasión para completarse deberás de haber obtenido un puntaje perfecto.",
"Al completar esta actividad habrás puesto a prueba lo aprendido en las anteriores actividades y lograrás una comprensión mas profunda de la autorregulación.",
2,
'00:15:00',
3,
FALSE,
TRUE
);

INSERT 
INTO actividad_siguiente
VALUES (11,12);

INSERT 
INTO actividad_siguiente
VALUES (12,13);

INSERT 
INTO actividad_siguiente
VALUES (13,14);

INSERT 
INTO actividad_siguiente
VALUES (14,15);

# Autoeficacia
INSERT
INTO actividad
VALUES (16,"Decisiones razón-emoción", 
"Desarrollar autoeficacia, conlleva el reconocer las capacidades que tenemos individualmente y aprender a tener confianza en ellas para lograr los objetivos que se tienen a largo, mediano y corto plazo.\nSe presentaran escenarios en los que se deberá de diferenciar entre razón () y emoción, tendrás que elegir entre lo que es una emoción o la razón dentro del escenario.",
"Debes realizar esta actividad un mínimo de dos veces durante distintos planes semanales, en esta actividad deberá realizar una lista con las razones para la toma de una decisión, realizando una comparativa de las actividades para decidir finalmente que decisión tomara.",
"Completar esta actividad refuerza el diferenciar entre un hecho que ocurre a partir de mis capacidades, reconocer como tomar la mejor decisión en función de mis capacidades y no tomar decisiones en función de las emociones.",
2,
'00:05:00',
4,
FALSE,
TRUE
);

INSERT
INTO actividad
VALUES (17,"Decisiones propias “Razón & Emoción”", 
"Reforzara los conocimientos adquiridos en la actividad Decisiones “Razón & Emoción”, se trabajara en la toma de decisiones de manera asertiva, descomponiendo las razones y emociones.",
"Deberas plantear una situación propia que tenga dos posibles opciones, posteriormente deberás descomponer ambas opciones en razones y emociones.",
"Completando esta actividad será capaz de descomponer situaciones que se presentan en el día a día en razón y emociones, aprendiendo a actuar en función de tus capacidades y generando un buen balance.",
2,
'00:10:00',
4,
FALSE,
TRUE
);

INSERT
INTO actividad
VALUES (18,"¿Qué harías ante estas situaciones?", 
"Reflexiona en tu forma de actuar con las situaciones.\nSiempre es bueno conocer más puntos de vista diferentes a lo que consideramos correcto. \nMuchas veces perdemos la oportunidad de tomar una mejor decisión por auto sabotearnos de distintas maneras, la mejor decisión no es fácil de tomar pero siempre trae beneficios.",
"Debes de realizar esta actividad tres veces en tu plan semanal. \nLa retroalimentación se da a medida que progreses en la actividad.",
"Podrás tener más experiencia en cuanto a como lidiar con tus emociones en ciertas situaciones, ya sea para usarlas a tu favor o evitar el autosabotaje.",
3,
'00:10:00',
4,
FALSE,
TRUE
);

INSERT
INTO actividad
VALUES (19,"Éxitos y Fracasos", 
"Reconoce tus éxitos y fracasos, aprende de cada uno de ellos y se consciente de ellos.\nDeberás de escribir el último éxito que recuerdes y el último fracaso para después contestar unas preguntas respecto a cada una de los eventos.",
"Deberás realizar esta actividad 3 veces en tu plan semanal.",
"Al completar esta actividad tendrás una mejor comprensión de tus éxitos y fracasos, ayudándote a ver cómo es que las emociones juegan un papel en ambos eventos.",
3,
'00:15:00',
4,
FALSE,
TRUE
);

INSERT
INTO actividad
VALUES (20,"Éxitos y Fracasos 2", 
"¿Qué pasaría si donde tuviste éxito hubieras fallado?, o al revés. Descúbrelo en esta actividad.\nDeberás de plantearte la anterior pregunta tanto en tus éxitos como en tus fracasos y contestar unas preguntas con respecto a cada situación.",
"Deberás realizar esta actividad 3 veces en tu plan semanal.",
"Realizando esta actividad, desarrollarás la capacidad de ver el fracaso como una oportunidad, no como un problema, sino como algo beneficioso y conocer que el éxito no siempre es constante, así se gestionara el fracaso y el éxito en el día a día.",
3,
'00:15:00',
4,
FALSE,
FALSE
);

INSERT 
INTO actividad_siguiente
VALUES (16,17);

INSERT 
INTO actividad_siguiente
VALUES (17,18);

INSERT 
INTO actividad_siguiente
VALUES (18,19);

INSERT 
INTO actividad_siguiente
VALUES (19,20);
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
    progreso VARCHAR(512) NOT NULL,
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
VALUES (3, "Autoregulacion");

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

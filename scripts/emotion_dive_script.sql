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
    advertencia_bandera VARCHAR(64) NOT NULL,
    offline_bandera VARCHAR(64) NOT NULL,
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



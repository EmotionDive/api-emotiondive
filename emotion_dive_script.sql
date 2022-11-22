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
    descripcion VARCHAR(1024) NOT NULL
);

CREATE TABLE usuario 
(
    username VARCHAR(512) NOT NULL PRIMARY KEY,
    correo VARCHAR(128) NOT NULL,
    edad INTEGER,
    sexo VARCHAR(12),
    estado_civil VARCHAR(128),
    id_situacion_habitacional INTEGER,
    active_account VARCHAR(3) NOT NULL,
    FOREIGN KEY (id_situacion_habitacional) 
    REFERENCES situacion_habitacional (id_situacion_habitacional),
    UNIQUE(correo)
);

CREATE TABLE test
(
	username_usuario VARCHAR(512) NOT NULL,
    fecha DATE NOT NULL,
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

CREATE TABLE usuario_password
(
	username_usuario VARCHAR(512) NOT NULL PRIMARY KEY,
	password_usuario CHAR(128) NOT NULL,
    FOREIGN KEY (username_usuario) 
    REFERENCES usuario (username)
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
    FOREIGN KEY (username_usuario) 
    REFERENCES usuario (username),
    PRIMARY KEY(username_usuario, id_competencia_cognitiva)
);

CREATE TABLE plan_semanal
(
	username_usuario VARCHAR(512) NOT NULL PRIMARY KEY,
    fecha_limit DATETIME NOT NULL,
    FOREIGN KEY (username_usuario) 
    REFERENCES usuario (username)
);

CREATE TABLE contiene
(
	username_usuario VARCHAR(512) NOT NULL,
    id_actividad INTEGER NOT NULL,
    progreso VARCHAR(512) NOT NULL,
    FOREIGN KEY (username_usuario) 
    REFERENCES usuario (username),
    FOREIGN KEY (id_actividad) 
    REFERENCES actividad (id_actividad),
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

INSERT 
INTO situacion_habitacional (id_situacion_habitacional, descripcion) 
VALUES (1, "Casa propia");
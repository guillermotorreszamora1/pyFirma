CREATE TYPE estado_solicitud AS ENUM('en_proceso','aceptada');
CREATE TABLE solicitud (
	nombre varchar ,
	nif varchar,
	clave_publica text ,
	fecha timestamp default now(),
	n_serie varchar PRIMARY KEY,
	estado_solicitud estado_solicitud default 'en_proceso'
);
CREATE TABLE certificado (
	nombre varchar ,
	nif varchar,
	n_serie varchar PRIMARY KEY,
	fecha_alta timestamp,
	fecha_baja timestamp,
	certificado text
);

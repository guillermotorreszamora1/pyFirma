from sqlalchemy import create_engine,text
import datetime
db_engine = create_engine("postgresql:///pyfirma",echo=False)
def get_nombre(n_serie):
    data = list(db_engine.execute(text("select nombre from solicitud where n_serie=:n_serie and estado_solicitud='en_proceso'"),
    {'n_serie':str(n_serie)}))
    return data[0][0]
def get_nif(n_serie):
    data = list(db_engine.execute(text("select nif from solicitud where n_serie=:n_serie and estado_solicitud='en_proceso'"),
    {'n_serie':str(n_serie)}))
    return data[0][0]
def aceptar_solicitud(n_serie):
    db_engine.execute(text("update solicitud set estado_solicitud='aceptada' where n_serie=:n_serie"),{'n_serie':str(n_serie)})
def anadir_certificado(nombre,nif,n_serie,cert_pem):
    fecha_alta = datetime.datetime.utcnow()
    fecha_baja = datetime.datetime.utcnow() + datetime.timedelta(days=3650)
    db_engine.execute(text("insert into certificado(nombre,nif,n_serie,fecha_alta,fecha_baja,certificado) values (:nombre,:nif,:n_serie,"
    ":fecha_alta,:fecha_baja,:certificado)"),
    {'nombre':nombre,'nif':nif,'n_serie':n_serie,'fecha_alta':fecha_alta,
    'fecha_baja':fecha_baja,'certificado':cert_pem})
def get_clave_publica(n_serie):
    data = list(db_engine.execute(text("select clave_publica from solicitud"
        " where n_serie=:n_serie"),{'n_serie':str(n_serie)}))
    return data[0][0]

#SOLO INTERFACES CON SQL
from sqlalchemy import create_engine,text
db_engine = create_engine("postgresql:///pyfirma",echo=False)
def registrar_solicitud(nombre,nif,clave_publica,n_serie):
    db_engine.execute(text("insert into solicitud(nombre,nif,clave_publica,n_serie)"
    " values(:nombre,:nif,:clave_publica,:n_serie)"),{"nombre":nombre,"nif":nif,
    "clave_publica":clave_publica,"n_serie":n_serie})
def descargar_cert(n_serie):
    result = list(db_engine.execute(text("select fecha_baja,certificado from certificado where n_serie=:n_serie"),
    {"n_serie":str(n_serie)}))
    if result == []:
        return [],[]
    return result[0][0],result[0][1]

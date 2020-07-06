import base64
import requests
import json
import model.signature
API_ENDPOINT =
def solicitud(nombre,nif,clave):
    base64_nombre = base64.b64encode(nombre.encode('UTF-8')).decode()
    data = {"name":base64_nombre,"nif":nif,"public_key":clave}
    r = requests.post(url = API_ENDPOINT+"solicitud/",json=data)
    print(r.text)
    json_response = json.loads(r.text)
    try:
        model.signature.check_json(r.text)
        assert(data['name']==json_response['response']['name'])
        assert(data['nif']==json_response['response']['nif'])
        assert(data['public_key']==json_response['response']['public_key'])
        return json_response['response']['serial_number']
    except:
        return -1
def descarga(user):
    data = {"n_serie":user.n_serie}
    r = requests.post(url = API_ENDPOINT+"descarga/",json=data)
    print(r.text)
    json_response = json.loads(r.text)
    model.signature.check_json(r.text)
    model.crypto.check_cert(json_response['response']['cert'],user.n_serie)
    user.save_cert(json_response['response']['cert'])

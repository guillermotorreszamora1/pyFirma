# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify,request,render_template,redirect
import server.cripto
import base64
import server.database
import hashlib
import json
import datetime
URL_PREFIX ='/proyecto_PKI'
app = Flask(__name__,template_folder='templates')
@app.route(URL_PREFIX+'/',methods=["GET","POST"])
def principal():
	return "Hello"
@app.route(URL_PREFIX+'/solicitud',methods=["POST","GET"])
@app.route(URL_PREFIX+'/solicitud/',methods=["POST","GET"])
def solicitud():
	n_serie = cripto.get_serial_number()
	nombre = base64.b64decode(request.json['name'].encode()).decode('UTF-8')
	request.json['serial_number'] = n_serie
	database.registrar_solicitud(nombre,request.json['nif'],request.json['public_key'],n_serie)
	signature = cripto.sign_json(json.dumps(request.json).encode())
	json_response = {'response':request.json,'signature':signature}
	return json_response
@app.route(URL_PREFIX+'/descarga/',methods=["POST","GET"])
def descarga():
	date, cert = server.database.descargar_cert(request.get_json()['n_serie'])

	if date==[]:
		json_data =  json.dumps({'Error':'El certificado no existe'})
	if datetime.datetime.now()>date:
		json_data =  json.dumps({'Error':'El certificado ha cadudado'})
	json_data = json.dumps({'cert':cert})
	signature = cripto.sign_json(json_data.encode())
	json_response = {'response':{'cert':cert},'signature':signature}
	return json_response

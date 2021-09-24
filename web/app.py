from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__, template_folder='templates')

variables_list = ['PH','Temperatura','Humedad Tierra','Humedad Aire','Distancia','Luz Solar']

@app.route('/listar-agrocadenas',methods=['GET'])
def listarSensores():
    agrocadenas_list = requests.get('http://18.217.185.186:5000/agrocadenas').json()
    return render_template('listarAgrocadenas.html', agrocadenas=agrocadenas_list)
    
@app.route('/crear-agrocadena',methods=['GET'])
def crearSensor():
    return render_template('crearSensor.html', variables=variables_list)

@app.route('/guardar-agrocadena',methods=['POST'])
def guardarSensor():
    sensor = dict(request.values)
    sensor['precio'] = int(sensor['precio'])
    requests.post('http://18.217.185.186:5000/agrocadena',json=sensor)
    return(listarSensores())

app.run(host='0.0.0.0',port=8000)
from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__, template_folder='templates')

variables_list = ['PH','Temperatura','Humedad Tierra','Humedad Aire','Distancia','Luz Solar']

@app.route('/listarSensores',methods=['GET'])
def listarSensores():
    sensores_list = requests.get('http://localhost:5000/tipoSensores').json()
    return render_template('listarSensores.html', sensores=sensores_list)
    
@app.route('/crearSensor',methods=['GET'])
def crearSensor():
    return render_template('crearSensor.html', variables=variables_list)

@app.route('/guardarSensor',methods=['POST'])
def guardarSensor():
    sensor = dict(request.values)
    sensor['precio'] = int(sensor['precio'])
    requests.post('http://localhost:5000/tipoSensores',json=sensor)
    return(listarSensores())

app.run(host='0.0.0.0',port=8000)
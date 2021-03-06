from flask import Flask, jsonify, request, render_template, url_for
import requests
from werkzeug.utils import redirect

app = Flask(__name__, template_folder='templates')

@app.route('/listar-agrocadenas',methods=['GET'])
def listarAgrocadenas():
    agrocadenas_list = requests.get('http://18.217.185.186:5000/agrocadenas').json()
    return render_template('listarAgrocadenas.html', agrocadenas=agrocadenas_list)
    
@app.route('/crear-agrocadena',methods=['GET'])
def crearAgrocadena():
    return render_template('crearAgrocadena.html')

@app.route('/guardar-agrocadena',methods=['POST'])
def guardarAgrocadena():
    agrocadena=dict(request.values)
    agrocadena['id'] = int(agrocadena['id'])
    print(agrocadena)
    requests.post('http://18.217.185.186:5000/agrocadena',json=agrocadena)
    return render_template('agrocadenaCreada.html')

app.run(host='0.0.0.0',port=8000)
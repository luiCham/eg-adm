from flask import Flask, request
from flask_cors import CORS
from controllers.Agrocadena import Agrocadena

app = Flask(__name__)
CORS(app)

@app.route('/agrocadenas',methods=['GET'])
def getAll():
    return (Agrocadena.list())

@app.route('/agrocadena',methods=['POST'])
def postOne():
    body = request.json
    return (Agrocadena.create(body))

app.run(host='0.0.0.0',port=5000)
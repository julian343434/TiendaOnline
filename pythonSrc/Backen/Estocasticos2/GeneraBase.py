from flask import Flask, jsonify, request,send_file
import Controlador as Controlador
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 
CORS(app, origins='http://localhost:7201')



def hello():

    name = request.args.get('name')

    if name is None:
        text = 'Hello!'

    else:
        text = 'Hello ' + name + '!'

    return text

@app.route('/json-data', methods=['GET'])
def json():
    name = request.args.get('name')
    return Controlador.leer_actualizar_json(name)

if __name__ == '__main__':
    app.run(debug=True, port=7201)
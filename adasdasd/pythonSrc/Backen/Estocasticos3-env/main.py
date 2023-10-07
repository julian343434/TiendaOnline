from fastapi import FastAPI, Request
import json

def leer_actualizar_json(archivo):
    aux = archivo + ".json"
    with open(aux, 'r') as f:
        datos = json.load(f)
    return datos

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hola mundo"}

@app.get("/json-data")
def json_data(request: Request):
    name = request.query_params.get('name')
    return leer_actualizar_json(name)

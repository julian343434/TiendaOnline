import json
def leer_actualizar_json(archivo):
            aux=archivo+".json"
            with open(aux, 'r') as f:
                datos = json.load(f)
                return datos



from Ranking import Ranking
from BaseDatos import BaseDatos

import time
import json


def dict_to_json(data, filename):
    json_data = json.dumps(data)
    with open(filename, 'w') as file:
        file.write(json_data)


def generate_users_json(self, output_file):
        users_json = {}
        for persona, info in self.usuarios.items():
            user_data = {}
            user_data['ranking'] = info['ranking'].pageRage
            user_data['zapatos'] = {}
            for zapato, metadata in info.items():
                if zapato != 'ranking':
                    user_data['zapatos'][zapato] = metadata

            users_json[persona] = user_data

        with open(output_file, 'w') as file:
            json.dump(users_json, file, indent=4)


if __name__ == '__main__':
    # Base de datos
    personas = ["hermes", "carlos", "deivid", "marlon", "yeiner"]
    usuarios = {}

    for persona in personas:
        # Crear la base de datos y el ranking para cada persona
        database = BaseDatos()
        database.genera_base_data()
        rankin = Ranking(database.data)

        # Agregar nodos (artículos de zapatos)
        usuarios[persona] = []
        for zapato, info in database.data.items():
            metadata = info['metadata']
            zapato_id = metadata['id']
            zapato_imagen = metadata['imagen']
            zapato_nombre = metadata['nombre']
            nodo = f"zapato{zapato_id}"
            rankin.graph.add_node(nodo, imagen=zapato_imagen, nombre=zapato_nombre)

        # Agregar aristas (enlaces entre artículos)
        for zapato, info in database.data.items():
            for enlace in info['enlaces']:
                rankin.graph.add_edge(zapato, enlace)

        # Generar el ranking para cada persona
        rankin.generadorRanking()

        # Actualizar la información de los zapatos con el ranking
        for zapato, info in database.data.items():
            ranking_zapato = rankin.pageRage.get(zapato)
            if ranking_zapato is not None:
                usuarios[persona].append({
                    'id': info['metadata']['id'],
                    'imagen': info['metadata']['imagen'],
                    'nombre': info['metadata']['nombre'],
                    'ranking': ranking_zapato
                })

        # Ordenar los objetos por el valor de ranking
        usuarios[persona] = sorted(usuarios[persona], key=lambda x: x['ranking'], reverse=True)




    dict_to_json(usuarios,"data_final.json")

        
        ################################################################
           


    # Calcular el PageRan
    #rankin.generadorRanking()

    # Búsquedas o clics del usuario (ejemplo)
    busquedas_usuario = []

    #rankin.agrega_valor_ranking(busquedas_usuario)

    #rankin.generate_sorted_results_json("hermes.json")


    #####################################
    def leer_actualizar_json(archivo):
            with open(archivo, 'r') as f:
                datos = json.load(f)
                return datos
    '''
    while True:
        # Ejemplo de cómo leer y actualizar un archivo JSON
        db = leer_actualizar_json("../db.json")
        historialUser =[]
        for historial in db['user']:
            ##historialUser.append({'id': historial['nombre'], 'historial': historial['historial']})
            historialUser.append({
                "nombre":historial['name'],
                "historial":historial['historial']
                })
        historialUser=historialUser[2:]
        for usuarioH in historialUser:
            for usuario in usuarios:
                usuario['rankin'].agrega_valor_ranking(usuarioH['historial'])
                usuario['rankin'].generate_sorted_results_json(f"../{usuario['nombre']}.json")
    
    '''
        ##with open(archivo, 'w') as f:
        ##    json.dump(datos, f, indent=4)


    ##loop principal
    ##while True:
        



    ##    time.sleep(10)




    

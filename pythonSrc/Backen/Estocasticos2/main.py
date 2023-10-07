from Ranking import Ranking
from BaseDatos import BaseDatos

import time
import json

if __name__ == '__main__':

# Base de datos
    personas = ["hermes", "carlos", "deivid", "marlon", "yeiner"]
    usuarios = [
        {
            "nombre": persona,
            "database": BaseDatos(),
            "rankin": None
        }
        for persona in personas
    ]

    # Generar base de datos y ranking para cada usuario
    for usuario in usuarios:
        usuario["database"].genera_base_data()
        usuario["rankin"] = Ranking(usuario["database"].data)

        # Agregar nodos (artículos de zapatos)
        for zapato, info in usuario["database"].data.items():
            usuario["rankin"].graph.add_node(zapato)

        # Agregar aristas (enlaces entre artículos)
        for zapato, info in usuario["database"].data.items():
            for enlace in info['enlaces']:
                usuario["rankin"].graph.add_edge(zapato, enlace)
        # Genera el rankin para cada usuario

        usuario['rankin'].generadorRanking()
        usuario['rankin'].generate_sorted_results_json(f"{usuario['nombre']}.json")


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




    

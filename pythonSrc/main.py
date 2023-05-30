from Ranking import Ranking
from BaseDatos import BaseDatos


if __name__ == '__main__':
<<<<<<< HEAD
    # Base de datos ficticia de zapatos con enlaces
=======
    #Base de datos
>>>>>>> 80e4ad1 (se agrego la base de datos y se probo el codigo de python)
    database=BaseDatos()
    database.genera_base_data()
    rankin=Ranking(database.data)

    # Agregar nodos (artículos de zapatos)
    for zapato, info in database.data.items():
        rankin.graph.add_node(zapato)

    # Agregar aristas (enlaces entre artículos)
    for zapato, info in database.data.items():
        for enlace in info['enlaces']:
            rankin.graph.add_edge(zapato, enlace)

    # Calcular el PageRank
    rankin.generadorRanking()

    # Búsquedas o clics del usuario (ejemplo)
    busquedas_usuario = ['zapato2', 'zapato3','zapato4', 'zapato5', 'zapato6']

    rankin.agrega_valor_ranking(busquedas_usuario)

    rankin.generate_sorted_results_json("hermes.json")


    

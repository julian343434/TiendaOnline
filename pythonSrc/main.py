from Ranking import Ranking
from BaseDatos import BaseDatos

# Ejemplo de uso
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

    # Actualizar los valores de PageRank en función de las búsquedas o clics del usuario
    for zapato in busquedas_usuario:
        if zapato in rankin.pageRage:
            rankin.pageRage[zapato] += 0.1

    # Mostrar los resultados
    sorted_results = sorted(rankin.pageRage.items(), key=lambda x: x[1], reverse=True)
    for zapato, rank in sorted_results:
        print(f'{zapato}: {rank}')

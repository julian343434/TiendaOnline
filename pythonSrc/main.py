from Ranking import Ranking


# Ejemplo de uso
if __name__ == '__main__':
    # Base de datos ficticia de zapatos con enlaces
    database = {
        'zapato1': {'enlaces': ['zapato2', 'zapato3']},
        'zapato2': {'enlaces': ['zapato1', 'zapato3']},
        'zapato3': {'enlaces': ['zapato1']}
    }
    rankin=Ranking(database)

    # Agregar nodos (artículos de zapatos)
    for zapato, info in database.items():
        rankin.graph.add_node(zapato)

    # Agregar aristas (enlaces entre artículos)
    for zapato, info in database.items():
        for enlace in info['enlaces']:
            rankin.graph.add_edge(zapato, enlace)

    # Calcular el PageRank
    rankin.generadorRanking()

    # Búsquedas o clics del usuario (ejemplo)
    busquedas_usuario = ['zapato2', 'zapato3']

    # Actualizar los valores de PageRank en función de las búsquedas o clics del usuario
    for zapato in busquedas_usuario:
        if zapato in rankin.pageRage:
            rankin.pageRage[zapato] += 0.1

    # Mostrar los resultados
    sorted_results = sorted(rankin.pageRage.items(), key=lambda x: x[1], reverse=True)
    for zapato, rank in sorted_results:
        print(f'{zapato}: {rank}')

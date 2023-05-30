import networkx as nx
import json

class Ranking :
    def __init__(self,dataBase) -> None:
        self.graph = nx.DiGraph()
        self.dataBase= dataBase
        self.pageRage=None

    #Genera el ranking de los items
    def generadorRanking(self):
        self.pageRage = nx.pagerank(self.graph)    
    
    #Actualiza el ranking de los items con las entradas de los usuarios
    def agrega_valor_ranking(self,busquedas_usuario) -> None:
        for zapato in busquedas_usuario:
            if zapato in self.pageRage:
                self.pageRage[zapato] += 0.1

    #Genera un JSON  de los items rankeados
    def generate_sorted_results_json(self,output_file):
        sorted_results = sorted(self.pageRage.items(), key=lambda x: x[1], reverse=True)
        sorted_json = []
        for zapato, rank in sorted_results:
            sorted_json.append({ "zapato": zapato, "rank": rank })
        with open(output_file, 'w') as file:
            json.dump(sorted_json, file)

















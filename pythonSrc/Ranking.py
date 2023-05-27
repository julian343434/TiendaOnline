import networkx as nx

class Ranking :
    def __init__(self,dataBase) -> None:
        self.graph = nx.DiGraph()
        self.dataBase= dataBase
        self.pageRage=None

    def generadorRanking(self):
        self.pageRage = nx.pagerank(self.graph)    
        


















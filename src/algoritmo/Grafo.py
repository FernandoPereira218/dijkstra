import sys
 
class Grafo(object):
    def __init__(self, vertices, dic_grafo):
        self.vertices = vertices
        self.grafo = self.criar_grafo(vertices, dic_grafo)
        
    def criar_grafo(self, vertices, dic_grafo):
        grafo = {}
        for vertice in vertices:
            grafo[vertice] = {}
        
        grafo.update(dic_grafo)
        
        for vertice, aresta in grafo.items():
            for vertice_adjacente, valor in aresta.items():
                if grafo[vertice_adjacente].get(vertice, False) == False:
                    grafo[vertice_adjacente][vertice] = valor
                    
        return grafo
    
    def get_arestas(self):
        return self.vertices
    
    def get_adjacentes(self, vertices):
        conexoes = []
        for adjacentes in self.vertices:
            if self.grafo[vertices].get(adjacentes, False) != False:
                conexoes.append(adjacentes)
        return conexoes
    
    def valor(self, vertice1, vertice2):
        return self.grafo[vertice1][vertice2]
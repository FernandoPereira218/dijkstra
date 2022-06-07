import sys
 
class Grafo(object):
    def __init__(self, vertices, init_graph):
        self.vertices = vertices
        self.grafo = self.construct_graph(vertices, init_graph)
        
    def construct_graph(self, vertices, init_graph):
        grafo = {}
        for vertice in vertices:
            grafo[vertice] = {}
        
        grafo.update(init_graph)
        
        for vertice, aresta in grafo.items():
            for vertice_adjacente, value in aresta.items():
                if grafo[vertice_adjacente].get(vertice, False) == False:
                    grafo[vertice_adjacente][vertice] = value
                    
        return grafo
    
    def get_nodes(self):
        return self.vertices
    
    def get_outgoing_edges(self, vertices):
        conexoes = []
        for adjacentes in self.vertices:
            if self.grafo[vertices].get(adjacentes, False) != False:
                conexoes.append(adjacentes)
        return conexoes
    
    def value(self, vertice1, vertice2):
        return self.grafo[vertice1][vertice2]
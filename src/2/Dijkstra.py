import sys
from Grafo import Grafo

class Dijkstra():
    def __init__(self):
        pass


    def dijkstra_algorithm(self, grafo, vertice_inicial):
        vertices_nao_testados = list(grafo.get_nodes())
    
        # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
        menor_caminho = {}
    
        # We'll use this dict to save the shortest known path to a node found so far
        vertices_anteriores = {}
    
        # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
        inf = sys.maxsize
        for vertice in vertices_nao_testados:
            menor_caminho[vertice] = inf
        # However, we initialize the starting node's value with 0   
        menor_caminho[vertice_inicial] = 0
        
        # The algorithm executes until we visit all nodes
        while vertices_nao_testados:
            # The code block below finds the node with the lowest score
            menor_vertice = None
            for vertice in vertices_nao_testados: # Iterate over the nodes
                if menor_vertice == None:
                    menor_vertice = vertice
                elif menor_caminho[vertice] < menor_caminho[menor_vertice]:
                    menor_vertice = vertice
                    
            # The code block below retrieves the current node's neighbors and updates their distances
            adjacentes = grafo.get_outgoing_edges(menor_vertice)
            for ajacente in adjacentes:
                valor = menor_caminho[menor_vertice] + grafo.value(menor_vertice, ajacente)
                if valor < menor_caminho[ajacente]:
                    menor_caminho[ajacente] = valor
                    # We also update the best path to the current node
                    vertices_anteriores[ajacente] = menor_vertice
    
            # After visiting its neighbors, we mark the node as "visited"
            vertices_nao_testados.remove(menor_vertice)
    
        return vertices_anteriores, menor_caminho

    
    def print_result(self, vertices_anteriores, menor_caminho, vertice_inicial, vertice_final):
        path = []
        node = vertice_final
        
        while node != vertice_inicial:
            path.append(node)
            node = vertices_anteriores[node]
    
        # Add the start node manually
        path.append(vertice_inicial)
        
        print("Melhor caminho com valor {}.".format(menor_caminho[vertice_final]))
        print(" -> ".join(reversed(path)))
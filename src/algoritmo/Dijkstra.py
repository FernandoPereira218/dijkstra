import sys
from Grafo import Grafo

class Dijkstra():
    def __init__(self):
        pass


    def algoritmo(self, grafo, vertice_inicial):
        vertices_nao_testados = list(grafo.get_arestas())

        #salvar menor caminho ao longo do algoritmo  
        menor_caminho = {}
    
        #vertices anteriores que formam o menor caminho até uma aresta
        vertices_anteriores = {}
    
        inf = sys.maxsize
        for vertice in vertices_nao_testados:
            menor_caminho[vertice] = inf


        menor_caminho[vertice_inicial] = 0
        
        while vertices_nao_testados:
            menor_vertice = None
            for vertice in vertices_nao_testados:
                if menor_vertice == None:
                    menor_vertice = vertice
                elif menor_caminho[vertice] < menor_caminho[menor_vertice]:
                    menor_vertice = vertice
                    
            
            adjacentes = grafo.get_adjacentes(menor_vertice)
            for ajacente in adjacentes:
                valor = menor_caminho[menor_vertice] + grafo.valor(menor_vertice, ajacente)
                if valor < menor_caminho[ajacente]:
                    menor_caminho[ajacente] = valor
                    
                    vertices_anteriores[ajacente] = menor_vertice
    
            
            vertices_nao_testados.remove(menor_vertice)
    
        return vertices_anteriores, menor_caminho

    
    def resultados(self, vertices_anteriores, menor_caminho, vertice_inicial, vertice_final):
        path = []
        node = vertice_final
        
        while node != vertice_inicial:
            path.append(node)
            node = vertices_anteriores[node]
    
        path.append(vertice_inicial)
        
        print(f"Melhor caminho de {vertice_inicial} até {vertice_final}:")
        print(" -> ".join(reversed(path)))
        print("Valor final: ", menor_caminho[vertice_final])
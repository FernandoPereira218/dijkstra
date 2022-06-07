from Dijkstra import Dijkstra
from Grafo import Grafo
import sys
import os

arquivo = sys.argv[1]
if os.path.exists(arquivo):
    with open(arquivo) as txt:
        linhas = txt.readlines()

    temp = linhas[0].replace('\n', '')
    vertices = temp.split(';')
    print("Vertices ", vertices)

    no_inicial_final = linhas[2].replace('\n', '')
    inicial = no_inicial_final.split(';')[0]
    final = no_inicial_final.split(';')[1]
    novo_grafo = {}
    for v in vertices:
        novo_grafo[v] = {}

    for i in range(4, len(linhas)):
        temp = linhas[i].replace('\n', '').split(';')
        novo_grafo[temp[0]][temp[1]] = int(temp[2])

    print(novo_grafo)

    grafo = Grafo(vertices, novo_grafo)
    dijkstra = Dijkstra()
    vertices_anteriores, menor_caminho = dijkstra.algoritmo(grafo, inicial)
    dijkstra.resultados(vertices_anteriores, menor_caminho, vertice_inicial=inicial, vertice_final=final)
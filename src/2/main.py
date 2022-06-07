from Dijkstra import Dijkstra
from Grafo import Grafo
import sys
import os
# nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]
arquivo = sys.argv[1]
if os.path.exists(arquivo):
    with open(arquivo) as txt:
        linhas = txt.readlines()

    # for line in lines:
    #     temp = line.replace('\n', '')
    #     nodes = temp.split(';')
    #     print(nodes)

    temp = linhas[0].replace('\n', '')
    vertices = temp.split(';')
    print(vertices)

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

    # nodes = ["J", "A", "P", "Q", "B", "C", "E"]
    # init_graph = {}
    # for node in nodes:
    #     init_graph[node] = {}
        
    # init_graph["Reykjavik"]["Oslo"] = 5
    # init_graph["Reykjavik"]["London"] = 4
    # init_graph["Oslo"]["Berlin"] = 1
    # init_graph["Oslo"]["Moscow"] = 3
    # init_graph["Moscow"]["Belgrade"] = 5
    # init_graph["Moscow"]["Athens"] = 4
    # init_graph["Athens"]["Belgrade"] = 1
    # init_graph["Rome"]["Berlin"] = 2
    # init_graph["Rome"]["Athens"] = 2


    # init_graph["J"]["A"] = 5
    # init_graph["J"]["P"] = 6
    # init_graph["J"]["Q"] = 10
    # init_graph["A"]["J"] = 5
    # init_graph["A"]["B"] = 13
    # init_graph["P"]["J"] = 6
    # init_graph["P"]["Q"] = 3
    # init_graph["P"]["B"] = 11
    # init_graph["P"]["C"] = 6
    # init_graph["Q"]["J"] = 10
    # init_graph["Q"]["P"] = 3
    # init_graph["Q"]["B"] = 6
    # init_graph["Q"]["C"] = 4
    # init_graph["B"]["A"] = 13
    # init_graph["B"]["P"] = 11
    # init_graph["B"]["Q"] = 6
    # init_graph["B"]["E"] = 3
    # init_graph["C"]["P"] = 6
    # init_graph["C"]["Q"] = 4
    # init_graph["C"]["E"] = 8
    # init_graph["E"]["B"] = 3
    # init_graph["E"]["C"] = 8

    grafo = Grafo(vertices, novo_grafo)
    dijkstra = Dijkstra()
    #previous_nodes, shortest_path = dijkstra.dijkstra_algorithm(graph, "Reykjavik")
    vertices_anteriores, menor_caminho = dijkstra.dijkstra_algorithm(grafo, inicial)
    #dijkstra.print_result(previous_nodes, shortest_path, start_node="Reykjavik", target_node="Athens")
    dijkstra.print_result(vertices_anteriores, menor_caminho, vertice_inicial=inicial, vertice_final=final)
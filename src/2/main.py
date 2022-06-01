#udacity
from Dijkstra import Dijkstra
from Graph import Graph
# nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]
nodes = ["J", "A", "P", "Q", "B", "C", "E"]
init_graph = {}
for node in nodes:
    init_graph[node] = {}
    
# init_graph["Reykjavik"]["Oslo"] = 5
# init_graph["Reykjavik"]["London"] = 4
# init_graph["Oslo"]["Berlin"] = 1
# init_graph["Oslo"]["Moscow"] = 3
# init_graph["Moscow"]["Belgrade"] = 5
# init_graph["Moscow"]["Athens"] = 4
# init_graph["Athens"]["Belgrade"] = 1
# init_graph["Rome"]["Berlin"] = 2
# init_graph["Rome"]["Athens"] = 2
init_graph["J"]["A"] = 5
init_graph["J"]["P"] = 6
init_graph["J"]["Q"] = 10
init_graph["A"]["J"] = 5
init_graph["A"]["B"] = 13
init_graph["P"]["J"] = 6
init_graph["P"]["Q"] = 3
init_graph["P"]["B"] = 11
init_graph["P"]["C"] = 6
init_graph["Q"]["J"] = 10
init_graph["Q"]["P"] = 3
init_graph["Q"]["B"] = 6
init_graph["Q"]["C"] = 4
init_graph["B"]["A"] = 13
init_graph["B"]["P"] = 11
init_graph["B"]["Q"] = 6
init_graph["B"]["E"] = 3
init_graph["C"]["P"] = 6
init_graph["C"]["Q"] = 4
init_graph["C"]["E"] = 8
init_graph["E"]["B"] = 3
init_graph["E"]["C"] = 8

	
graph = Graph(nodes, init_graph)
dijkstra = Dijkstra()
#previous_nodes, shortest_path = dijkstra.dijkstra_algorithm(graph, "Reykjavik")
previous_nodes, shortest_path = dijkstra.dijkstra_algorithm(graph, "J")
#dijkstra.print_result(previous_nodes, shortest_path, start_node="Reykjavik", target_node="Athens")
dijkstra.print_result(previous_nodes, shortest_path, start_node="J", target_node="E")
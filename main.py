# import graph.py
from graph import Graph

# create a new graph
G = Graph()

# add some nodes and edges
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1, 2)
G.add_edge(2, 3)

# visualize the graph
G.visualize()

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node_id):
        if node_id not in self.nodes:
            self.nodes[node_id] = {}

    def add_edge(self, node1, node2):
        if node1 not in self.nodes:
            self.add_node(node1)
        if node2 not in self.nodes:
            self.add_node(node2)
        self.edges.append((node1, node2))

    def remove_edge(self, node1, node2):
        if (node1, node2) in self.edges:
            self.edges.remove((node1, node2))

    def remove_node(self, node_id):
        if node_id in self.nodes:
            for edge in self.edges[:]:
                if node_id in edge:
                    self.edges.remove(edge)
            del self.nodes[node_id]

    def get_neighbors(self, node_id):
        return list(set([node2 for node1, node2 in self.edges if node1 == node_id] + [node1 for node1, node2 in self.edges if node2 == node_id]))

    def visualize(self):
        nodes_str = '\n'.join([f'  {node_id}' for node_id in self.nodes])
        edges_str = '\n'.join([f'  {node1} --> {node2}' for node1, node2 in self.edges])
        print(f'graph LR\n{nodes_str}\n{edges_str}')

    def __str__(self):
        nodes_str = "\n".join(str(node) for node in self.nodes)
        edges_str = "\n".join(f"{node1} -> {node2}" for node1, node2 in self.edges)
        return f"Nodes:\n{nodes_str}\nEdges:\n{edges_str}"

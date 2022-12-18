class Graph:
    '''
        Graph class represents the graph data structure. 
        It contains a nodes attribute (list) with all the nodes of the graph
    '''

    def __init__(self, nodes=None):
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes

    def add_node(self, node):
        ''' Ad a new node to the grpah'''
        self.nodes.append(node)

    def find_node(self, value):
        '''Return True if the node with the given value exists. Otherwise it returns False'''
        for node in self.nodes:
            if node.value == value:
                return node
        return None

    def add_edge(self, value1, value2, weight=1):
        '''Add a new edge between two nodes'''
        node1 = self.find_node(value1)
        node2 = self.find_node(value2)
        # Kruskal's algorithm works with undirected graphs so
        # we just store only the one direction of the edge, the other is implied
        if (node1 is not None) and (node2 is not None):
            node1.add_neighboor((node2, weight))
        else:
            print("Error: One or more nodes were not found")

    def number_of_nodes(self):
        '''Return the number of nodes of the graph'''
        return f"The graph has {len(self.nodes)} nodes"

    def are_connected(self, node_one, node_two):
        ''' Return True if the given nodes are connected. Otherwise return false'''
        node_one = self.find_node(node_one)
        node_two = self.find_node(node_two)

        for neighboor in node_one.neighbors:
            if neighboor[0].value == node_two.value:
                return True
        return False

    def __str__(self):
        ''' Print the nodes '''
        graph = ""
        for node in self.nodes:
            graph += f"{node.__str__()}\n"
        return graph

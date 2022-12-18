class Edge():
    ''' 
        Edge class represents each each of a graph.
        It takes three values as attributes
        node1  : type of Node represents the first node
        node2  : type of Node represents the second node
        weight : type of int represents the wight of the edge 
    '''

    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    '''__gt__ it is used to define the > between two edges based on the weight'''

    def __gt__(self, other):
        return self.weight > other.weight

    '''__lt__ it is used to define the < between two edges based on the weight'''

    def __lt__(self, other):
        return self.weight < other.weight

    '''__eq__ it is used to define the == between two edges based on the weight'''

    def __eq__(self, other):
        return self.weight == other.weight

    def __str__(self):
        return f"{self.node1.value} {self.node2.value} {self.weight}"

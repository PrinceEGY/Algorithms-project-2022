class Node:
    '''
        The Node class represents each node of the graph
        The attribute value represents the stored data
        The list of neighbors attribute represents the vertices with which exists a connection
    '''

    def __init__(self, value, neighbors=None):
        self.value = value
        if neighbors is None:
            self.neighbors = []
        else:
            self.neighbors = neighbors

    def has_neighbors(self):
        ''' Return True if the node is connected with at least one node
        otherwise returns false '''
        if len(self.neighbors) == 0:
            return False
        return True

    def number_of_neighbors(self):
        ''' Returns the number of vertices with which has a connection '''
        return len(self.neighbors)

    def add_neighboor(self, neighboor):
        ''' Adds a new connection to the neighboor list'''
        self.neighbors.append(neighboor)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.value == other.value
        return self.value == other

    def __str__(self):
        returned_string = ""
        if self.has_neighbors():
            for neighboor in self.neighbors:
                returned_string += f"{self.value} -> {neighboor[0].value} "
        else:
            returned_string += f"{self.value} -> None"

        return returned_string

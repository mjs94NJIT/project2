class Node:
    def __init__(self, v):
        self.value = v
        self.adj = set()

    def adj(self):
        return self.adj

    def add(self, node):
        self.adj.add(node)
    
    def remove(self, node):
        self.adj.remove(node)

class Graph:
    
    def addNode(self, value):
        self.nodes.append(Node(value))
        
    def getAllNodes(self):
        return self.nodes
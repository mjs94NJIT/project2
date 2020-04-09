import random 
from datetime import datetime

class Node:
    
    def __init__(self, v):
        self.value = v
        self.adj = {} #adj {adjacent node: weight of the edge}
#END OF CLASS Node 
        
class WeightedGraph:
    
    def __init__(self):
        self.nodes = [] #the list of nodes in the graph
        
    def addNode(self, value):
        self.nodes.append(Node(value))
    
    def addDirectedEdge(self, first, second, weight):
        first.adj[second] = weight
        
    def removeUndirectedEdge(self, first, second):
        if(first.adj[second]):
            del first.adj[second]
        
    def getAllNodes(self):
        return self.nodes

    #a method for testing that returns a node address that has a given value 
    def getNodeFromValue(self, value):
        for node in self.nodes:
            if node.value is value:
                return node
#END OF CLASS DirectedGraph

#helper methods 

def printATraversal(nodeList):
    if(not nodeList):
        print('Path not found.')
    else:
        for node in nodeList:
            if not node:
                continue
            print(str(node.value)+' ', end="")
        print()

#start main code 

def createRandomCompleteWeightedGraph(n):
    graph = WeightedGraph()
    for iter in range(0,n):
        graph.addNode(iter)
    nodeList = graph.getAllNodes()
    for first in nodeList: 
        for second in nodeList:
            if first is not second: #no path to itself
                first.adj[second] = random.randint(0,99)
    return graph
    

def createLinkedList(n): 
    graph = WeightedGraph()
    graph.addNode(0)
    last = graph.getAllNodes()[0]
    for iter in range(1,n):
        graph.addNode(iter)
        newest = graph.getAllNodes()[-1]
        graph.addDirectedEdge(last, newest, 1)
        last = newest

closed_nodes = 0
def dijkstras(start):
    global closed_nodes
    closed_nodes = 0
    distance = {} 
    previous = {} 
    queue = []
    visited = set()
    for vertex in start.adj:
        distance[vertex] = float('inf')
        previous[vertex] = None 
        if vertex is not start:
            queue.append(vertex) #tuple of vertex and distance to it 
            distance[start] = 0 
        queue.append(start)
    
    while queue:
        shortest = findMin(queue, distance)
        queue.remove(shortest)
        visited.add(shortest)
        closed_nodes += 1 
        for neighbor in shortest.adj: 
            if neighbor in visited:
                continue
            tempDistance = distance[shortest] + shortest.adj[neighbor]
            if tempDistance < distance[neighbor]:
                distance[neighbor] = tempDistance
                previous[neighbor] = shortest

    return distance, previous #returns a tuple
    
def findMin(queue, distance):
    minimumDistance = float('inf')
    minimumVertex = None
    for vertex in queue:
        if distance[vertex] <= minimumDistance:
            minimumDistance = distance[vertex]
            minimumVertex = vertex
    return minimumVertex


def testGraph(): 
    graph = WeightedGraph()
    for i in range (0, 5):
        graph.addNode(i)
    nodes = graph.getAllNodes()
    graph.addDirectedEdge(nodes[0], nodes[1], 9)
    graph.addDirectedEdge(nodes[0], nodes[2], 3)
    graph.addDirectedEdge(nodes[0], nodes[3], 2)
    graph.addDirectedEdge(nodes[0], nodes[4], 10)
    graph.addDirectedEdge(nodes[1], nodes[2], 8)
    graph.addDirectedEdge(nodes[1], nodes[3], 7)
    graph.addDirectedEdge(nodes[1], nodes[4], 5)
    graph.addDirectedEdge(nodes[2], nodes[3], 4)
    graph.addDirectedEdge(nodes[2], nodes[4], 11)
    graph.addDirectedEdge(nodes[3], nodes[4], 6)
    return graph



WGraph = createRandomCompleteWeightedGraph(50) #CHANGE ME TO CHANGE RANDOM GRAPH'S SIZE
LList = createLinkedList(10)
testgraph = testGraph()
startTime = datetime.now()
distance, previous = dijkstras(WGraph.getAllNodes()[0])
endTime = datetime.now()

print("RANDOM GRAPH")
print("Vertex\tDist.\tParent")
for vertex in distance: #for vertex key in distance 
    if(vertex):
        print(str(vertex.value), end = "\t")
        print(str(distance[vertex]), end = "\t")
        if(vertex in previous):
            print(str(previous[vertex].value))
        else:
            print("None")
print("Total nodes closed: " + str(closed_nodes))
print("Search time: " + str(endTime-startTime))
startTime = datetime.now()
distance, previous = dijkstras(testgraph.getAllNodes()[0])
endTime = datetime.now()
print("KNOWN GRAPH")
print("Vertex\tDist.\tParent")
for vertex in distance: #for vertex key in distance 
    if(vertex):
        print(str(vertex.value), end = "\t")
        print(str(distance[vertex]), end = "\t")
        if(vertex in previous):
            print(str(previous[vertex].value))
        else:
            print("None")
print("Total nodes closed: " + str(closed_nodes))
print("Search time: " + str(endTime-startTime))
    


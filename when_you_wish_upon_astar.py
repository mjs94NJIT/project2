from enum import Enum
import random
import datetime as datetime 

class Directions(Enum):
    UP = 0
    RIGHT = 1 
    DOWN = 2 
    LEFT = 3
#enumerator for directions 

class Node:
    
    def __init__(self, x, y, value): 
        self.value = value 
        self.x = int(x) 
        self.y = int(y)
        self.adj = {} #format is {node object: direction enum}
        
#END OF CLASS Node 

class GridGraph:
    
    def __init__(self):
        self.nodes = [] 
        
    def addGridNode(self,x,y,value):
        self.nodes.append(Node(x,y,value))
    
    def addUndirectedEdge(self, first, second):
        if(first.x is second.x): #if they are on the same row
            if(first.y + 1 == second.y):
                first.adj[second] = Directions.RIGHT 
                second.adj[first] = Directions.LEFT
            if(first.y - 1 == second.y):
                first.adj[second] = Directions.LEFT
                second.adj[first] = Directions.RIGHT
        if(first.y == second.y): #if they are the same collumn 
            if(first.x + 1 == second.x):#second is one up
                first.adj[second] = Directions.UP
                second.adj[first] = Directions.DOWN
            if(first.x - 1 == second.x):#second is one down 
                first.adj[second] = Directions.DOWN
                second.adj[first] = Directions.UP
                
    def removeUndirectedDedge(self, first, second):
        del first.adj[second]
        del second.adj[first]
        
    def getAllNodes(self):
        return self.nodes
#END OF CLASS GridGraph

#start main code 

def createRandomGirdGraph(n):
    print("Building random graph. This may take some time.")
    graph = GridGraph()
    for x in range(0,n):
        for y in range(0,n):
            graph.addGridNode(x,y,"("+str(x)+","+str(y)+")") #the nodes value is (x,y)
    
    for first in graph.getAllNodes():
        for second in graph.getAllNodes():
            if(random.choice([True, False])): #50% chance of connecting 
                graph.addUndirectedEdge(first, second) #the validitiy checking is done in the method itself 
    return graph



#a* helper methods 

def getH(source, dest):
    return (dest.x - source.x) + (dest.y - source.y)
            
def getMin(queue, dictionary): #gets the next min value from a queue 
    minVal = float('inf')
    minNode = None 
    for node in queue:
        if dictionary[node] < minVal: 
            minVal = dictionary[node]
            minNode = node
    return minNode
    
def getPath(parentMap, current):
    path = []
    path.append(current)
    while current in parentMap:
        current = parentMap[current]
        path.insert(0, current)
    return path



closed_nodes = 0
def astar(sourceNode, destNode):
    print("Beginning A* search.")
    openn = set() 
    closed = set()
    parent = {} 
    g = {} #distance so far 
    f = {} #g(n) + predicted distance 
    g[sourceNode] = 0 
    f[sourceNode] = getH(sourceNode, destNode)
    openn.add(start)
    while openn:
        current = getMin(openn, f)
        if current is destNode:
            return getPath(parent, current)
        closed.add(current)
        global closed_nodes
        closed_nodes += 1
        openn.remove(current)
        for neighbor in current.adj:
            if( g.get(neighbor, float('inf')) > g[current] ): #if the neighbor is not in g, the default is infinite 
                parent[neighbor] = current
                g[neighbor] = g[current] + 1 #one extra move was used 
                f[neighbor] = g[neighbor] + getH(neighbor, destNode)
                if neighbor not in closed:
                    openn.add(neighbor)
    return None
                

maze = createRandomGirdGraph(100)
start = maze.getAllNodes()[0]
end = maze.getAllNodes()[-1]


startTime = datetime.now()
path = astar(start, end)
endTime = datetime.now()

if(path):
    for node in path: 
        if node:
            print(node.value, end=" --> ")
    print("Goal!")
else:
    print("No path found.")
    
print("Search time: " + str(endTime-startTime))
print("Total nodes closed: " + str(closed_nodes))
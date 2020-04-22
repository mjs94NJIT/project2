from enum import Enum
import random
from datetime import datetime

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
    
    def __init__(self,n):
        self.nodes  = [[None for i in range(n)] for j in range(n)]
        
    def addGridNode(self,x,y,value):
        self.nodes[x][y] = Node(x,y,value)
    
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

def createRandomGridGraph(n):
    print("Building random graph. This may take some time.")
    graph = GridGraph(n)
    for x in range(0,n):
        for y in range(0,n):
            value= "(%d,%d)"
            graph.addGridNode(x,y,value % (x,y)) #the nodes value is (x,y)
    progress = 0
    nodes = graph.getAllNodes()
    for x in range(0,n):
        print("Progress: " + str(int(  progress/len( graph.getAllNodes() )  * 100)) +"%\r", end="")
        progress+=1
        for y in range(0,n):
            if(random.choice([True, False]) and y<n-1): #50% chance of connecting 
                graph.addUndirectedEdge(nodes[x][y], nodes[x][y+1]) #the validitiy checking is done in the method itself 
            if(random.choice([True, False]) and x<n-1): 
                graph.addUndirectedEdge(nodes[x][y], nodes[x+1][y]) 
            if(random.choice([True, False]) and y>0):
                graph.addUndirectedEdge(nodes[x][y], nodes[x][y-1]) 
            if(random.choice([True, False]) and x>0): 
                graph.addUndirectedEdge(nodes[x][y], nodes[x-1][y]) 
    print("Progress: Done!")
    return graph



#a* helper methods 

def getHurestic(source, dest):
    return abs(dest.x - source.x) + abs(dest.y - source.y)
            
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




def astar(sourceNode, destNode):
    closed_nodes = 0
    print("Beginning A* search.")
    not_visited = set() 
    visited = set()
    parent = {} 
    distance_from_start = {} #distance so far 
    distance_to_goal = {} #g(n) + predicted distance 
    distance_from_start[sourceNode] = 0 
    distance_to_goal[sourceNode] = getHurestic(sourceNode, destNode)
    not_visited.add(start)
    while not_visited:
        current = getMin(not_visited, distance_to_goal)
        if current is destNode:
            return getPath(parent, current), closed_nodes
        visited.add(current)
        closed_nodes += 1
        not_visited.remove(current)
        for neighbor in current.adj:
            if( distance_from_start.get(neighbor, float('inf')) > distance_from_start[current] ): #if the neighbor is not in g, the default is infinite 
                parent[neighbor] = current
                distance_from_start[neighbor] = distance_from_start[current] + 1 #one extra move was used 
                distance_to_goal[neighbor] = distance_from_start[neighbor] + getHurestic(neighbor, destNode)
                if neighbor not in visited:
                    not_visited.add(neighbor)
    return None, closed_nodes
                

maze = createRandomGridGraph(100) #change me to change random graph's size
start = maze.getAllNodes()[0][0]
end = maze.getAllNodes()[-1][-1]


startTime = datetime.now()
path, closed_nodes = astar(start, end)
endTime = datetime.now()

print("Start --> ", end="")
if(path):
    for node in path: 
        if node:
            print(node.value, end=" --> ")
    print("Goal!")
else:
    print("No path found.")
    
print("Search time: " + str(endTime-startTime))
print("Total nodes closed: " + str(closed_nodes))

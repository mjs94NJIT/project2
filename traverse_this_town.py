import random 

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

#END OF CLASS Node 

class Graph:
    
    def __init__(self):
        self.nodes = [] # a list of nodes in the graph 
        #adjList = {} # a direction where key is a node and value is the list of edges 
   
    def addNode(self, value):
        self.nodes.append(Node(value))
    
    def addUndirectedEdge(self, first, second):
        first.add(second)
        second.add(first) 
    
    def removeUndirectedEdge(self, first, second):
        first.remove(second)
        second.remove(first)

    #returns the list of all nodes in the graph 
    def getAllNodes(self):
        return self.nodes
    
    #a method for createLinkedList that adds a one-way edge 
    def addDirectedEdge(self, first, second): #for use in createLinkedList
        #if second in adjList[first]:
        #    return
        #adjList[first].append(second)
        first.adj.add(second)
    
    #a method for createLinkedList that returns the last node in the graph 
    def getTail(self):
        return self.nodes[-1]

    #a method for testing that returns a random node in the graph 
    def getRandomNode(self):
        return random.choice(self.nodes)
    
    #a method for testing that returns a node address that has a given value 
    def getNodeFromValue(self, value):
        for node in self.nodes:
            if node.value is value:
                return node

#END OF CLASS Graph


class GraphSearch:

    visited = set()

    def DFSRec(self, start, end, path):
        if(start not in self.visited):
            self.visited.add(start)
        if(start is end): #the node is found, return it the path
            return path
        for node in start.adj:
            if(node not in self.visited): #for each node not visited
                temp = self.DFSRec(node, end, path+[node]) #recur with each path + the neighbor 
                if(temp): #if the path is found
                    return temp #return it 
        return None #if the path is never found, return None 

    #a helper method to pass an empty path to the recursive function 
    def DFSRecHelper(self, start, end): 
        self.visited.clear()
        path = [start] #the path will always start with the first node 
        return self.DFSRec(start, end, path)

    def DFSIter(self, start, end):
        self.visited.clear()
        stack = []
        stack.append( (start, [start]) ) #a stack of tuples (current node, path taken current node)
        while(stack):
            (current, path) = stack.pop()
            if(current is end):
                return path 
            for node in current.adj:
                if(node not in self.visited):
                    self.visited.add(node)  
                    stack.append( (node, path+[node]) ) #add a new possible path to the stack
        return None
    
    def BFTRecHelper(self, queue, path):
        if not queue:
            return path
        node = queue.pop(0)
        path.append(node)
        for adj in node.adj:
            if(adj not in self.visited):
                self.visited.add(adj)
                queue.append(adj)
                self.BFTRecHelper(queue,path)
    
    def BFTRec(self, graph):
        self.visited.clear()
        path = []
        for node in graph.nodes:
            if node not in self.visited:
                self.visited.add(node)
                queue = [node]
                path.append(self.BFTRecHelper(queue, path))
        return path

    def BFTIter(self, graph):
        queue = [] 
        path = []
        self.visited.clear()
        for node in graph.nodes:
            if node not in self.visited:
                self.visited.add(node)
                queue.append(node)
                path.append(node)
                while queue:
                    current = queue.pop(0)
                    for adj in current.adj:
                        if adj not in self.visited:
                            self.visited.add(adj)
                            queue.append(adj)
                            path.append(adj)
        return path


#END OF CLASS GraphSearch 

def createRadomUnweightedGraphIter(n): #part b
    graph = Graph()
    for itr in range(0,n):
        graph.addNode(str(itr)) #using the character representation of the node number as the value 
    nodes = graph.getAllNodes()
    for itr in range(0,n):
        graph.addUndirectedEdge(random.choice(nodes), random.choice(nodes))
    return graph

def createLinkedList(n): #part c
    graph = Graph()
    graph.addNode(str(0))
    last = graph.getTail()
    for itr in range(1,n):
        graph.addNode(str(itr)) #add the new node 
        graph.addDirectedEdge(last, graph.getTail()) #add edge from the previous added node to the new node
        last = graph.getTail() #update last to the newly added node 
    return graph 

#create the graph pictured on page 1 
def createTestGraph():
    testGraph = Graph()
    for node in ['S','A','C','B','E','F','G','K','L','D']:
        testGraph.addNode(node)
    testGraph.addUndirectedEdge(testGraph.getNodeFromValue('S'),testGraph.getNodeFromValue('A'))
    testGraph.addUndirectedEdge(testGraph.getNodeFromValue('A'),testGraph.getNodeFromValue('C'))
    testGraph.addUndirectedEdge(testGraph.getNodeFromValue('A'),testGraph.getNodeFromValue('B'))
    testGraph.addUndirectedEdge(testGraph.getNodeFromValue('A'),testGraph.getNodeFromValue('E'))
    testGraph.addUndirectedEdge(testGraph.getNodeFromValue('B'),testGraph.getNodeFromValue('E'))
    testGraph.addUndirectedEdge(testGraph.getNodeFromValue('E'),testGraph.getNodeFromValue('F'))
    testGraph.addUndirectedEdge(testGraph.getNodeFromValue('F'),testGraph.getNodeFromValue('G'))
    testGraph.addUndirectedEdge(testGraph.getNodeFromValue('G'),testGraph.getNodeFromValue('K'))
    testGraph.addUndirectedEdge(testGraph.getNodeFromValue('K'),testGraph.getNodeFromValue('L'))
    testGraph.addUndirectedEdge(testGraph.getNodeFromValue('L'),testGraph.getNodeFromValue('D'))
    return testGraph 

#method to print a list of nodes in a line 
def printATraversal(nodeList):
    if(not nodeList):
        print('Path not found.')
    else:
        for node in nodeList:
            if not node:
                continue
            print(node.value+' ', end="")
        print()
    
#driver code 
searcher = GraphSearch()

testgraph = createTestGraph()
print("Traversals of the graph pictured on page 1.")

start = testgraph.getNodeFromValue('S')
goal = testgraph.getNodeFromValue('D')

print("Iterative DFS from "+start.value+" to "+goal.value, end=": ")
printATraversal(searcher.DFSIter(start, goal))
print("Recursive DFS from "+start.value+" to "+goal.value, end=": ")
printATraversal(searcher.DFSRecHelper(start,goal))
print("Iterative BFT", end=": ")
printATraversal(searcher.BFTIter(testgraph))
print("Recursive BFT", end=": ")
printATraversal(searcher.BFTRec(testgraph))

print()
print("Traversals of a random graph of 100 nodes.")
testgraph= createRadomUnweightedGraphIter(100)
start = testgraph.getRandomNode()
goal = testgraph.getRandomNode() 

print("Iterative DFS from "+start.value+" to "+goal.value, end=": ")
printATraversal(searcher.DFSIter(start, goal))
print("Recursive DFS from "+start.value+" to "+goal.value, end=": ")
printATraversal(searcher.DFSRecHelper(start,goal))
print("Iterative BFT", end=": ")
printATraversal(searcher.BFTIter(testgraph))
print("Recursive BFT", end=": ")
printATraversal(searcher.BFTRec(testgraph))

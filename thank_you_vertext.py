import random 

class Node:
    
    def __init__(self, v):
        self.value = v
        self.adj = set() #adj is the adjacent nodes
#END OF CLASS Node 
        
class DirectedGraph:
    
    def __init__(self):
        self.nodes = [] #the list of nodes in the graph
        
    def addNode(self, value):
        self.nodes.append(Node(value))
    
    def addDirectedEdge(self, first, second):
        first.adj.add(second)
        
    def removeUndirectedEdge(self, first, second):
        first.remove(second)
        
    def getAllNodes(self):
        return self.nodes

    #a method for testing that returns a node address that has a given value 
    def getNodeFromValue(self, value):
        for node in self.nodes:
            if node.value is value:
                return node
#END OF CLASS DirectedGraph

class TopSort:
    
        
    def __init__(self):
        self.visited = set()
        
    def Kahns(self, DAGraph):
        nodeMap = {} #structured {node object: num of incoming edges}
        retArray = []
        queue = []
        for node in DAGraph.getAllNodes(): #build the dictionary 
            if node not in nodeMap: #the node isn't pointed to by any other nodes
                nodeMap[node] = 0
            for adj in node.adj:
                if adj not in nodeMap:
                    nodeMap[adj] = 1 #the node has been pointed to for the first time
                else:
                    nodeMap[adj] += 1 #else the point is pointed to again 
        #note: this could be more efficient in the design of node/graph was changed but i'm using the same structure as part 1 
        
        for node in nodeMap:
            if nodeMap[node] is 0: 
                queue.append(node)
        
        while(queue): #while the queue is not empty 
            node = queue.pop(0) #dequeue
            retArray.append(node)
            for adj in node.adj:
                nodeMap[adj] -= 1
                if nodeMap[adj] is 0:
                    queue.append(adj)
            nodeMap[node] -= 1 
        
        return retArray

    def mDFS(self, DAGraph):
        self.visited.clear()
        stack = [] 
        for node in DAGraph.getAllNodes():
            if node not in self.visited:
                self.mDFSHelper(node, stack)
        return stack
    
    def mDFSHelper(self, v, stack):
        self.visited.add(v)
        for adj in v.adj:
            if adj not in self.visited:
                self.mDFSHelper(adj, stack)
        stack.insert(0, v)
        return stack

#END OF CLASS TopSort

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

def testDAGraph():
    #image included in readme
    graph = DirectedGraph()
    for i in range(1, 8):
        graph.addNode(i)
    graph.addDirectedEdge(graph.getNodeFromValue(1),graph.getNodeFromValue(2))
    graph.addDirectedEdge(graph.getNodeFromValue(1),graph.getNodeFromValue(3))
    graph.addDirectedEdge(graph.getNodeFromValue(2),graph.getNodeFromValue(4))
    graph.addDirectedEdge(graph.getNodeFromValue(2),graph.getNodeFromValue(5))
    graph.addDirectedEdge(graph.getNodeFromValue(3),graph.getNodeFromValue(6))
    graph.addDirectedEdge(graph.getNodeFromValue(4),graph.getNodeFromValue(7))
    graph.addDirectedEdge(graph.getNodeFromValue(5),graph.getNodeFromValue(7))
    graph.addDirectedEdge(graph.getNodeFromValue(6),graph.getNodeFromValue(5))
    graph.addDirectedEdge(graph.getNodeFromValue(6),graph.getNodeFromValue(7))
    return graph
    
#start main code 

def createRandomDAGIter(n):
    graph = DirectedGraph()
    for iter in range (0,n):
        graph.addNode(iter)
    nodes = graph.getAllNodes()
    for iter in range(0,n-1):
        #adds random edges to the graph by only adding them in a forward direction 
        #i.e. a node will only ever have an edge pointing to a node of a greater value
        #the last node will be the 'end' of the graph (no edges coming out)
        graph.addDirectedEdge(nodes[iter], random.choice(nodes[iter+1:]))
    return graph

sorter = TopSort()
DAGraph = testDAGraph()

print("On a known graph.")
print("Kahn's")
KAHN_Nodes = sorter.Kahns(DAGraph)
printATraversal(KAHN_Nodes)
print("mDFS")
mDFS_Nodes = sorter.mDFS(DAGraph)
printATraversal(mDFS_Nodes)
print("On a random graph.")

DAGraph = createRandomDAGIter(1000) #change me to change random graph's size 
print("Kahn's")
KAHN_Nodes = sorter.Kahns(DAGraph)
printATraversal(KAHN_Nodes)
print("mDFS")
mDFS_Nodes = sorter.mDFS(DAGraph)
printATraversal(mDFS_Nodes)


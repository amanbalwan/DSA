class Graph:
    def __init__(self):
        self.numberofNodes=0
        self.adjacentlist={}
        
    def addVertex(self,node):
        if node not in self.adjacentlist:
            self.adjacentlist[node]=[]
            self.numberofNodes+=1
        else:
            print("Node already exists")
        
    def addEdge(self,node1,node2):
        if node1 in self.adjacentlist and node2 in self.adjacentlist:
            self.adjacentlist[node1]+=[node2]
            self.adjacentlist[node2]+=[node1]

        else:
            print("node missing")


    def showConnections(self):
        for i in self.adjacentlist:
            print(i,"--->",self.adjacentlist[i])


myGraph=Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1') 
myGraph.addEdge('3', '4') 
myGraph.addEdge('4', '2') 
myGraph.addEdge('4', '5') 
myGraph.addEdge('1', '2') 
myGraph.addEdge('1', '0') 
myGraph.addEdge('0', '2') 
myGraph.addEdge('6', '5')
myGraph.showConnections()
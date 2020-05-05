# Python program to print all paths from a source to destination. 

from collections import defaultdict 

#This class represents a directed graph 
# using adjacency list representation 
class Graph:

    def __init__(self, vertices):
        self.v = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printAllPathsUtil(self, u, d, visited, path):

        path.append(u)
        visited[u] = True
        
        if u == d:
            print(path)
        else:
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path)
        
        path.pop()
        visited[u] = False

    def printAllPaths(self, s, d):
        visited = [False]*(self.v)
        path = []
        self.printAllPathsUtil(s, d, visited, path)



# Create a graph given in the above diagram 
g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(0, 3) 
g.addEdge(2, 0) 
g.addEdge(2, 1) 
g.addEdge(1, 3) 

s = 2
d = 3
g.printAllPaths(s, d) 

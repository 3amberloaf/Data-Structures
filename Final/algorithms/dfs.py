from collections import defaultdict

# Builds directed graph using adjacency list
class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
    
    # Add edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    # DFS Algorithm
    def DFSUtil(self, v, visited):
        
        # Current node is marked as visited
        visited.add(v)
        print(v, end=' ')
        
        # iterates through neighbors of current node and if they are not already visited, it will recursively call the function on them
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFSUtil(neighbor, visited)
    
    def DFS(self, v):
        
        # stored visited nodes
        visited = set()
        
        # prints DFS traversal
        self.DFSUtil(v, visited)
        
if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
 
    print("Following is Depth First Traversal (starting from vertex 0)")
     
    # Function call
    g.DFS(0)
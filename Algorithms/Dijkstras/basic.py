# Show how to modify Dijkstra’s algorithm to not only output the distance from v to each vertex in G, 
# but also to output a tree T rooted at v, such that the path in T from v to a vertex u is actually a shortest path in G from v to u.

import sys

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
        self.parent = [-1] * vertices

    def printSolution(self, distance):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", distance[node])
        print("\nThe constructed shortest path tree:")
        for i in range(1, self.V):
            print(f"{self.parent[i]} - {i}")
    
    def minDistance(self, distance, sptSet):
        
        min = sys.maxsize
        
        for u in range(self.V):
            if distance[u] < min and sptSet[u] == False:
                min = distance[u]
                min_index = u
        
        return min_index
    
    def dijsktra(self, src):
        
        distance = [sys.maxsize] * self.V
        distance[src] = 0
        sptSet = [False] * self.V
        
        for cout in range(self.V):
            
            x = self.minDistance(distance, sptSet)
            sptSet[x] = True
            
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                        distance[y] > distance[x] + self.graph[x][y]:
                    distance[y] = distance[x] + self.graph[x][y]
                    self.parent[y] = x
 
        self.printSolution(distance)

if __name__ == "__main__":
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]
 
    g.dijsktra(0)

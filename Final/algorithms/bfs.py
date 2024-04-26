from collections import deque

    
def BFS(adjacencyList, origin, visited):
        
    Q = deque()
        
    # Current node is marked and visited
    visited[origin] = True
    Q.append(origin)
    
    # Iterate through Q 
    while Q:
        
        # removed a queue and prints
        currentNode = Q.popleft()
        print(currentNode, end= ' ')
        
        # finds adjacent vertices of dequed node if not visited, it will visit and enqueue
        for neighbor in adjacencyList[currentNode]:
            if not visited[neighbor]:
                visited[neighbor] = True
                Q.append(neighbor)

def addEdge(adjacencyList, u, v):
    adjacencyList[u].append(v)
    
def main():
    # Number of vertices in the graph
    vertices = 5

    # Adjacency list representation of the graph
    adjList = [[] for _ in range(vertices)]

    # Add edges to the graph
    addEdge(adjList, 0, 1)
    addEdge(adjList, 0, 2)
    addEdge(adjList, 1, 3)
    addEdge(adjList, 1, 4)
    addEdge(adjList, 2, 4)

    # Mark all the vertices as not visited
    visited = [False] * vertices

    # Perform BFS traversal starting from vertex 0
    print("Breadth First Traversal starting from vertex 0:", end=" ")
    BFS(adjList, 0, visited)

if __name__ == "__main__":
    main()
    
    
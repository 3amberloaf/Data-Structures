import heapq

def dijkstra(graph, start_vertex):
    # The graph is assumed to be a dictionary where the keys are the vertex identifiers and the values are
    # dictionaries with the neighbors and corresponding edge distances, e.g., {u: {v: distance, ...}, ...}

    # Distances dictionary, start with all distances as infinity
    distances = {vertex: float('infinity') for vertex in graph}
    # The distance to the start vertex is always 0
    distances[start_vertex] = 0

    # Priority queue to hold vertices and their current distances
    pq = [(0, start_vertex)]

    while pq:
        # Get the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(pq)

        # If the distance is greater than the recorded, this is a stale record, skip it
        if current_distance > distances[current_vertex]:
            continue

        # Look at neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # If the computed distance is less than the recorded, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Enqueue the neighbor with its new better distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

graph = {
     'A': {'B': 1, 'C': 4},
     'B': {'A': 1, 'C': 2, 'D': 5},
     'C': {'A': 4, 'B': 2, 'D': 1},
     'D': {'B': 5, 'C': 1}
 }

start = 'A'
distances = dijkstra(graph, start)
print(distances)

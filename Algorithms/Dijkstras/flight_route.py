import heapq

def dijkstra(graph, start):
    # Distances dictionary with initial distances set to infinity, except the start node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Priority queue initialized with the start node
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # If this distance is not the shortest one known, skip processing
        if current_distance > distances[current_vertex]:
            continue
        
        # Examine each adjacent node
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Now using the function on your graph
graph_example = {
    'HNL': {'LAX': 2555},
    'SFO': {'LAX': 337, 'ORD': 1843},
    'LAX': {'SFO': 337, 'DFW': 1233, 'HNL': 2555},
    'ORD': {'SFO': 1843, 'DFW': 802, 'PVD': 849},
    'DFW': {'LAX': 1233, 'ORD': 802, 'LGA': 1387, 'MIA': 1120},
    'LGA': {'DFW': 1387, 'MIA': 1099, 'PVD': 142},
    'PVD': {'ORD': 849, 'MIA': 1209, 'LGA': 142},
    'MIA': {'DFW': 1120, 'LGA': 1099, 'PVD': 1205},
}

distances_from_HNL = dijkstra(graph_example, 'HNL')
print(distances_from_HNL)

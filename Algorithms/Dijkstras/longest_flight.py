from typing import Dict, List, Tuple, Optional

def flight_dfs(graph, start, end, path, distance):
    path.append(start)
    if start == end:
        return path, distance
    if start not in graph:
        return None, 0  

    longest_path = None
    max_distance = 0
    for node, dist in graph[start].items():
        if node not in path: 
            current_path, current_distance = flight_dfs(graph, node, end, path[:], distance + dist) 
            if current_path is not None and current_distance > max_distance:
                longest_path = current_path
                max_distance = current_distance

    return longest_path, max_distance

flight_routes = {
    'HNL': {'LAX': 2555},
    'SFO': {'LAX': 337, 'ORD': 1843},
    'LAX': {'SFO': 337, 'DFW': 1233, 'HNL': 2555},
    'ORD': {'SFO': 1843, 'DFW': 802, 'PVD': 849},
    'DFW': {'LAX': 1233, 'ORD': 802, 'LGA': 1387, 'MIA': 1120},
    'LGA': {'DFW': 1387, 'MIA': 1099, 'PVD': 142},
    'PVD': {'ORD': 849, 'MIA': 1209, 'LGA': 142},
    'MIA': {'DFW': 1120, 'LGA': 1099, 'PVD': 1205},
}

longest_path = flight_dfs(flight_routes, "PVD", "HNL", [], 0)
print("Longest Path from PVD to HNL:", longest_path)

# Draw a simple undirected graph G that has 12 vertices, 18 edges, and 3 connected components. Why would it be impossible to draw G with 3 connected
# components if G had 66 edges?

from graphviz import Graph

def create_graph():
    # Create an undirected graph
    g = Graph('G', filename='undirected_graph.gv', engine='neato')

    # Define vertices for three connected components
    # Component 1: Vertices 1-4
    # Component 2: Vertices 5-8
    # Component 3: Vertices 9-12

    # Add edges for each component to ensure they are connected
    # Component 1 edges
    edges_component_1 = [(1, 2), (2, 3), (3, 4), (4, 1), (4, 2), (1, 3)]
    # Component 2 edges
    edges_component_2 = [(5, 6), (6, 7), (7, 8), (8, 5), (8, 6), (5, 7)]
    # Component 3 edges
    edges_component_3 = [(9, 10), (10, 11), (11, 12), (12, 9), (12, 10), (9, 11)]

    # Add edges to graph
    for edge in edges_component_1 + edges_component_2 + edges_component_3:
        g.edge(str(edge[0]), str(edge[1]))

    return g

if __name__ == "__main__":
    graph = create_graph()
    graph.view()

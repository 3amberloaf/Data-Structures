def initialize_matrix(N):
    
    G = [[False for _ in range(N)] for _ in range(N)]
    return G

def computeGn(A, B, N):
    """ Matrix G2 defines connections via paths of exactly length 2 between nodes """
    
    G = initialize_matrix(N)
           
    for i in range(1, N):
        for j in range(1, N):
            for k in range(1, N):
                G[i][j] = G[i][j] or (A[i][k] and B[k][j])
    
    return G

def transitiveClosure(G, N):
    
    G_transitive = [row[:] for row in G] 
    G_power = G
    
    for _ in range(2, N+1):
        G_power = computeGn(G_power, G, N)
        for i in range(N):
            for j in range(N):
                G_transitive[i][j] = G_transitive[i][j] or G_power[i][j]

    return G_transitive

def print_matrix(M):
    for row in M:
        print(" ".join(['1' if x else '0' for x in row]))
        
def matrix_to_dot(matrix):
    n = len(matrix)
    dot_output = "\n"
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                dot_output += f"    {i} -> {j};\n"
    return dot_output


N = 8
# Graph 1
G1 = initialize_matrix(N)
G1[0][1] = True  # Arc 1-2
G1[1][2] = True  # Arc 2-3
G1[2][0] = True  # Arc 3-1
G1[3][4] = True  # Arc 4-5
G1[4][5] = True  # Arc 5-6
G1[5][3] = True  # Arc 6-4

G1_plus = transitiveClosure(G1, N)
G1_graph = matrix_to_dot(G1)
G1_plus_graph = matrix_to_dot(G1_plus)

# Print original graph and its transitive closure
print("Original Graph 1 as a Matrix:")
print_matrix(G1)
print("\nOriginal Graph 1 as a Graph:")
print(G1_graph)
print("\nTransitive Closure of Graph 1:")
print_matrix(G1_plus)
print("\nTransitive Closure as a Matrix:")
print(G1_plus_graph)

# Graph 2
G2 = initialize_matrix(N)
G2[0][1] = True  # Arc 1-2
G2[1][0] = True  # Arc 2-1
G2[2][3] = True  # Arc 3-4
G2[3][2] = True  # Arc 4-3
G2[4][5] = True  # Arc 5-6
G2[5][4] = True  # Arc 6-5

G2_plus = transitiveClosure(G2, N)
G2_graph = matrix_to_dot(G2)
G2_graph_plus = matrix_to_dot(G2_plus)

# Print original graph and its transitive closure
print("Original Graph 2 as a Matrix:")
print_matrix(G2)
print("\nOriginal Graph 2 as a Graph:")
print(G2_graph)
print("\nTransitive Closure of Graph 2:")
print_matrix(G2_plus)
print("\nTransitive Closure as a Matrix:")
print(G2_graph_plus)

# Graph 3
G3 = initialize_matrix(N)
G3[0][1] = True  # Arc 1-2
G3[1][2] = True  # Arc 2-3
G3[2][3] = True  # Arc 3-4
G3[3][4] = True  # Arc 4-5
G3[4][5] = True  # Arc 5-6
G3[5][6] = True  # Arc 6-7
G3[6][7] = True  # Arc 7-8

G3_plus = transitiveClosure(G3, N)
G3_graph = matrix_to_dot(G3)
G3_graph_plus = matrix_to_dot(G3_plus)

# Print original graph and its transitive closure
print("Original Graph 3 as a Matrix:")
print_matrix(G3)
print("\nOriginal Graph 3 as a Graph:")
print(G3_graph)
print("\nTransitive Closure of Graph 3:")
print_matrix(G3_plus)
print("\nTransitive Closure as a Matrix:")
print(G3_graph_plus)

# Graph 4
G4 = initialize_matrix(N)
G4[0][1] = True  # Arc 1-2
G4[1][2] = True  # Arc 2-3
G4[2][3] = True  # Arc 3-4
G4[4][5] = True  # Arc 5-6
G4[5][6] = True  # Arc 6-7
G4[6][7] = True  # Arc 7-8

G4_plus = transitiveClosure(G4, N)
G4_graph = matrix_to_dot(G4)
G4_graph_plus = matrix_to_dot(G4_plus)

# Print original graph and its transitive closure
print("Original Graph 4 as a Matrix:")
print_matrix(G4)
print("\nOriginal Graph 4 as a Graph:")
print(G4_graph)
print("\nTransitive Closure of Graph 4:")
print_matrix(G4_plus)
print("\nTransitive Closure as a Matrix:")
print(G4_graph_plus)

# Graph 5
G5 = initialize_matrix(N)
G5[0][1] = True  # Arc 1-2
G5[1][2] = True  # Arc 2-3
G5[2][3] = True  # Arc 3-4
G5[3][4] = True  # Arc 4-5
G5[4][5] = True  # Arc 5-6
G5[5][6] = True  # Arc 6-7
G5[7][0] = True  # Arc 8-1

G5_plus = transitiveClosure(G5, N)
G5_graph = matrix_to_dot(G5)
G5_graph_plus = matrix_to_dot(G5_plus)


# Print original graph and its transitive closure
print("Original Graph 5 as a Matrix:")
print_matrix(G5)
print("\nOriginal Graph 5 as a Graph:")
print(G5_graph)
print("\nTransitive Closure of Graph 5:")
print_matrix(G5_plus)
print("\nTransitive Closure as a Matrix:")
print(G5_graph_plus)
  
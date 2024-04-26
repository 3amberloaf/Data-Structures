# Graph 2
G2 = initialize_matrix(N)
G2[0][1] = True  # Arc 1-2
G2[1][0] = True  # Arc 2-1
G2[2][3] = True  # Arc 3-4
G2[3][2] = True  # Arc 4-3
G2[4][5] = True  # Arc 5-6
G2[5][4] = True  # Arc 6-5

G2_plus = transitiveClosure(G2, N)

# Print original graph and its transitive closure
print("Original Graph 2:")
print_matrix(G2)
print("\nTransitive Closure of Graph 2:")
print_matrix(G2_plus)

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

# Print original graph and its transitive closure
print("Original Graph 3:")
print_matrix(G3)
print("\nTransitive Closure of Graph 3:")
print_matrix(G3_plus)

# Graph 4
G4 = initialize_matrix(N)
G4[0][1] = True  # Arc 1-2
G4[1][2] = True  # Arc 2-3
G4[2][3] = True  # Arc 3-4
G4[4][5] = True  # Arc 5-6
G4[5][6] = True  # Arc 6-7
G4[6][7] = True  # Arc 7-8

G4_plus = transitiveClosure(G4, N)

# Print original graph and its transitive closure
print("Original Graph 4:")
print_matrix(G4)
print("\nTransitive Closure of Graph 4:")
print_matrix(G4_plus)

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


# Print original graph and its transitive closure
print("\nOriginal Graph 5:")
print_matrix(G5)
print("\nTransitive Closure of Graph 5:")
print_matrix(G5_plus)
            
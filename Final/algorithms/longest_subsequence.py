""" prints the full matrix for every prefix """

def LCS(string1, string2):
    
    n = len(string1)
    m = len(string2)
    L = [[0 for j in range(m + 1)] for i in range(n + 1)]
    """ creates a 2-D array for L with the size of i,j """
    
    for i in range(1, n+1):
        for j in range(1, m + 1):
            if string1[i - 1] == string2[j - 1]:
                L[i][j] = L[i -1][j -1] + 1
            else:
                L[i][j] = max(L[i -1][j], L[i][j-1])
    
    return 

def print_LCS_matrix(L):
    for row in L:
        print(' '.join(map(str, row)))

string1 = "CGATAATTGAGA"
string2 = "GTTCCTAATA"

L = LCS(string1, string2)
full_matrix = print_LCS_matrix(L)
print("Full Matrix", full_matrix)
    

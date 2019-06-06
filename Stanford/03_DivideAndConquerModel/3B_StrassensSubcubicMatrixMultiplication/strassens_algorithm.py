# strassens_algorithm.py

# A demonstration of Strassen's subcubic runtime matrix multiplication 
# algorithm on square matrices using the divide and conquer model.

import numpy as np

def main():
    m1 = np.array([[1,2],[3,4]])
    m2 = np.array([[5,6],[7,8]])

    print("The first square matrix is: ")
    print(m1)
    print("The second square matrix is: ")
    print(m2)

    output_matrix = strassens_algorithm(m1, m2)
    expected_matrix = np.matmul(m1, m2)

    print("When taking the dot product of m1 and m2 we expected an \
output matrix of:")
    print(expected_matrix)
    print("Using Strassen's subcubic runtime matrix multiplication \
algorithm we got:")
    print(output_matrix)

def strassens_algorithm(m1, m2):
    # Base case: A matrix of shape 1x1 is solved by default
    if np.shape(m1) == (1, 1):
        return np.asscalar(m1 * m2)

    # Pre-calculate the n/2 value. We'll be using it a lot and it's the same 
    # for matrix 1 and matrix 2 since they have equivalent square dimensions.
    n_over_2 = len(m1)//2

    # Divide
    # Create submatrix blocks from quadrants of m1
    # |A B|
    # |C D|
    A = m1[0:n_over_2, 0:n_over_2]
    B = m1[0:n_over_2, n_over_2:]
    C = m1[n_over_2:, 0:n_over_2]
    D = m1[n_over_2:, n_over_2:]

    # Create submatrix blocks from quadrants of m2
    # |E F|
    # |G H|
    E = m2[0:n_over_2, 0:n_over_2]
    F = m2[0:n_over_2, n_over_2:]
    G = m2[n_over_2:, 0:n_over_2]
    H = m2[n_over_2:, n_over_2:]

    # Conquer
    # Calculate the 7 products: (elements matrix 1) * (elements matrix 2)
    p1 = strassens_algorithm(A, F-H)        # p1 = A * (F - H)
    p2 = strassens_algorithm(A+B, H)        # p2 = (A + B) * H
    p3 = strassens_algorithm(C+D, E)        # p3 = (C + D) * E
    p4 = strassens_algorithm(D, G-E)        # p4 = D * (G - E)
    p5 = strassens_algorithm(A+D, E+H)      # p5 = (A + D) * (E + H)
    p6 = strassens_algorithm(B-D, G+H)      # p6 = (B - D) * (G + H)
    p7 = strassens_algorithm(A-C, E+F)      # p7 = (A - C) * (E + F)

    # Combine
    return np.array([[p5+p4-p2+p6, p1+p2],[p3+p4, p1+p5-p3-p7]])

if __name__ == "__main__":
    main()
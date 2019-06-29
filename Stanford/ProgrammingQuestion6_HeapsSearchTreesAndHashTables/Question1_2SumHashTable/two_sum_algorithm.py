# two_sum_algorithm.py
"""
Using algo1-programming_prob-2sum.txt.

The goal of this problem is to implement a variant of the 2-SUM 
algorithm (covered in the Week 6 lecture on hash table applications).

The file contains 1 million integers, both positive and negative 
(there might be some repetitions!).This is your array of integers, 
with the i-th row of the file specifying the i-th entry of the array.

Your task is to compute the number of target values t in the interval 
[-10000,10000] (inclusive) such that there are distinct numbers x, y in
the input file that satisfy x+y=t. (NOTE: ensuring distinctness 
requires a one-line addition to the algorithm from the lecture.)

Write your numeric answer (an integer between 0 and 20001) in the space 
provided.

OPTIONAL CHALLENGE: If this problem is too easy for you, try 
implementing your own hash table for it. For example, you could compare
performance under the chaining and open addressing approaches to 
resolving collisions.
"""

import numpy as np

def main():
    # Insert elements in the .txt into a hash table, H1, ensuring 
    # duplicate elements are not inserted.
    # Create second hash table, H2, for the values -10000 to 10000 
    # inclusive.
    h1, h2 = setup()
    h2_length = len(h1)

    # For each value, x, in the .txt file, check if there is a 
    # value, y, in H1 that satisfies t-x=y.
        # If present delete t from H2
    # After going through all the values return the length of H2.
    h2_final_length = two_sum_search(h1, h2)

    # The number of times a target value was found is the difference 
    # between the original length of h2 and the final length of h2.
    t_values = h2_length - h2_final_length
    
    print("The number of target values found to have sums was {}".format(t_values))

def setup():
    """
    setup hashes elements into hash tables.
    """

    

    # Since there are 1 million possible inputs for h1, 
    # let n1 be prime 2000003 gives a low load factor.
    n1 = 2000003
    h1 = np.zeros(n1)

    # Since there are 20001 possible inputs for h2,
    # let n2 be prime 40111.
    n2 = 40111
    h2 = np.zeros(n2)

    with open("algo1-programming_prob-2sum.txt") as f:
        # Exclude the newline character, \n
        for line in f:
            x = int(line.rstrip('\n'))
            
            h1[hash_it(x, n1)]

    for i in range(-10000, 10001):
        h2[hash_it(i, n2)]
            
    return h1, h2

def hash_it(x, n):
    return x%n

def two_sum_search(h1, h2):
    """
    two_sum_search checks each value in h1 two see if two numbers in h1
    reach one of the target values remaining in h2.
    """
    return len(h2)


if __name__ == "__main__":
    main()
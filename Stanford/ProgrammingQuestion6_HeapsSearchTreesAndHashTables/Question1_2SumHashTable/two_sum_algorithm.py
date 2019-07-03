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

import copy

def main():
    # Insert elements in the .txt into a hash table, h, ensuring 
    # duplicate elements are not inserted.
    # Create second list, target_list, for the values -10000 to 10000 
    # inclusive.
    h, target_list = setup()

    # For each value, x, in the .txt file, check if there is a 
    # value, y, in h that satisfies t-x=y.
    # After going through all the values return the count of targets
    # found.
    num_found_targets = two_sum_search(h, target_list)
    
    print("The number of target values found to have sums was {}.".format(num_found_targets))

def setup():
    """
    setup hashes elements into dictionaries (hash tables).
    """

    h, target_values = set(), set()
    for x in range(-10000, 10001):
        target_values.add(x)

    with open("algo1-programming_prob-2sum.txt") as f:
        # Exclude the newline character, \n
        for line in f:
            x = int(line.rstrip('\n'))
            h.add(x)
            
    return h, target_values

def two_sum_search(h, targets):
    """
    two_sum_search checks each value in h to see if two numbers in h
    reach one of the target values in the target list.
    """

    final_set = copy.deepcopy(targets)

    for t in targets:
        for x in h:
            if t-x in h:
                final_set.discard(t)
                break

    return len(final_set)

if __name__ == "__main__":
    main()
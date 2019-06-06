# index_is_an_element.py

"""You are given a sorted (from smallest to largest) array A of n distinct 
integers which can be positive, negative, or zero. You want to decide whether 
or not there is an index i such that A[i] = i. Design the fastest algorithm 
that you can for solving this problem."""

# I could only think of an algorithm that ran in linear time at best.
def main():
    A = [1,2,3,4,4,5,6,7]

    index_equals_element = find_index_equals_element(A)

    if len(index_equals_element) > 0:
        print("The index to element match list is", index_equals_element)
    else:
        print("There is no element in A where A[i] == i.")


def find_index_equals_element(A):
    index_equals_element = []
    for i in range(len(A)):
        if A[i] == i:
            index_equals_element.append(A[i])
    
    return index_equals_element

if __name__ == '__main__':
    main()
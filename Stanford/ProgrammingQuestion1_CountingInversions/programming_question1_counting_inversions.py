# programming_question1_counting_inversions.py

"""Given a text file, compute the number of inversions in the file, where row i 
of the file is equivalent to index i in the array. 

Because of the large size of the array, you should implement the fast 
divide-and-conquer-algorithm covered."""

from counting_inversion import sort_and_count_inversions

def main():
    initial_list = []
    with open('IntegerArray.txt') as f:
        # Exclude the newline character, '\n'
        initial_list = [int(line.rstrip('\n')) for line in f]

    count_of_inversions, _ = sort_and_count_inversions(initial_list)

    print("The number of inversions in the given file is {}.".format(count_of_inversions))

if __name__ == '__main__':
    main()
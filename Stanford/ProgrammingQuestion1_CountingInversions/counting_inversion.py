# counting_inversion.py
# A program implemented in O(n lg n) time to demonstrate counting inversions.

def main():
    A = [1, 5, 3, 6, 4, 2]
    print("The input list is", A)

    num_inversions, A = sort_and_count_inversions(A)

    print("The comparison list is", A)

    print("The number of inversions between the input list and the target list is {}.".format(num_inversions))

# Divide and conquer!
def sort_and_count_inversions(A):
    # Base case: An empty or one element length list is by default sorted and 
    # cannot have an inversion.
    if len(A) < 2:
        return 0, A

    # Divide with recursion
    list_lower_half = A[0:len(A)//2]
    list_upper_half = A[len(A)//2:]
    num_left_inversions, list_lower_half = sort_and_count_inversions(list_lower_half)
    num_right_inversions, list_upper_half = sort_and_count_inversions(list_upper_half)
    # Conquer with merge sort
    num_split_inversions, sorted_list = count_split_inversions(list_lower_half,                                                            list_upper_half)

    return num_left_inversions + num_right_inversions + num_split_inversions,           sorted_list

def count_split_inversions(x, y):
    sorted_list = []
    inversion_count = i = j = 0

    for _ in range(len(x) + len(y)):
        # Check if we've reached the end of a list
        if i >= len(x):
            # There are no inversions remaining as every element left in list y
            # is greater than anything that was in list x.
            while j < len(y):
                sorted_list.append(y[j])
                j += 1
            break
        elif j >= len(y):
            # Every element remaining in list x is greater than any element in
            # list y and has been accounted for below.
            while i < len(x):
                sorted_list.append(x[i])
                i += 1
            break

        # Not a split inversion
        if x[i] < y[j]:
            sorted_list.append(x[i])
            i += 1
        else:
            sorted_list.append(y[j])
            inversion_count += len(x) - i
            j += 1

    return inversion_count, sorted_list

if __name__ == "__main__":
    main()
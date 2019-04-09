# mergeSort.py
# An example program of the merge sort algorithm.

def main():
    # Define the example input array
    A = [5, 4, 1, 8, 7, 2, 6, 3, 9]
    print("The original list is", A)
    A = divide_and_conquer(A)
    print("The sorted list is", A)

def divide_and_conquer(input_list):
    # Base case: A single number or an empty list is sorted.
    if len(input_list) < 2:
        return input_list

    a = divide_and_conquer(input_list[0:len(input_list)//2])
    b = divide_and_conquer(input_list[len(input_list)//2:])

    sorted_list = merge_sort(a, b)

    return sorted_list

def merge_sort(a, b):
    sorted_list = []
    sorted_list_length = len(a) + len(b)
    # Initialize indexes for sublists to use in assignment to sorted_list
    i, j = 0, 0

    for _ in range(sorted_list_length):
        # Ensure we do not run off the end of the list
        if i >= len(a):
            while j < len(b):
                sorted_list.append(b[j])
                j += 1
            return sorted_list
        elif j >= len(b):
            while i < len(a):
                sorted_list.append(a[i])
                i += 1
            return sorted_list

        if a[i] < b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    
    return sorted_list

if __name__ == "__main__":
    main()
# heap_median_maintenance.py
"""
With the following text file: Median.txt

The goal of this problem is to implement the "Median Maintenance" 
algorithm (covered in the Week 5 lecture on heap applications). The 
text file contains a list of the integers from 1 to 10000 in 
unsorted order; you should treat this as a stream of numbers, arriving
one by one. Letting x-subscript i denote the i-th number of the file, 
the k-th median m-subscript k is defined as the median of the numbers 
x-subscript 1,..., x-subscript k. (So, if k is odd, then m-subscript k 
is ((k+1)/2)th smallest number among x-subscript 1,...,x-subscript k; 
if k is even, then m-subscript k is the (k/2)th smallest number among
x-subscript 1,...,x-subscript k.)

Find the sum of these 10000 medians, modulo 10000 
(i.e., only the last 4 digits). That is, you should compute
(m-subscript 1 + m-subscript 2 + ... + m-subscript 10000) mod 10000.

OPTIONAL EXERCISE: Compare the performance achieved by heap-based and 
search-tree-based implementations of the algorithm.
"""

import heap as h

def main():

    # Used to store highest half of elements
    high_half_heap = h.Heap()
    # Used to store lowest half of elements
    low_half_heap = h.Heap("max")

    median, median_total = 0, 0

    with open("Median.txt") as f:
        # Exclude the newline character, \n
        for line in f:
            x = int(line.rstrip('\n'))

            # Put x into the correct heap
            # If x > median, place x in high_half_heap
            if x > median:
                high_half_heap.insert(x)
            else:
                low_half_heap.insert(x)
            
            # Check if heaps need to be rebalanced
            rebalance(high_half_heap, low_half_heap)

            # Calculate the median given the new x
            median = find_median(high_half_heap, low_half_heap)

            # Add the median to the median_total
            median_total += median
            
    # Once the file is exhausted return_value = median_total%10000
    output = find_last_four(median_total)
    print("The last four digits of the sums of the medians is {}.".format(output))

def rebalance(h_high, h_low):
    """
    rebalance prevents one heap from hoarding all the values by 
    keeping the difference in the number of items between each 
    heap less than 2.
    """

    if abs(h_high.length() - h_low.length()) > 1:
        if h_high.length() > h_low.length():
            root, prs = h_high.extract_root()
            if prs:
                h_low.insert(root)
        else:
            root, prs = h_low.extract_root()
            if prs:
                h_high.insert(root)

def find_median(h_high, h_low):
    """
    find_median determines the median value between the two heaps.
    """

    count = h_high.length() + h_low.length()
    # r is the median's index
    r = 0
    if count%2 == 0:
        r = count//2
    else:
        r = (count + 1)//2
        
    if r > h_low.length():
        median, _ = h_high.peek()
    else:
        median, _ = h_low.peek()
        
    return median

def find_last_four(total):
    return total%10000

if __name__ == "__main__":
    main()
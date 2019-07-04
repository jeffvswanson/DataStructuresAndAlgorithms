/*
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
*/
package main

import "fmt"

func main() {
	fmt.Println("Hello")
}

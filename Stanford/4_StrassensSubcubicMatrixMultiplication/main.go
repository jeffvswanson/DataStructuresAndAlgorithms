package main

// A demonstration of Strassen's subcubic runtime matrix multiplication
// algorithm on square matrices using the divide and conquer model.

import (
	"fmt"

	"gonum.org/v1/gonum/mat"
)

func main() {
	m1 := mat.NewDense(2, 2, []float64{
		1, 2,
		3, 4,
	})
	m2 := mat.NewDense(2, 2, []float64{
		5, 6,
		7, 8,
	})

	// Expected output
	var o mat.Dense
	o.Mul(m1, m2)

	// Prefix number of spaces = 5, the number "m1 = " takes up.
	fmt.Println("m1 =", mat.Formatted(m1, mat.Prefix("     "), mat.Squeeze()))

	fmt.Println("m2 =", mat.Formatted(m2, mat.Prefix("     "), mat.Squeeze()))

	fmt.Println("Expected output:")
	fmt.Println(mat.Formatted(&o, mat.Squeeze()))

	fmt.Println("Strassen's algorithm output:")
	outputMatrix := strassensAlgorithm(m1, m2)
	fmt.Println(mat.Formatted(outputMatrix, mat.Squeeze()))
}

func strassensAlgorithm(m1, m2 *mat.Dense) *mat.Dense {
	var productMatrix mat.Dense

	rows, _ := m1.Dims()
	// Base case: A square matrix of dimension 1x1 is solved by default.
	if rows == 1 {
		productMatrix.Mul(m1, m2)
		return &productMatrix
	}

	// Break up m1 into submatrices from quadrant blocks
	// |a b|
	// |c d|
	a := m1.Slice(0, rows/2, 0, rows/2)
	b := m1.Slice(0, rows/2, rows/2, rows)
	c := m1.Slice(rows/2, rows, 0, rows/2)
	d := m1.Slice(rows/2, rows, rows/2, rows)

	// Break up m2 into submatrices from quadrant blocks
	// |e f|
	// |g h|
	e := m2.Slice(0, rows/2, 0, rows/2)
	f := m2.Slice(0, rows/2, rows/2, rows)
	g := m2.Slice(rows/2, rows, 0, rows/2)
	h := m2.Slice(rows/2, rows, rows/2, rows)

	// Calculate the 7 products: (elements matrix 1)*(elements matrix 2).
	// Resultants are used for intermediate step calculations, add/subtract.
	var resultant1 mat.Dense
	var resultant2 mat.Dense

	// p1 = a * (f-h)
	resultant1.Sub(f, h)
	p1 := strassensAlgorithm(a.(*mat.Dense), &resultant1)

	// p2 = (a+b) * h
	resultant1.Add(a, b)
	p2 := strassensAlgorithm(&resultant1, h.(*mat.Dense))

	// p3 = (c+d) * e
	resultant1.Add(c, d)
	p3 := strassensAlgorithm(&resultant1, e.(*mat.Dense))

	// p4 = d * (g-e)
	resultant1.Sub(g, e)
	p4 := strassensAlgorithm(d.(*mat.Dense), &resultant1)

	// p5 = (a+d) * (e+h)
	resultant1.Add(a, d)
	resultant2.Add(e, h)
	p5 := strassensAlgorithm(&resultant1, &resultant2)

	// p6 = (b-d) * (g+h)
	resultant1.Sub(b, d)
	resultant2.Add(g, h)
	p6 := strassensAlgorithm(&resultant1, &resultant2)

	// p7 = (a-c) * (e+f)
	resultant1.Sub(a, c)
	resultant2.Add(e, f)
	p7 := strassensAlgorithm(&resultant1, &resultant2)

	// Product matrix quadrants
	// |i j|
	// |k l|
	var i, j, k, l mat.Dense
	// i = p5 + p4 - p2 + p6
	resultant1.Add(p5, p4)
	resultant2.Sub(&resultant1, p2)
	i.Add(&resultant2, p6)
	// j = p1 + p2
	j.Add(p1, p2)
	// k = p3 + p4
	k.Add(p3, p4)
	// l = p1 + p5 - p3 - p7
	resultant1.Add(p1, p5)
	resultant2.Sub(&resultant1, p3)
	l.Sub(&resultant2, p7)

	// Build the product matrix
	var topHalf, bottomHalf mat.Dense
	topHalf.Augment(&i, &j)
	bottomHalf.Augment(&k, &l)
	productMatrix.Stack(&topHalf, &bottomHalf)

	return &productMatrix
}

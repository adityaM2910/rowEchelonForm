# Row - Echelon - Form

In linear algebra, a matrix is in echelon form if it has the shape resulting from a Gaussian elimination.

A matrix being in row echelon form means that Gaussian elimination has operated on the rows, and column echelon form means that Gaussian elimination has operated on the columns. In other words, a matrix is in column echelon form if its transpose is in row echelon form. Therefore, only row echelon forms are considered in the remainder of this article. The similar properties of column echelon form are easily deduced by transposing all the matrices. Specifically, a matrix is in row echelon form if

All rows consisting of only zeroes are at the bottom.
The leading coefficient (also called the pivot) of a nonzero row is always strictly to the right of the leading coefficient of the row above it.
Some texts add the condition that the leading coefficient must be 1.

These two conditions imply that all entries in a column below a leading coefficient are zeros

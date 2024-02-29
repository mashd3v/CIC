# Maths

**Give definition of a scalar, a vector, a matrix, and a tensor.**

- **Scalar:** is just a nuber. For example, "Let say $\textit{s} \in \Re$ be the slope of the line."

- **Vector:** is an a rray of numbers. For example, $\vec{x} = \begin{bmatrix}
                                                            x_{1} \\
                                                            x_{2} \\
                                                            \vdots \\
                                                            x_{n} 
                                                            \end{bmatrix}$

  We can think of vectors as identifying points in space, with each element giving the coordinate along a different axis.

- **Matrix:** is a 2-D array of numbers, so each element is identified by two indices instead of just one. For example, $\textbf{A} = \begin{bmatrix}
                                    A_{1,1} & A_{1,2} \\
                                    A_{2,1} & A_{2,2} 
                                    \end{bmatrix}$

- **Tensor:** describes a multilinear relationship between sets of algebraic objects related to a vector space. For example, we can identify the element of $\mathbf{A}$ at coordinates $(i,j,k)$ by writing $\mathbf{A}_{i,j,k}$

**What is the Hadamard product?**

Also known as wise-element, it is an operation performed between two matrices of the same size, where each element of the result is obtained by multiplying the corresponding elements of the original matrices. If you have two matrices $A$ and $B$ of the same size, the Hadamard product is denoted as A and its definition is as follows:

$$(A \odot B)_{ij} = A_{ij} \cdot B_{ij}$$

Where $A_{ij}$ and $B_{ij}$ are the elements in position \((i, j)\) of the matrices \(A\) and \(B\) respectively, and \((A \odot B)\) is the corresponding element in position \((i, j)\) of the resulting matrix \(A \odot B\).
In simpler terms, multiply element by element of the two matrices to obtain a new matrix of the same size.

**Define the following matrices: transpose, symmetric, identity, inverse, diagonal.**

- **Transpose matrix:** is obtained by swapping its rows and columns. If \(A\) is a matrix, then its transpose is denoted as \(A^T\), and the elements of the transpose are given by \((A^T)_{ij} = A_{ji}\).

- **Symmetric matrix:** is one that is equal to its own transpose. Mathematically, a matrix \(A\) is symmetric if \(A = A^T\).

- **Identity matrix:** is a square matrix with ones on the main diagonal and zeros elsewhere. The identity matrix is often denoted as \(I\) and has the property that for any matrix \(A\), \(A \cdot I = I \cdot A = A\).

- **Inverse matrix:** the inverse of a square matrix \(A\), denoted as \(A^{-1}\), is the matrix such that \(A \cdot A^{-1} = A^{-1} \cdot A = I\), where \(I\) is the identity matrix. Not all matrices have an inverse, and a matrix must be square (tamaño cuadrado) to have an inverse.

- **Diagonal matrix:** a diagonal matrix is one where all elements outside the main diagonal are zero. If \(D\) is a diagonal matrix, then $D_{ij} = 0$ for \(i \neq j\). Diagonal matrices are often denoted with a diagonal set of values, such as $D = \text{diag}(d_{1}, d_{2}, \ldots, d_{n})$, where $d_{i}$ are the diagonal elements.

**What is a linear transformation?**

Is a mathematical function between vector spaces that preserves vector addition and scalar multiplication. In other words, if \(T\) is a linear transformation, and \(u\) and \(v\) are vectors, and \(c\) is a scalar, then the following properties hold:

- \(T(u + v) = T(u) + T(v)\) (Additivity)
- \(T(cu) = cT(u)\) (Homogeneity)

Examples of linear transformations include rotations, scaling, and shearing. The matrix representation of a linear transformation can often be described using a transformation matrix. If \(T\) is a linear transformation from a vector space \(V\) to a vector space \(W\), and \(\mathbf{v}\) is a vector in \(V\), the action of \(T\) on \(\mathbf{v}\) is often denoted as \(T(\mathbf{v})\) or represented as a matrix-vector product.

**What is the inverse of a diagonal matrix?**

Is obtained by taking the reciprocal of each non-zero element on the main diagonal. A diagonal matrix \(D\) is invertible if and only if all diagonal elements are non-zero. If \(D = \text{diag}(d_1, d_2, \ldots, d_n)\) is a diagonal matrix, its inverse \(D^{-1}\) is given by \(\text{diag}(1/d_1, 1/d_2, \ldots, 1/d_n)\).

For a diagonal matrix to be invertible, none of its diagonal elements should be zero. If any diagonal element is zero, the matrix is singular, and its inverse does not exist. The product of a diagonal matrix and its inverse is the identity matrix:

\[
\text{diag}(d_1, d_2, \ldots, d_n) \cdot \text{diag}(1/d_1, 1/d_2, \ldots, 1/d_n) = I
\]

This property reflects the fact that the diagonal elements and their reciprocals cancel each other out in the product.

**What is a linear combination of two vectors?**

Say \(\mathbf{\vec{v}}\) and \(\mathbf{\vec{w}}\), is obtained by scaling each vector by a scalar and then adding the results. Mathematically, given vectors \(\mathbf{\vec{v}}\) and \(\mathbf{\vec{w}}\), and scalars \(a\) and \(b\), the linear combination is given by \(a\mathbf{\vec{v}} + b\mathbf{\vec{w}}\).

The general form of a linear combination involving two vectors \(\mathbf{v}\) and \(\mathbf{w}\) can be expressed as:

$$c_{1} \mathbf{\vec{v}} + c_{2} \mathbf{\vec{w}} + \ldots + c_{n} \mathbf{\vec{u}}_{n} $$

where $c_{1}, c_{2}, \ldots, c_{n}$ are scalars and $\mathbf{\vec{u}}_{n}$ represents additional vectors if the combination involves more than two vectors. Linear combinations are fundamental in linear algebra and are used to explore vector spaces and spans.

**What vectors are linearly dependent/independent?**

- **Linearly dependent vectors:** if there exist non-zero scalars $c_{1}, c_{2}, \ldots, c_{n}$, not all zero, such that $c_{1} \mathbf{\vec{v}}_{1} + c_{2} \mathbf{\vec{v}}_{2} + \ldots + c_{n} \mathbf{\vec{v}}_{n} = \mathbf{0}$. In other words, one or more vectors in the set can be expressed as a linear combination of the others.

- **Linearly independent vectors:** is linearly independent if the only scalars $c_{1}, c_{2}, \ldots, c_{n}$ that satisfy $c_{1} \mathbf{\vec{v}}_{1} + c_{2} \mathbf{\vec{v}}_{2} + \ldots + c_{n} \mathbf{\vec{v}}_{n} = \mathbf{0}$ are all zero. In other words, no vector in the set can be expressed as a linear combination of the others. For a set of vectors $\{\mathbf{\vec{v}}_{1}, \mathbf{\vec{v}}_{2}, \ldots, \mathbf{\vec{v}}_{n}\}$, if the only solution to $c_{1} \mathbf{\vec{v}}_{1} + c_{2} \mathbf{\vec{v}}_{2} + \ldots + c_{n} \mathbf{\vec{v}}_{n} = \mathbf{0}$ is $c_{1} = c_{2} = \ldots = c_{n} = 0$, then the vectors are linearly independent. Otherwise, if there exists a nontrivial solution with at least one $c_{i}$ not equal to zero, the vectors are linearly dependent.

**What is the span of a vector(s)?**

The span of a set of vectors $\{\mathbf{\vec{v}}_1, \mathbf{\vec{v}}_2, \ldots, \mathbf{\vec{v}}_{n}\}$ is the set of all possible linear combinations of these vectors. It is the subspace of the vector space that can be reached by scaling and adding the vectors in the set. Mathematically, the span is denoted as $\text{span}(\mathbf{\vec{v}}_{1}, \mathbf{\vec{v}}_{2}, \ldots, \mathbf{\vec{v}}_{n})$ and is given by:

$$\text{span}(\mathbf{\vec{v}}_{1}, \mathbf{\vec{v}}_{2}, \ldots, \mathbf{\vec{v}}_{n}) = \{c_{1} \mathbf{v}_{1} + c_{2} \mathbf{\vec{v}}_{2} + \ldots + c_{n} \mathbf{\vec{v}}_{n} \mid c_{1}, c_{2}, \ldots, c_{n} \text{ are scalars}\}$$

The span of a set of vectors represents all the possible vectors that can be created by linear combinations of the original vectors. It forms a subspace of the entire vector space. If the vectors are linearly independent, their span forms a subspace with dimension equal to the number of vectors in the set; otherwise, the dimension of the span is less than the number of vectors, as linearly dependent vectors do not contribute additional dimensions.

**What is the range of a matrix?**

The range of a matrix, also known as the column space, is the set of all possible linear combinations of its independent column vectors. In other words, it is the span of the column vectors of the matrix. Mathematically, if \(A\) is an \(m \times n\) matrix with columns $\mathbf{a}_{1}, \mathbf{a}_{2}, \ldots, \mathbf{a}_{n}$, then the range of \(A\) is denoted as \(\text{range}(A)\) and is given by:

$$\text{range}(A) = \text{span}(\mathbf{a}_1, \mathbf{a}_2, \ldots, \mathbf{a}_n)$$

The range of a matrix is a subspace of the codomain (target space) of a linear transformation represented by the matrix. It provides insight into the dimensionality of the output space and is crucial in understanding the behavior of linear transformations. The rank of a matrix is the dimension of its range and provides valuable information about the linear independence of its columns.

**What is a singular matrix?**

A singular matrix is a square matrix that is not invertible, meaning it does not have an inverse. In other words, if \(A\) is a square matrix (same number of rows and columns), and there exists no matrix \(B\) such that \(AB = BA = I\), where \(I\) is the identity matrix, then \(A\) is singular.

Mathematically, a square matrix \(A\) is singular if and only if its determinant is zero (\(\det(A) = 0\)). The determinant being zero implies that the columns (or rows) of the matrix are linearly dependent, and therefore, the matrix cannot be inverted.

\[ A \text{ is singular} \iff \det(A) = 0 \]

Singular matrices play a crucial role in linear algebra, and their properties are fundamental in understanding systems of linear equations and transformations. If a system of linear equations has a singular coefficient matrix, it may not have a unique solution, and if a linear transformation is represented by a singular matrix, it may not be one-to-one or onto.

**What is a norm of a vector/matrix? Define the following norms: L1, L2, Frobenius**

The norm of a vector or matrix is a measure of its size or magnitude. It is a function that assigns a non-negative value to the vector or matrix, typically satisfying certain properties such as non-negativity, homogeneity, and the triangle inequality. Different norms exist, each capturing different aspects of the size of the vector or matrix.

- **L1 Norm (Norma L1):** The L1 norm of a vector \(\mathbf{\vec{v}}\) is the sum of the absolute values of its components. For a matrix, it is the maximum absolute column sum. Mathematically, for a vector \(\mathbf{\vec{v}} = [v_1, v_2, \ldots, v_n]\) and a matrix \(A\):

  $$\|\mathbf{\vec{v}}\|_{1} = \sum_{i=1}^n |v_{i}|$$
  $$\|A\|_{1} = \max_{1 \leq j \leq n} \sum_{i=1}^m |a_{ij}|$$

- **L2 Norm (Euclidean norm):** The L2 norm of a vector \(\mathbf{\vec{v}}\) is the square root of the sum of the squares of its components. For a matrix, it is the square root of the sum of the squares of its singular values. Mathematically:

  $$\|\mathbf{\vec{v}}\|_2 = \sqrt{v_{1}^2 + v_{2}^2 + \ldots + v_{n}^2}$$
  $$\|A\|_2 = \sqrt{\sigma_1^2 + \sigma_2^2 + \ldots + \sigma_r^2}$$

- **Frobenius norm:** The Frobenius norm of a matrix \(A\) is the square root of the sum of the squares of its elements. Mathematically:

  \[ \|A\|_F = \sqrt{\sum_{i=1}^m \sum*{j=1}^n |a*{ij}|^2} \]

These norms provide different ways to measure the magnitude or size of vectors and matrices, and the choice of norm depends on the specific application or context.

**What vectors are orthogonal, orthonormal? What matrix is called orthogonal? What are its properties?**

**Orthogonal vectors:** Two vectors \(\mathbf{\vec{v}}\) and \(\mathbf{\vec{w}}\) in an inner product space are orthogonal if their dot product is zero:

\[ \mathbf{\vec{v}} \cdot \mathbf{\vec{w}} = 0 \]

**Orthonormal vectors:** A set of vectors \(\{\mathbf{\vec{v}}\_1, \mathbf{\vec{v}}\_2, \ldots, \mathbf{\vec{v}}\_n\}\) is orthonormal if each vector has a magnitude of 1 (unit vector) and every pair of distinct vectors is orthogonal:

\[ \|\mathbf{\vec{v}}\_i\| = 1 \]
\[ \mathbf{\vec{v}}\_i \cdot \mathbf{\vec{v}}\_j = 0 \quad \text{for } i \neq j \]

**Orthogonal matrix:** An orthogonal matrix is a square matrix \(Q\) whose columns (and rows) are orthonormal vectors. The inverse of an orthogonal matrix is its transpose:

\[ Q^T = Q^{-1} \]

**Properties of orthogonal matrices:**

- **Orthogonality preservation:** If \(Q\) is orthogonal, then the columns (and rows) of \(Q\) form an orthonormal set.

- **Length preservation:** Orthogonal matrices preserve vector lengths, meaning if \(\mathbf{\vec{v}}\) is a vector, then \(\|Q\mathbf{\vec{v}}\| = \|\mathbf{\vec{v}}\|\).

- **Angle preservation:** If \(\mathbf{\vec{v}}\) and \(\mathbf{\vec{w}}\) are vectors, then the angle between them is the same as the angle between \(Q\mathbf{\vec{v}}\) and \(Q\mathbf{\vec{w}}\).

- **Determinant preservation:** The determinant of an orthogonal matrix is either 1 or -1.

Orthogonal matrices have numerous applications, particularly in transformations and solving systems of linear equations. They provide a geometrically meaningful way to represent rotations and reflections in linear algebra.

**What is an eigenvector of a matrix $A$?**

Given a square matrix \(A\), a non-zero vector \(\mathbf{\vec{v}}\) is called an eigenvector of \(A\) if the product of \(A\) and \(\mathbf{\vec{v}}\) is a scalar multiple of \(\mathbf{\vec{v}}\):

\[ A\mathbf{\vec{v}} = \lambda \mathbf{\vec{v}} \]

Here, \(\lambda\) is the eigenvalue associated with the eigenvector \(\mathbf{\vec{v}}\).

Eigenvectors are important in the study of linear transformations represented by matrices. They represent directions in space that remain unchanged, except for a scaling factor, when the linear transformation is applied. The corresponding eigenvalues (\(\lambda\)) indicate the amount of scaling along each eigenvector direction.

The equation \(A\mathbf{\vec{v}} = \lambda \mathbf{\vec{v}}\) can be rearranged as \((A - \lambda I)\mathbf{\vec{v}} = \mathbf{0}\), where \(I\) is the identity matrix. The non-trivial solutions to this equation (i.e., solutions where \(\mathbf{\vec{v}}\) is not the zero vector) exist only if the matrix \((A - \lambda I)\) is singular, leading to the characteristic equation \(\det(A - \lambda I) = 0\). The roots of this characteristic equation are the eigenvalues of the matrix \(A\), and for each eigenvalue, there exists a corresponding eigenvector.

**Write the formula for eigendecomposition of a matrix $A$, explain the formula.**

The eigendecomposition of a square matrix \(A\) involves expressing it as a product of three matrices: a matrix of its eigenvectors, a diagonal matrix of its eigenvalues, and the inverse of the matrix of eigenvectors (or its transpose if the eigenvectors are orthogonal).

**Formula:**
\[ A = P \Lambda P^{-1} \]

Here:

- \(A\) is the original square matrix.
- \(P\) is the matrix containing the eigenvectors of \(A\) as columns.
- \(\Lambda\) is a diagonal matrix containing the eigenvalues of \(A\).

**Explanation:**

1. **Eigenvectors Matrix (\(P\)):** The matrix \(P\) is formed by arranging the eigenvectors of \(A\) as its columns. Each column of \(P\) corresponds to an eigenvector of \(A\).

2. **Eigenvalues Matrix (\(\Lambda\)):** The matrix \(\Lambda\) is a diagonal matrix where the diagonal elements are the eigenvalues of \(A\). If \(\lambda_1, \lambda_2, \ldots, \lambda_n\) are the eigenvalues, then \(\Lambda\) looks like:
   \[ \Lambda = \begin{bmatrix} \lambda_1 & 0 & \ldots & 0 \\ 0 & \lambda_2 & \ldots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \ldots & \lambda_n \end{bmatrix} \]

3. **Inverse or Transpose of Eigenvectors Matrix (\(P^{-1}\) or \(P^T\)):** The matrix \(P^{-1}\) (inverse of \(P\)) is used if the eigenvectors are not necessarily orthogonal. If the eigenvectors are orthogonal (and \(P\) is an orthogonal matrix), then \(P^{-1} = P^T\) (transpose of \(P\)).

The eigendecomposition is particularly useful when the matrix \(A\) has a full set of linearly independent eigenvectors, allowing for the diagonalization of \(A\). It simplifies computations involving powers of \(A\) and can reveal important insights into the behavior of linear transformations represented by \(A\). Keep in mind that not all matrices are diagonalizable, and the eigendecomposition exists only for certain types of matrices.

**What is the eigendecomposition of a real symmetric matrix?**
Is the orthogonal matrix of its own

**What is the minimum/maximum of the function $f(\vec{x})=\vec{x}^{T}A\vec{x}$ subject to $‖\vec{x}‖_{2}=1$? For what x this function reaches its minimum/maximum?**

**What matrix is positive definite, positive semidefinite, negative definite, negative semidefinite?**

**Write the formula for singular value decomposition of a matrix $A$, explain the formula.**

**What is the Moore pseudoinverse? How to compute it? What are the solutions of linear equations using this pseudoinverse of a rectangular matrix?**

**Describe the trace operator and its properties.**

**What is the determinant of a matrix? What does the determinant say about its matrix?**

**Write the steps (formulas) of the PCA algorithm derivation and explain it.**

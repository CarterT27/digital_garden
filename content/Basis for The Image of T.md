---
mathLink: auto
tags:
  - "#Type/Theorem"
  - "#Topic/Linear_Algebra"
  - "#Class/MATH_31AH"
---
Proved by: <i>Not Applicable</i>  
References: <i>Not Applicable</i>  
Justifications: <i>Not Applicable</i>  

Specializations: <i>Not Applicable</i>  
Generalizations: <i>Not Applicable</i>  

> [!theorem] Basis for the Image of T
> The [[pivotal columns]] of $[T]$ form a [[basis]] for $\text{img }T$.

*Example:* Consider the matrix $A$ below, which describes a [[linear transformation]] from $\mathbb{R}^5$ to $\mathbb{R}^4$.  
$$A=\begin{bmatrix}1 & 2 & 4 & -1 & 2 \\-1 & 0 & -2 & -1 & 1 \\2 & 0 & 4 & 2 & 1 \\1 & 1 & 3 & 0 & 2\end{bmatrix}\text{, which row reduces to }\tilde{A}=\begin{bmatrix}1 & 0 & 2 & 1 & 0 \\0 & 1 & 1 & -1 & 0 \\0 & 0 & 0 & 0 & 1 \\0 & 0 & 0 & 0 & 0\end{bmatrix}.$$
The pivotal 1's of the row-reduced matrix $\tilde{A}$ are in columns 1, 2, and 5, so columns 1, 2, and 5 of the original matrix $A$ are a basis for the image. We can express any vector in the image of $A$ uniquely as a [[linear combination]] of those three [[Point, Vector, and Coordinates|vectors]]. For instance, $\vec{w}=2\vec{a}_{1}+\vec{a}_{2}-\vec{a}_{3}+2\vec{a}_{4}-3\vec{a}_{5}$, can be written  
$$\vec{w}=\begin{bmatrix}-8 \\-5 \\1 \\6\end{bmatrix}=2\begin{bmatrix}1 \\-1 \\2 \\1\end{bmatrix}-2\begin{bmatrix}2 \\0 \\0 \\1\end{bmatrix}-3\begin{bmatrix}2 \\1 \\1 \\2\end{bmatrix}.$$  
Note that each vector in the [[basis]] for the [[Image of Linear Transformation|image]] has four entries, as it must, since the image is a [[Subspace of R^n|subspace]] of $\mathbb{R}^4$. But the image is not of course $\mathbb{R}^4$; a basis for $\mathbb{R}^4$ must have four elements.

---

**Proof.**
Let $A=[\vec{a}_{1},\dots,\vec{a}_{m}]$.  
1. The *pivotal columns of* $A$ (in fact, all columns of $A$) are in the image, since $A\vec{e}_{i}=\vec{a}_{i}$.
2. The *pivotal columns are linearly independent*.
3. The *pivotal columns span the image*, since each nonpivotal column is a linear combination of the preceding pivotal ones. Suppose the $k$th column of $A$ is nonpivotal. View the first $k$ columns of $A$ as an augmented matrix, i.e., try to express the $k$th column as a linear combination of the earlier ones. Row reduce the submatrix of $A$ consisting of the first $k$ columns, which is the same thing as considering the first $k$ columns of $\tilde{A}$. Since the $k$th column is nonpivotal, there is no pivotal 1 in the last column, so it is possible to express the $k$th column of $A$ as a linear combination of the earlier ones, and in fact the entries of the $k$th column of $\tilde{A}$ tell us how to express it as a linear combination of the earlier pivotal columns.
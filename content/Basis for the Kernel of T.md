---
mathLink: auto  
tags:  
- "Type/Theorem"  
- "Topic/Linear_Algebra"  
- "Class/MATH_31AH"  
---
Proved by: <i>Not Applicable</i>  
References: <i>Not Applicable</i>  
Justifications: <i>Not Applicable</i>  
  
Specializations: <i>Not Applicable</i>  
Generalizations: <i>Not Applicable</i>  
  
> [!theorem] Basis for the [[Kernel]] of T.  
> Let $p$ be the number of nonpivotal columns of $A$, and $k_{1},\dots,k_{p}$ their positions. For each nonpivotal column, form the [[Point, Vector, and Coordinates|vector]] $\vec{v}_{i}$ satisfying $A\vec{v}_{i}=\vec{0}$ and such that its $k_{i}$th entry is 1, and its $k_{j}$th entries are all 0, for $j\neq i$. The vectors $\vec{v}_{1},\dots,\vec{v}_{p}$ form a basis of $\text{ker }A$.  
  
*Example:* Consider the matrix $A$ below, which describes a [[linear transformation]] from $\mathbb{R}^5$ to $\mathbb{R}^4$.  
$$A=\begin{bmatrix}1 & 2 & 4 & -1 & 2 \\-1 & 0 & -2 & -1 & 1 \\2 & 0 & 4 & 2 & 1 \\1 & 1 & 3 & 0 & 2\end{bmatrix}\text{, which row reduces to }\tilde{A}=\begin{bmatrix}1 & 0 & 2 & 1 & 0 \\0 & 1 & 1 & -1 & 0 \\0 & 0 & 0 & 0 & 1 \\0 & 0 & 0 & 0 & 0\end{bmatrix}.$$  
The third and fourth columns of $A$ are nonpivotal, so $k_{1}=3$ and $k_{2}=4$. The system has a unique solution for any values we choose of the third and fourth unknowns. In particular, there is a unique vector $\vec{v}_{1}$ whose third entry is 1 and fourth entry is 0, such that $A\vec{v}_{1}=\vec{0}$. There is another, $\vec{v}_{2}$, whose fourth entry is 1 and third entry is 0, such that $A\vec{v}_{2}=\vec{0}$:  
$$\vec{v}_{1}=\begin{bmatrix}-\\-\\1\\0\\-\end{bmatrix},\vec{v}_{2}=\begin{bmatrix}-\\-\\0\\1\\-\end{bmatrix}.$$  
The first, second, and fifth entries of $\vec{v}_{1}$ and $\vec{v}_{2}$ correspond to the pivotal unknowns. We read their values from the first three rows of $[\tilde{A}|\tilde{0}]$ (remembering that a solution for $\tilde{A}\vec{x}=\tilde{0}$ is also a solution for $A\vec{x}=\vec{0}$):  
$$[\tilde{A}|\tilde{0}]=\begin{bmatrix}1&0&2&1&0&0\\0&1&1&-1&0&0\\0&0&0&0&1&0\\0&0&0&0&0&0\end{bmatrix},$$  
that is,  
$$x_{1}+2x_{3}+x_{4}=0$$  
$$x_{2}+x_{3}-x_{4}=0$$  
$$x_{5}=0,$$  
which gives  
$$x_{1}=-2x_{3}-x_{4}$$  
$$x_{2}=x_{4}-x_{3}$$  
$$x_{5}=0.$$  
So for $\vec{v}_{1}$, where $x_{3}=1$ and $x_{4}=0$, the first entry is $x_{1}=-1$, the second is $-1$ and the fifth is $0$; the corresponding entries for $\vec{v}_{2}$ are $-3,-2,\text{ and }0$:  
$$\vec{v}_{1}=\begin{bmatrix}-2\\-1\\1\\0\\0\end{bmatrix};\vec{v}_{2}=\begin{bmatrix}-1\\1\\0\\1\\0\end{bmatrix}.$$  
These two vectors form a basis of the kernel of $A$.  

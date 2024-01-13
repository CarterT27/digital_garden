---
aliases: right inverse, left inverse
mathLink: auto
tags:
  - "Type/Definition"
  - "Topic/Linear_Algebra"
  - "Class/MATH_31AH"
---
Types: <i>Not Applicable</i>  
Examples: <i>Not Applicable</i>  
Constructions: <i>Not Applicable</i>  
Generalizations: <i>Not Applicable</i>  

Properties: <i>Not Applicable</i>  
Sufficiencies: <i>Not Applicable</i>  
Equivalences: <i>Not Applicable</i>  
Justifications: <i>Not Applicable</i>  

> [!definition] Left and Right Inverses of Matrices
> Let $A$ be a [[matrix]]. If there is a matrix $B$ such that $BA=I$, then $B$ is a *left inverse* of $A$. If there is a matrix $C$ such that $AC=I$, then $C$ is a *right inverse* of $A$.

*Example:* The matrix $\begin{bmatrix}1&0\\0&0\end{bmatrix}$ does not have a right or left inverse. To see this, assume it has a right inverse. Then there exists a matrix $\begin{bmatrix}a&b\\c&d\end{bmatrix}$ such that $$\begin{bmatrix}1 & 0 \\
0 & 0\end{bmatrix}\begin{bmatrix}a & b \\
c & d\end{bmatrix}=\begin{bmatrix}1 & 0 \\
0 & 1\end{bmatrix}.$$
But that product is $\begin{bmatrix}a&b\\0&0\end{bmatrix}$, with 0 in the bottom right corner, not the required 1. A similar computation shows that there is no left inverse.

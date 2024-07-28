---
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

Properties: [[Noncommutativity of Matrix Multiplication]], [[The ith Column of A is Aei]], [[The ith Column of AB is Abi]], [[The ith Row of AB is the Product of The ith Row of A and Matrix B]], [[Matrix Multiplication is Associative]]  
Sufficiencies: <i>Not Applicable</i>  
Equivalences: <i>Not Applicable</i>  
Justifications: <i>Not Applicable</i>  

> [!definition] Matrix Multiplication  
> If $A$ is an $m \times n$ [[Matrix]] whose $(i,j)$th entry is $a_{i,j}$ and $B$ is an $n \times p$ matrix whose $(i,j)$th entry is $b_{i,j}$, then $C=AB$ is the $m \times p$ matrix with entries  
> $$c_{i,j}=\sum_{k=1}^{n}a_{i,k}b_{k,j}$$  
> $$=a_{i,1}b_{1,j}+a_{i,2}b_{2,j}+\dots+a_{i,n}b_{n,j}.$$  

*Example:* $$A=\begin{bmatrix}1 & 0 \\  
2 & 3\end{bmatrix},B=\begin{bmatrix}0 & 1 \\  
0 & 1\end{bmatrix}$$  
$$AB=\begin{bmatrix}1 & 0 \\  
2 & 3\end{bmatrix}\begin{bmatrix}0 & 1 \\  
0 & 1\end{bmatrix}=\begin{bmatrix}1(0)+0(0) & 1(1)+0(1) \\  
2(0)+3(0) & 2(1)+3(1)\end{bmatrix}=\begin{bmatrix}0 & 1 \\  
0 & 5\end{bmatrix}$$  

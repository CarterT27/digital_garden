---
tags:
- "Type/Note"
- "Topic/Differential_Equations"
- "Class/MATH_20D"
date:
- 2024-02-12
---
> [!note] Eigenvalues and Eigenvectors.  
> Let $A$ be an $n\times n$ matrix. If there exists a non-zero vector $\vec{x}$ such that $A\vec{x}=\lambda\vec{x}$ for some scalar $\lambda$ then  
> - The scalar $\lambda$ is called an **eigenvalue** of $A$.  
> - The vector $\vec{x}$ is called an **eigenvector** of $A$.  

> [!note] Remark  
> - In general, given any $n\times n$ matrix, $A$. A scalar $\lambda$ is an eigenvalue of $A$ iff the homogeneous equation $(A-\lambda I)\vec{x}=\vec{0}$ has a non-trivial solution $\vec{x}$.  
> - The homogeneous equation has a non-trivial solution iff $(A-\lambda I)$ is singular, which in turn is equivalent to $det(A-\lambda I)=0$.  
> - The equation $det(A-\lambda I)=0$ is called the **characteristic equation** of the matrix $A$. The solutions to the characteristic equation are the eigenvalues of $A$.  
> - For each eigenvalue $\lambda$, we can find the corresponding eigenvector $\vec{x}_\lambda$ by solving the equation $(A-\lambda I)\vec{x}=\vec{0}$  

> [!note] Algebraic and Geometric Multiplicity  
> Suppose $A$ is an $n\times n$ matrix with $n$ eigenvalues $\lambda_1,\lambda_2,\dots,\lambda_n$, some of them may be repeated.  
> - If one of the $\lambda_i$ appears $k$ times as a root to the characteristic equation $det(A-\lambda I)=0$ then we say $\lambda_i$ has **algebraic multiplicity** $k$.  
> - If an eigenvalue $\lambda_i$ gives rise to $p$ linearly independent eigenvectors, then we say that $\lambda_i$ has **geometric multiplicity** $p$.  

> [!note] Homogeneous Linear Systems with Constant Coefficients  
> Suppose the $n\times n$ matrix $A$ has eigenvalues $\lambda_1,\lambda_2,\dots,\lambda_n$ (some of them may be repeated) and $n$ **linearly independent** eigenvectors $\vec{x_1},\vec{x_2},\dots,\vec{x_n}$. Then the general solution to the homogeneous system $\vec{x}'=A\vec{x}$ is given by $$\vec{x}(t)=C_1e^{\lambda_1t}\vec{x_1}+C_2e^{\lambda_2t}\vec{x_2}+\dots+C_ne^{\lambda_nt}\vec{x_n}$$  
> where $C_i$'s are arbitrary constants.  


---
tags:
- "Type/Note"
- "Topic/Differential_Equations"
- "Class/MATH_20D"
date:
- 2024-02-21
---
> [!note] Case 5a. $A$ has repeated eigenvalue $\lambda>0$ and one independent eigenvector  
> - Origin is an improper source/degenerate source  
> - Unstable b/c only eigenvalue we have is $>0$  

> [!note] Case 5b. $A$ has repeated eigenvalue $\lambda<0$ and one independent eigenvector  
> - Origin is an improper source/degenerate source  
> - Stable b/c only eigenvalue we have is $>0$  

> [!note] Fundamental matrix  
> $\begin{bmatrix}\vert&\vert\\\vec{x}^{(1)}&\vec{x}^{(2)}\\\vert&\vert\end{bmatrix}=\begin{bmatrix}e^{2t}&0\\0&e^{2t}\end{bmatrix}=\Psi$  

# $2\times2$ Systems with Repeated Eigenvalues  

Let $A=\begin{bmatrix}2&0\\0&2\end{bmatrix}$ with repeated eigenvalue $\lambda_1=\lambda_2=2,\vec{v}_1=\begin{bmatrix}1\\0\end{bmatrix},\vec{v}_2=\begin{bmatrix}0\\1\end{bmatrix}$.  
Then the general solution to the system $\vec{x}'=A\vec{x}$ is given by  
$$y=C_1e^{2t}\begin{bmatrix}1\\0\end{bmatrix}+C_2e^{2t}\begin{bmatrix}0\\1\end{bmatrix}$$  

Let $A=\begin{bmatrix}2&1\\4&6\end{bmatrix}$ with repeated eigenvalue $\lambda=4$ and eigenvector $\vec{v}=\begin{bmatrix}1\\-1\end{bmatrix}$. Find the general solution to the system $\vec{x}'=A\vec{x}$  
- We can still obtain one solution $\vec{x}^{(1)}=e^{\lambda t}\vec{v}\Rightarrow \vec{x}^{(1)}e^{4t}\begin{bmatrix}1\\-2\end{bmatrix}$  
- Next, we generate another solution $\vec{x}^{(2)}$ based on our current eigenvalue/eigenvector  
WARNING: The second solution won't be as nice as $t\vec{x}^{(1)}$ as we saw earlier  

> [!definition] Generalized Eigenvector of $A$ with rank $k$  
> Let $A$ be an $n\times n$ matrix and suppose that $\lambda$ is an eigenvalue of $A$. We say that a nonzero vector $\vec{v}_k$ is a **generalized eigenvector of $A$ with rank $k$** (corresponding to $\lambda$) provided that $$(A-\lambda I)^k\vec{v}_k=0\text{ but }(A-\lambda I)^i\vec{v}_k\neq0$$ for all integers $0\leq i<k$.  

> [!note] Jordan Chain of Independent Vectors  
> If $\vec{v}_k$ is a generalized eigenvector of $A$ with rank $k$ then there exists a **Jordan Chain** of **independent** vectors $\vec{v}_1,\vec{v}_2,\dots,\vec{v}_k$ (corresponding to $\lambda$) such that  
> $$(A-\lambda I)\vec{v}_1=0\text{ (here, }\vec{v}_1\text{ is an eigenvector of }A)$$  
> $$(A-\lambda I)\vec{v}_2=\vec{v}_1$$  
> $$(A-\lambda I)\vec{v}_3=\vec{v}_2$$  
> $$\vdots$$  
> $$(A-\lambda I)\vec{v}_k=\vec{v}_{k-1}$$  
> Note: An eigenvector is a generalized eigenvector of rank 1  

> [!note] Fact  
> If $\vec{v}_1,\vec{v}_2,\dots$ is a Jordan chain of $A$ corresponding to $\lambda$ then  
> $\vec{x}_1=e^{\lambda t}\vec{v}_1$  
> $\vec{x}_2=e^{\lambda t}(t\vec{v}_1+\vec{v}_2)$  
> $\vec{x}_3=e^{\lambda t}(\frac{t^2}{2!}\vec{v}_1+t\vec{v}_2+\vec{v}_3)$  
> $\vec{x}_4=e^{\lambda t}(\frac{t^3}{3!}\vec{v}_1+\frac{t^2}{2!}\vec{v}_2+t\vec{v}_3+\vec{v}_4)$  
> $\vdots$  
> $\vec{x}_k=e^{\lambda t}(\frac{t^{k-1}}{(k-1)!}\vec{v}_1+\frac{t^{k-2}}{(k-2)!}\vec{v}_2+\dots+\frac{t^2}{2!}\vec{v}_{k-2}+t\vec{v}_{k-1}+\vec{v}_k)$  
> are all solutions to $\vec{x}'=A\vec{x}$  

Basically, if $A$ is a $2\times2$ with repeated eigenvalue and only one eigenvector $\vec{v}_1$, then the second solution is given by $$\vec{x}_2=e^{\lambda t}(t\vec{v}_1+\vec{v}_2)$$  
where $\vec{v}_2$ is the solution to $(A-\lambda I)\vec{v}_2=\vec{v}_1$  

---  

## Summary  

Consider a system of two first-order ODEs  
$$x_1'=ax_1+bx_2$$  
$$x_2'=cx_1+dx_2$$  
The equivalent matrix form (normal form) of this system is given by  
$$\vec{x}'=\begin{bmatrix}a&b\\c&d\end{bmatrix}\vec{x}.$$  
There are three cases:  
1. $A$ has two distinct, real eigenvalues  
Let $\lambda_1,\lambda_2$ be the eigenvalues, and let $\vec{v}_1,\vec{v}_2$ be the corresponding eigenvector. Then the general solution to $\vec{x}'=A\vec{x}$ is given by  
$$\vec{x}=C_1e^{\lambda_1 t}\vec{v}_1+C_2e^{\lambda_2 t}\vec{v}_2$$  
2. $A$ has complex eigenvalues  
Here, the eigenvalues and eigenvectors must occur as conjugate pairs. So we let $\lambda_{1,2}=\alpha\pm i\beta$ denote the eigenvalues and $\vec{v}_{1,2}=\vec{a}\pm i\vec{b}$ denote the corresponding eigenvectors. Then the general solution to $\vec{x}'=A\vec{x}$ is given by  
$$\vec{x}=C_1e^{\alpha t}(\vec{a}\cos{(\beta t)}-\vec{b}\sin{(\beta t)})+C_2e^{\alpha t}(\vec{a}\sin{(\beta t)}+\vec{b}\cos{(\beta t)})$$  
3. A has repeated eigenvalue $\lambda_1=\lambda_2=\lambda$ There are two sub-cases:  
3a. If $\lambda$ has two linearly independent eigenvectors $\vec{v}_1,\vec{v}_2$. Then the general solution to $\vec{x}'=A\vec{x}$ is given by  
$$\vec{x}=C_1e^{\lambda t}\vec{v}_1+C_2e^{\lambda t}\vec{v}_2$$  
3b. If $\lambda$ has only one eigenvector $\vec{v}$ then we need to solve the system of algebraic equations  
$$(A-\lambda I)\vec{v}_2=\vec{v}_1$$  
for any solution $\vec{v}_2$. Then the general solution to $\vec{x}'=A\vec{x}$ is  
$$\vec{x}=C_1e^{\alpha t}\vec{v}_1+C_2e^{\lambda t}(t\vec{v}_1+\vec{v}_2)$$  

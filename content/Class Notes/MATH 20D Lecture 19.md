---
tags:
- "Type/Note"
- "Topic/Differential_Equations"
- "Class/MATH_20D"
date:
- 2024-02-23
---
# Section 9.7 - Solving Non-Homogeneous Linear Systems  

A non-homogeneous linear system has the form $\vec{x}'=A\vec{x}+\vec{g}$, where $\vec{g}\neq\vec{0}$.  
The general solution to this equation is given by  
$$\vec{x}=\vec{x}_H+\vec{x}_P$$  
where  
- $\vec{x}_H$ is the general solution to the corresponding homogeneous equation $\vec{x}'=A\vec{x}$ and  
- $\vec{x}_P$ is a particular solution to $\vec{x}'=A\vec{x}+\vec{g}$  
This is known, again, as the **Superposition Principle**.  

> [!definition] Let $A$ be an $n\times n$ matrix and let $\vec{x}_1(t),\vec{x}_2(t),\dots,\vec{x}_n(t)$ be $n$ linearly independent solutions to the homogeneous system $\vec{x}'=A\vec{x}$. Then the **fundamental matrix** for the system $\vec{x}'=A\vec{x}$ is given by  
$$\Psi(t)=\begin{bmatrix}\vert&\vert& &\vert\\\vec{x}_1(t)&\vec{x}_2(t)&\dots&\vec{x}_n(t)\\\vert&\vert& &\vert\end{bmatrix}.$$  
The general solution of $\vec{x}'=A\vec{x}$ can be expressed as  
$$\vec{x}(t)=C_1\vec{x}_1+\dots+C_n\vec{x}_n=\begin{bmatrix}\vec{x}_1&\dots&\vec{x}_n\end{bmatrix}\begin{bmatrix}C_1\\C_2\\\vdots\\C_n\end{bmatrix}=\Psi(t)\begin{bmatrix}C_1\\C_2\\\vdots\\C_n\end{bmatrix}$$  

> [!note] Variations of Parameters  
> Look for a particular solution of the form  
> $$\vec{x}_P=\Psi(t)\vec{u}\text{ where }\Psi(t)\vec{u}'=\vec{g}.$$  
> Steps:  
> 1. Write down $\vec{x}_H$, form the fundamental matrix $\Psi(t)$, and find its inverse  
> 2. Find $\vec{u}'=\Psi^{-1}(t)\vec{g}$  
> 3. Find $\vec{u}$ by integrating $\vec{u}'$  
> 4. Compute $\vec{x}_P=\Psi(t)\vec{u}$  
> 5. Obtain the general solution $\vec{x}=\vec{x}_H+\vec{x}_P$  

> [!note] Undetermined Coefficients  
> Applicable to non-homogeneous linear system $\vec{x}'=A\vec{x}(t)+\vec{g}(t)$ where  
> - $A$ is a matrix with **constant** entries  
> - All entries of $\vec{g}(t)$ are polynomials, exponentials, sines and cosines, or sums and products of the three  
> Steps:  
> 1. Write down $\vec{x}_H$ and form the fundamental matrix $\Psi(t)$  
> 2. Make an initial guess for $\vec{x}_P$ based on the form of the RHS $\vec{g}$  
> 3. Solve for the coefficients in our guess for $\vec{x}_P$  
> 4. Obtain the general solution $\vec{x}=\vec{x}_H+\vec{x}_P$  

> [!note] Issues w/ Undetermined Coefficient Method  
> 1. When $\vec{g}$ consists of more than one type of exponential  
> 2. When there's "conflict" b/w $\vec{g}$ and $\Psi$  

---
tags:
- "Type/Note"
- "Topic/Differential_Equations"
- "Class/MATH_20D"
date:
- 2024-03-15
---
> [!note] Solving Non-Homogeneous Systems  
> 1. Find evals/evects of $A$ then form $\vec{x}_H=c_1e^{\lambda_1t}\vec{v}_1+c_2e^{\lambda_2t}\vec{v}_2$  
> 2. Form fundamental matrix $\psi=\begin{bmatrix}\vert&\vert\\e^{\lambda_1t}\vec{v}_1&e^{\lambda_2t}\vec{v}_2\\\vert&\vert\end{bmatrix}$  
> 3. Find the inverse $\psi^{-1}$  
> 4. Compute $\vec{u}'=\psi^{-1}\cdot g$ then $\vec{u}=\int\vec{u}'$  
> 5. $\vec{x}_P=\psi\cdot\vec{u}$  

> [!note] Exercise. Find the general solution to the non-homogeneous systems $$\vec{x}'(t)=A\vec{x}(t)+\vec{g}=\begin{bmatrix}2&-1\\3&-2\end{bmatrix}\vec{x}+\begin{bmatrix}e^t\\-e^t\end{bmatrix}$$  

$u(t-a)=u_a(t)=\begin{cases}0\text{ if }t<a\\1\text{ if }t\geq a\end{cases}$  
$u_0(t)=u(t)$  

> [!note] Example. Find the Laplace transform of $f(t)=\begin{cases}3t^2-2,t<4\\e^{5t}+t,4\leq t<9\\0,\text{ otherwise}\end{cases}$  
> $f(t)=[u_\infty(t)-u_4(t)](3t^2-2)+[u_4(t)-u_9(t)](e^{5t}+t)+[u_9(t)-u_\infty(t)](0)$  

> [!note] Example. Solve the IVP $y''-6y'=\delta(t-1)-u_4(t),y(0)=-4,y'(0)=0$.  

> [!note] Exercise. Solve the IVP $y'''-y'=0,y(0)=0,y'(0)=1,y''(0)=-1$.  

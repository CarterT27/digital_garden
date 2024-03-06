---
tags:
- "Type/Note"
- "Topic/Calculus"
- "Class/MATH_20C"
date:
- 2024-03-04
---
# 14.8 Lagrange Multipliers  

> [!note] Theorem  
> Assume $f(x,y)$ and $g(x,y)$ are differentiable.  
> If $f(x,y)$ has a local max or min on the constraint curve $g(x,y)=C$ at $P=(a,b)$ and if $\nabla g_p\neq\vec{0}$ then there is a scalar $\lambda$ s.t. $$\nabla f_p=\lambda\nabla g_p$$  
> - $\lambda$ is called the **Lagrange multiplier**  
> - The equation is called **Lagrange condition/equations**.  
>  
> Explicitly,  
>  
> $f_x(a,b)=\lambda g_x(a,b)$  
> $f_y(a,b)=\lambda g_y(a,b)$  

> [!note] Critical Point, Critical Value  
> Constraint Condition $g(a,b)=C$  
> A point $P=(a,b)$ satisfying the above equations is called a **critical point** for the optimization problem with a **constraint** and $f(P)$ is called a **critical value**.  

> [!note] Remark  
> If the constraint curve $g(x,y)=C$ is not bounded, $f(x,y)$ may **not** have a global max or min.  

> [!note] Lagrange Multiplier in three variables  
> The method of Lagrange multiplier also works in three variables.  
> We want to optimize $f(x,y,z)$ subject to the constraint $g(x,y,z)=C$  
> The critical points can be found by solving  
> $\begin{cases}\nabla f=\lambda\nabla g\\g=c\end{cases}=\begin{cases}f_x=\lambda g_x\\f_y=\lambda g_y\\f_z=\lambda g_z\\g=c\end{cases}$  

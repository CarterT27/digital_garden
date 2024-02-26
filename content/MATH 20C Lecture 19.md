---
tags:
- "Type/Note"
- "Topic/Calculus"
- "Class/MATH_20C"
date:
- 2024-02-23
---
# 14.6 - Multivariable Chain Rule  

> [!note] Theorem  
> Let $f(x_1,x_2,\dots,x_n)$ be a differentiable function of n variables.  
> Suppose $x_1,\dots,x_n$ are differentiable functions of m independent variables $t_1,\dots,t_m$  
> $f(x_1(t_1,\dots,t_m),x_2(t_1,\dots,t_m),\dots,x_n(t_1,\dots,t_m))$  
> Then for $k=1,\dots,m$  
> $$\frac{\partial f}{\partial t_k}=\frac{\partial f}{\partial x_1}\cdot\frac{\partial x_1}{\partial t_k}+\frac{\partial f}{\partial x_2}\cdot\frac{\partial x_2}{\partial t_k}+\frac{\partial f}{\partial x_n}\cdot\frac{\partial x_n}{\partial t_k}$$  

> [!note] Mnemonic  
> Ex: $f(x(s,t),y(s,t),z(s,t))$  
> ![[Screenshot 2024-02-26 at 3.01.53 AM.jpg]]  
> $\frac{\partial f}{\partial s}=\frac{\partial f}{\partial x}\cdot\frac{\partial x}{\partial s}+\frac{\partial f}{\partial y}\cdot\frac{\partial y}{\partial s}+\frac{\partial f}{\partial z}\cdot\frac{\partial z}{\partial s}$  

---  

Recall $F(x,y,z)=0$  
$\Rightarrow z$ is an **implicit function** of $x$ and $y$  

---  

# 14.7 Optimization  

> [!definition] Local Extreme Values  
> A function $f(x,y)$ has a **local extremum** at $P=(a,b)$ if there exists a neighborhood $D$ such that  
> - local maximum $$f(x,y)\leq f(a,b)\text{ for }(x,y)\in D$$  
> - local minimum $$f(x,y)\geq f(a,b)\text{ for }(x,y)\in D$$  

> [!definition] Critical Points  
> A point $P=(a,b)$ in the domain of $f(x,y)$ is called a **critical point** if  
> - $\nabla f(P)=\langle f_x(P),f_y(P)\rangle=\langle 0,0\rangle$  
> - $f_x(a,b)$ does not exist or $f_y(a,b)$ does not exist  

> [!note] Theorem  
> If $f(x,y)$ has a **local min/max** at $P=(a,b)$ then $(a,b)$ is a **critical point** of $f(x,y)$  

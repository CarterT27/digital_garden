---
tags:
- "Type/Note"
- "Topic/Calculus"
- "Class/MATH_20C"
date:
- 2024-02-21
---
# 14.5 - The Gradient and Partial Derivatives  

> [!definition] Directional Derivative  
> The **directional derivative** of $f$ at $P=(a,b)$ in the direction of the **unit vector** $\vec{u}=\langle h,k\rangle$ is  
> $$D_{\vec{u}}f(p)=D_{\vec{u}}f(a,b)=\frac{d}{dt}f(\vec{r}(t))\vert_{t=0}$$  

> [!note] Theorem  
> If $f$ is differentiable at $P$ and $\vec{u}$ is a **unit vector** then  
> $$D_{\vec{u}}f=\nabla f_p\cdot\vec{u}$$  
> (Recall $\nabla f_p=\langle f_x(a,b),f_y(a,b)\rangle$)  
> This formula holds for functions with two or three variables  
> Pf: $\vec{r}(t)\langle a+th,b+tk\rangle$  
> $\vec{u}=\langle h,k\rangle$  
> $D_\vec{u}f=\frac{d}{dt}(f(\vec{r}(t))\vert_{t=0}$  
> $=\nabla f_{\vec{r}(0)}\cdot\vec{r}'(0)$  
> $=\nabla f_p\cdot \langle h,k\rangle$  
> $=\nabla f_p\cdot\vec{u}$  

> [!note] Properties of the **directional derivative**  
> $D_\vec{u}f(p)$  
> Suppose $p$ and $f$ are given. Then it depends on $\vec{u}$  
> $D_\vec{u}f(p)=\nabla f_p\cdot\vec{u}$  
> $=\Vert\nabla f_p\Vert\Vert\vec{u}\Vert\cos{\theta}$  
> $=\Vert\nabla f_p\Vert\cos{\theta}$  

> [!note] Theorem  
> Assume $\nabla f_p\neq\vec{0}$. Let $\vec{u}$ be a unit vector. Then  
> $$D_\vec{u}f(p)=\Vert\nabla f_p\Vert\cos{\theta}$$  
> where $\theta$ is the angle between $\nabla f_p$ and $\vec{u}$  

> [!note] Properties of the **directional derivative** continued...  
> - $D_\vec{u}f(p)$ is maximal when $\theta=0$  
>   - In other words, $\vec{u}$ and $\nabla f_p$ point in the same direction.  
>   - $\nabla f_p$ points in the direction of the fastest rate of **increase** of $f$ at $P$, and this maximal rate is $\Vert\nabla f_p\Vert$  
> $$D_\vec{u}f(p)=\Vert\nabla f_p\Vert\cos{\theta}$$  
> - $D_\vec{u}f(p)$ is minimal when $\theta=\pi$.  
>   - In this case, $\vec{u}$ and $\nabla f_p$ point in the opposite direction  
>   - $\nabla f_p$ points in the direction of the fastest rate of decrease and the maximal rate of decrease is $\Vert\nabla f_p\Vert$  
> - $D_\vec{u}f(p)=0$ if $\theta=\frac{\pi}{2}$  
>   - $\nabla f_p$ is orthogonal to the level curve or surface of $f$ at $P$.  

## Tangent plane revisited  

Previously, we have an equation for the tangent plane of the graph of $z=f(x,y)$ (explicit function)  
In general, $F(x,y,z)=k$, with $k$ as a constant. We say $z$ is an **implicit function** of $x,y$.  

Explicit functions $z=f(x,y)$ are also implicit functions: $$f(x,y)-z=0$$  
The set $\{(x,y,z)\vert F(x,y,z)=k\}$ is the level surface of $F(x,y,z)$ in $\mathbb{R}^3$  
Note $\nabla F_p$ is perpendicular to the tangent plane.  

> [!note] Theorem  
> Let $P=(a,b,c)$ on the level surface $F(x,y,z)=k$  
> Then $\nabla F_p$ is a normal vector to the tangent plane to the surface at $P$. Moreover, the tangent plane has the equation:  
> $$F_x(P)(x-a)+F_y(P)(y-b)+F_z(P)(z-c)=0$$  
> Where $\nabla F_p=\langle F_x(P),F_y(P),F_z(P)\rangle$  

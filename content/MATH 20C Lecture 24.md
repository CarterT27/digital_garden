---
tags:
- "Type/Note"
- "Topic/Calculus"
- "Class/MATH_20C"
date:
- 2024-03-06
---
# 14.8  

> [!note] Find the closest point on the plane $x+y+2z=1$ to the origin  
> $g(x,y,z)=x+y+2z$  
> $f(x,y,z)=x^2+y^2+z^2$, distance squared  
> We want to find the global min of $f$ subject to the constraint $g=1$  
> It has to be a critical point obtained by solving  
> $$\begin{cases}\nabla f=\lambda\nabla g\\g=1\end{cases}\Rightarrow\begin{cases}f_x=\lambda g_x\\f_y=\lambda g_y\\f_z=\lambda g_z\\g=1\end{cases}\Rightarrow\begin{cases}2x=\lambda\\2y=\lambda\\2z=2\lambda\\x+y+2z=1\end{cases}$$  
> $$\Rightarrow\begin{cases}x=\frac{\lambda}{2}\\y=\frac{\lambda}{2}\\z=\lambda\end{cases}$$  
> Plug into $x+y+2z=1$  
> $\frac{\lambda}{2}+\frac{\lambda}{2}+2\lambda=1\Rightarrow3\lambda=1\Rightarrow\lambda=\frac{1}{3}$  
> Plug in $(x,y,z)=(\frac{1}{6},\frac{1}{6},\frac{1}{3})$  
> Since we only have one ctitical point and the global min exists, it has to be $(\frac{1}{6},\frac{1}{6},\frac{1}{3})$  

> [!note] Find the extreme values of $f(x,y)$ in the domain $D$  
> $D$ is bounded and closed $\Rightarrow$ $f$ has a global max and a global min in $D$  
> Step 1: find the interior critical points of $f$  
> Step 2: find the critical points on the boundary of $D$  
> Step 3: compare the values of $f$ of all these points  

# 15.1 Double Integral  

---  

Recall  
> [!definition] Single Integral  
> $\int_a^bf(x)dx$  
> Divide $[a,b]$ into $n$ subintervals of width $\Delta x=\frac{b-a}{n}$  
> Area over the i-th subinterval under the graph of $f(x)\approx f(p_i)\Delta x$  
> Riemann sum  
> $f(p_1)\Delta x+f(p_2)\Delta x+\dots+f(p_n)\Delta x=\sum_{i=1}^nf(p_i)\Delta x$  
> $\int_a^bf(x)dx=\lim_{n\to\infty}\sum_{i=1}^nf(p_i)\Delta x$  

---  

Let's consider functions of 2-variables  
Let $R=[a,b]\times[c,d]$ be the set of points $(x,y)$ s.t. $a\leq x\leq b,c\leq y\leq d$  
$\Rightarrow R$ is a rectangle  
We define the double integral $\int\int f(x,y)dA$ as the volume under the graph of $f(x,y)$ over $R$  

---  

Now let's define the double integral using Riemann sum  

Step 1 (subdivisions):  
- subdivide $[a,b]$ into $N$ subintervals of the same length $\frac{b-a}{N}$  
- subdivide $[c,d]$ into $M$ subintervals of the same length $\frac{d-c}{M}$  
This creates an $N\times M$ grid of subrectangles $R_{ij}$ in $R$.  

Step 2:  
next time  

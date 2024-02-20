---
tags:
- "Type/Note"
- "Topic/Calculus"
- "Class/MATH_20C"
date:
- 2024-02-16
---
# 14.5 Gradient and Directional Derivatives  

> [!note] Volume of a Rectangular Cuboid  
> $V=abc$  
> Suppose $V$ is computed using $a=1.1\text{m},b=2.2\text{m},c=0.9\text{m}$  
> Use the linear approx. to estimate the **maximal percentage error** $R$ in $V$ if each of these values has a possible percentage error of at most $2\%$  
> $\vert\bar{a}-a\vert=\Delta a\leq2\%a$  
>  
> Sol:  
> $\Delta V\approx V_a\Delta a+V_b\Delta b+V_c\Delta c$  
> $=bc\Delta a+ac\Delta b+ab\Delta c$  
> Maximal percentage erros in $a,b,c$ are 2%  
> $\frac{\Delta a}{a}=\frac{\Delta a}{1.1}=0.02,\frac{\Delta b}{b}=\frac{\Delta b}{2.2}=0.02,\frac{\Delta c}{c}=\frac{\Delta c}{0.9}=0.02$  
> $\Rightarrow\Delta a=0.022,\Delta b=0.044,\Delta c=0.018$  
> $\Rightarrow\Delta V\approx bc\Delta a+ac\Delta b+ab\Delta c$  
> Maximal error $=2.2\times0.9\times0.022+1.1\times0.9\times0.044+1.1\times2.2\times0.018=0.13068$  
> Maximal percentage error $\frac{\Delta V}{V}\times100\%=\frac{0.13068}{1.1\times2.2\times0.9}\times100\%=6\%$  

# 14.5  

Recall that  
$f_x=\frac{df}{dx}$ rate of change in the **x-direction**  
$f_y=\frac{df}{dy}$ rate of change in the **y-direction**  

> [!definition] Gradient  
> The **gradient** (vector) of $f(x,y)$ at $P=(a,b)$ is $\nabla f_p=\langle f_x(a,b),f_y(a,b)\rangle$  
> - $f(x,y,z)$ and $P=(a,b,c)$ define $\nabla f_p=\langle f_x(a,b,c),f_y(a,b,c),f_z(a,b,c)\rangle$  
> sometimes we omit reference to the point $P$  
> and $\Delta f=\langle\frac{df}{dx},\frac{df}{dy}\rangle$  
> or $\Delta f=\langle\frac{df}{dx},\frac{df}{dy},\frac{df}{dz}\rangle$  

> [!note] Properties of Gradient  
> $f,g$ differentiable (in 2 or 3 variables)  
> c constant, scalar valued  
> Then  
> 1. $\nabla(f+g)=\nabla f+\nabla g$  
> 2. $\nabla(cf)=c\nabla f$  
> 3. $\nabla(fg)=g\nabla f+f\nabla g$  
> 4. Chain Rule  
> $F(t)$ differentiable in $t$, then $$\nabla F(f(x,y))=F'(f(x,y))\nabla f(x,y)$$  
> or $\nabla F(f(x,y,z))=F'(f(x,y,z))\nabla f(x,y,z)$  
> 5. Chain rule for path  
> If $f$ and $\vec{r}(t)$ are differentiable $$\frac{d}{dt}f(\vec{r}(t))=\nabla f_{\vec{r}(t)}\cdot\vec{r}'(t)$$  

Let $\vec{u}$ be a unit vector.  
How do we measure the rate of change in the direction of $\vec{u}$?  
$\vec{r}(t)=\langle a,b\rangle+t\langle h,k\rangle=\langle a+th,b+tk\rangle$  

> [!definition] Directional Derivative  
> The **directional derivative** of $f(x,y)$ at $P=(a,b)$ in the direction of the unit vector $\vec{u}=\langle h,k\rangle (h^2+k^2=1)$ is $$D_{\vec{u}}f(P)=D_{\vec{u}}f(a,b)$$  
> $=\lim_{t\to0}\frac{f(a+ht,b+tk)-f(a,b)}{t}$  
> $=\frac{d}{dt}f(\vec{r}(t))\vert_{t=0}$  

> [!note] $D_{\vec{u}}f(P)=\nabla f_P\cdot\vec{u}$  

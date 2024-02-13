---
id: MATH 20D Lecture 14
aliases: []
tags:
- Type/Note
- Topic/Differential_Equations
- Class/MATH_20D
date:
- "2024-02-09"
---
# Section 9.1 - The Matrix Method  

> [!note] $ay''(t)+by'(t)+cy(t)=f(t),x_1(t)=y(t),x_2(t)=y'(t)$  
> If $x_2=y'=x_1'$  
> From the original ODE: $ay''+by'+cy=f(t)$  
> $ax_2'+bx_2+cx_1=f(1)\implies x_2'+\frac{b}{a}x_2+\frac{c}{a}x_1=f(t)/a$  
> $\implies x_2'=-\frac{c}{a}x_1-\frac{b}{a}x_2+\frac{f(i)}{a}$  
> System we obtain: $$x_1'=x_2$$ $$x_2'=-\frac{c}{a}x_1-\frac{b}{a}x_2+\frac{f(i)}{a}$$  
> Linear: $$\begin{bmatrix}x_1'\\x_2'\end{bmatrix}=\begin{bmatrix}0&1\\-\frac{c}{a}&-\frac{b}{a}\end{bmatrix}\begin{bmatrix}x_1\\x_2\end{bmatrix}+\begin{bmatrix}0\\\frac{f(t)}{a}\end{bmatrix}$$  
> Non-homogeneous system  

> [!note] $y^{(4)}+y=0,x_1=y,x_2=y',x_3=y'',x_4=y'''$  
> $$x_1'=x_2$$ $$x_2'=x_3$$ $$x_3'=x_4$$ $$x_4'=-x_1$$  
> From the given ODE: $y^{(4)}+y=0\to x_4'+x_2=0\to x_4'=-x_2$  
> $$\begin{bmatrix}x_1'\\x_2'\\x_3'\\x_4'\\\end{bmatrix}=\begin{bmatrix}x_1\\x_2\\x_3\\x_4\end{bmatrix}'=\begin{bmatrix}0&1&0&0\\0&0&1&0\\0&0&0&1\\-1&0&0&0\end{bmatrix}\begin{bmatrix}x_1\\x_2\\x_3\\x_4\end{bmatrix}$$  
> Linear, homogeneous  

> [!note] $4y'''+8y^2y''-\sin(y')=0,x_1=y,x_2=y',x_3=y''$  
> $4x_3'+8x_1^2x_3-\sin(x_2)=0\implies x_3'=-2x_1^2x_3+\frac{1}{4}\sin(x^2)$  
> $$x_1'=x_2$$ $$x_2'=x_3$$ $$x_3'=-2x_1^2x_3+\frac{1}{4}\sin(x^2)$$  
> Non-linear. No normal form  

> [!note] $t^2y''+(t+1)y'+(1-t)y=0,y(1)=2,y'(1)=1$  
> Let $x_1=y$ and $x_2=y'$ so $x_1'=x_2$  
> From the given ODE:  
> $t^2x_2'+(t+1)x_2+(1-t)x_1=0\implies t^2x_2'=(t-1)x_1-(t+1)x_2$  
> $\implies x_2'=\left(\frac{t-1}{t^2}\right)x_1-\left(\frac{t+1}{t^2}\right)x_2$  
> $$\begin{bmatrix}x_1'\\x_2'\end{bmatrix}=\begin{bmatrix}0&1\\\frac{t-1}{t^2}&-\frac{t+1}{t^2}\end{bmatrix}\begin{bmatrix}x_1\\x_2\end{bmatrix}$$  
> Linear. Homogeneous  
> Initial Condition $$\begin{bmatrix}x_1(1)\\x_2(1)\end{bmatrix}=\begin{bmatrix}2\\1\end{bmatrix}$$  

> [!note] Transform the following system of first order ODEs into a single equation  
> $$x_1'=3x_1-2x_2\tag{1}$$  
> $$x_2'=2x_1-2x_2\tag{2}$$  
> Solve for $x_2$ in terms of $x_1$ and $x_1'$ in (1).  
> $$x_1'=3x_1-2x_2\implies2x_2=3x_1-x_1'\implies x_2=\frac{3}{2}x_1-\frac{1}{2}x_1'$$  
> Then we plug $x_2=\frac{3}{2}x_1-\frac{1}{2}x_1'$ into (2)  
> $x_2'=2x_1-2x_2$  
> $\left(\frac{3}{2}x_1-\frac{1}{2}x_1'\right)'=2x_1-2\left(\frac{3}{2}x_1-\frac{1}{2}x_1'\right)$  
> $\frac{3}{2}x_1'-\frac{1}{2}x_1''=2x_1-3x_1+x_1'$  
> $\implies -\frac{1}{2}x_1''+\frac{1}{2}x_1'+x_1=0$  
> Now relabel $x_1=y$ to get: $-\frac{1}{2}y''+\frac{1}{2}y'+y=0$  

Generally, a system of ODEs has the form  
$$x_1'=F_1(t;x_1,\dots,x_n)$$  
$$x_2'=F_2(t;x_1,\dots,x_n)$$  
$$\vdots$$  
$$x_n'=F_n(t;x_1,\dots,x_n)$$  
If all $F_k$ above are of the form  
$$F_k(t;x_1,\dots,x_n)=a_{k1}(t)x_1+a_{k2}(t)x_2+\dots+a_{kn}(t)x_n+g_k(t)$$  
then the system is called linear. Otherwise, it is a non-linear system.  
We can transform linear systems into the form  
$$\begin{bmatrix}x_1'\\x_2'\\\vdots\\x_n'\end{bmatrix}=\begin{bmatrix}a_{11}&a_{12}&\dots&a_{1n}\\a_{21}&a_{22}&\dots&a_{2n}\\\vdots&\vdots&\ddots&\vdots\\a_{n1}&a_{n2}&\dots&a_{nn}\end{bmatrix}\begin{bmatrix}x_1\\x_2\\\vdots\\x_n\end{bmatrix}+\begin{bmatrix}g_1(t)\\g_2(t)\\\vdots\\g_n(t)\end{bmatrix}\text{ or }x'=Ax+g$$  
Here, if $g=0$ then we have a homogeneous system; otherwise, it is non-homogeneous.  

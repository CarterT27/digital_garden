---
tags:
- "Type/Note"
- "Topic/Calculus"
- "Class/MATH_20C"
date:
- 2024-02-14
---
# 14.4 Differentiability, Tangent Planes, Linear Approximation  

## Recall  

> [!note] Theorem  
> If $f_{xy}$ and $f_{yx}$ both exist and are **continuous** on a domain $D$  
> then $\frac{\partial^2f}{\partial y\partial x}=\frac{\partial^2 f}{\partial x\partial y}$  
> or $f_{xy}=f_{yx}$  

> [!note] Corollary  
> $f_{xyy}=f_{yxy}=f_{yyx}=\dots$  

## Back to 14.4  

> [!note] Tangent Line for $z=f(x,y)$  
> Slope $f_x(a,b)=\vec{r}_1(x)=\langle x,b,f(x,b)\rangle$  
> Slope $f_y(a,b)=\vec{r}_2(y)=\langle a,y,f(a,y)\rangle$  

> [!note] Normal Vector to the Tangent Plane  
> $\vec{v}=\vec{r}_1'(x)=\langle 1,0,\frac{d}{dx}f(x,b)\vert_{x=a}\rangle=\langle 1,0,f_x(a,b)\rangle$  
> $\vec{w}=\vec{r}_2'(y)=\langle 0,1,\frac{d}{dy}f(a,y)\vert_{y=b}\rangle=\langle 0,1,f_y(a,b)\rangle$  
> $\vec{n}=\vec{v}\times\vec{w}=\begin{bmatrix}\vec{i}&\vec{j}&\vec{k}\\1&0&f_x(a,b)\\0&1&f_y(a,b)\end{bmatrix}$  
> $=\vec{i}\begin{bmatrix}0&f_x(a,b)\\1&f_y(a,b)\end{bmatrix}-\vec{j}\begin{bmatrix}1&f_x(a,b)\\0&f_y(a,b)\end{bmatrix}+\vec{k}\begin{bmatrix}1&0\\0&1\end{bmatrix}$  
> $=-f_x(a,b)\vec{i}-f_y(a,b)\vec{j}+\vec{k}$  
> $=\langle -f_x(a,b),-f_y(a,b),1\rangle$  
> So the tangent plane to the graph of $f(x,y)$ at $P=(a,b,f(a,b))$ is  
> $-f_x(a,b)(x-a)-f_y(a,b)(y-b)+z-f(a,b)=0$  
> or tangent plane equation  
> $z=f(a,b)+f_x(a,b)(x-a)+f_y(a,b)(y-b)$  

> [!definition] Linearization of $f(x,y)$  
> Assume $f(x,y)$ is defined in a region $D$ containing $(a,b)$ and $f_x(a,b),f_y(a,b)$ exist  
> Then $$L(x,y)=f(a,b)+f_x(a,b)(x-a)+f_y(a,b)(y-b)$$  
> is called the **linearization** of $f(x,y) centered at $(a,b)$  

> [!definition] Differentiable  
> $f(x,y)$ is **differentiable** at $(a,b)$ if $$\lim_{(x,y)\to(a,b)}\frac{f(x,y)-L(x,y)}{\sqrt{(x-a)^2+(y-b)^2}}=0$  
> i.e. the linearization $L(x,y)$ is a good approximation for $f(x,y)$ near $(a,b)$  
> i.e. If $(x,y)$ is close to $(a,b)$ $f(x,y)\approx L(x,y)$  
> We say $f(x,y)$ is differentiable on a domain $D$ if it is differentiable at all points in $D$  

> [!note] Continuity Implies Differentiability  
> If $f_x$ and $f_y$ exist and are **continuous** on $D$ then $f(x,y)$ is **differentiable**.  

> [!definition] Linear Approximation  
> $$f(a+\Delta x,b+\Delta y)\approx f(a,b)+f_x(a,b)\Delta x+f_y(a,b)\Delta y$$  

> [!note] $\Delta f$  
> Let $\Delta f=f(x,y)-f(a,b)=f(a+\Delta x,b+\Delta y)-f(a,b)$  
> $\Rightarrow\Delta f\approx f_x(a,b)\Delta x+f_y(a,b)\Delta y$  

> [!note] Differentiable Form  
> Let $dx=\Delta x=x-a,dy=\Delta y=y-b$  
> Define $df=f_x(a,b)dx+f_y(a,b)dy$  
> The linear approximation can be written as $\Delta f\approx df$  

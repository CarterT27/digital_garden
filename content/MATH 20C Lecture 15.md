---
tags:
- Type/Note
- Topic/Calculus
- Class/MATH_20C
date:
- "2024-02-12"
---
> [!note] $\lim_{(x,y)\to(0,0)}x^2y^2\ln(x^2+y^2)$  
> $=\lim_{r\to0^+}(r\cos\theta)^2(r\sin\theta)^2\ln(r^2)$  
> $=\lim_{r\to0^+}r^4\ln(r^2)\cos^2\theta\sin^2\theta$  
> Note $\lim_{r\to0^+}r^4\ln(r^2)$  
> $=\lim_{r\to0^+}2r^4\ln(r)$  
> $=\lim_{r\to0^+}2\frac{\ln(r)}{r^{-4}}$ $(\frac{-\infty}{\infty})$  
> $=\lim_{r\to0^+}2\frac{\frac{1}{r}}{-4r^{-5}}$  
> $=\lim_{r\to0^+}-\frac{1}{2}r^4=0$  
> Since $0\leq\cos^2\theta\sin^2\theta\leq1$  
> $0\geq r^4\ln(r^2)\cos^2\theta\sin^2\theta\geq r^4\ln(r^2)$  
> Since $\lim_{r\to0^+}r^4\ln(r^2)=0$,  
> $\lim_{r\to0^+}r^4\ln(r^2)\cos^2\theta\sin^2\theta=0$  
> by the squeeze theorem  
> $\implies\lim_{(x,y)\to(0,0)}x^2y^2\ln(x^2+y^2)=0$  

# 14.3 Partial Derivatives  

> [!note] Partial Derivative  
> $f_x(a,b)=\lim_{h\to0}\frac{f(a+h,b)-f(a,b)}{h}$  
> $f_y(a,b)=\lim_{h\to0}\frac{f(a,b+h)-f(a,b)}{h}$  
> $f_x$ is called the **partial derivative** of $f$ with respect to (w.r.t.) $x$.  
> $f_y$ is called the **partial derivative** of $f$ with respect to (w.r.t.) $y$.  

> [!note] Partial Derivative Notation  
> Notation $f_x=\frac{\partial f}{\partial x}, f_y=\frac{\partial f}{\partial y}$  
> $f_x(a,b)=\frac{\partial f}{\partial x}\vert_{(a,b)},f_y(a,b)=\frac{\partial f}{\partial y}\vert_{(a,b)}$  

> [!note] Note that  
> $f_x(a,b)=\frac{d}{dx}f(x,b)\vert_{x=a}$  
> $f_y(a,b)=\frac{d}{dy}f(a,y)\vert_{y=b}$  

By definition, to compute $f_x$, we treat $y$ as a constant, and take the derivative w.r.t. $x$. Similarly, to compute $f_y$, we differentiate $f$ w.r.t. $y$, assuming $x$ is a constant.  

> [!note] Higher Order Partial Derivatives  
> $f_{xx}=\frac{\partial}{\partial x}\left(\frac{\partial}{\partial x}\right)$, $f_{yy}=\frac{\partial}{\partial y}\left(\frac{\partial}{\partial y}\right)$  

> [!note] Mixed Partials  
> $f_{xy}=\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)$, $f_{yx}=\frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right)$  

> [!note] Lebniz Notation  
> $f_{xx}=\frac{\partial^2f}{\partial x^2},f_{yy}=\frac{\partial^2f}{\partial y^2}$  
> $f_{xy}=\frac{\partial^2f}{\partial y\partial x},f_{yx}=\frac{\partial^2f}{\partial x\partial y}$  

> [!note] Higher Derivatives  
> $f_{xxy}=\frac{\partial}{\partial y}f_{xx}$  
> $f_{xyy}=\frac{\partial}{\partial y}f_{xy}$  

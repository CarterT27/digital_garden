---
tags:
- "Type/Note"
- "Topic/Differential_Equations"
- "Class/MATH_20D"
date:
- 2024-01-08
---
Source: https://canvas.ucsd.edu/courses/52767/files/11229957?module_item_id=2111692  
Source: https://canvas.ucsd.edu/courses/52767/files/11240075?module_item_id=2119876  

> [!definition] Differential Equation  
> An equation that contains some derivatives of an unknown function.  
> If the equations involves the derivatives of one variable with respect to another then the former is called a **dependent variable** and the latter is called an **independent variable**.  

> [!example] $\frac{d^2y}{dx^2}-\frac{2y}{x}=0$  
> $y''(x)-\frac{2y(x)}{x}=0$  
> unknown is function $y(x)$  
> $x$: independent variable  
> $y$ or $y(x)$: dependent variable  

> [!definition] Ordinary Differential Equation (ODE)  
> only **one** independent variable  

> [!definition] Order of a Differential Equation  
> **Order** of a differential equation is the order of the highest-order derivative present.  

> [!example] Order of $\frac{dy}{dx}+y^3=\sin(y)$  
> $y'(x)+[y(x)]^3=\sin(y(x))$  
> 1st order given by $y'(x)$  

> [!definition] Linear vs. Nonlinear ODE  
> an n-th order linear ODE can be written in the form  
> $a_{n(x)}\frac{d^ny}{dx^n}+a_{n-1}(x)\frac{d^{n-1}y}{dx^{n-1}}+\dots+a_{1}(x)\frac{dy}{dx}+a_{0}(x)y=F(x)$  
> Otherwise, the ODE is said to be nonlinear  

> [!definition] Solution to a Differential Equation  
> A **solution** to a differential equation (DE) on an interval $I$ is all functions $y(x)$ which satisfies the given DE for all values $x\in I$.  

> [!example] The differential equation $y'=f(t)$ has the general solution given by $y(t)=F(t)+C$  
> where $F(t)$ is the anti-derivative of $f(t)$ and $C$ is an arbitrary constant.  
> $y'=(F(t)+c)'=F'(t)=f(t)$  

> [!example] The differential equation $x\frac{dy}{dx}=2y$ has a solution $y(x)=x^2$  
> LHS=$x\frac{dy}{dx}=xy'(x)=x\cdot 2x=2x^2=2y(x)=$RHS  

> [!example] The differential equation $y'\cdot y=x$ has an (implicit) solution given by $x^2-y^2=C$ for any arbitrary constant C.  
> implicit definition needs implicit differentiation  
> $x^2-y^2=C\implies \frac{d}{dx}(x^2-y^2)=\frac{d}{dx}(C)\implies 2x-2y\cdot y'=0\implies x=y\cdot y'$  

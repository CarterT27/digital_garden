---
tags:
  - "#Type/Note"
  - "#Topic/Differential_Equations"
  - "#Class/MATH_20D"
date:
  - 2024-01-12
---

> [!definition] Autonomous Differential Equations
> Differential equations of the form $\frac{dy}{dt}=f(y)$ are called **autonomous**.
> or an autonomous equation, the solutions y(t) = yi, where yi’s are the  
> roots of f (t), are called equilibrium.  
> - If an equilibrium **repels** neighboring solutions as t → ∞ then it is called a **source**, **repeller**, or **unstable** equilibrium,  
> - If an equilibrium **attracts** neighboring solutions as t → ∞ then it is called a **sink**, **attractor**, or **stable** equilibrium,  
> - If an equilibrium is neither a source nor a sink, then it is called a **node**, or **semi-stable**.

> [!note] Equilibrium solution
> Occurs at the points where $\text{RHS}=f(y)=0$

> [!question]- $\frac{dy}{dx}=(y-1)(y-2)^2(y-3)$
> Equilibrium solutions: $y=1,y=2,y=3$
> $\frac{dy}{dx}>0$ when $y>3$
> $y=3$ is a source/repeller/unstable
> $\frac{dy}{dx}<0$ when $2<y<3$
> $y=2$ is a node/semi-stable
> $\frac{dy}{dx}<0$ when $1<y<2$
> $y=1$ is a sink/attractor/stable
> $\frac{dy}{dx}>0$ when $y<1$

> [!question]- $\frac{dy}{dx}=y\sin(y)$
> $\frac{dy}{dx}<0$ when $y>3\pi$
> $\frac{dy}{dx}>0$ when $2\pi<y<3\pi$
> $\frac{dy}{dx}<0$ when $\pi<y<2\pi$
> $\frac{dy}{dx}>0$ when $0<y<\pi$
> $\frac{dy}{dx}>0$ when $-\pi<y<0$
> $\frac{dy}{dx}<0$ when $y=-2\pi<y<-\pi$
> $\frac{dy}{dx}>0$ when $y=-3\pi<y<-2\pi$
> $\frac{dy}{dx}<0$ when $y<-3\pi$

# Chapter 2: First-Order ODEs

## Three main types of First-Order Equations

> [!definition] Separable ODE
> $\frac{dy}{dx}=f(x)g(y)$

> [!definition] Linear (1st order) ODE
> $\frac{dy}{dx}=p(x)y+q(x)$

> [!definition] Exact ODE
> $p(x,y)\frac{dy}{dx}+q(x,y)=0$ where $\frac{dp}{dx}=\frac{dq}{dy}$

## Separable ODEs

> [!check] $x^2\frac{dy}{dx}+\sin(y)=0$
> $\implies x^2\frac{dy}{dx}=-\sin(y)$
> $\implies \frac{dy}{dx}=\left( \frac{1}{x^2} \right)(-\sin(y))$

> [!danger] $xy\frac{dy}{dx}-(y-x)^2=0$
> $\implies xy\frac{dy}{dx}=(y-x)^2$
> Assume that $xy\neq 0$$\implies\frac{dy}{dx}=\frac{(y-x)^2}{xy}$
> $(y-x)^2$ is inseparable, so this is **NOT** a separable ODE

> [!check] $(1-y^2)\frac{dy}{dx}=x^2$
> $\implies \frac{dy}{dx}=x^2(\frac{1}{1-y^2})$

> [!note] Solving Separable ODEs
> *"Separate then integrate"*
> 1. Convert the given equation into the form $h(y)dy=g(x)dx$
> 2. Integrate both sides $\int h(y) \, dy=\int g(x) \, dx$ to obtain $H(y)=G(x)+C$. This gives the implicit solution to the given equation. (General solution in implicit form)
> 3. Convert the solution obtained in step 2 to explicit form and use the initial condition to solve for the constant C, if required/able.

> [!question] Solve the following IVP: $\frac{dy}{dx}=\frac{3x^2+4x+2}{2(y-1)},y(0)=-1$
> 1. Separate $2(y-1)dy=(3x^2+4x+2)dx$
> 2. Integrate $\int 2(y-1) \, dy=\int (3x^2+4x+2) \, dx$
> $\implies y^2-2y=x^3+2x^2+2x+C$
> 3. Use initial condition $x=0,y=-1$ to solve for C: $(-1)^2-2(-1)=C\implies C=3$
> Thus, the particular soln in implicit form is $y^2-2y=x^3+2x^2+2x+3$
> To convert this into explicit form:
> $y^2-2y+1=x^3+2x^2+2x+1$
> $\implies (y-1)^2=x^2+2x^2+2x+4$
> $\implies y-1=\pm \sqrt{ x^2+2x^2+2x+4 }$
> $\implies y=1+\pm \sqrt{ x^2+2x^2+2x+4 }$
> There can only be 0, 1, or infinitely many solutions. Not 2, so we have to figure out if we are using the + or - sign.
> Under the inital condition when $x=0,RHS:1\pm \sqrt{ 4 }$, which is $3$ if the sign is +, or $-1$ if the sign is -
> So the correct sign is -
> $y=1-\sqrt{ x^3+2x^2+2x+4 }$ is the particular solution in explicit form.

> [!question] $x \frac{dy}{dx}=\frac{x^2+1}{(x+1)^2(y-1)},y(1)=2$
> 1. Separate $(y-1)dy=\frac{x^2+1}{x(x+1)^2}dx$
> 2. Integrate $\int (y-1) \, dy=\int \frac{x^2+1}{x(x+1)^2}\, dx$
> $\implies\frac{1}{2}y^2-y=$
---  
tags:  
- Type/Note  
- Topic/Differential_Equations  
- Class/MATH_20D  
date:  
- 2024-01-22  
---  
  
> [!note] Exact Equation  
> $M(x,y)dx+N(x,y)dy=0$ where $\frac{\partial M(x,y)}{\partial y}=\frac{\partial N(x,y)}{\partial x}$ "cross derivative" or "mixed partial"  
> If equation is exact, then soln will always be given by $F(x,y)=c$ where c is some constant  
> Where $F(x,y)=\int M(x,y) \, dx=\int N(x,y) \, dy$  
  
> [!question] $(3x-e^x\cos y)y'=e^x\sin y-3y$  
> $\implies (3x-e^x\cos y)\frac{dy}{dx}+(3y-e^x\sin y)=0$  
> $\implies(3x-e^x\cos y)dy+(3y-e^x\sin y)dx=0$  
> Check for exact:  
> $\frac{\partial M}{\partial y}=\frac{\partial}{\partial y}(3y-e^x\sin y)=3-e^x\cos y$  
> $\frac{\partial N}{\partial x}=\frac{\partial}{\partial x}(3x-e^x\cos y)=3-e^x\cos y$  
> We look for the general soln of the form $F(x,y)=c$  
> $F(x,y)=\int M(x,y) \, dx=\int (3y-e^x\sin y) \, dx=3xy-e^x\sin y+c_{1}(y)$  
> $F(x,y)=\int N(x,y) \, dy=\int (3x-e^x\cos y) \, dy=3xy-e^x\sin y+c_{2}(x)$  
> $F(x,y)=3xy-e^x\sin y+0y+0x$  
> General solution is $3xy-e^x\sin y=c$  
  
> [!question] $\left( y-\frac{1}{x} \right)y'=x-\frac{y}{x^2},y(1)=2$  
> $\implies\frac{\left( y-\frac{1}{x} \right)dy}{dx}+\left( \frac{y}{x^2}-x \right)=0\implies\left( y-\frac{1}{x} \right)dy+\left( \frac{y}{x^2}-x \right)dx=0$  
> Check for exact:  
> $\frac{\partial M}{\partial y}=\frac{\partial}{\partial y}\left( \frac{y}{x^2}-x \right)=\frac{1}{x^2}$  
> $\frac{\partial N}{\partial x}=\frac{\partial}{\partial x}\left( y-\frac{1}{x} \right)=\frac{1}{x^2}$  
> We look for the general solution of the form $F(x,y)=c$  
> $=\int M(x,y) \, dx=\int \left( \frac{y}{x^2}-x \right) \, dx=-\frac{y}{x}-\frac{x^2}{2}+c_{1}(y)$  
> $=\int N(x,y) \, dy=\int \left( y-\frac{1}{x} \right) \, dy=\frac{y^2}{2}-\frac{y}{x}+c_{2}(x)$  
> $F(x,y)=-\frac{y}{x}+\frac{y^2}{2}-\frac{x^2}{2}=c$  
> We plug in $x=1,y=2$ and solve for $c$: $c=\frac{2^2}{2}-\frac{1^2}{2}-\frac{2}{1}=-\frac{1}{2}$  
> Particular solution in implicit form: $\frac{y^2}{2}-\frac{y}{x}-\frac{x^2}{2}+\frac{1}{2}=0$  
  
> [!question] $\left( \sin y-\frac{x}{y} \right)dy=dx$  
> $\implies 1dx+\left( \frac{x}{y}\sin y \right)dy=0$  
> Check for exact:  
> $\frac{\partial M}{\partial x}=\frac{\partial}{\partial x}(1)=0$  
> $\frac{\partial N}{\partial x}=\frac{\partial}{\partial x}\left( \frac{x}{y}-\sin y \right)=\frac{1}{y}$  
> So this is not an exact equation.  
> "Clever trick" multiply both sides by y to turn it into an exact equation.  
> $ydx+(x-y\sin y)dy=0$  
> Check for exact:  
> $\frac{\partial M}{\partial y}=\frac{\partial}{\partial y}(y)=1$  
> $\frac{\partial N}{\partial x}(x-y\sin y)=1$  
  
> [!note] Method for finding special integrating factor  
> If the equation $M(x,y)dx+N(x,y)dy=0$ is not separable, linear, or exact, then check the following:  
> 1. $\frac{\left( \frac{\partial M}{\partial y}-\frac{\partial N}{\partial y} \right)}{N}$ is a function of only x  
> 2. $\frac{\left( \frac{\partial N}{\partial x}-\frac{\partial M}{\partial y} \right)}{M}$ is a function of only y  
> If (1) holds, then the integrating factor is  
> $$u(x)=\exp \left[ \int \frac{\left( \frac{\partial M}{\partial y}-\frac{\partial N}{\partial x} \right)}{N} \, dx  \right]$$  
> If (2) holds, then the integrating factor is  
> $$u(x)=\exp \left[ \int \frac{\left( \frac{\partial N}{\partial x}-\frac{\partial M}{\partial y} \right)}{M} \, dy  \right]$$  
  
# Chapter 4 - Linear Second-Order ODEs  
  
> [!definition] Second-order linear ODE  
> $a_{2}(t)y''+a_{1}(t)y'+a_{0}(t)y=F(t)$ with $a_{2}(t)\neq 0$  
> In our case, we consider only second-order ODE with **constant coefficients**:  
> $$ay''+by'+cy=F(t)\text{ with }a\neq 0$$  
> In the special case where $F(t)=0$, we obtain the **homogenous form**  
> $$ay''+by'+cy=0\text{ with }a\neq 0$$  
> For the IVP, we need **two** initial conditions: $y(t_{0})=y_{0}$ and $y'(t_{0})=y_{0}'$  
  
> [!note] How to solve homogenous linear second-order ODE  
> Key idea: look for solutions of the form $y(t)=e^{rt}$  
> Plug in $y(t)=e^{rt}\implies y'(t)=re^{rt}\implies y''(t)=r^2e^{rt}$  
> So $ay''+by'+cy=ar^2e^{rt}+bre^{rt}+ce^{rt}=(ar^2+br+c)e^{rt}$  
> If $ay''+by'+cy=0$ then $ar^2+br+c=0$  
> Thus, if r is a solution to $ar^2+br+c=0$ (if r is a root of the polynomial $ar^2+br+c$) then $y(t)=e^{rt}$ will be a soln to the ODE $ay''+by'+cy=0$  
> $\Delta=b^2-4ac$  
> $\Delta>0$: $ar^2+br+c=0$ has 2 distinct (real-valued) solns. The ODE $ay''+by'+cy=0$ will have general soln: $r_{1,2}=\frac{-b\pm \sqrt{ b^2-4ac }}{2}\to y(t)=c_{1}e^{r_{1}t}+c_{2}e^{r_{2}t}$  
> $\Delta=0$: $ar^2+br+c=0$ has a repeated soln: $r=-\frac{b}{2a}$  
> $\Delta<0$: $ar^2+br+c=0$ has complex solutions in the form $r_{1,2}=\lambda\pm iu$ (conjugate pairs)  
> $ar^2+br+c=0$ is called the characteristic/auxiliary equation  
  
> [!question] $y''+y'-2y=0,y(0)=0,y'(0)=-3$  
> Characteristic equation: $r^2+r-2=0\implies(r-1)(r+2)=0\implies r_{1}=1,r_{2}=-2$  
> General soln is: $y(t)=c_{1}e^t+c_{2}e^{-2t}$  
> Now we use the initial condition to find $c_{1},c_{2}$  
> $y(t)=c_{1}e^t+c_{2}e^{-2t}\to 0=y(0)=c_{1}e^0+c_{2}e^{-0}=c_{1}+c_{2}$  
> $y'(t)=c_{1}e^t-2c_{2}e^{-2t}\to -3=y'(0)=c_{1}-2c_{2}$  
> So, by solving the system $0=c_{1}+c_{2},-3=c_{1}-2c_{2}$ we have $c_{1}=-1,c_{2}=1$.  
> Thus, the particular soln is $y(t)=-e^t+e^{-2t}$  

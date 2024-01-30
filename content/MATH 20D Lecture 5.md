---  
tags:  
- Type/Note  
- Topic/Differential_Equations  
- Class/MATH_20D  
date:  
- 2024-01-19  
---  
  
> [!note] $a\log_{b}(x)=\log_{b}(x^a)$  
  
> [!question] Solve the IVP $xy'+2y=x^2+x-1,y(1)=-1/2$  
> Convert into standard form: $y'+\frac{2}{x}y=x+1-\frac{1}{x}$ (assume $x\neq 0$)  
> Here $P(x)=\frac{2}{x}$ so $\int P(x) \, dx=\int \frac{2}{x} \, dx=2\ln|x|=\ln(x^2)$  
> So $u(x)=e^{\int p(x) \, dx}=e^{\ln(x^2)}=x^2$  
> The integrating factor is $u(x)=x^2$  
> Now multiply $u(x)=x^2$ to both sides of the standard form eqn  
> $(x^2)\left( y'+\frac{2}{x}y \right)=\left( x+1-\frac{1}{x} \right)(x^2)$  
> $\implies x^2y'+2xy=x^3+x^2-x$  
> $\implies(yx^2)'=x^3+x^2-x$  
> $\implies yx^2=\int (x^3+x^2-x) \, dx=\frac{x^4}{4}+\frac{x^3}{3}-\frac{x^2}{2}+C$  
> $\implies y=\frac{x^2}{4}+\frac{x}{3}-\frac{1}{2}+\frac{C}{x^2}$  
> Now we use initial value $x=1,y=-1/2$  
> $-\frac{1}{2}=\frac{1}{4}+\frac{1}{3}-\frac{1}{2}+\frac{C}{1}\implies C=-\frac{7}{12}$  
> Therefore, particular soln in explicit form is  
> $y=\frac{x^2}{4}+\frac{x}{3}-\frac{1}{2}-\frac{7}{12x^2}$  
  
> [!note] Why does the choice of $u(x)=e^{\int P(x) \, dx}$ work?  
> Recall the standard form of our 1st-order linear ODE: $y'=P(x)y=Q(x)$  
> After multiplying $u(x)$ to both sides of this standard form:  
> $u(x)y'+u(x)P(x)y=u(x)Q(x)$  
> So to turn LHS into a single derivative w/ product rule, we want $u'(x)=u(x)P(x)$  
> So $u(x)$ is a soln to the ODE: $u'(x)=u(x)P(x)$  
> This is a separable equation $\frac{du}{dx}=uP(x)$  
> $\implies \frac{du}{u}=P(x)dx$  
> $\implies \int \frac{du}{u}=\int P(x) \, dx$  
> $\implies \ln(u)=\int P(x) \, dx$  
> $\implies u=e^{\int P(x) \, dx}$  
  
> [!definition] Exact ODEs  
> An **exact equation** has the form  
> $$N(x,y)\frac{dy}{dx}+M(x,y)=0\text{ or }M(x,y)dx+N(x,y)dy=0$$  
> where $\frac{\partial M(x,y)}{\partial y}=\frac{\partial N(x,y)}{\partial x}$ "cross deriv."  
  
> [!note] Method for Solving Exact Equations  
> In general, if $M(x,y)dx+N(x,y)dy=0$ is exact then there exists a function $F(x,y)$ such that  
> $$M(x,y)=\frac{\partial F}{\partial x}\text{ and }N(x,y)=\frac{\partial F}{\partial y}.$$  
> The *implicit solution is then given by * $F(x,y)=C.$  
  
> [!question] Solve $(y^4-2)+4xy^3\frac{dy}{dx}=0$  
> 1. Integrate $\frac{\partial F}{\partial x}=M(x,y)$ with respect to $x$ to obtain  
> $$F(x,y)=\int M(x,y) \, dx +c_{1}(y)$$  
> $F(x,y)=\int (y^4-2) \, dx=xy^4-2x+c_{1}(y)$  
> 1. Integrate $\frac{\partial F}{\partial y}=N(x,y)$ with respect to $y$ to obtain  
> $$F(x,y)=\int N(x,y) \, dy+c_{2}(x) $$  
> $F(x,y)=\int (4xy^3) \, dy=xy^4+c_{2}(x)$  
> 3. Match the annswers from the previous steps to determine $F(x,y)$  
> $xy^4-2x+c_{1}(y)=F(x,y)=xy^4+c_{2}(x)+0$  
> $F(x,y)=xy^4-2x$  
> Implicit soln: $F(x,y)=C$ or $xy^4-2x=C$  

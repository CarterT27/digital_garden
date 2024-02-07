---
tags:  
- Type/Note  
- Topic/Differential_Equations  
- Class/MATH_20D  
date:  
- 2024-01-26  
---
  
# Section 4.2 - How to solve $ay''+by'+cy=0$  
  
Look for solutions of the form $y(t)=e^{rt}$  
  
In general, given the second-order equation $ay''+by'+c=0$ whose characteristic equation is $ar^2+br+c=0$. The roots of this characteristic equation is given by  
$$r=\frac{-b\pm \sqrt{ b^2-4ac }}{2a}$$  
  
There are now three cases:  
1. If $b^2-4ac>0$ then the characteristic equation has two **distinct, real-valued** roots $r_{1},r_{2}$. The solution to the ODE $ay''+by'+c=0$ is  
$$y=C_{1}e^{r_{1}t}+C_{2}e^{r_{2}t}$$  
for arbitrary constants $C_{1},C_{2}$.  
2. If $b^2-4ac=0$ then the characteristic equation has a **repeated root** $r$. The solution to the ODE $ay''+by'+c=0$ is  
$$y=C_{1}e^{rt}+C_{2}te^{rt}$$  
for arbitrary constants $C_{1},C_{2}$.  
3. If $b^2-4ac<0$ then the characteristic equation has **complex roots** $r_{1,2}=\lambda\pm i\mu$ where $\lambda=-b/2a$ and $\mu=\sqrt{ 4ac-b^2 }/2a$. The solution to the ODE $ay''+by'+c=0$ is  
$$y=e^{\lambda t}(C_{1}\cos(\mu t)+C_{2}\sin(\mu t))$$  
for arbitrary constants $C_{1},C_{2}$.  
  
# Sections 4.4 & 4.5 - The Method of Undetermined Coefficients (a.k.a. Making educated guesses)  
  
> [!note] Undetermined Coefficients Method  
> Consider the non-homogenous second order linear equation with constant coefficients  
> $$ay''+by'+cy=g(t),\text{ where }a\neq 0,g(t)\neq 0.$$  
> Then the solution to this non-homogeneous equation, $Y(t)$, can be expressed in the form  
> $$Y=Y_{H}+Y_{P}$$  
> $Y_{H}$ is soln to the corresponding homogeneous eqn $ay''+by'+cy=0$ (what we've been doing this week)  
> $Y_{P}$: any particular solution to the non-hom. eqn  
> $$ay''+by'+cy=g(t)$$  
> For certain RHS, we can make a guess for what $Y_{P}$ will be.  
> Here $g(t)$ must be one of:  
> - Exponential: $e^{kt}$  
> - Polynomial: $a_{n}t^n+a_{n-1}t^{n-1}+\dots+a_{2}t^2+a_{1}t+a_{0}$  
> - $\sin(kt)$ and/or $\cos(kt)$  
> - any product/combo of the above 3  
  
> [!note] $g(t)=ke^{\omega t}$  
> $t$: indep. variable  
> $k,w$: arbitrary parameters/constants  
> Our guess for $Y_{P}$: $Y_{P}=Ae^{\omega t}$  
  
> [!question] $y''-2y'-3y=e^{2t},\omega=2$  
> 1. Solve corresponding hom. eqn. for $y_{H}$. Here, we solve $y''-2y'-3y=0$ for $y_{H}$  
> Chara. eqn.: $r^2-2r-3=0$ which has soln $r_{1}=3,r_{2}=-1$  
> $(r-3)(r+1)=0$  
> So $y_{H}=c_{1}e^{-t}+c_{2}e^{3t}$  
> 2. Guess that $y_{P}=Ae^{2t}$, plug in the ODE and solve for $A$.  
> $y_{P}'=2Ae^{2t}$ and $y_{P}''=4Ae^{2t}$  
> plug in $y_{P}$ in LHS: $y_{P}''-2y_{P}'-3y_{P}=4Ae^{2t}-2(2Ae^{2t})-3(Ae^{2t})=-3Ae^{2t}$  
> Meanwhile RHS $=e^{2t}$  
> So $-3Ae^{2t}=e^{2t}\implies A=-\frac{1}{3}$  
> Thus, $y_{P}=-\frac{1}{3}e^{2t}$  
> 3. General soln to the non-homo. eqn. is $y(t)=y_{H}+y_{P}\implies y(t)=c_{1}e^{-t}+c_{2}e^{3t}-\frac{1}{3}e^{2t}$  
> 2. Based on RHS, we guess that $y_{P}=Ae^{3t}$. But there is a "conflict" between $y_{P}$ & $y_{H}$ so we make another one, by multiplying our current guess by $t$. New guess: $y_{P}=Ate^{3t}$  
> Now there's no more "conflict", we can use $y_{P}=Ate^{3t}$ and plug it into the ODE to solve for $A$.  
> LHS = $y_{P}''-2y_{P}'-3y_{P}=6Ae^{3t}+9Ate^{3t}-2Ae^{3t}-6Ate^{3t}-3Ate^{3t}=4Ae^{3t}$  
> With RHS = $5e^{3t}$, we have $5e^{3t}=4Ae^{3t}$ so $5=4A\implies A=\frac{5}{4}$ thus, $y_{P}=\frac{5}{4}te^3t$  
> General soln: $y(t)=y_{H}+y_{P}=c_{1}e^{-t}+c_{2}e^{3t}+\frac{5}{4}te^{3t}$  

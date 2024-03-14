---
tags:
- "Type/Note"
- "Topic/Differential_Equations"
- "Class/MATH_20D"
date:
- 2024-03-13
---
> [!note] Example. Solve the IVP $y''+y=4u(t-3),y(0)=0,y'(0)=1$  

# 7.9 - Dirac Delta Function  

> [!definition] Dirac Delta Function  
> The **Dirac Delta Function** or **unit impulse function**, denoted $\delta(t)$, is defined by two properties:  
> $$\delta(t)=0\text{ if }t\neq0\text{ and }\int_{-\infty}^\infty\delta(t)\,dt=1$$  
> Dirac Delta function can sometimes be seen as having $\infty$ value at $t=0$. In addition, the impulse can occur at an arbitraty time $t=a$. In this case, we have  
> $$\delta(t-a)=0,\text{ if }t\neq a\text{ and }\int_{-\infty}^\infty\delta(t-a)\,dt=1$$  
> Fact:  
> 1. $\frac{du(t-a)}{dt}=\delta(t-a)$ where $u(t)$ is the unit step (Heaviside) function  
> 2. $\int_\alpha^\beta f(t)\delta(t-a)\,dt=\begin{cases}f(a),\text{ if }\alpha<a<\beta\\0,\text{ otherwise}\end{cases}$  

> [!note] Properties of Dirac Delta Function  
> 1. Let $f$ be continuous function such that $\lim\limits_{t\to}f(t)=0$, and let $a\geq0$. Then  
> $$\int_{-\infty}^\infty\delta(t-a)f(t)\,dt=f(a).$$  
> 2. Laplace transforms for Dirac Delta functions:  
> $$\mathcal{L}\{\delta(t)\}=1,\mathcal{L}\{\delta(t-a)\}=e^{-as},\text{ and }\mathcal{L}\{\delta(t-a)f(t)\}=f(a)e^{-as},\text{ for }a>0$$  

> [!note] Example. Solve the IVP: $2y''+y'+2y=\delta(t-5);y(0)=y'(0)=0$  
> $\mathcal{L}\{RHS\}=e^{-5s}$  
> Do the rest of it normally  

> [!note] Example. Solve the IVP: $y''+6y'+5y=\delta(t)+\delta(t-2);y(0)=1,y'(0)=0$  
> $\mathcal{L}\{RHS\}=\mathcal{L}\{f(t)\}+\mathcal{L}\{\delta(t-2)\}=1+e^{-2s}$  
> Do the rest normally  

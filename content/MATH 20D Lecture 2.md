---
tags:
- "Type/Note"
- "Topic/Differential_Equations"
- "Class/MATH_20D"
date:
- 2024-01-10
---

Source: https://canvas.ucsd.edu/courses/52767/files/11229957?module_item_id=2111692

# Section 1.2 - Initial Value Problems

> [!definition] Initial Value Problem (IVP)
> An **initial value problem** (IVP) is a differential ewquation that has its conditions specified at some value $x_{0}$.  

> [!example] $y'\cdot y=x,y(2)=-1$
> Previously, we saw that every function $y(x)$ of the form $x^2-y^2=C$ is a solution to $y'\cdot y$  
> We refer to $x^2-y^2=C$ as general solution.  
> We now use the initial condition/value: $y(2)=-1$ means when $x=2,y=1$.  
> To solve for C, $2^2-(-1)^2=C\implies C=3$  
> Thus, $x^2-y^2=3$ is a particular solution to the given IVP  

> [!example] Verify that any function of the form $y(x)=c_{1}e^x+c_{2}e^{-2x}$ for arbitrary constants $c_{1},c_{2}$ is a solution to the differential equation $\frac{d^2y}{dx^2}+\frac{dy}{dx}-2y=0$
> $y(x)=c_{1}e^x+c_{2}e^{-2x}\implies y'(x)=\frac{dy}{dx}=c_{1}e^x-2c_{2}e^{-2x}$  
> $\implies y''(x)=\frac{d^2y}{dx^2}=c_{1}e^x+4c_{2}e^{-2x}$  
> So we plug them in: $y''(x)+y'(x)-2y(x)=(c_{1}e^x+4c_{2}e^{-2x})+(c_{1}e^x-2c_{2}e^{-2x})-2(c_{1}e^x+c_{2}e^-2x)$  
> $=(c_{1}e^x+c_{1}e^x-2c_{1}e^x)+(4c_{2}e^{-2x}-2c_{2}e^{-2x}-2c_{2}e^{-2x})=0$  
> Thus, $y(x)=c_{1}e^x+c_{2}e^{-2x}$ is general solution to $y''+y'-2y=0$  

> [!example] $\frac{d^2y}{dx^2}+\frac{dy}{dx}-2y=0,y(0)=2,y'(0)=1$
> So far, we know $y(x)=c_{1}e^x+c_{2}e^{-2x}$ are general solutions.  
> We now use the inital condition to solve for $c_{1},c_{2}$.  
> When $x=0,y(0)=2\implies_{2}=c_{1}e^0+c_{2}e^0\implies c_{1}+c_{2}=2$  
> Recall $y'(x)=c_{1}e^x-2c_{2}e^{-2x}$ so when $x=0,y'(0)=1$  
> Thus, $1=c_{1}e^0-2c_{2}e^0\implies c_{1}-2c_{2}=1$  
> We obtain a system of 2 equations, 2 unknowns  
> $c_{1}=\frac{5}{3},c_{2}=\frac{1}{3}$  
> Hence, the particular solution is: $y(x)=\frac{5}{3}e^x+\frac{1}{3}e^{-2x}$  

> [!note] In general, an *n*-th order initial value problem requires *n* initial conditions:
> $y(x_{0})=y_{0};\frac{dy}{dx}(x_{0})=y_{1};\frac{d^2y}{{dx^2}}(x_{0})=y_{2};\dots;\frac{d^{n-1}y}{dx^{n-1}}$  

> [!definition] Explicit Solution
> A function f(x) is called an explicit solution to the given ODE on an interval I provided that, when substituted for y, it satisfies the given equation for all in I.  

> [!definition] Implicit Solution
> A relation G(x,y)=0 is said to be an implicit solution to the given ODE on the interval I if it defines one or more explicit solutions on I.  

> [!definition] General Solution
> The general solution is the solution of the given ODE that contains  
an abitrary constant C.

> [!definition] Particular Solution
> he particular solution is the solution to the IVP, obtained from the  
general solution by solving for C using the given initial value(s)

> [!note] In general an IVP can have
> No solution  
> A unique solution  
> Infinitely many solutions  

# Section 1.3 - Direction Field

> [!example] The logistic equation for the population p (in thousands) at time t of a certain species is given by $\frac{dp}{dt}=p(2-p)$
> Equilibrium solutions: 0, 2  
> p=2: sink/stable equilibrium  
> p=0: source/unstable equilibrium  

> [!definition] Phase line
> We need the **phase line** to study the behavior of the solution $p(t)$.  
> Vertical line pointing upwards with P at the tip. p=0, p=2 (points at the roots). Examining where the first derivative of the function is positive and negative (when the population is increasing and decreasing). Draw smaller arrows that show which way the population goes in relation to the roots.  

> [!definition] Autonomous Differential Equations
> Differential equations of the form $\frac{dy}{dt}=f(y)$ are called **autonomous**.  
> or an autonomous equation, the solutions y(t) = yi, where yi’s are the  
> roots of f (t), are called equilibrium.  
> - If an equilibrium repels neighboring solutions as t → ∞ then it is called a source, repeller, or unstable equilibrium,  
> - If an equilibrium attracts neighboring solutions as t → ∞ then it is called a sink, attractor, or stable equilibrium,  
> - If an equilibrium is neither a source nor a sink, then it is called a node, or semi-stable.  

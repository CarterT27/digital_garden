---
tags:
- Type/Note
- Topic/Differential_Equations
- Class/MATH_20D
date:
- 2024-02-05
---
A second-order linear ODE with variable-coefficients is given by  
$$a_{2}(t)y''+a_{1}(t)y'+a_{0}(t)y=f(t)$$  
where $a_{2}(t)$ is non-zero. This can also be converted into **standard form**  
$$y''(t)+p(t)y'(t)+q(t)y=g(t).$$  
Bad news: There is no method to solving the general case above!  
What we can do:  
1. If we have 2 linearly independent solutions to the corresponding homogeneous case  
$$a_{2}(t)y''+a_{1}(t)y'+a_{0}(t)y=0$$  
(call them $y_{1}$&$y_{2}$) then $y_{H}=c_{1}y_{1}+c_{2}y_{2}$.  
Then use variation by parameters to find $y_{P}=\mu_{1}y_{1}+\mu_{2}y_{2}$  
2. If we have only one solution to the given ODE (call $y_{1}$)  
Then we can use Reduction by Order to generate $y_{2}$ that is independent from $y_{1}$  
Now go back to case 1  
3. When the coefficients $a_{0}(t),a_{1}(t),a_{2}(t)$ are "nice" then we can still find $y_{H}$.  
An example of "nice coefficient" is Cauchy-Euler Equation  
where $a_{2}(t)=at^2,a_{1}(t)=bt,a_{0}(t)=c$, and $a,b,c$ are constants.  

> [!note] Cauchy-Euler Equation  
> $$at^2y''+bty'+cy=f(t)$$  
> where $a,b,c$ are constants.  
> The solutions to the corresponding homogeneous equation $at^2y''+bty'+cy=0$ can be found in the form $t^r$ for $t>0$.  
> Here $y=t^r$ then $y'=r\cdot t^{r-1}$, $y''=r(r-1)t^{r-2}$  
> So LHS=$at^2y''+bty'+cy=at^2r(r-1)t^{r-2}+btrt^{r-1}+ct^r$  
> $=ar(r-1)t^r+brt^r+ct^r$  
> $=(ar(r-1)+br+c)t^r$  
> $=(ar^2+(b-a)r+c)t^r$  
> when RHS$=0\implies ar^2+(b-a)r+c=0$: characteristic equation  

> [!question] $t^2y''+14ty'+42y=0$  
> $ar^2+(b-a)r+c=0\implies r^2+13r+42=0$  
> which has 2 soln $r_{1}=-6,r_{2}=-7$ so  
> $y_{1}=t^{-6}$ and $y_{2}=t^{-7}$ are 2 linearly independent solutions  
> Thus $y_{H}=c_{1}t^{-6}+c_{2}t^{-7}$  

> [!note] Cases of the Cauchy-Euler Equation  
> $ar^2+(b-a)r+c=0$  
> 1. If there are two distinct, real-valued solutions $r_{1},r_{2}$. Then the general solution is given by $$y=C_{1}t^{r_{1}}+C_{2}t^{r_{2}}$$  
> 2. If there are complex solutions $r_{1,2}=\alpha\pm i\mathrm{B}$. Then the general solution is given by $$y=C_{1}t^\alpha \cos(\beta\ln t)+C_{2}t^\alpha \sin(\beta\ln t)$$  
> 3. If there is a repeated/unique solution $r$ then the general solution is given by $$y=C_{1}t^r+C_{2}t^r\ln t$$  
> Remark: Homogeneous Cauchy-Euler equation can be converted into a 2nd order linear ODE with constant coefficients under the substitution $t=e^x$  

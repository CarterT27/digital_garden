---
tags:
- Type/Note
- Topic/Differential_Equations
- Class/MATH_20D
date:
- 2024-01-25
---
# Linear Second-Order ODEs  

> [!definition] Second-Order Linear ODE  
> A **second-order linear ODE** has the general form  
> $$a_{2}(t)y''+a_{1}(t)y'+a_{0}(t)y=F(t)\text{ with }a_{2}(t)\neq 0$$  
> In our case, we consider only second-order ODE with **constant coefficients**:  
> $$ay''+by'+cy=F(t)\text{ with }a\neq 0$$  
> In the special case where $F(t)=0$, we obtain the **homogenous form**  
> $$ay''+by'+cy=0\text{ with }a=0$$  
> For the IVP, need **two** initial conditions: $y(t_{0})=y_{0}$ and $y'(t_{0})=y_{0}'$  

> [!definition] Linear Independence of Two Functions  
> Two functions $y_{1}(t)$ and $y_{2}(t)$ are said to be **linearly independent on the interval $I$** if and only if neither of them is a **constant multiple of the other**, for all $t\in I$.  

> [!note] A condition for Linear Independence of Solutions  
> Two solutions $y_{1}(t)$ and $y_{2}(t)$ are **linearly independent** on the interval $I$ if  
> $$W[y_{1},y_{2}](t)=\begin{vmatrix}y_{1}(t) & y_{2}(t) \\  
y_{1}'(t) & y_{2}'(t)\end{vmatrix}=y_{1}(t)y_{2}'(t)-y_{1}'(t)y_{2}(t)\neq 0$$  
> for some value $t\in I$. If $W[y_{1},y_{2}](t)=0$ for all $t\in I$ then $y_{1}(t)$ and $y_{2}(t)$ are **linearly dependent**.  
> Here, $W[y_{1},y_{2}](t)$ is called the Wronskian of $y_{1},y_{2}$.  

> [!note] General solution of Homogeneous second-order ODE  
> In general, if $ya(t)$ and $y_{2}(t)$ are two linearly independent solutions of the homogeneous second-order ODE $ay''+by'+cy=0$ then the general solution to this ODE is given by  
> $$c_{1}y_{1}(t)+c_{2}y_{2}(t)$$  
> for constants $c_{1},c_{2}$.  
> In the case the characteristic equation $ar^2+br+c=0$ has repeated roots $r_{1}=r_{2}=r$ then the general solution to the corresponding homogeneous 2nd-order ODE $ay''+by'+cy=0$ is given by  
> $c_{1}e^{rt}+c_{2}te^{rt}$  
> for constants $c_{1},c_{2}$.  

> [!note] Characteristic Equation with Complex Roots  

> [!question] $y''+k^2y=0,y(0)=y_{0},y'(0)=y_{1}$  
> Show that a solution of this equation has the general form  
> $$y=C_{1}\cos(kt)+C_{2}\sin(kt)$$  
> $y_{1}(t)=\cos(kt)\implies y_{1}'(t)=-k\sin(kt)\implies y_{1}''(t)=-k^2\cos(kt)$  
> $y_{1}''+k^2y_{1}=-k^2\cos(kt)+k^2\cos(kt)=0$  
> So $y_{1}(t)=\cos(kt)$ is indeed a soln to $y''+k^2y=0$  
> Can you do the same for $y_{2}(t)=\sin(kt)$?  
> To show $\cos(kt)\&\sin(kt)$ are linearly independent we calculate their Wronskian  
> $$W[y_{1},y_{2}](t)=\begin{vmatrix}\cos(kt) & \sin(kt) \\  
-k\sin(kt) & k\cos(kt)\end{vmatrix}=(\cos(kt))(k\cos(kt))-(-k\sin(kt))(\sin(kt))=k\cos^2(kt)+k\sin^2(kt)=k\neq 0$$  
> Therefore, $y(t)=C_{1}\cos(kt)+C_{2}\sin(kt)$ will be our general soln to $y''+k^2y=0$  

Now let's solve the same problem using its characteristic equation  

> [!question] $y''+k^2y=0,y(0)=y_{0},y'(0)=y_{1}$  
> Chara. Eqn.: $r^2+0r+k^2=0\implies r^2=-k^2=(-1)k^2\implies r=\pm k\sqrt{ -1 }=\pm ki$  
> So according to Case 1, we do have 2 distinct soln. $r_{1}=ki,r_{2}=-ki$ from the chara. eqn.  
> $y(t)=c_{1}e^{rt}+c_{2}e^{rt}=c_{1}e^{(ik)t}+c_{2}e^{(-ik)t}$  

> [!note] Euler's Formula  
> $e^{i\theta}=\cos \theta+i\sin \theta$  
> If $\theta=kt: e^{ikt}=\cos(kt)+i\sin(kt)$  
> If $\theta=-kt: e^{-ikt}=\cos(-kt)+i\sin(-kt)=\cos(kt)-i\sin(kt)$  
> $y(t)=c_{1}(\cos(kt)+i\sin(kt))+c_{2}(\cos(kt)-i\sin(kt))=(c_{1}+c_{2})\cos(kt)+(c_{1}-c_{2})i\sin(kt)=K_{1}\cos(kt)+K_{2}\sin(kt)$  

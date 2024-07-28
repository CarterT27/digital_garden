---
tags:
- "Type/Note"
- "Topic/Differential_Equations"
- "Class/MATH_20D"
date:
- 2024-02-16
---
# 5.4 - Phase Plane of $2\times2$ Systems  

> [!note] Case 1. $A$ has two real-valued eigenvalues of opposite signs.  
> The origin is called a **saddle**  
> "semi-stable"  
> 2 kinds of "long-term" behavior for our solution:  
> 1. If our initial condition starts on the direction of the eigenvector corresponds to the negative eigenvalue  
> Then $\lim_{t\to\infty}\vec{x}(t)=\begin{bmatrix}\lim_{t\to\infty}x_1(t)\\\lim_{t\to\infty}x_2(t)\end{bmatrix}=\begin{bmatrix}0\\0\end{bmatrix}$ "stable direction"  
> 2. If our initial condition starts everywhere else, then $\lim_{t\to\infty}\vec{x}(t)=\begin{bmatrix}\infty\\\infty\end{bmatrix}$ "unstable direction"  

> [!note] Case 2a. $A$ has two distinct real-valued eigenvalues that are both negative.  
> "fast direction"  
> - eigenvector of eigenvalue that is "more negative"  
> - controls the solution behavior away from origin  
> "slow direction"  
> - eigenvector of eigenvalue that is "less negative"  
> - controls behavior near origin  
> Origin is stable, called sink/attractor  

> [!note] Case 2b. $A$ has two distinct real-valued eigenvalues that are both positive.  
> "fast direction"  
> - eigenvector of the eigenvalue that is "more positive"  
> - controls behaviors away/far from the origin  
> "slow direction"  
> - eigenvector of the eigenvalue that is "less positive"  
> - controls behavior near origin  
> Origin is source/repellor/unstable  

> [!note] Case 3a. $A$ has complex eigenvalues $\lambda_{1,2}=\pm i\beta$ (pure imaginary eigenvalues)  
> Origin is a circle/ellipse (because solutions will orbit around circles, depend only on sin/cosine)  
> Stability N/A  

> [!note] Case 3b. $A$ has complex eigenvalues $\lambda_{1,2}=\pm i\beta$ with $\alpha>0$  
> Origin is a spiral source (because $\alpha=Re(\lambda_1)>0$)  
> Unstable  

> [!note] Case 3c. $A$ has complex eigenvalues $\lambda_{1,2}=\pm i\beta$ with $\alpha<0$  
> Origin is a spiral sink, stable  

> [!note] Case 4a. $A$ has repeated eigenvalue $\lambda>0$ and two independent eigenvectors  
> Origin is called a star source, unstable (because $\lambda>0$)  

> [!note] Case 4b. $A$ has repeated eigenvalue $\lambda<0$ and two independent eigenvectors  
> Origin is called a star sink, stable (because $\lambda<0$)  

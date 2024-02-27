---
tags:
- "Type/Note"
- "Topic/Calculus"
- "Class/MATH_20C"
date:
- 2024-02-26
---
# 14.7 Optimization  

> [!question] How to classify critical points?  
> Answer: The second derivative test  

> [!definition] Discriminant  
> $D=D(a,b)$ of $f(x,y)$ at $(a,b)$  
> by $D=D(a,b)=\begin{bmatrix}f_{xx}(a,b)&f_{xy}(a,b)\\f_{yx}(a,b)&f_{yy}(a,b)\end{bmatrix}$  
> $=f_{xx}(a,b)f_{yy}(a,b)-(f_{xy}(a,b))^2$  

> [!note] Theorem: The second derivative test for $f(x,y)$  
> Let $P=(a,b)$ be a critical point of $f(x,y)$. Assume $f_{xx},f_{yy},f_{xy}$ are continuous near $P$. Then  
> 1. If $D(P)>0$ and $f_{xx}(P)>0$ then $P$ is a local minimum.  
> 2. If $D(P)>0$ and $f_{xx}(P)<0$ then $P$ is a local maximum.  
> 3. If $D(P)<0$, then $P$ is a saddle point.  
> 4. If $D(P)=0$, the test is inconclusive.  

> [!definition] Global Extrema  
> The minimum and maximum values of a function $f$ on a given domain $D$ are called global extreme values.  

> [!definition] Bounded  
> A domain $D$ is **bounded** if it is contained in a disk of radius $M$ centered at the origin for some $M>0$.  

> [!definition] Closed  
> A domain $D$ is **closed** if it contains all boundary points.  

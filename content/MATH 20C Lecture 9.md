---
tags:  
- Type/Note  
- Topic/Calculus  
- Class/MATH_20C  
date:  
- 2024-01-29  
---
  
# 13.1 Vector-Valued Integration  
  
> [!definition] Definite Integral  
> Let $\vec{r}(t)=\langle x(t),y(t),z(t) \rangle$  
> Define $\int _{a}^b \vec{r}(t)\, dt=\langle \int _{a}^bx(t) \, dt,\int _{a}^by(t) \, dt,\int _{a}^bz(t) \, dt \rangle$  
  
> [!definition] Antiderivative  
> An **antiderivative** of $\vec{r}(t)$ is a vector-valued function $\vec{R}(t)$ s.t. $\vec{R}'(t)=\vec{r}(t)$.  
  
> [!definition] Indefinite Integral  
> The **indefinite integral** is the family of all antiderivatives of $\vec{r}(t)$.  
> $\int \vec{r}(t) \, dt=\vec{R}(t)+\vec{c}$  
  
> [!definition] Fundamental Theorem of Calculus for Vector-Valued Functions  
> 1. If $\vec{r}(t)$ is continuous on $[a,b]$ and $\vec{R}(t)$ is an antiderivative of $\vec{r}(t)$  
> Then $\int _{a}^b\vec{r}(t) \, \frac{d}{dt}=\vec{R}(t)|_{a}^b=\vec{R}(b)-\vec{R}(a)$  
> 2. $\vec{r}(t)$ is continuous on an open interval $I$  
> Let $a\in I$. Then,  
> $\int _{a}^t\vec{r}(s) \, ds$ is an antiderivative of $\vec{r}(t)$  
> i.e. $\frac{d}{dt}\left( \int _{a}^t \vec{r}(s)\, ds \right)=\vec{r}(t)$  
  
# 13.3 Arc Length  
  
> [!note] Velocity vector  
> $\vec{r}(t)$ position vector  
> Then  
> 1. $\vec{v}(t)=\vec{r}'(t)$ is the **velocity vector**  
> 2. $v(t)=\Vert\vec{v}(t)\Vert$ is the **speed function**  
  
> [!note] Let $C$ be the curve parameterized by $\vec{r}(t)=\langle x(t), y(t), z(t) \rangle$ for $a\leq t\leq b$  
> Then the arc length $s$ of $C$ over $[a,b,]$ is $s=\int _{a}^bv(t) \, dt=\int _{a}^b\Vert\vec{v}(t)\Vert \, dt=\int _{a}^b\sqrt{ (x'(t))^2+(y'(t))^2+(z'(t))^2 } \, dt$ = distance traveled  

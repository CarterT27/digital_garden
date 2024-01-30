---  
tags:  
- Type/Note  
- Topic/Calculus  
- Class/MATH_20C  
date:  
- 2024-01-25  
---  
  
> [!note] Relative Position Between Two Planes in $\mathbb{R}^{3}$  
> 1. $P_{1}$ and $P_{2}$ are **parallel** or **coincide**. $\vec{n}_{1}$ is parallel to $\vec{n}_{2}$. $\vec{n}_{1}=\lambda \vec{n}_{2}$ for some scalar $\lambda$.  
> 2. If $P_{1}$ and $P_{2}$ are not parallel, then they intersect along a line. $\vec{n}_{1}$ and $\vec{n}_{2}$ are not parallel.  
  
> [!note] Relative Position Between a Line and a Plane in $\mathbb{R}^{3}$  
> 1. $L$ is parallel to $P$ or is contained in $P$. The direction vector $\vec{v}$ of $L$ is **orthogonal** to the normal vector $\vec{n}$ of $P$. $\vec{n}\cdot \vec{v}=\vec{0}$  
> 2. If the line and plane are not parallel, then they intersect at a unique point. $\vec{n}\cdot \vec{v}\neq \vec{0}$  
  
# 13.1 Vector Valued Function  
  
> [!note] Curve/Space Curve  
> Can be represented as $\vec{r}(t)=\langle x(t),y(t),z(t)\rangle=x(t)\vec{i}+y(t)\vec{j}+z(t)\vec{k}$  
> - $t$ is called a **parameter**  
> - $x(t),y(t),z(t)$ are called **components** or **coordinate functions**  
> - $\vec{r}(t)$ is called a **vector parameterization of the space curve**  
  
> [!question] Parameterize the Curve $C$ which is the intersection between $x^2-y^2=z-1,x^2+y^2=4$  
> $(x,y)=(2\cos t,2\sin t),0\leq t<2\pi$  
> $z=x^2-y^2+1=(2\cos t)^2-(2\sin t)^2+1=4\cos^2t-4\sin^2t+1$  
> $\implies \vec{r}(t)=\langle 2\cos t,2\sin t,4\cos^2t-4\sin^2t+1\rangle,0\leq t<2\pi$ is a vector parameterization of $C$.  
  
# 13.2 Limits  
  
> [!definition] Limit of Vector-Valued Function  
> Let $\vec{r}(t)=\langle x(t),y(t),z(t) \rangle$  
> The limit of the vector-valued function $\vec{r}(t)$ as $t\to t_{0}$ is defined as $\lim_{ t \to t_{0} }\vec{r}(t)=\langle \lim_{ t \to t_{0} }x(t),\lim_{ t \to t_{0} }y(t),\lim_{ t \to t_{0} }z(t)\rangle$  
  
> [!definition] Continuous  
> $\vec{r}(t)=\langle x(t),y(t),z(t) \rangle$ is **continuous** at $t=t_{0}$ if $\lim_{ t \to t_{0} }\vec{r}(t_{0})=\vec{r}(t_{0})$  
> 1. $\vec{r}(t)$ is continuous at $t_{0}$ iff all components $x(t),y(t),z(t)$ are continuous at $t_{0}$  
> 2. If $\vec{r}(t)$ is continuous at all values of t in the domain, we simply say the function is continuous.  

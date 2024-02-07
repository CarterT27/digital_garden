---
tags:  
- Type/Note  
- Topic/Calculus  
- Class/MATH_20C  
date:  
- 2024-01-17  
---
  
> [!note] Intersection of Two Lines  
> Remark: We say $\vec{r}_{1}(t)$ and $\vec{r}_{2}(t)$ **intersect** if $\vec{r}_{1}(t_{1})=\vec{r}_{2}(t_{2})$ for some $t_{1},t_{2}$.  
> $\vec{r}_{1}(t)$ and $\vec{r}_{2}(t)$ **collide** if $\vec{r}_{1}(t)=\vec{r}_{2}(t)$ for some t.  
  
# Surfaces in $\mathbb{R}^{3}$  
  
> [!note] Sphere  
> R: radius, $Q=(a,b,c)$ center  
> $\{(x,y,z)|(x-a)^2+(y-b)^2+(z-c)^2=R^2\}$  
  
> [!note] Cylinder  
> radius R, central axis $(a,b,c)$  
> Cylinder of radius R whose central axis is the vertical line through $(a,b,0)$ is  
> $\{(x,y,z)|(x-a)^2+(y-b)^2=R^2\}$  
  
> [!note] Dot Product  
> $\vec{v}\cdot\vec{w}=\langle v_{1},v_{2}\rangle\cdot \langle w_{1},w_{2}\rangle=v_{1}w_{1}+v_{2}w_{2}$  
> $\vec{v}\cdot\vec{w}=\langle v_{1},v_{2},v_{3}\rangle\cdot \langle w_{1},w_{2},w_{3}\rangle=v_{1}w_{1}+v_{2}w_{2}+v_{3}w_{3}$  
  
> [!note] $\Vert \vec{v}\Vert=\sqrt{ \vec{v}\cdot \vec{v} }$  
  
> [!note] Properties of the Dot Product  
> 1. $\vec{0}\cdot \vec{v}=\vec{v}\cdot  \vec{0}=0$  
> 2. $\vec{v}+\vec{w}=\vec{w}+\vec{v}$  
> 3. $(\lambda \vec{v})\cdot \vec{w}=\lambda(\vec{v}\cdot \vec{w})=\vec{v}\cdot(\lambda \vec{w})$  
> 4. $\vec{u}\cdot(\vec{v}+\vec{w})=\vec{u}\cdot \vec{v}+\vec{u}\cdot \vec{w}$  
> $(\vec{v}+\vec{w})\cdot\vec{u}=\vec{v}\cdot \vec{u}+\vec{w}\cdot \vec{u}$  
> 5. $\Vert \vec{v}\Vert^2=\vec{v}\cdot \vec{v}$  
  
> [!note] $\vec{v}\cdot \vec{w}=\Vert\vec{v}\Vert\Vert\vec{w}\Vert\cos \theta,0\leq \theta\leq \pi$  
> If $\vec{v},\vec{w}\neq \vec{0}$  
> $\cos \theta=\frac{\vec{v}\cdot \vec{w}}{\Vert\vec{v}\Vert\Vert\vec{w}\Vert}$  
  
> [!note] Angle between two vectors  
> 1. $\vec{v}\cdot\vec{w}=0\iff \theta=\frac{\pi}{2}\iff \vec{v}\perp \vec{w}$ (Orthogonal/Perpendicular)  
> 2. $\vec{v}\cdot \vec{w}<0\iff \frac{\pi}{2}<\theta\leq\pi \iff \theta$ is obtuse  
> 3. $\vec{v}\cdot \vec{w}>0\iff 0\leq \theta<\frac{\pi}{2}\iff \theta$ is acute  
  
> [!note] Projections  
> Assume $\vec{v}\neq \vec{0}$  
> 1. The **projection** of $\vec{u}$ along $\vec{v}$ is $\vec{u}_{\Vert\vec{v}}=\frac{\vec{u}\cdot \vec{v}}{\Vert\vec{v}\Vert^2}\vec{v}=\frac{\vec{u}\cdot \vec{v}}{\Vert\vec{v}\Vert}\frac{\vec{v}}{\Vert\vec{v}\Vert}=\text{proj}_{\vec{v}}\vec{u}$  
> $\implies\Vert\vec{u}_{\Vert\vec{v}}\Vert=\frac{\vec{u}\cdot \vec{v}}{\Vert\vec{v}\Vert}$  
> 2. The scalar $\frac{\vec{u}\cdot \vec{v}}{\Vert\vec{v}\Vert}=\text{comp}_{\vec{v}}\vec{u}$ is called the component or scalar component of $\vec{u}$ along $\vec{v}$  
> 3. $\vec{u}_{\perp \vec{v}}=\vec{u}-\vec{u}_{\Vert\vec{v}}$ is orthogonal to $\vec{v}$  
> 4. $\vec{u}=\vec{u}_{\Vert\vec{v}}+\vec{u}_{\perp \vec{v}}$ where $\vec{u}_{\Vert\vec{v}}$ is parallel to $\vec{v}$ and $\vec{u}_{\perp \vec{v}}$ is perpendicular to $\vec{v}$  

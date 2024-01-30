---  
tags:  
- "Type/Note"  
- "Topic/Calculus"  
- "Class/MATH_20C"  
date:  
- 2024-01-12  
---  
  
# 12.2 3D Space: Surfaces, Vectors, and Curves  
  
## Vector Operations  
  
$\vec{v}=\langle v_{1},v_{2},v_{3} \rangle,\vec{w}=\langle w_{1},w_{2},w_{3} \rangle$  
  
> [!note] 3D Vector Addition  
> $\vec{v}+\vec{w}=\langle v_{1}+w_{1},v_{2}+w_{2},v_{3}+w_{3}\rangle$  
  
> [!note] 3D Scalar Multiplication  
> $\lambda \vec{v}=\langle \lambda v_{1},\lambda v_{2},\lambda v_{3}$  
  
> [!note] Two nonzero vectors $\vec{v}$ and $\vec{w}$ are parallel iff $\vec{v}=\lambda \vec{w}$ for some scalar $\lambda$  
  
> [!note] Standard bases in $\mathbb{R}^{3}$  
> $\vec{i}=\langle 1,0,0\rangle,\vec{j}=\langle 0,1,0\rangle,\vec{k}=\langle 0,0,1\rangle$  
  
> [!note] Any 3D vector can be written uniquely as a linearl combination of $\vec{i},\vec{j},\vec{k}$.  
> $\langle a,b,c \rangle=a\vec{i}+b\vec{j}+c\vec{k}=a \langle 1,0,0 \rangle+b \langle 0,1,0 \rangle+c \langle 0,0,1 \rangle$  
  
> [!note] Norm/Length/Magnitude of $\vec{v}=\langle a,b,c \rangle$  
> $\Vert \vec{v}\Vert =\sqrt{ a^2+b^2+c^2 }$  
> In particular, the distance between $P=(a_{1},b_{1},c_{1}),Q=(a_{2},b_{2},c_{2})$ is $\Vert \vec{PQ}\Vert=\Vert a_{2}-a_{1},b_{2}-b_{1},c_{2}-c_{1}\rangle\Vert$  
> $=\sqrt{ (a_{2}-a_{1})^2+(b_{2}-b_{1})^2+(c_{2}-c_{1})^2 }$  
  
> [!definition] Vector Parameterization of a Line  
> $\vec{r}(t)=\langle x_{0},y_{0},z_{0}\rangle+t \langle a,b,c \rangle$  
> $\vec{v}$ is a **direction vector** of L  
> Parametric equations of the line L:  
> - $x(t)=x_{0}+ta$  
> - $y(t)=y_{0}+tb$  
> - $z(t)=z_{0}+tc$  
  
> [!note] Relative Position between two lines in $\mathbb{R}^{2}$  
> $L_{1},L_{2}$ are parallel or coincide $\iff \vec{v}_{1}=\lambda \vec{v}_{2}$ for some scalar $\lambda$  
> $L_{1},L_{2}$ intersect at a point  
> $L_{1},L_{2}$ do not intersect and are not parallel (skew lines)  

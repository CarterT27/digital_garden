---
tags:  
- Type/Note  
- Topic/Calculus  
- Class/MATH_20C  
---
  
> [!note] Projection: Given $\vec{v}\neq \vec{0}$  
> $\vec{u}_{\Vert\vec{v}}$ is the projection of $\vec{u}$ onto $\vec{v}$.  
> $\vec{u}_{\perp \vec{v}}$ is the component of $\vec{u}$ perpendicular to $\vec{v}$.  
> $\vec{u}=\vec{u}_{\Vert\vec{v}}+\vec{u}_{\perp \vec{v}}$  
  
> [!definition] $\vec{u}_{\Vert\vec{v}}$  
> $\vec{u}_{\Vert\vec{v}}=\frac{\vec{u}\cdot \vec{v}}{\Vert\vec{v}\Vert^2}\vec{v}=\frac{\vec{u}\cdot \vec{v}}{\Vert\vec{v}\Vert}e_{\vec{v}}$  
> Where $e_{\vec{v}}=\frac{\vec{v}}{\Vert\vec{v}\Vert}$  
  
> [!question] Find the distance from the point $P=(5,1,-3)$ to the line $L=\langle x(t),y(t),z(t) \rangle=\langle 4,4,2\rangle t$  
> Choose $\vec{v}=\langle 4,4,2\rangle$  
> $\vec{u}=\vec{0P}=\langle 5,1,-3 \rangle$  
> distance $=\Vert\vec{u}_{\perp \vec{v}}\Vert=\Vert\vec{u}-\vec{u}_{\Vert\vec{v}}\Vert$  
> $\vec{u}-\frac{\vec{u}\cdot \vec{v}}{\Vert\vec{v}\Vert^{2}}\vec{v}=\langle 5,1,-3\rangle-\frac{\langle 5,1,-3 \rangle\cdot \langle 4,4,2 \rangle}{\Vert \langle 4,4,2 \rangle\Vert^{2}}\langle 4,4,2 \rangle$  
> $=\langle 5, 1, -3 \rangle-\langle 2, 2, 1 \rangle=\langle 3, -1, 4 \rangle$  
> distance = $\sqrt{ 3^2+(-1)^2+(-1)^2 }=\sqrt{ 26 }$  
  
# 12.4 Cross Product  
  
> [!definition] Determinant $\in\mathbb{R}$  
> $$\begin{vmatrix}a & b \\ c & d\end{vmatrix}=ad-bc$$  
> $$\begin{vmatrix}a_{1} & b_{1} & c_{1} \\  a_{2} & b_{2} & c_{2} \\  a_{3} & b_{3} & c_{3}\end{vmatrix}=a_{1}\begin{vmatrix}b_{2} & c_{2} \\  b_{3} & c_{3}\end{vmatrix}-b_{1}\begin{vmatrix}a_{3} & c_{2} \\  a_{3} & c_{3}\end{vmatrix}+c_{1}\begin{vmatrix}a_{2} & b_{2} \\  a_{3} & b_{3}\end{vmatrix}$$  
  
> [!definition] Cross Product of 3D Vector  
> $\vec{v}=\langle v_{1},v_{2},v_{3} \rangle\in \mathbb{R}^{3}$  
> $\vec{w}=\langle w_{1},w_{2},w_{3} \rangle\in \mathbb{R}^{3}$  
> $$\vec{v}\times \vec{w}=\begin{vmatrix}\vec{i} & \vec{j} & \vec{k} \\  v_{1} & v_{2} & v_{3} \\  w_{1} & w_{2} & w_{3}\end{vmatrix}$$  
> $$=\vec{i}\begin{vmatrix}v_{2} & v_{3} \\  w_{2} & w_{3}\end{vmatrix}-\vec{j}\begin{vmatrix}v_{1} & v_{3} \\  w_{1} & w_{3}\end{vmatrix}+\vec{k}\begin{vmatrix}v_{1} & v_{2} \\  w_{1} & w_{2}\end{vmatrix}\in \mathbb{R}^{3}$$  
  
> [!note] Geometric Facts of Cross Product  
> 1. $\vec{v}\times \vec{w}$ is orthogonal to $\vec{v}$ and $\vec{w}$  
> 2. The direction of $\vec{v}\times \vec{w}$ is determined by the right-hand rule  
> 3. $\Vert\vec{v}\times \vec{w}\Vert=\Vert\vec{v}\Vert\Vert\vec{w}\Vert\sin \theta$  
  
> [!note] Basic Properties of the Cross Product  
> 1. $\vec{w}\times \vec{v}=-\vec{v}\times \vec{w}$  
> 2. $\vec{v}\times \vec{v}=\vec{0}$  
> 3. $\vec{v}\times \vec{w}=\vec{0}\iff \vec{v}=\vec{0}\text{ or }\vec{w}=\vec{0}\text{ or }\vec{v}=\lambda \vec{w}$ for some $\lambda$  
> 4. $(\lambda \vec{v})\times \vec{w}=\lambda(\vec{v}\times \vec{w})=\vec{v}\times(\lambda \vec{w})$  
> 5. $(\vec{u}+\vec{v})\times \vec{w}=\vec{u}\times \vec{w}+\vec{v}\times \vec{w}$  
> $\vec{u}\times(\vec{v}+\vec{w})=\vec{u}\times \vec{v}+\vec{u}\times \vec{w}$  

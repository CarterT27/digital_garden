---
tags:
- "Type/Note"
- "Topic/Calculus"
- "Class/MATH_20C"
date:
- 2024-01-10
---
# Continuation of 12.1  

> [!note] Components are written with angle brackets to emphasize that they are vectors and not points.  

> [!note] Vectors have length, points do not.  

> [!note] Length of a Vector  
> length/magnitude/norm of $\vec{v}=<a,b>$ is defined by $||v||=\sqrt{ a^2+b^2 }$  

> [!example] Compute the distance from P to Q  
> $P=(3,7),Q=(6,5)$  
> $||\vec{PQ}||=\text{distance}$  
> $\vec{PQ}=<6-3,5-7>=<3,-2>$  
> $||\vec{PQ}||=\sqrt{ (3)^2+(-2)^2 }=\sqrt{ 9+4 }=\sqrt{ 13 }$  

## Vector operations  

$\vec{v}=<a,b>,\vec{w}=<c,d>,\lambda\in\mathbb{R}$  
> [!note] Vector Addition  
> $\vec{v}+\vec{w}=<a+c,b+d>$  
> $\vec{v}-\vec{w}=<a-c,b-d>$  
> $\vec{v}+0=0+\vec{v}=\vec{v}$  

> [!note] Scalar Multiplication  
> $\lambda\vec{v}=<\lambda a,\lambda b>$  

> [!example] Computing Linear Combinations  
> $3\vec{v}-2\vec{w}$  
> $\vec{v}=<1,4>\vec{w}=<2,3>$  
> $3\vec{v}-2\vec{w}=3<1,4>-2<2,3>$  
> $=<3,12>-<4,6>$  
> $=<-1,6>$  

## Properties of vectors $\vec{u},\vec{v},\vec{w}$  

> [!note] Commutative  
> $\vec{v}+\vec{w}=\vec{w}+\vec{v}$  

> [!note] Associative  
> $(\vec{u}+\vec{v})+\vec{w}=\vec{u}+(\vec{v}+\vec{w})$  

> [!note] Distributive  
> $\lambda(\vec{v}+\vec{w})=\lambda \vec{v}+\lambda \vec{w}$  

## Linear Combination  

> [!definition] Linear Combination  
> A **linear combination** of $\vec{v}$ and $\vec{w}$ is a vector of the form $r\vec{v}+s\vec{w}$ where $r,s$ are scalars  
> e.g. $2\vec{v}+3\vec{w},5\vec{v}-\vec{w},\vec{v},\dots$  

> [!example] Standard basis vectors  
> $\vec{i},\vec{j}$  
> $\vec{i}=<1,0>,\vec{j}=<0,1>$  
> Any $\vec{v}\in\mathbb{R}^2$ is a unique linear combination of $\vec{i},\vec{j}$.  
> $\vec{v}=<a,b>\in\mathbb{R}^2=r\vec{i}+s\vec{j}$ has the unique solution $r=a,s=b$  
> $\vec{v}=<a,b>=a\vec{i}+b\vec{j}$  
> Check:  
> $a\vec{i}+b\vec{j}=a<1,0>+b<0,1>\impliedby a,0>+<0,b>=<a,b>$  

## Direction of vectors  

> [!definition] Unit Vector  
> A vector of length 1 is called a **unit vector**.  
> $\vec{e}=<a,b>$  
> $\vec{e}$ is a unit vector iff $||\vec{e}||=\sqrt{ a^2+b^2 }=1$  
> $\vec{e}$ is a unit vector iff $a^2+b^2=1$  

> [!example] Unit vectors  
> $<\frac{1}{2},\frac{\sqrt{ 3 }}{2}>$ is a unit vector  
> $<1,2>$ is not a unit vector  

> [!note] If $\vec{e}$ is a unit vector, $\vec{e}=<a,b>=<\cos \theta,\sin \theta>$  
> $x\text{ degrees}=\frac{x}{180}\pi \text{ radians}$  

> [!note] For any vector, we can obtain a unique unit vector in the same direction.  
> $\vec{v}=<v_{1},v_{2}>$  
> $\vec{e}_{v}=\frac{\vec{v}}{||\vec{v}||}=\frac{1}{||\vec{v}||}\vec{v}$  
> Check:  
> $||\frac{1}{||\vec{v}||}\vec{v}||=\frac{1}{||\vec{v}||}||\vec{v}||=1$  
> $\vec{v}=||\vec{v}||\vec{e}_{v}=\text{length}\cdot \text{direction}$  

> [!example] $\vec{v}=<2,4>$ compute $\vec{e}_{v}$  
> $\vec{e}_{v}=\frac{\vec{v}}{||\vec{v}||}=\frac{<2,4>}{\sqrt{ 4+16 }}=\frac{<2,4>}{\sqrt{ 20 }}=<\frac{2}{\sqrt{ 20 }},\frac{4}{\sqrt{ 20 }}>$  
> *Final solution need not be simplified unless specified because calculators are not allowed on the exams.  

# 12.2 - 3D Space: Surfaces, vectors, and curves  

> [!definition] Right Hand Rule  
> The z axis is perpendicular to both the x and y axes. The conventional direction of z is determined by the **right hand rule**  
> Point your fingers extended outwards towards x, curl them towards y, the thumb is pointed to z.  

> [!note] 3D Set Notation  
> $\mathbb{R}^3=\{ (a,b,c)|a,b,c\in\mathbb{R} \}$  
> *Set notation: $\{ \text{elements}|\text{conditions} \}$  

> [!note] 3D point and vector notation  
> $P=(a,b,c),\vec{v}=<a,b,c>$  

> [!definition] Coordinate Planes  
> xy-plane=$\{ (a,b,0)|a,b\in\mathbb{R} \}$  
> xz-plane=$\{ (a,0,c)|a,c\in\mathbb{R} \}$  
> yz-plane=$\{ (0,b,c)|b,c\in\mathbb{R} \}$  

> [!note] 3D vector operations are similar to those in 2D  

> [!example] $P=(1,2,3),Q=(2,-2,0)$  
> $\vec{PQ}=<2-1,-2-2,0-3>=<1,-4,-3>$  
> $\vec{QP}=<1-2,2-(-2),3-0>=<-1,4,3>$  

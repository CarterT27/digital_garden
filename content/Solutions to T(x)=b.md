---
mathLink: Solutions to $T(\vec{x})=\vec{b}$
tags:
  - "#Type/Proposition"
  - "#Topic/Linear_Algebra"
  - "#Class/MATH_31AH"
---
Proved by: <i>Not Applicable</i>  
References: [[Kernel]], [[Image of Linear Transformation]]  
Justifications: <i>Not Applicable</i>  

Specializations: <i>Not Applicable</i>  
Generalizations: <i>Not Applicable</i>  

> [!proposition] Solutions to $T(\vec{x})=\vec{b}$
> Let $T:\mathbb{R}^n\to\mathbb{R}^m$ be a [[linear transformation]]. The system of linear equations $T(\vec{x})=\vec{b}$ has  
> 1. *at most one solution* for every $\vec{b}\in\mathbb{R}^m$ iff $\text{ker }T=\vec{0}$.
> 2. *at least one solution* for every $\vec{b}\in\mathbb{R}^m$ iff $\text{img }T=\mathbb{R}^m$.

**Proof.**
1. If the kernel of $T$ is not $\{\vec{0}\}$, then there is more than one solution to $T(\vec{x})=\vec{0}$. (Of course, one solution is $\vec{x}=\vec{0}$).  
In the other direction, if there exists a $\vec{b}$ for which $T(\vec{x})=\vec{b}$ has more than one solution, i.e.,  
$$T(\vec{x}_{1})=T(\vec{x}_{2})=\vec{b}\text{ and }\vec{x}_{1}\neq \vec{x}_{2}\text{, then}$$
$$T(\vec{x}_{1}-\vec{x}_{2})=T(\vec{x}_{1})-T(\vec{x}_{2})=\vec{b}-\vec{b}=\vec{0}.$$
So $(\vec{x}_{1}-\vec{x}_{2})$ is a nonzero element of the kernel, so $\text{ker }T\neq\{\vec{0}\}$.
2. Saying that $\text{img }T=\mathbb{R}^m$ is exactly saying that $T$ is onto.
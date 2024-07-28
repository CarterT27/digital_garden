---
tags:
- "Type/Note"
- "Topic/Differential_Equations"
- "Class/MATH_20D"
date:
- 2024-02-14
---
# 9.5 and 9.6 - Homogeneous Linear Systems with Constant Coefficients  

Fact: Suppose the $n\times n$ matrix has eigenvalues $\lambda_1,\lambda_2,\dots,\lambda_n$ (some of them may be repeated) and *$n$ linearly independent* eigenvectors $\vec{x}_1,\vec{x}_2,\dots,\vec{x}_n$. Then the general solution to the homogeneous system $\vec{x}'=A\vec{x}$ is given by  
$$\vec{x}(t)=C_1e^{\lambda_1t}\vec{x}_1+C_2e^{\lambda_2t}\vec{x}_2+\cdots+C_ne^{\lambda_nt}\vec{x}_n$$  
where $C_i$'s are arbitrary constants.  

Fact: Suppose the real matrix $A$ has *complex eigenvalues* $\alpha\pm i\beta$ with corresponding eigenvectors $a\pm ib$ then two linearly independent solutions to the homogeneous system $\vec{x}'=A\vec{x}$ are given by  
$$\vec{x}_1=e^{\alpha t}\cos(\beta t)\vec{a}-e^{\alpha t}\sin(\beta t)\vec{b}$$  
$$\vec{x}_2=e^{\alpha t}\sin(\beta t)\vec{a}+e^{\alpha t}\cos(\beta t)\vec{b}$$  

## 5.4 - Phase Plane of $2\times2$ Systems  

For each of the following examples, we are given a $2\times2$ matrix $A$ and its eigenvalues/eigenvectors.  
1. Write the general solution to the system $\vec{x}'=A\vec{x}$  
2. Draw the phaseplane of the system $\vec{x}'=A\vec{x}$ and discuss the asymptotic behavior of the solution curves  
3. Discuss the type and stability of the origin  

**Case 1.** $A$ has two distinct real-valued eigenvalues of opposite signs.  
**Case 3b.** $A$ has complex eigenvalues $\lambda_{1,2}=\alpha\pm i\beta$ with $\alpha>0$  
**Case 3c.** $A$ has complex eigenvalues $\lambda_{1,2}=\alpha\pm i\beta$ with $\alpha<0$  

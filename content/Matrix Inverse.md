---
mathLink: auto
tags:
  - "Type/Definition"
  - "Topic/Linear_Algebra"
  - "Class/MATH_31AH"
---
Types: <i>Not Applicable</i>  
Examples: [[Inverse of a 2x2 Matrix]]  
Constructions: <i>Not Applicable</i>  
Generalizations: <i>Not Applicable</i>  

Properties: <i>Not Applicable</i>  
Sufficiencies: <i>Not Applicable</i>  
Equivalences: <i>Not Applicable</i>  
Justifications: <i>Not Applicable</i>  

> [!definition] Matrix Inverse
> If a [[matrix]] $A$ has both a [[Left and Right Inverses of Matrices|left inverse]] and a [[Left and Right Inverses of Matrices|right inverse]], then it has only one left inverse and one right inverse, and they are identical; such a matrix is called the **inverse** of $A$ and is denoted $A^{-1}$.

**Proof.** If a matrix $A$ has a right inverse $B$, then $AB=I$. If it has a left inverse $C$, then $CA=I$. So  
$$C(AB)=CI=C\text{ and }(CA)B=IB=B,\text{ so }C=B.$$
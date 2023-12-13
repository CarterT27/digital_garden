---
mathLink: auto
tags:
  - "#Type/Theorem"
  - "#Topic/Linear_Algebra"
  - "#Class/MATH_31AH"
---
Proved by: <i>Not Applicable</i>  
References: <i>Not Applicable</i>  
Justifications: <i>Not Applicable</i>  

Specializations: <i>Not Applicable</i>  
Generalizations: <i>Not Applicable</i>  

> [!theorem] Transpose of Product
> The **transpose of a product** is the product of the transposes in reverse order:  
> $$(AB)^T=B^TA^T.$$

**Proof.** 
$$(AB)^T_{i,j}=(AB)_{j,i}$$
$$(AB)_{j,i}=\sum_{n=1}^ka_{j,n}b_{n,i}=\sum_{n=1}^kb_{n,i}a_{j,n}=(B^TA^T)_{i,j}$$
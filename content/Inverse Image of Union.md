---
mathLink: $f^{-1}(A\cup B)=f^{-1}(A)\cup f^{-1}(B)$
tags:
  - "#Type/Proposition"
  - "#Topic/Linear_Algebra"
  - "#Class/MATH_31AH"
---
Proved by: <i>Not Applicable</i>  
References: <i>Not Applicable</i>  
Justifications: <i>Not Applicable</i>  

Specializations: <i>Not Applicable</i>  
Generalizations: <i>Not Applicable</i>  

> [!proposition] Inverse Image of Union
> The [[inverse image]] of a union equals the union of the inverse images:  
> $$f^{-1}(A\cup B)=f^{-1}(A)\cup f^{-1}(B).$$

**Proof.**
($\implies$) Let $x\in f^{-1}(A\cup B)$.
$\implies f(x)\in A\cup B$
$\implies f(x)\in A$ or $f(x)\in B$
$\implies x\in f^{-1}(A)$ or $x\in f^{-1}(B)$
$\implies x\in f^{-1}(A)\cup f^{-1}(B)$

($\impliedby$) Let $x\in f^{-1}(A)\cup f^{-1}(B)$
$\implies x\in f^{-1}(x)$ or $x\in f^{-1}(B)$
$\implies f(x)\in A$ or $f(x)\in B$
$\implies f(x)\in A\cup B$
$\implies x\in f^{-1}(A\cup B)$

Together, these two implications prove $f^{-1}(A\cup B)=f^{-1}(A)\cup f^{-1}(B)$.
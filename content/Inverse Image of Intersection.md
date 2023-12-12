---
mathLink: $f^{-1}(A\cap B)=f^{-1}(A)\cap f^{-1}(B)$
tags:
  - "#Type/Proposition"
  - "#Topic/TOPIC"
  - "#Class/CLASS"
---
Proved by: <i>Not Applicable</i>  
References: <i>Not Applicable</i>  
Justifications: <i>Not Applicable</i>  

Specializations: <i>Not Applicable</i>  
Generalizations: <i>Not Applicable</i>  

> [!proposition] Inverse Image of Intersection
> The [[inverse image]] of an intersection equals the intersection of the inverse images:  
> $$f^{-1}(A\cap B)=f^{-1}(A)\cap f^{-1}(B).$$

**Proof.**
($\implies$) Let $x\in f^{-1}(A\cap B)$.  
$\implies f(x)=A\cap B$
$\implies f(x)=A$ and $f(x)=B$
$\implies x\in f^{-1}(A)$ and $x\in f^{-1}(B)$.
$\implies x\in f^{-1}(A)\cap f^{-1}(B)$

($\impliedby$) Let $x\in f^{-1}(A)\cap f^{-1}(B)$.
$\implies x\in f^{-1}(A)$ and $x\in f^{-1}(B)$
$\implies f(x)=A$ and $f(x)=B$
$\implies f(x)=A\cap B$
$\implies x\in f^{-1}(A\cap B)$

Together, these two implications prove that $f^{-1}(A\cap B)=f^{-1}(A)\cap f^{-1}(B)$
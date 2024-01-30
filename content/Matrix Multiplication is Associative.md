---  
mathLink: auto  
tags:  
- "Type/Proposition"  
- "Topic/Linear_Algebra"  
- "Class/MATH_31AH"  
---  
Proved by: [[The ith Column of AB is Abi]], [[The ith Row of AB is the Product of The ith Row of A and Matrix B]]  
References: <i>Not Applicable</i>  
Justifications: <i>Not Applicable</i>  
  
Specializations: <i>Not Applicable</i>  
Generalizations: <i>Not Applicable</i>  
  
> [!proposition] Matrix Multiplication is Associative  
> If $A$ is an $n \times n$ [[matrix]], $B$ is an $m \times p$ matrix, and $C$ a $p \times q$ matrix, so that $(AB)C$ and $A(BC)$ are both defined, then they are equal:  
> $$(AB)C=A(BC).$$  
  
**Proof.**  
Since [[The ith Column of AB is Abi]] and [[The ith Row of AB is the Product of The ith Row of A and Matrix B]], the $(i,j)$the entry of both $A(BC)$ and $(AB)C$ depend on only the $i$th row of $A$ and the $j$th column of $C$ (but on all the entries of $B$). Without loss of generality we can assume that $A$ is a line matrix and $C$ is a column matrix ($n=q=1$), so that both $(AB)C$ and $A(BC)$ are numbers. Now apply the [[Multiplicative Associativity|associativity of multiplication of numbers]]:  
$$(AB)C=\sum_{l=1}^{p}\left( \sum_{k=1}^ma_{k}b_{k,l}\right)c_{l}$$  
$$=\sum_{l=1}^p\sum_{k=1}^na_{k}b_{k,l}c_{l}=\sum_{k=1}^ma_{k}\left( \sum_{l=1}^p b_{k,l}c_{l}\right)=A(BC).$$  

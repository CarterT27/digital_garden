---
tags:
- "Type/Note"
- "Topic/Mathematics"
- "Class/MATH_109"
date:
- 2024-09-30
---

## Priority of logical connectors

high to low: $\neg$, $\land$, $\lor$

$(\neg P) \lor Q$

Implication: $\implies$

In $P \implies Q$:
- $P$ is called the **hypothesis**
- $Q$ is called the **conclusion**

Ways to read $P\implies Q$
- $P$ implies $Q$
- If $P$ then $Q$
- $Q$ if $P$
- $P$ only if $Q$
- $Q$ whenever $P$
- $P$ is sufficient for $Q$
- $Q$ is necessary for $P$

The **converse** of $P\implies Q$ is $Q\implies P$  
The **negation** of $P\implies Q$ is $\neg (P\implies Q)$  
The **contrapositive** of $P\implies Q$ is $\neg Q\implies \neg P$

Equivalence: $\iff$
$P\iff Q$ reads as:
- $P$ is equivalent to $Q$
- $P$ is necessary and sufficient for $Q$
- $P$ if and only if $Q$
- $P$ iff $Q$
- $P$ precisely when $Q$

| $P$ | $Q$ | $P \iff Q$ |
| --- | --- | --- |
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

$P \iff Q$ is true when $P$, $Q$ have the same truth value.

$P\iff Q$ is the same as $(P\implies Q)\land (Q\implies P)$

When $P\iff Q$ is true, we say $P$, $Q$ are **logically equivalent**

> [!definition] Logically Equivalent
> Two statements $P$, $Q$ are logically equivalent if $P\iff Q$ is always true for all possibilities of atomic statement truth value combinations

Example: $P\iff Q$ is logically equivalent to $Q\iff P$

To verify, we check $(P \iff Q) \iff ((P \implies Q) \land (Q \implies P))$ is true

| $P$ | $Q$ | $P\iff Q$ | $Q\iff P$ | $(P \iff Q) \iff ((P \implies Q) \land (Q \implies P))$ |
| --- | --- | --- | --- | --- |
| T | T | T | T | T |
| T | F | F | F | T |
| F | T | F | F | T |
| F | F | T | T | T |

---
tags:
- "Type/Note"
- "Topic/Mathematics"
- "Class/MATH_109"
date:
- 2024-10-02
---

Definitions and axioms

> [!definition] Axiom
> Statement that we assume to be true

Assuming familiarity with
- Natural numbers ($\mathbb{N}$): 0, 1, 2, 3, ...
- Integers ($\mathbb{Z}$)
- Rational numbers ($\mathbb{Q}$)
- Real numbers ($\mathbb{R}$)

> [!definition] Let $a, b$ be two integers
> We say $a$ divides $b$ if there exists an integer $c$ s.t. $b=ac$

> [!definition] If $a$ divides $b$
> We say that $b$ is a **multiple** of $a$
> And that $a$ is a **factor** of $b$
> We can also denote $a$ divides $b$ as $a \vert b$

> [!definition] An integer $m$ is **even** if $2\vert m$

> [!definition] An integer $m$ is **odd** if $m$ is not even

0 is even because $0=2\cdot0$

> [!proposition] 0 is an even number
> $0=2\cdot 0$
> 2 divides 0
> By definition of even numbers, 0 is an even number

> [!proposition] The sum of two even numbers is even
> Let $m, n$ be two even numbers such that their sum is even.
> There exists two integers $s, t$ such that $m=2s, n=2t$
> $m+n = 2s + 2t = 2(s+t)$
> The sum of two integers is an integer
> $s+t$ is an integer, therefore 2 divides $m+n$.
> Therefore, $m+n$ must be even

> [!proposition] 1 is not even (1 is odd)
> $1=2\cdot \frac{1}{2}$ - not a proof because we need to prove that $\frac{1}{2}$ is not an integer $c$
> Circular reasoning

Axioms of Orders (3.1.2 in the textbook)
- $a>b,a=b,a<c$ - one of them is true
- If $a>b$ then $a+c>b+c$, and if $a<b$ then $a+c<b+c$
- If $a>b,c>0$ then $ac>bc$, and if $a>b,c<0$, then $ac<bc$
- If $a>b,b>c$ then $a>c$

Let $q$ be a natural number  
Case 1: If $q=0$ then $2q=0$ so $q\neq 1$  
Case 2: If $q<0$ then $2q<q*0=0$ so $q \neq 1$  
Case 3: If $q>0$ then $2q\geq q*1 \geq 2$ so $q \neq 1$  
So in all cases, $2q\neq 1$ so 1 is odd

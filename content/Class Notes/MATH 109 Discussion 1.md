---
tags:
- "Type/Note"
- "Topic/Mathematics"
- "Class/MATH_109"
date:
- 2024-10-03
---

# Necessary and Sufficient Conditions, Axiomatic Properties of the Real Numbers

> [!proposition] 2.3.1: + and - for real numbers
> $a,b\in \mathbb{R}$
> 1. Commutativity: $a+b=b+a, a\cdot b = b\cdot a$
> 2. Associativity: $(a+b)+c=a+(b+c), (a\cdot b)\cdot c = a\cdot (b\cdot c)$
> 3. Distributivity: $a\cdot(b+c) = c\cdot b + a\cdot c, (a+b)\cdot c = a\cdot c + b \cdot c$
> 4. Zero Identity: $0\in \mathbb{R}, a+0=a\forall a \in \mathbb{R}$
> 5. Unity: $1\in \mathbb{R}, a\cdot 1 = a \forall a \in \mathbb{R}$
> 6. Subtractivity: $\forall a, \text{the equation } a+x=0\text{ has a unique solution, called }-a$ ($b-a$ is defined as $b+(-a)$)
> 7. Division: $\forall a \neq 0,\text{ the equation }a \cdot x = 1 \text{ has a unique solution }\frac{1}{a}$ ($\forall b$, $\frac{b}{a}$ is defined as $b\cdot\left(\frac{1}{a}\right)$)
> 
> In one word, 1-7 collectively say $\mathbb{R}$ is a **field**.

> [!question] Which of the following conditions are necessary for the positive integer $n$ to be divisible by 6 (proofs are not necessary)?
> 1. 3 divides $n$
> 2. 9 divides $n$
> 3. 12 divides $n$
> 4. $n=12$
> 5. 6 divides $n^2$
> 6. 2 divides $n$ and 3 divides $n$
> 7. 2 divides $n$ or 3 divides $n$

> [!answer]-
> Necessary is the same as saying $n$ is divisible by 6 $\implies$ a condition
> 1, 5, 6, 7
> Strong condition (6) implies weak condition (7)
> 
> Sufficient is the same as saying condition $\implies$ $n$ is divisible by 6
> 1. 3 divides $n$ - necessary
> 2. 9 divides $n$ - neither
> 3. 12 divides $n$ - sufficient
> 4. $n=12$ - sufficient
> 5. 6 divides $n^2$ - necessary, sufficient
> 6. 2 divides $n$ and 3 divides $n$ - necessary, sufficient
> 7. 2 divides $n$ or 3 divides $n$ - necessary

> [!question] Use the properties of addition and multiplication of real numbers given in Properties 2.3.1 to deduce that, for all real numbers $a$ and $b$,
> 1. $a\times 0 = 0 = 0 \times a$
> 2. $(-a)b=-ab=a(-b)$
> 3. $(-a)(-b)=ab$

> [!answer]
> **Problem 1.** $a\times 0 = 0 = 0\times a$
> 
> $a\times (1+0) = a\times 1= a$
> $a\times (1+0) = a\times 1 + a\times 0= a + a\times 0$
> Subtracting $a$ from both sides:
> $a\times 0 = 0$
> Commutative: $0\times a = a \times 0 = 0$
> 
> **Problem 2.** $(-a)b=-ab=a(-b)$
> 
> $(a+(-a))\times b = 0 \times b = 0$
> $=a\times b + (-a) \times b$
> Subtracting $a\times b$: $(-a)\times b = -ab$
> Commutative: $b\times(-a) = -ba$
> 
> **Problem 3.** $(-a)(-b)=ab$
> 
> $(-a)(-b) = -(a\cdot(-b)) = -(-(ab))$
> $-(-ab)$ and $ab$ both solve the equation $x+(-ab)=0$ so $-(-ab)=ab$

---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/DSC_40B"
date:
- 2024-10-03
---

# Growth Rates

## Common Growth Rates

$\Theta(1)$: Constant
$\Theta(\log n)$: Logarithmic
$\Theta(n)$: Linear
$\Theta(n \log n)$: Linearithmic
$\Theta(n^2)$: Quadratic
$\Theta(n^3)$: Cubic
$\Theta(2^n)$: Exponential

## Asymptotic Notation

$\Theta(\cdot)$ vs. $O(\cdot)$ and $\Omega(\cdot)$

$\Theta(\cdot)$ ignores constant factors and lower-order terms

> [!definition] Big Theta
> We say that $f(n)=\Theta(g(n))$ if there are positive constants $N, c_1, c_2$ such that for all $n \geq N$:
> $$c_1 \cdot g(n) \leq f(n) \leq c_2 \cdot g(n)$$

Basically means we can sandwich $f(n)$ between two versions of $g(n)$

## Upper bounding tips

- Promote lower-order positive terms
- Drop negative terms

## Lower bounding tips

- Drop lower-order positive terms
- Promote and cancel negative lower-order terms if possible
- Cancel negative lower-order terms with big constants by breaking off a piece of high term

## Caution

- To upper bound a fraction $\frac{A}{B}$, you must
    - Upper bound the numerator, $A$
    - Lower bound the denominator, $B$
- To lower bound a fraction $\frac{A}{B}$, you must
    - Lower bound the numerator, $A$
    - Upper bound the denominator, $B$

## Big-O and Big-$\Omega$

Sometimes we only care about an upper bound.  
$f(n) = O(g(n))$ if $f$ "grows at most as fast as $g$

Examples:
- $4n^2=O(n^100)$
- $4n^2=O(n^3)$
- $4n^2=O(n^2)$

> [!definition] Big O
> We say that $f(n)=O(g(n))$ if there are positive constants $N, c$ such that for all $n \geq N$:
> $$f(n) \leq c \cdot g(n)$$

Sometimes we only care about a lower bound.
$f(n) = \Omega(g(n))$ if $f$ "grows at least as fast as fast" as $g$.
- $4n^{100}=\Omega(n^5)$
- $4n^{2}=\Omega(n)$
- $4n^{2}=\Omega(n^2)$

> [!definition] Big Omega
> We say that $f(n)=\Omega(g(n))$ if there are positive constants $N, c$ such that for all $n \geq N$:
> $$c \cdot g(n) \leq f(n)$$

## Theta, Big O, and Big Omega

- If $f=\Theta(g)$, then $f=O(g)$ and $f=\Omega(g)$
- If $f=O(g)$ and $f=\Omega(g)$ then $f=\Theta(g)$

In other words (symbols)
- $\Theta \implies (O \land \Omega)$
- $(O \land \Omega) \implies \Theta$

## Analogies

- $\Theta$ is kind of like $=$
- O is kind of like $\leq$
- $\Omega$ is kind of like $\geq$

## Other notations

- $f(n) = o(g(n))$ if $f$ grows "much slower" than $g$
- $f(n) = \omega(g(n))$ if $f$ grows "much faster" than $g$

## Properties of $\Theta$

1. **Symmetry**: If $f=\Theta(g)$, then $g=\Theta(f)$
2. **Transitivity**: If $f=\Theta(g)$ and $g=\Theta(h)$ then $f=\Theta(h)$
3. **Reflexivity**: $f=\Theta(f)$

- If $f=O(g)$ and $g=O(h)$ then $f=O(h)$
- If $f_1=\Theta(g_1)$ and $f_2=\Theta(g_2)$ then $f_1 \times f_2 = \Theta(g_1 \times g_2)$

## Proving/Disproving Properties

- Start by trying to disprove
- Finding a counterexample
- If you can't disprove, maybe it's true

1. State the assumptions (constants)
2. Use the assumptions (chain of inequalities)

> [!property] Sums of Theta
> If $f_1=\Theta(g_1)$ and $f_2=\Theta(g_2)$ then $f_1 + f_2 = \Theta(g_1 + g_2)$
> Used when analyzing **sequential** code

> [!property] Products of Theta
> If $f_1=\Theta(g_1)$ and $f_2=\Theta(g_2)$ then $f_1 \cdot f_2 = \Theta(g_1 \cdot g_2)$
> Used when analyzing **loops**
> **Careful**: If the inner loop index depends on the outer loop, you have to be more careful.

## Asymptotic Notation Practicalities

Asymptotic notation is not just used to denote algorithms, e.g. "n choose k" and error of sample mean in Central Limit Theorem

### Faux Pas

- Don't include constants or lower-order terms in the notation
- Don't include base in logarithm
- Don't misinterpret the meaning of $\Theta(\cdot)$
- Time complexity is not a **complete** measure of efficiency
    - Asymptotic notation "hides the constants"

> [!note] Main Idea
> Time complexity is not the **only** way to measure efficiency, and it can be misleading.
> Sometimes even a $\Theta(2^n)$ algorithm is better than a $\Theta(n)$ algorithm, if the data size is small.

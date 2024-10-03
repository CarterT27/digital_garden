---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/DSC_40B"
date:
- 2024-10-01
---

Source: https://dsc40b.com/materials/lectures/02-time_complexity-pt_I/slides-marked.pdf

> [!example] Design an algorithm for the following problem
> Given the heights of $n$ people, what is the height of the tallest doctor you can make by stacking two of them?

Brute force solution
- Loop through all possible (ordered) pairs
- Check height of each
- Keep the best

```python
def tallest_doctor(heights):
    max_height = -float('inf')
    n = len(heights)
    for i in range(n):
        for j in range(n):
            if i == j:
            continue
            height = heights[i] + heights[j]
            if height > max_height:
            max_height = height
            return max_height
```
$\Theta(n^2)$

```python
def tallest_doctor_2(heights):
    max_height = -float('inf')
    n = len(heights)
    for i in range(n):
        for j in range(i + 1, n):
            height = heights[i] + height[j]
            if height > max_height:
                max_height = height
```
$\sum_{i=1}^{n} i=\frac{n(n+1)}{2}$
$\Theta(n^2)$

> [!definition] Linear Time
> $T(n)=\Theta(n)$

> [!definition] Quadratic Time
> $T(n)=\Theta(n^2)$

Linear growth: if input size doubles, time roughly doubles

Quadratic growth: if input size doubles, time roughly quadruples

Exponential growth: increasing input size by one doubles (or triples, quadruples, etc.) time taken

Example: brute force search of $2^n$ subsets

Logarithmic growth: to increase time taken by one unit, must double (triple, etc.) input size

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

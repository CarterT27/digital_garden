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

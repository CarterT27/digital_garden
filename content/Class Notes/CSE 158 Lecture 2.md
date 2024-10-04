---
tags:
- "Type/Note"
- "Topic/Data_Mining"
- "Class/CSE_158"
date:
- 2024-10-01
---

# Supervised Learning and Regression

> [!definition] Regression
> **Regression** is one of the simplest supervised learning approaches to learn relationships between input variables (features) and output variables (predictions).

> [!definition] Linear regression
> **Linear regression** assums a predictor of the form 
> $$X\theta=y$$
> $X$: matrix of features (data)
> $\theta$: unknowns (which features are relevant)
> $y$: vector of outputs (labels)
> $$\text{Or }Ax=b\text{ if you prefer}$$

One observation: $y=x\cdot\theta$

Q: Solve for theta  
A: $X^{-1}X\theta = X^{-1}y$ - doesn't work because $X$ is not necessarily invertible (not square)  
A: $\theta=(X^T X)^{-1} X^T y$

```python
theta, residuals, rank, s = numpy.linalg.lstsq(X, y)
```

We can perform arbitrary combinations of the **features** and the model will still be linear in in the **parameters** (theta):
$$\text{Rating}=\theta x$$

The **linear** models we've seen so far do not support transformations (they need to be linear in their parameters)
There *are* alternative models that support non-linear transformations of parameters, e.g. neural networks


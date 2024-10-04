---
tags:
- "Type/Note"
- "Topic/Data_Mining"
- "Class/CSE_158"
date:
- 2024-10-03
---

**one-hot encoding**: encoding where the feature vector has a single "1" entry
- feature = \[0, 0, 0\] for "male"
- feature = \[1, 0, 0\] for "female"
- feature = \[0, 1, 0\] for "other"
- feature = \[0, 0, 1\] for "not specified"
- Note that to capture 4 possible categories, we only need three dimensions (a dimension for "male" would be redundant)
- This approach can be used to capture a variety of categorical feature types, along with objects that belong to multiple categories

Features can be piecewise functions, allowing us to handle complex shapes, periodicity, etc.
- Still a form of **one-hot** encoding

## Regression Diagnostics

> [!definition] Mean-squared error (MSE)
> $$\frac{1}{N} \Vert y - X\Theta \Vert_2^2$$
> $$=\frac{1}{N} \sum_{i=1}^N (y_i - X_i \cdot \Theta)^2$$

$\Vert x \Vert_2^2 = \sum_i x_i^2$
$\Vert x \Vert_a = \sqrt[a]{\sum_i x_i^a}$

> [!question] Why MSE (and not mean-absolute-error or something else)
> Assuming the errors form a Gaussian distribution (centered around 0, mostly small errors, large errors are rare)
> (not important) Can use a Q-Q plot to visualize the distribution of the errors
> $y_i = x_i\cdot \Theta + N(0, \sigma^2)$
> $P_0(y \vert X) = \prod_i \frac{1}{\sqrt{2\pi}\sigma} e - \frac{(y_i - x_i\cdot \Theta)^2}{2\sigma^2}$
> $max P_\Theta(y \vert X) = \sum_i - (y_i - x_i \cdot \Theta)^2$
> $min -P_\Theta(y \vert X) = \sum_i (y_i - x_i \cdot \Theta)^2$

> [!question] How long does the MSE have to be before it's "low enough"?
> It depends. The MSE is proportional to the **variance** of the distribution

> [!definition] Coefficient of determination
> The $R^2$ statistic
> Mean: $\bar{y} = \frac{1}{N} \sum_i y_i$
> Variance: $\text{var}(y) = \frac{1}{N} \sum_i (y_i - \bar{y})^2$
> MSE: $\text{MSE}_\Theta (y \vert X) = \frac{1}{N} \sum_i (y_i - x_i \cdot \Theta)^2$
> 
> $$\text{FVU}(f) = \frac{\text{MSE}(f)}{\text{Var}(y)}$$
> FVU = fraction of variance unexplained
> FVU(f) = 1: trivial predictor
> FVU(f) = 0: perfect predictor
> 
> $R^2 = 1 - \text{FVU}(f) = 1 - \frac{\text{MSE}(f)}{\text{Var}(y)}$
> $R^2$ = 0: trivial predictor
> $R^2$ = 1: perfect predictor

> [!question] Can't we get an $R^2$ of 1 by throwing in a bunch of random features?
> Yes
> "Among competing hypotheses, the one with the fewest assumptions should be selected"

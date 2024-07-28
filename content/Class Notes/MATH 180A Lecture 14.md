---
tags:
- "Type/Note"
- "Topic/Probability"
- "Class/MATH_180A"
date:
- 2024-05-06
---

## Functions of Continuous Random Variables

Expectation of function of discrete r.v. $X: \mathbb{E}[g(X)]=\sum_{a\in \mathbb{R}}g(a)p_{X}(a)$.

> [!note] **Theorem**: If $X$ is a continuous random variable and $g$ is a function, then
> $$\mathbb{E}[g(X)]=\int _{-\infty}^{\infty}g(t)f_{X}(t) \, dt $$

**Example.** You throw a dart at a circular board of radius 1 ft. It hits a point on the board uniformly at random, and you win $\$ \frac{1}{r}$ if the dart hits a point at distance $r$ ft from the center. What are your expected winnings?

$W=g(X)$ where X = distance of point to center, $g(t)=\frac{1}{t},g(X)=\frac{1}{X}$
$\mathbb{E}[W]=\int _{-\infty}^{\infty}g(t)f_{X}(t) \, dt=\int _{0}^{1} \frac{1}{t}2t \, dt=\int _{0}^{1}2 \, dt=\boxed{\$2}$

**Example.** Suppose $X$ is a r.v. w/ cdf $F_{X}(t)=\begin{cases} \frac{1}{t^{2}}& t\leq-1\\1&-1<t\end{cases}$. Is $X$ discrete or continuous? If so, calculate (i) the mean of $X$, (ii) $\mathbb{E}[\sqrt[3]{ X }]$, and (iii) $\mathbb{E}[\cos(X)]$.

$F_{X}$ continuous and piecewise continuously differentiable $\implies X$ is a continuous r.v.
$f_{X}(t)=F'_{X}(t)=\begin{cases} -\frac{2}{t^3}&t<-1\\0&-1<t \end{cases}$
(i) $\mathbb{E}[X]=\int _{-\infty}^{\infty}tf_{X}(t) \, dt=\int _{-\infty}^{-1}t \left( \frac{-2}{t^3} \right) \, dt=\int _{-\infty}^{-1} -\frac{2}{t^2}\, dt= \frac{2}{t}\vert_{t=-\infty}^{-1} = \frac{2}{-1}-\frac{2}{-\infty}=-2-0=\boxed{-2}$
(ii) $\mathbb{E}[\sqrt[3]{ X }]=\int  \, dx$
(iii) 
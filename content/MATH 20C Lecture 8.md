---
tags:
- Type/Note
- Topic/Calculus
- Class/MATH_20C
date:
- 2024-01-26
---

> [!definition] Differentiable
> $\vec{r}(t)$ is **differentiable** at $t$ if  
> $$\lim_{ h \to 0 } \frac{\vec{r}(t+h)-\vec{r}(t)}{h}\text{ exists}$$  
> If $\vec{r}(t)$ is differentiable at $t$ we denote the above limit by  
> $\vec{r}'(t)\text{ or }\frac{d\vec{r}}{dt}\text{ or }\frac{d}{dt}\vec{r}(t)$  

> [!note] $\vec{r}'(t)=\langle x'(t),y'(t),z'(t) \rangle$
> In particular, $\vec{r}'(t)$ is differentiable iff all components are differentiable at $t$.  

> [!note] Higher derivatives
> $r''(t)=\frac{d}{dt}(\vec{r}'(t))$  
> $r'''(t)=\frac{d}{dt}(\vec{r}''(t))$  

# Differentiation Rules

Assume that $\vec{r}(t),\vec{r}_{1}(t),\vec{r}_{2}(t)$ are differentiable.

> [!note] $(\vec{r}_{1}(t)+\vec{r}_{2}(t))'=\vec{r}_{1}'(t)+\vec{r}_{2}'(t)$

> [!note] $(c\vec{r}_{1}(t))'=c\vec{r}_{1}'(t)$

> [!note] Product Rule
> Let $f(t)$ be a differentiable scalar-valued function  
> $\frac{d}{dt}(f(t)\vec{r}(t))=f'(t)\vec{r}(t)+f(t)\vec{r}'(t)$  

> [!note] Chain Rule
> Let $g(t)$ be a differentiable scalar-valued function  
> $\frac{d}{dt}(\vec{r}(g(t)))=\vec{r}'(g(t))g'(t)$  

# Product Rules for the Dot and Cross Products

> [!note] Dot Product Rule
> $\frac{d}{dt}(\vec{r}_{1}(t)\cdot \vec{r}_{2}(t))=\vec{r}_{1}'(t)\vec{r}_{2}(t)+\vec{r}_{1}(t)\vec{r}_{2}'(t)$  

> [!note] Cross Product Rule
> $\frac{d}{dt}(\vec{r}_{1}(t)\times \vec{r}_{2}(t))=\vec{r}_{1}'(t)\times \vec{r}_{2}(t)+\vec{r}_{1}(t)\times \vec{r}_{2}'(t)$  

# Geometry of the Derivatives

> [!note] $\vec{r}'(t_{0})$ is a tangent vector to the curve at $t=t_{0}$
> The tangent line at $\vec{r}(t_{0})$ is $L(s)=\vec{r}(t_{0})+s \vec{r}'(t_{0})$  

> [!definiton] Vector-Valued Integration
> $\int_{a}^b \vec{r}(t) \, dt=\langle \int_{a}^b x(t) \, dt,\int_{a}^b y(t) \, dt,\int_{a}^b z(t) \, dt \rangle$  

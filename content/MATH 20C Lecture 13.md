---
tags:
- Type/Note
- Topic/Calculus
- Class/MATH_20C
date:
- 2024-02-07
---
# 14.1  

Vertical trace: $(a,y,f(a,y))$  
Vertical trace: $(x,b,f(x,b))$  
Horizontal trace: $(x,y,f(x,y)=c$  
Level curve: $(x,y)\text{ }s.t.\text{ }f(x,y)=c$  

> [!definition] Contour map  
> A contour map is a plot in the domain in the xy-plane that the level curves $f(x,y)=c$ for **equally spaced** values of $c$  

> [!definition] Contour interval  
> The difference between two consecutive values of $c$.  

# 14.2 - Limit and Continuity  

## Limits  

$y=f(x)$  
$\lim_{ x \to a }f(x)=L\iff \text{As x approaches a from both sides, the values of f(x) approach L}$  

$\lim_{ (x,y) \to (a,b) }f(x,y)=L\iff \text{As (x,y) approaches (a,b) in any direction, the values of f(x,y) approach L}$  

> [!note] Limit Laws  
> $P=(a,b)$  
> Assume that $\lim_{ (x,y) \to P }f(x,y)$ and $\lim_{ (x,y) \to P }g(x,y)$ exist.  
> 1. $\lim_{ (x,y) \to P }f(x,y)+g(x,y)=\lim_{ (x,y) \to P }f(x,y)+\lim_{ (x,y) \to P }g(x,y)$  
> 2. $\lim_{ (x,y) \to P }kf(x,y)=k\lim_{ (x,y) \to P }f(x,y)$, k is a scalar  
> 3. $\lim_{ (x,y) \to P }f(x,y)g(x,y)=(\lim_{ (x,y) \to P }f(x,y))(\lim_{ (x,y) \to P }g(x,y))$  
> 4. If $\lim_{ (x,y) \to P }g(x,y)\neq 0$, then $\lim_{ (x,y) \to P }\frac{f(x,y)}{g(x,y)}=\frac{\lim_{ (x,y) \to P }f(x,y)}{\lim_{ (x,y) \to P }g(x,y)}$  

> [!note] Squeeze Theorem  
> If $f(x,y)\leq h(x,y)\leq g(x,y)$ and $\lim_{ (x,y) \to P }f(x,y)=\lim_{ (x,y) \to P }g(x,y)=L$ then $\lim_{ (x,y) \to P }h(x,y)=L$  

> [!definition] Continuity  
> A function $f(x,y)$ is continuous at $(a,b)$ if $\lim_{ (x,y) \to (a,b) }f(x,y)=f(a,b)$  
> We say $f$ is continuous if it is continuous at every point in the domain.  

> [!note] Remark: Elementary functions are continuous  
> polynomials: $x^2+xy+2y^2$  
> trig functions: $\sin(x+y)+\cos(xy)$  
> logarithm: $\ln(xy)-\ln(y)$  
> exponential: $e^x+e^{xy}$  

> [!note] Remark: All sums, scalar multiples, quotients, and products of continuous functions are still continuous  

> [!note] Remark: Compositions of continuous functions are continuous  

## How to find limits  

> [!note] If $f$ is continuous at $(a,b)$, then $\lim_{ (x,y) \to (a,b) }f(x,y)=f(a,b)$  

---
tags:
- Type/Note
- Topic/Probability
- Class/MATH_180A
date:
- 2024-05-01
---
**Example.** Taco Villa makes many tacos per day, and they almost always get each customer's taco order correct. On 75% of the days, they get every taco order correct, and on the other 25%, they get at least one taco order wrong. What is the probability that tomorrow, Taco Villa gets exactly 3 taco orders wrong?  

W = # of taco orders get wrong tomorrow.  
**Not** .25 chance they get each order wrong. We don't n or p, but we know n is large, p is small.  
$W\sim \text{Poisson}(\lambda)$  
$\mathbb{P}(W=0)=0.75$  
$-\lambda=\ln(.75)$  
$\lambda=-\ln(.75)=-\ln\left( \frac{3}{4} \right)=\ln\left( \frac{4}{3} \right)$  
$\mathbb{P}(W=3)=e^{-\ln(4/3)}\frac{\ln\left( \frac{4}{3} \right)^3}{3!}=e^{\ln(3/4)} \frac{\ln\left( \frac{4}{3} \right)^3}{6}$  
$=\frac{3}{4}\frac{\ln\left( \frac{4}{3} \right)^3}{6}=\frac{1\cdot \ln\left( \frac{4}{3} \right)^3}{8}$  

$\text{Unif}[a,b]$ Continuous random variable  
$\text{Ber}(p)$ Discrete  
$\text{Bin}(n,p)$  
$\text{Geom}(p)$  
$\text{Poisson}(\lambda)$  

## Section 3.3  

**Expectation**  
**Discrete Random Variables**  

Suppose that a discrete distribution on $\mathbb{R}$ has pmf $p$. Hang a weight of mass $p(a)$ at each point $a\in \mathbb{R}$. Where is the center of mass? In other words, where should fulcrum be placed to balance the weights? For example, take $p(-1)=\frac{7}{15},p(2)=\frac{1}{3},p(4)=\frac{1}{5}$  

$-1\cdot \frac{7}{15}+2\cdot \frac{1}{3}+4\cdot \frac{1}{5}=1$  
$=\text{center of mass}=\text{expectation}$  

> [!definition] Expectation/Mean/Average  
> Suppose $X$ is a discrete random variable w/ pmf $p_{X}$. Its **expectation/mean/average** is the real number  
> $$\mathbb{E}[X]=\sum_{a\in \mathbb{R}} a \mathbb{P}(X=a) = \sum_{a\in \mathbb{R}} a p_{X}(a)$$  

**Example.** Let $X$ be the outcome of a fair die roll. Calculate $\mathbb{E}[X]$.  

$[X]=\sum_{a\in \mathbb{R}}a \mathbb{P}(X=a)=1\cdot \frac{1}{6} + 2\cdot \frac{1}{6}+3\cdot \frac{1}{6}+4\cdot \frac{1}{6}+5\cdot \frac{1}{6}+6\cdot \frac{1}{6}$  
$=3.5$  
expectation doesn't have to be a possible value  

**Examples.**  

1. Suppose $W\sim \text{Ber}(p)$. Calculate $\mathbb{E}[W]$.  
$\mathbb{E}[W]=\sum_{a\in \mathbb{R}} a \mathbb{P}(W=a) = 0\cdot \mathbb{P}(W=0) + 1\cdot \mathbb{P}(W=1)=0(1-p)+1\cdot p=p$  
2. Suppose $X\sim \text{Bin}(n,p)$. Calculate $\mathbb{E}[X]$.  
$\mathbb{E}[X] = \sum_{a\in \mathbb{R}} a \mathbb{P}(X=a)= \sum_{k=0}^{n} k \begin{pmatrix}n\\k\end{pmatrix} p^{k} (1-p)^{n-k}$ to be continued...  
3. Suppose $Y\sim \text{Geom}(p)$. Calculate $\mathbb{E}[Y]$.  
$\mathbb{E}[Y] = \sum_{a\in \mathbb{R}} a \mathbb{P}(Y=a)=\sum_{k=1}^{\infty} K(1-p)^{K-1}p$  
---  
$1=\sum_{k=1}^{\infty}(1-p)^{k-1}p\implies \frac{1}{p}=\sum_{k=1}^{\infty} (1-p)^{k-1}$ take derivative wrt p  
$-\frac{1}{p^2}=\sum_{k=2}^{\infty}-(k-1)(1-p)^{k-2}$  
$j+1=k \sum_{j+1=2}^{\infty}-(j)(1-p)^{j-1}$  
$+\frac{1}{p^2}=\sum_{j=1}^{\infty}j(1-p)^{j-1}\implies \frac{1}{p}=\frac{p}{p^2}=\sum_{j=1}^{\infty}j(1-p)^{j-1}p=\mathbb{E}[Y]$  
4. Suppose $Z\sim \text{Poisson}(\lambda)$. Calculate $\mathbb{E}[Z]$.  
$\mathbb{E}[Z] = \sum_{a\in \mathbb{R}}a \mathbb{P}(Z=a)=\sum_{k=1}^{\infty}ke^{-\lambda} \frac{\lambda^k}{k!}=\sum_{k=1}^{\infty} \frac{e^{-\lambda}\lambda^k}{(k-1)!}$  
$=\lambda \sum_{k=1}^{\infty} \frac{e^{-\lambda}\lambda^{k-1}}{(k-1)!}$ reindex $j=k-1$  
$\lambda \sum_{j=0}^{\infty} \frac{e^{-\lambda}\lambda^j}{j!}=\lambda$  

> [!note] **Theorem:** Expectation is **linear**: If $X,Y$ are random variables defined on the same probability space and $c\in \mathbb{R}$, then  
> $\mathbb{E}[X+Y]=\mathbb{E}[X]+\mathbb{E}[Y]$ and $\mathbb{E}[cX]=c \mathbb{E}[X]$  


*Proof*.  

**Example.** We return to $X\sim \text{Bin}(n,p)$. Calculate $\mathbb{E}[X]$.  
$X=X_{1}+X_{2}+\dots+X_{n}$  
$X_{i}\sim \text{Ber}(p)$  
$\mathbb{E}[X]=\mathbb{E}[X_{1}]+\mathbb{E}[X_{2}] + \dots + \mathbb{E}[X_{n}]=p+p+\dots+p=np$  

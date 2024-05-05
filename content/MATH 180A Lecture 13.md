---
tags:
- "Type/Note"
- "Topic/Probability"
- "Class/MATH_180A"
date:
- 2024-05-03
---

> [!note] **Theorem**: Expectation is **linear**: If $X,Y$ are random variables defined on the same probability space and $c\in\mathbb{R}$, then
> $$\mathbb{E}[X+Y]=\mathbb{E}[X]+\mathbb{E}[Y]\text{ and }\mathbb{E}[cX]=c \mathbb{E}[X]$$

*Proof*.
$\mathbb{E}[X+Y]=\sum_{a\in \mathbb{R}}a \mathbb{P}(X+Y=a)=\sum_{a}a\sum_{b\in \mathbb{R}}\mathbb{P}(X+Y=a(Y=b)\mathbb{P}(Y=b))$
$= \sum_{a\in \mathbb{R}}\sum_{b\in \mathbb{R}}a \mathbb{P}(X=a-b\vert Y=b)\mathbb{P}(Y=b)$
$= \sum_{b\in \mathbb{R}}\sum_{a\in \mathbb{R}}a \mathbb{P}(X=a-b\vert Y=b)\mathbb{P}(Y=b)$
$= \sum_{b\in \mathbb{R}}\sum_{c\in \mathbb{R}-b}(c+b) \mathbb{P}(X=c\vert Y=b)\mathbb{P}(Y=b)$
$= \sum_{b\in \mathbb{R}}\sum_{c\in \mathbb{R}}(c+b) \mathbb{P}(X=c\vert Y=b)\mathbb{P}(Y=b)$
$=\sum_{c\in \mathbb{R}}c\sum_{b\in \mathbb{R}}\mathbb{P}(X=c(Y=b)\mathbb{P}(Y=b))+\sum_{b\in \mathbb{R}}\sum_{c\in \mathbb{R}}b \mathbb{P}(X=c\vert Y=b)\mathbb{P}(Y=b)$
$=\sum_{c\in \mathbb{R}}c \mathbb{P}(X=c)$
$=\sum_{c\in \mathbb{R}}c \mathbb{P}(X=c)+\sum_{b\in \mathbb{R}}b \sum_{c\in \mathbb{R}}\mathbb{P}(Y=b\vert X=c)\cdot \frac{\mathbb{P}(X=c)}{\mathbb{P}(Y=b)}\mathbb{P(Y=b)}$
$=\sum_{c\in \mathbb{R}}c \mathbb{P}(X=c)+\sum_{b\in \mathbb{R}}b \mathbb{P}(Y=b)=\mathbb{E}[X]+\mathbb{E}[Y]$

**Example.** We return to $X\sim \text{Bin}(n,p)$. Calculate $\mathbb{E}[X]$.
$X=X_{1}+X_{2}+\dots+X_{n}$
$X_{i}\sim \text{Ber}(p)$
$\mathbb{E}[X]=\mathbb{E}[X_{1}]+\mathbb{E}[X_{2}]+\dots+\mathbb{E}[X_{n}]=p+p+\dots+p=np$

## Functions of Discrete Random Variables

A biased coin lands heads 2/3 of the time. I flip it repeatedly until it lands heads. You win $\$2^k$ if it lands heads for the first time on the *k*th flip. How many dollars are you expected to win?

W = # of dollars we win
$\mathbb{E}[W]=\sum_{a\in \mathbb{R}}a \mathbb{P}(W=a)$
$=\sum_{K=1}^{\infty} 2^{K} \left( \frac{1}{3} \right)^{K-1} \cdot \frac{2}{3}$
$=\frac{2}{3}\cdot 2 \sum_{K=1}^{\infty} 2^{K-1} \left( \frac{1}{3} \right)^{K-1}$
$=\frac{4}{3} \sum_{K=1}^{\infty} \left( \frac{2}{3} \right)^{K-1} = \frac{4}{3} \sum_{j=0}^{\infty} \left( \frac{2}{3} \right)^{j}$
$j+1=K$
$=\frac{4}{3}\left( \frac{1}{1-\frac{2}{3}} \right)=\boxed{4}$

$\mathbb{P}(W=2)=\frac{2}{3}$
$\mathbb{P}(W=4)=\frac{1}{3}\cdot \frac{2}{3}$
$\mathbb{P}(W=8)=\left( \frac{1}{3} \right)^{2} \cdot \frac{2}{3}$
$\vdots$
$\mathbb{P}(W=2^{K}) = \left( \frac{1}{3} \right)^{K-1} \cdot \frac{2}{3}$

$W=2^N$ where N = # of coin flips
Thus, $W=g(N)$ where $N\sim \text{Geom}\left( \frac{2}{3} \right)$ $g(K)=2^K$
$\mathbb{E}[W]=\sum_{a\in \mathbb{R}}g(a) \mathbb{P}(N=a)$

---

By definition, if $X:\Omega\to \mathbb{R}$ is a discrete random variable and $g:\mathbb{R}\to \mathbb{R}$ is a function, then $g(X):\Omega\to \mathbb{R}\to \mathbb{R}$ is also a discrete random variable and $\mathbb{E}[g(X)]=\sum_{a\in \mathbb{R}}a \mathbb{P}(g(X)=a)$

> [!note] **Theorem**: If $X$ is a discrete random variable and $g$ is a function, then 
> $$\mathbb{E}[g(X)]=\sum_{a\in \mathbb{R}}g(a)\mathbb{P}(X=a)=\sum_{a\in \mathbb{R}}g(a)p_{X}(a)$$

**Example.** A biased coin lands heads 75% of the time. You flip it 4 times. If it lands heads an even number of times, I win $1. If it lands heads an odd number of times, I lose $2. How many dollars am I expected to win?

W = # of dollars I win.
$W=g(X)$ where X = # of heads,
$g(0)=1,g(1)=-2$
$g(2)=1, g(3)=-2$
$g(4)=1$
$\mathbb{E}[W]=\sum_{a\in \mathbb{R}}g(a)\mathbb{P}(X=a)$
$=g(0)\mathbb{P}(X=0)+g(1)\mathbb{P}(X=1)+g(2)\mathbb{P}(X=2)+g(3)\mathbb{P}(X=3)+g(4)\mathbb{P}(X=4)$
$=1\cdot\left( \frac{1}{4} \right)^{4}\left( \frac{3}{4} \right)^{0}\begin{pmatrix}4\\0\end{pmatrix} + (-2)\left( \frac{1}{4} \right)^{3}\left( \frac{3}{4} \right)^{1}\begin{pmatrix}4\\1\end{pmatrix}+1\cdot \left( \frac{1}{4} \right)^{2}\left( \frac{3}{4} \right)^{2}\begin{pmatrix}4\\2\end{pmatrix}+(-2)\left( \frac{1}{4} \right)^{1}\left( \frac{3}{4} \right)^{3}\begin{pmatrix}4\\3\end{pmatrix}+1\cdot \left( \frac{1}{4} \right)^{0}\left( \frac{3}{4} \right)^{4}\begin{pmatrix}4\\4\end{pmatrix}$
$=-0.40625$

## Continuous Random Variables

Expectation of discrete r.v. $X:\mathbb{E}[X]=\sum_{a\in \mathbb{R}}ap_{X}(a)$.

> [!definition] Expectation
> Let $X$ be a continuous random variable, then its expectation is defined by 
> $$\mathbb{E}[X]=\int_{\infty}^{\infty}af_{X}(a) \, da = \int_{-\infty}^{\infty} tf_{X}(t) \, dt $$
> $f_{X}$ is the pdf

**Examples.**
1. Let $U\sim \text{Unif}[a,b]$. Calculate $\mathbb{E}[U]$.
$\mathbb{E}[U]=\int_{-\infty}^{\infty}tf_{u}(t) \, dt$
$=\int _{a}^{b} t \frac{1}{b-a}\, dt=\frac{1}{b-a}\int _{a}^{b}t \, dt=\frac{1}{b-a}\left( \frac{b^{2}}{2}-\frac{a^{2}}{2} \right)$
$=\frac{1}{2}\left( \frac{b^{2}-a^{2}}{b-a} \right)=\frac{1}{2}\left( \frac{(b-a)(b+a)}{b-a} \right)=\frac{a+b}{2}$
2. A dart hits a circular board of radius 1 uniformly at random. What is the expected distance from the point it hits to the center of the board?
$X=$ distance to center
$\mathbb{E}[X]=\int _{-\infty}^{\infty}tf_{X}(t) \, dt$
$f_{X}(t)=F'_{X}(t)$
$F_{X}(t)=\mathbb{P}(X\leq t)$
$F_{X}(t)=\begin{cases}0&t<0\\t^{2}&0\leq  t\leq 1\\1&1\leq t\end{cases}$
$f_{X}'(t)=\begin{cases}0&t<0\\2t&0<t<1\\0&1<t\end{cases}$
$=\int _{0}^{1}t\cdot 2t \, dt=\int _{0}^{1}2t^{2} \, dt$
$\frac{2t^3}{3}\vert_{0}^{1}=\frac{2}{3}$
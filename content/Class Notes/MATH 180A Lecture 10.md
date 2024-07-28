---
tags:
- "Type/Note"
- "Topic/Probability"
- "Class/MATH_180A"
date:
- 2024-04-26
---
# Section 2.4  

## Independent Random Variables  

> [!definition] Mutually Independent  
> A finite or infinite sequence of random variables $X_{1},X_{2},\dots$ defined on the same probability space are **mutually independent** if for every choice of subsets $B_{1},B_{2},\dots,B_{n}\subseteq \mathbb{R}$, the events $\{X_{1}\in B_{1}\}, \{X_{2}\in B_{2}\},\dots\{X_{n}\in B_{n}\}$ are mutually independent events.  
> i.e. $\mathbb{P}(X_{1}\in A_{1},X_{2}\in A_{2}, \dots , X_{n}\in A_{n}) = \mathbb{P}(X_{1}\in A_{1})\cdot\mathbb{P}(X_{2}\in A_2)\dots\mathbb{P}(X_{n}\in A_{n})$  

**Example.** A fair coin is tossed twice. Let $X_{1}$ be the total number of heads on the 1st toss and $S$ the total number of heads among both tosses. Show that $X_{1},S$ are not mutually independent random variables.  

$\mathbb{P}(X_{1}=1,S=0)=0$  
$\mathbb{P}(X_{1}=1)\cdot \mathbb{P}(S=0)=\frac{1}{2}\cdot \frac{1}{4} = \frac{1}{8}$  
$\mathbb{P}(X_{1}=1,S=0)\neq \mathbb{P}(X_{1}=1)\cdot \mathbb{P}(S=0)$  
So $X_{1},S$ are not independent  

## Bernoulli Random Variables  

Suppose we perform an experiment and designate certain outcomes as "successes" and the rest as "failures." Then we can define a random variable $X:\Omega\to \mathbb{R}$ by  
$$X(\omega)=\begin{cases}1 & \omega \text{ is a success} \\0 & \omega \text{ is a failure}\end{cases}$$  

**Examples.**  
1. $\Omega=\{H,T\},H$ is a success. Then $X(T)=0,X(H)=1$  
2. $\Omega=\{1,2,3,4,5,6\},\leq 4$ is a success. Then $X(1)=X(2)=X(3)=X(4)=1,X(5)=X(6)=0$  

Suppose $\mathbb{P}(\{\text{successful outcomes}\})=p$. Then $X$ is a discrete random variable with pmf given by  
$$p_{X}(0)=\mathbb{P}(X=0)=1-p$$  
$$p_{X}(1)=\mathbb{P}(X=1)=p$$  
In this case we call $X$ a **Bernoulli random variable** with success probability $p$ and write $X\sim \text{Ber}(p)$. Its distribution $\mathbb{P}_{X}$ is called the **Bernoulli distribution**.  

**Examples.**  
1. Flip a fair coin, $H$ is a success. Then $X\sim \text{Ber}\left( \frac{1}{2} \right)$  
2. Roll a fair die, $\leq 4$ is a success. Then $X\sim \text{Ber}\left( \frac{4}{6} \right)=X\sim \text{Ber}\left( \frac{2}{3} \right)$  

## Binomial Random Variables  

Suppose we perform 4 independent trials each w/ success probability $p$. Let $X_{i}=1$ if the *i*th trial is a success and $X_{i}=0$ if the *i*th trial is a failure. Then $X_{1},X_{2},X_{3},X_{4}$ are mutually independent $\text{Ber}(p)$ random variables.  
- Calculate $\mathbb{P}(X_{1}=1,X_{2}=1,X_{3}=0,X_{4}=1)$  
$=\mathbb{P}(X_{1}=1)\mathbb{P}(X_{2}=1)\mathbb{P}(X_{3}=0)\mathbb{P}(X_{4}=1)$ b/c $X_{i}$'s are independent  
$=p\cdot p\cdot(1-p)\cdot p=p^3(1-p)^1$  
- Calculate $\mathbb{P}(X_{1}=0,X_{2}=1,X_{3}=1,X_{4}=0)$  
$=p^2(1-p)^2$  

Let $S_{4}=\text{total number of successes}=X_{1}+X_{2}+X_{3}+X_{4}$  
$S_{4}$ is a discrete random variable. What is its pmf?  

$p_{S_{4}}(0)=\mathbb{P}(S_{4}=0)=\mathbb{P}(X_{1}=0,X_{2}=0,X_{3}=0,X_{4}=0)=p^0(1-p)^4$  
$p_{S_{4}}(1)=\mathbb{P}(S_{4}=1)=\mathbb{P}(X_{1}=1,X_{2}=0,X_{3}=0,X_{4}=0)+\mathbb{P}(X_{1}=0,X_{2}=1,X_{3}=0,X_{4}=0)+\mathbb{P}(X_{1}=0,X_{2}=0,X_{3}=1,X_{4}=0)+\mathbb{P}(X_{1}=0,X_{2}=0,X_{3}=0,X_{4}=1)$  
$=4p^1(1-p)^3$  
$p_{S_{4}}(2)=\mathbb{P}(S_{4}=2)=$ 6 terms $\mathbb{P}(X_{1}=1,X_{2}=1,X_{3}=0,X_{4}=0)+\mathbb{P}(X_{1}=1,X_{2}=0,X_{3}=1,X_{4}=0)$  
$=6p^2(1-p)^2=\begin{pmatrix}4\\2\end{pmatrix}p^2(1-p)^2$  
$p_{S_{4}}(3)=\mathbb{P}(S_{4}=3)=\begin{pmatrix}4\\3\end{pmatrix}p^3(1-p)^1=4p^3(1-p)^1$  
$p_{S_{4}}(4)=\mathbb{P}(S_{4}=4)=\begin{pmatrix}4\\4\end{pmatrix}p^4(1-p)^0=p^4$  

In general, we say that $S$ is a **binomial random variable** w/ parameteres $n,p$ for all $k\in\{0,1,\dots,n\},\mathbb{P}(S=k)=\begin{pmatrix}n\\k\end{pmatrix}p^k(1-p)^{n-k}$ and we write $S\sim \text{Bin}(n,p)$. Its distribution $\mathbb{P}_{S}$ is called the **binomial distribution**.  

**Takeaway**: A $\text{Bin}(n,p)$ random variable counting the total # of successes of $n$ independent trials each having success probability $p$.  

> [!question] **Example.** A fair die is rolled 10 times. What is the probability that a six is rolled at least 3 times?  
> $S=$ total number of 6's. $S\sim \text{Bin}\left( 10, \frac{1}{6} \right)$  
> $\mathbb{P}(S\geq 3)=\displaystyle\sum_{a=3}p_{S}(a)=\displaystyle\sum_{k=3}^{10}p_{S}(k)=\displaystyle\sum_{k=3}^{10}\begin{pmatrix}10\\k\end{pmatrix} \left( \frac{1}{6} \right)^{k} \left( \frac{5}{6} \right)^{10-k}$  
> $=1-\mathbb{P}(S<3)=1-\displaystyle\sum_{k=0}^2\begin{pmatrix}10\\k\end{pmatrix} \left( \frac{1}{6} \right)^{k} \left( \frac{5}{6} \right)^{10-k}$  
> $=\boxed{1-\left(  \left( \frac{5}{6} \right)^{10} + 10 \left( \frac{1}{6} \right) \left( \frac{5}{9} \right)^{9} + 45 \left( \frac{1}{6} \right)^{2} \left( \frac{5}{6} \right)^8 \right)}$  

## Geometric Random Variables  

$$X_{i}(j)=\begin{cases}0 & j \neq 6 \\ 1 & j = 6\end{cases}$$  
I roll a fair die repeatedly. What is the probability that a six is rolled  
for the first time on the 2nd roll? $\mathbb{P}(X_{1}=0,X_{2}=1)=\frac{5}{6}\cdot \frac{1}{6}$  
for the first time on the 3rd roll? $\left( \frac{5}{6} \right)^{2} \cdot \frac{1}{6}$  
for the first time on the *n*th roll? $\left( \frac{5}{6} \right)^{n-1}\cdot \frac{1}{6}$  

In general, we say that *N* is a **geometric random variable** w/ success parameter $p$ for all $k\in\{1,2,3,\dots\},\mathbb{P}(N=k)=(1-p)^{k-1}p$ and we write $N\sim \text{Geom}(p)$. Its distribution $\mathbb{P}_{N}$ is called the **geometric distribution**.  

**Takeaway:** A $\text{Geom}(p)$ random variable counts the number of trials until first success, (if each trial has success probability $p$)  
We expect that $p_{N}(k)=(1-p)^{k-1}p$ defines a pmf. Let's check that its sum is 1:  

$$\sum_{k=1}^{\infty} (1-p)^{k-1}p = p \sum_{k=1}^{\infty} (1-p)^{k-1}$$  
Let $k=j+1\implies k-1=j$  
$$=p \sum_{j+1=y}^{\infty} (1-p)^{j}$$  
$$=p \frac{1}{1-(1-p)}$$  
$$=p \frac{1}{p}=\boxed{1}$$  

How we could simplify the sum: Series magic  
$0<r<1$  
$$S_{n}=\sum_{k=0}^{n}=1+r+r^2+\dots+r^n$$  
$$rS_{n}=r+r^2+r^3+\dots+r^{n+1}$$  
$$rS_{n}-S_{n}=r^{n+1}-1$$  
$$S_{n}(r-1)=r^{n+1}-1$$  
$$S_{n}=\frac{r^{n+1}-1}{r-1}=\boxed{\frac{1-r^{n+1}}{1-r}}$$  
$$\sum_{k=0}^{\infty}=\lim_{ n \to \infty } \frac{1-r^{n+1}}{1-r}=\frac{1}{1-r}$$  

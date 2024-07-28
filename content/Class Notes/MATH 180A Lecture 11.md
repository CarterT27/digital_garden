---
tags:
- "Type/Note"
- "Topic/Probability"
- "Class/MATH_180A"
date:
- 2024-04-29
---
**Example.** A weighted coin lands heads 60% of the time. I flip the coin repeatedly. What is the probability that it lands tails 5 or fewer times before it lands heads?  

N = # of flips until 1st heads. $N\sim \text{Geom}(0,6)$  
$\mathbb{P}(N\leq 6)=\displaystyle\sum_{a\leq 6}p_{N}(a)=\displaystyle\sum_{k=1}^{6} (1-0.6)^{k-1} (0.6)$  
$=\displaystyle \sum_{k=1}^{6}(0.4)^{k-1}(0.6)=(0.6) \sum_{k=1}^{k=6} (0.4)^{k-1}$  
reindex $k=j+1$  
$=(0.6) \sum_{j+1=1}^{j+1=6} (0.4)^{j+1-1}$  
$=(0.6) \sum_{j=0}^{5} (0.4)^j$  
$=0.6 \frac{1-(0.4)^6}{1-(0.4)}$  
$=\boxed{1-(0.4)^6}$  

---  

$\mathbb{P}(N\leq 6) = 1 - \mathbb{P}(N>6) = 1 - \sum_{k=7}^{\infty} (1-0.6)^{k-1} (0.6)$  
$=1-0.6((0.4)^6+(0.4)^7+(0.4)^8+\dots)$  
$=1-(0.6)(0.4)^6(1+(0.4)+(0.4)^2+\dots)$  
$=1-0.6(0.4)^{6} \frac{1}{1-0.4} = 1 - (0.4)^6$  
$N\sim \text{Geom}(p)$  
$\mathbb{P}(N>k)=(1-p)^k$  

# Section 4.4  

## Rare Events & the Poisson Distribution  

A factory produces 10 ipads per day. On average, 3 of the ipads they produce are defective and are not distributed for sale. Assuming that the probabilities of the ipads being defective are mutually independent, what is the probability that exactly 2 ipads produced are defective in a day?  

$X$ = # of defective ipads in a given day.  
$X\sim \text{Bin}(10,p)=X\sim \text{Bin}\left( 10, \frac{3}{10} \right)$  
$\mathbb{P}(X=2)=\left( \frac{3}{10} \right)^2\left( \frac{7}{10} \right)^8\begin{pmatrix}10\\2\end{pmatrix}\approx 0.233$  

The factory boosts production to 100 ipads per day while maintaining an average of 3 defective ipads per day. Now what is the probability that exactly 2 ipads produced are defective in a day?  

$X$ = # of defective ipads in a given day  
$X\sim \text{Bin}\left( 100, \frac{3}{100} \right)$  
$\mathbb{P}(X=2)=\left( \frac{3}{100} \right)^2\left( \frac{97}{100} \right)^{98}\begin{pmatrix}100\\2\end{pmatrix}\approx 0.225$  

The probabilities in the previous example are converging to something... Suppose $S_{n}\sim \text{Bin}(n,p)$ where $p=\frac{\lambda}{n}$. Then for each $k$, $\lim_{ n \to \infty }\mathbb{P}(S_{n}=k)=$  
$\lim_{ n \to \infty }\left( \frac{\lambda}{n} \right)^k\left( 1-\frac{\lambda}{n} \right)^{n-k}\begin{pmatrix}n\\k\end{pmatrix}$  
$=\lim_{ n \to \infty }\left( \frac{\lambda}{n} \right)^k\left( 1-\frac{\lambda}{n} \right)^{n-k}\frac{n\cdot(n-1)\cdot(n-2)\dots(n-k+1)}{k!}$  
$=\lim_{ n \to \infty }\lambda^{k}\left( 1-\frac{\lambda}{n} \right)^{n-k}\frac{\left( \frac{n}{n} \right)\left( \frac{n-1}{n} \right)\left( \frac{n-2}{n} \right)\dots\left( \frac{n-k+1}{n} \right)}{k!}$  
$=\lim_{ n \to \infty }\lambda^{k}\left( 1-\frac{\lambda}{n} \right)^{n-k}\frac{1\cdot_{1}\cdot_{1}\dots_{1}}{k!}$  
$=\lim_{ n \to \infty }\frac{\lambda^k}{k!}\left( 1-\frac{\lambda}{n} \right)^{n}\left( 1-\frac{\lambda}{n} \right)^-k$  
$=\lim_{ n \to \infty }\frac{\lambda^{k}}{k!}\left( 1-\frac{\lambda}{n} \right)^n\cdot 1$  
$=\frac{\lambda^k}{k!}e^{-\lambda}$  

$\left( 1+\frac{r}{n} \right)^n$ interest rate $r$ compounding $n$ times per year, gain rate after $1$ year. Take $n to \infty$ get continuous interest $e^r$  

In general, we say that $S$ is a **Poisson random variable** w/ parameters $\lambda$ if for all $k\in\{0,1,\dots\}, \mathbb{P}(S=k)=e^{-\lambda}\frac{\lambda^k}{k!}$ and we write $S\sim \text{Poisson}(\lambda)$. Its distribution $\mathbb{P}_S$ is called the **Poisson distribution**.  

**Takeaway**: A $\text{Poisson}(\lambda)$ random variable counts total number of successes of "many" trials, where probability of success in each trial is very small. In other words, $S$ counts the number of occurrences of a "rare event".  

Let's check that $p_{S}(k)=e^{-\lambda}\frac{\lambda^k}{k!}$ is a pmf:  
$\displaystyle\sum_{k=0}^{\infty}e^{-\lambda}\frac{\lambda^k}{k!}=e^{-\lambda}\displaystyle\sum_{k=0}^{\infty}\frac{\lambda^k}{k!}=e^{-\lambda}\cdot e^{\lambda}=\boxed{1}$  
Taylor series for $e^\lambda$ centered at $a=0$.  

**Example.** Suppose $X\sim \text{Bin}(986,0.001)$. Approximate $\mathbb{P}(X=3)$.  

$p=\frac{\lambda}{n}$  
$\lambda=np$  
$\lambda=986\cdot(0.001)=0.986$  
$X$ well approximated by $Y\sim \text{Poisson}(.986)$  
$\mathbb{P}(X=3)\approx \mathbb{P}(Y=3)=e^{-0.986}\frac{(0.986)^3}{3!}$  

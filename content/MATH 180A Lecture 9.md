---
tags:
- "Type/Note"
- "Topic/Probability"
- "Class/MATH_180A"
date:
- 2024-04-19
---
## Discrete & Continuous Random Variables, Probability Mass & Density Functions  

There are two important types of probability measure $\mathbb{R}$ that we will focus on.  

> [!definition] Discrete, Probability Mass Function (pmf)  
> A probability measure $\mathbb{P}$ on $\mathbb{R}$ is **discrete** if there exists a finite or infinite sequence of numbers $a_1,a_2,\dots \in \mathbb{R}$ such that  
> $$\sum_{i=1}^\infty \mathbb{P}(\{a_i\}) = 1, \text{ equivalently, } \mathbb{P}(\mathbb{R} \setminus \{a_1,a_2,\dots\}) = 0$$  
> A random variable $X$ is **discrete** if its distribution $\mathbb{P}_X$ is discrete.  
> In this case, we call the function $\mathbb{P}_X:\mathbb{R} \to \mathbb{R}$ defined by $\mathbb{P}_X(a) := \mathbb{P}(X=a)$ the **probability mass function of $X$ (pmf)**  

Crucial fact: pmf completely determines the distribution of a discrete random variable. Because $$\mathbb{P}_X(A) = \mathbb{P}(X \in A) = \sum_{a \in A} \mathbb{P}(X=a) = \sum_{a \in A} p_X(a)$$.  

> [!definition] Continuous, Probability Density Function (pdf)  
> A probability measure $\mathbb{P}$ on $\mathbb{R}$ is **continuous** if there exists an **integrable** function $f:\mathbb{R} \to \mathbb{R}$ s.t.  
> $$\mathbb{P}(A) = \int_A f(x)\,dx$$  
> A random variable $X$ is **continuous** if its distribution $\mathbb{P}_X$ is continuous.  
> In this case, we call $f_x$ the **probability density function (pdf)** of $X$.  

> [!note]  
> $$\int_{[-2,0]\cup [\pi,6]} f(x)\,dx$$  
> $$\int_{[a,b]} f(x)\,dx = \int_a^b f(x)\,dx = \int_{-2}^0 f(x)\,dx + \int_\pi^6 f(x)\,dx$$  
>  
> $$\mathbb{P}(X\in A) = \int_A f_x(t)\,dt$$  
> $$\mathbb{P}(2\leq X<3) = \int_2^3 f_x(t)\,dt$$  

Crucial fact: pdf completely determines the distribution of continuous random variables.  

**Examples.**  

> [!question] A fair coin is tossed 3 times. Let $X$ = "number of heads". $X$ is a discrete random variable. Find its pmf.  
> $\mathbb{P}_X(a) = \mathbb{P}(X=a)$  
> $\mathbb{P}_X(0) = \frac{1}{8} = \mathbb{P}(X=0)$  
> $\mathbb{P}_X(1) = \frac{3}{8} = \mathbb{P}(X=1)$  
> $\mathbb{P}_X(2) = \frac{3}{8} = \mathbb{P}(X=2)$  
> $\mathbb{P}_X(3) = \frac{1}{8} = \mathbb{P}(X=3)$  
> $\mathbb{P}_X(a) = 0$ for all other values of $a$  

> [!question] A point is chosen uniformly at random from the unit disk. Let $X$ = "distance of the point from the cetner". $X$ is a continuous random variable. Find its pdf.  
> $$\mathbb{P}(X \in A) = \int_A f_X(t)\,dt \leftrightarrow \mathbb{P}(X\leq s) = F_X(s) = \int_{-\infty}^s f_X(t)\,dt$$  
> take the derivative of each side  
> $F_X'(s) = f_x(s)$ Fundamental theorem of calculus  
> $$\frac{d}{ds} \begin{cases} 0 & s<0 \\ s^2 & 0\leq s \leq 1 \\ 1 & 1<s\end{cases} = \begin{cases} 0 & s<0 \\ 2s & 0<s<1 \\ 0 & 1<s \end{cases} = f_X(s)$$  

> [!definition] Uniform  
> We say that a random variable $X$ is **uniform on [a,b]** if $X$ is continuous and its pdf is given by  
> $$f_X(t) = \begin{cases} \frac{1}{b-a} & t\in[a,b] \\ 0 & t\notin[a,b]\end{cases}$$  
> In this case we write $X \sim \text{Unif}[a,b]$.  

**Example.** Suppose $X \sim \text{Unif}[a,b]$. Calculate $\mathbb{P}(c\leq X\leq d)$.  
$$\mathbb{P}(c \leq X \leq d) = \int_c^d f_X(t)\,dt = \begin{cases} 0 & d\leq a \\ 0 & c \geq b \\ \int_a^d \frac{1}{b-a}\,dt = \frac{d-a}{b-a} & c\leq a\leq d \leq b\end{cases}$$  
In general, $\mathbb{P}(c\leq X\leq a) = \frac{\text{length}([c,d]\cap[a,b])}{\text{length}([a,b])}$  

## Going from pmf/pdf to cdf  

The formulas to go from the pmf/pdf of a discrete/continuous random variable to its cdf are straightforward:  
- If $X$ is discrete, $F_X(t) = \mathbb{P}(X\leq t) = \sum_{a\leq t} p_X(a)$.  
- If $X$ is continuous, $F_X(t) = \mathbb{P}(X\leq t) = \int_{-\infty}^t f_X(s)\,ds$.  

**Examples.**  

> [!question] Suppose $X$ is discrete w/ pmf $p_X(-\pi) = \frac{1}{3},p_X(\sqrt{2}) = \frac{2}{3}$. Find its cdf.  
> $F_X(t) = \begin{cases} 0 & t<-\pi \\ \frac{1}{3} & -\pi \leq t < \sqrt{2} \\ 1 & \sqrt{2} \leq t \end{cases}$  

> [!question] Suppose $X \sim \text{Unif}[-1,2]$. Find its cdf.  
> $F_X(t) = \int_{-\infty}^t f_X(s)\,ds = \begin{cases} 0 & t<-1 \\ \int_{-1}^t \frac{1}{3}\,ds & -1\leq t\leq 2 \\ \int_{-1}^2 \frac{1}{3}\,ds & 2<t\end{cases} = \begin{cases} 0 & t<-1 \\ \frac{t+1}{3} & -1\leq t \leq 2 \\ 1 & 2<t\end{cases}$  

## Going from cdf to pmf/pdf  

The formulas to go from the cdf to the pmf/pdf of a discrete/continuous random variable are slightly more involved.  

**Fact:** Let $X$ be a random variable and $F_X$ its cdf.  
- If $F_X$ is **piecewise constant**, then $X$ is **discrete** and its pmf is found by claculating the magnitude of the jumps at the points on discontinuity.  
- If $F_X$ is **continuous and piecewise continuously differentiable**, then $X$ is **continuous** and its pdf is given by $f_X(t)=F_X'(t)$.  

**Examples.**  

> [!question] Suppose $X$ has cdf given by $F_X(s) = \begin{cases} 0 & s<-\pi \\ \frac{1}{3} & -\pi \leq s < \sqrt{2} \\ 1 & \sqrt{2} \leq s \end{cases}$. Is $X$ discrete or continuous? If so, find its pmf/pdf.  
> $\mathbb{P}_X(-\pi) = \frac{1}{3}-0 = \frac{1}{3}$  
> $\mathbb{P}_X(\sqrt{2}) = 1 - \frac{1}{3} = \frac{2}{3}$  

> [!question] Suppose $X$ has cdf given by $F_X(s) = \begin{cases} 0 & s<0 \\ \sin{s} & 0 \leq s < \frac{\pi}{2} \\ 1 & \frac{\pi}{2}\leq s \end{cases}$. Is $X$ discrete or continuous? If so, find its pmf/pdf.  
> $F_X$ is continuous + continuously piecewise differentiable $\implies$ $X$ is continuous and  
> $$f_X(s) = \begin{cases} 0 & s<0 \\ \cos{s} & 0 \leq s < \frac{\pi}{2} \\ 0 & \frac{\pi}{2}<s \end{cases}$$  

## Defining Properties of pdf's, pmf's, pdf's  

> [!note] Fact  
> A function $F:\mathbb{R}\to\mathbb{R}$ is the cdf of a random variable if and only if  
> 1. $\lim\limits_{t\to\infty} F(t) = 1$ and $\lim\limits_{t\to-\infty} F(t) = 0$  
> 2. Nondecreasing meaning $t\geq s \implies F(t) \geq F(s)$  
> 3. Right-continuous $\lim\limits_{t\to a^+} F(t) = F(a)$ comes from $F_X(t) = \mathbb{P}(X\leq t)$ right-continuous, $\mathbb{P}(X < t)$ left -continuous  

> [!note] Fact  
> A function $p: \mathbb{R}\to\mathbb{R}$ is the pmf of a discrete random variable if and only if there exists a finite or infinite sequence of numbers $a_1,a_2,\dots\in \mathbb{R}$ such that  
> 1. $0\leq p(a)\leq 1$ for all $a\in \mathbb{R}$  
> 2. \sum_{i=1}^\infty p(a_i) = 1$  
> 3. $p(b)=0$, $b\notin\{a_1,a_2,\dots\}$  

> [!note] Fact  
> A function $f:\mathbb{R}\to\mathbb{R}$ is the pdf of a continuous random variable if and only if $f$ is integrable and  
> 1. $f(t)\geq 0$  
> 2. $\int_{-\infty}^\infty f(t)\,dt = 1$  
>  
> $0\leq \mathbb{P}(a\leq X\leq b) \leq 1$  
> $\mathbb{P}(a\leq X\leq b) = \int_a^b f_X(t)\,dt$  

---
tags:
- "Type/Note"
- "Topic/Probability"
- "Class/MATH_180A"
date:
- 2024-04-17
---
## Distributions  

> [!definition] Probability Distribution  
> Let ($\Omega,\mathcal{F},\mathbb{P}$) be a probability space and $X:\Omega\to \mathbb{R}$ a random variable. The (**probability**) **distribution** of $X$ is the probability measure on $\mathbb{R}$ defined by $\mathbb{P}_X(A):=\mathbb{P}(X\in A)\forall A\subseteq \mathbb{R}$  
> $\iff \mathbb{P}(\{\omega \in \Omega:X(\omega) \in A\})$  
> $\mathbb{R}$ is the sample space  

**Examples.**  

> [!question] Fair coin toss: $\Omega=\{H,T\}$. Define $X:\Omega\to \mathbb{R}$ by $X(H)=\pi, X(T)=-\sqrt{2}$. What is the distribution of $X$?  
> $\mathbb{P}_X(A) = \mathbb{P}(X \in A) = \mathbb{P}(\{\omega \in \Omega : X(\omega) \in A \})$  
> $\mathbb{P}_X([0,\infty)) = \mathbb{P}(X \in [0,\infty)) = \mathbb{P}(\{\omega \in \{H,T\} : X(\omega) \in [0,\infty) \})=\mathbb{P}(\{H\})=\frac{1}{2}$  
> $\mathbb{P}_X((-1,2]) = \mathbb{P}(\emptyset)=0$  
> $\mathbb{P}_X((-\infty,0]) = \mathbb{P}(\{T\})=\frac{1}{2}$  
> $\mathbb{P}_X((-10,10)) = \mathbb{P}(\{H,T\})=1$  
>  
> $\mathbb{P}_X(A) = \begin{cases} 0 & \pi,-\sqrt{2}\notin A \\ \frac{1}{2} & \pi \in A \text{ or } - \sqrt{2} \in A \text{ but not both} \\ 1 & \pi,-\sqrt{2}\in A\end{cases}$  

> [!question] Roll a fair die twice: $\Omega = \{1, 2, 3, 4, 5, 6\}^2$. Define $S: \Omega \to \mathbb{R}$ by $S((i,j)) = i + j$. What is the distribution of $S$?  
> $\mathbb{P}_S(\{2\}) = \mathbb{P}(S=2) = \mathbb{P}(\{(1, 1)\}) = \frac{1}{36}$  
> $\mathbb{P}_S(\{3\}) = \mathbb{P}(S=3) = \mathbb{P}(\{(1, 2), (2, 1)\}) = \frac{2}{36}$  
> $\mathbb{P}_S(\{4\}) = \mathbb{P}(S=4) = \mathbb{P}(\{(1, 3), (2, 2), (3, 1)\}) = \frac{3}{36}$  
> $\mathbb{P}_S(\{5\}) = \frac{4}{36}$  
> $\mathbb{P}_S(\{6\}) = \frac{5}{36}$  
> $\mathbb{P}_S(\{7\}) = \frac{6}{36}$  
> $\mathbb{P}_S(\{8\}) = \frac{5}{36}$  
> $\mathbb{P}_S(\{9\}) = \frac{4}{36}$  
> $\mathbb{P}_S(\{10\}) = \frac{3}{36}$  
> $\mathbb{P}_S(\{11\}) = \frac{2}{36}$  
> $\mathbb{P}_S(\{12\}) = \frac{1}{36}$  
> $\mathbb{P}_S(A) = \sum_{a \in A} \mathbb{P}_S(\{a\})$  
> e.g. $\mathbb{P}_S([10, 20]) = \sum_{a \in [10,20]} \mathbb{P}_S\{A\}$  
> $=\mathbb{P}_S(10) + \mathbb{P}_S(11) + \mathbb{P}_S(12) = \frac{3 + 2 + 1}{36} = \frac{1}{6}$  

> [!question] Choose a point uniformly at random on a random disk: $\Omega = \{(x, y) \in \mathbb{R}^2: x^2 + y^2 \leq 1\}$. Define $X: \Omega \to \mathbb{R}$ by $X((x,y)) = \sqrt{x^2 + y^2}$. What is the distribution of $X$?  
> $\mathbb{P}_X(A) = \mathbb{P}(X \in A) = \mathbb{P}(\{(x, y) \in \Omega: \sqrt{x^2+y^2} \in A\})$  
> $\mathbb{P}_X([\frac{1}{2}, 1]) = \mathbb{P}(\{\frac{1}{2} \leq \sqrt{x^2+y^2} \leq 1\}) = \frac{\pi 1^2 - \pi \left(\frac{1}{2}\right)^2}{\pi 1^2} = \frac{3}{4}$  
> We'll learn a good way to describe this distribution in 3.1-3.2.  

---  

# Sections 3.1 and 3.2  

## Cumulative Distribution Functions  

> [!definition] Cumulative Distribution Function (CDF)  
> Let $X$ be a random variable. The **cumulative distribution function (cdf)** of $X$ is the function $F_X: \mathbb{R} \to \mathbb{R}$ defined by $$F_X(t) := \mathbb{P}(X \leq t) = \mathbb{P}(X \in (-\infty, t]) = \mathbb{P}_X((-\infty, t])$$  

Crucial Fact: The cdf completely determines the distribution. Meaning, if $F_X(t)=F_Y(t)$, then $\mathbb{P}_X(A)=\mathbb{P}_Y(A) \forall A \subseteq \mathbb{R}$.  

For example, suppose $F_X(2)=\frac{1}{3}$. What is $\mathbb{P}_X((2, \infty))$?  
$F_X(2) = \mathbb{P}_X((-\infty, 2]) = 1 - \mathbb{P}_X((2, \infty))$  
$\implies \mathbb{P}_X((2, \infty)) = \frac{2}{3}$.  
$F_X(2)=\frac{1}{3}$  

**Examples.**  

> [!question] A fair coin is tossed 3 times. Let $X$ = "number of heads". Find the cdf of $X$ and sketch its graph.  
> $$F_X(t) = \mathbb{P}(X \leq t) = \begin{cases} 0 & t<0 & \mathbb{P}(X\leq0)=\mathbb{P}(\{TTT\}) \\ \frac{1}{8} & 0\leq t\leq1 & \mathbb{P}(X\leq1)=\mathbb{P}(\{TTT,HTT,THT,TTH\}) \\ \frac{1}{2} & 1\leq t<2 & \mathbb{P}(X\leq2)=\mathbb{P}(\{TTT,HTT,THT,TTH,THH,HTH,HHT\}) \\ \frac{7}{8} & 2\leq t<3 & \dots \\ 1 & 3<t & \dots \end{cases}$$  

> [!question] A point is chosen uniformly at random from the unit disk. Let $X$ = "distance of the point from the center". Find the cdf of $X$ and sketch its graph.  
> $F_X(t) = \mathbb{P}(X\leq t) = \mathbb{P}(\text{points in unit disk where distance to center} \leq t)$  
> $$=\frac{\text{area("")}}{\text{total area}} = \begin{cases} 0 & t<0 \\ \frac{\pi t^2}{\pi 1^2} = t^2 & 0\leq t\leq1 \\ 1 & 1<t\end{cases}$$  

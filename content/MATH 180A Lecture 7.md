---
tags:
- "Type/Note"
- "Topic/Probability"
- "Class/MATH_180A"
date:
- 2024-04-15
---
> [!note] **Theorem:** Let $A,B$ be two events in a probability space. Then  
> $A,B$ are independent $\iff$ $A,B^C$ are independent.  

*Proof.* $\Rightarrow$ Assume $A,B$ independent.  

Remember $\mathbb{P}(A\cap B)+\mathbb{P}(A\cap B^C) = \mathbb{P}(A)$  
$\mathbb{P}(A\cap B^C)=\mathbb{P}(A)-\mathbb{P}(A\cap B)$  
$=\mathbb{P}(A)-\mathbb{P}(A)\mathbb{P}(B)$  
$=\mathbb{P}(A)(1-\mathbb{P}(B))$  
$=\mathbb{P}(A)\mathbb{P}(B^C)$  
Shows that $A,B^C$ are independent  

**Example.** Suppose $A,B$ are independent events in a probability space w/ $\mathbb{P}(A)=\frac{1}{3}$ and $\mathbb{P}(B)=\frac{1}{4}$. What is the probability that exactly one of $A,B$ occurs?  
$\mathbb{P}(A\ominus B)$  
$A\ominus B=A\cup B \setminus (A\cap B)$  
$\mathbb{P}(A\ominus B)=\mathbb{P}(A\cap B^C)+\mathbb{P}(B)\mathbb{P}(A^C)$  
$=\frac{1}{3}(1-\frac{1}{4})+\frac{1}{4}(1-\frac{1}{3})$  
$=\frac{1}{4}+\frac{1}{6}=\frac{5}{12}$  

> [!definition] Mutual independence  
> A sequence of events $A_1,A_2,\dots$ in a probability space are **mutually independent** if any collection of events $\mathbb{P}(A_1\cap A_2\cap \dots\cap A_n)=\mathbb{P}(A_1)\mathbb{P}(A_2)\dots\mathbb{P}(A_n)$  

For example, $A_1,A_2,A_3$ are mutually independent if  
$\mathbb{P}(A_1\cap A_2)=\mathbb{P}(A_1)\mathbb{P}(A_2)$  
$\mathbb{P}(A_2\cap A_3)=\mathbb{P}(A_2)\mathbb{P}(A_3)$  
$\mathbb{P}(A_3\cap A_1)=\mathbb{P}(A_3)\mathbb{P}(A_1)$  
$\mathbb{P}(A_1\cap A_2\cap A_3)=\mathbb{P}(A_1)\mathbb{P}(A_2)\mathbb{P}(A_3)$  

**Example.** I toss a fair coin 3 times. Consider the events  
$A$ = {exactly 1 tails in 1st and 2nd toss} = {THH,THT,HTH,HTT}, $\mathbb{P}(A)=\frac{1}{2}$  
$B$ = {exactly 1 tails in 2nd or 3rd toss} = {HTH,TTH,HHT,THT}, $\mathbb{P}(B)=\frac{1}{2}$  
$C$ = {exactly 1 tails in 1st or 3rd toss} = {THH,TTH,HHT,HTT}, $\mathbb{P}(C)=\frac{1}{2}$  
Are $A,B,C$ mutually independent?  
$A\cap B = \{THT,HTH\}$, $\mathbb{P}(A\cap B)=\frac{1}{4}=\mathbb{P}(A)\mathbb{P}(C)$  
$B\cap C = \{TTH,HHT\}$, $\mathbb{P}(B\cap C)=\frac{1}{4}=\mathbb{P}(B)\mathbb{P}(C)$  
$C\cap A = \{THH,HHT,HTH\}$, $\mathbb{P}(C\cap A)=\frac{1}{4}=\mathbb{P}(C)\mathbb{P}(A)$  
$\implies$ they are pairwise independent  
$A\cap B\cap C=\emptyset,\mathbb{P}(A\cap B\cap C)=\emptyset\neq\mathbb{P}(A)\mathbb{P}(B)\mathbb{P}(C)$  
$\implies$ not mutually independent  

# Section 1.5  

## Random Variables  

> [!definition] Random Variable  
> A real-valued **random variable** is a function $X:\Omega\to\mathbb{R}$ where $\Omega$ is the sample space of some probability space, and $X$ is measurable.  
$\{X\in I_1\cup I_2\cup \dots I_n\}\iff \{\omega\in\Omega:X(\omega)\in I_1\text{ or }X(\omega)\in I_2\text{ or }X(\omega)\in I_n\}$  
$I_j$'s are intervals  

**Examples.**  

> [!question] Fair coin toss: $\Omega=\{H,T\}$. Define $X:\Omega\to\mathbb{R}$  
> $X(H)=\pi,X(T)=-\sqrt 2$  

> [!question] Roll a fair die twice: $\Omega=\{1,2,3,4,5,6\}^2$. Define $S:\Omega\to\mathbb{R}$  
> $S((i,j))=i+j$ is the sum of the 2 rolls  

> [!question] Chooes a point uniformly on unit disk $\Omega=\{(x,y)\in\mathbb{R}^2:x^2+y^2+2\}$. Define $x:\Omega\to R$  
> $X((x,y))=\sqrt {x^2 + y^2}$ distance to center of when dart hits.  

### Distributions  

> [!definition] Probability Distribution  
> Let ($\Omega,\mathcal{F},\mathbb{P})$ be a probability space $X:\Omega \to R$ a random variable. The **probability distribution** of $X$ is the probability measure on $\mathbb{R}$  
$\mathbb{P}_x(A):=\mathbb{P}(x\in A) = \mathbb{P}(\{\omega\in\Omega:X(\omega)\in A\})$ for all $A\subseteq \mathbb{R}$.  

**Examples.**  

> [!question] Fair coin toss $\Omega=\{H,T\}$. Define $X:\Omega\to\mathbb{R}$ by $X(H)=\pi, X(T)=-\sqrt{2}$. What is the distribution of $X$?  
> $\mathbb{P}_X(A)$ for every $A\subseteq \mathbb{R}$  
> $\mathbb{P}_X((0,\infty))=\mathbb{P}(X\in[0,\infty))=\frac{1}{2}$  
> $\mathbb{P}_X([-1,1])$  
> $\mathbb{P}_X((-\infty,0])$  

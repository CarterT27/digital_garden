---
tags:
- "Type/Note"
- "Topic/Probability"
- "Class/MATH_180A"
date:
- 2024-04-03
---
Events are subsets of the sample space $\Omega$  
$A,B\subseteq\Omega$  
$0\leq\mathbb{P}(A)\leq1$  
$\mathbb{P}(\Omega)=1$  
$\mathbb{P}(\emptyset)=0$  
$\mathbb{P}(A\cup B)\leq1$  
$C\subseteq A\implies\mathbb{P}(C)\leq\mathbb{P}(A)$  

$\mathbb{P}(A)=\frac{\vert A\vert}{\vert\Omega\vert}=\frac{10}{20}=\frac{1}{2}$  
$\mathbb{P}(B)=\frac{12}{20}$  
$\mathbb{P}(A\cup B)=\frac{\vert A\cup B\vert}{\vert\Omega\vert}=\frac{\vert A\vert+\vert B\vert-\vert A\cap B\vert}{\vert\Omega\vert}=\mathbb{P}(A)+\mathbb{P}(B)+\mathbb{P}(A\cap B)=\frac{1}{2}+\frac{12}{20}-\frac{5}{20}=\frac{17}{20}$  

> [!definition] Inclusion Exclusion Principle  
> $$\mathbb{P}(A\cup B)=\mathbb{P}(A)+\mathbb{P}(B)-\mathbb{P}(A\cap B)$$  

$\mathbb{P}(A\cup B\cup C)=\mathbb{P}(A)+\mathbb{P}(B)+\mathbb{P}(C)-\mathbb{P}(A\cap B)-\mathbb{P}(A\cap C)-\mathbb{P}(B\cap C)+\mathbb{P}(A\cap B\cap C)$  
$\mathbb{P}(A_1\cup\dots\cup A_n)$  

Note: $\mathbb{P}(B\cap C)=\mathbb{P}(BC)$  

6-sided fair die  
$X\in\{1,\dots,6\}$  
$\mathbb{P}(X=3)=\frac{1}{6}$  
A := $X$ is even $\to\mathbb{P}(A)=\frac{3}{6}=\frac{1}{2}$  
B = $X$ is a multiple of 3 $\to\mathbb{P}(B)=\frac{1}{3}$  
C = $X$ is odd $\to\mathbb{P}(C)=\mathbb{P}(A^C)=1-\mathbb{P}(A)=1-\frac{1}{2}=\frac{1}{2}$  
$A\cup B=\{2,4,6\}$  
$\mathbb{P}(A\cup B)=\frac{1}{2}+\frac{1}{3}-\frac{1}{6}=\frac{2}{3}$  

> [!definition] Disjoint  
> $A,B$ are disjoint $\iff A\cap B=\emptyset$  
> $\mathbb{P}(A\cup B)=\mathbb{P}(A)+\mathbb{P}(B)$  

$X\in\{1,\dots,10\}$  
$\mathbb{P}(X=i)=\frac{1}{10}$ uniform  

$X\in\{1,\dots,100\}$  
$\mathbb{P}(X=i)=\frac{1}{100}$  
$\mathbb{P}(\Omega)=\sum_{i=1}^{100}\mathbb{P}(X=i)=\sum_{i=1}^{100}\frac{1}{100}=100\times\frac{1}{100}=1$  

$x\in\mathbb{Z}=\{\dots,-3,-2,-1,0,1,2,3,\dots\}$  
Case I: $\mathbb{P}(x=i)=0\implies\mathbb{P}(\Omega)=0$ ...Contradiction  
Case II: $\mathbb{P}(x=i)=\alpha>0\implies\mathbb{P}(\Omega)=\sum_{i=-\infty}^{\infty}\mathbb{P}(x=i)=\sum_{i=-\infty}^{\infty}\alpha=\infty$ ...Contradiction  
$\implies$ **Can't** have a uniform distribution on $\mathbb{Z}$  
Furthermore you can't have a uniform distribution on $\mathbb{R}$ (use integral magic)  

$x\in[0,1]$  
$\mathbb{P}(x=\frac{1}{2})=0$  
$\mathbb{P}(x\leq\frac{1}{2})=\frac{1}{2}$  
$\mathbb{P}(x\leq\frac{1}{4})=\frac{1}{4}$  
$\mathbb{P}(x\leq\alpha)=\frac{\alpha}{1}=\alpha$ cumulative distribution function  
CDF $\to$ PDF by differentiation  
PDF $\to$ CDF by integration  
$\mathbb{P}(\Omega)=\int_0^1f(x)\,dx$ where $f(x)$ is the probability distribution function  

$x\in[0,2]$  
$\mathbb{P}(x\leq\alpha)=\frac{\alpha}{2}\to f(\alpha)=\frac{1}{2}$  

$x=\text{\# of rolls until I get the first 6 (count the last roll)}$ Geometric distribution  
$x\in\{1,2,\dots\}$  
$\mathbb{P}(x=1)=\frac{1}{6}$  
$\mathbb{P}(x=2)=\frac{5}{6}\times\frac{1}{6}$  
$\mathbb{P}(x=3)=\left(\frac{5}{6}\right)^2\times\frac{1}{6}$  
$\mathbb{P}(x=k)=\left(\frac{5}{6}\right)^{k-1}\times\frac{1}{6}$  
What is the probability that I never get a 6?  
Let's call this event $A$  
$\mathbb{P}(A)=1-\mathbb{P}(A^C)$  
$A^C=(x=k\text{ for some }k\in\{1,\dots\})$  
$\mathbb{P}(A^C)=\sum_{k=1}^\infty\mathbb{P}(x=k)$  
$=\sum_{k=1}^\infty\left(\frac{5}{6}\right)^{k-1}\left(\frac{1}{6}\right)$  
$=\left(\frac{1}{6}\right)\left[\sum_{k=1}^\infty\left(\frac{5}{6}\right)^{k-1}\right]$  
$=\left(\frac{1}{6}\right)\left[\sum_{t=0}^\infty\left(\frac{5}{6}\right)^t\right]$ Geometric series  
$=\frac{1}{6}\times\frac{1}{1-\frac{5}{6}}=1$  
$\mathbb{P}(A)=1-1=0$  

$1+x+x^2+x^3+\dots=\frac{1}{1-x}$  
$1+2x+3x^2+\dots=\frac{d}{dx} 1+x+x^2+x^3+\dots=\frac{d}{dx}\frac{1}{1-x}=\frac{1}{(1-x)^2}$  

$\mathbb{E}(x)=\sum_{k=1}^\infty k\mathbb{P}(x=k)$  
$=\sum_{k=1}^\infty k\left(\frac{5}{6}\right)^{k-1}\left(\frac{1}{6}\right)$  
$=\frac{1}{6}\sum_{k=1}^\infty k\left(\frac{5}{6}\right)^{k-1}$  
$=\frac{1}{6}\times\frac{1}{\left(1-\frac{5}{6}\right)^2}=6$  

$e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\dots$  
$(A\cup B)^C=A^C\cap B^C$  
$(A\cap B)^C=A^C\cup B^C$  

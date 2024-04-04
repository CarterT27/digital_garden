---
tags:
- "Type/Note"
- "Topic/Probability"
- "Class/MATH_180A"
date:
- 2024-04-03
---
> [!definition] Uniform Probability Measure  
> Let $\Omega$ be a set with $\#\Omega < \infty$. The **uniform probability measure** on $\Omega$ is defined by $\mathbb{P}(A)=\frac{\#A}{\#\Omega}$  
> $\#A$ = cardinality of $A$ = number of elements in $A$  
> A probability is uniform $\iff$ $\mathbb{P}(\{w_1\})=\mathbb{P}(\{w_2\})$ for every $w_1,w_2\in\Omega$.  

TODO: Prove this equivalence using the three axioms of probability.  

## Example. A fair die is rolled twice.  

> [!question] a) Describe the sample space and probability measure  
> $\Omega=\{1,2,3,4,5,6\}\times\{1,2,3,4,5,6\}=\{1,2,3,4,5,6\}^2$  
> $\times$: Cartesian product, means all ordered pairs  
> $\mathbb{P}$ = uniform probability measure on $\Omega$.  
> $\mathbb{P}(\{(i,j)\})=\frac{\#\{(i,j)\}}{\#\Omega}=\frac{1}{6}$  
> $\mathbb{P}(A)=\frac{\#A}{\#\Omega}=\frac{\#A}{36}$  

> [!question] b) Calculate the probability that the sum of two rolls is 8.  
> $\mathbb{P}(\text{"sum = 8"})=\mathbb{P}(\{(2,6), (3,5), (4,4), (5,3), (6, 2)\})=\frac{5}{36}$  

> [!question] c) Calculate the probability that the 2nd roll is strictly larger than the 1st roll.  
> $\mathbb{P}(\text{"2nd roll > 1st roll"})=\mathbb{P}(\{(1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (2,4), (2,5), (2,6), (3,4), (3,5), (3,6), (4,5), (4,6), (5,6)\})$  
> $=\frac{15}{36}=\frac{5}{12}$  

Key Property of Probability Space: If $A_1,A_2,\dots$ is a (finite or infinite) sequence of disjoint events, then $\mathbb{P}(A_1\cup A_2\cup\dots)=\mathbb{P}(A_1)+\mathbb{P}(A_2)+\dots$  

## Example. Suppose 2 fair coins are flipped. What is the probability that both are heads or both are tails?  

$\mathbb{P}(\{HH\}\cup\{TT\})=\mathbb{P}(\{HH\})+\mathbb{P}(\{TT\})=\frac{1}{4}+\frac{1}{4}=\frac{1}{2}$  
$\{HH\}\cap\{TT\}=\emptyset$  

Suppose we flip 2 fair coins again. Let $A$ = "at least one heads" = $\{HH,HT,TH\}$  
and $B$ = "at least one tails" = $\{HT,TH,TT\}$  

Then $\mathbb{P}(A)+\mathbb{P}(B)=\frac{3}{4}+\frac{3}{4}=\frac{6}{4}=\frac{3}{2}>1\neq\mathbb{P}(A\cup B)$  
The formula $\mathbb{P}(A\cup B)=\mathbb{P}(A)+\mathbb{P}(B)$ doesn't hold because $A\cap B=\{HT,TH\}\neq\emptyset$  
not disjoint  

> [!definition] Inclusion-Exclusion Principle (2 events)  
> For any 2 events $A,B$ in any probability space, $\mathbb{P}(A\cup B)=\mathbb{P}(A)+\mathbb{P}(B)-\mathbb{P}(A\cap B)$  

**Proof.**  
$A=(A\setminus B)\cup(A\cap B)$  
$B=(B\setminus A)\cup(A\cap B)$  
$\mathbb{P}(A)+\mathbb{P}(B)=\mathbb{P}(A\setminus B)+\mathbb{P}(A\cap B)+\mathbb{P}(B\setminus A)+\mathbb{P}(A\cap B)$  
$=\mathbb{P}(A\cup B)+\mathbb{P}(A\cap B)$  
$\implies\mathbb{P}(A\cup B)=\mathbb{P}(A)+\mathbb{P}(B)-\mathbb{P}(A\cap B)$  

# Section 1.2  

## Random Sampling  

We successively select $k$ elements from a finite set $S$ ($\# S=n$) and record the outcome.  

Example: $S=\{r,w,b\},k=2$  

Variant 1: w/replacement, order matters  
$\Omega=\{(r,r),(r,w),(r,b),(w,r),(w,w),(w,b),(b,r),(b,w),(b,b)\}$  
$\Omega=\{r,w,b\}^2=s^2$  
$\Omega=S^k$  
$\#\Omega=n^k$  

Variant 2: w/o replacement, order matters  
$\Omega=\{(r,w),(r,b),(w,r),(w,b),(b,r),(b,w)\}$  
$\Omega$ = set of distinct $k$-tuples from $S$.  
$\#\Omega=(n)(n-1)\dots(n-k+1)=\frac{n!}{(n-k)!}=(n)_k$ "$n$ permute $k$"  

Variant 3: w/o replacement, order doesn't matter (use $\{\}$ to show that order doesn't matter)  
$\Omega=\{\{r,w\},\{r,b\},\{w,b\}\}$  
$\Omega$ = "set of unordered distinct $k$-tuples from $S$" = "set of subsets of $S$ w/ cardinality $k$"  
$\#\Omega=\frac{n!}{(n-k)!k!}=\begin{pmatrix}n\\k\end{pmatrix}$ "$n$ choose $k$"  

The probabilitiy measure will consider for these problems is **uniform**  

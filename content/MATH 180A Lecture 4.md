---
tags:
- "Type/Note"
- "Topic/Probability"
- "Class/MATH_180A"
date:
- 2024-04-08
---
# Section 1.4  

## Decompositions  

In this section we will see many important uses of the identity $\mathbb{P}(A_1\cup A_2\cup\dots)=\mathbb{P}(A_1)+\mathbb{P}(A_2)+\dots$ for disjoint events $A_1,A_2,\dots$  

**Example.** A fair coin is flipped 5 times. Calculate the probability that it lands tails at least 3 times.  

$A=$ "$\geq3$ T"  
$A_3=$ "$=3$ T"  
$A_4=$ "$=4$ T"  
$A_5=$ "$=5$ T"  
$A_3,A_4,A_5$ are disjoint,  
and $A=A_3\cup A_4\cup A_5$  
means $\mathbb{P}(A)=\mathbb{P}(A_3)+\mathbb{P}(A_4)+\mathbb{P}(A_5)$  
$A_3=\{HHTTT,TTTHH,THHTT,\dots\}$  
#$A_3$ = choosing 3 positions out of 5 to be T = $\begin{pmatrix}5\\3\end{pmatrix}=\frac{5\cdot4}{2\cdot1}=10$  
$\mathbb{P}(A_3)=\frac{\#A_3}{\#\Omega}=\frac{10}{2^5}=\frac{5}{16}$  
$\mathbb{P}(A_4)=\frac{\#A_4}{\#\Omega}=\frac{\begin{pmatrix}5\\4\end{pmatrix}}{2^5}$  
$\mathbb{P}(A_5)=\frac{\#A_5}{\#\Omega}=\frac{\begin{pmatrix}5\\5\end{pmatrix}}{2^5}=\frac{1}{32}$  
$\mathbb{P}(A)=\frac{10}{2^5}+\frac{5}{2^5}+\frac{1}{2^5}=\frac{1}{2}$  

## Complements  

> [!note] **Fact.** Let $A$ be an event in a probability space and $A^C=\Omega\setminus A$ its complement.  
> Then $\mathbb{P}(A^C)=1-\mathbb{P}(A)$  

*Proof.*  
$\Omega=A\cup A^C,\emptyset=A\cap A^C$ (disjoint)  
$\mathbb{P}(\Omega)=\mathbb{P}(A)+\mathbb{P}(A^C)$  
$\Rightarrow \mathbb{P}(A^C)=1-\mathbb{P}(A)$  

**Example.** 4 fair dice are rolled. Calculate the probability that we get at least one pair of doubles.  

look at complement  
$\mathbb{P}($"at least one pair of doubles"$)$  
$=1-\mathbb{P}($"don't get at least 1 pair of doubles"$)$  
$=1-\mathbb{P}($"4 rolls are distinct"$)$  
$=1-\frac{\#\text{"4 rolls are distinct"}}{\#\Omega}=1-\frac{(6)_4}{6^4}$  
$=1-\frac{10}{36}=\frac{13}{18}$  

**Birthday Problem:**  
$\mathbb{P}($"at least 2 same bday"$)=1-\mathbb{P}($"distinct bdays"$)$  
$=1-\frac{(365)_{240}}{365^{240}}$  

## Inclusion-Exclusion  

$$\mathbb{P}(A\cup B)=\mathbb{P}(A)+\mathbb{P}(B)-\mathbb{P}(A\cap B)$$  

**Example.** In a given country, 20% of the population owns a cat, 25% owns a dog, and 5% owns one of each.  
What is the probability that a person chosen uniformly at random from this country owns neither a cat nor a dog?  

$C$ = person owns a cat  
$D$ = person owns a dog  
owns neither = $C^C\cap D^C=(C\cup D)^C$ de Morgan's Law  

> [!note] Side Note de Morgan's Law  
> Also says  
> $C^C\cup D^C=(C\cap D)^C$  

$\mathbb{P}($"owns neither"$)=\mathbb{P}(C^C\cap D^C)=\mathbb{P}((C\cup D)^C)$  
$=1-\mathbb{P}(C\cup D)$  
$=1-(\mathbb{P}(C)+\mathbb{P}(D)-\mathbb{P}(C\cap D))$  
$=1-(0.2+0.25-0.05)$  
$=1-0.4=0.6$  

## Monotonicity  

> [!note] **Fact.** If $A\subseteq B$, then $\mathbb{P}(A)\leq\mathbb{P}(B)$  

*Proof.*  
$B=A\cup(B\setminus A)$  
$\mathbb{P}(B)=\mathbb{P}(A)+\mathbb{P}(B\setminus A)$  
$\geq\mathbb{P}(A)+0$  
$=\mathbb{P}(A)$.  

**Example.** Suppose that out of the total North American population, 50% of the  
people have at some point in their lives visited the US, 30% has visited Texas, and 40% has visited California. Knowing only this information, what is the smallest possible percentage of the North American population that has visited both Texas and California? And largest?  

$T$ = "person visited Texas"  
$C$ = "person visited California"  
$U$ = "person visited US"  

$\mathbb{P}(T\cup C)=\mathbb{P}(T)+\mathbb{P}(C)-\mathbb{P}(T\cap C)$  
$T\cup C\subseteq U\implies \mathbb{P}(T\cup C)\leq \mathbb{P}(U)$  
$\mathbb{P}(U)\geq\mathbb{P}(T)+\mathbb{P}(C)-\mathbb{P}(T\cap C)$  
$\mathbb{P}(T\cap C)\geq \mathbb{P}(T)+\mathbb{P}(C)-\mathbb{P}(U)$  
$\mathbb{P}(T\cap C)\geq0.3+0.4-0.5=0.2$  
Smallest is 20%  

$\mathbb{P}(T\cap C)\leq min(\mathbb{P}(T),\mathbb{P}(C))$ b/c $T\cap C\subseteq T$ and $T\cap C\subseteq C$  
$=min(0.3,0.4)=0.3$  
30% is largest  

# Section 2.1  

## Conditional Probability  

**Example.**  

> [!question] Your friend rolls a pair of fair dice. What is the probability that the sum is 10?  
> $\mathbb{P}($"sum is 10"$)=\frac{\#\{(4,6),(5,5),(6,4)\}}{\#\Omega}=\frac{3}{6^2}=\frac{1}{12}$  

> [!question] Your friend rolls a pair of fair dice and tells you that the sum is a 2 digit number. Now what is the probability that the sum is 10?  
> $\frac{\#\{(4,6),(5,5),(6,4)\}}{\#\{(4,6), (5,5), (6,4), (5,6), (6,5), (6,6)\}}=\frac{3}{6}=\frac{1}{2}$  

> [!question] Your friend rolls a pair of fair dice and tells you that one of the rolls is a 6. What is the probability that the sum is 10?  
> answer not $\frac{1}{6}$  

---
tags:
- "Type/Note"
- "Topic/Probability"
- "Class/MATH_180A"
date:
- 2024-04-01
---
Souce: https://canvas.ucsd.edu/courses/55106/assignments/syllabus  

# Section 1.1  

> [!question] There are roughly 240 students in this class. Which of the following is closest to the probability that at least 2 students share the same birthday?  
> a. 1%  
> b. $\frac{240\cdot239}{365\cdot364}\approx43\%$  
> c. $\frac{240}{365}\approx66\%$  
> d. 99%  
> **e. 100%**  

## Use of Probability in History  

1600s - Gambling  
1900s - Quantum Mechanics  
1950s - Finance/Stock Market  
2000s - Machine Learning  

## Modern rigorous formulation of probability theory due to Kolmorgorov in 1933.  

Common Ingredients In Models of Randomness:  

> [!definition] Probability Space  
> A **probability space** is a triple ($\Omega,\mathcal{F},\mathbb{P}$), where  
>  
> **sample space** ($\Omega$) - collection of possible outcomes, i.e. {HH, HT, TH, TT}  
>  
> collection of **events** ($\mathcal{F}$) - An event is a subset of $\omega$, i.e. $A\in \mathcal{F}$, A="1st flip is T"={TH,TT}, A="at least 1 H"={HH,HT,TH}, $\mathbb{P}(\text{"1st flip is T"})=\frac{\{TH,TT\}}{\Omega}=\frac{2}{4}$, $\mathbb{P}(\text{"at least 1 H"})=\frac{3}{4}$  
>  
> **probability measure** ($\mathbb{P}$)  
> $P:\mathcal{F}\to[0,1]$  
> a function from  
> $\mathcal{F}\text{ to }[0,1]$  
> satisfying Kolmorgorov's axioms:  
> - $0\leq\mathbb{P}(A)\leq1$  
> - $\mathbb{P}(\emptyset)=0, \mathbb{P}(\Omega)=1$  
> - $\mathbb{P}(A\text{ or }B) = \mathbb{P}(A) + \mathbb{P}(B)$  
>  
> (A disjoint from B (meaning A and B can't happen)})  
> $\emptyset$ = "empty set"  

Area($A\cup B$) = area($A$) + area($B$)  

> [!note] If $A_1,A_2,\dots$ is a sequence of disjoint events, then $\mathbb{P}(A_1\cup A_2\cup\dots)=\mathbb{P}(A_1)+\mathbb{P}(A_2)+\dots$  
> disjoint means $A_i\cap A_j = \emptyset$  

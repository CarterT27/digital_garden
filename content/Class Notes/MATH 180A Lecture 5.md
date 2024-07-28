---
tags:
- "Type/Note"
- "Topic/Probability"
- "Class/MATH_180A"
date:
- 2024-04-10
---
> [!question] Your friend rolls a pair of fair dice and tells you that one of the rolls is a 6. What is the probability that the sum is 10?  
> answer not $\frac{1}{6}$  
> $\frac{\#\{(4,6),(6,4)\}}{\#\{(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(1,6),(2,6),(3,6),(4,6),(5,6)\}}=\frac{2}{11}$  

> [!definition] $\mathbb{P}(\cdot\vert B)$  
> Given a probability space $(\Omega, \mathcal{F}, \mathbb{P})$ and a positive-probability event $B\in \mathcal{F}$, we define a new probability measure $\mathbb{P}(\cdot \vert B)$ on $(\Omega,\mathcal{F})$ defined by  
> $$\mathbb{P}(A \vert B):= \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}$$  
> "Probability of $A$ given $B$"  

Note:  
$\mathbb{P}(\cdot \vert B)$ satisfies everything that a probability measure satisfies  
1. $0 \leq \mathbb{P}(A \vert B) \leq 1$  
2. $\mathbb{P}(\Omega) = 1$  
3. $A_1,A_2$ disjoint $\implies \mathbb{P}(A_1 \cup A_2 \vert B) = \mathbb{P}(A_1 \vert B) + \mathbb{P}(A_2 \vert B)$  
4. $\mathbb{P}(A^C \vert B) = 1 - \mathbb{P}(A \vert B)$  
5. $A_1 \subseteq A_2 \implies \mathbb{P}(A_1 \vert B) \leq \mathbb{P}(A_2 \vert B)$  

> [!note] What if $\mathbb{P}$ is uniform?  
> $$\mathbb{P}(A \vert B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}=\frac{\# A \cap B / \Omega}{\# B / \# \Omega }=\frac{\# A \cap B}{\# B}$$  

**Example.** An urn contains 4 red marbles and 6 blue marbles. 3 are drawn w/o replacement.  

> [!question] What is the probability that exactly 2 of the marbles drawn are red?  
> $=\frac{\begin{pmatrix}4\\2\end{pmatrix}\begin{pmatrix}6\\1\end{pmatrix}}{\begin{pmatrix}10\\3\end{pmatrix}}=\frac{\frac{4\cdot3}{2\cdot1}\cdot\frac{6}{1}}{\frac{10\cdot9\cdot8}{3\cdot2\cdot1}}=\frac{3}{10}$  

> [!question] Suppose we know that at least 1 of the marbles drawn is red. Given this information, what is the probability that exactly 2 are red?  
> $\mathbb{P}(\text{2 red}\vert\geq\text{ 1 red})=\frac{\mathbb{P}(\text{"2 are red" and }\geq\text{" 1 are red"})}{\mathbb{P}(\geq\text{"1 are red"})}$  
> $=\frac{\mathbb{P}(\text{"2 red"})}{\mathbb{P}(\geq\text{"1 red"})}=\frac{\frac{3}{10}}{1-\mathbb{P}(\text{"0 red"})}$  
> $\mathbb{P}(\text{"0 red"})=\frac{\begin{pmatrix}4\\0\end{pmatrix}\begin{pmatrix}6\\3\end{pmatrix}}{\begin{pmatrix}10\\3\end{pmatrix}}=\frac{\frac{6\cdot5\cdot4}{3\cdot2\cdot1}}{\frac{10\cdot9\cdot8}{3\cdot2\cdot1}}=\frac{1}{6}$  
> $\frac{\frac{3}{10}}{1-\mathbb{P}(\text{"0 red"})}=\frac{\frac{3}{10}}{1-\frac{1}{6}}=\frac{9}{25}$  

---  

## Multiplication Rule  

> [!definition] Multiplication Rule  
> $$\mathbb{P}(A \cap B) = \mathbb{P}(A \vert B) \cdot \mathbb{P}(B)=\mathbb{P}(B \vert A) \cdot \mathbb{P}(A)$$  

*Proof.*  
Take definition $\mathbb{P}(A \vert B)= \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}$  
Multiply by $\mathbb{P}(B) \Rightarrow \mathbb{P}(A \vert B) \mathbb{P}(B) = \mathbb{P}(A \cap B)$.  

**Example.** An urn contains 4 red marbles and 6 blue marbles. 2 are drawn w/o replacement. Calculate the probability that both marbles drawn are red.  

Before we would do:  
$\frac{\begin{pmatrix}4\\10\end{pmatrix}\begin{pmatrix}3\\9\end{pmatrix}}{\begin{pmatrix}10\\2\end{pmatrix}}=\frac{4}{10}\frac{3}{9}$  

Using multiplication rule:  
$\mathbb{P}(\text{"both are red"})=\mathbb{P}(\text{"1st is red" and "2nd is red"})$  
$=\mathbb{P}(\text{"2nd is red"}\vert\text{"1st is red"})\cdot\mathbb{P}(\text{"1st is red"})$  
$=\frac{3}{9}\cdot\frac{4}{10}$  

---  

## Two-Stage Experiments  

The previous example falls into a more general category of problems, called two-stage experiments, where  
- first, an experiment with a random outcome is performed, and then  
- a second experiment is performed, whose setup depends on the outcome of the first experiment.  

**Example.** Urn 1 contains 1 red marble and 2 blue marbles. Urn 2 contains 3 white marbles and 2 red marbles. First one of the urns is chosen uniformly at random, and then one marble is drawn uniformly at random from the chosen urn. What is the probability that the marble drawn is red?  

$\mathbb{P}(\text{"red"})=\mathbb{P}($"red"$\cap$"urn 1"$)+\mathbb{P}($"red"$\cap$"urn 2"$)$  
$=\mathbb{P}(\text{"red"}\vert\text{"urn 1"})\cdot\mathbb{P}(\text{"urn 1"})+\mathbb{P}(\text{"red"}\vert\text{"urn 2"})\cdot\mathbb{P}(\text{"urn 2"})$  
$=\frac{1}{3}\cdot\frac{1}{2}+\frac{2}{5}\cdot\frac{1}{2}$  
$=\frac{11}{30}$  

---  

## Law of Total Probability  

The calculation in the previous example can be generalized to an important law.  

> [!definition] Law of Total Probability  
> If $B_1,B_2,\dots\in\mathcal{F}$ is a finite or infinite sequence of events partitioning $\Omega$, then for any event $A\in\mathcal{F}$,  
> 1. $\mathbb{P}(A)=\sum_i\mathbb{P}(A\cap B_i)=\mathbb{P}(A\cap B_1)+\mathbb{P}(A\cap B_2)+\dots$  
> 2. $\mathbb{P}(A)=\sum_i\mathbb{P}(A\vert B_i)\mathbb{P}(B_i)=\mathbb{P}(A\vert B_1)\mathbb{P}(B_1)+\mathbb{P}(A\vert B_2)\mathbb{P}(B_2)+\dots$  

*Proof.*  
(2) follows from (1) and the multiplication rule.  
(1) can be proved using the decomposition rule  

**Example.** 90% of coins are fair. 9% of coins land on heads 60% of the time, and 1% of coins land on tails 80% of the time. You pick up a random coin off the street and flip it. How likely is it to land on heads?  

$\mathbb{P}(\text{"heads"})=\mathbb{P}(H\vert \text{coin 1})\mathbb{P}(\text{coin 1})+\mathbb{P}(H\vert \text{coin 2})\mathbb{P}(\text{coin 2})+\mathbb{P}(H\vert \text{coin 3})\mathbb{P}(\text{coin 3})$  
$=\frac{1}{2}\cdot 0.9+0.6\cdot 0.09+0.8\cdot 0.01=0.572=57.2\%$  

---
tags:
- "Type/Note"
- "Topic/Probability"
- "Class/MATH_180A"
date:
- 2024-04-12
---

# Section 2.2

## Bayes' Rule

> [!question] A flu test is 99% accurate, meaning that the false positive rate is 1% and the false negative rate is 1%. Currently, 0.33% of the US population has the flu. A randomly chosen person from the US population tests positive for the flu. What is the probability that this person actually has the flu, roundest to the nearest percent?
> a. 99%
> b. 75%
> **c. 25%**
> d. 0.33%
> F = "person has the flu" 1st stage event
> P = "person tests positive" 2nd stage event
> $\mathbb{P}(F\vert P)=\mathbb{P}(P\vert F)\cdot\frac{\mathbb{P}(F)}{\mathbb{P}(P)}$
> $=\left[1-\mathbb{P}(P^C\vert F)\right]\frac{\mathbb{P}(F)}{\mathbb{P}(P)}=\frac{0.99\cdot0.0033}{\mathbb{P}(P\vert F)\cdot\mathbb{P}(F)+\mathbb{P}(P\vert F^C)\mathbb{P}(F^C)}$
> $=\frac{0.99\cdot0.0033}{0.99\cdot0.0033+0.01\cdot(1-0.0033)}\approx24.69\%$

**Example.** 90% of coins are fair. 9% of coins are slightly biased, meaning they land heads 60% of the time, and 1% of coins are heavily biased, meaning they land heads 80% of the time. I pick up a random coin off the street and flip it. It lands heads. What is the probability that the coin I picked up is heavily biased?

Asking for $\mathbb{P}(\text{1st event in experiment}\vert\text{2nd event in experiment})$
$\Rightarrow$ Use Bayes' Rule

---

$\mathbb{P}(B\vert A) \neq \mathbb{P}(A\vert B)$
$\mathbb{P}(B\vert A)=\frac{\mathbb{P}(B\cap A)}{\mathbb{P}(A)}$
$\mathbb{P}(A\vert B)=\frac{\mathbb{P}(A\cap B)}{\mathbb{P}(B)}$
$\mathbb{P}(A\vert B)\frac{\mathbb{P}(B)}{\mathbb{P}(A)}=\frac{\mathbb{P}(A\cap B)}{\mathbb{P}(A)}$

> [!definition] Bayes' Rule
> $$\mathbb{P}(B\vert A)=\mathbb{P}(A\vert B)\cdot \frac{\mathbb{P}(B)}{\mathbb{P}(A)}$$

---

Fair: $C_1$, Lightly Biased: $C_2$, Heavily Biased: $C_3$
$\mathbb{P}(C_3\vert H)=\mathbb{P}(H\vert C_3)\frac{\mathbb{P}(C_3)}{\mathbb{P}(H)}$
$=\frac{0.8\cdot 0.01}{0.512}\approx 0.0156=1.56\%$

# Section 2.3

## Independence

I flip a fair coin 2 times. What is the probability that the 2nd flip is heads? Suppose I told you that the 1st flip is tails. Now what is the probability that the 2nd flip is heads?
$\frac{1}{2},\frac{1}{2}$

> [!definition] Independent
> Two events $A,B$ in a probability space are **independent** if any of the three equivalent conditions hold:
> 1. $\mathbb{P}(A\vert B)=\mathbb{P}(A)$
> 2. $\mathbb{P}(A\cap B)=\mathbb{P}(A)\cdot\mathbb{P}(B)$
> 3. $\mathbb{P}(B\vert A)=\mathbb{P}(B)$

Why are these equivalent?
$\mathbb{P}(A\cap B)=\mathbb{P}(A)\cdot\mathbb{P}(B)$
$\mathbb{P}(A\vert B)=\frac{\mathbb{P}(A\cap B)}{\mathbb{P}(B)}=\mathbb{P}(A)$
$\mathbb{P}(B\vert A)=\frac{\mathbb{P}(B\cap A)}{\mathbb{P}(A)}=\mathbb{P}(B)$

**Example.** A bag contains 4 red marbles and 7 blue ones. Two are sampled. Let $A$ be the event that the 1st marble is red and $B$ the event that the 2nd marble is blue.

> [!question] If the sampling is done w/ replacement, are $A,B$ independent?
> $\mathbb{P}(B\vert A)=\frac{7}{11}=\mathbb{P}(B)$

> [!question] If the sampling is done w/o replacement, are $A,B$ independent?
> $\mathbb{P}(B\vert A)=\frac{7}{10}$
> $\mathbb{P}(B) = \mathbb{P}(B\vert A)\cdot\mathbb{P}(A)+\mathbb{P}(B\vert A^C)\cdot\mathbb{P}(A^C)$
> $=\frac{7}{10}\frac{4}{11}+\frac{6}{10}\frac{7}{11}=\frac{7}{11}\neq\frac{7}{10}$
> $\implies$ not independent

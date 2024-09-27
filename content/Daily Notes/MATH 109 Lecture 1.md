---
tags:
- "Type/Note"
- "Topic/Mathematics"
- "Class/MATH_109"
date:
- 2024-09-27
---

Textbook: An Introduction to Mathematical Reasoning - Peter Eccles
Textbook ISBN: 0521597188

## Rough Overview

Weeks 1-2: Basic Proof Theory (Ch. 1-5)
- Proof by contradiction
- Mathematical induction (important)

Week 3-4: Sets and Functions (Ch. 6-?)
- End of midterm 1 content

Elementary Number Theory

Combinatorics - counting things
- End of midterm 2 content

## Chapter 1

> [!definition] Statement
> A (mathematical) **statement** is a sentence that asserts something and is either **true** or **false**.

> [!example] Today is September 30
> False statement

> [!example] $3>2$
> True statement

> [!example] $12+11$
> Not a statement

> [!example] $12+11=23$
> True statement

> [!example] If $a>b$ and $b>0$ then $a^2 > b^2$.
> Involves "and," "if," "then"
> Involves "variables" $a$, $b$

> [!definition] A statement is **atomic** if it cannot be broken up into smaller ones
> More complicated mathematical statements are made from combining atomic statements with logical connectors.

## Logical "not", "and", and "or"

(next class "imply" and "equivalent" (Ch. 2))

not ($\neg$) (negation)
and ($\land$) (conjunction)
or ($\lor$) (disjunction)

From now on, $P$, $Q$, $R$ represent statements
- $\neg P$ - negation of $P$
- $P \land Q$ - $P$ and $Q$
- $P \lor Q$ - $P$ or $Q$

Concrete exercise
Let $P$ be $3 > 2$
Let $Q$ be $2 > 1$
$\neg P$ - It is false that $3 > 2$
$P \land Q$ - $3>2$ & $2>1$

## Truth Table for Locial Connectors

Truth Table - deducing the truth value of complicated mathematical statements using the truth values of atomic statements and truth rules

> [!example] Truth Table for $\land$
> | $P$ | $Q$ | $P\land Q$ |
> | --- | --- | --- |
> | T | T | T |
> | T | F | F |
> | F | T | F |
> | F | F | F |
> The last column represents the truth values for $\land$

> [!example] Truth Table for $\neg$
> | $P$ | $\neg P$ |
> | --- | --- |
> | T | F |
> | F | T |

> [!example] Truth Table for $\lor$
> | $P$ | $Q$ | $P\lor Q$ |
> | --- | --- | --- |
> | T | T | T |
> | T | F | T |
> | F | T | T |
> | F | F | F |

> [!remark] Suppose $P\lor Q$ is true
> Some people might think that exactly one of $P,Q$ is true.
> However, it just means they are not both false.

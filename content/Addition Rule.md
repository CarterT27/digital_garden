---
tags:
  - "#Type/Definition"
  - "#Topic/Data_Science"
  - "#Class/DSC_10"
---

> [!definition] Addition Rule
> If $A$ and $B$ are any two [[Mutually Exclusive|mutually exclusive]] [[Event|events]], then $$P(A\text{ or }B)=P(A)+P(B)$$

> [!question]- Suppose I have two biased coins, coin $A$ and coin $B$. Coin $A$ flips heads with probability 0.6, and coin $B$ flips heads with probability 0.3. I flip both coins once. What's the probability I see two different faces?
> $P=P(HT)+P(TH)=0.6\cdot0.7+0.4\cdot0.3$

**Proof:**
If $A$ and $B$ are events consisting of [[Equally-Likely Outcomes|equally-likely outcomes]], and furthermore $A$ and $B$ are mutually exclusive (meaning they have no overlap), then $$P(A\text{ or }B)=\frac{\text{\# of outcomes satisfying either A or B}}{\text{total \# of outcomes}}$$ $$=\frac{(\text{\# of outcomes satisfying A})+(\text{\# of outcomes satisfying B})}{\text{total \# of outcomes}}$$ $$=\frac{(\text{\# of outcomes satisfying A})}{\text{total \# of outcomes}}+\frac{(\text{\# of outcomes satisfying B})}{\text{total \# of outcomes}}$$ $$=P(A)+P(B)$$
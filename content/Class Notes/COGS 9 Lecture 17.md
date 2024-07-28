---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/COGS_9"
date:
- 2024-02-16
---
Source: https://drive.google.com/file/d/1G9UA2k7KRaprGxA79ZzbusKUYbH24SCz/view?usp=sharing  

# Inferential Analysis  

## Inference and Sampling  

**Problem:** Does Sesame Street affect kids brain development?  
**Data science question:** Is there a relationship between watching Sesame Street and test scores among children?  
**Type of analysis:** Inferential analysis  

Inferential analysis is done by taking a representative sample of the population and using the data collected to extrapolate the results to the rest of the population.  

## Approaches to Inference  

> [!note] Correlation  
> Association between variables  
> Positive and negative correlation  
> Stronger relationship = higher correlation  
> i.e. Pearson Correlation, Spearman Correlation  

> [!note] Pearson's $r$  
> Linear correlation between two variables  
> Takes values [-1,1]  

Correlation does not equal slope.  
Correlation does not equal causation.  
Correlation establishes a relationship.  
It does NOT establish causation.  

> [!note] Comparison of Means  
> Difference in means between variables  
> i.e. t-test, ANOVA  

> [!note] t-test  
> tests for difference in means between groups  
> Assumptions:  
> - Data are continuous  
> - Normally distributed  
> - Large enough sample size  
> - Equal variance b/w groups  

> [!note] p-value  
> the probability of getting the observed results (or results more extreme) by chance alone  

> [!note] Regression  
> Does change in one variable mean change in another?  
> i.e. simple regression, multiple regression  

> [!note] Non-Parametric Tests  
> For when assumptions in these 3 other categories are not met  
> i.e. Wilcoxon rank-sum test, Wilcoxon sign-rank test, sign test  

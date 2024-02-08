---
tags:
- Type/Note
- Topic/Data_Science
- Class/COGS_9
date:
- 2024-02-05
---
Source: https://drive.google.com/file/d/1dZnXorO3mHcLTs1tggE6NFs_t3xgRSmJ/view  

> [!note] Why Effective Data Communication Matters  
> 1. It's often the only thing your coworkers/bosses see  
> 2. It can set your work apart from others'  
> 3. It helps show off the awesome stuff you've done  
> 4. Cognitive load is a thing  

> [!note] Less is More  
> effective, attractive, impactive  

# Descriptive and Exploratory Data Analyses  

## Analytical Approaches  

### Typically Less Effort  

> [!note] Descriptive Analysis  
> - 1st thing you do on new data  
> - Summarize the data  
> - Univariate plots of variables  

> [!note] Exploratory Analysis  
> - Exploring relationships  
> - Asking/Defining Questions  
> - Univariate/Bivariate/Multivariate analysis and plotting  

> [!note] Inferential Analysis  
> - Estimating uncertainty  
> - Test theories (inferring) about the population (world)  
> - Building inference models  

> [!note] Predictive Analysis  
> - Building predictive models  
> - Use historical knowledge to predict future events  
> - Finding patterns  

> [!note] Causal Analysis  
> - Determine the average change in one variable when you alter another  
> - Typically requires experiments (e.g. randomized studies)  
> - "Gold" standard in data analysis  

> [!note] Mechanistic Analysis  
> - Understand precise changes one variable has on another  
> - Typically modeled using deterministic equations  

## Descriptive Analysis  
1. Size  
2. Missingness  
3. Shape  
4. Central tendency  
5. Variability  

> [!note] Outliers can occur due to...  
> - Data entry errors  
> - Poor sampling procedures  
> - Technical or mechanical error  
> - Unexpected changes in weather  
> - People providing inaccurate information  

> [!warning] Observations should only be removed from your dataset if you have a valid reason to do so.  

> [!note] mean and median are used to summarize the central tendency for quantitative variables  

> [!note] mode is most helpful in describing the central tendency for categorical variables  

> [!note] The central tendency tells you part of the story. The variability in the values in your observation helps fill in the rest.  

> [!note] Variability tells how spread out the values are  
> Range: highest score - lowest score  
> Interquartile range (IQR): 75th percentile - 25th percentile  
> Variance: measures how close the values in the distribution are to the middle of the distribution  
> - average squared difference from the mean  
> - $s^2=\frac{\sum(x_{i}-\bar{x})^2}{n-1}$  
> - $s^2$: sample variance  
> - $x_{i}$: ith element of the sample  
> - $\bar{x}$: mean of the sample  
> - $n$: sample size  
> Standard Deviation (SD): square root of the variance  

![[Pasted image 20240206002951.png]]  

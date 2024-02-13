---
tags:
- Type/Note
- Topic/Data_Science
- Class/COGS_9
date:
- 2024-02-07
---
Source: https://drive.google.com/file/d/1Om8FZiWzg8Ok3UoUpGIA87bPbVrKX7ou/view  

# Descriptive & Exploratory Data Analyses  

> [!note] Variability Tells you how spread out values are  
> **Range**: highest score - lowest score  
> **Interquartile Range (IQR)**: 75th percentile - 25th percentile  
> **Variance**: measures how close the values in a distribution are to the middle of the middle of the distribution  
> - average squared difference of the scores from the mean  
> $$s^2=\sum(x_{i}-\bar{x})^2/(n-1)$$  
> **Standard deviation (SD)**: square-root of the variance  

# Why Central Tendency doesn't tell the whole story  

> [!note] Anscomb's Quartet  
> The same summary statistics can be for wildly different data  

> [!note] Exploratory  
> The goal is to find unknown relationships between the variables you have measured in your data set. Exploratory analysis is open ended and designed to verify expected or find unexpected relationships between measurements.  

> [!note] Why Exploratory Data Analysis  
> - Summarize data - basic stats  
> - Understand basic properties  
> - Discover patterns  
> - Suggest modeling strategies  
> - Check assumptions (sanity checks)  
> - Communicate results (present the data)  
> and if you don't, you'll regret it  

> [!note] How to EDA  
> - Look for missing values  
> - Look for outlier values  
> - Calculate numerical summaries  
> - Generate plots to explore relationships  
> - Use tables to explore relationships  
> - Search for patterns (i.e. linear vs nonlinear)  
> - If necessary, transform variables  

## EDA Approaches to Get a Feel for the Data  

> [!note] Univariate  
> understanding one variable  
> i.e. histogram, densityplot, barplot  

> [!note] Bivariate  
> understanding relationship between 2 variables  
> i.e. boxplot, scatterplot, grouped barplot  

> [!note] Multivariate  
> projecting high-D data into lower-D space  
> i.e. PCA, ICA, clustering  

## Types of Variables within EDA  

> [!note] Explanatory (independent) variable  
> It explains variations in the response variable, this is the variable a research would change  

> [!note] Response (dependent) variable  
> This is either a predicted value, or a value explained by the explanatory variable. This is the measured outcome in an experiment.  

> [!note] General approach to using zip codes  
> 1. Map zip codes to latitude and longitude  
> 2. Count how many people fall into each zip code  
> 3. Plot each place on a map  

> [!note] When NOT to do EDA  
> - To identify samples that you can remove from your study after you've already analyzed all of your data  
> - After running a statistical test and seeing that your p-value is 0.054  
> - After completing an analysis and getting an answer you don't like  
> - To improve the correlation between two variables  
> EDA is NOT a tool to get your data analysis to give you the results you want.  

> [!note] EDA (John Tukey)  
> Focuses on:  
> - understanding the data's underlying structure  
> - develop intuition about the data set  
> - consider how the data were collected (to aid in cleaning)  
> - decide how to further investigate with more formal statistical methods  

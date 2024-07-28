---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/COGS_9"
date:
- 2024-02-21
---
Source: https://drive.google.com/file/d/14-xuR8p5mXivM52VjypE2J2AixCDuf02/view  

> [!definition] p-value  
> The probability of getting the observed results (or results more extreme) by chance alone  

> [!note] Regression  
> Does change in one variable mean change in another?  
> i.e. simple regression, multiple regression  

> [!note] Linear Regression  
> best-fitting line is a **model** of the data  
> - can be used to determine whether a change in one variable is related to the change in the other variable  
> - the magnitude of the relationship is measured by the slope of the line (referred to as the model's **effect size**)  

> [!definition] Models  
> Mathematical equations generated to *represent* the real life situation  

"All models are **wrong**, but some are **useful.** - George Box  

> [!note] Correlation  
> Measures the strength of the linear relationship between two variables  

> [!note] Effect Size ($\beta$)  
> can be estimated using the slope of the line  

> [!note] Standard Error  
> The closer the points are to the regression line, the less uncertain we are in our estimate.  

P-value takes into account effect size ($\beta$) and the standard error  

> [!note] Assumptions of linear regression  
> 1. Linear relationship  
> 2. Multivariate normality  
> 3. No multicollinearity  
> 4. No autocorrelation  
> 5. Homoscedasticity  

> [!note] Multicollinearity  
> Linear regression assumes no multicollinearity. **Multicollinearity** occurs when the independent variables (in multiple linear regression) are too highly correlated with each other.  

> [!note] Autocorrelation  
> Autocorrelation occurs when the observations are *not* independent of one another (i.e. stock prices)  

> [!note] Homoscedastic  
> Points are relatively equidistant from the line of best fit at all points on the line  

## p-hacking  

> [!note] Many forms of p-hacking  
> - Using a subset of data  
> - Not adjusting for, or reporting multiple 'testing'  
> - Trying different tests with the same hypothesis  
> - Experimenting with your data during model fitting  
> - Inclusionary/Exclusionary protocols for data, i.e. outliers, definitions e.g. "college students", or "developing nations", etc.  
> - Optional stopping of data collection based on results thus far  
> - Changing your alpha values on the fly  
> - Rounding your p-values arbitrarily, e.g. 0.0558 $\to$ 0.05  

## Confounding  

Variable1 $\to$ Confounder $\leftarrow$ Variable2  

You can plan ahead to avoid confounding and/or include confounders in your models to account for their role on the outcome variable.  
Ignoring confounders will lead you to draw incorrect conclusions from your analyses.  

# Machine Learning  

> [!note] Predictive Machine Learning  
> Apply machine learning techniques to data you have currently to generate a model that will be able to make a prediction on future data  

> [!note] What is machine learning?  
> "Machine Learning (ML) is a fascinating field of artificial intelligence (AI) research and practice where we investigate how computer agents can improve their perception, cognition, and action with experience. Machine learning is about **machines improving from data, knowledge, experience, and interaction.**"  
> - Manuela Veloso, Head of ML at Carnegie Mellon  

> [!note] Software Engineering vs. ML Systems  
> Data/Input, Program $\to$ Computation $\to$ Output/Result  
> Data/Input, Output Result $\to$ Computation $\to$ Program  

ML is the field of study that gives computers the ability to learn without being explicity programmed. - Arthur Samuel (1959)  

Machine learning approaches use data to make predictions in the future  

## Three Main Machine Learning Generalizations  

> [!note] Supervised Learning  
> - Labeled data  
> - Make predictions  
> - Classification or Regression!  

> [!note] Unsupervised Learning  
> - Unlabeled data  
> - Find structure  
> - Reduce dimensions  

> [!note] Reinforcement Learning  
> - Learn a set of actions  
> - Reward feedback system  
> - Agent explores a world  

> [!note] Two Types of Supervised Learning  
> Predicting a Continuous Value  
> Predicted a Class  

> [!note] What is Labeled Data?  
> Labeled images vs. unlabeled images  
> Labeled column vs. unlabeled column  

> [!note] Why does the label matter?  
> Supervised Approach  
> - Train on labels  
> - Predict labels  
> Unsupervised approach  
> - Predict groups  

> [!note] Machine learning in the real world  
> - Classification: Spam Filter  
> - Classification: Image Recognition  
> - Regression: Electricity Demand  
> - Simple ML System  
>   - Historical data  
>   - Training Data  
>   - \+ Code  
>   - Train a model  
>   - Win!  

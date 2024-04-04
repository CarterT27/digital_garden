---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/DSC_40A"
date:
- 2024-04-02
---
Source: https://dsc40a.com/resources/lectures/lec01/lec01-blank.pdf  

# Introduction to Modeling  

## What is this class about?  

**Theoretical Foundations** of Data Science I  
Mathematical Foundations of Machine Learning  

**Why** do we need to study theoretical foundations?  
To understand and improve the tools we use.  

Machine learning is about **automatically learning patterns from data.**  
Humans are good at understanding handwriting - but how do we get computers to understand handwriting?  

https://dsc40a.com  
https://practice.dsc40a.com  

> [!note] Commute time example  
> Goal: Predict your commute time.  
> That is, predict how long it'll take to get to school.  
> How can we do this? $\to$ Learn from data  
> What will we need to assume? $\to$ Data in the future looks like data from the past  

A **model** is a set of assumptions about how data (plural) were generated.  
"datum" singular  
"All models are wrong but some are useful"  

> [!note] Possible Models Of Commuting Time  
> - Simple linear regression model - Assumes number of minutes it takes for you to get to school is a linear function of the time that you leave home.  
> - Constant model - Assumes all commute times are constant no matter what time you leave during the day.  

> [!note] Notation  
> $x$: "input", "independent variable", or "feature"  
> $y$: "response", "dependent variable", or "target"  
> **We use $x$ to predict $y$.**  
> The $i$th observation is denoted $(x_i,y_i)$.  

> [!definition] Hypothesis functions  
> A **hypothesis function**, $H$, takes in an $x$ as an input and returns a predicted $y$.  

> [!definition] Parameters  
> **Parameters** define the relationship between the input and output of a hypothesis function.  

The constant model, $H(x)=h$, has one parameter: $h$.  
- Use $H$ to make predictions (i.e. hypothesis model)  

The simple linear regression model, $H(x)=w_0+w_1 x$, has two parameters: $w_0$ and $w_1$.  
- Fancy $y=mx+b$  
- $w_0$ intercept  
- $w_1$ slope  
- Change parameters: change how predictions are made  

## The constant model  

Where should we draw the horizontal line?  

Transitioning from scatter plot to histogram  
- Horizontal line to vertical line  

> [!note] A concrete example  
> Smaller dataset of just five historical commute times in minutes. How can you come up with a prediction for your future commute time?  
> Possible Strategies: Average, Median, Midrange  

> [!definition] Summary Statistics  
> Summarize a collection of numbers with a single number  

## The cost of making predictions  

> [!definition] Loss function  
> A loss function quantifies how bad a prediction is for a single data point.  
> - If our prediction is **close** to the actual value, we should have a **low** loss.  
> - If our prediction is **far** from the actual value, we should have **high** loss.  
>  
> A good starting point is error, which is the difference between **actual** and **predicted** values.  
> $$e_i=y_i-H(x_i)$$  
> Suppose my commute actually takes 80 minutes.  
> - If I predict 75 minutes: error: $80-75=5$  
> - If I predict 72 minutes: error: $80-72=8$  
> - If I predict 100 minutes: error: $80-100=-20$  
>  
> Issue: Some errors are negative, others are positive  

> [!note] Squared loss  
> One loss function is squared loss, $L_{sq}$, which computes (actual - predicted)$^2$.  
> $$L_{sq}(y_i,H(x_i))=(y_i-H(x_i))^2$$  
> Note that for the constant model $H(x_i)=h$, so we can simplify this to:  
> $$L_{sq}(y_i,h)=(y_i-h)^2$$  
> Note: $(y_i-h)^2=(h-y_i)^2$  
> Squared loss is note the only loss function that exists. It is popular because it is **differentiable**. Absolute loss, another loss function, is **not** differentiable.  

> [!note] A concrete example, revisited  
> Suppose we predict the median, $h=85$. What is the squared lsos of $85$ for each data point?  
> $y_1=72\to(72-85)^2=169$  
> $y_2=90\to(90-85)^2=25$  
> $y_3=61\to(61-85)^2=576$  
> $y_4=85\to(85-85)^2=0$  
> $y_5=92\to(92-85)^2=49$  
> Goal: Find a single number that describes the loss for the prediction $h=85$ on my entire dataset  

> [!note] Averaging squared losses  
> We'd like a single number that describes the quality of our predictions across our entire dataset. One way to compute this is as the **average of the squared losses.**  
> - For the median, $h=85$:  
> $\frac{1}{5}((72-85)^2+(90-85)^2+(61-85)^2+(85-85)^2_(92-85)^2)=163.8$  
> - For the mean, $h=80$:  
> $\frac{1}{5}((72-80)^2+(90-80)^2+(61-80)^2+(85-80)^2_(92-80)^2)=138.8$  
>  
> 80 is the better prediction, since its average squared loss is **lower**.  

$L_{sq}$: loss for one data point  
$R_{sq}$: average loss for all data points  

> [!note] Mean squared error  
> L: loss for one data point  
> R: average loss over all data points  
> - Another term for **average squared loss** is **mean squared error** (MSE).  
> - The mean squared error on our smaller dataset for any prediction $h$ is of the form:  
> $$R_{sq}(h)=\frac{1}{5}((72-h)^2+(90-h)^2+(61-h)^2+(85-h)^2+(92-h)^2)$$  
> $R$ stands for "risk", as in "empirical risk."  
> - For example, if we predict $h=100$, then:  
> $$R_{sq}(100)=\frac{1}{5}((72-100)^2+(90-100)^2+(61-100)^2+(85-100)^2+(92-100)^2)=538.8$$  
> - We can pick any $h$ as a prediction, but the smaller $R_{sq}(H)$ is, the better $h$ is  

> [!note] Visualizing mean squared error  
> $$R_{sq}(h)=\frac{1}{5}((72-h)^2+(90-h)^2+(61-h)^2+(85-h)^2+(92-h)^2)$$  
> $(90-h)^2$ is a parabola centered at $90$  
> We want to minimize MSE  

> [!note] Mean squared error, in general  
> - Suppose we colelct $n$ commute times, $y_1,y_2,\dots,y_n$.  
> - The mean squared error of the prediction $h$ is:  
> $$\frac{1}{n}[(y_1-h)^2+(y_2-h)^2+\dots+(y_n-h)^2]$$  
> - Or, using **summation notation**:  
> $$R_{sq}(h)=\frac{1}{n}\sum_{i=1}^n(y-h)^2$$  
> ```Python  
> total = 0  
> for i in range(1, n+1):  
>   total += (y[i]-h)**2  
> total = total / n  
> ```  

> [!note] The best prediction  
> $$R_{sq}(h)=\frac{1}{n}\sum_{i=1}^n(y_i-h)^2$$  
> - We want the **best** prediction, $h^*$.  
> - The smaller $R_{sq}(h)$ is, the better $h$ is.  
> - **Goal**: Find the $h$ that minimizes $R_{sq}(h)$.  
>   The resulting $h$ will be called $h^*$.  
> - How do we find $h^*$?  

> [!note] Summary  
> - We started with the abstract problem:  
> > Given historical commute times, predict your future commute time.  
> - We've turned it into a formal optimization problem:  
> > Find the prediction $h^*$ that has the smallest mean squared error $R_{sq}(h)$ on the data.  
> - Implicitly, we introduced a three-step modeling process that we'll keep revisiting:  
>   1. Choose a model.  
>   2. Choose a loss function.  
>   3. Minimize average loss, $R$.  
> - Next time: We'll solve this optimization problem by-hand  

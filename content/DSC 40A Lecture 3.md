---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/DSC_40A"
date:
- 2024-04-09
---
Source: https://dsc40a.com/resources/lectures/lec03/lec03-blank.pdf  

# Comparing Loss Functions  

---  

## Recap: Empirical risk minimization  

### Goal  

We had one goal in Lecture 2: given a dataset of values from the past, **find the best constant prediction** to make.  
$$y_1=72,y_2=90,y_3=61,y_4=85,y_5=92$$  
**Key idea:** Different definitions of "best" give us different "best predictions."  
median, mean are both the **best**, under different conditions.  

### The modeling recipe  

In Lecture 2, we made two full passes through our "modeling recipe."  
1. Choose a model.  
$H(x)=h$ constant model  
2. Choose a loss function.  
$L_{sq}(y_i,h)=(y_i-h)^2$, $L_{abs}(y_i,h)=\vert y_i-h\vert$  
3. Minimize average loss to find optimal model parameters.  
Mean Squared Error$=R_{sq}(h)=\frac{1}{n}\sum_{i=1}^n(y_i-h)^2\implies h^*=Mean(y_1,y_2,\dots,y_n)$  
Mean Absolute Error$=R_{abs}(h)=\frac{1}{n}\sum_{i=1}^n\vert y_i-h\vert\implies h^*=Median(y_1,y_2,\dots,y_n)$  

### Empirical risk minimization  

- The formal name for the process of minimizing average loss is **empirical risk minimization**.  
- Another name for "average loss" is **empirical risk**.  
- When we use the squared loss function $L_{sq}(y_i,h)=(y_i-h)^2$, the corresponding empirical risk is mean squared error.  
$$R_{sq}(h)=\frac{1}{n}\sum_{i=1}^n(y_i-h)^2$$  
- When we use the absolute loss function $L_{abs}(y_i,h)=\vert y_i-h\vert$, the corresponding empirical risk is mean absolute error.  
$$R_{abs}(h)=\frac{1}{n}\sum_{i=1}^n\vert y_i-h\vert$$  

### Empirical risk minimization, in general  

**Key idea**: If $L(y_i,h)$ is **any** loss function, the corresponding empirical risk is  
$$R(h)=\frac{1}{n}\sum_{i=1}^n L(y_i,h)$$  

---  

## Choosing a Loss Function  

### Now what?  

- We know that, for the consatnt model $H(x)=h$, the **mean** minimizes mean **squared** error.  
- We also know that, for the constant model $H(x)=h$, the **median** minimizes mean **absolute** error.  
- **How does our choice of loss function impact the resulting optimal prediction?**  

### Comparing the mean and median  

- Consider our example dataset of 5 commute times.  
$$y_1=72,y_2=90,y_3=61,y_4=85,y_5=92$$  
- As of now, the **median is 85** and the **mean is 80**.  
- What if we add 200 to the largest commute time, 92?  
$$y_1=72,y_2=90,y_3=61,y_4=85,y_5=292$$  
- Now, the median is still 85 but the mean is 120  
- **Key idea**: The mean is quite **sensitive** to outliers.  

### Outliers  

Below, $\vert y_4-h\vert$ is 10 times as big as $\vert y_3-h\vert$, but $(y_4-h)^2$ is 100 times $(y_3-h)^2$.  
The result is that the **mean** is "pulled" in the direction of outliers, relative to the **median**.  
As a result, we say the **median** is **robust** to outliers. But the **mean** was easier to solve for.  

### Balance points  

Both the **mean** and **median** are "balance points" in the distribution.  
- The **mean** is the point where $\sum_{i=1}^n(y_i-h)=0$.  
$$\sum_{y_i<h}^n\vert y_i-h\vert=\sum_{y_i>h}^n\vert y_i-h\vert$$  
- The **median** is the point where $\#(y_i<h)=\#(y_i>h)$.  

### Why stop at squared loss?  

| Empirical Risk, $R(h)$ | Derivative of Empirical Risk, $\frac{d}{dh}R(h)$ | Minimizer |  
| --- | --- | --- |  
| $\frac{1}{n}\sum_{i=1}^n \vert y_i-h\vert$ | $\frac{1}{n}\left(\sum_{y_i<h}1-\sum_{y_i>h}1\right)$ | median |  
| $\frac{1}{n}\sum_{i=1}^n (y_i-h)^2$ | $\frac{-2}{n}\sum_{i=1}^n (y_i-h)$ | mean |  
| $\frac{1}{n}\sum_{i=1}^n \vert y_i-h \vert^3$ | | ??? |  
| $\frac{1}{n}\sum_{i=1}^n (y_i-h)^4$ |  | ??? |  
| $\frac{1}{n}\sum_{i=1}^n (y_i-h)^{100}$ |  | ??? |  
| ... | ... | ... |  

### Generalized $L_p$ loss  

> [!note] "p-norm of a vector"  
> $\Vert x \Vert_2 = \sqrt{x_1^2+x_2^2+\dots+x_n^2}$  
> $\Vert x \Vert_3 = \root{3}\of{x_1^2+x_2^2+\dots+x_n^2}$  
> $\Vert x \Vert_{100} = \root{100}\of{x_1^2+x_2^2+\dots+x_n^2}$  
> $\vdots$  
> $\Vert x \Vert_\infty = max(x_1,x_2,\dots,x_n)$  

For any $p\geq1$, define the $L_p$ loss as follows:  
$$L_p(y_i,h)=\vert y_i-h\vert^p$$  
The corresponding empirical risk is:  
$$R_p(h)=\frac{1}{n}\sum_{i=1}^n \vert y_i-h\vert^p$$  

### What value does $h^*$ approach as $p\to\infty$?  

The $x$-axis is $p$.  
The $y$-axis is $h^*$, the optimal constant prediction for $L_p$ loss:  
$$h^*=argmin_h \frac{1}{n}\sum_{i=1}^n \vert y_i-h\vert^p$$  

### The *midrange* minimizes average $L_\infty$ loss!  

On the previous slide, we saw that as $p\to\infty$, the minimizer of mean $L_p$ loss approached **the midpont of the minimum and maximum values in the dataset**, or the **midrange**.  
- As $p\to\infty,R_p(h)=\frac{1}{n}\sum_{i=1}^n \vert y_i-h\vert^p$ minimizes **the "worst case" distance from any data point"**. (Read more [here](https://mathworld.wolfram.com/L-Infinity-Norm.html))  
- If your measure of "good" is "not far from any one data point", then the midrange is the best prediction.  

mean = 5, worst case distance = $\vert14-5\vert=9$  
median = 2.5, worst case distance = $\vert14-2.5\vert=11.5$  
midrange = 7.5, worst case distance = $\vert14.7.5\vert=6.5$  

### Another example $0-1$ loss  

Consider, for example, the **0-1 loss**:  
$$L_{0,1}(y_i,h)=\begin{cases}0,y_i=h\\1,y_i\neq h\end{cases}$$  
The corresponding empirical risk is:  
$$R_{0,1}(h)=\frac{1}{n}\sum_{i=1}^n L_{0,1}(y_i-h)$$  
Proportion of points NOT equal to $h$  

### Minimizing empirical risk for 0-1 loss  

$$R_{0,1}(h)=\frac{1}{n}\sum_{i=1}^n\begin{cases}0,y_i=h\\1,y_i\neq h\end{cases}$$  
= proportion of points NOT equal to $h$  
Minimized when $y_i=h$ as often as possible  
$\implies$ set $h^*=Mode(y_1,y_2,\dots,y_n)$  
most common value  
$\Rightarrow$ not usually unique!  

### Summary: Choosing a loss function  

**Key idea**: Different lsos functions lead to different best predictions, $h^*$!  

| Loss | Minimizer | Always Unique? | Robust to Outliers? | Differentiable? |  
| --- | --- | --- | --- | --- |  
| $L_{sq}$ | mean | yes | no | yes |  
| $L_{abs}$ | median | no | yes | no |  
| $L_\infty$ | midrange | yes | no | no |  
| $L_{0,1}$ | mode | no | yes | no |  

The optimal predictions, $h^*$, are all **summary statistics** that measure the **center** fo the dataset in different ways.  

---  

## Center and Spread  

### What does it mean?  

- The general form of empirical risk, for any loss function $L(y_i,h)$, is:  
$$R(h)=\frac{1}{n}\sum_{i=1}^n L(y_i,h)$$  
- As we just saw, the input $h^*$ that minimizes $R(h)$ is some measure of the **center** of the dataset.  
- The minimum output, $R(h^*)$, represents some measure of the **spread**, or variation, in the dataset.  

### Squared loss  

- The empirical risk for squared loss, i.e. mean squared error, is:  
$$R_{sq}(h)=\frac{1}{n}\sum_{i=1}^n (y_i-h)^2$$  
- $R_{sq}(h)$ is minimized when $h^*=Mean(y_1,y_2,\dots,y_n)$  
- Therefore, the minimum value of $R_{sq}(h)$ is:  
$$R_{sq}(h^*)=R_{sq}(Mean(y_1,y_2,\dots,y_n))$$  
$$=\frac{1}{n}\sum_{i=1}^n(y_i-Mean(y_1,y_2,\dots,y_n))^2$$  

### Variance  

- The minimum value of $R_{sq}(h)$ is the mean squared deviation from the mean, more commonly known as the **variance**.  
$$Variance(y_1,y_2,\dots,y_n)=\frac{1}{n}\sum_{i=1}^n(y_i-Mean(y_1,y_2,\dots,y_n))^2$$  
TODO  
- It measures the squared  

### Absolute loss  

- The empirical risk for absolute loss, i.e. mean absolute error, is:  
TODO  
- $R_{abs}(h)$ is minimized when $h^*=Median(y_1,y_2,\dots,y_n)$  
- Therefore, the minimum value of $R_{abs}(h)$ is:  
$$R_{abs}(h^*)=\frac{1}{n}\sum_{i=1}^n\vert y_i-h\vert$$  
$$=R_{abs}(h)=\frac{1}{n}\sum_{i=1}^n \vert y_i-Median(y_1,y_2,\dots,y_n)\vert$$  

### Mean absolute deviation from the median  

- The minimum value of $R_{abs}(h)$ is the **mean absolute deviation from the median.**  
MAD from the median($y_1,y_2,\dots,y_n)=\frac{1}{n}\sum_{i=1}^n \vert y_i$-Median($y_1,y_2,\dots,y_n)\vert$  
- It measures how far each data point is from the median, on average.  
- **Example**: What is the MAD from the median in the dataset 2,3,3,4,5?  
$1+0+0+1=\frac{4}{5}$  

### Summary of center and spread  

- Different loss functions $L(y_i,h)$ lead to different empirical risk functions $R(h)$, which are minimized at various measures of **center**.  
- The minimum values of empirical risk, $R(h^*)$ are various measures of **spread**.  
- There are many different ways to measure both center and spread; these are sometimes called **descriptive statistics**.  

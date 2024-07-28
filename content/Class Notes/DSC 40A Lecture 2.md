---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/DSC_40A"
date:
- 2024-04-04
---
Source: https://dsc40a.com/resources/lectures/lec02/lec02-filled.pdf  

# Empirical Risk Minimization  

## Overview  

- We started by introducing the idea of a hypothesis function, $H(x)$.  
- We looked at two possible models:  
- The constant model, $H(x)=h$.  
- The simple linear regression model, $H(x)=w_0+w_1x$.  
- We decided to find the **best constant prediction** to use for predicting commute times, in minutes.  

## Mean squared error  

- Let's suppose we have just a smaller dataset of just five historical commute times in minutes.  
$y_1=72,y_2=90,y_3=61,y_4=85,y_5=92$  
- The **mean squared error** of the constant prediction $h$ is:  
$R_{sq}(h)=\frac{1}{5}((72-h)^2+(90-h)^2+(61-h)^2+(85-h)^2+(92-h)^2)$  
- For example, if we predict $h=100$, then:  
$R_{sq}(100)=\frac{1}{5}((72-100)^2+(90-100)^2+(61-100)^2+(85-100)^2+(92-100)^2)=538.8$  
- **We can pick any $h$ as a prediction, but the smaller $R_{sq}(h)$ is, the better $h$ is!**  

## The best prediction  

- Suppose we collect $n$ commute times, $y_1,y_2,\dots,y_n$.  
- The mean squared error of the prediction $h$ is:  
$$R_{sq}(h)=\frac{1}{n}\sum_{i=1}^n(y_i-h)^2$$  
- We want the best prediction, $h^*$.  
- The smaller $R_{sq}(h)$ is, the better $h$ is.  
- **Goal**: Find the $h$ that minimizes $R_{sq}(h)$.  
The resulting $h$ will be called $h^*$.  
- **How do we find $h^*$?** $\to$ using calculus!  

# Minimizing mean squared error  

## Minimizing using calculus  

We'd like to minimize:  
$$R_{sq}(h)=\frac{1}{n}\sum_{i=1}^n(y_i-h)^2$$  
In order to minimize $R_{sq}(h)$, we:  
1. take its derivative with respect to $h$,  
2. set it equal to 0,  
3. solve for the resulting $h^*$, and  
4. perform a second derivative test to ensure that we found a minimum  

## Step 0: The derivative of $(y_i-h)^2$  

- Remeber from calculus that:  
- if $c(x)=a(x)+b(x)$, then  
- $\frac{d}{dx}c(x)=\frac{d}{dx}a(x)+\frac{d}{dx}b(x)$.  
- This is relevant because $R_{sq}(h)=\frac{1}{n}=\sum_{i=1}^n(y_i-h)^2$ involves the sum of $n$ individual terms, each of which involve $h$.  
- So, to take the derivative of $R_{sq}(h)$, we'll first need to find the derivative of $(y_i-h)^2$.  
$\frac{d}{dh}(y_i-h)^2=2(y_i-h)\frac{d}{dh}(y_i-h)$  
$=2(y_i-h)(-1)$  
$=-2(y_i-h)=2(h-y_i)$  

## Step 1: The derivative of $R_{sq}(h)$  

$$\frac{d}{dh}R_{sq}(h)=\frac{d}{dh}\left(\frac{1}{n}\sum_{i=1}^n(y_i-h)^2\right)$$  
$=\frac{1}{n}\sum_{i=1}^n(y_i-h)^2$  
$=\frac{1}{n}\sum_{i=1}^n(-2)(y_i-h)$  
$=\frac{-2}{n}\sum_{i=1}^n(y_i-h)$  

## Step 2 and 3: Set to 0 and solve for the minimzer, $h^*$  
$\frac{d}{dh}R_{sq}(h)=\frac{-2}{n}\sum_{i=1}^n(y_i-h)=0$ $\Leftarrow$ multiply both sides by $\left(\frac{-n}{2}\right)$  
$\sum_{i=1}^nh=h+h+\dots+h$ ($n$ times) $=nh$  
$\sum_{i=1}^n(y_i-h)=0$  
$\sum_{i=1}^ny_i-\sum_{i=1}^nh=0$  
$\sum_{i=1}^ny_i-nh=0$  
$\sum_{i=1}^ny_i=nh$  
$h^*=\frac{\sum_{i=1}^ny_i}{n}$  
$=Mean(y_1,y_2,\dots,y_n)$  

## Step 4: Second derivative test  

We already saw that $R_{sq}(h)$ is **convex** i.e. that it opens upwards, so the $h^*$ we found must be a minimum, not a maximum.  
$$R_{sq}(h)=\frac{1}{n}\sum_{i=1}^n(y_i-h)^2$$  
$$\frac{d}{dh}R_{sq}(h)=\frac{-2}{n}\sum_{i=1}^n(y_i-h)$$  
$$\frac{d^2}{dh^2}R_{sq}(h)=\frac{-2}{n}\sum_{i=1}^n(-1)=\frac{-2}{n}(-n)=2>0$$  
So, $R_{sq}(h)$ opens upwards (convex), and we found a minimizer!  

## The mean minimzes mean squared error!  

- The problem we set out to solve was, find the $h^*$ that minimizes:  
$$R_{sq}(h)=\frac{1}{n}\sum_{i=1}^n(y_i-h)^2$$  
- The answer is:  
$$h^*=Mean(y_1,y_2,\dots,y_n)=\bar{y}$$  
- The **best constant prediction**, in terms of mean squared error, is always the **mean**.  
- We call $h^*$ our **optimal model parameter**, for when we use:  
- the constant model, $H(x)=h$, and  
- the squared loss function, $L_{sq}(y_i,h)=(y_i-h)^2$.  

## Aside: Notation  

Another way of writing  
$$h^*\text{ is the value of }h\text{ that minimizes }\frac{1}{n}\sum_{i=1}^n(y_i-h)^2$$  
is  
$$h^*=\text{argmin}_{h}\left(\frac{1}{n}\sum_{i=1}^n(y_i-h)^2\right)$$  
$h^*$ is the solution to an **optimization problem**.  

## The modeling recipe  

We've implicitly introduced a three-step process for finding optimal model parameters (like $h^*$) that we can use for making predictions.  
1. Choose a model.  
$H(x)=h$  
2. Choose a loss function.  
$L_{sq}(y_i,h)=(y_i-h)^2$  
3. Minimize average loss to find optimal model parameters.  
$h^*=Mean(y_1,y_2,\dots,y_n)$  

# Another loss function  

## Another loss function  

- Last lecture, we started by computing the **error** for each of our **predictions**, but ran into the issue that some errors were positive and some were negative.  
$$e_i=y_i-H(x_i)$$  
- THe solution was to **square** the errors, so that all are non-negative. The resulting loss function is called **squared loss**.  
$$L_{sq}(y_i,H(x_i))=(y_i-H(x_i))^2$$  
- Another loss function, which also measures how far $H(x_i)$ is from $y_i$, is **absolute loss**.  
$$L_{abs}(y_i,H(x_i))=\vert y_i-H(x_i)\vert$$  

## Squared loss vs. absolute loss  

For the constant model, $H(x_i)=h$, so we can simplify our loss functions as follows:  
- Squared loss: $L_{sq}(y_i,h)=(y_i-h)^2$.  
- Absolute loss: $L_{abs}(y_i,h)=\vert y_i-h\vert$.  
Consider again, our example **dataset of five commute times**, and the **prediction $h=80$.  
$$y_1=72,y_2=90,y_3=61,y_4=85,y_5=92$$  
- When we use squared loss, $h^*$ is the point at which the average squared loss is minimized.  
- When we use absolute loss, $h^*$ is the point at which the average absolute loss is minimized.  

## Mean absolute error  
- Suppose we collect $n$ commute times, $y_1,y_2,\dots,y_n$.  
- The **average absolute loss**, or **mean absolute error (MAE)**, of the prediction $h$ is:  
$$R_{abs}(h)=\frac{1}{n}\sum_{i=1}^n\vert y_i-h\vert$$  
- We'd like to find the best prediction, $h^*$.  
- Previously, we used calculus to find the optimal model parameter $h^*$ that minimized $R_{sq}$ - that is, when using squared loss.  
- Can we use calculus to minimize $R_{abs}(h)$, too?  

# Minimizing mean absolute error  

## Minimizing using calculus, again  

We'd like to minimize:  
$$R_{abs}(h)=\frac{1}{n}\sum_{i=1}^n\vert y_i-h\vert$$  
In order to minimize $R_{abs}(h)$, we:  
1. take its derivative with respect to $h$,  
2. set it equal to 0,  
3. solve for the resulting $h^*$, and  
4. perform a second derivative test to ensure we found a minimum.  

## Step 0: The "derivative" of $\vert y_i-h\vert$  

Remember that $\vert x\vert$ is a **piecewise linear** function of $x$:  
$$\vert x\vert=\begin{cases}x, x>0\\0, x=0\\-x, x<0\end{cases}$$  
So, $\vert y_i-h\vert$ is also a piecewise linear function of $h$:  
$$\vert y_i-h\vert=\begin{cases}y_i-h, h<y_i\\0, y_i=h\\h-y_i, h>y_i\end{cases}$$  
What is $\frac{d}{dh}\vert y_i-h\vert$?  
$\frac{d}{dh}\vert y_i-h\vert=\begin{cases}-1, h<y_i\\undefined, y_i=h\\+1, h>y_i\end{cases}$  

## Step 1: The "derivative" of $R_{abs}(h)$  

$$\frac{d}{dh}R_{abs}(h)=\frac{d}{dh}\left(\frac{1}{n}\sum_{i=1}^n\vert y_i-h\vert\right)$$  
$=\frac{1}{n}\sum_{i=1}^n\frac{d}{dh}\vert y_i-h\vert$  
a sum of a bunch of +1s and -1s!  
we +1 whenever $h>y_i$, and  
we -1 whenever $h<y_i$  
$=\frac{1}{n}\left[^\#(h>y_i)-^\#(h<y_i)\right]$ slope of mean absolute error (MAE)  

## Step 2 and 3: Set to 0 and solve for the minimizer, $h^*$  

$\frac{d}{dh}R_{abs}(h)=\frac{1}{n}\left[^\#(h>y_i)-^\#(h<y_i)\right]=0$ multiply both sides by $n$  
$\Rightarrow ^\#(h>y_i)=^\#(h<y_i)$  
The $h^*$ that minimizes mean absolute error is the one where  
\# points to the left of h = \# points to the right of h $\Rightarrow$ median!  

## The median minimizes mean absolute error!  

- The new problem we set out to solve was find the $h^*$ that minimizes:  
$$R_{abs}(h)=\frac{1}{n}\sum_{i=1}^n\vert y_i-h\vert$$  
- The answer is:  
$$h^*=Median(y_1,y_2,\dots,y_n)$$  
- This is because the median has an equal number of data points to the left of it and to the right of it.  
- To make a bit more sense of this result, let's graph $R_{abs}(h)$.  

## Visualizing mean absolute error  

Consider, again, our example dataset of five commute times.  
$$72,90,61,85,92$$  
Where are the "bends" in the graph of $R_{abs}(h)$ - that is, where does its slope change?  
The bends are at data points!  

## Visualizing mean absolute error, with an even number of points  

What if we add a sixth data point?  
$$72,90,61,85,92,75$$  
Is there a unique $h^*$?  
No, $h^*$ is not unique!  
Any value in the range $75\leq h^*\leq85$ minimizes mean absolute error!  

Convex functions - the critical point is guaranteed to be a minimum  

## The median minimizes mean absolute error!  

- The new problem we set out to solve was, find the $h^*$ that minimizes:  
$$R_{abs}(h)=\frac{1}{n}\sum_{i=1}^n\vert y_i-h\vert$$  
- The answer is:  
$$h^*=Median(y_1,y_2,\dots,y_n)$$  
- The **best constant prediciton**, in terms of mean absolute error, is always the **median**.  
- When $n$ is odd, this answer is unique.  
- When $n$ is even, any number between the middle two data points (when sorted) also minimizes mean absolute error.  
- When $n$ is even, define the median to be the mean of the middle two data points.  

## The modeling recipe, again  

We've now made two full passes through our "modeling recipe."  
1. Choose a model  
$H(x)=h$  
2. Choose a loss function.  
$L_{sq}(y_i,h)=(y_i-h)^2$, $L_{abs}(y_i,h)=\vert y_i-h\vert$  
3. Minimize average loss to find optimal model parameters.  
$h^*=Mean(y_1,y_2,\dots,y_n)$, $h^*=Median(y_1,y_2,\dots,y_n)$  

## Empirical risk minimization  

- The formal name for the process of minimizing average loss is **empirical risk minimization**.  
- Another name for "average loss" is **empirical risk**.  
- When we use the squared loss function, $L_{sq}(y_i,h)=(y_i-h)^2$, the corresponding empirical risk is mean squared error:  
$$R_{sq}(h)=\frac{1}{n}\sum_{i=1}^n(y_i-h)^2$$  
- When we use the absolute loss function, $L_{abs}(y_i,h)=\vert y_i-h\vert$, the corresponding empirical risk is mean absolute error:  
$$R_{abs}(h)=\frac{1}{n}\sum_{i=1}^n\vert y_i-h\vert$$  

## Empirical risk minimization, in general  

**Key idea**: If $L(y_i,h)$ is **any** loss function, the corresponding empirical risk is:  
$$R(h)=\frac{1}{n}\sum_{i=1}^nL(y_i,h)$$  

## Summary, next time  

- $h^*=Mean(y_1,y_2,\dots,y_n)$ minimizes mean squared error, $R_{sq}(h)=\frac{1}{n}\sum_{i=1}^n(y_i-h)^2$.  
- $h^*=Median(y_1,y_2,\dots,y_n)$ minimizes mean absolute error, $R_{abs}(h)=\frac{1}{n}\sum_{i=1}^n\vert y_i-h\vert$.  
- $R_{sq}(h)$ and $R_{abs}(h)$ are examples of **empirical risk** - that is, average loss.  
- **Next time**: What's the relationship between the mean and median? What is the significance of $R_{sq}(h^*)$ and $R_{abs}(h^*)$?  

> [!question] Practice exam problem  
> Define the extreme mean (EM) of a dataset to be the average of its largest and smallest values. Let $f(x)=-3x+4$.  
> Show that for any dataset $x_1\leq x_2\leq\dots\leq x_n$,  
> $$EM(f(x_1),f(x_2),\dots,f(x_n))=f(EM(x_1,x_2,\dots,x_n))$$  

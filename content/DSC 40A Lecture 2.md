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

## The best prediction  

- Suppose we collect $n$ commute times, $y_1,y_2,\dots,y_n$.  
- The mean squared error of the prediction $h$ is:  
$$R_{sq}(h)=\frac{1}{n}\sum_{i=1}^n(y_i-h)^2$$  
- We want the best prediction, $h^*$.  
- The smaller $R_{sq}(h)$ is, the better $h$ is.  

## Minimizing using calculus  

We'd like to minimize:  
$$R_{sq}(h)=\frac{1}{n}\sum_{i=1}^n(y_i-h)^2$$  
In order to minimize $R_{sq}(h)$, we:  
1. take its derivative with respect to $h$,  
2. set it equal to 0,  
3. solve for the resulting $h^*$, and  
4. perform a second derivative test to ensure that we found a minimum  

## Step 0: The derivative of $(y_i-h)^2$  

## Step 1: The derivative of $R_{sq}(h)$  

$$\frac{d}{dh}R_{sq}(h)=\frac{d}{dh}\left(\frac{1}{n}\sum_{i=1}^n(y_i-h)^2\right)$$  

## Step 2 and 3: Set to 0 and solve for the minimzer, $h^*$  

## Step 4: Second derivative test  

$$R_{sq}(h)=\frac{1}{n}\sum_{i=1}^n(y_i-h)^2$$  
$$\frac{d}{dh}R_{sq}(h)=\frac{-2}{n}\sum_{i=1}^n(y_i-h)$$  
$$\frac{d^2}{dh^2}R_{sq}(h)=\frac{-2}{n}\sum_{i=1}^n(-1)=\frac{-2}{n}(-n)=2>0$$  
So, $R_{sq}(h)$ opens upwards (convex), and we found a minimum.  

## The mean minimzes mean squared error!  

- The problem we set out to solve was, find the $h^*$ that minimizes:  
$$R_{sq}(h)=\frac{1}{n}\sum_{i=1}^n(y_i-h)^2$$  
- The answer is:  
$$h^*=Mean(y_1,y_2,\dots,y_n)$$  

## Aside: Notation  

## The modeling recipe  

## Another loss function  

- Last lecture, we started by computing the **error** for each of our **predictions**, but ran into the issue that some errors were positive and some were negative.  
$$e_i=y_i-H(x_i)$$  
- THe solution was to **square** the errors, so that all are non-negative. The resulting loss function is called **squared loss**.  
$$L_{sq}(y_i,H(x_i))=(y_i-H(x_i))^2$$  
- Another loss function, which also measures how far $H(x_i)$ is from $y_i$, is **absolute loss**.  
$$L_{abs}(y_i,H(x_i))=\vert y_i-H(x_i)\vert$$  

## Squared loss vs. absolute loss  

## Mean absolute error  

## Minimizing using calculus, again  

## Step 0: The "derivative" of $\vert y_i-h\vert$  

## Step 1: The "derivative" of $R_{abs}(h)$  

$$\frac{d}{dh}R_{abs}(h)=\frac{d}{dh}\left(\frac{1}{n}\sum_{i=1}^n\vert y_i-h\vert\right)$$  
$=\frac{1}{n}\sum_{i=1}^n\frac{d}{dh}\vert y_i-h\vert$  
a sum of a bunch of +1s and -1s!  
we +1 whenever $h>y_i$, and  
we -1 whenever $h<y_i$  
$=\frac{1}{n}\left[^\#(h>y_i)-^\#(h<y_i)\right]$ slope of mean absolute error (MAE)  

## Step 2 and 3: Set to 0 and solve for the minimizer, $h^*$  

<!-- $\Rrightarrow$ -->  

## Visualizing mean absolute error  

## Visualizing mean absolute error, with an even number of points  

Convex functions - the critical point is guaranteed to be a minimum  

## The median minimizes mean absolute error!  

## The modeling recipe, again  

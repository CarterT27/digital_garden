---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/DSC_40A"
date:
- 2024-04-11
---
Source: https://dsc40a.com/resources/lectures/lec04/lec04-filled.pdf

# Simple Linear Regression  

---  

## Recap - Center and Spread  

### The relationship between $h^*$ and $R(h^*)$  

- Recall, for a general loss function $L$ and the constant model $H(x)=h$ empirical risk is of the form:
$$R(h)=\frac{1}{h}\sum_{i=1}^n L(y_i,h)$$  
- $h^*$, the value of $h$ that minimizes empirical risk, represents the **center** of the dataset in some way.
- $R(h^*)$, the smallest possible value of empirical risk, represents the **spread** of the dataset in some way.
- The specific center and spread depend on the choice of loss function.

### Examples  

When using **squared loss**:
- $h^* = \text{Mean}(y_1, y_2, ..., y_n)$.
- $R_\text{sq}(h^*) = \text{Variance}(y_1, y_2, ..., y_n)$.

When using **absolute loss**:
- $h^* = \text{Median}(y_1, y_2, ..., y_n)$.
- $R_\text{abs}(h^*) = \text{MAD from the median}$.

### 0-1 Loss  

- The empirical risk for the 0-1 loss is:
$$R_{0,1}(h) = \frac{1}{n} \sum_{i = 1}^n \begin{cases} 0 & y_i = h \\ 1 & y_i \neq h \end{cases}$$
- This is the proportion (between 0 and 1) of data points not equal to $h$.
- $R_{0,1}(h)$ is minimized when $h^* = \text{Mode}(y_1, y_2, ..., y_n)$.
- Therefore, $R_{0,1}(h^*)$ is the proportion of data points not equal to the mode.
- **Example**: What's the proportion of values not equal to the mode in the dataset $2, 3, 3, 4, 5$?
$\frac{3}{5}$

### A poor way to measure spread

- The minimum value of $R_{0,1}(h)$ is the proportion of data points not equal to the mode.
- A higher value means less of the data is clustered at the mode.
- Just as the mode is a very basic way of measuring the center of the data, $R_{0,1}(h^*)$ is a very basic and uninformative way of measuring spread.

### Summary of center and spread

- Different loss functions $L(y_i, h)$ lead to different empirical risk functions $R(h)$, which are minimized at various measures of **center**.
- The minimum values of empirical risk, $R(h^*)$, are various measures of **spread**.
    - larger values of spread $\to$ data is **more** spread out
- There are many different ways to measure both center and spread; these are sometimes called **descriptive statistics**.

---

## Simple linear regression

### What's next?

- In Lecture 1, we introduced the idea of a hypothesis function, $H(x)$.
- We've focused on finding the best **constant model**, $H(x) = h$.
- Now that we understand the modeling recipe, we can apply it to find the best **simple linear regression model**, $H(x) = w_0 + w_1 x$.
- This will allow us to make predictions that aren't all the same for every data point.

### Recap: Hypothesis functions and parameters  

A hypothesis function, $H$, takes in an $x$ as an input and returns a predicted $y$.  
**Parameters** define the relationship between the input and output of a hypothesis function.  

The simple linear regression model, $H(x)=w_0+w_1 x$, has two parameters: $w_0$ and $w_1$.  

### The modeling recipe  

1. Choose a model.  
Before: $H(x)=h$  
Now: $H(x)=w_0+w_1 x$  
2. Choose a loss function.  
$L_{sq}(y_i,H(x_i))=(y_i-H(x_i))^2$  
$L_{abs}(y_i,H(x_i))=\vert y_i - H(x_i)\vert$  
3. Minimize average loss to find optimal model parameters.  
$R_{sq}(H)=\frac{1}{n}\sum_{i=1}^n(y_i-H(x_i))^2$  
$R_{abs}(H)=\frac{1}{n}\sum_{i=1}^n\vert y_i - H(x_i)\vert$  

### Minimizing mean squared error for the simple linear model  

- We'll choose squared loss, since it's the easiest to minimize.  
- Our goall then, is to find the linear hypothesis function $H^*(x)$ that minimizes empirical risk:  
$$R_{sq}(H)=\frac{1}{n}\sum_{i=1}^n(y_i-H(x_i))^2$$  
- Since linear hypothesis functions are of the form $H(x)=w_0+w_1 x$, we can re-write $R_{sq}$ as a function of $w_0$ and $w_1$:  
$$R_{sq}(w_0,w_1)=\frac{1}{n}\sum_{i=1}^n(y_i-(w_0+w_1 x_i))^2$$  
- How do we find parameters $w_0^*$ and $w_1^*$ that minimize $R_{sq}(w_0,w_1)$?  

### Loss surface  

For the constant model, the graph of $R_{sq}(h)$ looked like a parabola.  
What does the graph of $R_{sq}(w_0,w_1)$ look like for the simple linear regression model? $\to$ bowl-looking "loss surface"  

---  

## Minimizing mean squared error for the simple linear model  

### Minimizing multivariate functions  

- Our goal is to find the parameters $w_0^*$ and $w_1^*$ that minimize mean squared error:  
$$R_{sq}(w_0,w_1)=\frac{1}{n}\sum_{i=1}^n(y_i-(w_0+w_1 x_i))^2$$  
- $R_{sq}$ is a function of two variables: $w_0$ and $w_1$.  
- To minimize a function of multiple variables:  
- Take partial derivatives with respect to each variable.  
- Set all partial derivatives to 0.  
- Solve the resulting system of equations.  
- Ensure that you've found a minimum, rather than a maximum or saddle point (using the second derivative test for multivariate functions).  

> [!question] **Example.** Find the point $(x,y,z)$ at which the following function is minimized. $f(x,y)=x^2-8x+y^2+6y-7$  
> $f_x=\frac{\partial f}{\partial x} = 2x-8 \to 2x-8=0 \Rightarrow x=4$  
> $f_y=\frac{\partial f}{\partial y} = 2y+6 \to 2y+6=0 \Rightarrow y=-3$  
> Minimized at $x=4,y=-3$  

### Minimizing mean squared error  

$$R_{sq}(w_0,w_1)=\frac{1}{n}\sum_{i=1}^n(y_i-(w_0+w_1 x_i))^2$$  
To find the $w_0^*$ and $w_1^*$ that minimize $R_{sq}(w_0,w_1)$, we'll:  
1. Find $\frac{\partial R_{sq}}{\partial w_0}$ and set it equal to 0.  
2. Find $\frac{\partial R_{sq}}{\partial w_1}$ and set it equal to 0.  
3. Solve the resulting system of equations.  

$R_{sq}(w_0,w_1)=\frac{1}{n}\sum_{i=1}^n (y_i - (w_0 + w_1 x_i))^2$  
$\frac{\partial R_{sq}}{\partial w_0}=\frac{1}{n}\sum_{i=1}^n 2(y_i-(w_0+w_1 x_i)) \cdot (-1)$  
$=\frac{-2}{n}\sum_{i=1}^n (y_i-(w_0+w_1x_i))$  

$\frac{\partial R_{sq}}{\partial w_1}=\frac{1}{n}\sum_{i=1}^n 2(y_i-(w_0+w_1 x_i)) \cdot (-x_i)$  
$=\frac{-2}{n}\sum_{i=1}^n (y_i-(w_0+w_1x_i))x_i$  

### Strategy  

We have a system of two equations and two unknowns ($w_0$ and $w_1$):
$$-\frac{2}{n} \sum_{i=1}^n \left( y_i - (w_0 + w_1x_i) \right) = 0 \qquad -\frac{2}{n} \sum_{i=1}^n \left( y_i - (w_0 + w_1x_i) \right) x_i = 0$$

To proceed, we'll:
1. Solve for $w_0$ in the first equation.
The result becomes $w_0^*$, because it's the "best intercept."
1. Plug $w_0^*$ into the second equation and solve for $w_1$.
The result becomes $w_1^*$, because it's the "best slope."

### Solving for $w_0^*$  

$\frac{-2}{n}\sum_{i=1}^n (y_i-(w_0+w_1x_i))=0$  
$\sum_{i=1}^n (y_i-w_0-w_1x_i)=0$  
$\sum_{i=1}^n y_i-\sum_{i=1}^nw_0-\sum_{i=1}^nw_1x_i=0$  
$\sum_{i=1}^n y_i-nw_0-\sum_{i=1}^nw_1x_i=0$  
$\sum_{i=1}^n y_i - w_1\sum_{i=1}^n x_i=nw_0$  
$w_0=\frac{\sum_{i=1}^ny_i-w_1\sum_{i=1}^nx_i}{n}$  
$=\frac{1}{n}\sum_{i=1}^n y_i - w_1\frac{1}{n}\sum_{i=1}^n x_i$  
$w_0^*=\bar{y}-w_1\bar{x}$  

### Solving for $w_1^*$  

Goal: isolate $w_1$.  
$\frac{-2}{n}\sum_{i=1}^n (y_i-(w_0+w_1x_i))x_i=0$  
$\sum_{i=1}^n (y_i-(w_0+w_1x_i))x_i=0$  
Use $w_0^*=\bar{y}-w_1\bar{x}$  
$\sum_{i=1}^n (y_i-(\bar{y}-w_1\bar{x})-w_1x_i)x_i=0$  
$\sum_{i=1}^n(y_i-\bar{y}+w_1\bar{x}-w_1x_i)x_i=0$  
$\sum_{i=1}^n(y_i-\bar{y})x_i-\sum_{i=1}^nw_1(\bar{x}-x_i)x_i=0$  
$\sum_{i=1}^n(y_i-\bar{y})x_i+w_1\sum_{i=1}^n(\bar{x}-x_i)x_i=0$  
$\sum_{i=1}^n(y_i-\bar{y})x_i-w_1\sum_{i=1}^n(x_i-\bar{x})x_i=0$  
$w_1\sum_{i=1}^n(w_i-\bar{x})x_i=\sum_{i=1}^n(y_i-\bar{y})x_i$  
$$w_1^*=\frac{\sum_{i=1}^n(y_i-\bar{y})x_i}{\sum_{i=1}^n(x_i-\bar{x})x_i}$$  

### An equivalent formula for $w_1^*$  

Claim:  
$$w_1^*=\frac{\sum_{i=1}^n(y_i-\bar{y})x_i}{\sum_{i=1}^n(x_i-\bar{x})x_i}=\frac{\sum_{i=1}^n(x_i-\bar{x})(y_i-\bar{y})}{\sum_{i=1}^n(x_i-\bar{x})^2}$$  
Key idea: $\sum_{i=1}^n(x_i-\bar{x})=0$  
Proof:  
$\sum_{i]1}^n(x_i-\bar{x})(y_i-\bar{y})=\sum_{i=1}^n x_i(y_i-\bar{y})-\sum_{i=1}^n\bar{x}(y_i-\bar{y})$  
$=\sum_{i=1}^n(y_i-\bar{y})x_i-\bar{x}\sum_{i=1}^n(y_i-\bar{y})$  
$=\sum_{i=1}^n(y_i-\bar{y})x_i$ left numerator  
denominator follows a similar argument  

### Least squares solutions  

- The **least squares solutions** for the intercept $w_0$ and slope $w_1$ are:  
$$w_1^*=\frac{\sum_{i=1}^n(x_i-\bar{x})(y_i-\bar{y})}{\sum_{i=1}^n(x_i-\bar{x})^2},w_0^*=\bar{y}-w_1\bar{x}$$  
- We say $w_0^*$ and $w_1^*$ are **optimal parameters**, and the resulting line is called the **regression line**.  
- The process of minimizing empirical risk to find optimal parameters is also called "**fitting to the data.**"  
- To make predictions about the future, we use $H^*(x)=w_0^*+w_1^*x$.  

### Causality  

Can we conclude that leaving later **causes** you to get to school earlier?  
No! This is just an observed pattern  

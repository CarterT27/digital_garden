---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/DSC_40A"
date:
- 2024-04-11
---
Source: https://dsc40a.com/resources/lectures/lec04/lec04-blank.pdf  

# Simple Linear Regression  

---  

## Recap - Center and Spread  

### The relationship between $h^*$ and $R(h^*)$  

- Recall, for a general loss function $L$ and the constant model $H(x)=h$ empirical risk is of the form  
$$R(h)=\frac{1}{h}\sum_{i=1}^n L(y_i,h);  
TODO  

### Examples  

TODO?  

### 0-1 Loss  

TODO  

**TODO** a lot of stuff  

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

TODO  

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

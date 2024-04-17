---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/DSC_40A"
date:
- 2024-04-16
---
# More Simple Linear Regression  

## Correlation  

### Quantifying patterns in scatter plots  

- Correlation coefficient $r$  
- A measure of the strength of the **linear association** of two variables, $x$ and $y$  
- Intuitively, it measures how tightly clustered a scatter plot is around a straight line  
- ranges between -1 and 1  
- $r$ negative: negative association  
- $r$ positive: positive association  

### The correlation coefficient  

- The correlation coefficient, $r$, is defined as the **average of the product of $x$ and $y$, when both are in standard units**.  
- Let $\sigma_x$ be the standard deviation of the $x_i$s, and $\bar{x}$ be the mean of the $x_i$s.  
- $x_i$ in standard units is $\frac{x_i-\bar{x}}{\sigma_x}$.  
- The correlation coefficient, then, is:  
$$r=\frac{1}{n} \sum_{i=1}^n \left( \frac{x_i - \bar{x}}{\sigma_x} \right) \left( \frac{y_i - \bar{y}}{\sigma_y} \right)$$  

> [!question] Why multiply the product of SUs?  
> Top right $x_{i(su)}$ positive and $y_{i(su)}* positive  
> Bottom Left $x_{i(su)}$ negative and $y_{i(su)}$ negative  

### Another way to express $w_1^*$  

- It turns out that for $w_1^*$, the optimal slope for the linear hypothesis function when using squared loss (i.e. the regression line), can be written in terms of $r$  
$$w_1^* = \frac{\sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y})}{(x_i - \bar{x})^2} = r \frac{\sigma_y}{\sigma_x}$$  
TODO  

### Proof that $w_1^*=r\frac{\sigma_y}{\sigma_x}$  

$\sigma_x = \sqrt{\frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2}$  
$\sigma_x^2 = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2$  
$n\sigma_x^2 = \sum_{i=1}^n (x_i - \bar{x})^2$  

$r=\frac{1}{n} \sum_{i=1}^n \left( \frac{x_i - \bar{x}}{\sigma_x} \right) \left( \frac{y_i - \bar{y}}{\sigma_y} \right)$  
$r=\frac{1}{n\sigma_x\sigma_y} \sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y})$  
$rn\sigma_x\sigma_y=\sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y})$  

$w_1^* = \frac{\sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y})}{(x_i - \bar{x})^2}$  
$=\frac{rn\sigma_x\sigma_y}{n\sigma_x^2}=r\frac{\sigma_y}{\sigma_x}$  

---  

## Interpreting the formulas  

### Interpreting the slope  

$$w_1^*=r\frac{\sigma_y}{\sigma_x}$$  
- The units of the slope are **units of $y$ per units of $x$**.  
- In our commute times example, $H(x)=142.25 - 8.19x$, our predicted commute time **decreases by 8.19 minutes per hour.**  
- Since $\sigma_x\geq 0$ and $\sigma_y\geq 0$, the slope's sign is $r$'s sign.  
- As the $y$ values get more spread out, $\sigma_y$ increases, so the slope gets steeper.  
- As the $x$ values get more spread out, $\sigma_x$ increases, so the slope gets shallower.  

### Interpreting the intercept  

$$w_0^*=\bar{y}-w_1^*\bar{x}$$  
- What are the units of the intercept?  
- units of $y$: minutes  
- What is the value of $H^*(\bar{x})$?  
$H(x)=w_0^*+w_1^*x$  
$=\bar{y}-w_1^*\bar{x}+w_1^*x$  
$=\bar{y}+w_1^*(x-\bar{x})$  
$\implies H^*(\bar{x})=\bar{y}$  

### Correlation and mean squared error  

- **Claim**: Suppose that $w_0^*$ and $w_1^*$ are the optimal intercept and slope for the regression line. Then,  
$$R_{sq}(w_0^*,w_1^*)=\sigma_y^2(1-r^2)$$  
- That is, the **mean squared error of the regression line's predictions** and the correlation coefficient, $r$, always satisfy the relationship above.  
- Even if it's true, why do we care?  
- In machine learning, we often use both the mean squared error and $r^2$ to compare the performances of different models.  
- If we can prove the above statement, we can show that finding models that minimize mean squared error is equivalent to finding models that maximize $r^2$  

Important for #Class/DSC_80  

---  

## Connections to related models  

### Exercise  

Suppose we chose the model $H(x)=w_1x$ and squared loss.  
What is the optimal model parameter, $w_1^*$?  

$R_{sq}(w_1)=\frac{1}{n} \sum_{i=1}^n (y_i - w_1x_i)$  
TODO  

### Comparing mean squared errors  

TODO  

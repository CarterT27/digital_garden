---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/DSC_40A"
date:
- 2024-04-25
---
Source: https://dsc40a.com/resources/lectures/lec08/lec08-filled.pdf  

# Regression and Linear Algebra  

## Overview: Spans and Projections  

# Regression and Linear Algebra  

### Projecting onto the span of a single vector  

- **Question**: What vector in $\text{span}({\color{#007aff} \vec x})$ is closest to $\color{orange} \vec{y}$?  
- The answer is the vector $w {\color{#007aff} \vec x}$, where the $w$ is chosen to minimize the **length** of the <span style="color:red">error vector</span>:  
$$\lVert {\color{red} \vec e} \rVert = \lVert {\color{orange} \vec y} - w {\color{#007aff} \vec{x}} \rVert$$  
- **Key idea**: To minimize the length of the <span style="color:red">error vector</span>, choose $w$ so that the <span style="color:red">error vector</span> is **orthogonal** to ${\color{#007aff} \vec x}$.  
- **Answer**: It is the vector $w^* {\color{#007aff}\vec x}$, where:  
$$w^* = \frac{{\color{#007aff}\vec x} \cdot {\color{orange}\vec y}}{{\color{#007aff}\vec x} \cdot {\color{#007aff}\vec x}}$$  

### Projecting onto the span of multiple vectors  

- **Question**: What vector in $\text{span}({\color{#007aff} \vec{x}^{(1)}}, {\color{#007aff} \vec{x}^{(2)}})$ is closest to ${\color{orange} \vec{y}}$?  
- The answer is the vector $w_1 {\color{#007aff} \vec{x}^{(1)}} + w_2 {\color{#007aff} \vec{x}^{(2)}}$, where $w_1$ and $w_2$ are chosen to minimize the **length** of the <span style="color:red">error vector</span>:  
$$\lVert {\color{red} \vec e} \rVert = \lVert {\color{orange} \vec{y}} - w_1 {\color{#007aff} \vec{x}^{(1)}} - w_2 {\color{#007aff} \vec{x}^{(2)}}\rVert$$  
- **Key idea**: To minimize the length of the <span style="color:red">error vector</span>, choose $w_1$ and $w_2$ so that the <span style="color:red">error vector</span> is **orthogonal** to **both** $\color{#007aff} \vec{x}^{(1)}$ **and** $\color{#007aff} \vec{x}^{(2)}$.  

If $\color{#007aff} \vec{x}^{(1)}$ and $\color{#007aff} \vec{x}^{(2)}$ are **linearly<br> independent**, they span a **plane**.  

### Matrix-vector products create linear combinations of columns!  

- **Question**: What vector in $\text{span}({\color{#007aff} \vec{x}^{(1)}}, {\color{#007aff} \vec{x}^{(2)}})$ is closest to ${\color{orange} \vec{y}}$?  
- To help, we can create a **matrix**, ${\color{#007aff} X}$, by stacking $\color{#007aff} \vec{x}^{(1)}$ and $\color{#007aff} \vec{x}^{(2)}$ next to each other:  
$${\color{#007aff} X} = \begin{bmatrix} \mid & \mid \\ {\color{#007aff} \vec x^{(1)}} & {\color{#007aff} \vec x^{(2)}} \\ \mid & \mid \end{bmatrix} = \begin{bmatrix} {\color{#007aff} 2} & {\color{#007aff} -1} \\ {\color{#007aff} 5} & {\color{#007aff} 0} \\ {\color{#007aff} 3} & {\color{#007aff} 4} \end{bmatrix} \qquad {\color{orange} \vec{y} = \begin{bmatrix} 1 \\ 3 \\ 9 \end{bmatrix}}$$  
- Then, instead of writing vectors in  $\text{span}({\color{#007aff} \vec{x}^{(1)}}, {\color{#007aff} \vec{x}^{(2)}})$ as $w_1 {\color{#007aff} \vec{x}^{(1)}} + w_2 {\color{#007aff} \vec{x}^{(2)}}$, we can say:  
$${\color{#007aff} X} \vec{w} \:\:\:\:\:\:\:\:\:\:\:\:\: \text{where } \vec{w} = \begin{bmatrix} w_1 \\ w_2 \end{bmatrix}$$  
- **Key idea**: Find $\vec{w}$ such that the <span style="color:red">error vector</span>, ${\color{red} \vec e} = {\color{orange} \vec{y}} - {\color{#007aff} X}\vec{w}$, is **orthogonal** to **every column of ${\color{#007aff} X}$**.  

### Constructing an orthogonal error vector  

- **Key idea**: Find $\vec{w} \in \mathbb{R}^d$ such that the <span style="color:red">error vector</span>, ${\color{red} \vec e} = {\color{orange} \vec{y}} - {\color{#007aff} X}\vec{w}$, is **orthogonal** to the **columns of ${\color{#007aff} X}$**.  
- Why? Because this will make the <span style="color:red">error vector</span> as short as possible.  
- The $\vec{w}^*$ that accomplishes this satisfies:  
$${\color{#007aff} X^T}  {\color{red} \vec{e}} = 0$$  
- Why? Because ${\color{#007aff} X^T}  {\color{red} \vec{e}}$ contains the **dot products** of each column in ${\color{#007aff} X}$ with $\vec{e}$. If these are all 0, then $\color{red} \vec{e}$ is **orthogonal** to **every column of ${\color{#007aff} X}$**!  
$${\color{#007aff} X^T}{\color{red} \vec{e}} = \begin{bmatrix} - \:{\color{#007aff} \vec{x}^{(1)^T}} - \\ - \:{\color{#007aff} \vec{x}^{(2)^T}} - \end{bmatrix}{\color{red} \vec{e}} = \begin{bmatrix} {\color{#007aff} \vec{x}^{(1)^T}}{\color{red} \vec{e}} \\ {\color{#007aff} \vec{x}^{(2)^T}}{\color{red} \vec{e}} \end{bmatrix}$$  

### The normal equations  

- **Key idea**: Find $\vec{w} \in \mathbb{R}^d$ such that the <span style="color:red">error vector</span>, ${\color{red} \vec e} = {\color{orange} \vec{y}} - {\color{#007aff} X}\vec{w}$, is **orthogonal** to the **columns of ${\color{#007aff} X}$**.  
- The $\vec{w}^*$ that accomplishes this satisfies:  
$$\begin{align*} {\color{#007aff} X^T}  {\color{red} \vec{e}} &= 0 \\ {\color{#007aff} X^T} ({\color{orange} \vec{y}} - {\color{#007aff} X} \vec{w}^*) &= 0 \\ {\color{#007aff} X^T} {\color{orange} \vec{y}} - {\color{#007aff} X^TX}\vec{w}^* &= 0 \\ \implies {\color{#007aff} X^TX} \vec{w}^* &= {\color{#007aff} X^T} {\color{orange} \vec y} \end{align*}$$  
- The last statement is referred to as the **normal equations**.  

- Assuming $\color{#007aff} X^TX$ is invertible, this is the vector:  
$$\boxed{\vec{w}^* = ({\color{#007aff}{X^TX}})^{-1} {\color{#007aff}{X^T}}\color{orange}\vec{y}}$$  
- This is a big assumption, because it requires ${\color{#007aff}{X^TX}}$ to be **full rank**.  
- If ${\color{#007aff}{X^TX}}$ is not full rank, then there are infinitely many solutions to the normal equations, ${\color{#007aff} X^TX} \vec{w}^* = {\color{#007aff} X^T} {\color{orange} \vec y}$.  

### What does it mean?  

- **Original question**: What vector in $\text{span}({\color{#007aff} \vec{x}^{(1)}}, {\color{#007aff} \vec{x}^{(2)}})$ is closest to ${\color{orange} \vec{y}}$?  
- **Final answer**: Assuming ${\color{#007aff} X^TX}$ is invertible, it is the vector ${\color{#007aff} X} \vec{w}^*$, where:  
$$\vec{w}^* = ({\color{#007aff}{X^TX}})^{-1} {\color{#007aff}{X^T}}\color{orange}\vec{y}$$  
- Revisiting our example:  
$${\color{#007aff} X} = \begin{bmatrix} \mid & \mid \\ {\color{#007aff} \vec x^{(1)}} & {\color{#007aff} \vec x^{(2)}} \\ \mid & \mid \end{bmatrix} = \begin{bmatrix} {\color{#007aff} 2} & {\color{#007aff} -1} \\ {\color{#007aff} 5} & {\color{#007aff} 0} \\ {\color{#007aff} 3} & {\color{#007aff} 4} \end{bmatrix} \qquad {\color{orange} \vec{y} = \begin{bmatrix} 1 \\ 3 \\ 9 \end{bmatrix}}$$  
- Using a computer gives us $\vec{w}^* =  ({\color{#007aff}{X^TX}})^{-1} {\color{#007aff}{X^T}}{\color{orange}\vec{y}} \approx \begin{bmatrix} 0.7289 \\ 1.6300 \end{bmatrix}$.  
- So, the vector in $\text{span}({\color{#007aff} \vec{x}^{(1)}}, {\color{#007aff} \vec{x}^{(2)}})$ closest to ${\color{orange} \vec{y}}$ is $0.7289 {\color{#007aff} \vec{x}^{(1)}} + 1.6300 {\color{#007aff} \vec{x}^{(2)}}$.  

### An optimization problem, solved  

- We just used linear algebra to solve an **optimization problem**.  
- Specifically, the function we minimized is:  
$${\color{red}\text{error}}(\vec{w}) =  \lVert {\color{orange} \vec{y}} - {\color{#007aff} X}\vec{w} \rVert$$  
- This is a function whose input is a vector, $\vec{w}$, and whose output is a scalar!  
- The input, $\vec{w}^*$, to ${\color{red}\text{error}}(\vec{w})$ that minimizes it is one that satisfies the **normal equations**:  
$${\color{#007aff} X^TX} \vec{w}^* = {\color{#007aff} X^T} {\color{orange} \vec y}$$  
If ${\color{#007aff} X^TX}$ is invertible, then the unique solution is:  
$$\vec{w}^* = ({\color{#007aff}{X^TX}})^{-1} {\color{#007aff}{X^T}}\color{orange}\vec{y}$$  
- We're going to use this frequently!  

---  

## Regression and linear algebra  

### Wait... why do we need linear algebra?  

- Soon, we'll want to make predictions using more than one feature.  
- Example: Predicting commute times using departure hour and temperature.  
- Thinking about linear regression in terms of **matrices and vectors** will allow us to find hypothesis functions that:  
- Use multiple features (input variables).  
- Are non-linear in the features, e.g. $H(x) = w_0 + w_1 x + w_2 x^2$.  
- Let's see if we can put what we've just learned to use.  

### Simple linear regression, revisited  

- **Model**: $H(x) = w_0 + w_1x$.  
- **Loss function**: $(y_i - H(x_i))^2$.  
- To find $w_0^*$ and $w_1^*$, we minimized empirical risk, i.e. average loss:  
$$R_\text{sq}(H) = \frac{1}{n} \sum_{i = 1}^n \left( y_i - H(x_i) \right)^2$$  
- **Observation**: $R_\text{sq}(w_0, w_1)$ _kind of_ looks like the formula for the norm of a vector, $\lVert \vec v \rVert = \sqrt{v_1^2 + v_2^2 + \ldots + v_n^2}$.  

### Regression and linear algebra  

Let's define a few new terms:  
- The **observation vector** is the vector $\color{orange} \vec{y} \in \mathbb{R}^n$. This is the vector of observed "actual values".  
- The **hypothesis vector** is the vector $\color{purple} \vec{h} \in \mathbb{R}^n$ with components $\color{purple}H(x_i)$. This is the vector of predicted values.  
- The **error vector** is the vector $\color{red} \vec{e} \in \mathbb{R}^n$ with components:  
$${\color{red} e_i} = {\color{orange} y_i} - {\color{purple}H(x_i)}$$  

### Example  

Consider $\color{purple}H(x) = 2 + \frac{1}{2}x$.  

${\color{orange}\vec{y}} = \:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\: {\color{purple}\vec{h}} =$  

${\color{red}\vec{e}} = {\color{orange} \vec y} - {\color{purple} \vec h} =$  

$\displaystyle \begin{align*}R_\text{sq}({\color{purple}H}) &= \frac{1}{n} \sum_{i = 1}^n \left( {\color{orange} y_i} - {\color{purple}H(x_i)} \right)^2 \\ &=\end{align*}$  

### Regression and linear algebra  

Let's define a few new terms:  
- The **observation vector** is the vector $\color{orange} \vec{y} \in \mathbb{R}^n$. This is the vector of observed "actual values".  
- The **hypothesis vector** is the vector $\color{purple} \vec{h} \in \mathbb{R}^n$ with components $\color{purple}H(x_i)$. This is the vector of predicted values.  
- The **error vector** is the vector $\color{red} \vec{e} \in \mathbb{R}^n$ with components:  
$${\color{red} e_i} = {\color{orange} y_i} - {\color{purple}H(x_i)}$$  
- **Key idea**: We can rewrite the mean squared error of $\color{purple}H$ as:  
$$R_\text{sq}({\color{purple}H}) = \frac{1}{n} \sum_{i = 1}^n \left( {\color{orange} y_i} - {\color{purple}H(x_i)} \right)^2 = \frac{1}{n} \lVert {\color{red} \vec e} \rVert^2 = \frac{1}{n} \lVert {\color{orange} \vec y} - {\color{purple} \vec{h}} \rVert^2$$  

### The hypothesis vector  

- The **hypothesis vector** is the vector $\color{purple} \vec{h} \in \mathbb{R}^n$ with components $\color{purple}H(x_i)$. This is the vector of predicted values.  
- For the linear hypothesis function $\color{purple} H(x) = w_0 + w_1x$, the hypothesis vector can be written:  
$${\color{purple} \vec h} = \begin{bmatrix} {\color{purple} w_0 + w_1 x_1} \\ {\color{purple} w_0 + w_1 x_2} \\ \vdots \\ {\color{purple} w_0 + w_1 x_n} \end{bmatrix} = \:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:$$  

### Rewriting the mean squared error  

- Define the **design matrix** $\color{#007aff} X \in \mathbb{R}^{n \times 2}$ as:  
$${\color{#007aff} X} = \begin{bmatrix} {\color{#007aff} 1} & {\color{#007aff} x_1} \\ {\color{#007aff} 1} & {\color{#007aff} x_2} \\ \vdots & \vdots \\ {\color{#007aff} 1} & {\color{#007aff} x_n} \end{bmatrix}$$  
- Define the **parameter vector** $\vec{w} \in \mathbb{R}^2$ to be $\vec{w} = \begin{bmatrix} w_0 \\ w_1 \end{bmatrix}$.  
- Then, ${\color{purple} \vec h} = {\color{#007aff} X} \vec{w}$, so the mean squared error becomes:  
$$R_\text{sq}({\color{purple}H}) =  \frac{1}{n} \lVert {\color{orange} \vec y} - {\color{purple} \vec{h}} \rVert^2 \implies \boxed{R_\text{sq}(\vec{w}) = \frac{1}{n}  \lVert {\color{orange} \vec{y}} - {\color{#007aff} X}\vec{w} \rVert^2}$$  

### Minimizing mean squared error, again  

- To find the optimal model parameters for simple linear regression, $w_0^*$ and $w_1^*$, we previously minimized:  
$$R_\text{sq}(w_0, w_1) = \frac{1}{n} \sum_{i = 1}^n ({\color{orange} y_i} - (w_0 + w_1 {\color{#007aff} x_i}))^2$$  
- Now that we've reframed the simple linear regression problem in terms of linear algebra, we can find $w_0^*$ and $w_1^*$ by finding the $\vec{w}^* = \begin{bmatrix} w_0^* & w_1^* \end{bmatrix}^T$ that minimizes:  
$$\boxed{R_\text{sq}(\vec{w}) = \frac{1}{n}  \lVert {\color{orange} \vec{y}} - {\color{#007aff} X}\vec{w} \rVert^2}$$  
- Do we already know the $\vec{w^*}$ that minimizes $R_\text{sq}(\vec{w})$?  

### An optimization problem we've seen before  

- The optimal parameter vector, $\vec{w}^* = \begin{bmatrix} w_0^* & w_1^* \end{bmatrix}^T$, is the one that minimizes:  
$$R_\text{sq}(\vec{w}) = \frac{1}{n}  \lVert {\color{orange} \vec{y}} - {\color{#007aff} X}\vec{w} \rVert^2$$  
- Previously, we found that $\vec{w}^* = ({\color{#007aff}{X^TX}})^{-1} {\color{#007aff}{X^T}}\color{orange}\vec{y}$ minimizes the length of the error vector, $\lVert {\color{red} \vec{e}} \rVert = \lVert {\color{orange} \vec{y}} - {\color{#007aff} X}\vec{w} \rVert$  
- $R_\text{sq}(\vec{w})$ is closely related to $\lVert {\color{red} \vec{e}} \rVert$:  
- The minimizer of $\lVert {\color{red} \vec{e}} \rVert$ is the same as the minimizer of $R_\text{sq}(\vec{w})$!  
- **Key idea**: $\vec{w}^* = ({\color{#007aff}{X^TX}})^{-1} {\color{#007aff}{X^T}}\color{orange}\vec{y}$ also **minimizes** $R_\text{sq}(\vec{w})$!  

### The optimal parameter vector, $\vec{w}^*$  

- To find the optimal model parameters for simple linear regression, $w_0^*$ and $w_1^*$, we previously minimized $R_\text{sq}(w_0, w_1) = \frac{1}{n} \sum_{i = 1}^n ({\color{orange} y_i} - (w_0 + w_1 {\color{#007aff} x_i}))^2$.  
- We found, using calculus, that:  
- $\boxed{w_1^* = \frac{\sum_{i = 1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i = 1}^n (x_i - \bar{x})^2} = r \frac{\sigma_y}{\sigma_x}}$.  
- $\boxed{w_0^* = \bar{y} - w_1^* \bar{x}}$.  
- Another way of finding optimal model parameters for simple linear regression is to find the $\vec{w}^*$ that minimizes $R_\text{sq}(\vec{w}) = \frac{1}{n}  \lVert {\color{orange} \vec{y}} - {\color{#007aff} X}\vec{w} \rVert^2$.  
- The minimizer, if ${\color{#007aff}{X^TX}}$ is invertible, is the vector $\boxed{\vec{w}^* = ({\color{#007aff}{X^TX}})^{-1} {\color{#007aff}{X^T}}\color{orange}\vec{y}}$.  
- These formulas are equivalent!  

### Roadmap  

- To give us a break from math, we'll switch to a notebook, [linked here](http://datahub.ucsd.edu/user-redirect/git-sync?repo=https://github.com/dsc-courses/dsc40a-2024-sp&subPath=lectures/lec08/lec08-code.ipynb), showing that both formulas – that is, (1) the formulas for $w_1^*$ and $w_0^*$ we found using calculus, and (2) the formula for $\vec{w}^*$ we found using linear algebra – give the same results.  
- Then, we'll use our new linear algebraic formulation of regression to incorporate **multiple features** in our prediction process.  

### Summary: Regression and linear algebra  

- Define the **design matrix** $\color{#007aff} X \in \mathbb{R}^{n \times 2}$, **observation vector** $\color{orange} \vec{y} \in \mathbb{R}^n$, and parameter vector $\vec{w} \in \mathbb{R}^2$ as:  
$${\color{#007aff} X} = \begin{bmatrix} {\color{#007aff} 1} & {\color{#007aff} x_1} \\ {\color{#007aff} 1} & {\color{#007aff} x_2} \\ \vdots & \vdots \\ {\color{#007aff} 1} & {\color{#007aff} x_n} \end{bmatrix} \qquad {\color{orange} \vec{y} = \begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{bmatrix}} \qquad \vec{w} = \begin{bmatrix} w_0 \\ w_1 \end{bmatrix}$$  
- How do we make the <span style="color:purple">hypothesis vector</span>, ${\color{purple} \vec h} = {\color{#007aff} X} \vec{w}$,  as close to ${\color{orange} \vec{y}}$ as possible? Use the parameter vector $\vec{w}^*$:  
$${\vec{w}^* = ({\color{#007aff}{X^TX}})^{-1} {\color{#007aff}{X^T}}\color{orange}\vec{y}}$$  
- We chose $\vec{w}^*$ so that ${\color{purple} \vec h^*} = {\color{#007aff} X} \vec{w}^*$ is **the projection of $\color{orange} \vec{y}$ onto the span of the columns of the design matrix, $\color{#007aff}X$**.  

---  

## Multiple linear regression  

So far, we've fit **simple** linear regression models, which use only **one** feature (`'departure_hour'`) for making predictions.  

### Incorporating multiple features  

- In the context of the commute times dataset, the simple linear regression model we fit was of the form:  
$$\begin{align*}\text{pred. commute} &= H(\text{departure hour}) \\ &= w_0 + w_1 \cdot \text{departure hour} \end{align*}$$  
- Now, we'll try and fit a multiple linear regression model of the form:  
$$\begin{align*}\text{pred. commute} &= H(\text{departure hour}) \\ &= w_0 + w_1 \cdot \text{departure hour} + w_2 \cdot \text{day of month} \end{align*}$$  
- Linear regression with **multiple** features is called **multiple linear regression**.  
- How do we find $w_0^*$, $w_1^*$, and $w_2^*$?  

### Geometric interpretation  

- The hypothesis function:  
$$H(\text{departure hour}) = w_0 + w_1 \cdot \text{departure hour}$$  
looks like a **line** in 2D.  
- **Questions**:  
- How many dimensions do we need to graph the hypothesis function:  
$$H(\text{departure hour}) = w_0 + w_1 \cdot \text{departure hour} + w_2 \cdot \text{day of month}$$  
- What is the shape of the hypothesis function?  
Our new hypothesis function is a **plane** in 3D!  

### The setup  

- Suppose we have the following dataset.  
- We can represent each day with a **feature vector**, $\vec{x}$:  

### The hypothesis vector  

- When our hypothesis function is of the form:  
$$H(\text{departure hour}) = w_0 + w_1 \cdot \text{departure hour} + w_2 \cdot \text{day of month}$$  
the hypothesis vector $\color{purple} \vec{h} \in \mathbb{R}^n$ can be written as:  
$${\color{purple} \vec{h}} = \begin{bmatrix}  
H(\text{departure hour}_1, \text{day}_1) \\  
H(\text{departure hour}_2, \text{day}_2) \\  
... \\  
H(\text{departure hour}_n, \text{day}_n) \\  
\end{bmatrix}  
= \begin{bmatrix}  
1      & \text{departure hour}_1 & \text{day}_1   \\  
1      & \text{departure hour}_2 & \text{day}_2    \\  
... & ... & ... \\  
1      & \text{departure hour}_n & \text{day}_n  
\end{bmatrix} \begin{bmatrix}  
w_0 \\  
w_1 \\  
w_2  
\end{bmatrix}  $$  

### Finding the optimal parameters  

- To find the optimal parameter vector, $\vec{w}^*$, we can use the **design matrix** $\color{#007aff} X \in \mathbb{R}^{n \times 3}$ and **observation vector** $\color{orange} \vec y \in \mathbb{R}^n$:  
$${\color{#007aff} X = \begin{bmatrix}  
1      & \text{departure hour}_1 & \text{day}_1   \\  
1      & \text{departure hour}_2 & \text{day}_2    \\  
... & ... & ... \\  
1      & \text{departure hour}_n & \text{day}_n  
\end{bmatrix}} \qquad {\color{orange} \vec{y} = \begin{bmatrix} \text{commute time}_1 \\ \text{commute time}_2 \\ \vdots \\ \text{commute time}_n \end{bmatrix}}$$  
- Then, all we need to do is solve the **normal equations**:  
$${\color{#007aff} X^TX} \vec{w}^* = {\color{#007aff} X^T} {\color{orange} \vec y}$$  
If ${\color{#007aff} X^TX}$ is invertible, we know the solution is:  
$$\vec{w}^* = ({\color{#007aff}{X^TX}})^{-1} {\color{#007aff}{X^T}}\color{orange}\vec{y}$$  

### Roadmap  

- To wrap up today's lecture, we'll find the optimal parameter vector $\vec{w}^*$ for our new two-feature model in code. We'll switch back to our notebook, [linked here](http://datahub.ucsd.edu/user-redirect/git-sync?repo=https://github.com/dsc-courses/dsc40a-2024-sp&subPath=lectures/lec08/lec08-code.ipynb).  

- Next class, we'll present a more general framing of the multiple linear regression model, that uses $d$ features instead of just two.  

- We'll also look at how we can **engineer** new features using existing features.  

- e.g. How can we fit a hypothesis function of the form $H(x) = w_0 + w_1 x + w_2 x^2$?  

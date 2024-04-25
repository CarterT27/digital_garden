---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/DSC_40A"
date:
- 2024-04-23
---
Source: https://dsc40a.com/resources/lectures/lec07/lec07-filled.pdf  

# Orthogonal Projections  

## Spans and Projections  

### Projecting onto a single vector  

- Let $\vec{x}$ and $\vec{y}$ be two vectors in $\mathbb{R}^n$.  
- The span of $\vec{x}$ is the set of all vectors of the form:  
$$w\vec{x}$$  
where $w\in\mathbb{R}$ is a scalar.  
- **Question**: What vector in $\text{span}(\vec{x})$ is closest to $\vec{y}$?  
- The vector in $\text{span}(\vec{x})$ that is closest to $\vec{y}$ is the ___ **projection of $\vec{y}$ onto** $\text{span}(\vec{x})$.  

### Projection error  

- Let $\vec{e} = \vec{y} - w\vec{x}$ be the **projection error**: that is, the vector that connects $\vec{y}$ to $\text{span}(\vec{x})$.  
- **Goal: Find the $w$ that makes $\vec{e}$ as short as possible.**  
- That is, minimize: $$\Vert \vec{e} \Vert$$  
- Equivalently, minimize: $$\Vert \vec{y}-w\vec{x}$$  
- **Idea**: To make $\vec{e}$ as short as possible, it should be **orthogonal to** $w\vec{x}$.  

### Minimizing projection error  

- **Goal: Find the $w$ that makes $\vec{e}=\vec{y}-w\vec{x}$ as short as possible**.  
- **Idea**: To make $\vec{e}$ as short as possible, it should be **orthogonal to** $w\vec{x}$.  
- Can we prove that making $\vec{e}$ orthogonal to $w\vec{x}$ minimizes $\Vert \vec{e}\Vert$?  
- Pythagorean theorem:  
$$\Vert \vec{e}' \Vert^{2} = \Vert \vec{e}^{*}\Vert^{2} + \Vert w'\vec{x} - w^*\vec{x} \Vert^2$$  
$$\Vert \vec{e}' \Vert^{2} \geq \Vert \vec{e}^{*}\Vert^2$$  
$$\implies \vec{e}^*\text{ is the shortest possible error vector!}$$  
- Now we know that to minimize $\Vert \vec{e} \Vert,\vec{e}$ must be orthogonal to $w\vec{x}$.  
- Given this fact, how can we solve for $w$?  
$$\vec{e}\text{ orthogonal to }w\vec{x}\implies w\vec{x}\cdot \vec{e}=0$$  
$$w\vec{x}\cdot(\vec{y}-w\vec{x})=0$$$$\vec{x}\cdot(\vec{y}-w\vec{x})=0$$$$\vec{x}\cdot \vec{y}-\vec{x}\cdot(w\vec{x})=0$$$$x\vec{v}\cdot \vec{y}-w(\vec{x}\cdot \vec{w})=0$$$$\vec{x}\cdot\vec{y}=w(\vec{x}\cdot \vec{x})$$  
$$\implies w^*=\frac{\vec{x}\cdot \vec{y}}{\vec{x}\cdot \vec{x}}$$  

### Orthogonal projection  

- **Question**: What vector in $\text{span}(\vec{x})$ is closest to $\vec{y}$?  
- **Answer**: It is the vector $w^*\vec{x}$, where: $$w^*=\frac{\vec{x}\cdot \vec{y}}{\vec{x}\cdot \vec{x}}$$  
- Note that $w^*$ is the solution to a minimization problem, specifically, this one: $$\text{error}(w)=\Vert \vec{e} \Vert = \Vert \vec{y} - w\vec{x} \Vert$$  
- We call $w^*\vec{x}$ the **orthogonal projection of $\vec{y}$ onto** $\text{span}(\vec{x})$j.  
- Think of $w^*\vec{x}$ as the "shadow" of $\vec{y}$.  

### Exercise  

Let $\vec{a}=\begin{bmatrix}5\\2\end{bmatrix}$ and $\vec{b}=\begin{bmatrix}-1\\9\end{bmatrix}$.  
What is the orthogonal projection of $\vec{a}$ onto $\text{span}(\vec{b})$?  
Your answer should be of the form $w^*\vec{b}$, where $w^*$ is a scalar.  
$$w^*=\frac{\vec{b}\cdot \vec{a}}{\vec{b}\cdot \vec{b}}=\frac{(-1)(5)+(9)(2)}{(-1)^2+(9)^2}=\frac{13}{82}$$  
Orthogonal projection of $\vec{a}$ onto $\text{span}(\vec{b})$ is $\frac{13}{82}\vec{b}$.  

### Moving to multiple dimensions  

- Let's now consider three vectors, $\vec{y},\vec{x}^{(1)},$ and $\vec{x}^{(2)}$, all in $\mathbb{R}^n$.  
- **Question**: What vector in $\text{span}(\vec{x}^{(1)},\vec{x}^{(2)})$ is closest to $\vec{y}$?  
- Vectors in $\text{span}(\vec{x}^{(1)},\vec{x}^{(2)})$ are of the form $w_{1}\vec{x}^{(1)}+w_{2}\vec{x}^{(2)}$, where $w_{1},w_{2}\in\mathbb{R}$ are scalars.  

### Minimizing projection error in multiple dimensions  

- **Question**: What vector in $\text{span}(\vec{x}^{(1)},\vec{x}^{(2)})$ is closest to $\vec{y}$?  
- That is, what vector minimizes $\Vert \vec{e} \Vert$, where: $$\vec{e} = \vec{y} - w_{1}\vec{x}^{(1)}-w_{2}\vec{x}^{(2)}$$  
- **Answer**: It's the vector such that $w_{1}\vec{x}^{(1)} + w_{2}\vec{x}^{(2)}$ is **orthogonal** to $\vec{e}$.  
- **Issue**: Solving for $w_{1}$ and $w_{2}$ in the following equation is difficult: $$(w_{1}\vec{x}^{(1)}+w_{2}\vec{x}^{(2)})\cdot(\vec{y}-w_{1}\vec{x}^{(1)}-w_{2}\vec{x}^{(2)})=0$$  
- It's hard for us to solve for $w_{1}$ and $w_{2}$ in: $$(w_{1}\vec{x}^{(1)}+w_{2}\vec{x}^{(2)})\cdot(\vec{y}-w_{1}\vec{x}^{(1)}-w_{2}\vec{x}^{(2)})=0$$  
- **Observation**: All we really need is for $\vec{x}^{(1)}$ and $\vec{x}^{(2)}$ to individually be orthogonal to $\vec{e}$.l  
- That is, it's sufficient for $\vec{e}$ to be orthogonal to the spanning vectors themselves.  
- If $\vec{x}^{(1)}\cdot \vec{e}=0$ and $\vec{x}^{(2)}\cdot \vec{e}=0$ then: $$(w_{1}\vec{x}^{(1)}+w_{2}\vec{x}^{(2)})\cdot \vec{e}=w_{1}\vec{x}^{(1)}\cdot \vec{e}+w_{2}\vec{x}^{(2)}\cdot \vec{e}$$  
$$=w_{1}(\vec{x}\cdot \vec{e})+w_{2}(\vec{x}^{(2)}\cdot \vec{e})$$  
$$=w_{1}(0)+w_{2}(0)$$  
$$=0$$  
- **Question**: What vector in $\text{span}(\vec{x}^{(1)},\vec{x}^{(2)})$ is closest to $\vec{y}$?  
- **Answer**: It's the vector such that $w_{1}\vec{x}^{(1)}+w_{2}\vec{x}^{(2)}$ is **orthogonal** to $\vec{e}=\vec{y}-w_{1}\vec{x}^{(1)}-w_{2}\vec{x}^{(2)}$.  
- **Equivalently, it's the vector such that $\vec{x}^{(1)}$ and $\vec{x}^{(2)}$ are both orthogonal to $\vec{e}$**:  
$$\vec{x}^{(1)}\cdot(\vec{y}-w_{1}\vec{x}^{(1)}-w_{2}\vec{x}^{(2)})=0$$  
$$\vec{x}^{(2)}\cdot(\vec{y}-w_{1}\vec{x}^{(1)}-w_{2}\vec{x}^{(2)})=0\to \text{need to find }w_{1}^*,w_{2}^*$$  
- This is a system of two equations, two unknowns ($w_{1}$ and $w_{2}$), but it still looks difficult to solve.  

### Now what?  

- We're looking for the scalars $w_{1}$ and $w_{2}$ that satisfy the following equations:  
$$\vec{x}^{(1)}\cdot(\vec{y}-w_{1}\vec{x}^{(1)}-w_{2}\vec{x}^{(2)})=0$$  
$$\vec{x}^{(2)}\cdot(\vec{y}-w_{1}\vec{x}^{(1)}-w_{2}\vec{x}^{(2)})=0$$  
- In this example, we just have two spanning vectors, $\vec{x}^{(1)}$ and $\vec{x}^{(2)}$.  
- If we had any more, this system of equations would get extremely messy, extremely quickly.  
- **Idea**: Rewrite the above system of equations **as a single equation, involving matrix-vector products**.  

---  

## Matrices  

### Matrices  

- An $n \times d$ **matrix** is a table of numbers with $n$ rows and $d$ columns.  
- We use upper-case letters to denote matrices.  
$$A=\begin{bmatrix}  
2&5&8\\-1&5&-3  
\end{bmatrix}_{2\times 3}$$  
- Since $A$ has two rows and three columns, we say $A\in\mathbb{R}^{2\times 3}$.  
- **Key idea**: Think of a matrix as **several column vectors, stacked next to each other**.  

### Matrix addition and scalar multiplication  

- We can add two matrices only if they have the same dimensions.  
- Addition occurs elementwise  
- TODO  
- Scalar multiplication occurs elementwise, too:  
- TODO  

### Matrix-matrix multiplication  

- **Key idea**: We can multiply matrices $A$ and $B$ **if and only if**:  
$$\text{\# columns in A = \# rows in B}$$  
- If $A$ is $n\times d$ and $B$ is $d\times p$, then $AB$ is $n\times p$.  
- Example: If $A$ is as defined below, what is $A^TA$?  
$$A=\begin{bmatrix}2&5&8\\-1&5&-3\end{bmatrix}_{2\times3}$$  

### Matrix-vector multiplication  

- A vector $\vec{v}\in\mathbb{R}^n$ is a matrix with $n$ rows and 1 column.  
$$\vec{v}=\begin{bmatrix}v_{1}\\v_{2}\\\vdots\\v_{n}\end{bmatrix}$$  
- Suppose $A\in\mathbb{R}^{n\times d}$.  
- What must the dimensions of $\vec{v}$ be in order for the product $A\vec{v}$ to be valid?  
- What must the dimensions of $\vec{v}$ be in order for the product $\vec{v}^TA$ to be valid?  

### One view of matrix-vector multiplication  

- One way of thinking about the product $A\vec{v}$ is that it is **the dot product of $\vec{v}$ with every row of $A$**.  

### Another view of matrix-vector multiplication  

- Another way of thinking about the product of $A\vec{v}$ is that it is **a linear combination of the columns of $A$, using the weights in $\vec{v}$**.  

### Matrix-vector products create linear combinations of columns!  

- **Key idea**: It'll be very useful to think of the matrix-vector product $A\vec{v}$ as a linear combination of the columns of $A$, using the weights in $\vec{v}$.  
$$A=\begin{bmatrix}a_{11}&a_{12}&\dots&a_{1d}\\a_{21}&a_{22}&\dots&a_{2d}\\\vdots&\vdots&\vdots&\vdots\\a_{n1}&a_{n2}&\dots&a_{nd}\end{bmatrix},\vec{v}=\begin{bmatrix}v_{1}j\\v_{2}\\\vdots\\v_{d}\end{bmatrix}$$  
$$A\vec{v}=v_{1}\begin{bmatrix}a_{11}\\a_{21}\\\dots\\a_{n1}\end{bmatrix}+v_{2}\begin{bmatrix}a_{12}\\a_{22}\\\vdots\\a_{n2}\end{bmatrix}+\dots+v_{d}\begin{bmatrix}a_{1d}\\a_{2d}\\\vdots\\v_{nd}\end{bmatrix}\implies \text{result is a vector in }\mathbb{R}^n$$  

---  

## Spans and projections, revisited  

### Moving to multiple dimensions  

- Let's now consider three vectors, $\vec{y},\vec{x}^{(1)}$, and $\vec{x}^{(2)}$, all in $\mathbb{R}^n$.  
- **Question**: What vector in $\text{span}(\vec{x}^{(1)},\vec{x}^{(2)})$ is closest to $\vec{y}$?  
- That is, what values of $w_{1}$ and $w_{2}$ minimize $\Vert \vec{e} \Vert=\Vert \vec{y}-w_{1}\vec{x}^{(1)}-w_{2}\vec{x}^{(2)}$?  
Answer: $w_{1}$ and $w_{2}$ such that:  
$$\vec{x}^{(1)}\cdot \vec{e}=0$$  
$$\vec{x}^{(2)}\cdot \vec{e}=0$$  

### Matrix-vector products create linear combinations of columns!  

- Combining $\vec{x}^{(1)}$ and $\vec{x}^{(2)}$ into a single matrix gives:  
$$X=\begin{bmatrix}\vert & \vert \\ \vec{x}^{(1)} & \vec{x}^{(2)} \\ \vert & \vert\end{bmatrix}$$  
- Then, if $\vec{w}=\begin{bmatrix}w_{1}\\w_{2}\end{bmatrix}$, linear combinations of $\vec{x}^{(1)}$ and $\vec{x}^{(2)}$ can be written as $X\vec{w}$.  
- The **span of the columns of $X$**, or $\text{span}(X)$, consists of all vectors that can be written in the form $X\vec{w}$.  

### Minimizing projection error in multiple dimensions  

- **Goal**: Find the vector $\vec{w}=\begin{bmatrix}w_{1}&w_{2}\end{bmatrix}^T$ such that $\Vert \vec{e} \Vert = \Vert \vec{y} - X\vec{w} \Vert$ is minimizedl.  
- As we've seen, $\vec{w}$ must be such that:  
$$\vec{x}^{(1)}\cdot(\vec{y}-w_{1}\vec{x}^{(1)}-w_{2}\vec{x}^{(2)})=0$$$$\vec{x}^{(2)}\cdot(\vec{y}-w_{1}\vec{x}^{(1)}-w_{2}\vec{x}^{(2)})=0$$  
- **How can we use our knowledge of matrices to rewrite this system of equations as a single equation?**  

### Simplifying the system of equations, using matrices  

$$X=\begin{bmatrix}\vert & \vert \\ \vec{x}^{(1)} & \vec{x}^{(2)} \\ \vert & \vert\end{bmatrix}$$  
$$\vec{x}^{(1)}\cdot(\vec{y}-w_{1}\vec{x}^{(1)}-w_{2}\vec{x}^{(2)})=0$$$$\vec{x}^{(2)}\cdot(\vec{y}-w_{1}\vec{x}^{(1)}-w_{2}\vec{x}^{(2)})=0$$  
$$w_{1}\vec{x}^{(1)}+w_{2}\vec{x}^{(2)}=X\vec{w}$$  
$$\implies \vec{e}=\vec{y}-w_{1}\vec{x}^{(1)}-w_{2}\vec{x}^{(2)}=\vec{y}-X\vec{w}$$  
1. $w_{1}\vec{x}^{(1)}+w_{2}\vec{x}^{(2)}$ can be written as $X\vec{w}$, so $\vec{e}=\vec{y}-X\vec{w}$.  
2. **The condition that $\vec{e}$ must be orthogonal to each column of $X$ is equivalent to the condition that $X^T\vec{e}=0$**.  
$\vec{x}^{(1)}\cdot(\vec{y}-X\vec{w})=0$  
$\vec{x}^{(2)}\cdot(\vec{y}-X\vec{w})=0$  
$\implies X^T(\vec{y}-X\vec{w})=\vec{0}$  
$X^T\vec{e}=\begin{bmatrix}- & \vec{x}^{(1)T}& -\\-&\vec{x}^{(2)T}&-\end{bmatrix}\vec{e}=\begin{bmatrix}\vec{x}^{(1)T}\vec{e}\\\vec{x}^{(2)T}\vec{e}\end{bmatrix}=\vec{0}$  
Rows of $X^T$ are the columns of $X$  

### The normal equations  

- **Goal**: Find the vector $\vec{w}=\begin{bmatrix}w_1,w_2\end{bmatrix}^T$ such that $\Vert \vec{e} \Vert=\vec{y}-X\vec{w} \Vert$ is minimized.  
- We now know that it is the vector $\vec{w}^*$ such that:  
$$X^T\vec{e}=0$$  
$$X^T(\vec{y}-X\vec{w}^*)=0$$  
$$X^T\vec{y}-X^TX\vec{w}^*=0$$  
$$\implies X^TX\vec{w}^*=X^T\vec{y}$$  
- The last statement is referred to as the **normal equations**.  

### The general solution to the normal equation  

$$X\in\mathbb{R}^{n\times d},\vec{y}\in\mathbb{R}^n$$  
- **Goal, in general**: Find the vector $\vec{w}\in\mathbb{R}^d$ such that $\Vert \vec{e} \Vert = \Vert \vec{y} - X\vec{w} \Vert$ is minimized.  
- We now know that it is the vector $\vec{w}^*$ such that:  
$$X^T\vec{e}=0$$  
$$\implies X^TX\vec{w}^*=X^T\vec{y}$$  
- Assuming $X^TX$ is invertible, this is the vector:  
$$\vec{w}^*=(X^TX)^{-1}X^T\vec{y}$$  
- This is a big assumption, because it requires $X^TX$ to be **full rank**.  
- If $X^TX$ is not full rank, then there are infinitely many solutions to the normal equations, $X^TX\vec{w}^*=X^T\vec{y}$.  

### What does it mean?  

- **Original question**: What vector in $\text{span}(\vec{x}^{(1)},\vec{x}^{(2)})$ is closest to $\vec{y}$?  
- **Final answer**: It is the vector $X\vec{w}^*$, where:  
$$\vec{w}^*=(X^TX)^{-1}X^T\vec{y}$$  
- $\vec{w}^*=(X^TX)^{-1}X^T\vec{y}$  

### An optimization problem, solved  

- We just used linear algebra to solve an **optimization problem**.  
- Specifically, the function we minimized is:  
$$\text{error}(\vec{w})=\Vert \vec{y} - X\vec{w} \Vert$$  
- This is a function whose input is a vector, $\vec{w}$, and whose output is a scalar  
- The input, $\vec{w}^*$, to $\text{error}(\vec{w})$ that minimizes it is:  
$$\vec{w}^*=(X^TX)^{-1}X^T\vec{y}$$  
- We're going to use this frequently!  

---  

## Regression and linear algebra  

### Wait... why do we need linear algebra?  

- Soon, we'll want to make predictions using more than one feature.  
- Example: Predicting commute times using departure hour and temperature.  
- Thinking about linear regression in terms of **matrices and vectors** will allow us to find hypothesis functions that:  
- Use multiple features (input variables).  
- Are non-linear in the features, e.g. $H(x)=w_{0}+w_{1}x+w_{2}x^2$.  
- Let's see if we can put what we've just learned to use.  

### Simple linear regression, revisited  

- **Model**: $H(x)=w_{0}+w_{1}x$.  
- **Loss function**: $(y_{i}-H(x_{i}))^2$.  
- To find $w_{0}^*$ and $w_{1}^*$ we minimized empirical risk, i.e. average loss:  
$$R_{sq}(H)=\frac{1}{n}\sum_{i=1}^n(y_{i})-H(x_{i}))^2$$  
- **Observation**: $R_{sq}(w_{0},w_{1})$ kind of looks like the formula for the norm of a vector,  
$$\Vert \vec{v} \Vert = \sqrt{ v_{1}^2+v_{2}^2+\dots+v_{n}^2 }$$  

### Regression and linear algebra  

Let's define a few new terms:  
- The **observation vector** is the vector $\vec{y}\in\mathbb{R}^n$. This is the vector of observed "actual values".  
- The **hypothesis vector** is the vector $\vec{h}\in\mathbb{R}^n$ with components $H(x_{i})$. This is the vector of predicted values.  
- The **error vector** is the vector $\vec{e}\in\mathbb{R}^n$ with components:  
$$e_{i}=y_{i}-H(x_{i})$$  
- **Key idea**: We can rewrite the mean squared error of $H$ as:  
$$R_{sq}(H) = \frac{1}{n} \sum_{n=1}^{n} (y_{i} - H(x_{i}))^{2} = \frac{1}{n} \Vert \vec{e} \Vert^{2} = \frac{1}{n} \Vert \vec{y} - \vec{h} \Vert^2$$  

### The hypothesis vector  

- The **hypothesis vector** is the vector $\vec{h}\in\mathbb{R}^n$ with components $H(x_{i})$. This is the vector of predicted values.  
- For the linear hypothesis function $H(x)=w_{0}+w_{1}x$, the hypothesis vector can be written:  
$$\vec{h}=\begin{bmatrix}w_{0}+w_{1}x_{1}\\w_{0}+w_{1}x_{2}\\\vdots\\w_{0}+w_{1}x_{n}\end{bmatrix}=$$  

### Rewriting the mean squared error  

- Define the **design matrix** $X\in\mathbb{R}^{n\times_{2}}$ as:  
$$X=\begin{bmatrix}1&x_{1}\\1&x_{2}\\\vdots&\vdots\\1&x_{n}\end{bmatrix}$$  
- Define the **parameter vector** $\vec{w}\in\mathbb{R}^2$ to be $\vec{w}=\begin{bmatrix}w_0\\w_1\end{bmatrix}$.  
- Then, $\vec{h}=X\vec{w}$, so the mean squared error becomes:  
$$R_{sq}(H)=\frac{1}{n}\Vert \vec{y}-\vec{h}\Vert^{2}\implies R_{sq}(\vec{w})=\frac{1}{n} \Vert \vec{y}-X\vec{w}\Vert^2$$  

### What's next?  

- To find the optimal model parameters for simple linear regression, $w_{0}^*$ and $w_{1}^*$, we previously minimized:  
$$R_{sq}(w_{0},w_{1})=\frac{1}{n}\sum_{i=1}^{n} (y_{i}-(w_{0}+w_{1}x_{i}))^{2}$$  
- Now that we've reframed the simple linear regression problem in terms of linear algebra, we can find $w_{0}^*$ and $w_{1}^*$ by minimizing:  
$$R_{sq}(\vec{w})=\frac{1}{n}\Vert \vec{y}-X\vec{w}\Vert^2$$  
- **We've already solved this problem! Assuming $X^TX$ is invertible, the best $\vec{w}$ is**:  
$$\vec{w}^*=(X^TX)^{-1}X^T\vec{y}$$  

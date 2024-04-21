---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/DSC_40A"
date:
- 2024-04-18
---
Source: https://dsc40a.com/resources/lectures/lec06/lec06-filled.pdf  

# Dot Products and Projections  

## Recap: Friends of the Simple Linear Regression Model  

## Dot products  

### Vectors  

- A **vector** in $\mathbb{R}^n$ is an **ordered collection of $n$ numbers**.  
- We use lower-case letters with an arrow on top to represent vectors, and we usually write vectors as **columns**.  
$$\vec{v} = \begin{bmatrix} 8 \\ 3 \\ -2 \\ 5 \end{bmatrix}$$  
- Another way of writing the above vector is $\vec{v} = [8,3,-2,5]^T$. (transpose)  
- Since $\vec{v}$ has four **components** ("elements"), we say $\vec{v} \in \mathbb{R}^4$.  

### The geometric interpretation of a vector  

- A vector $\vec{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix}$ is an arrow to the point $(v_1,v_2,\dots,v_n)$ from the origin.  
- The **length**, or $L_2$ **norm**, of $\vec{v}$ is:  
$$\Vert \vec{v} \Vert = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2 }$$  
- A vector is sometimes described as an object with a **magnitude/length** and **direction**.  

### Dot product: coordinate definition  

- The **dot product** of two vectors $\vec{u}$ and $\vec{v}$ in $\mathbb{R}^n$ is written as:  
$$\vec{u}\cdot\vec{v} = \vec{u}^T\vec{v}$$  
- The computational definition of the dot product:  
$$\vec{u}\cdot\vec{v} = \sum_{i=1}^n u_iv_i = u_1v_1 + u_2v_2 + \dots + u_nv_n$$  
- The result is a **scalar**, i.e. a single number.  

### Dot product: geometric definition  

- The computational definition of the dot product:  
$$\vec{u}\cdot\vec{v} = \sum_{i=1}^n u_iv_i = u_1v_1 + u_2v_2 + \dots + u_nv_n$$  
- The geometric definition of the dot product:  
$$\vec{u}\cdot\vec{v} = \Vert \vec{u} \Vert \Vert \vec{v} \Vert \cos{\theta}$$  
where $\theta$ is the angle between $\vec{u}$ and $\vec{v}$.  
- The two definitions are equivalent. This equivalence allows us to find the angle $\theta$ between two vectors.  

### Orthogonal vectors  

- Recall: $\cos{90\textdegree} = 0$  
- Since $\vec{u}\cdot\vec{v} = \Vert \vec{u} \Vert \Vert \vec{v} \Vert \cos{\theta}$, if the angle between two vectors is $90\textdegree$, their dog product is $\Vert \vec{u} \Vert \Vert \vec{v} \Vert \cos{90\textdegree} = 0$.  
- If the angle between two vectors is $90\textdegree$, we say they are perpendicular, or more generally, **orthogonal**.  
- **Key idea**:  
$$\text{two vectors are orthogonal} \iff \vec{u}\cdot\vec{v} = 0$$  

---  

## Spans and projections  

### Adding and scaling vectors  

- The sum of two vectors $\vec{u}$ and $\vec{v}$ in $\mathbb{R}^n$ is the **element-wise sum** of their components:  
$$\vec{u}+\vec{v} = \begin{bmatrix} u_1 + v_1 \\ u_2 + v_2 \\ \vdots \\ u_n + v_n \end{bmatrix}$$  
- If $c$ is a scalar, then:  
$$c\vec{v} = \begin{bmatrix} cv_1 \\ cv_2 \\ \vdots \\ cv_n \end{bmatrix}$$  

### Linear combinations  

- Let $\vec{v}_1,\vec{v}_2,\dots,\vec{v}_d$ be all vectors in $\mathbb{R}^n$.  
- A **linear combination** of $\vec{v}_1,\vec{v}_2,\dots,\vec{v}_d$ is any vector of the form:  
$$a_1\vec{v}_1 + a_2\vec{v}_2 + \dots + a_d\vec{v}_d$$  
where $a_1,a_2,\dots,a_d$ are all scalars.  

### Span  

- Let $\vec{v}_1,\vec{v}_2,\dots,\vec{v}_d$ all be vectors in $\mathbb{R}^n$.  
- The **span** of $\vec{v}_1,\vec{v}_2,\dots,\vec{v}_d$ is the set of all vectors that can be created using linear combinations of those vectors.  
- Formal definition:  
$$\text{span}(\vec{v}_1,\vec{v}_2,\dots,\vec{v}_d)=\{a_1,\vec{v}_1+a_2\vec{v}_2+\dots+a_d\vec{v}_d:a_1,a_2,\dots,a_d\in\mathbb{R}\}$$  

### Projecting onto a single vector  

- Let $\vec{x}$ and $\vec{y}$ be two vectors in $\mathbb{R}^n$.  
- The span of $\vec{x}$ is the set of all vectors of the form:  
$$w\vec{x}$$  
where $w\in\mathbb{R}$ is a scalar.  
- **Question**: What vector in $\text{span}(\vec{x})$ is closest to $\vec{y}$?  
- The vector in $\text{span}(\vec{x})$ that is closest to $\vec{y}$ is the **projection of $\vec{y}$ onto** $\text{span}(\vec{x})$.  

### Projection error  

- Let $\vec{e}=\vec{y}-w\vec{x}$ be the **projection error**: that is, the vector that connects $\vec{y}$ to $\text{span}(\vec{x})$.  
- **Goal: Find the $w$ that makes $\vec{e}$ as short as possible.**  
- That is, minimize:  
$$\Vert\vec{e}\Vert$$  
- Equivalently, minimize:  
$$\Vert \vec{y} - w\vec{x} \Vert$$  
- **Idea**: To make $\vec{e}$ as short as possible, it should be **orthogonal to $w\vec{x}$.  

### Minimizing projection error  

- **Goal: Find the $w$ that makes $\vec{e}=\vec{y}-w\vec{x}$ as short as possible**.  
- **Idea**: To make $\vec{e}$ as short as possible, it should be **orthogonal to $w\vec{x}$**.  
- Can we prove that making $\vec{e}$ orthogonal to $w\vec{x}$ minimizes $\Vert \vec{e} \Vert$?  

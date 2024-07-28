---
id: MATH 20D Lecture 13
aliases: []
tags:
- Type/Note
- Topic/Differential_Equations
- Class/MATH_20D
date:
- "2024-02-07"
---
# Reduction of Order  

> [!note] Reduction of Order  
> If we have an equation of the form $$y''(t)+p(t)y'(t)+q(t)y=0$$ and are given one solution $y_1$ (not identically zero).  
> We can find $y_2$ of the form $$y_2(t)=v(t)y_1(t)$$ where  
> $$v(t)=\int\frac{1}{y_1^2(t)}exp\left(-\int p(t)\right)dt=\int\frac{1}{y_1^2(t)}e^{-\int p(t)dt}$$  

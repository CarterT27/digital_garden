---
tags:
- "Type/Note"
- "Topic/Calculus"
- "Class/MATH_20C"
date:
- 2024-03-13
---
# 15.2  

> [!note] Evaluate $\int\int\limits_{D}e^{x+y}\,dA$ over $D$ defined by $x\geq1,y\geq1,x+y\leq5$  
> $\int\int\limits_De^{x+y}\,dA=\int_1^4\int_1^{5-x}e^{x+y}\,dy\,dx$  
> $=\int_1^4e^{x+y}\vert_{y=1}^{5-x}\,dx$  
> $=\int_1^4(e^5-e^{x+1})\,dx$  
> $=(e^5x-e^{x+1})\vert_{x=1}^4$  
> $=(e^5\cdot4-e^5)-(e^5-e^2)$  
> $=3e^5-e^5+e^2$  
> $=2e^5+e^2$  

> [!note] $D=\left\{(x,y)\vert c\leq y\leq d,h_1(y)\leq x\leq h_2(y)\right\}$  
> - The horizontal strips are labeled by their y-values  
> - The range of the horizontal strips is from $c$ to $d$  
> - For the horizontal strip at $y$, the bounds for x values are from $h_1(y)$ to $h_2(y)$  
> $\int\int\limits_Df(x,y)\,dA=\int_c^d\int_{h_1(y)}^{h_2(y)}f(x,y)\,dx\,dy$  

$$\int_a^b\int_c^df(x,y)\,dy\,dx=\int_c^d\int_a^bf(x,y)\,dx\,dy$$  

> [!note] Change of order  
> $\int_0^4\int_{\frac{x}{2}}^2e^{y^2}\,dy\,dx\neq\int_\frac{x}{2}^2\int_0^4e^{y^2}\,dx\,dy$  
> $\int_0^4\int_{\frac{x}{2}}^2e^{y^2}\,dy\,dx=\int_0^2\int_0^{2y}e^{y^2}\,dx\,dy$  

> [!note] Find the volume $V$ of the region under the plane $z=2x+3y$ over the triangle $D$ bounded by $y=\frac{x}{2},y=x,y=2$  
> $V=\int\int\limits_D(2x+3y)\,dA$  
> $=\int_0^2\int_\frac{x}{2}^x(2x+3y)\,dy\,dx+\int_2^4\int_\frac{x}{2}^2(2x+3y)\,dy\,dx$  
> or  
> $=\int_0^2\int_y^{2y}(2x+3y)\,dx\,dy$  
> $=\int_0^2(x^2+3xy)\vert_{x=y}^{2y}\,dy$  
> $\dots$  
> $=16$  

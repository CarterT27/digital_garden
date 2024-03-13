---
tags:
- "Type/Note"
- "Topic/Calculus"
- "Class/MATH_20C"
date:
- 2024-03-11
---
# 15.2 - Double Integral Over More General Regions  

> [!note] Theorem  
> Let $f(x,y)$ be a continuous on $R=[a,b]\times[c,d]$. Suppose $f(x,y)=g(x)h(y)$ is a product. Then  
> $$\int\int\limits_Df(x,y)\,dA=\left(\int_a^bg(x)\,dx\right)\left(\int_c^dh(y)\,dy\right)$$  
> Proof: $\int\int\limits_R g(x)h(y)\,dA$  
> $=\int_a^b\int_c^dg(x)h(y)\,dy\,dx$  
> $=\int_a^bg(x)\left(\int_c^dh(y)\,dy\right)\,dx$  
> $=\left(\int_c^dh(y)\,dy\right)\left(\int_a^bg(x)\,dx\right)$  

> [!note] Example. $\int\int\limits_R\frac{x}{y}\,dA$ over $R=[-1,2]\times[1,2]$  
> $\int\int\limits_R x\frac{1}{y}\,dA$  
> $=\left(\int_{-1}^2x\,dx\right)\left(\int_1^2\frac{1}{y}\,dy\right)$  
> $=\left(\frac{4}{2}-\frac{1}{2}\right)\left(\ln{2}-\ln{1}\right)$  
> $=\frac{3}{2}\ln{2}$  

> [!note] $D$ Domain  
> $\int\int\limits_{D} f(x,y)\,dA$ = volume under the graph of $f(x,y)$ and over $D$  
> One can define it precisely using Riemann sum.  

> [!note] Theorem  
> Assume that $f(x,y)$ and $g(x,y)$ are integrable on a domain $D$. Then  
> 1. $\int\int\limits_D\left(f(x,y)+g(x,y)\right)\,dA$  
>   $=\int\int\limits_D f(x,y)\,dA+\int\int g(x,y)\,dA$  
> 2. For any constant $c$  
>   $\int\int\limits_D cf(x,y)\,dA=c\int\int\limits_D f(x,y)\,dA$  
> 3. $\int\int\limits_{D} c\,dA=c\text{ Area}(D)$  

> [!note] Regions between two graphs  
> $D=\{(x,y)\vert a\leq x\leq b,g_1(g)\leq y\leq g_2(x)\}$  
> - Each vertical strip is labeled by its x-coord  
> - The range of the vertical strips is from $a$ to $b$  
> - For a vertical strip at $x$ the bounds for $y$ are from $g_1(x)$ to $g_x(x)$  
> $$\int\int\limits_{D}f(x,y)\,dA=\int_a^b\int_{g_1(x)}^{g_2(x)}f(x,y)\,dy\,dx$$  

> [!note] Example. Evaluate $\int\int\limits_De^{x+y}\,dA$ over $D$ defined by $x\geq1,y\geq1,x+y\leq5$  
> $\int\int\limits_De^{x+y}\,dA=\int_1^4\int_1^{5-x}e^{x+y}\,dy\,dx$  
> Finish the computation next time...  

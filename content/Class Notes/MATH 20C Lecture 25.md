---
tags:
- "Type/Note"
- "Topic/Calculus"
- "Class/MATH_20C"
date:
- 2024-03-08
---
# 15.1 Double Integral  

---  

Recall $R=[a,b]\times[c,d]$  
$=\left\{(x,y)\vert a\leq x\leq b,c\leq y\leq d\right\}$  
Double Integral $\int\int\limits_R f(x,y)dA=$ the volume under the graph of $f(x,y)$ over $R$  

---  

Now let's define the double integral using Riemann Sum  

Step 1 (subdivisions):  
- Subdivide $[a,b]$ into $N$ subintervals of the same length $\frac{b-a}{N}$  
- Subdivide $[c,d]$ into $M$ subintervals of the same length $\frac{d-c}{M}$  
This creates an $N\times M$ grid of subrectangles $R_{ij}$ in $R$.  

Step 2:  
Choose a sample point $f_{ij}$ in each $R_{ij}$  

Step 3:  
Volume under the graph over $R_{ij}$  
$\approx f(p_{ij})\Delta A=f(p_{ij})\Delta x\Delta y$  
Define the Riemann Sum  
$S_{NM}=\sum_{i=1}^N\sum_{j=1}^M f(p_{ij})\Delta A$  
This approximates the volume under the graph of $f(x,y)$ over $R$  

> [!definition] Double Integral of $f(x,y)$  
> The double integral of $f(x,y)$ over a rectangle $R$ is defined by $\int\int\limits_R f(x,y)dA=\lim_{N,M\to\infty}\sum_{i=1}^N\sum_{j=1}^M f(p_{ij})\Delta A$  
> If the limit exists, we say $f(x,y)$ is **integrable** over $R$  

> [!note] Fact  
> If $f(x,y)$ is **continuous** on $R$, then $f(x,y)$ is integrable on $R$.  

> [!note] Example. $f(x,y)$ $R=[1,4]\times[1,3]$ $N=3,M=2$  
> Riemann sum  
> $=f(1,1)\Delta A+f(2,1)\Delta A+f(3,1)\Delta A+f(1,2)\Delta A+f(2,2)\Delta A+f(3,2)\Delta A$  
> $=\Delta A(f(1,1)+f(2,1)+f(3,1)+f(1,2)+f(2,2)+f(3,2))$  

> [!note] Theorem  
> Assume that $f(x,y)$ and $g(x,y)$ are continuous over a rectangle $R$. Then  
> 1. $\int\int\limits_R(f(x,y)+g(x,y))\,dA$  
>   $=\int\int\limits_R f(x,y)\,dA+\int\int\limits_R g(x,y)\,dA$  
> 2. For any constant $c$  
>   $\int\int\limits_R cf(x,y)\,dA=c\int\int\limits_R f(x,y)\,dA$  
> 3. $\int\int\limits_R c\,dA=c \text{ Area}(R)$  
>   $dA\to \,dx\,dy,\Delta A\to\Delta x\Delta y$  

> [!note] How to compute double integrals?  
> Iterated integrals $R=[a,b]\times[c,d]=x\times y$  
> $\int_{x=a}^b\int_{y=c}^d f(x,y)dydx=\int_a^b\int_c^d f(x,y)\,dy\,dx$  
> View $x$ as a constant for the inner integral and integrate $y$  
> $\int_{y=c}^d f(x,y)dy$ is a function of $x$  
> $\int_{y=c}^d\int_{x=a}^b f(x,y)dxdy=\int_c^d\int_a^b f(x,y)\,dx\,dy$  
> View $y$ as a constant for the inner integral and integrate $x$  
> $\int_a^b f(x,y)dx$ is a function in $y$  

> [!note] Example. $\int_{x=0}^1\int_{y=0}^{\frac{\pi}{6}}x^3\cos{y}\,dy\,dx$  
> $=\int_{x=0}^1(x^3\sin{y}\vert_{y=0}^{\frac{\pi}{6}}\,dx$  
> $=\int_{x=0}^1(x^3\sin{\frac{\pi}{6}}-x^3\sin{0})\,dx$  
> $=\int_{x=0}^1\frac{x^3}{2}\,dx$  
> $=\frac{x^4}{8}\vert_{x=0}^1=\frac{1}{8}$  

> [!note] Example. $\int_0^1\int_0^2(x^2-\sin{y})\,dx\,dy$  
> $=\int_0^1(\frac{x^3}{3}-x\sin{y})\vert_{x=0}^2\,dy$  
> $=\int_0^1(\frac{8}{3}-2\sin{y})\,dy$  
> $=(\frac{8}{3}y+2\cos{y})\vert_{y=0}^1$  
> $=\frac{8}{3}+2\cos{1}-(0+2\cos{0})$  
> $=\frac{2}{3}+2\cos{1}$  

> [!definition] Fubini's Theorem  
> Let $f(x,y)$ be a continuous function on $R=[a,b]\times[c,d]$  
> $\int\int\limits_R f(x,y)\,dA=\int_a^b\int_c^d f(x,y)\,dy\,dx$  
> $=\int_c^d\int_a^b f(x,y)\,dx\,dy$  

$S(x_0)=\int_c^d f(x_0,y)\,dy$  
$S(y_0)=\int_a^b f(x,y_0)\,dx$  

> [!note] Example. Evaluate $\int\int xe^{xy}\,dA$ where $R=[0,1]\times[0,1]$  
> $\int_0^1\int_0^1 xe^{xy}\,dx\,dy$  
> $\int_0^1\int_0^1 xe^{xy}\,dy\,dx$  
> Second double integral is easier  
> $\int_0^1 (e^{xy})\vert_{y=0}^1\,dx$  
> $=\int_0^1 (e^x-e^0)\,dx$  
> $=\int_0^1 (e^x-1)\,dx$  
> $=(e^x-x)\vert_{x=0}^1$  
> $=(e-1)-(e^0-0)$  
> $=e-2$  

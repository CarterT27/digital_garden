---
tags:
- "Type/Note"
- "Topic/Differential_Equations"
- "Class/MATH_20D"
date:
- 2024-03-08
---
> [!note] Example. Use Laplace transform to solve the system  
> $$\begin{bmatrix}x'(t)\\y'(t)\end{bmatrix}=\begin{bmatrix}-4&13\\-1&2\end{bmatrix}\begin{bmatrix}x(t)\\y(t)\end{bmatrix},\begin{bmatrix}x(0)\\y(0)\end{bmatrix}=\begin{bmatrix}1\\-1\end{bmatrix}$$  
> Apply Laplace Transform to both equations  
> $\begin{cases}\mathcal{L}\{x'\}=-4\mathcal{L}\{x\}+13\mathcal{L}\{y\}\\\mathcal{L}\{y'\}=-\mathcal{L}\{x\}+2\mathcal{L}\{y\}\end{cases}\Rightarrow\begin{cases}s\mathcal{L}\{x\}-x(0)=-4\mathcal{L}\{x\}+13\mathcal{L}\{y\}\\s\mathcal{L}\{y\}-y(0)=-\mathcal{L}\{x\}+2\mathcal{L}\{y\}\end{cases}$  
> $\Rightarrow\begin{cases}(s+4)\mathcal{L}\{x\}-13\mathcal{L}\{y\}=1\\\mathcal{L}\{x\}+(s-2)\mathcal{L}\{y\}=-1\end{cases}\to$ augmented matrix $\begin{bmatrix}(s+4)&-13&|&1\\1&(s-2)&|&-1\end{bmatrix}$  
>  
> Multiply 2nd equation by $s+4$ then subtract the first  
$\begin{cases}(s+4)\mathcal{L}\{x\}-13\mathcal{L}\{y\}=1\\(s+4)\mathcal{L}\{x\}+(s+4)(s-2)\mathcal{L}\{y\}=-(s+4)\end{cases}$  
> $\left[(s+4)(s-2)+13\right]\mathcal{L}\{y\}=-(s+4)-1$  
> $\Rightarrow(s^2+2s+5)\mathcal{L}\{y\}=-s-5\Rightarrow\mathcal{L}\{y\}=\frac{-s-5}{s^2+2s+5}$  
>  
> So $\mathcal{L}\{x\}=-1-(s-2)\mathcal{L}\{y\}=-1+\frac{(s+5)(s-2)}{s^2+2s+5}=\frac{s-15}{s^2+2s+5}$  
>  
> Now we find inverse Laplace transform of $\frac{s-15}{s^2+2s+5}$ and $\frac{-s-5}{s^2+2s+5}$  
>  
> Bottom = $s^2+2s+5=s^2+2s+1+4=(s+1)^2+2^2$  
>  
> Let's inverse $\frac{s-15}{s^2+2s+5}=A_1\left[\frac{(s+1)}{(s+1)^2+4}\right]+A_2\left[\frac{2}{(s+1)^2+4}\right]$  
> $\Rightarrow s-15=A_1(s+1)+2A_2=A_1s+(A_1+2A_s)$  
> So $A_1=1$ and $A_1+2A_2=-15\Rightarrow A_2=-8$  
> $\Rightarrow\mathcal{L}\{x\}=\mathcal{L}\{e^{-t}\cos{2t}\}-8\mathcal{L}\{e^{-t}\sin{2t}\}$  
> $x=\mathcal{L}^{-1}\{\frac{s-15}{s^2+2s+5}\}=e^{-t}\cos{2t}-8e^{-t}\sin{2t}$  
> You try to inverse $\frac{-s-5}{s^2+2s+5}$ to get $y=-e^{-t}\cos{2t}-2e^{-t}\sin{2t}$  

---  

$x(t)$: population of fish in a lake at time $t$ (in years)  

Simplest logistic Equation: $x'(t)=kx(t), (k>0)$ and $x(0)=A$ (some constant)  

Suppose we want to restock the fish at a constant rate of $r$ unit of fish per year.  
New equation: $x'(t)=kx(t)+r\Rightarrow x'-kx=r$.  
We can easily solve this new equation.  

---  

What if we run out of money and restocking program ends after just 6 months?  

$x'-kx=f(t)$ where $f(t)=\begin{cases}r\text{ for }0\leq t\lt\frac{1}{2}\\0\text{ for }\frac{1}{2}\leq t\end{cases}$  

What if during the 2nd half of the year, we fundraise enough to restart restocking fish and we can restock the fish at rate $r_2$ (unit of fish per year) for another 4 months  

$x'-kx=g(t)$ where $g(t)=\begin{cases}r\text{ for }0\leq t\lt\frac{1}{2}\\0\text{ for }\frac{1}{2}\leq t\lt1\\r_2\text{ for }1\leq t\lt\frac{4}{3}\\0\text{ for }\frac{4}{3}\leq t\end{cases}$  

# 7.6 - Laplace Transform of Unit Step Functions  

> [!definition] Heaviside/Unit step function  
> The **heaviside step function** or **unit step function**, denoted $u$ is a discontinuous function defined by  
> $$u(x)=\begin{cases}0,x<0\\1,x\geq0\end{cases}$$  

> [!note] Example. Let $c>0$. Express the following function in terms of the unit step functions  
> $$u(t-c)=\begin{cases}0,t<c\\1,t\geq c\end{cases}$$  

> [!note] Example. Express the following in terms of the unit step functions:  
> $$f(t)=\begin{cases}-2,t<1\\1,1\leq t<3\\-5,3\leq t\end{cases}$$  
>  
> $f(t)=Au(t-1)+Bu(t-3)+C$  
> When $t<1$: $LHS=f(t)=-2$  
> $u(t-1)=u(t-3)=0\Rightarrow RHS=c\Rightarrow c=-2$  
> When $1\leq t<3$: $LHS=1$  
> $u(t-1)=1$ but $u(t-3)=0\Rightarrow RHS=A+C=A-2\Rightarrow A=3$  
> When $3\leq t$: $LHS=-5$  
> $u(t-1)=u(t-3)=1$ so $RHS=A+B+C\Rightarrow B=-6$  
> $\Rightarrow f(t)=-2+3u(t-1)-6u(t-3)$  

> [!note] Theorem.  
> For $a>0,\mathcal{L}\{u(t-a)f(t)\}=e^{-as}\mathcal{L}\{f(t+a)\}$  
> $u(t-a)f(t)=\begin{cases}0,t<a\\f(t),t\geq a\end{cases}$  
> $\mathcal{L}\{u(t-a)f(t)\}=\int_0^\infty e^{-st}u(t-a)f(t)\,dt=\int_0^a e^{-st}(0)\,dt+\int_a^\infty e^{-st}f(t)\,dt$  
> We make the substitution $t=x+a$ so when $t=a,x=0$ and $dt=dx$.  
> Thus, $\int_a^\infty e^{-st}f(t)\,dt=\int_0^\infty e^{-s(x+a)}f(x+a)\,dx$  
> $=\int_0^\infty e^{-sx}e^{-sa}f(x+a)\,dx$  
> $=e^{-as}\int_0^\infty e^{-sx}f(x+a)\,dx$  
> $=e^{-as}\int_0^\infty e^{-st}f(t+a)\,dt$  
> $=e^{-as}\mathcal{L}\{f(t+a)\}$  
> $\mathcal{L}\{u(t-a)f(t)\}=e^{-as}\mathcal{L}\{f(t+a)\}$  

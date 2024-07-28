---
tags:
- "Type/Note"
- "Topic/Differential_Equations"
- "Class/MATH_20D"
date:
- 2024-03-01
---
> [!note] Example. Let $f(t)$ be a function with Laplace transform $\mathcal{L}\{f(t)\}=F(s)$. Find $\mathcal{L}\{tf(t)\}$ in terms of $F(s)$.  
> $\mathcal{L}\{tf(t)\}(s)=\int_0^\infty e^{-st}tf(t)dt=\int_0^\infty(te^{-st})f(t)dt$  
> $=\int_0^\infty\left(-\frac{\partial}{\partial s}e^{-st}\right)f(t)dt$  
> $=-\frac{\partial}{\partial s}\left[\int_0^\infty e^{-st}f(t)dt\right]=-\frac{\partial}{\partial s}\left[\mathcal{L}\{f(t)\}(s)\right]$  
> $=-\frac{d}{ds}\left[\mathcal{L}\{f(t)\}(s)\right]$  
> So $\mathcal{L}\{tf(t)\}(s)=-\frac{d}{ds}\mathcal{L}\{f\}(s)$  
> $\mathcal{L}\{t\}(s)=\frac{1}{s^2}\Rightarrow\mathcal{L}\{t^2\}(s)=-\frac{d}{ds}\left[\mathcal{L}\{t\}(s)\right]=-\frac{d}{ds}\left(\frac{1}{s^2}\right)=\frac{2}{s^3}$  
> $\mathcal{L}\{t^3\}(s)=-\frac{d}{ds}\left[\mathcal{L}\{t^2\}(s)\right]=-\frac{d}{ds}\left(\frac{2}{s^3}\right)=\frac{2\cdot3}{s^4}$  
> $\mathcal{L}\{t^4\}(s)=-\frac{d}{ds}\left[\mathcal{L}\{t^3\}(s)\right]=-\frac{d}{ds}\left(\frac{2\cdot3}{s^4}\right)=\frac{2\cdot3\cdot4}{s^5}$  
> $\vdots$  
> $\mathcal{L}\{t^n\}(s)=\frac{2\cdot3\cdot4\dots\cdot n}{s^{n+1}}=\frac{n!}{s^{n+1}}$  

> [!note] Example. Let $f(t)$ be a function with Laplace transform $\mathcal{L}\{f(t)\}=F(s)$. Find $\mathcal{L}\{e^{at}f(t)\}$ in terms of $F(s)$ for any fixed $a$.  
> $\mathcal{L}\{e^{at}f(t)\}(s)=\int_0^\infty e^{-st}e^{at}f(t)dt=\int_0^\infty e^{-(s-a)t}f(t)dt$  
> Recall, $F(s)=\mathcal{L}\{f(t)\}(s)=\int_0^\infty e^{-st}f(t)dt$  
> Replace $s$ by $s-a$ in this formula  
> $F(s-a)=\int_0^\infty e^{-(s-a)t}f(t)dt$  
> Thus, $\mathcal{L}\{e^{at}f(t)\}(s)=F(s-a)$ where $F(s)=\mathcal{L}\{f(t)\}(s)$  
> "Shift the transform of $f(t)$ by a unit" (i.e. replace $s$ in $F(s)$ by $s-a$)  

> [!note] Examples  
> 1. $\mathcal{L}\{\cos{bt}\}=\frac{s}{s^2+b^2}$ for $s>0$.  
>   $\mathcal{L}\{e^{at}\cos{bt}\}=\frac{s-a}{(s-a)^2+b^2}$ for $s-a>0$ or $s>a$  
> 2. $\mathcal{L}\{e^{2t}\sin{t\sqrt{3}}\}(s)$  
>   Here $\mathcal{L}\{\sin{t\sqrt{3}}\}=\frac{\sqrt{3}}{s^2+(\sqrt{3})^2}=\frac{\sqrt{3}}{s^2+3}$ for $s>0$  
>   $\mathcal{L}\{e^{2t}\sin{t\sqrt{3}}\}=\frac{\sqrt{3}}{(s-2)^2+3}$ for $s-2>0$ or $s>2$  
> 3. $\mathcal{L}\{t^ne^{-3t}\}$  
>   First $\mathcal{L}\{t^n\}=\frac{n!}{s^{n+1}}$ for $s>0$  
>   $a=-3$ so $\mathcal{L}\{e^{-3t}t^n\}=\frac{n!}{(s+3)^{n+1}}$ for $s+3>0$ or $s>-3$  

> [!note] Example. Let $f(t)$ be a function with Laplace transform $\mathcal{L}\{f(t)\}$. Find $\mathcal{L}\{f'(t)\}$ and $\mathcal{L}\{f''(t)\}$  
> $\mathcal{L}\{f'(t)\}=\int_0^\infty e^{-st}f'(t)dt=e^{-st}f(t)\vert_{t=0}^{t=\infty}+s\int_0^\infty e^{-st}f(t)dt$  
>  
> $e^{-st}f(t)\vert_{t=0}^{t=\infty}=\left[\lim_{k\to\infty}e^{-sk}f(k)\right]-f(0)$  
> When $s\leq0$, the limit D.N.E but when $s>0$, this limit $\to0$  
> Thus, when $s>0$, $e^{-st}f(t)\vert_{t=0}^{t=\infty}=-f(0)$  
>  
> $s\int_0^\infty e^{-st}f(t)dt=s\mathcal{L}\{f\}$  
> Therefore, when $s>0$, $\mathcal{L}\{f'\}=s\mathcal{L}\{f\}-f(0)$  
>  
> $f''=$ deriv. of $f'$  
> $\mathcal{L}\{f''\}=s\mathcal{L}\{f'\}-f'(0)$  
> $=s(s\mathcal{L}\{f\}-f(0))-f'(0)$  
> $=s^2\mathcal{L}\{f\}-sf(0)-f'(0)$ for $s>0$  
>  
> $\mathcal{L}\{f'''\}=s\mathcal{L}\{f''\}-f''(0)$  
> $=s\left[s^2\mathcal{L}\{f\}-sf(0)-f'(0)\right]-f''(0)$  
> $=s^3\mathcal{L}\{f\}-s^2f(0)-sf'(0)-f''(0)$ for $s>0$  
>  
> $\mathcal{L}\{f^{(n)}\}=s^n\mathcal{L}\{f\}-s^{n-1}f(0)-s^{n-2}f'(0)-s^{n-3}f''(0)-\dots-sf^{(n-2)}(0)-f^{(n-1)}(0)$ for $s>0$  

## Summary. Our results so far  

| $f(t)=\mathcal{L}^{-1}\{F(s)\}$ | $F(s)=\mathcal{L}\{f(t)\}$ |  
| --- | --- |  
| $1$ | $\frac{1}{s},s>0$ |  
| $e^{at}$ | $\frac{1}{s-a},s>a$ |  
| $t^n$ | $\frac{n!}{s^{n+1}},s>0$ |  
| $t^ne^{at}$ | $\frac{n!}{(s-a)^{n+1}},s>a$ |  
| $\sin{\omega t}$ | $\frac{\omega}{s^2+\omega^2},s>0$ |  
| $\cos{\omega t}$ | $\frac{s}{s^2+\omega^2},s>0$ |  
| $e^{at}\sin{\omega t}$ | $\frac{\omega}{(s-a)^2+\omega^2},s>a$ |  
| $e^{at}\cos{\omega t}$ | $\frac{s-a}{(s-a)^2+\omega^2},s>a$ |  
| $f'(t)$ | $sF(s)-f(0)$ |  
| $f''(t)$ | $s^2F(s)-sf(0)-f'(0)$ |  
| $f^{(n)}(t)$ | $s^nF(s)-s^{n-1}f(0)-s^{n-2}f'(0)-\dots-sf^{(n-2)}(0)-f^{(n-1)}(0)$ |  

If $F(S)=\mathcal{L}\{f(t)\}$ then  
- $\mathcal{L}\{tf(t)\}=-F'(s)$ and  
- $\mathcal{L}\{e^{at}f(t)\}=F(s-a)$  

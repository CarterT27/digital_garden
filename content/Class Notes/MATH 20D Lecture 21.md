---
tags:
- "Type/Note"
- "Topic/Differential_Equations"
- "Class/MATH_20D"
date:
- 2024-02-28
---
# Chapter 7 - Laplace Transform  

## Section 7.2 & 7.3 - Definition and Properties of Laplace Transform  

> [!definition] Laplace Transform  
> Given a function $f(t)$ defined for all $t\geq0$, then the Laplace Transform of $f$ is given by  
> $$\mathcal{L}\{f\}(s)=\int_0^\infty e^{-st}f(t)dt$$  

Reason to use Laplace Transform  
ODE $\to$ Soln to given ODE is hard  
ODE $\to$ Algebraic Equation $\to$ Soln to Algebraic Equation $\to$ Soln to Given ODE is easier  
Going from Soln to the Algebraic Equation to Soln to Given ODE requires an Inverse Laplace Transform  

> [!note] Fact  
> Let $k,a>0$. If $f$ is piecewise continuous and $\vert f(t)\vert\leq ke^{\alpha t}$ for $t$ "big enough" then the Laplace transform $\mathcal{L}\{f\}(s)$ exists for all $s>a$.  
> In addition, Laplace transform is a **linear operator**: for any functions $f,g,\text{ and scalar }c$:  
> $$\mathcal{L}\{f+g\}=\mathcal{L}\{f\}+\mathcal{L}\{g\}\text{ and }\mathcal{L}\{cf\}=c\mathcal{L}\{f\}$$  
> provided that each transformation $\mathcal{L}\{f\},\mathcal{L}\{g\}$ exists.  

> [!note] Example. Let $f(t)=e^{at}$. Find $\mathcal{L}\{f\}$.  
> $\mathcal{L}\{e^{at}\}(s)=\int_0^\infty e^{-st}e^{at}dt=\int_0^\infty e^{(a-s)t}dt=\frac{1}{a-s}e^{(a-s)t}\vert_{t=0}^{t=\infty}$  
> $=[\lim_{k\to\infty}\frac{1}{a-s}e^{(a-s)k}]-\frac{1}{a-s}e^{(a-s)(0)}$  
> $=[\lim_{k\to\infty}\frac{1}{a-s}e^{(a-s)k}]+\frac{1}{s-a}$  
> If $a-s\geq0$ (or equivalently, $s\leq a$), then limit D.N.E. As a result, Laplace transform also D.N.E.  
> If $a-s<0$ (or $s>a$) then this limit is 0, and thus, the transform is now $\mathcal{L}\{e^{\alpha t}\}(s)=\frac{1}{s-a}$  
> Therefore: $\mathcal{L}\{e^{\alpha t}\}(s)=\frac{1}{s-a}$ whenever $s>a$  

> [!note] Example. Let $f(t)=1$. Find $\mathcal{L}\{f\}$.  
> $\mathcal{L}\{1\}(s)=\int_0^\infty e^{-st}(1)dt=\int_0^\infty e^{-st}dt=-\frac{1}{s}e^{-st}\vert_{t=0}^{t=\infty}$  
> $=[\lim_{k\to\infty}-\frac{1}{s}e^{-sk}]+\frac{1}{s}$  
> If $s\leq0$ then limit D.N.E.  
> If $s>0$ then limit = 0 making $\mathcal{L}\{1\}(s)=\frac{1}{s}$  
> $\mathcal{L}\{1\}(s)=\frac{1}{s}$, for $s>0$  
> A "smarter way" to derive this formula is to let $a=0$ in the previous formula.  

> [!note] Example. Let $f(t)=t$. Find $\mathcal{L}\{f\}$.  
> $\mathcal{L}\{t\}(s)=\int_0^\infty e^{-st}tdt=-\frac{t}{s}e^{-st}\vert_{t=0}^{t=\infty}+\frac{1}{s}\int_0^\infty e^{-st}dt$  
> $=[\lim_{k\to\infty}-\frac{k}{s}e^{-sk}]-(0)+\frac{1}{s^2}$  
> When $s\leq0$, limit & Laplace transform D.N.E.  
> When $s>0$, limit $\to$ 0 making $\mathcal{L}\{t\}(s)=\frac{1}{s^2}$  
> So $\mathcal{L}\{t\}(s)=\frac{1}{s^2}$, for $s>0$  

Euler's formula: $e^{i\theta}=\cos\theta+i\sin\theta$  
If $\theta=at$:  
$e^{iat}=\cos{at}+i\sin{at}$  
$t:=-t$:  
$e^{-iat}=\cos{-at}+i\sin{-at}$  
$=\cos{at}-i\sin{at}$  

$e^{iat}+e^{-iat}=2\cos{at}\Rightarrow\cos{at}=\frac{1}{2}(e^{iat}+e^{-at})$  
$e^{iat}-e^{-iat}=2i\sin{at}\Rightarrow\sin{at}=\frac{1}{2i}(e^{iat}-e^{-iat})$  

> [!note] Example. Let $f(t)=\sin{at}$ and $g(t)=\cos{at}$. Find $\mathcal{L}\{f\}$ and $\mathcal{L}\{g\}$.  
> $\mathcal{L}\{\sin{at}\}(s)=\int_0^\infty e^{-st}\sin{at}dt=\int_0^\infty \frac{1}{2i}(e^{iat}-e^{-iat})dt$  
> $=\frac{1}{2i}\int_0^\infty e^{-st}e^{iat}dt-\frac{1}{2i}\int_0^\infty e^{-st}e^{-iat}dt$  
> $=\frac{1}{2i}\mathcal{L}\{e^{iat}\}-\frac{1}{2i}\mathcal{L}\{e^{-iat}\}$  
> $=\frac{1}{2i}\frac{1}{s-ia}-\frac{1}{2i}\frac{1}{s+ia}$  
> $=\frac{1}{2i}[\frac{(s+ia)-(s-ia)}{(s-ia)(s+ia)}]=\frac{1}{2i}\frac{2ia}{s^2+a^2}=\frac{a}{s^2+a^2}$  
> $\mathcal{L}\{\sin{at}\}(s)=\frac{a}{s^2+a^2}$, for $s>0=Re(\pm ia)$  
>  
> $\mathcal{L}\{\cos{at}\}(s)=\int_0^\infty e^{-st}\cos{at}dt=\int_0^\infty e^{-st}\frac{1}{2}(e^{iat}+e^{-iat})dt$  
> $=\frac{1}{2}\left[\int_0^\infty e^{-st}e^{iat}dt+\int_0^\infty e^{-st}e^{-iat}dt\right]$  
> $=\frac{1}{2}\left[\mathcal{L}\{e^{iat}\}(s)+\mathcal{L}\{e^{-iat}\}(s)\right]=\frac{1}{2}\left(\frac{1}{s-ia}+\frac{1}{s+ia}\right)$  
> $=\frac{1}{2}\frac{(s+ia)+(s-ia)}{(s-ia)(s+ia)}=\frac{2s}{2(s^2+a^2)}=\frac{s}{s^2+a^2}$ for $s>0$  
> $\mathcal{L}\{\cos{at}\}(s)=\frac{s}{s^2+a^2}$, for $s>0$  

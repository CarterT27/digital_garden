---
tags:
- "Type/Note"
- "Topic/Differential_Equations"
- "Class/MATH_20D"
date:
- 2024-03-11
---
> [!note] Theorem.  
> For $a>0,\mathcal{L}\{u(t-a)f(t)\}=e^{-as}\mathcal{L}\{f(t+a)\}$.  
> Proof:  
> $\mathcal{L}\{u(t-a)f(t)\}=\int_0^\infty e^{-st}u(t-a)f(t)\,dt=\int_0^ae^{-st}(0)\,dt+\int_a^\infty e^{-st}f(t)\,dt$  
> We make the subs. $t=x+a$ so when $t=a,x=0$ and $dt=dx$.  
> Thus, $\int_a^\infty e^{-st}f(t)\,dt=\int_0^\infty e^{-s(x+a)}f(x+a)\,dx$  
> $=\int_0^]infty e^{-sx}e^{-sa}f(x+a)\,dx$  
> $=e^{-as}\int_0^\infty e^{-sx}f(x+a)\,dx$  
> $=e^{-as}\int_0^\infty e^{-st}f(t+a)\,dt$  
> $=e^{-as}\mathcal{L}\{f(t+a)\}$  
> $\mathcal{L}\{u(t-a)f(t)\}=e^{-as}\mathcal{L}\{f(t+a)\}$  

> [!note] Example. Find the Laplace transform of the function $f(t)=\begin{cases}-2,t<1\\1,1\leq t<3\\-5,3\leq t\end{cases}$  
> $f(t)=-2+3u(t-1)-6u(t-3)$  
> $\Rightarrow\mathcal{L}\{f(t)\}=-2\mathcal{L}\{1\}+3\mathcal{L}\{u(t-1)\}-6\mathcal{L}\{u(t-3)\}$  
> $=-2\left(\frac{1}{s}\right)+3\frac{e^{-s}}{s}-6\frac{e^{-3s}}{s}$  
> $\mathcal{L}\{u(t-a)f(t)\}=e^{-as}\mathcal{L}\{f(t+a)\}$  
> We know that $f(t)=1$ so $\mathcal{L}\{f(t)\}=\mathcal{L}\{1\}=\frac{1}{s}$ $(s>0)$  
> $\mathcal{L}\{u(t-a)\}=e^{-as}\mathcal{L}\{f(t+a)\}=e^{-as}\mathcal{L}\{1\}=\frac{e^{-as}}{s}$ $(s>0)$  
> Let $a=0:\mathcal{L}\{u(t)\}=\frac{1}{s}$  

Let $c\geq0$, another type unit step function is given by  
$$u_c(t)=u(t-c)=\begin{cases}0,t<c\\1,t\geq c\end{cases}$  
In this case, the jump can occur at an arbitrary time $c\geq0$  

Unit step functions can be used as an "on-off switch" to control the behavior of a given function $f(t)$ over certain time intervals. In general, if $f(t)$ is a piecewise function given by  
$$f(t)=\begin{cases}f_1(t),t<t_1\\f_2(t),t_1\leq t<t_2\\f_3(t),t_2\leq t<t_3\\\vdots\\f_n(t),t_{n-1}\leq t\end{cases}$$  
Then $f$ can be expressed in terms of unit step functions as  
$f(t)=(1-u_{t_1}(t))f_1(t)+(u_{t_1}(t)-u_{t_2}(t))f_2(t)+(u_{t_2}(t)-u_{t_3}(t))f_3(t)+\dots+(u_{t_{n-2}}(t)-u_{t_{n-1}}(t))f_{n-1}(t)+u_{t_{n-1}}f_n(t)$  

> [!note] Theorem  
> For $s>a>0$, the Laplace transform of the unit step function is given by  
> $$\mathcal{L}\{u(t)\}=\frac{1}{s};\mathcal{L}\{u_a(t)\}=\mathcal{L}\{u(t-a)\}=\frac{e^{-as}}{s};\mathcal{L}\{u(t-a)f(t)\}=e^{-as}\mathcal{L}\{f(t+a)\}.$$  

---  

**Example.** Find the Laplace transform for the following functions  

> [!note] $u(t-2)e^{7t}$  
> $=u_2(t)e^{7t}$ $(a=2)$  
> $\mathcal{L}\{u_2(t)e^{7t}\}=e^{-2s}\mathcal{L}\{e^{7(t+2)}\}=e^{-2s}\mathcal{L}\{e^{14}e^{7t}\}$  
> $=e^{-2s}e^{14}\mathcal{L}\{e^{7t}\}$  
> $=e^{-2s}e^{14}\frac{1}{s-7}$ for $s>7$  

> [!note] $u(t-\pi/2)$ and $u(t-\pi/2)\sin{(t-\pi/2)}$  
> $\mathcal{L}\{u_{\pi/2}(t)\sin{t}\}=e^{-\pi/2s}\mathcal{L}\{\sin{t+\pi/2}\}=e^{-\frac{-\pi s}{2}}\mathcal{L}\{\cos{t}\}=e^{-\frac{\pi s}{2}}\frac{s}{s^2+1}$ for $s>0$  
>  
> $\mathcal{L}\{u_{\pi/2}\sin{(t-\pi/2)}\}=e^{-\frac{\pi s}{2}}\mathcal{L}\{\sin{(t+\pi/2-\pi/2)}\}$  
> $=e^{-\frac{\pi s}{2}}\mathcal{L}\{\sin{t}\}=e^{-\frac{\pi s}{2}}\frac{1}{s^2+1}$ for $s>0$  

> [!note] $u(t-1)(t^2+3t+2)$  
> $u_1(t)(t^2+3t+2)$  
> $\mathcal{L}\{u_1(t)(t^2+3t+3)\}=e^{-s}\mathcal{L}\{(t+1)^23(t+1)+2\}$  
> $=e^{-s}\mathcal{L}\{t^2+2t+1+3t+3+2\}=e^{-s}\mathcal{L}\{t^2+5t+6\}$  
> $e^{-s}\left(\mathcal{L}\{t^2\}+5\mathcal{L}\{t\}+6\mathcal{L}\{1\}\right)$  
> $e^{-s}\left(\frac{2}{s^3}+\frac{5}{s^2}+\frac{6}{s}\right)$ for $s>0$  

---  

> [!note] Example. Find the inverse Laplace transform for $Y(s)=e^{-3s}\frac{s+1}{(s-3)(s-5)}$.  
> Suggest the final answer is $f(t)=u_3(t)g(t)$ where $\mathcal{L}\{g(t+3)\}=\frac{s+1}{(s-3)(s-5)}$  
> We find $\mathcal{L}^{-1}\{\frac{s+1}{(s-3)(s-5)}\}$ using partial fraction decomposition  
> Here, $\frac{s+1}{(s-3)(s-5)}=\dots=\frac{-2}{s-3}+\frac{3}{s-5}$  
> So $\mathcal{L}^{-1}\{\frac{s+1}{(s-3)(s-5)}\}=-2\mathcal{L}^{-1}\{\frac{1}{s-3}\}+3\mathcal{L}^{-1}\{\frac{1}{s-5}\}$  
> $=-2e^{3t}+3e^{5t}$  
> This is not $g(t)$. This is actually $g(t+3)$  
> We do one final shift $t\to t-3$ to find $g(t)$  
> $g(t)=-2e^{3(t-3)}+3e^{5(t-3)}=-2e^{-9}e^{3t}+3e^{-15}e^{5t}$  
> So $f(t)=u_3(t)\left(-2e^{-9}e^{3t}+3e^{-15}e^{5t}\right)$  

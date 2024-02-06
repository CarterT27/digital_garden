---  
tags:  
- Type/Note  
- Topic/Calculus  
- Class/MATH_20C  
date:  
- 2024-02-05  
---  
  
# Functions of multiple variables  
  
> [!question] A projectile is fired from the ground at an angle of 45 degrees.  
> What initial speed must the projectile have in order to hit the top of a 100m tower located 200m away?  
> Find $v_{0}=v(0)$ initial speed  
> $\vec{F}=m \langle 0,-g \rangle,g\approx 9.8m/s^2$  
> By Newton's law  
> $\vec{F}=m\vec{r}''(t)\implies \vec{r}''(t)=\langle 0,-g \rangle$  
> $\vec{r}'(t)=\int \vec{r}''(t) \, dt=\int \langle 0,-g \rangle \, dt=\langle 0,-gt \rangle+\vec{v}_{0}$  
> $\vec{r}(t)=\int \vec{r}'(t) \, dt=\int \langle 0,-g \rangle+\vec{v}_{0} \, dt=\langle 0,-\frac{g}{2}t^{2}\rangle+ \vec{v}_{0}t+\vec{c}_{0}$  
> $\vec{r}(t)=\langle 0,-\frac{g}{2}t^{2}\rangle +\vec{v}_{0}t$  
> We know that $\vec{v}_{0}=v_{0} \left\langle  \cos\left( \frac{\pi}{4} \right),\sin\left( \frac{\pi}{4} \right)  \right\rangle=v_{0}\langle \frac{\sqrt{ 2 }}{2},\frac{\sqrt{ 2 }}{2} \rangle$  
> For some $t$: $\vec{r}(t)=\langle 200,100 \rangle=\langle 0,-\frac{g}{2}t^{2}\langle +tv_{0} \left\langle  \frac{\sqrt{ 2 }}{2},\frac{\sqrt{ 2 }}{2}  \right\rangle=\langle tv_{0}\frac{\sqrt{ 2 }}{2},-\frac{g}{2}t^2+tv_{0}\frac{\sqrt{ 2 }}{2} \rangle$  
  
# 14.1 Function of multi-variables  
  
$z=f(x,y)$  
$f:D\to \mathbb{R},D\subset\mathbb{R}$  
  
> [!definition] The set of all inputs that we consider is called the domain of $f(x,y)$ or $f(x,y,z)$  
  
> [!definition] Level Curves and Contour Map  
> 1. Horizontal trace at height C = intersection of the graph with the horizontal plane $Z=C$ = $\{(x,y,c)|f(x,y)=c\}$  
> 2. Level curve: the curve $f(x,y)=c$ in the xy-plane = $\{(x,y)|f(x,y)=c\}$  

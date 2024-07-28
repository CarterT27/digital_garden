---
id: MATH 20C Lecture 14
aliases: []
tags:
- Type/Note
- Topic/Calculus
- Class/MATH_20C
date:
- "2024-02-09"
---
# 14.2 Limits and Continuity  

## How to find limits  

> [!note] Method 1  
> If $f(x,y)$ is continuous at $(a,b)$, then $$lim_{(x,y)->(a,b)}f(x,y)=f(a,b)$$  

> [!note] Method 2  
> $\lim_{(x,y)\to(0,0)}\frac{\sin(x^2+y^2)}{x^2+y^2}$  
> $\lim_{u\to0}\frac{\sin(u)}{u}$  
> Let $u=x^2+y^2=>$ As $(x,y)\to0,u\to0$  
> L'Hospital's Rule  
> If $\lim_{u\to a}\frac{f(u)}{g(u)}$ is of the form $\frac{0}{0}$ or $\frac{\infty}{\infty}$ then $\lim_{u\to a}\frac{f(u)}{g(u)}=\lim_{u\to a}\frac{f'(u)}{g'(u)}$  
> $\lim_{(x,y)\to(0,0)}\frac{\sin(x^2+y^2)}{x^2+y^2}=\lim_{u\to0}\frac{\sin(u)}{u}=1$  

> [!note] Method 3: Squeeze Theorem  
> $\lim_{(x,y)\to(0,0)}\sin\left(\frac{1}{x^2+y^2}\right)\tan(x^2y^4)$  
> Note $-1\leq\sin\left(\frac{1}{x^2+y^2}\right)\leq1$  
> $\implies-\tan(x^2y^4)\leq\sin\left(\frac{1}{x^2+y^2}\right)\tan(x^2y^4)\leq\tan(x^2y^4)$  
> Since $\lim_{(x,y)\to(0,0}\tan(x^2y^4)=\tan(0)=0=\lim_{(x,y)\to(0,0)}-\tan(x^2y^4)=-\tan(0)$  
> By the squeeze theorem  
> $\lim_{(x,y)\to(0,0)}\sin\left(\frac{1}{x^2+y^2}\right)tan(x^2y^4)=0$  

> [!note] Method 4: Showing that a limit does not exist (DNE)  
> $\lim_{(x,y)\to(0,0)}\frac{x^2}{x^2+2y^x}\text{ is DNE}$  
> Find the limit approaching $(0,0)$ along the x axis and along the y axis. Show that they are not equal.  
> $\lim_{x\to0}\frac{x^2}{x^2+0}=\lim_{x\to0}1=1$  
> $\lim_{y\to0}\frac{0}{0+2y^2}=0\neq1$  
> $\implies\lim_{(x,y)\to(0,0)}\frac{x^2}{x^2+2y^2}\text{ DNE}$  

> [!note] Method 5  
> Does the limit $\lim_{(x,y)\to(0,0)}\frac{x^4y}{x^8+y^2}$ exist?  
> $f(x,mx)$  
> $=\frac{x^4mx}{x^8+m^2x^2}=\frac{mx^3}{x^6+m^2}$  
> This shows that the limit along all lines are the same. But this does not prove that $\lim_{(x,y)\to(0,0)}f(x,y)$ exists.  
> $f(x,mx^4)$  
> $=\frac{x^4(mx^4)}{x^8+(mx^4)^2}=\frac{m}{1+m^2}$  
> $\lim_{x\to0}f(x,mx^4)=\frac{m}{1+m^2}$ depends on $m$.  
> $\implies\lim_{(x,y)\to(0,0)}f(x,y)$ DNE  

> [!note] Method 6: Polar coordinates  
> $x=r\cos\theta,y=r\sin\theta$  
> $(r,\theta)$ are the polar coordinates.  
> $(r\geq0,0\leq\theta<2\pi)$.  
> For any path to $(0,0)$, we can consider $\theta$ as a function of $r$ near $(0,0)$  

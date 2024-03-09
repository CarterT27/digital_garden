---
tags:
- "Type/Note"
- "Topic/Differential_Equations"
- "Class/MATH_20D"
date:
- 2024-03-04
---
If $F(s)=\mathcal{L}\{f(t)\}$ then  
- $\mathcal{L}\{tf(t)\}=-F'(s)$  
$\Rightarrow\mathcal{L}\{t^2e^{-t}\}=\frac{d^2}{ds^2}\mathcal{L}\{e^{-t}\}=\frac{d^2}{ds^2}\left(\frac{1}{s+1}\right)=\frac{2}{(s+1)^3}$  

# 7.4 & 7.5 - Inverse Laplace Transform and Solution to IVP  

> [!note] Solve the IVP: $y'=ay,y(0)=y_0$  
> 1. Apply Laplace Transform to both sides of the given ODE  
>   $\mathcal{L}\{LHS\}=\mathcal{L}\{y'\}=s\mathcal{L}\{y\}-y(0)=s\mathcal{L}\{y\}-y_0$  
>   $\mathcal{L}\{RHS\}=\mathcal{L}\{ay\}=a\mathcal{L}\{y\}$  
> 2. Set $\mathcal{L}\{LHS\}=\mathcal{L}\{RHS\}$ to derive an algebraic equation. Solve this algebraic equation for $\mathcal{L}\{\text{soln}\}$  
>   $\mathcal{L}\{LHS\}=\mathcal{L}\{RHS\}\Rightarrow s\mathcal{L}\{y\}-y_0=a\mathcal{L}\{y\}$  
>   $\Rightarrow\mathcal{L}\{y\}=\frac{y_0}{s-a}$  
> 3. Reverse/Inverse the transform to obtain our soln  
>   We have $\mathcal{L}\{e^{at}\}=\frac{1}{s-a}$ so $\mathcal{L}\{y_0e^{at}\}=\frac{y_0}{s-a}$  
>   So if $\mathcal{L}\{y\}=\frac{y_0}{s-a}=\mathcal{L}\{y_0e^{at}\}$  
>   Then our soln $y=y_0e^{at}$  

> [!note] Summary  
> 1. If you see $\mathcal{L}\{y\}=\frac{const}{(s-a)^{power}}$  
>   Look for $y=ct^{power-1}e^{at}$  
>   using $\mathcal{L}\{t^ne^{at}\}=\frac{n!}{(s-a)^{n+1}}$  
> 2. If you see $\mathcal{L}\{y\}=\frac{\dots}{(s-a)(s-b)(s-b)...}$  
>   Use **partial fraction decomp**  
>   $\mathcal{L}\{y\}=\frac{A}{s-a}+\frac{B}{s-b}+\frac{C}{s-c}$  
>   $=A\mathcal{L}\{e^{at}\}+B\mathcal{L}\{e^{Bt}\}+C\mathcal{L}\{e^{ct}\}+\dots$  

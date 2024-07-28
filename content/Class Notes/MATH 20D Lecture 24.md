---
tags:
- "Type/Note"
- "Topic/Differential_Equations"
- "Class/MATH_20D"
date:
- 2024-03-06
---
$s^2+1$ is called irreducible, i.e. we cannot write it as $(s-a)(s-b)$ for real numbers $a,b$  

> [!note] Example. Find the inverse Laplace transform of $Y(s)=\frac{2s^2-s+3}{(s^2+1)(s-2)}$  
> Partial fraction decomp $\frac{2s^2-s+3}{(s^2+1)(s-2)}=\frac{As+B}{s^2+1}+\frac{C}{s-2}$  
> $\Rightarrow\frac{2s^2-s+3}{(s^2+1)(s-2)}=\frac{(As+B)(s-2)+C(s^2+1)}{(s^2+1)(s-2)}$  
> $\Rightarrow2s^2-s+3=(As+B)(s-2)+C(s^2+1)$  
> When $s=2$: $9=C(2^2+1)\Rightarrow C=\frac{9}{5}$  
> When $s=0$: $3=B(-2)+\frac{9}{5}\Rightarrow B=-\frac{3}{5}$  
> When $s=1$: $4=(A-\frac{3}{5})(-1)+\frac{9}{5}(1^2+1)\Rightarrow A=\frac{1}{5}$  
> Partial Fraction Decomposition $\frac{2s^2-s+3}{(s^2+1)(s-2)}$  
> So $Y(s)=\frac{\frac{1}{5}s-\frac{3}{5}}{s^2+1}+\frac{\frac{9}{5}}{s-2}$ where $\frac{9}{5}\frac{1}{s-2}=\frac{9}{5}\mathcal{L}\{e^{2t}\}$  
> and $\frac{\frac{1}{5}s-\frac{3}{5}}{s^2+1}=\frac{1}{5}\frac{s}{s^2+1}-\frac{3}{5}\frac{1}{s^2+1}=\frac{1}{5}\mathcal{L}\{\cos{t}\}-\frac{3}{5}\mathcal{L}\{\sin{t}\}$  
> Thus, $Y(s)=\mathcal{L}\{\frac{1}{5}\cos{t}-\frac{3}{5}\sin{t}+\frac{9}{5}e^{2t}\}$  
> $\Rightarrow\mathcal{L}^{-1}\{Y(s)\}=\frac{1}{5}\cos{t}-\frac{3}{5}\sin{t}+\frac{9}{5}e^{2t}$  

> [!note] Find $\mathcal{L}\{\frac{2s-3}{s^2+2s+10}\}$  
> Complete the square from denom $s^2+2s+10=(s+1)^2+3^2$ - from this, $a=-1,w=3$  
> The denominator suggests that the inverse Laplace transform will be a combination of $e^{-t}\cos{3t}$ and $e^{-t}\sin{3t}$ whose Laplace transforms are $\frac{s+1}{(s+1)^2+9}$ and $\frac{3}{(s+1)^2+9}$  
> We let $\frac{2s-3}{(s+1)^2+9}=A\left[\frac{s+1}{(s+1)^2+9}\right]+B\left[\frac{3}{(s+1)^2+9}\right]$  
> $\Rightarrow2s-3=A(s+1)+3B$  
> $\Rightarrow2s-3=As+(A+3B)$  
> So $\begin{cases}A=2\\A+3B=-3\end{cases}\Rightarrow\begin{cases}A=2\\B=-\frac{5}{3}\end{cases}$  
> Thus, $F(s)=2\left[\frac{s+1}{(s+1)^2+9}\right]-\frac{5}{3}\left[\frac{3}{(s+1)^2+9}\right]$  
> $=2\mathcal{L}\{e^{-t}\cos{3t}\}-\frac{5}{3}\mathcal{L}\{e^{-t}\sin{3t}\}$  
> $=\mathcal{L}\{2e^{-t}\cos{3t}-\frac{5}{3}e^{-t}\sin{3t}\}$  
> $\mathcal{L}^{-1}\{F(s)\}=2e^{-t}\cos{3t}-\frac{5}{3}e^{-t}\sin{3t}$  

> [!note] Find the inverse Laplace transform of $Y(s)=\frac{12}{(s^2+2s+5)^2}$  
> Look at the denom $(s^2+2s+5)^2=\left[(s+1)^2+2^2\right]^2$, which suggests $a=-1,w=2$  
> So the answer will involve $e^{-t}\cos{2t}$ and $e^{-t}\sin{2t}$  
> $m=2$ suggests that the answer also involves $te^{-t}\cos{2t}$ and $te^{-t}\sin{2t}$  
> In fact, $\mathcal{L}\{te^{-t}\cos{2t}\}=-\frac{d}{ds}\mathcal{L}\{e^{-t}\cos{2t}\}$  
> $=-\frac{d}{ds}\left(\frac{s+1}{(s+1)^2+2^2}\right)=\frac{(s+1)^2-2^2}{\left[(s+1)^2+2^2\right]^2}$  
> and $\mathcal{L}\{te^{-t}\sin{2t}\}=-\frac{d}{ds}\mathcal{L}\{e^{-t}\sin{2t}\}=\frac{4(s+1)}{\left[(s+1)^2+2^2\right]^2}$  
> Next we write $\frac{12}{(s^2+2s+5)^2}$ as a linear combo of $\mathcal{L}\{e^{-t}\cos{2t}\},\mathcal{L}\{e^{-t}\sin{2t}\},\mathcal{L}\{te^{-t}\cos{2t}\},\mathcal{L}\{te^{-t}\sin{2t}\}$ and solve for the coefficients  
> $\frac{12}{\left[(s+1)^2+4\right]^2}=A_1\left[\frac{(s+1)^2-4}{\left[(s+1)^2+4\right]^2}\right]+A_2\left[\frac{4(s+1)}{\left[(s+1)^2+4\right]^2}\right]+A_3\left[\frac{s+1}{(s+1)^2+4}\right]+A_4\left[\frac{2}{(s+1)^2+4}\right]$  
> $12=A_1((s+1)^2-4)+4A_2(s+1)+A_3(s+1)((s+1)^2+4)+2A_4((s+1)^2+4)$  
> $\Rightarrow12=A_3(s+1)^3+(A_1+2A_4)(s+1)^2+(4A_2+4A_3)(s+1)+(8A_4-4A_1)$  
> $\begin{cases}A_3=0\\A_1+2A_4=0\\4A_2+4A_3=0\\8A_4-4A_1=12\end{cases}\Rightarrow\begin{cases}A_1=-\frac{3}{2},A_4=\frac{3}{4}\\A_2=A_3=0\end{cases}$  
> $\Rightarrow F(s)=-\frac{3}{2}\mathcal{L}\{te^{-t}\cos{2t}\}+\frac{3}{4}\mathcal{L}\{e^{-t}\sin{2t}\}$  
> $\Rightarrow\mathcal{L}^{-1}\{F(s)\}=-\frac{3}{2}te^{-t}\cos{2t}+\frac{3}{4}e^{-t}\sin{2t}$  

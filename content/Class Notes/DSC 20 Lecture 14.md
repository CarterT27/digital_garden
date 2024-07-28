---
tags:
- Type/Note
- Topic/Data_Science
- Class/DSC_20
date:
- 2024-02-09
---
# Logs  

> [!note] Proof $\log_{a}b^c=c\cdot \log_{a}b$  
> $\log_{a}b=n$  
> $a^{nc}=b^c$  
> $\log_{a}a^{nc}=\log_{a}b^c$  
> $nc=\log_{a}b^c$  
> $c\cdot \log_{a}b^c=\log_{a}b^c$  

> [!note] Proof $\log_{a}b=\frac{\log_{c}b}{\log_{c}a}$  
> $\log_{a}b=n$  
> $a^n=b$  
> $\log_{c}a^n=\log_{c}b$  

> [!note] Example $\log_{3}81=\frac{\log_{9}81}{\log_{9}3}=\frac{2}{1/2}=4$  

> [!note] Why we don't care about the base of logs in Big O notation  
> $\log_{10}n=\frac{\log_{2}n}{\log_{2}10}=\frac{1}{\log_{2}10}\log_{2}n=c\cdot \log_{2}n=\log_{2}n$  
> We can drop any constant terms because in Big O notation, we don't care about them.  

> [!note] Properties of Orders of Growth  
> - **Constants**: Constant terms do not affect the order of growth of a process$$\Theta(n),\Theta(500\cdot n),\Theta\left( \frac{1}{500}\cdot n \right)$$  
> - **Logarithms**: The base of a logarithm does not affect the order growth of a process$$\Theta(\log_{2}n),\Theta (\log_{10}n),\Theta(\ln n)$$  
> - **Lower-order terms**: The fastest-growing part of the computation dominates the total$$\Theta(n^2),\Theta(n^2+n),\Theta(n^2+500\cdot n+\log_{2}n+1000)$$  

> [!note] Comparing Orders of Growth (n is the problem size)  
> $\Theta(1)$ Constant. The problem size doesn't matter  
> $\Theta(\log n)$ Logarithmic growth.  
> $\Theta(n\cdot \log n)$  
> $\Theta(\sqrt{ n })$ Square root growth.  
> $\Theta(n)$ Linear growth.  
> $\Theta(n^2)$ Quadratic growth.  
> $\Theta(b^n)$ Exponential growth. Recursive `fib` takes $\Theta(\phi^n)$ steps, where $\phi=\frac{1+\sqrt{ 5 }}{2}\approx 1.61828$  

> [!note] Abused Notation  
> VERY often Big-O is used in Big-Theta (in Computer Science)  
> Not as an upper bound!  

> [!note] Useful Formula, in the context of Big O  
> $\sum_{i=1}^ni=\frac{n(n+1)}{2}=\frac{1}{2}(n^2+n+1)=n^2$  

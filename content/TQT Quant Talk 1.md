---
tags:
- "Type/Note"
- "Topic/Quantitative_Finance"
- "Club/Triton_Quantitative_Trading"
date:
- 2024-03-05
---
# Probability & Statistics in Quant Finance - [Siddharth Vishwanath](https://sidvishwanath.com/)  

> [!note] Topological Data Analysis  
> Persistence diagrams to compare objects topologically  
> Comparing the distribution of points  

> [!note] Statistics & finance  
> Martin Baxter  

> [!note] A Tale of Two Probabilities  
> $\mathbb{P}\text{ vs. }\tilde{\mathbb{P}}$  
>  
> The forward probability $\mathbb{P}$  
> - Goal: Model the future  
> - Uses: Risk management, investing  
> - Reference: the "real world" probability  
> - Machinery: High-dimensional statistics, machine learning, etc.  
>  
> The risk neutral probability $\tilde{\mathbb{P}}$  
> - Goal: Extrapolate the present  
> - Uses: Pricing, hedging  
> - Reference: the "risk neutral" probability  
> - Machinery: Ito calculus, Partial Differential Equations  

> [!note] What is the risk-neutral probability?  
> Consider the following setup:  
> - For time intervals $0=t_0<t+1<t_2<\dots<t_n$  
> - At each time $t_n$ you have access to:  
>   - A stock with price $S_n$  
>   - A bond (risk-free asset) with price $B_n$  
> - From time $t_n$ to $t_{n+1}$ the obnd always gives you risk-free return $$B_{n+1}$  

> [!definition] Portfolio  
> A portfolio is a collection of assets you own at any given time.  
> $$V_n=\alpha_nS_n+\beta_nB_n\text{s.t. }\alpha_n+\beta_n=1$$  

> [!note]  
> - At each time $t_n$, choose a value $\alpha_{n+1},\beta_{n+1}$ such that  
> - Your net value $V_{n+1}=\alpha_{n+1}S_{n+1}+\beta_{n+1}B_{n+1}$ is maximized  

> [!definition] European Call Option  
> A European Call option $X$ is a derivative where the payoff at time $t_n$ is $$X_n=max(S_n-K,0)$$  
> where $K$ is called the strike price  
> Can only be exercised at time of expiration, unlike American Call Options  
> At time $t_{n+1}$ suppose one of two thing can happen:  
> $$S_{n+1}=(1+u)\times S_n\text{ with probability }p$$  
> $$S_{n+1}=(1-d)\times S_n\text{ with probability }1-p$$  
> here, $p$ is the "real-world" probability  
> $$X_{n+1}^u=\left(\alpha_{n+1}\times(1+u)S_n\right)+\left(\beta_{n+1}\times(1+r)B_n\right)$$  
> $$X_{n+1}^d=\left(\alpha_{n+1}\times(1-d)S_n\right)+\left(\beta_{n+1}\times(1+r)B_n\right)$$  
> Solving for $\alpha_{n+1}$ and $\beta_{n+1}$  
> $$\alpha_{n+1}=\frac{X^u_{n+1}-X^d_{n+1}}{(u+d)S_n}$$  
> $$\beta_{n+1}=\frac{1}{1+r}\left(\frac{(1+u)X^d_{n+1}-...}{...}\right)$$  
> $V_n=\alpha_{n+1}S_n+\beta_{n+1}B_n$  
> $=\tilde{p}X^u_{n+1}+(1-\tilde{p})X^d_{n+1}=\mathbb{E}_\tilde{p}(X_{n+1})$  
> Here $\tilde{p}=\frac{r+d}{u+d}$ is the risk-neutral probability  
> When the stock price $S_t$ doesn't just go up/down but can take a range of values  
> $$S_{n+1}\vert S_n\sim N(S_n,\sigma^2)\equiv P$  
> Then $\tilde{P}\sim N(0,1)$  
> - Stochastic differential equations  
> - Brownian Motion  
> - Girsanov's theorem  

> [!note] Examples of cutting-edge DL models  
> - Transformers  

> [!Note] Derivative Pricing  
> Use real world probability to model the stock price  
> Use the risk neutral probability to price the derivative  
> The price of the derivative is the expected value of the derivative at time T under the risk-neutral probability $\tilde{P}$  

> [!note] Estimating $\mathbb{P}$  
> $r_1$ is a stochastic interest rate  
> Used to evaluate bond prices, create interest rate swaps, and underlies almost every other financial derivative  
> A common model for $r_t$ is to assume it follows a Vasicek model, i.e.  
> $$dr_1=(\alpha-\beta r_t)dt+\sigma dW_t$$  
> where $W_t$ is a Brownian motion  
> $$r_{t+\Delta t}\sim N(r_t+(\alpha-\beta r_t)\cdot\Delta t,\sigma^2\cdot\Delta t)$$  
> Let $f_t(r_t\vert \alpha,\beta,\sigma)$ be the probability density function of $r_t$ at time $t$. Then the likelihood of the data is  
> $$L(\alpha,\beta,\sigma)=\prod_{i=1}^n f_{t_1}(r_{t_1}\vert\alpha,\beta,\sigma)$$  

> [!note] The statistical advantage  
> If you can do the math, you can  
> - Estimate $\hat{\theta}$ using a dinosaur computer  
> - Use $\hat{\theta}$ to make predictions about the future  
> - Quantify how much uncertainty you have in your predictions  
> - Quantify the effect that changing $\hat{\theta}$ to $\hat{\theta}$ + $\Delta\theta$ has on your predictions  

> [!note] 21st Century Forecasting  
> If you have enough compute you can  
> - estimate theta hat using state of the art GPUs  
> - Use $\hat{\theta}$ to make predictions about the future  
> - But it comes at the price of uncertainty quantification  
> - But you don't have to worry about the math  

> [!note] Physics informed deep learning  

> [!note] Which is better?  
> It depends  
>  
> Philosophically  
> - The first method is based on assumptions  
>   - Assumptions have consequences  
> - The second method is based on data  
>   - Garbage in, garbage out!  
>   - Signal to noise ratio - more noise than signal  
>  
> Realistically  
> - First approach for mathematicians, second approach for computer scientists  

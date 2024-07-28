---
tags:
- "Type/Note"
- "Topic/Quantitative_Trading"
- "Class/CSE_198"
date:
- 2024-04-17
---
Source: https://docs.google.com/presentation/d/1N0hcegbG6UyH9BJeJrK2xblXKo3kdREF-iIsQ3XPWYk/edit#slide=id.g2c88701fe5c_0_0  

### How Do Options Values Change?  

- Greek variables that are used to assess risk in the options market.  
- Each Greek variable is a result of an imperfect assumption or relationship of the option with another underlying variable.  
- Traders use different Greek values to assess options risk and manage option portfolios.  
- https://www.investopedia.com/terms/g/greeks.asp  

### Theta  

![](https://lh7-us.googleusercontent.com/99ZyLhbFh6gxI06eNfzhTpAUZ9YTE_c70VyssnQWUAGPA_latgsP9FyKXlTPAQzWGKthU1_HlpzILsPNYgVBDP0NzfFuoRoIk1ixRw3hebQCr2O743Q-bSVm5kty2yWOj-BZpPcJwkaypeUhPfT6NwsAlw=s2048)  
- Measures value decrease of options due to passage of time.  
- Represented as 1 day worth of time decay.  
- If you have Option worth $5 on Day 0 with theta 0.5 then on Day 1 it costs $4.5, if all other factors remain the same.  
- More the magnitude of theta, more the option is sensitive to time.  
- Theta increase in magnitude as Options approach expiration  
- So Does theta increase in magnitude continuously ?  
- https://www.investopedia.com/ask/answers/06/forwardsandfutures.asp  
- Theta (magnitude) increases when options are at-the-money, and decreases when options are in- and out-of-the money.  

Theta as function of price  
![](https://lh7-us.googleusercontent.com/w7x0LdjIvdeLTKt9W2JbnOHNCUFgi92mCr5Vuamm3Cy2pTDNGWuknXzTTbmqcemdQ5Pe4nhw69pNdnZQEhO_ULYK4l3znB3axoU51y-gV56guWIDqpo-oVAJon4CRw8h9G0M7XTNZfodPNSTjZC5r2gCFw=s2048)  

Option value as function of time  
![](https://lh7-us.googleusercontent.com/2SZK08DPGq0-qHIqqIhQDKarZNXzZieHbNfM6-wKdk6hy0Vr9uiWba7iuhe-7YF6ljEQ0O13h6i5mMQd2YpudOu8QzX2NMmkTaNmPmRJ0IJ_yhZ_5b5PJ0yhw3MFs-CAftylmQZCTnBcgVmfkI5FCUjLow=s2048)  

### Delta  

- Measures change in price of Option due to change in price of stock.  
- 0.5 delta means - For a $1 increase in stock price, Options value increase by $0.5  
- For Call Option: $0\leq \Delta \leq 1$  
- For Put Option: $-1\leq \Delta \leq 0$  
- A 0.25 delta means that Call option has 25% chance of expiring ITM (with profit)  

![](https://lh7-us.googleusercontent.com/V2TwRtIwnZM4srZZV9s1ieXwy5qDJGCrKA7YzIQ--7uHzaXxT4bW4fHCIJ6-Q92t3veFrEcQT7zcR5SRbfzjH-jEVYJeIng_mrjCEcNu5UxV3B-TjroVWicER4olFifVBg-XW2M6UU6m6ou32Bi-1c0KXg=s2048)  

### Use of Delta - Hedging  

- Let’s say we sold 10 call options that have a 20 delta, we have a delta position of -200. To be **delta neutral**, we need to buy 2 underlying Futures contract.  
- Future Contracts have delta + 1 or -1  
- How would you actually face it in real world assessments ?  
- An option's premium is 1.50 and has a 40 delta with the Underlying future at 100. If the underlying future moved from 100 to 102, what would the option's new premium be based on delta?  
- Treat underlying future = stock price  
- Delta is more important than it seems !  
- We should monitor change in delta too !  

### Gamma  

![](https://lh7-us.googleusercontent.com/HthwgEwwkiqY8EFa90rMOfmaZc5zyxfdkKRBcb8dvDjAqchTRXKwopFZSF2ungmq62ZUuvRsm_zq6g4k1lY1HjJj3fgR7yY5JlhK3j0vdrpD5vMyii90JpS3L7aF3KFl3hSi8QXe_8c4Onv34bvN7iveqw=s2048)  
- Gamma ($\Gamma$) represents the rate of change between an option's delta and the underlying asset's price.  
- Gamma indicates the amount the delta would change given a $1 move in the underlying security.  
- Option Traders like to be both Delta & Gamma neutral in order to decrease risk  
- https://www.investopedia.com/terms/g/greeks.asp  

### Implied Volatility - Sigma($\sigma$) - Not a Greek Var  

- Implied volatility is the market's forecast of a likely movement in a security's price.  
- When applied to the stock market, implied volatility generally increases in bearish markets, when investors believe equity prices will decline over time.  
- $\sigma$ decreases when the market is bullish. This is when investors believe prices will rise over time. Bearish markets are considered to be undesirable and riskier to the majority of equity investors.  
- Options with high implied volatility have higher premiums and vice versa.  

### Vega  

![](https://lh7-us.googleusercontent.com/gYeJmfIPHZZv44remGCNRPW2ir-3yaPNSlvGFmOHKWuMiwC5B1hYcJFo5peQU3Mo-mny23nY5lvFSv6W8W1UqQ7fvEoMjHre1q1o4KjgxlEEhEm893nFph-AjybhvT9pNC6JsmLMOhDH_QD071E4n7S2Aw=s2048)  
- Vega (ν) represents the rate of change between an option's value and the underlying asset's implied volatility. This is the option's sensitivity to volatility.  
- For example, an option with a vega of 0.10 indicates the option's value is expected to change by 10 cents if the implied volatility changes by 1%  
- Vega Effect  
- Consider Option Price = $7.5, Implied Volatility = 25%  
- Option’s Vega = 0.12  
- If Volatility changes to 30% then Option price becomes  
- 7.5 + (30 - 25)*0.12 = $8.1  

### Rho ($\rho$)  

![](https://lh7-us.googleusercontent.com/jJrF_HT8T6DTv-iuGZZL-8n9yM9n6AV18lzoR4dum-PQaL03QuujRYug3geEYheQ7OK1dv6iBOjmfiYrBAAHqBuDPpT_JoGNk1Eq4yLFJutxBCb0028aXewVG2woF_hfl-jq_e3T-e8-tpeB4ZQGE5uS_w=s2048)  
- It represents the rate of change between an option's value and a 1% change in the interest rate.  
- This measures sensitivity to the interest rate.  
- For example, assume a call option has a rho of 0.05 and a price of $1.25.  
- If interest rates rise by 1%, the value of the call option would increase to $1.30, all else being equal.  

### Black Scholes Model  

![](https://lh7-us.googleusercontent.com/kfXqgyevk8LIpjgjadsmgUrbWBNgAdb6wOf7GkylcP_EcUbh8hOm0hZ1sTcswVJ_fvHS6qQUMOd1ivtH6egi7EYGBee4pjZnyePYoEFo3ZKs_OHHD4REN8B4Ev0gTi4QnrMu-ZAk36xGlWD46XfqM9oMMA=s2048)  
- Idea - Continuously revised delta hedging  
- Assumptions  
1. The stock pays no dividends during the option’s life  
2. European exercise style  
3. Markets are efficient  
4. No transaction costs  
5. Interest rates remain constant  
6. Prices are lognormally distributed  
- C = Call Option Price  
- S = Current Stock Price  
- K = Strike Price  
- R = risk free interest rate  
- T = time to maturity  
- N = Normal Distribution  
- The valuation equation has two parts  
- One gives a "pseudo-probability" weighted expected stock price (an inflow)  
- One gives the time-value of money adjusted expected payment at exercise (an outflow)  
$$C=SN(d_{1})-KE^{-RT}N(d_{2})$$  
- $d_{1}=\frac{\ln{\frac{S}{K}} + \left( r+\frac{\sigma^2}{2} \right)(T-t)}{\sigma \sqrt{ T-t }}$  
- $d_{2}=d_{1}-\sigma \sqrt{ T-t }$  
![](https://lh7-us.googleusercontent.com/HSOwW547RpYwbPIY_XztY6kqVapxgya3ZVh9yR89Qh7_dwFhJLBB2lircphe-DtCFuYCRHc2qEtCr1RAakrUsyhTZ7NCBukzHWGVBO4bKcyvMgGIOiyyKohifx_9ttkOc70C3z74aC_Ht1c8UuiDJ8zNCg=s2048)  

- Valuing a Microsoft Call Example  
- We would like to value a MSFT OCT 70 call in the year 2000. Microsoft closed at $70.75 on August 23 (58 days before option expiration). Microsoft pays no dividends.  
- We need the interest rate and the stock volatility to value the call.  
- Consulting the “Money Rate” section of the Wall Street Journal, we find a T-bill rate with about 58 days to maturity to be 6.10%.  
- To determine the volatility of returns, we need to take the logarithm of returns and determine their volatility. Assume we find the annual standard deviation of MSFT returns to be 0.5671.  

![](https://lh7-us.googleusercontent.com/SJoA2FZmUjEvYVkC-RuIOf2jegxBg_DcT3k_tmTxz9tBwob9ztgmkQPSHpK5PMBm7plZHaH2VPuPyu7SqTycPM6ps8Fw2z58RMyTJHLJulAIkZ5rahlWoapmTfd1ViDkJYIgqjWVfp3WBY_UDALE0CE2cw=s2048)  
![](https://lh7-us.googleusercontent.com/3XhPD8Os24PeB_2G0-01bCppf90fRv8or1A8jZoa8und8mrgpcXK-CMoiJu7wD3eQke8XjsAzSN9RhLYScNlFQcAZnQN06bv1k6-a7TXcSuQvKcYO_Zlbh-yWCCf3te3_Uyo3nHluV7qIgOjUOt4jQiH0w=s2048)  
![](https://lh7-us.googleusercontent.com/JpmhHDcZ78kws6qA26Qn52k61x_8QUKwE3owLikJOAnIc8_a8KSv4qZT-Ik9rHAIkesaoBu7uf_7Ltxp6SQPCTgLtSBYq1_S7sKYX3L-0o-dyubTEmS7UgPlej4HYPYhEWSfOmOmKeBmAh1QCLbwF2ByYQ=s2048)  
![](https://lh7-us.googleusercontent.com/CPx1xL6CTrmF-uYiUd4dcrTUDpAv3scpHtz754fAmd_NRIvxzgzZOFIZsQpk3nMuJcC8rsJYWxb_CO43w6ypbpdz6K3mf0W35_zjvnJ44-J13zdAgARcnY3azrozRloSzdp8QJFumSx4RDYMV4iSwyXucw=s2048)  

- The call actually sold for $4.88.  
- The only thing that could be wrong in our calculation is the volatility estimate. This is because we need the volatility estimate over the option’s life, which we cannot observe.  
- Instead of solving for the call premium, assume the market-determined call premium is correct  
- Then solve for the volatility that makes the equation hold  
- This value is called the implied volatility  

![](https://lh7-us.googleusercontent.com/YDOJsvKgESvUy196BcJr55_bA9ikVjb_65ag5mzBMMr0cJSOZtW13O556sfChrzSeraLx64kcwKA08l6479nFGLxD6XJRk8ld-364anini_4QjbcSvlabRnppYnCbBVQBpFIs4x52MhDWfAvlizFW8JFVQ=s2048)  

- The implied volatility for the MSFT OCT 70 call is 35.75%, which is much lower than the 57% value calculated from the monthly returns over the last two years.  

### Conclusion & Improvements  

- The Black Scholes model is a continuous time model of stock prices built on a Brownian motion z which includes a constant parameter volatility σ describing the risk of the stock. The Black Scholes model uses a partial differential equation from which a formula of the option price can be derived.  
- The Volatility is actually NOT A CONSTANT  
- Improvement upon Black Scholes is a **Heston model** which allows Stochastic Volatility (variable)  

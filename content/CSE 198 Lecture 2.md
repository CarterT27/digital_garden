---
tags:
- "Type/Note"
- "Topic/Quantitative_Trading"
- "Class/CSE_198"
date:
- 2024-04-10
---
### Recap - [[CSE 198 Lecture 1]]  

---  

# Options  

## Do you always have to OWN stocks?  

Short selling is essentially a buy or sell transaction in reverse.  
Buying stock later and returning borrowed stock to lender is called **covering**.  

### Can I invest with less money?  

## Derivatives  

A derivative or contingent claim is a security whose value depends on the value of some underlying security. Examples of derivatives are forward contracts, futures contracts, options, swaps, etc.  

### Forward and Future Contracts  

Forward and futures contracts involve two parties agreeing to buy and sell an asset at a specified price by a specific date.  

A forward contract is a private, customizable agreement that settles at the end of the agreement and is traded over the  
TODO  

## Options - Futures with more flexibility  

Leverage - Options provide greater leverage than stocks, allowing control over more shares with less money. This can amplify returns but also increases risk.  
TODO  

## Options  

An option is a contract which gives the holder of the option the right, but not the obligation, to buy or sell a given security at a given price (called the exercise price or strike price) within a fixed time period [0,T].  

A European option can only be exercised by the holder of the option at the expiration time T, whereas an American option can be exercised by the holder at any time in [0,T].  

Strike Price: The price at which the option holder can buy (for a call option) or sell (for a put option) the underlying asset.  
Expiration Date: The date when the option contract expires.  
Premium: The price paid by the option buyer to the option seller for the rights conveyed by the option.  

**Put option** on a stock is the option without obligation to sell 1 share of at a future time for price of \$K.  
The payoff on a put option is  
$$(K-S_t)^+=\begin{cases}k-S_t, k>S_t\\0, k\leq S_t\end{cases}$$  

A **call option** gives the option holder the right to buy at the given price \$K.  
The payoff on a call option is  
$$(S_t-k)^+=\begin{cases}0, S_t\leq k\\S_t-k, S_t>k\end{cases}$$  

## Long vs. Short  

Long = BUY  
Short = SELL  

For call options, the lower the strike price relative to the current market price of the stock, the more valuable the option is because it allows the holder to purchase the stock at a lower price.  
TODO  

## Binomial Models  

- The binomial option pricing model is a mathematical model used for pricing options. It's based on the assumption that the price of the underlying asset can either go up by a certain factor or down by a certain factor over a given period.  
- It involves constructing a binomial tree to represent possible paths of the underlying asset's price over time.  
- At each node of the tree, the option value is calculated based on the expected payoff from exercising the option at that node.  
- By recursively calculating the option values backward through the tree, you can determine the fair value of the option at the current time.  

### Replicating Portfolios  

A replicating portfolio is a portfolio of assets that has the same cash flows as a given financial instrument. In the context of options, a replicating portfolio can be created using the underlying asset and a risk-free asset to mimic the payoffs of the option. The portfoio is (a,b) where a is investment in stocks and b in bonds.  

### Linking it to a Binomial Model  

Create a replicating portfoilio for each node of the binomial tree.  
Use a combination of the underlying asset and a risk-free asset to mimic option payoffs.  
By replicating option payoffs, estimate the fair value of the option at each node.  
Assesses the combined value of the replicating portfolio to determine option value accurately.  
Utilize replicating portfolio concept to integrate option pricing into the binomial model.  

### Example of a Replicating Portfolio  

- Imagine you have an option to buy a stock at a certain price (let's call it C0) in the future.  
- You can create a replicating portfolio using a mix of stocks and bonds to mimic the payoff of this option.  
- If the initial price of the option (C0) is higher than its fair value / theoretical value (V0), there's an opportunity for risk-free profit.  
- You could sell the overpriced option, use some of the money to invest in the replicating portfolio, and buy additional bonds with the rest.  
- By doing this, you create a trading strategy where you're guaranteed to make a profit.  

> [!note] Why bonds?  
> Bonds give interest hence we want to see if investing in stocks is actually beneficial  


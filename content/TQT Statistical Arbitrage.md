---  
tags:  
- "Type/Note"  
- "Topic/Quantitative_Finance"  
- "Club/Triton_Quantitative_Trading"  
date:  
- 2024-01-12  
---  
  
# Cointegration, Pairs Trading  
  
> [!definition] [Cointegration](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.coint.html)  
> **Cointegration** suggests a long-term equilibrium relationship between the prices of stock pairs.  
> Studying how to make profit from two correlated stocks  
> Example: Coca Cola and PepsiCo  
> ```Python  
> from statsmodels.tsa.stattools import coint # use this library to find this out the p_value  
> ```  
  
> [!definition] Arbitrage  
> Cross-trading between two stocks, no additional investment  
> Little to no risk, positive profit, quickly disappears  
  
> [!note] Signals based on z score from rolling mean and std  
> Assumption that the stocks will follow movement with each other  
  
> [!note] Increasing trade frequency (decreasing time range) when z-score is extremely high  
  
Sources:  
- https://colab.research.google.com/drive/1Cp08Q2Y30Ed0m6aXFYqlGU4Esc1mHvmP?authuser=1#scrollTo=CUSLoCs6i3kU  
- https://medium.com/auquan/pairs-trading-data-science-7dbedafcfe5a  

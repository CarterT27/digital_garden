---
tags:
- Type/Note
- Topic/Quantitative_Trading
- Class/CSE_198
date:
- 2024-04-24
---
## Moving and Exponential Averages  

https://colab.research.google.com/drive/15-Vt437lm-3tx-cwEQTjJHAJ2oywjlhI?usp=sharing  

## More Alpha Ideas - Quant Research  

- https://arxiv.org/pdf/1601.00991.pdf  
- [https://platform.worldquantbrain.com/learn/documentation/discover-brain/read-first-starter-pack](https://platform.worldquantbrain.com/learn/documentation/discover-brain/read-first-starter-pack)  
- [https://platform.worldquantbrain.com/learn/documentation/interpret-results/parameters-simulation-results](https://platform.worldquantbrain.com/learn/documentation/interpret-results/parameters-simulation-results)  
- Sharpe Ratio - Compares the return of an investment with its risk  
[https://www.investopedia.com/terms/s/sharperatio.asp](https://www.investopedia.com/terms/s/sharperatio.asp)  
- Drawdown (in %) - how much an investment or trading account is down from the peak before it recovers back to the peak.  
- Turnover = percent of portfolio traded per day  
- Fitness = Overall performance, Margin = The profit per dollar traded  

## Trading Strategy 1 - Reversion  

- Reversion theory - Prices that have moved substantially away from their historical average are expected to revert back.  
- HYPOTHESIS: If the stock price of a company has increased over the last 2 days, it may decrease in the future (time series delta of closing price today and closing price 2 days ago).  
- IMPLEMENTATION: If company A's stock price had increased twice as much as the stock price of another company B, the prices of both stocks may decrease in the future.  In this reversion example, stock A may not fall double stock B, though it may fall more than stock B (rank operator).  
- By neutralizing against a broad market index, you can attempt to isolate movements that are specific to the stock itself, rather than movements that are reflective of the broader market.  
`rank(-ts_delta(close,2));`  

## Trading Strategy 2 - Liabilities  

- HYPOTHESIS: "Fair value accounting" aims to measure and report on-going valuations of assets and liabilities. A recent increase in the fair value of liabilities may indicate a higher cost to be borne by the company in the future. This may deteriorate the company's financial health, potentially leading to lower profitability or financial distress.  
- IMPLEMENTATION: Using ts_rank() operator, sell stocks when there is an increase in the fair value of liabilities within a year  
- HINT TO IMPROVE THE ALPHA: Could observing the increase over a shorter period improve accuracy?  
`-ts_rank(fn_liab_fair_val_l1_a,252)`  

## Trading Strategy 3 - Operating Income  

- HYPOTHESIS: If the operating income of a company is currently higher than its past 1 year history, buy the company’s stock and vice-versa.  
- IMPLEMENTATION: Using ts_rank to identify current performance of the company compared to its own history  
- HINT TO IMPROVE THE ALPHA: Rather than comparing the value directly, can calculating a ratio that includes stock market moves, improve the signal?  
`ts_rank(operating_income,170)`  

## How do I merge my ideas?  

- Create rank for individual idea and then take weighted average of ranks to get a composite score  
```  
delta_rank = rank(-ts_delta(close,2));  
income_rank = ts_rank(operating_income, 170);  
(delta_rank + income_rank)/2  
```  

## TS4 - How to incorporate hints  

- HYPOTHESIS: Companies that generate high income from operations compared to their debt, may do well in the future  
- IMPLEMENTATION: Rank the ratio of Funds from Operations (FFO) to long-term debt  
- HINT TO IMPROVE THE ALPHA: Can performing a time series comparison of the ratio of FFO to long-term debt, highlight increasing financial health overtime and produce better signal?  
`rank(fnd6_fopo/debt_lt)`  

- Modified code - Using ChatGPT can help with idea but you have to  
find correct fast expression operator and data available  

### Calculate the ratio of FFO to long-term debt for each period  
`ratio = fnd6_fopo / debt_lt;`  

### Calculate the average ratio over the specified window  
`average_ratio = ts_mean(ratio, 150);`  

### Rank the companies based on the trend of the average ratio over time  
`-rank(ts_mean(average_ratio,150) - average_ratio)`  

## You can create alphas for CHINA Market! TS5  

- HYPOTHESIS: Retained Earnings is a measure of a firm's net income that it has accrued over time and saved after the distribution of dividend. So Retained Earnings are an indicator of the capability of future investment and dividend.  
- IMPLEMENTATION: Use sharesout to normalize the amount of retained earnings; then apply ts_delta() operator to capture the change of the ratio over the last three months (one quarter). Finally use rank() operator to normalize the result.  
`rank(ts_delta(retained_earnings / sharesout, 63))`  

- Note - 63 days in a quarter,  
- We missed by just sharpe ratio !  

## TS6- Some strategies are meant for big companies  

- HYPOTHESIS: Companies with high asset fair value but comparatively lower EBIT are likely companies that have invested for growth over the past years and have more room for growth in the future  
- IMPLEMENTATION: Rank domestic and foreign EBIT separately with grouping by industry, because different industries may have different splits between domestic and foreign EBIT. Set lower alpha signal for companies with lower asset fair value.  
- Note - Alpha would work well if comparing among companies that are already more sizeable (TOP500), because companies that are too small may consider this metric as too risky as it is a sign of lower cashflows.  
`alpha = -group_rank(fnd2_ebitdm, industry) - group_rank(fnd2_ebitfr, industry);`  
`group_rank(fn_assets_fair_val_a, industry) > 0.5 ? alpha * 2 : alpha`  

- Above is if-else condition operator ⇒ cond ? expr1 : expr2  
- If cond is True, then expr1, else expr2.  


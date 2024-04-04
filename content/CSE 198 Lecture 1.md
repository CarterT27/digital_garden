---
tags:
- "Type/Note"
- "Topic/Quantitative_Trading"
- "Class/CSE_198"
date:
- 2024-04-03
---
Source:  

## Syllabus  

Week 1: Trading Terminologies and Market Making  
Week 2: Stock Options and Trading Floors  
Week 3: Risk Analysis, Hedging and Greeks Variable (Remote)  
Week 4: Models - Black-Scholes, Stochastic  
Week 5: Trading Strategies 1 - Moving & Exponential Averages  
Week 6: Trading Strategies 2 (Remote)  
Week 7: Accessing and Reading Real Time Stocks Data - NASDAQ  
Week 8:  
Week 9:  
Week 10:  

## Terminologies in Trading  

Bid: The (highest) price for which someone is willing to buy something.  
Offer: The (lowest) price at which someone is willing to sell something.  
Size: The amount of contracts one is willing to trade at a price.  
Make a market: To provide a bid and ask price and sizes for each.  
Spread: The difference between the bid and ask price.  
Hedge: A trade or investment to reduce the risk of price movement in an asset.  
Paper: The interested parties trading against Akuna (or other market makers).  
Broker: A person or company that acts as an intermediary between buyers and sellers.  
Tick size: The increment between one level and the next level.  
Queue Priority: A structure used to determine the right of precedence between those in the list.  
Common: Price-time priority  

## Stock Markets  

50 bid for 100 - willing to buy 100 shares for a price of 50  
30 offered at 54 - 30 shares selling at price of 54  

**Hit the bid** is to sell a stock to another party at its bid price.  
**Lift the offer** means buyer agrees to buy at the lowest bid price.  
Data list of individual orders is called **Market Depth**  

## Market Making  

The way most High Frequency Trading (HFTs) firms make money  

| Buy         |       | Sell  |          |  
| ----------- | ----- | ----- | -------- |  
| Quantity    | Price | Price | Quantity |  
| By Veer 100 | 51    | 53    | 100      |  
| 100         | 50    | 54    | 30       |  
| 50          | 48    | 56    | 200      |  
| 200         | 47    | 57    | 500      |  

Veer, an HFT quant, enters the market. Optimistically, he will sway the Seller 1 to sell at 51 and buyer 1 to buy at 53. Net, he makes \$2 per stock.  

## How to Represent Data  

Line Charts - Plots the closing prices of any stocks over time.  
Candlesticks charts - Developed in Japan. The chart utilizes the opening, high, low, and closing price data (OHLC) per specified time interval.  
Bar Charts - American version of Candlesticks.  

## Optional Terminologies  

Immediate or Cancel (order): A type of order that requires all or part of the order to be executed immediately. Unfilled parts of order are cancelled.  
Good for Day (GFD) order: A type of order that will remain active until executed (in part or full) or until the end of the trading day. Then canceled.  
Good-Til-Cancelled (GTC): A type of order that will remain active until completed or cancelled.  
All-or-None (AON): An order type that must be executed in its entirety, or not executed at all.  
Fill or Kill (FOK): An order type that must be executed immediately in its entirety. Otherwise order is cancelled. (Few seconds, floor trading)  

https://www.bloomberg.com/features/2015-stock-chart-trading-game/  

Fail value of a stock  
Internal Fair - intuition  
Theoretical Fair - valuation from models such as DCF or Black Scholes  
True Value - based on a perfect model that analyzes all available past data  
Actual market price can be different from Intrinsic, Theoretical, and True values  
Market is **efficient** if Market Price = True Value  

## Efficient Market Hypothesis  

1. States that share prices reflect all available information and consistent alpha generation is impossible.  
2. EMH argues that markets are efficient, leaving no room to make excess profits by investing since everything is already fairly and accurately priced.  
3. Market inefficiencies may exist due to information asymmetries, a lack of buyers and sellers (i.e. low liquidity), high transaction costs or delays, market psychology, and human emotion  

Weak-Form EMH - All past information like historical trading price and volume data is reflected in the market prices.  
Semi-Strong EMH - All publicly available information is reflected in the current market prices.  
Strong-Form EMH - All public and private information, inclusive of insider information, is reflected in market prices.  

## Key Parameters to Consider When Trading Stocks  

https://tquantt.ucsd.edu/blog/post-detail/3  

> [!definition] Price to Earnings (P/E) Ratio  
> The P/E ratio is a fundamental indicator that helps you evaluate a stock's valuation. It is calculated by dividing the stock's market price by its earnings per share (EPS). A high P/E ratio indicates that investors have high expectations for future growth, while a low ratio may suggest undervaluation. When buying, a favorable P/E ratio can be a good sign, but when selling, it's essential to keep an eye on whether the ratio has reached an unsustainable level.  
> $\frac{\text{Net Income - Preferred Dividends}}{\text{End-of-Period Common Shares Outstanding}}$  

> [!definition] Earnings Per Share (EPS)  
> EPS measures a company's profitability and is calculated by dividing the company's net income by the number of outstanding shares. A rising EPS over time can indicate a healthy and growing company. When buying, look for stocks with a strong EPS, and when selling, consider a decline in EPS a warning sign.  

> [!definition] Dividend Yield  
> Dividend yield is the annual dividend payment as a percentage of the stock's current market price. This is especially important for investors looking for passive income. A high dividend yield can provide a steady stream of income, making a stock attractive for buying, while a lower or declining yield might signal the right time to sell.  

> [!definition] Price-to-Book Ratio  
> The P/B ratio compares a stock's market value to its book value (the value of assets minus liabilities). A low P/B ratio suggests that a stock may be undervalued, while a high ratio may indicate overvaluation. When buying, a low P/B ratio can be a good indicator, and when selling, a high P/B ratio might suggest it's time to cash in on profits  

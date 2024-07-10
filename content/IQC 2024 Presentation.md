---
tags:
- "Type/Note"
- "Topic/Quantitative_Finance"
- "Club/Triton_Quantitative_Trading"
date:
- 2024-07-02
---

# Introduction

## Who we are

- Group of four first-year undergraduates at University of California, San Diego
- Studying Data Science, Computer Science, Math, and Economics

# Alpha 1 - Social media sentiment

## Idea

## Implementation

Parameters, code, optimizations

## Performance

## Improvements

# Alpha 2 - Volatility Bolinger Bands

## Idea

## Implementation

Parameters, code, optimizations

```
gp = subindustry;
volatility_turnover_rank = rank(-mdl175_volatility * log(volume)) * (1 + group_rank(mdl175_revenuettm,gp));
volatility_neut_turnover_moving_avg = group_vector_neut(volatility_turnover_rank, ts_mean(mdl175_02amvt, 50), gp);
alpha = volatility_neut_turnover_moving_avg * rank(vwap) * (1 - rank(volume * close));

buy_event = open > mdl175_bollup && volume > 1.03 * adv20;
sell_event = open < mdl175_bolldown && volume < 0.94 * adv20;

trade_when(buy_event, alpha, sell_event)
```

Market - China
0 Decay, 0 Delay
0.01 truncation
Market neutralization because it was handled with gp variable

## Performance

## Improvements

# Alpha 3 - {}

## Idea

## Implementation

Parameters, code, optimizations

## Performance

## Improvements

# Conclusion

- This competition was an introduction to quantitative finance for a lot of us, and we learned a lot along the way

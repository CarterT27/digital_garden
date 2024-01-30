---
tags:
- "Type/Definition"
- "Topic/Data_Science"
- "Class/DSC_10"
---

> [!definition] Float Data Type
> In Python, the `float` data type is a number with a decimal point.  

Floats may be printed using scientific notation.

```python
type(23.0) # float
type(3.2 + 2.5) # float
2.0 ** 300 # 2.037035976334486e+90
```

---

Floats have limited precision. The final few decimal places after arithmetic can be unexpectedly wrong.
> [!question]- Why are floats inaccurate?
> https://stackoverflow.com/questions/21895756/why-are-floating-point-numbers-inaccurate  

Floats have limited size.
```python
2.0 ** 3000 # OverflowError: (1, 'Numerical result out of range')
```

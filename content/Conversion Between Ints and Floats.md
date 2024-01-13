---
tags:
  - "Type/Remark"
  - "Topic/Data_Science"
  - "Class/DSC_10"
---

> [!example] Conversion Between Ints and Floats
> If you mix [[Int Data Type|ints]] and [[Float Data Type|floats]] in an expression, the result will always be a `float`.
> Note that when you divide two `int`s, you get a `float` back.
> A value can be explicity **coerced** (i.e. converted) using the `int` and `float` functions.
> Calling the `int` function on a float truncates everything after the decimal point.

```python
2.0 + 3 # 5.0
12 / 2 # 6.0
int(12 / 2) # 6
int(-2.9) # -2
```
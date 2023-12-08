---
tags:
  - "#Type/Definition"
  - "#Topic/TOPIC"
  - "#Class/CLASS"
---

> [!definition] Element-Wise Arithmetic
> Operations that are computed**element-wise** mean that the arithmetic operation is applied to one pair of elements from each [[Array|array]] at a time.  
> Both arrays must have the same length.

```Python
a = np.array([4, 5, -1])
b = np.array([2, 3, 2])

a + b # array([6, 8, 1])
a / b # array([ 2., 1.66666667, -0.5])
a ** 2 + b ** 2 # array([20, 34, 5])
```
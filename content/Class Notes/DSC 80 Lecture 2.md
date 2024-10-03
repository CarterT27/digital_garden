---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/DSC_80"
date:
- 2024-10-01
---

```python
sample = np.random_choice([True, False], size=len(df))
df[sample] # randomly select rows from df
```

# `numpy` overview

**fast** computation involving arrays and matrices

`numpy` arrays
- homogeneous - all values are of the same type
- (potentially) multi-dimensional

`numpy` computation is fast because
- much of it is implemented in `C`
- `numpy` arrays are stored more efficiently in memory than Python lists

`array.argmax()` gets the first index of the max element in the array

for loop vs. vectorized arithmetic in numpy

```python
%%timeit
squares = []
for i in range(1_000_000):
    squares.append(i * i)
```

```python
%%timeit
squares = np.arange(1_000_000) ** 2
```

## 2D arrays

Using axis to compress along axes for computations

Using square brackets to index using same slicing as Python or commas

```python
a[0][1]
a[0, 1]
```

## Pictures as numpy arrays

Each image has pixels of RGB

Grayscale by averaging RGB values
```python
mean_2d = img.mean(axis=2)
mean_3d = np.repeat(mean_2d[:, :, np.newaxis], 3, axis=2)
```

Sepia filter

```python
sepia_filter = np.array([
    [0.393, 0.769, 0.189],
    [0.349, 0.686, 0.168],
    [0.272, 0.534, 0.131]
])
filtered = (img @ sepia_filter.T).clip(0, 1)
filtered
```

## Pandas

DataFrame: 2d tables  
Series: 1d array-like object  
Index: sequence of column or row labels

```python
import pandas as pd
import numpy as np
```

- The standard way to select a column in `pandas` is by using the `[]` operator
- Specifying a column name returns a Series
- Specifying a list of column names returns a DataFrame

Querying with multiple conditions: use `&` and `|`  
Querying using `.query()` - can use `and` and ignore parentheses

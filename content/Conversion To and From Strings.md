---
tags:
  - "#Type/Remark"
  - "#Topic/Data_Science"
  - "#Class/DSC_10"
---

> [!example] Conversion To and From Strings
> Any value can be converted to a string using `str`.  
> Some strings can be converted to `int` and `float`.

```Python
str(3) # '3'
float('3') # 3.0
int('4') # 4
int('word') # ValueError: invalid literal for int() with base 10: 'word'
int('4.3') # ValueError: invalid literal for int() with base 10: '4.3'
```
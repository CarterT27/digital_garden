---
tags:  
- "Type/Definition"  
- "Topic/Data_Science"  
- "Class/DSC_10"  
---
  
> [!definition] String Methods  
> **String methods** are special functions for working with [[String Data Type|strings]].  
  
Common string methods include `str.upper`, `str.title`, and `str.replace`  
  
```python  
my_cool_string = 'data science is super cool!'  
my_cool_string.title() # 'Data Science Is Super Cool!'  
my_cool_string.upper() # 'DATA SCIENCE IS SUPER COOL!'  
my_cool_string.replace('super cool', '💯' * 3) # 'data science is 💯💯💯!'  
```  
  
> [!warning]- `len(my_cool_string)` is not a method  
> `len` does not use dot notation, so it is a regular function, not a method.  

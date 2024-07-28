---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/DSC_20"
date:
- 2024-03-06
---
Source: https://docs.google.com/presentation/d/1vRgHqvw7YxlADO_tKuuNWONEkH1onKFwYxtCT9kFCcU/edit#slide=id.p1 (cont.)  

## Special Methods  

> [!note] Special Method Names in Python  
> `__init__`: Method invoked automatically when an object is constructed  
> `__repr__`: Method invoked to display an object as a Python expression  
> `__add__`: Method invoked to add one object to another  
> `__bool__`: Method invoked to convert an object to True or False  
> `__float__`: Method invoked to convert an object to a float (real number)  

## Implementing `str` and `repr`  

> [!note] Implementing `str` and `repr`  
> The behavior of `str` is complicated:  
> - An instance attribute called `__str__` is ignored  
> - If no `__str__` attribute is found, uses `repr` string  
> - By the way, `str` is a class, not a function  
>   - When you call `str`, you call a constructor for the built-in string type called `str`  

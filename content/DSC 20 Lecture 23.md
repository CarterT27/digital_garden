---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/DSC_20"
date:
- 2024-03-04
---
Source: https://docs.google.com/presentation/d/1vRgHqvw7YxlADO_tKuuNWONEkH1onKFwYxtCT9kFCcU/edit#slide=id.p1  

# String Representation and Special Methods  

> [!note] String Representations  
> - An object value should behave like the kind of data it is meant to represent  
> - For instance, by producing a string representation of itself  
> In Python, all objects produce **two** string representations  
> - The `str` is easy for humans, to be readable  
>   - Informal representation  
> - The `repr` is easy for the Python interpreter  
>   - Official representation  

> [!note] The `repr` String for an Object  
> The result of calling `repr` on a value is what Python **prints** in an interactive session  
> Some objects do not have a simple Python-readable string  
> The `repr` function returns a Python expression (a string) that evaluates to an equal object (same object when passed to `eval()`): https://docs.python.org/3/library/functions.html#repr  
> - i.e. `eval(repr(object)) == object`  

> [!note] `eval()`  
> **utility** which lets Python program run Python code within itself, by evaluating *expressions*.  
> - It is used on sites like [codepad.org](https://codepad.org) to allow you to execute scripts in a test environment.  
> `eval(expression, globals=None, locals=None)`  
> - **expression**: this string is parsed and evaluated as a Python expression  
> - **globals (optional)**: a dictionary to specify the available global methods and variables  
> - **locals (optional)**: another dictionary to specify the local methods and variables  

> [!definition] Polymorphic Functions  
> **Polymorphic function**: a function that applies to many (*poly*) different forms (morph) of data  
> `str` and `repr` are both polymorphic; they apply to any object  
> `repr` asks an argument to display itself  
> invokes a zero-argument method `__repr__` on its argument  

> [!note] User-defined classes  
> - Need to have methods `__str__` and `__repr__` in order to be able to print string representation of an object.  
> - If `__str__` does not exist, then `__repr__` will be used  
> - At the very least, you should implement `__repr__`  

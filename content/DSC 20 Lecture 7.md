---
tags:
- Type/Note
- Topic/Data_Science
- Class/DSC_20
date:
- 2024-01-24
---
# Assert Statements in Python  

> [!note] Asserts and Exceptions  
> Assertions should be used to check something that should never happen, while an exception should be used to check something that might happen.  

> [!note] Assertions  
> `assert` is a keyword in Python  
> Syntax:  
> ```Python  
> assert "condition"  
> assert "condition", "optional error message"  
> ```  
> If condition is `False` raise `AssertError` exception  
> - Assertions can be disabled at runtime using parameters, and [are disabled by default](http://java.sun.com/javase/6/docs/technotes/tools/windows/java.html), so don't count on them except for debugging purposes.  
> - Using -O    ( O is for Optimized)  
> - Assertions are used for debugging purposes only.  

> [!note] `type()` vs. `isinstance()`  
> ```Python  
> name = "Carter"  
> print(type(name) == str) # True  
> print(isinstance(name, str)) # True  
> ```  

> [!note]  
> ```Python  
> print(isinstance(1, int))  
> print(isinstance(True, int)) # True, because booleans are a subclass of integers  
> ```  

> [!note] In this class, we will use `assert`, `type()`, `isinstance()` to validate function parameters  
> This is not recommended in production code.  

> [!note] `callable()`  
> Check if something is a function  
> ```Python  
> def my_func():  
> 	return  
> print(callable(my_func))  
> ```  

> [!note] `all()`  
> The `all()` function returns `True` if all items in an iterable are true, otherwise it returns `False`.  
> ```Python  
> lst1 = [1, 2, 3, 4]  
> lst2 = [1.1, 2, 3, 4]  
> assert all([isinstance(elem, int) for elem in lst1]), 'each elem is not int in lst1'  
> assert all([isinstance(elem, int) for elem in lst2]), 'each elem is not int in lst2'  
> ```  

> [!note] `any()`  
> The `any()` function returns `True` if at least one item in the iterable is true, otherwise it returns `False`.  

> [!note] Can't check for integers in list before checking if it is actually a list  

> [!note] Realistic example of assert  
> ```Python  
> def apply_discount(product, discount):  
> 	price = int(product['price']*(1.0 - discount))  
> 	assert 0 <= price <= product['price']  
> 	return price  
> ```  

> [!note] General rules  
> Don't use asserts for data validation  
> - can be disabled  
> - homeworks: for grading/learning purposes  
> Asserts that never fail  

# Strings  

> [!note] Representing data  

> [!note] Representing language  

> [!note] Representing program  

> [!note] Escape characters  
> ```Python  
> try:  
> 	print("Hello "Carter"")  
> except Exception as e:  
> 	print(e)  
> print("Hello \"Carter\"")  
> print("Hello \\Carter\\)  
> ```  

> [!note] `\a` Bell escape character  
> Makes noise?  
> Originated to alert programmers when their programs finished  

> [!note] String operations  
> `str * int`: `str` written `int` times  
> `str[int]`: character at `int` index of `str`  
> `str[int:int]`: substring from `int` index to `int` index  

> [!note] Slicing `str[int:int:int]`  
> Can omit indices, use negative indices, specify step  
> ```Python  
> test_str = 'abcdefghijklmnopqrstuvwxyz'  
> print(test_str[::-2])  
> ```  

> [!note] String modification  
> `str[16] = ""` 'str' item does not support item assignment (immutable)  
> `str = str[:16] + " " + str[17:]`  

> [!note] `str.replace()`  
> ```Python  
> newStr = "The exam is coming."  
> print(newStr.replace("coming", "cancelled")) # Does not modify newStr  
> print(newStr)  
> exam = newStr.replace("coming", "cancelled")  
> print(exam)  
> ```  

---
tags:  
- "Type/Definition"  
- "Topic/Data_Science"  
- "Class/DSC_10"  
---
  
> [!definition] Variable  
> A place to store a value so it can be used later in code.  
  
Variables are defined using an [[Assignment Statement|assignment statement]].  
  
```python  
my_number = 27  
my_number # 27  
```  
  
---
  
Before a variable is defined, it has no meaning (evaluates to None).  
  
```python  
undefined_variable # Prints nothing, the value is None  
```  
  
---
  
Variables should have helpful, descriptive names so you know what they refer to.  
> [!warning] Unhelpful variable names  
> ```python  
> six = 15  
> i_45love_chocolate_9999 = 60 * 60 * 24 * 365  
> ```  
  
Variable names can contain uppercase and lowercase characters, the digits 0-9, and underscores.  
> [!success] Helpful variable names  
> ```python  
> seconds_per_hour = 60 * 60  
> hours_per_year = 24 * 365  
> seconds_per_year = seconds_per_hour * hours_per_year  
> ```  
  
They cannot start with a number.  
They are case sensitive!  
> [!error] Invalid variable names  
> ```python  
> 7_days = 24 * 7  
> 3 = 2 + 1  
> ```  
  
---
  
Some common naming conventions are `UpperCamelCase` for class names, `CAPITALIZED_WITH_UNDERSCORES` for constants, and `snake_case` for other names, including most variable names.  

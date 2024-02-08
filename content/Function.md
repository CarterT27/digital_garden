---
tags:
- "Type/Definition"
- "Topic/Data_Science"
- "Class/DSC_10"
---
> [!definition] Function  
> A **function** is a reusable block of code that has inputs, **arguments**, and can **return** a value when it is **called**.  

```python  
abs(-23) # 23  
```  
Here, the function name is `abs`. It is passed in the value of `-23`, and returns `23` when called with `abs()`.  

---  

Some functions can be passed a variable number of arguments.  
```python  
max(2, -3, -6, 10, -4) # 10  
max(1) # 1  
```  

---  

We can **nest** function calls to evaluate sophisticated expressions.  
```python  
min(abs(max(-1, -2, -3, min(4, -2))), max(5, 100)) # 1  
```  

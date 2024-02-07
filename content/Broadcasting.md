---
tags:  
- "Type/Definition"  
- "Topic/Data_Science"  
- "Class/DSC_10"  
---
  
> [!definition] Broadcasting  
> https://numpy.org/doc/stable/user/basics.broadcasting.html  
> **Broadcasting** is the process in [[Numpy]] that makes it easy to perform the same operation to every element in an [[Array|array]].  
  
```python  
temperature_array # array([68, 73, 70, 74, 76, 72, 74])  
  
# Increase all temperatures by 3 degrees.  
temperature_array + 3 # array([71, 76, 73, 77, 79, 75, 77])  
  
# Halve all temperatures.  
temperature_array / 2 # array([34. , 36.5, 35. , 37. , 38. , 36. , 37. ])  
  
# Convert all temperatures to Celsius.  
(5 / 9) * (temperature_array - 32)  
# array([20., 22.77777778, 21.11111111, 23.33333333, 24.44444444, 22.22222222, 23.33333333])  
```  

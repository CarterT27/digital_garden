---
tags:
- "Type/Definition"
- "Topic/Data_Science"
- "Class/DSC_10"
---
> [!definition] Array  
> **Arrays** are a [[Numpy]] [[Data Type|data type]] similar to [[List|lists]], but optimized with additional support for mathematical functions in Numpy.  

```python  
import numpy as np  
array = np.array([3, 4, 5])  
temperature_list = [68, 73, 70, 74, 76, 72, 74]  
temperature_array = np.array([68, 73, 70, 74, 76, 72, 74])  
another_temperature_array = np.array(temperature_list) # no brackets because temperature_list is already a list  
```  

---  

We can access elements in an `array` or `list` by their position.  
In Python, elements are 0-indexed(meaning the position of the first element in an array is 0, not 1).  
One interpretation of this is that an element's position represents the number of elements before it.  

```python  
temperature_array # array([68, 73, 70, 74, 76, 72, 74])  
temperature_array[0] # 68  
temperature_array[1] # 73  
```  

---  

Accessing an element at the end of an array can be done in multiple ways:  

```python  
temperature_array[6] # 74, only works for this array  
temperature_array[len(temperature_array) - 1] # 74, we subtract 1 because the array is 0-indexed  
temperature_array[-1] # 74, counts backwards  

temperature_array[-2] # 72, two from the back of the array  
```  

---  

One difference between lists and arrays is that arrays can only store one data type.  

```python  
nums_and_strings_lst = ['uc', 'sd', 1961, 3.14]  
np.array(nums_and_strings_lst) # array(['uc', 'sd', '1961', '3.14'], dtype='<U32'), numpy converted the numerical types into strings  
```  

---  

Operations with arrays are handled with a behavior called [[Broadcasting|broadcasting]].  

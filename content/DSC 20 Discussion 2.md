---
tags:
- Type/Note
- Topic/Data_Science
- Class/DSC_20
date:
- 2024-01-17
---

> [!definition] Imports
> Makes code from other packages available in your code.  

> [!note] Escape Character
> - \\ is the escape "operator"  
> - bypasses the next character for some functionality  

> [!note] Loops
> **loops** are used to repeat computations many times  
> two types of loops:  
> - while loop: uses logical conditions  
> - for loop: uses an iterable object  

> [!definition] List
> - mutable vector of values  
> - can store any data type, multiple types at a time  
> - elements are accessed via indexing  

> [!definition] Tuple
> - immutable vector of values  
> - all else equal to list  

> [!definition] Set
> - mutable vector of values  
> - only stores unique elements (removes duplicates)  
> - otherwise, list like behavior  

> [!definition] Mutability
> - Object is mutable if it can be directly changed after it is created  
> - If it can't, it is immutable  
> - Lists are mutable  
> - Strings, tuples, and numbers are immutable  

> [!definition] Indexing/Slicing
> **indexing/slicing** refers to accessing specific elemtn(s) from an iterable object  
> - iterable\[start:stop:skip](start:inclusive,stop:NOT inclusive)  
> - not every section needs to be specified (can just use start or stop or skip)  
> - sub indexes can be applied  
> - trying to access an index that doesn't exist in the list will result in an error  

> [!definition] In-Place Operations
> An operation is **in-place** if the result occurs directly ...  

> [!note] List Methods
> - `list.pop(index)` removes the element at index. in-place operation. returns the value removed.  
> - `list.append(element)` adds the element to the end of the list. in-place operation  
> - `list.sort()` sorts the list. can specify ascending or descending  

> [!note] String Methods
> - `string.split(separator)` splits a string into a list of elements on each separator  
> - `[string].join(iterable)` returns the iterable "joined" with the \[string] in between each element  
> - `string.lower()/string.upper()` lowers/uppers all elements in a string  
> - `string.title()` changes to title case like a book  
> - `string.strip()` removes whitespace from beginning and end of the string  

> [!definition] Dictionaries
> - Mutable storage of key, value pairs  
> - Can store any data type, multiple at a time  
> - Elements are accessed via keys  
> - Keys must be hashable and unique  
> Methods  
> - `dict.keys()` accessing keys  
> - `dict.values()` accessing as values  
> - `dict.items()` accessing key, value as pairs  

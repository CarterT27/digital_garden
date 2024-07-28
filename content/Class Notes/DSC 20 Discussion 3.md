---
tags:
- Type/Note
- Topic/Data_Science
- Class/DSC_20
date:
- 2024-01-24
---
> [!note] Files  
> - storage for data  
> - unique methods to access within code  
> Access modes:  
> - `w` write: wipes the file and adds your data  
> - `a` append: appends your data to the end of the file  
> - `r` read: opens the file just for reading  

> [!note] Text Processing  
> `file.read()`  
> `file.readline()`  
> `file.readlines()`  

> [!note] List Comprehension  
> - Fancy, shorthand method of writing for loops  
> - Syntax changes depending on use case  
> - Can be nested in each other, just like lists  
> - Can contain multiple for loops in one list comp  
> - Can also be a nested loop  
> Syntax  
> - `[x for x in iterable]`  
> - `[x for x in iterable if (condition)]`  
> - `[x if (condition) else y for x in iterable]`  
> - `[x if (condition) else y if (condition) else z for x in iterable]`  

> [!note] Dictionary Comprehension  
> - Fancy, shorthand method of populating dicitonaries  
> - Syntax changes depending on use case  
> Syntax  
> - basically the same as list comp, but now it expects key:value  
> - can include a list comp  
> ```Python  
> {x.split(',')[0]:x.split(',')[1] for x in data}  
> ```  

> [!note] Assert Statements  
> - Used to evaluate written code  
> - asserts -> input validation (are the arguments the correct type?)  
> - Often combined with boolean functions (`any()`, `all()`, etc.)  
> `assert isinstance(lst, list)`  

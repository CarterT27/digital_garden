---
tags:
- Type/Note
- Topic/Data_Science
- Class/DSC_20
date:
- 2024-01-31
---
> [!note] Lambda Functions  
> - known as anonymous functions (their functions are so simple, they don't need a name)  
> - syntax: `lambda (input): (some operation)`  
> - within the scope of this course, lambda is used in conjunction with map and filter  

> [!note] Iterator  
> Syntax: `iter(iterable), next(iterator)`  
> - An iterator in Python is an object that can be iterated upon, meaning that you can traverse through all the values.  
> - Typically, an iterator is created from an iterable using the `iter()` function and the elements are accessed via the `next()` function.  
> - Iterators remember the state as you traverse through them. The next call to `next()` starts off where the previous one stopped.  

> [!note] Map  
> Syntax: `map(function, iterable)`  
> - Map allows you to apply a function to all elements to an iterable input  
> - very common to use a lambda function as the function to apply  
> - returns a lazy iterator through the iterable object, applying the function as it traverses  

> [!note] Filter  
> Syntax: filter(function, iterable)  
> - Filter takes in a function that returns a boolean and only keeps elements that satisfy the function (i.e. return True).  
> - Very common to use a lambda function as the function to apply, but keep in mind the function **must return a boolean**.  
> - Returns a lazy iterator through the iterable object that only yields values that pass the function.  

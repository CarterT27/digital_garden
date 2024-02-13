---
id: DSC 20 Lecture 15
aliases: []
tags:
- Type/Note
- Topic/Data_Science
- Class/DSC_20
date:
- "2024-02-12"
---
Source: https://docs.google.com/presentation/d/15saIVRjgeoZB_ymuNC2Sa9nT4LpYJFsP/edit#slide=id.p1  

# Advanced Argument Passing  

> [!note] Argument Passing: Keyworded Arguments  
> When defining a function, you can specify only what you need  

> [!note] Default Arguments  
> Default `=` at the end  
> Order matters  
> Having a positional argument after a keyword argument will result in errors.  

> [!note] Arbitrary number of arguments  
> - Sometimes, we do not know in advance the number of arguments that will be passed into a function.  
> - We use an asterisk (\*) before the parameter name to denote this kind of argument.  
> - These arguments get wrapped up into a *tuple* before being passed into the function.  

> [!note] `**kwargs`  
> - `**kwargs` allows you to write functions with arbitrary number of arguments with names (or keywords) associated with it.  
> - The number of arguments is *variable*, because you don't know ahead how many arguments will the function get.  

> [!note] Order Matters  
> If you choose to use and combine the special matching modes, Python has two  
> ordering rules:  
> - In the call, keyword arguments must appear after all non keyword arguments.  
> - In a function header, the `*args` must be after normal arguments and  
>   defaults, and `**kwargs` must be last.  
> `def func(normal arguments, *args, **kwargs)`  

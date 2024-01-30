---
tags:
- Type/Note
- Topic/Data_Science
- Class/DSC_20
date:
- 2024-01-26
---

Source: https://docs.google.com/presentation/d/1zobt3pulWxmpmY5JYEV2nVzeM4rq0Rev2Jx1fiSJzeI/edit#slide=id.g28d07e1b48b_0_131

# Lambda Expressions (Functions)

> [!definition] Lambda Expressions
> - An expression that evaluates to a function  
> - Known as anonymous functions  
> - We use lambda functions when we require a (nameless) function for a short period of time.  
> - We generally use it as an argument to a higher-order function (soon)  
> -  Lambda functions are used along with built-in functions like filter() and  map() (soon)  
> - Used with apply when working with Pandas  
> - No “return” keyword  
> - return: Must be a single expression:  
> 	- The lambda's body is similar to what we'd put in a def body's return statement.  
> - Can not contain complex statements (like while or for loops)  

> [!note] Lambda expressions must use `else`

> [!note] `str.join(list)` Joins a list with the given string

# Iterator, Map(), Filter()

> [!definition] `Map()`
> - `map(function_to_apply, list_of_inputs)`  
> - `function_to_apply`: can be a lambda function  
> - `list_of_inputs`: iterable  
> Returns an iterable  

> [!note] Iterator object
> - Think of it as a cursor that goes along the list  
> - `next()` moves the cursor  

> [!note] Lazy Evaluation (used in iterator objects)
> Useful when you have a very large data set to compute. It allows you to start using the data immediately, while the whole data set is being computed.  

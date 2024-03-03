---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/DSC_20"
date:
- 2024-03-01
---
Source: https://docs.google.com/presentation/d/1edV5Anteq8OSMqrIEX6lZcG7zgK0_T2N/edit#slide=id.p1  

# Exceptions  

> [!note] Why?  
> - An **exception** is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions.  
>   - A function receives an argument value of an improper type  
>   - Some resource (such as a file) is not available  
>   - A network connection is lost in the middle of data transmission  
> - In general, when a Python script encounters a situation that it cannot cope with, it raises an **exception**.  
> - An **exception** is a Python *object* that represents an error.  

> [!definition] Exceptions  
> - A *built-in* mechanism in a programming language to declare and repsond to exceptional conditions.  
> - Python **raises** an **exception** whenever an error occurs  
> - Exceptions can be **handled** by the program, preventing the interpreter from halting (come to an abrupt stop)  
> - *Unhandled* exceptions will cause Python to halt execution and print a *stack trace*  
>   - Long message that tells you what line has what error  

## Raising Exceptions  

> [!note] Raise Statements  
> Exceptions are raised with a `raise` statement  
> `raise <expression>`  
> `<expression>` must evaluate to a subclass of `BaseException` or an instsance of one.  
> Exceptions are constructed like any other object. E.g., `TypeError('Bad argument!')`  
> - `TypeError`: A function was passed the wrong number/type of argument  
> - `NameError`: A name wasn't found  
> - `KeyError`: A key wasn't found in a dictionary  
> - `RuntimeError`: Catch-all for troubles during interpretation  

## Try Statements  

> [!note] Try statements  
> Try statements *handle* exceptions  
> ```Python  
> try:  
>   <try suite>  
> except <exception class> as <name>:  
>   <except suite>  
> ...  
> ```  
> Execution Rule:  
> - The `<try suite>` is executed first  
> - If, during the course of executing the `<try suite>`, an exception is raised and  
> - the `<exception class>` is executed, with `<name>` bound to the exception  

> [!note] Handling Exceptions  
> Exception handling can prevent a program from terminating  
> ```Python  
> try:  
>   x = 1/0  
> except ZeroDivisionError as e:  
>   print('handling a', type(e))  
>   x = 0  
> ```  
> Multiple try statements: Control jumps to the except suite of the **most recent** try statement that handles that type of exception  

> [!note] Multiple Excepts  
> ```Python  
> try:  
>   You do your operations here;  
> except ExceptionI:  
>   If there is ExceptionI, then execute this block.  
> except ExceptionII:  
>   If there is ExceptionII, then execute this block.  
> else:  
>   If there is no exception then execute this block.  
> ```  

> [!note] Pass: ignore and move on  
> ```Python  
> try:  
>   x = 17 + "Carter"  
> except:  
>   pass  
> ```  
> Nothing will happen and the code resumes its execution  

> [!note] Difference between **assert** and **exception**  
> `try/except` blocks let you catch and manage exceptions. Exceptions can be triggered by `raise/assert`, and a large number of errors such as trying to index an empty list. `raise` is typically used when you have detected an error condition.  
> - `raise` and `assert` have a different philosophy. There are many "normal" errors in code that you detect and raise errors on. Perhaps a web site doesn't exist or a parameter value is out of range.  
> - Assertions are generally reserved for "I swear this cannot happen" issues that seem to happen anyway. It's more like runtime debugging than normal runtime error detection. Assertions can be disabled if you use the `-O` flag or run from `.pyc` files instead of `.py` files, so they should not be part of regular error detection.  
> - If production quality code raises an exception, then figure out what you did wrong. If it raises an `AssertionError`, you've got a bigger problem.  

> [!note] Recap about exceptions  
> - **Exception**: is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions.  
> - Can occur due to different issues: syntax errors or runtime errors  
> - How to handle an exception?  
>   - Use try ... except block  
> - Exceptions are raised with a `raise` statement  

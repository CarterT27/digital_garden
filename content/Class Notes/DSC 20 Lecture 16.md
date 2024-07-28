---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/DSC_20"
date:
- 2024-02-14
---
Source: https://docs.google.com/presentation/d/1ulz0I4fynph7gmrbB766HG6ILopyuOw_FlcJGiIMgSk/edit  

# Recursion  

> [!note] What is Recursion?  
> - Algorithmically: a way to design solutions to problems by divide-and-conquer method  
>   - Reduce a problem to a simpler version of the same problem  
> - Semantically: a programming technique where a function calls itself  
>   - In programming, the goal is NOT to have an infinite recursion  
>   - Must have at least 1 base case that are easy to solve  
>   - Must solve the same problem on some other input with the goal of simplifying the larger problem input.  

> [!note] Why Recursion?  
> - Why do we use it?  
>   - Perfect for problems where there is an obvious answer for some small problem and all larger problems build from smaller problems  
> - There are iterative (loop based) solutions for every problem solvable with recursion. Use whichever is simpler  
>   - Although there may be performance implications of each  

> [!definition] Recursive Functions  
> A function is called **recursive** if the body of the function **calls** itself.  

> [!note] Recursion: Base Case  
> - Know when to stop! Known as the base case  
>   - When the array only has one element (or no elements)  
>   - Solution to a small problem  

> [!note] Steps to design a recursive algorithm  
> - Base Case:  
>   - For small values of n, it can be solved directly  
> - Recursive case(s):  
>   - Smaller versions of the same problem  
> Algorithmic Steps  
> - Identify the base case and provide a solution for it  
> - Reduce the problem to a smaller version of itself  
> - Move towards the base case using smaller input versions  

## Mutual Recursion  

> [!note] Direct Recursion  
> ```Python  
> def function(x):  
>   ...  
>   function(x-1)  
>   ...  
> ```  

> [!note] Indirect (Mutual) Recursion  
> ```Python  
> def function_a(x):  
>   ...  
>   function_b(x-1)  
>   ...  
> def function_b(y):  
>   ...  
>   function_a(y-2)  
>   ...  
> ```  

## Tree Recursion  

> [!note] Tree Recursion  
> Tree-shaped processes arise whenever executing the body of a recursive function makes more than one recursive call.  

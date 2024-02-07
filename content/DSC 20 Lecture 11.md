---
tags:  
- Type/Note  
- Topic/Data_Science  
- Class/DSC_20  
date:  
- 2024-02-02  
---
  
Source: https://docs.google.com/presentation/d/13tq-_X0-q12T5oxLZIeGv9OU9rOzqxF05s8iXGFnlg0/edit#slide=id.g1221aeef44a_0_1050  
  
# Higher-Order Functions  
  
> [!note] Guide to Designing Functions  
> - Give each function exactly one job, but make it apply to many related situations  
> - Don't Repeat Yourself (DRY): Implement a process just once, but execute it many times  
> - Define functions generally  
  
> [!note] Overall Idea  
> - Want: is the ability to build **abstractions** by assigning names to common patterns and then to work in terms of the names directly.  
> - Need: to construct functions that can *accept* other functions as arguments or *return* functions as values.  
> - Functions that manipulate functions are called **higher-order** functions  
  
## Nested Functions and Closures  
  
> [!note] Encapsulation  
> A function can be created as an inner function in order to protect it from everything that is happening outside of the function. In that case, the function will be hidden from the global scope.  
  
> [!note] Locally Defined Function  
> Functions defined within another function bodies are bound to names in a local frame.  
  
> [!note] The Purpose of Higher Order Functions  
> Higher-order function: A function that takes a function as an argument value or returns a function as a return value  
> Useful:  
> - Express general methods of computation  
> - Remove repetition from programs  
> - Each function has exactly one job  
> Environment diagrams describe how higher-order functions work!  
  

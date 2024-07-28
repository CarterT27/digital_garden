---
tags:
- "Type/Note"
- "Topic/Data_Structures"
- "Class/DSC_30"
date:
- 2024-04-05
---
Source: https://docs.google.com/presentation/d/1dhz8i4x4Q89OnVy5K6I-95i7pxSX4UWy/edit#slide=id.p1  

## Constructor  

- Same name as the class, no return type  
- Called automatically by `new` operator  
- Often overloaded:  
- Constructor without parameters is called the *default* constructor  

## Stack  

> [!definition] The Stack ADT (Abstract Data Type)  
> A **Stack** is a collection of objects inserted and removed according to the Last In First Out (LIFO) principle. Think of a stack of dishes.  

Aside: only two data structures are array-based form and link-based form  

## Stack Operations  

**Push** and **Pop** are the two main operations  

## A lot of applications  

- Think of the **undo** operation of an editor. The recent changes are **pushed** into a stack, and the undo operation **pops** it from the stack.  
- Reverse strings  
- The expression evaluation stacks are also used for parameter passing and local variable storage.  
- Think of ED diagrams and recursions!  
- Check if a given expression has correct “(“ ,   “)” order.  

## Classic Example: Parenthesis Checker  

(2 + 3) - (4 + 1)  
- Push “(“  
- Ignore 2,“+”, 3  
- If you see” )” then Pop “(”. Exists?  
- Ignore “-”  
- Push “(“  
- Ignore 4, “+”, 1  
- If you see” )” then Pop “(”. Exists?  
- Empty Stack, empty Input! Hooray!  

## Implementation. Arrays  

**Main update methods:**  
- `Push(e)`: add an element to the stack  
- `Pop()`: remove an element from the stack  

**Additional useful methods**  
- `Peek()`: Same as pop, but does not remove the element  
- `Empty()`: Boolean, True when the stack is empty  
- `Size()`: Returns the size of the stack  

## Implementing stack  

top can either be 0 or -1  

if top is -1  
```Java  
push(int elem) {  
st[top] = elem;  
}  
```  

```Java  
pop() {  
// check for corner cases  
top--;  
return st[top];  
}  
```  

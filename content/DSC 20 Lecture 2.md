---
tags:
  - "#Type/Note"
  - "#Topic/Data_Science"
  - "#Class/DSC_20"
date:
  - 2024-01-10
---

Source: https://docs.google.com/presentation/d/1c9pHlFfRfZfS_iDAmV27IWpSbavJQ51uPN8Z3Fh1hMo/edit#slide=id.gd19033697b_0_0

# Short circuiting with booleans

```Python
>>> 1/0
Error
>>> False and 1/0
False
```

> [!definition] Short Circuiting
> Stopping of execution of boolean operation if the truth value of expression has been determined already.

> [!example] Practice Short Circuiting
> ```Python
> >>> True and False
> False
> >>> True or False and False
> True
> >>> 2 or not 2
> 2
> >>> "Be" and 1 and 2 and 3 and 4 and 5
> 5
> >>> 3 or 1/0 and 5
> 3 # expression short circuits at 3 or and evaluates to 3 without evaluating 1/0 and 5
> >>> 0 or 0 and 1/0
> 0
> >>> 0 or 5 and 1/0
> Error
> ```

# Variables

> [!definition] Variable
> A **variable** is a named memory location (box) that contains a value (in the box) and can be used in expressions.

# Assignment

> [!definition] Execution Rule
> 1. Evaluate all expressions to the right of = from left to right. 
> 2. Bind all names to the left of = to those resulting values.

> [!example]
> ```Python
> >>> a, b = 0, 1
> >>> a, b = b, a
> >>> a, b
> (1, 0)
> ```

> [!note] Do not name your variables as built-in function names
> E.g. sum, max, etc.

> [!definition] Functions
> A **function** takes as input one or more arguments, computes a new value, a string or a number, and returns the value, so that it can be assigned to a variable or output.

> [!note] Parameters vs. Arguments
> The **arguments** are the data you pass intoo the function's **parameters**.

> [!note] Control Flow
> 1. Reading the function definition without executing
> 2. Seeing a "call" to the function, jumping up to the start of the function and executing
> 3. Returning back to the place in the program that called the function and continuing. 
---
tags:
  - "Type/Note"
  - "Topic/Data_Science"
  - "Class/DSC_20"
date:
  - 2024-01-09
---

Source: https://docs.google.com/presentation/d/1BIX3N29ThpFJMh3NJnudmct-kLhylWpWOctIW-xwARk/edit#slide=id.gd19033697b_0_0

# Expressions vs Statements

> [!definition] Expression
> A representation of something. Python evaluates expressions, resulting in a value.

> [!definition] Statement
> Does something. Python executes statements, not necessarily resulting in a value.

# Integer Operations
+, -, *, /,
\**,  unary -

> [!note] Operations on integers must yield integers
> Example: 
> ```Python
> >>> 1/2
> 0.5
>  ```
>  / is not an integer operation
> ```Python
> >>> 1//2
> 0
> ```

# Float Type
- Values are approximations of real numbers
- Numbers with "." are float literals
- Numbers without "." are int literals

Floats have finite precision because they are represented as an integer mantissa times a power of 2. This results in an approximation error.

> [!example] 0.1 + 0.2
> ```Python
> >>> 0.1 + 0.2
> 0.30000000000000004
> ```

[Read More](https://medium.com/better-programming/why-is-0-1-0-2-not-equal-to-0-3-in-most-programming-languages-99432310d476)

# Str type
- Any sequence of characters
- + operation concatenates strings (cannot add `'string' + 2`)
- **String literal**: a sequence of characters in quotes

# Bool type
- True, False
- operations: not, and, or
- comes from comparing other types (>=, <=, \==, !=, etc.)

# Converting between types
- `type(value)`
- explicit conversion through casting (`int(2.0)`)

# Short circuiting
- boolean expressions stop evaluating if the truth value is already determined
- ```Python
>>> False and 1/0 # 1/0 by itself would produce an error
False
```
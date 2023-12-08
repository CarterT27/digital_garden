---
tags:
  - "#Type/Definition"
  - "#Topic/Data_Science"
  - "#Class/DSC_10"
---

> [!definition] Assignment Statement
> Assignment statements define variables by evaluating the expression on the right side and assigning the value to whatever is on the left side.

```Python
zebra = 23 - 14
zebra # 9
```

When run, the interpreter first evaluates the expression $23-14$, $9$, and assigns the value $9$ to the [[variable]] named *zebra*.

---

Using variables in an expression without using an assignment statement will not change the value of the variable.

```Python
zebra * 3 # 27
zebra # 9

zebra = zebra + 2
zebra # 11
```
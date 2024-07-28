---
tags:
- Type/Note
- Topic/Data_Science
- Class/DSC_20
date:
- 2024-01-22
---
Source: https://docs.google.com/presentation/d/14EF42i3A8RrRnhmocf0F5s40H7aht5Pl7UVHh3PEPzs/edit  

> [!note] Working with files  
> ```Python  
> with open('DSC 20 Lecture 6.md', 'r') as f:  
> 	read_data = f.read()  
> f.closed # True  
> ```  

> [!note] Writing to a file  
> 1. Open file in writing mode ('w' or 'a')  
> 2. Use `.write` method and pass a string that you want to write to a file  
> Note: must cast to string when writing to file  

# List Comprehension, Strings  

> [!note] List Comprehension Came From Math  
> It is Python's way of implementing a well-known notation for sets as used by mathematicians.  
> $\{x^{2}\vert x\in\mathbb{N}\}$  
> An elegant way to create lists in Python  
> Faster than a regular loop with append  

> [!question] Convert C to F  
> ```Python  
> ctemps = [24,20,56,32,10]  
> # For loop  
> ftemps = []  
> for c in ctemps:  
> 	f = C_to_F(c)  
> 	ftemps.append(f)  
> # List comp  
> [C_to_F(c) for c in ctemps]  
> ```  

```Python  
[str(i) + str(j) for i in range(3) for j in range(2)]  
```  

```Python  
sentence = "What did the fish say when it swam into the wall? Dam!"  
words = sentence.split()  

print([len(word) for word in words if word != "the"])  
```  

```Python  
[[1 if i_idx == row_idx else 0 for i_idx in range(0,3)] for row_idx in range(0,3)] # 3x3 diagonal matrix  
```  

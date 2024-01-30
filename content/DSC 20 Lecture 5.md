---  
tags:  
- Type/Note  
- Topic/Data_Science  
- Class/DSC_20  
date:  
- 2024-01-19  
---  
  
> [!note] Dictionary iterates keys by default  
> ```Python  
> d = {"key1":"value1","key2":"value2","key3":"value3"}  
> for key in d:  
> 	print(key)  
> ```  
  
> [!note] Basic File Usage  
> `with open(file_name, [access_mode]) as f:`  
> - `file_name`: a string value  
> - `access_mode`: determines the mode in which the file has to be opened, i.e., read, write, append, etc.  
  
> [!note] `f` methods  
> - `f.write(data)`: writes the string to the file, needs `'\n'` if writing multiple lines  
  
> [!note] access modes  
> - `w`: overwrites the file  
> - `a`: appends data to the end of the file  
> - `r`: read-only file access  
  
> [!note] Ways to read a file  
> `with open('myfile.txt', 'r') as f:`  
> 1. `print(f.read())`  
> 2. `for line in f.readlines():\n\tprint(line)`  
> 3. `for line in f:\n\tprint(line)`  

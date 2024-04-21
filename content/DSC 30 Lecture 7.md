---
tags:
- "Type/Note"
- "Topic/Data_Structures"
- "Class/DSC_30"
date:
- 2024-04-15
---

Source: https://docs.google.com/presentation/d/1J3pc0cppixQEYul-UMnkKf4ukbmhTnkh/edit#slide=id.p1  

# Static/Non-Static  

### Memory  

- Stack - The stack is for local variables and for maintaining a record of function calls. The stack grows from the top of memory down towards the heap.  
- Heap - The heap is for dynamically allocated data items. The heap grows from the top of the static data area up as data items are allocated.  

- Static Data - This is a block of reserved space in RAM for all the global and **static** variables from your program. Allocated once and lasts for duration of a program.  
### Static: Belongs to the class  

- Class creates objects  
- Constructor makes them unique (if needed)  
- How to create a property that all objects share?  
- You do not want to modify this property for each object. You may want to change it just once!  
- Example: number of the cars sold, sound of the horn  

### Static: Shared properties and methods  

### Static variables: Common to all instances  (One fixed memory location)  

```java  
public static void main(String[] args)  
```  

### One special role for strings: Command line arguments  

```java  
public class ArgsDemo {  
/** Prints out the 0th command line argument. */  
public static void main(String[] args) {  
System.out.println(args[0]);  
}  
}  
```  



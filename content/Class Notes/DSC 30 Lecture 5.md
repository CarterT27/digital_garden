---
tags:
- "Type/Note"
- "Topic/Data_Structures"
- "Class/DSC_30"
date:
- 2024-04-10
---
Source: https://docs.google.com/presentation/d/1lgH34pfgzLpmSYOFyfZFkRESpjgJkRVs/edit#slide=id.p1  

# Exceptions  

## Exceptions  

> [!definition] Exception  
> An exception is an **abnormal condition** in which the normal execution of a code gets interrupted.  

2 Types  
- **Checked exceptions:** you have to catch those, otherwise the program will not compile: (java.lang.Exceptions)  
- ClassNotFound  
- IOExceptions  
- **Runtime (unchecked) exceptions:** problems during runtime: java.lang.RunTimeException  
- ArithmeticException  
- IndexOutOfBounds  
- IllegalArgumentException  
- ...  

## Handling Errors  

The Java approach to handling exceptional events is to **throw** an **exception**.  
- Disrupts normal flow of the program  
- You saw that these exceptions just cause the program to crash, printing out a helpful (?) message for the user.  

## Exceptions: May be Explicitly or Implicitly Thrown  

Java itself can throw exceptions *implicitly*  
Java code can also throw exceptions explicitly using `throw` keyword  

## Try... Catch  

```java  
try {  
// code  
}  
catch (Exception e) {  
// code  
}  
```  

## Try... Catch Again  

```java  
try {  
// code  
}  
catch (IndexOutOfBounds e) {  
// code  
}  
catch (ArithmeticException e) {  
// code  
}  
```  

---  

## Try-Catch and declaring exceptions  

## There are TWO ways to handle exceptions  

1. Use `try/catch` block`  
2. Use `throws` block  

---  

## Checked Exception (Code will not compile)  

### “Must be Caught or Declared to be Thrown”  

Occasionally, you’ll find that your code won’t even compile, for the mysterious reason that an exception “must be caught or declared to be thrown”.  
- The basic idea: Some exceptions are considered so disgusting by the compiler that you MUST handle them somehow.  
- We call these “checked” exceptions.  

### Checked Exceptions  

Examples so far have been **unchecked exceptions**. There are also **checked exceptions**:  
- Compiler requires that these be “caught” or “specified”.  
- Goal: Disallow compilation to prevent avoidable program crashes.  

### Unchecked Exceptions  

By contrast unchecked exceptions have no such restrictions.  
- Code below will compile just fine (but will crash at runtime).  

### Checked vs. Unchecked Exceptions  

Any subclass of **RuntimeException** or **Error** is *unchecked*, all other Throwables are *checked*.  
- Compiles fine, because the possibility of unchecked exceptions is allowed:  
```java  
public class UncheckedExceptionDemo {  
public static void main(String[] args) {  
if (today == "Wed") {  
throw new RuntimeException("as a joke"); }  
}  
}  
```  
- Won't compile, because there exists possibility of checked exception:  
```java  
public class Eagle {  
public static void gulgate() {  
if (today == "Wed") {  
throw new IOException("hi"); }  
}  
}  
```  

### Checking Exceptions  

Compiler requires that all checked exceptions be **caught** or **specified**.  
Two ways to satisfy compiler:  
- **Catch**: Use a catch block after potential exception.  
- **Specify** method as dangerous with **throws** keyword.  
- Defers to someone else to handle exception.  

If a method uses a 'dangerous' method (i.e. might throw a checked exception), it becomes dangerous itself.  

### Why Exceptions?  

Allows you to keep error handling code separate from 'real' code.  
- Consider pseudocode that reads a file  

### Error Handling Code (Naive)  

This naive approach is clearly a bad idea.  
```java  
func readFile {  
open the file;  
if (theFileIsOpen) {  
determine its size;  
if (gotTheFileLength) {  
allocate that much memory;  
} else {  
return error("fileLengthError");  
}  
if (gotEnoughMemory) {  
read the file into memory;  
if (readFailed) {  
return error("readError");  
}  
...  
} else {  
return error("memoryError");  
}  
} else {  
return error("fileOpenError");  
}  
}```  

### With Exceptions  

```java  
func readFile {  
try {  
open the file;  
determine its size;  
allocate that much memory;  
read the file into memory;  
close the file;  
} catch (fileOpenFailed) {  
doSomething;  
} catch (sizeDeterminationFailed) {  
doSomething;  
} catch (memoryAllocationFailed) {  
doSomething;  
} catch (readFailed) {  
doSomething;  
} catch (fileCloseFailed) {  
doSomething;  
}  
}```  

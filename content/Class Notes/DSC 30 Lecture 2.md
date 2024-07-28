---
tags:
- "Type/Note"
- "Topic/Data_Structures"
- "Class/DSC_30"
date:
- 2024-04-03
---
# Continuation of [[DSC 30 Lecture 1]]  

## Documenting your code with Javadoc  

```Java  
class SmallerFunction {  
/** Returns the smaller of the two */  
public static int smaller(int x, int y) {  
if (x < y) {  
return x;  
}  
return y;  
}  
}  
```  

## For Loop in Java  

```Java  
for (int i=0; i<10; i++) {  
// Loop statement to be executed  
}  
```  

## Reflections on Static Typing  

The Good:  
- Debugging is a lot easier, type errors are avoided.  
- Code on the user side has no type errors, which means phones won't crash because of type errors.  
- Programs run more efficiently in time and memory.  
- Self-documenting: YOU KNOW WHAT YOU'VE GOT  

The Bad:  
- Code is more verbose.  
- Code is less general. There is a way around this in Java (Generics)  

---  

Source: https://docs.google.com/presentation/d/1dhz8i4x4Q89OnVy5K6I-95i7pxSX4UWy/edit#slide=id.p1  

# Classes and Objects  

## Classes  

- **Constructor** - how to set up your object when it's created  
- **State (instance variables)** - what describes your object (variables)  
- **Behaviors** - what your object can do (methods)  

## Object Instantiation  

- Classes can be instantiated as **objects**.  
- We'll create a single Car class, and then create instances of this class.  
- The class provides a *blueprint* that all Car objects will follow.  
- By storing different data in **instance** variables.  
- Defining different **behaviors** in methods.  

## Defining a Typical Class (Terminology)  

**Instance Variable**. Can have as many of these as you want.  
**Constructor** (similar to a method, but not a method). Determines how to instantiate the class. Has the same name as a class.  
**Non-static method, a.k.a. Instance Method.** Idea: If the method is going to be invoked by an instance of the class (as in the static slide), then it should be non-static.  
Roughly speaking: If the method needs to use "**my** instance variables", the method must be non-static.  


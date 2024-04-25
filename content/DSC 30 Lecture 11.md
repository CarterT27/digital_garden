---
tags:
- "Type/Note"
- "Topic/Data_Structures"
- "Class/DSC_30"
date:
- 2024-04-24
---
Source: https://docs.google.com/presentation/d/17QT9WUj8D-StdA7U1XgVwEE03brrYORPLvlj-t8xY2U/edit#slide=id.gd379e3d7b3_0_127  

# Inheritance, Adapter Design Pattern, Inner Class, Object Class  

## Inheritance  

### Inheritance in Java  

- It is the **mechanism** in Java (Python) by which one class is allowed to inherit the features (fields and methods) of another class.  
- The subclass can *add* its own fields and methods in addition to the superclass fields and methods.  
- The subclass can *override* methods from the superclass  

### "Is-a" relationship  

`public class DSC30 extends DSC{}`  

### Class Hierarchy  

### Method Overriding  

- If a subclass (child class) provides the specific implementation of the method that has been declared by one of its parent class, it is known as method overriding.  
- Method overriding is used to provide the specific implementation of a method which is already provided by its superclass.  

Rules for Java Method Overriding  
1. The method must have the same name as in the parent class.  
2. The method must have the same parameter list as in the parent class.  
3. There must be an IS-A relationship (inheritance).  

*How to find:* closer scope first (just like variable names in Python)  

### Private Fields: Visible by the class members only  

### Protected fields: Visible by the subclasses only  

---  

## Adapter Pattern Design  

### Adapter Pattern  

We need to implement the Stack interface with the following methods:  
- `push (int element)` - add element on the stack  
- `int pop()` - remove element from top of the stack  
- `int peek()` - return the element at the top of the stack  

We would like to find a way to **reduce** our work  

We know that there is a nice implementation of a *Double-ended List* (head and tail) interface **DList** which provides the following methods:  
- `addFront (int element)`  
- `int removeFront()`  
- `int peekFront()`  
- `addBack(int element)`  
- `int removeBack()`  
- `int peekBack()`  

### Idea: Inheritance!  

We could just make **Stack** *extend* the **DList** and write the additional methods by using other existing methods.  

### Pros? Cons?  

It is possible just make Stack extend the DList:  
`public class Stack extends Dlist`  

> [!question] Which of the following is the biggest drawback of  this approach:  
> A: It	is inefficient from a running-time perspective: A double-ended linked	 list is not a good choice for a Stack implementation.  
> B: It	is incorrect. There is no way to implement all the methods in the	 Stack interface with the methods in the double-ended linked list.  
> C: It exposes methods that are not supposed to be part of the Stack interface.  

### Inheritance is not always the right answer  

We know that there is a nice implementation of a *Double-ended List* (head and tail) interface **DList** which provides the following methods:  
- `addFront (int element)`  
- `int removeFront()`  
- `int peekFront()`  
- `addBack(int element)`  
- `int removeBack()`  
- `int peekBack()`  

The other methods in the *DList* are public and accessible by anyone. But a *Stack* does not expose such methods!  

### Adapter Design Pattern  

- In software engineering, one of the classic "design patterns" is the *adapter*.  
- An *adapter* is a class that "maps" from the interface of one ADT -- the one we're trying to implement -- into the interface of another ADT that already exists.  
- If we adapt an **ADT B** to implement another **ADT A**, then every method of A must be "converted" into a related call of B.  
- I can use a **private** *DList* variable  
- And use its methods within a *Stack* class  

---  

## Nested Classes  

### Nested classes: briefly  

- In Java, class can have *another class* as its member.  
- The class written  within is called the **nested class**, and the class that holds the inner class is called the **outer class**.  

```java  
class Outer {  
class Inner {  

}  
}  
```  

### Nested Classes  

- Inner classes are a *security* mechanism in Java.  
- In general, a class **cannot** be associated with the access modifier **private**, but if we have the class as a member of another class, then the *inner* class can be made **private**.  

### Mapping Attributes  

- Before deciding on what methods to use, one needs to **map** the corresponding attributes.  
- **For example:** To use the List as a Stack, we need to map the **top** of the stack to some position in the list (front or back - our choice, but how to choose?)  

### Mapping Methods  

- Once this is done, we can map the methods on top of the stack to methods operating on the head of the List.  
- If we choose the front...  
- `push -> addFront`  
- `pop -> removeFront`  
- `peek -> peekFront`  

---  

## Mapping  

---  

## Object class  

### The Java Platform Class Hierarchy  

The **Object** class, defined in the `java.lang` package, defines and implements behavior common to all classes  

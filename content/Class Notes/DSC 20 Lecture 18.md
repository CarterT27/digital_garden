---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/DSC_20"
date:
- 2024-02-21
---
Source: https://docs.google.com/presentation/d/1-MMZ7LfluJuktyRK9RXDIDrWjBki5RxJuYGWLw2HSvk/edit#slide=id.p1  

# Object Oriented Programming  

## Detour: String formatting (vs. concatenation)  

> [!note] F-Strings in Python  
> ```Python  
> f"Hello my name is {name} and I am {age} years old."  
> ```  

> [!note] `.format`  
> ```Python  
> "Hello my name is {name} and I am {age} years old.".format(name='Carter', age=19)  
> "Hello my name is {1} and I am {0} years old.".format(19, 'Carter')  
> "Hello my name is {} and I am {} years old.".format('Carter', 19)  
> ```  

## Objects  

> [!note] Classes  
> - A class serves as a **template** for its **instances**.  
> - Each object serves as an *instance* of some class.  

> [!note] The Class Statement  
> - A *class statement* creates a new class and binds that class to `<name>` in the first frame of the current environment.  
> - *Assignment* and *def* statements in `<suite>`create **attributes** of the class (not names in frames)  

> [!note] Object Construction  
> When a class is called:  
> 1. A new instance of that class is created  
> 2. The `__init__` method of the class is called with the new object as its first argument (named `self`), along with any additional arguments provided in the call expression  

> [!note] Classes and Objects  
> - **Class** is a template (blueprint, factory, prototype) for creating *objects*.  
> - **Object** (instance of a class): basic unit of Object Oriented Programming and represents the *real life entities*.  
> - **Constructor**: a *special* kind of method that Python calls when it instantiates (creates) an object using the definitions found in your class.  

> [!note] Object Identity  
> - Every object that is an *instance* of a user-defined class has a unique identity  

## Methods  

> [!definition] Methods  
> **Methods** are functions defined in the suite of a class statement  

> [!note] Invoking Methods  
> All invoked methods have access to the object via the *self* parameter, and so they can all access and manipulate the object's state.  

> [!definition] Attributes  
> data that is stored within either an instance or the class itself  

@classmethod  

@staticmethod - cannot access class or instance data, they cannot modify the class state  

> [!note] Methods and Functions  
> Python distinguishes between  
> - **Functions**, which we have been using since the beginning of the course  
> - **Bound methods**, which couple together a function and the object on which that method will be invoked  
> Object + Function = Bound Method  

> [!note] Class Attributes  
> Class attributes are "shared" across all instances of a class because they are attributes of a **class**, not the instance.  

> [!note] Looking up attributes by name  
> `<expression>.<name>`  
> To evaluate a dot expression:  
> 1. Evaluate the `<expression>` to the left of the dot, which yields the object of the dot expression  
> 2. `<name>` is matched against the instance attributes of that object; if an attribute with that name exists, its value is returned  
> 3. If not, `<name>` is looked up in the class, which yields a class attribute value  
> 4. That value is returned unless it is a function, in which case a bound method is returned instead  

> [!note] Assignment to Attributes  
> **Assignment** statements with a dot expression on their left-hand side **affect** attributes for the object of that dot expression  
> - If the object is an instance, then assignment **sets** an instance attribute  
> - If the object is a class, then assignment **sets** a class attribute  

## Inheritance  

> [!note] Inheritance Terminology  
> - Parent class  
> - Super class  
> - Base class  
>  
> - Child class  
> - Subclass  
> - Derived class  

> [!note] Inheritance  
> - Inheritance is a technique for relating classes together  
> - **A common use**: Two similar classes differ in their degree of specialization  
> - The specialized class may have the same attributes as the general class, along with some special-case behavior  
> - Conceptually, the new *subclass* (child class) *inherits* (shares) attributes of its base (parent, super) class  
> - The subclass may *override* certain inherited attributes  
> - Using inheritance, we implement a *subclass* by specifying its differences from the base class  

> [!note] Looking Up Attribute Names on Classes  
> Base class attributes aren't copied into subclasses!  
> To look up a name in a class:  
> 1. If it names an attribute in the class, return the attribute value  
> 2. Otherwise, look up the name in the base class, if there is one  

## Object-Oriented Design  

> [!note] Designing for Inheritance  
> Don't repeat yourself; use existing implementations  
> Attributes that have been overwritten are still accessible via class objects  
> Loop up attributes on instances whenver possible  

> [!note] Inheritance and Composition  
> Composition: when one object has another object as an attribute  
> Inheritance is best for representing *is-a* relationships  
> Composition is best for representing *has-a* relationships  

> [!note] Multiple Inheritance  
> One child class has multiple parent classes  
> A class may inherit from *multiple* base classes in Python  

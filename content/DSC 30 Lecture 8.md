---
tags:
- "Type/Note"
- "Topic/Data_Structures"
- "Class/DSC_30"
date:
- 2024-04-17
---

Source: https://docs.google.com/presentation/d/1GwFQAmsPDPjWQEn8jE-rBv67IxofcXfB/edit#slide=id.p1

# Box and Pointer Notation

### Bits

Your computer stores information in "memory".
- Information is stored in memory as a sequence of ones and zeros.
Each Java type has a different way to interpret the bits:
- 8 primitive types in Java: byte, short, int, long, float, double, boolean, char

### Declaring a Variable (Simplified)

When you declare a variable of a certain type in Java:
- Your computer sets aside exactly enough bits to hold a thing of that type.
    - Example: Declaring an int sets aside a “box” of 32 bits.
    - Example: Declaring a double sets aside a box of 64 bits.
- Java creates an internal table that maps each variable name to a location.
- Java does NOT write anything into the reserved boxes.
    - For safety, Java will not let access a variable that is uninitialized.

### The Golden Rule of Equals (GRoE)

Given variables y and x:
- y = x copies all the bits from x into y

---

## References

### Reference Types

There are 8 primitive types in Java: 
- byte, short, int, long, float, double, boolean, char

Everything else, including arrays, is a reference type.

### Class Instantiations

When we instantiate an Object (e.g. Car, Aquarium, Queue):
- Java first allocates a box of bits for each instance variable of the class and fills them with a default value (e.g. 0, null).
- The constructor then usually fills every such box with some other value.

Can think of new as returning the address of the newly created object.
- Addresses in Java are 64 bits.

### Reference Type Variable Declarations

When we declare a variable of any reference type (Aquarium, Dog, Queue):
- Java allocates exactly a box of size 64 bits, no matter what type of object.
- These bits can be either set to:
    - Null (all zeros).
    - The 64 bit “address” of a specific instance of that class (returned by new).

### Reference Types Obey the Golden Rule of Equals

Just as with primitive types, the equals sign copies the bits.
- In terms of our visual metaphor, we “copy” the arrow by making the arrow in the b box point at the same instance as a.

---

## Parameter Passing

### The Golden Rule of Equals (and Parameter Passing)

Given variables b and a:
- b = a copies all the bits from a into b.

Passing parameters obeys the same rule: Simply copy the bits to the new scope.

### The Golden Rule: Summary

There are 9 types of variables in Java:
- 8 primitive types (byte, short, int, long, float, double, boolean, char).
- The 9th type is references to Objects (an arrow). References may be null.

In box-and-pointer notation, each variable is drawn as a labeled box and values are shown in the box. 
- Addresses are represented by arrows to object instances.

The golden rule:
- b = a copies the bits from a into b.
- Passing parameters copies the bits.

## Instantiation of Arrays

### Declaration and Instantiation of Arrays

Arrays are also Objects. As we’ve seen, objects are (usually) instantiated using the new keyword. 
- `Animal p = new Animal(0, 0, 0, 0, 0, “blah.png”);`
- `int[] x = new int[]{0, 1, 2, 95, 4};`

`int[] a;`
- Declaration creates a 64 bit box intended only for storing a reference to an int array. No object is instantiated.

`new int[]{0, 1, 2, 95, 4};`
- Instantiates a new Object, in this case an int array.

### Assignment of Arrays

`int[] a = new int[]{0, 1, 2, 95, 4};`
- Creates a 64 bit box for storing an int array address. (declaration)
- Creates a new Object, in this case an int array. (instantiation)
- Puts the address of this new Object into the 64 bit box named a. (assignment)

Note: Instantiated objects can be lost!
- If we were to reassign a to something else, we’d never be able to get the original Object back!

### Primitive Arrays

### Memory

- Primitive type variables are not initialized to 0 
- Compiler error if program uses variable before initialized
- Primitive arrays are initialized to 0 
    - What are char[ ], int[ ], float[ ], double[ ] initialized to?

---
tags:
- "Type/Note"
- "Topic/Data_Structures"
- "Class/DSC_30"
date:
- 2024-04-08
---
Source: https://docs.google.com/presentation/d/1QJtk0qU26hy_vLGz-ASaaQHnD5Ed40c2aX4X1k3EMQ0/edit#slide=id.g2c9eedc97a3_0_208  

# Stack  

## Implementation and Design  

```Java  
push (int elem) {  
top++;  
stack[top]= elem;  
}  
```  

```Java  
int pop() {  
e = stack[top];  
top --;  
return e;  
}  
```  

## Advantage and Limitation  

Advantages of Array-based Implementation Fast:  
*all* operations are completed in one step. No loops are needed O(1)  
Limitations of Array-based Implementation:  
You have to know the upper bound of growth and allocate memory accordingly. If the array is **full** and there is another **push** operation then you encounter an exception (error).  

---  

Source: https://docs.google.com/presentation/d/1ryohkuP2uwf2AyvQS37RY3F2YVS5Jozp/edit#slide=id.p1  

# JUnit, Compilation Steps  

## Testing  

Black-box Testing  
- You don't know (or you pretend you don't know) how something is implemented  
- You test only based on inputs and outputs  
Clear-box Testing (aka "white-box testing")  
- If you can look inside the black box and see how a method is implemented, you can do more detailed testing  
Why Bother? http://stackoverflow.com/questions/10858990/why-use-junit-for-testing  

## Unit (Micro)-Testing  

- Whether you are doing black-box or clear-box testing, you should test every unit of a software system.  
- What is a **unit**? In object-oriented programming, usually a software unit is taken to be a single method.  
- So: we should test every method of every class in the software.  
- JUnit is a widely used framework for unit testing of Java software.  

## Test-Driven Development (TDD)  

Steps to developing according to TDD:  
- Identify a new feature.  
- Write a unit test for that feature.  
- Run the test. It should fail. (RED)  
- Write code that passes test. (GREEN)  
- Implementation is certifiably good!  
- Optional: Refactor code to make it faster, cleaner, etc.  

Not required but testing is always needed.  

## Problem to Solve  

- Swap characters in the string:  
- "Marina" $\to$ "aniraM"  
- "Class" $\to$ "ssalC"  

```Java  
public class JUnitExample {  
public static String swap(String word) {  
char[] word_as_char = word.toCharArray();  
char temp;  
for (int i = 0; i < word.length() / 2; i++) {  
temp = word_as_char[i];  
word_as_char[i] = word_as_char[word.length() - 1 - i];  
word_as_char[word.length() - 1 - i] = temp;  
}  
String result = word_as_char.toString();  
return result;  
}  
}  
```  

## `@BeforeEach`, `@AfterEach`, `@BeforeAll`  

- `@BeforeEach`  
- annotation is used to signal that the annotated method should be executed before each invocation.  
- `@AfterEach`  
- is used to signal that the annotated method should be executed after each `@Test`.  
- `@BeforeAll`  
- runs once before any of the test methods in the class  

---
tags:
- "Type/Note"
- "Topic/Data_Structures"
- "Class/DSC_30"
date:
- 2024-04-19
---
Source: https://docs.google.com/presentation/d/1npWOehaHb9Gke5pjywR0unLIJM9XfWr5/edit#slide=id.p1  

# Linked Lists  

### Motivation  

- Suppose I have an *array* with 5 elements: 1, 3, 5, 7, 9  
- I want to insert -1 before 1. What should I do?  
- Create a new bigger array  
- Shift previous elements to the right  
- Insert -1 before 1  
- Change reference from old array to new one  

### Disadvantage of using arrays  

- arrays are static structures  
- cannot be easily extended or reduced to fit the data set  
- Once you created an array, it can’t be changed anymore.  
- You have to create a new one each time  
- Arrays are also expensive to maintain new insertions and deletions  

### Linked Lists  

- A linked list is a linear data structure where each element is a separate object.  
- A linked list is a dynamic data structure.  
- The number of nodes in a list is not fixed and can grow and shrink on demand.  
- Any application which has to deal with an unknown number of objects will need to use a linked list.  

### Disadvantage of Linked Lists  

- One disadvantage of a linked list against an array is that it does not allow direct access to the individual elements:  
- If you want to access a particular item then you have to start at the head and follow the references until you get to that item.  
- Another disadvantage is that a linked list uses more memory compare with an array - we extra 4 bytes (on 32-bit CPU) to store a reference to the next node.  

### Operations for Linked List  

- Append element to the list (end)  
- Get an element at index  
- Find an element  
- Insert at index  
- Delete at index  
- Prepend  
- Size  
- Sort  
- Empty the list  

### References inside objects  

- It is also (sometimes) useful for an object to contain a reference to another object of the same class.  
- In this way, we can “chain” together multiple objects.  

### Nodes and Lists  

- A different way of implementing a List  interface  
- There is another class called ArrayList that implements the same interface using arrays.  
- https://docs.oracle.com/javase/8/docs/api/java/util/List.html  
- Each element of a Linked List is a separate Node object.  
- Each node tracks a single piece of data plus a reference (pointer) to the next node.  
- Create a new Node every time we add something to the List  
- Remove nodes when item is removed from list and allow garbage collector to reclaim that memory  

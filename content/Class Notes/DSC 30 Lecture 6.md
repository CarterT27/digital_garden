---
tags:
- "Type/Note"
- "Topic/Data_Structures"
- "Class/DSC_30"
date:
- 2024-04-12
---
Source: https://docs.google.com/presentation/d/1o_j1QNnS0OQJS0qno36tTtvAmS9G2x8Z/edit#slide=id.p1  

# Queues  

## The Queue ADT  

The **Queue** is a collection of objects inserted and removed according to the First in First Out principle.  

## Queue Operations  

**Enqueue (insert)** and **Dequeue (remove)** are the two main operations  

## Implementation. Arrays O(1)  

**Main update methods:**  

- `Enqueue(e)`  
- `Dequeue()`  

**Additional useful methods**  

- `Peek()`: same as dequeue, but does not remove the element  
- `Empty()`: Boolean, True when the queue is empty  
- `Size()`: Returns the size of the queue  

## Regular Array  

- Neither of those solutions are very good as they both involve moving all the existing data elements, which has high time cost  
- Idea: Instead of moving data elements to a **fixed** position for front when removing, let front advance through the array  

## Making a linear array appear circular  

## Design Decisions: Where do front and rear point?  

### Queues using circular arrays  

---
tags:
- "Type/Note"
- "Topic/Data_Structures"
- "Class/DSC_30"
date:
- 2024-04-22
---
Source: https://docs.google.com/presentation/d/1npWOehaHb9Gke5pjywR0unLIJM9XfWr5/edit#slide=id.p47  

### Lists with sentinel (dummy) node  

- Dummy nodes are Nodes whose data fields are always null – they contain no data from the “user”.  
- The dummy nodes will always exist, even if the user hasn’t added any data yet.  
- Head will never points to null  
- These nodes will simplify the implementation for certain methods.  
- No need to check if the list is empty.  

### Generic Types  

Allow us to have `null` as a data value.  
`int` vs. `Integer`  

- Generic types must be reference types. You cannot replace a generic type with a primitive type such as int or char.  
- For example, the following statement is wrong:  
- `ArrayList<int> intList = new ArrayList<int>();`  
- To create an ArrayList object for int values, you have to use:  
- `ArrayList<Integer> intList = new ArrayList<Integer>();`  
- You can add an int value to intList by creating a new object of type Integer. For example,  
- `intList.add(new Integer(5));`  
- Another way: You can add an int value to intList. For example,  
- `intList.add(5);`  
- Java automatically wraps 5 into new Integer(5). This is called autoboxing  

### Diamond Operator `<>`  

- Before JDK 7: Explicitly specifying generic class's instantiation parameter type.  
- `ArrayList<String> list = new ArrayList<String>();`  
- After JDK 7:  
- `ArrayList<String> list = new ArrayList<>();`  


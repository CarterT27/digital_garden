---
tags:
- "Type/Note"
- "Topic/Data_Structures"
- "Class/DSC_30"
date:
- 2024-05-01
---

Source: https://docs.google.com/presentation/d/1k7foXPFkhLLuarSAZdc-bpaA1roJc8UM/edit

|            | Interface                               | Abstract Class                          |
| ---------- | --------------------------------------- | --------------------------------------- |
| Same       | Cannot be instantiated                  | Cannot be instantiated                  |
| Same       | Blueprint                               | Blueprint                               |
| Difference | No objects, no constructor              | No objects, Yes constructor             |
| Difference | `implements`                            | `extends`                               |
| Difference | Abstract methods only                   | Abstract and non-abstract methods       |
| Difference | Class can implement multiple interfaces | Subclass only extend one abstract class |

## Selection Sort

- Breaks the array into two parts: sorted and unsorted.  Finds the next best element from the unsorted section and puts it at the end of the sorted section.
- 1, 2, 3, 7, 4, 9
- Here, 1, 2, 3 have been sorted already, so the algorithm will look through 7, 4, 9,find that 4 is the next best choice, and swap 7 and 4 to put the first 4 elements in the proper order.
- Best case: O(n^2)  Worst case: O(n^2)  Average case: O(n^2)
- Space complexity
	- In place
- Worst case scenario
	- Selection sort performs the same on every kind of list

## Insertion Sort

- Best case: O(n)  Worst case: O(n^2)  Average case: O(n^2)
- Space complexity
	- In place
- Best case scenario: input list is in increasing order
- Worst case scenario: input list is in decreasing order
- It’s often used as the final stage of more sophisticated sorts, such as quicksort.
- Works the best if the data is sorted or partly sorted.

## Merge Sort

- Splits the array in half, splits that half in half, and so on, until each element is on its own, then merges all the singular elements back together so one and one become two, two and two become four, and so on.
- Best Case: O(nlogn).  Worst Case: O(nlogn).  Average Case: O(nlogn).
- Space complexity    
- O(n)

## Quick Sort

- Picks a partition point and reorders elements so that values smaller than the pivot are to the left, and values larger are to the right.  Pick new partitions for the left and right sides to sort further and further until a sorted array is generated.
- Best Case: O(n logn) Worst case: O(n^2)  Average case: O(nlogn)
- Space complexity
	- O(log n)
- Best/worse case scenario: pick a good pivot!

|                | Best Case Runtime   | Average Runtime     | Worst Case Runtime  | Additional Space | Stability |
| -------------- | ------------------- | ------------------- | ------------------- | ---------------- | --------- |
| Selection sort | $\Theta(n^2)$       | $\Theta(n^2)$       | $\Theta(n^2)$       | $\Theta(1)$      | No        |
| Insertion sort | $\Theta(n)$         | $\Theta(n^2)$       | $\Theta(n^2)$       | $\Theta(1)$      | Yes       |
| Merge sort     | $\Theta(n\,log\,n)$ | $\Theta(n\,log\,n)$ | $\Theta(n\,log\,n)$ | $\Theta(n)$      | Yes       |
| Quick sort     | $\Theta(n\,log\,n)$ | $\Theta(n\,log\,n)$ | $\Theta(n^2)$       | $\Theta(log\,n)$ | No        |
| Counting sort  | $\Theta(n+k)$       | $\Theta(n+k)$       | $\Theta(n+k)$       | $\Theta(k)$      | Yes       |
| Check sort     | $\Theta(n)$         | $\Theta(n!)$        | $\Theta(n!)$        | $\Theta(1)$      | No        |



---
tags:
- "Type/Note"
- "Topic/Data_Structures"
- "Class/DSC_30"
date:
- 2024-04-29
---
Source: https://docs.google.com/presentation/d/1k7foXPFkhLLuarSAZdc-bpaA1roJc8UM/edit#slide=id.p1  

# Sorting: Checksort, selection, insertion, merge, quick, compareTo

## Sorting

### Sorting

- Sorting takes an unordered collection and makes it an ordered one.

### Performance Definitions

- Time complexity
- Space complexity
    - the "extra" memory usage of an algorithm

### Check Sort

### Bogosort

Bogosort (aka permutation sort, stupid sort, slowsort, shotgun sort, or monkey sort) is a highly ineffective sorting function based on the generate and test paradigm. The function successively generates permutations of its input until it finds the sorted permutation.

```
while not isInOrder(deck):
    shuffle(deck)
```

---

## Selection Sort

### Common mistake when done by hand (selection)

### Selection Sort. Complexity

**Pseudocode**: `selectionSort(E[] array)`
1. while the size of the unsorted part is greater than 1
2.     find the position of the smallest element in the unsorted part
3.     move (swap) this element into the last position of the sorted part
4.     decrement the size of the unsorted part by 1.

### Costs

| | Best Case Running time | Worst Case Running time | Additional Space |
| --- | --- | --- | --- |
| Selection sort | $\Theta(N^2)$ | $\Theta(N^2)$ | $\Theta(1)$ |

---

## Insertion Sort

### Insertion Sort

General strategy:
- Starting with an empty output sequence.
- Add each item from input, inserting into output at right point.

**Pseudocode**: `insertionSort(primitiveType[] array)`
1. while the size of the unsorted part is greater than 0
2.     let the target element be the first element in the unsorted part
3.     find target's insertion point in the sorted part
4.     insert the target in its final, sorted position

**Pseudocode**: finding the insertion point for the target in the sorted part
1. get a copy of the first element in the unsorted part
2. while (there are elements in the unsorted part to examine AND we haven't found the insertion point for the target)
3.     move the element up a position

- In most cases the insertion sort is the best of the elementary sorts.
- It still executes in $\Theta(N^2)$ time, but it's about twice as fast as the bubble sort and somewhat faster than the selection sort in normal situations.
- It's also not too complex, although it's slightly more involved than the bubble and selection sorts.
- It's often used as the final state of more sophisticated sorts, such as quicksort.
- Works the best if the data is sorted or *partly sorted*.

| | Best Case Running time | Worst Case Running time | Additional Space |
| --- | --- | --- | --- |
| Selection sort | $\Theta(N^2)$ | $\Theta(N^2)$ | $\Theta(1)$ - in place |
| Insertion sort | $\Theta(N)$ | $\Theta(N^2)$ | $\Theta(1)$ - in place |

---

## Merge Sort

### MergeSort

- Split items into 2 roughly even pieces.
- Mergesort each half (steps not shown, this is a recursive algorithm)
- Merge the two sorted halves to form the final result.

### Lost in Recursion Land

- Beginners often fail to appreciate that a recursion **must** have a conditional statement or conditional expression that checks for the "bottom-out" condition of the recursion and terminates the recursive descent
- We call the bottom-out condition the "base case" of the recursion

Warning!!
If you fail to do this properly, you end up lost in Recursion Land and will never return!

### Merge Sort: More General

Intuitive explanation:
- Every level does N work
    - Top level does N work.
    - Next level does N/2 + N/2 = N.
    - One more level down: N/4 + N/4 + N/4 + N/4 = N.
- Thus work is just Nk, where k is the number of levels.
    - How many levels? Goes until we get to size 1.
    - k = log(N)
- Overall runtime is N log N.

- Split items into 2 roughly even pieces.
- Mergesort each half (steps not shown, this is a recursive algorithm)
- Merge the two sorted halves to form the final result.

Space complexity with aux array: Costs $\Theta(N)$ memory.

Also possible to do in-place merge sort, **but** algorithm is very complicated, and runtime performance suffers by a significant constant factor.

### Costs

| | Best Case Running time | Worst Case Running time | Additional Space |
| --- | --- | --- | --- |
| Selection sort | $\Theta(N^2)$ | $\Theta(N^2)$ | $\Theta(1)$ - in place |
| Insertion sort | $\Theta(N)$ | $\Theta(N^2)$ | $\Theta(1)$ - in place |
| Merge sort | $\Theta(N log N)$ | $\Theta(N log N)$ | $\Theta(N)$ - not in place |

---

## Quick Sort

### The Core Idea: Partitioning

To partition an array a[] on element x=a[i] is to rearrange a[] so that:
- x moves to position j (may be the same as i)
- All entries to the left of x are <= x.
- All entries to the right of x are >= x.



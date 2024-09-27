---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/DSC_40B"
date:
- 2024-09-26
---

Source: https://dsc40b.com/materials/lectures/01-intro/slides.pdf

Course Website: [dsc40b.com](https://dsc40b.com/)
Course Notes: https://dsc40b.com/materials/default/notes/book.pdf

How to compute the median in Python?

```python
nums.sort() # O(n log n)

middle_idx = len(nums) // 2
if len(nums) % 2 == 1:
    return nums[middle_idx]
return (nums[middle_idx] + nums[middle_idx+1]) / 2
```

Not the optimal solution.

40B is about creating the algorithms for the math we learned in 40A.

Clustering is assigning datapoints to groups

Naive Approach: Brute force ($2^n$ iterations of checking the separation)

Measuring Time Complexity
Approach 1: Stopwatch
Approach 2: Time Complexity Analysis

Peter Norvig's Essay https://norvig.com/21-days.html

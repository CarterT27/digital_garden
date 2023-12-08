---
tags:
  - "#Type/Definition"
  - "#Topic/Data_Science"
  - "#Class/DSC_10"
---

> [!definition] Simulation
> The production of a computer model of something, especially for the purpose of study.

Simulations are used to estimate probabilities.

---

To perform a random experiment on the computer, we use `np.random.choice(options)`.  
The input, `options`, is a list or array to choose from.  
The output is a random element in `options`. By default, all elements are equally likely to be chosen.  

```python
# Simulate a fair coin flip.
np.random.choice(['Heads', 'Tails']) # 'Tails'

# Simulate a roll of a die.
np.random.choice(np.arange(1, 7)) # '6'

# Simulate 10 fair coin flips.
np.random.choice(['Heads', 'Tails'], 10)
# array(['Tails', 'Tails', 'Heads', 'Tails', 'Tails', 'Heads', 'Tails',
# 'Tails', 'Tails', 'Tails'], dtype='<U5')
```

By default, `np.random.choice` selects **with** replacement.  
```python
# Choose three colleges to win free HDH swag.
colleges = ['Revelle', 'John Muir', 'Thurgood Marshall', 
            'Earl Warren', 'Eleanor Roosevelt', 'Sixth', 'Seventh', 'Eighth']

np.random.choice(colleges, 3, replace=False)
# array(['Sixth', 'Eighth', 'Seventh'], dtype='<U17')
np.random.choice(colleges, 3)
# array(['Sixth', 'Sixth', 'Seventh'], dtype='<U17')
```

---

> [!example] What is the probability of getting 60 or more heads if we flip 100 coins?
> **Plan:**
> 1. Figure out how to run the [[Experiment|experiment]] (flipping 100 coins) once.  
> 2. Repeat the experiment many times.  
> 3. Find the proportion of experiments in which the number of heads was 60 or more.  
> ```python
> # Step One
> def coin_experiment():
> 	coins = np.random.choice(['Heads', 'Tails'], 100)
> 	return np.count_nonzero(coins == 'Heads')
>
> # Step Two
># Specify the number of repetitions.
>repetitions = 10000
>
># Create an empty array to store the results.
>head_counts = np.array([])
>
>for i in np.arange(repetitions):
>    # For each repetition, run the experiment and add the result to head_counts.
>    head_count = coin_experiment()
>    head_counts = np.append(head_counts, head_count
>
> # Step Three
># In how many experiments was the number of heads >= 60?
>at_least_60 = np.count_nonzero(head_counts >= 60)
>at_least_60 # 298
>at_least_60 / repetitions # 0.0298
> np.mean(head_counts >= 60) # 0.0298
> ```
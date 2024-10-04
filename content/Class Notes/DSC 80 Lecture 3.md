---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/DSC_80"
date:
- 2024-10-03
---

# Aggregating

## Adding and Modifying Columns

Adding a new column to a dataframe using `assign`
```python
dogs = pd.read_csv(Path('data') / 'dogs43.csv', index_col='breed')
dogs.assign(cost_per_year=dogs['lifetime_cost'] / dogs['longevity'])
```

Chain methods together instead of writing long, hard-to-read lines
- Need to wrap expression in parentheses to add newlines before every method call

```python
(dogs
 .assign(cost_per_year=dogs['lifetime_cost'] / dogs['longevity'])
 .sort_values('cost_per_year')
 .iloc[:5]
)
```

Assign with special column names (spaces, special characters)
```python
dogs.assign(**{'cost per year 💵': dogs['lifetime_cost'] / dogs['longevity']})
```

`df.copy()` copies a dataframe in place

`df[] = ` assigns column in place

`df.assign()` assigns a column to a new dataframe

Avoid `inplace=True` - plans to remove in future releases of pandas, not good practice

`df[column].to_numpy()` returns the numpy array of a column

`dogs.max(axis=1)` won't work because you are trying to take the max of a mix of datatypes

## Data Granularity and the `groupby` method

Fine granularity: small details  
Coarse: bigger picture  

You should opt for **finer granularity** for more detail if you have the resources to do so

How to go from fine to coarse granularity: **Aggregating**

> [!definition] Aggregation
> Aggregating is the act of combining many values into a single value

`penguins.groupby('species')['body_mass_g'].mean()`

"Split-apply-combine" Paradigm

[https://dsc80.com/resources/lectures/lec03/imgs/image_0.png]()

```python
(penguins
 .assign(is_dream = penguins['island'] == 'Dream')
 .groupby('species')
 ['is_dream']
 .mean()
)
```

```python
%%pt
penguins_small.groupby('species')
```

Allows us to visualize groupby_objects

Aggregation Methods
- `count()`
- `sum()`
- `mean()`
- `max()`
- `last()`
- `first()`

```python
(penguins
 .sort_values('body_mass_g')
 .groupby('sex')
 .last()
)
```

Generally, you should select column(s) directly after groupby

## Beyond default aggregation methods

```python
(penguins
 .groupby('species')
 ['body_mass_g']
 .aggregate(['count', 'mean'])
)
```

```python
(penguins
 .groupby('species')
 .aggregate({'bill_length_mm': 'max', 'island': 'unique'})
)
```

```python
def iqr(s):
    return np.percntile(s, 75) - np.percentile(s, 25)

(penguins
 .groupby('species')
 ['body_mass_g']
 .agg(iqr) # agg is short for .aggregate
)
```

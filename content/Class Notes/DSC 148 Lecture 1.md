---
tags:
- "Type/Note"
- "Topic/Data_Mining"
- "Class/DSC_148"
date:
- 2025-01-07
---

# Data Type - Tabular

- Feature Table
    - One of the most popular data types
- Features (attributes, dimensions, variables)
    - A data field, representing a characteristic

# Feature Types

- Nominal: categories, states, or "names of things"
- Binary: Nominal attribute with only 2 states (0 and 1)
    - Symmetric binary: both outcomes equally important
    - Asymmetric binary: outcomes not equally important
- Ordinal: values have a meaningful order (ranking) but magnitude between successive values is not known
- Numeric: quantitative (integer or real-valued)
    - Interval-scaled
        - Measured on a scale of equal-sized units
        - Values have order
            - No true zero-point
    - Ratio-scaled
        - Inherent zero-point
        - We can speak of values as being an order of magnitude larger than the unit of measurement

| | Categorical | | Quantitative | | |
| --- | --- | --- | --- | --- |
| Level | Nominal | Ordinal | Interval | Ratio |
| Defining Features | Distinct Categories | Ordered Categories | Meaningful Distances | Absolute Zero |
| Operations | $= \neq$ | <> | +- | $\times\div$ |

# Discrete vs. Continuous

- Discrete: has only a finite or countably infinite set of values
- Continuous: has real numbers as attribute values

# Other datatypes

- Relational data
- Transactional records
- Text data
- Networks/Graphs, aka information networks
- Sequential data
- Spatial/Image data

# Important Characteristics of Structured Data

- Dimensionality (Curse of Dimensionality)
- Sparsity (Only presence counts)
- Resolution (Patterns depend on the scale)
- Distribution (Centrality and dispersion)

# Mean, Median, and Mode

- Mean (sample vs. population)
- Weighted arithmetic mean
- Trimmed mean
- Median
- Estimated by interpolation (for grouped data)
- Mode
- Unimodal
- Multi-modal

# Symmetric vs. Skewed Data

- Positively skewed: mean > median > mode
- Symmetric
- Negatively Skewed: mean < median < mode

# Properties of Normal Distribution

- Z-score: $z=\frac{x-\mu}{\sigma}$

# Variance and Standard Deviation

- Variance
    - Can be computed incrementally by keeping track of sum and sum of squares
- Standard deviation: s (or $\sigma$) is the square root of variance $s^2$ (or $\sigma^2$)

# Quantiles of Outliers

- Quartiles: Q1 (25th percentile) and Q3 (75th percentile)
- Inter-quartile range: IQR = Q3 - Q1
- Five number summary: min, Q1, median, Q3, max
- Boxplot: data is represented with a box
- Outliers: points beyond a specified outlier threshold, plotted individually, usually higher than 1.5 \* IQR

# Histogram

- Histogram: graph display of tabulated frequencies, shown as bars

# Scatter Plot and Correlations

- Provides a first look at bivariate data to see clusters of points, outliers, etc.
- Each pair is treated as coordinates and plotted on a plane

# Supervised vs. Unsupervised

- Supervised tasks have one or more target variables
    - Learning with **labels** and **data**
    - Goal: predict some value
    - e.g. classification, regression, ranking
- Unsupervised tasks are more like data analysis
    - Learning with **data only**
    - Goal: find some underlying patterns/groupings
    - e.g. clustering, frequent patterns, dimension reduction, ...

# Classification vs. Regression

- Classification and Regression are **both supervised** tasks
- The target variables in **classification** are **discrete**
- The target variables in **regression** are **continuous**

# Classification vs. Clustering

- Classes have their order, while Clusters are exchangeable

# Cross Validation - k folds

- Partition data into 5 subsets (randomly) and evaluate based on each mini-validation set

# Train/Dev/Test

- Can sometimes be too expensive to have k fold cross validation (i.e. LLMS)

# Time Series Splitting

- Time series split vs. Blocking time series split

# TP, TN, FP, FN

- True Positive
- True Negative
- False Positive
- False Negative
- Confusion Matrix: Actual values vs. Predicted values

# Accuracy, Precision, Recall, F1, ...

- Accuracy: (TP+TN)/(TP+FP+FN+TN)
- Precision: TP/(TP+FP)
- Recall: TP/(TP+FN)
- F1: Harmonic Mean between Prec and Rec
    - 2 \* Prec \* Rec / (Prec + Rec)

# Minkowski distance (L norm)

- A popular distance measure, where we have l-dimensional objects and p order
- Properties
    - d(i, j) > 0 if i $\neq$ j, and d(i, i) = 0 (positivity)
    - Symmetry
    - Triangle Inequality
- A distance that satisfies these properties is a **metric**

# MAE, MSE, RMSE

# Ranking Measurements

- Precision-Recall Curve
- AUC
- MAP
- nDCG
- MRR

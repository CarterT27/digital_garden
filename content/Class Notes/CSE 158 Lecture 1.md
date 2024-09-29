---
tags:
- "Type/Note"
- "Topic/Data_Mining"
- "Class/CSE_158"
date:
- 2024-09-28
---

Recommender Systems
- Prediction: What rating will someone give to a particular product?
- Application: Build system to recommend products that people are interested in
- Insights: How are opinions influenced by factors like time, gender, age, and location?

Social Networks
- Prediction: Whether two users of a social network are likely to be friends
- Application: "People you may know" and friend recommendation systems
- Insights: What are the features around which friendships form?

Advertising
- Prediction: Will I click on an advertisement?
- Application: Recommend relevant ads to maximize revenue
- Insights: What products tend to be purchased together, what do people purchase at different times of the year?

Medical Informatics
- Prediction: What symptom will a person exhibit on their next visit to the doctor?
- Application: Recommend preventative treatment
- Insights: How do diseases progress, and how do different people progress through these stages?

## What we need to do data mining

1. Are the data associated with meaningful outcomes?
    - Are the data **labeled**?
    - Are the instances (relatively) independent?
2. Is there a clear objective to be optimized?
    - How will we **know** if we've modeled the data well?
    - Can actions be taken based on our findings?
3. Is there enough data?
    - Are our results statistically significant?
    - Can features be collected?
    - Are the features useful/relevant/predictive?

## What is covered in this course?

This course aims to teach
- How to **model** data in order to make **predictions** like those above
- How to **test and validate** those predictions to ensure that they are meaningful
- How to **reason about** the findings of our models

i.e., data mining

But, with a focus on applications from **recommender systems and the web**
- **Web** datasets
- Predictive tasks concerned with human **activities, behavior, and opinions**

i.e., recommender systems

## Expected Knowledge (What won't be taught)

**Basic** data processing
- Text manipulation: count instances of a word in a string, remove punctuation, etc.
- Graph analysis: represent a graph as an adjacency matrix, edge list, node-adjacency list, etc.
- Process formatted data, e.g. JSON, html, csv files, etc.

**Basic** mathematics
- Some linear algebra, e.g. $Ax = y \rightarrow x = (A^T A)^{-1} A^T y$
- Some optimization
- Some statistics (standard errors, normal/binomial distributions)

All coding exercises will be done in **Python** with the help of some libraries (numpy, scipy, NLTK, etc.)

Idea with "expected knowledge" is not that you know all of these things, but rather you learn those that you don't **on your own**

The most related classes are:
- CSE 150/151
- CSE 250A
- CSE 250B

Last year's links: [CSE 158](https://cseweb.ucsd.edu/classes/fa23/cse258-a)

[Course Webpage](https://cseweb.ucsd.edu/classes/fa24/cse258-b)

## Course Outline

1. Fundamentals
    - Regression
    - Classification
    - Recommender Systems
2. More advanced
    - Content and Structure in Recommendation
    - Temporal Data Mining and Recommendation
    - Text mining
    - (A little bit of visual recommendation)
    - Ethics of Personalized Recommendation

Regression
- Linear regression and least-squares
- A little bit of feature design
- Overfitting and regularization
- Gradient descent
- Training, validation, and testing
- Model selection

How can we use **features** to make predictions about **real-valued** outcomes?  
How can we prevent our models from **overfitting** by favoring simpler models over more complex ones?

Classification
- Logistic regression
- Multiclass and multilabel classification
- {How to evalutate classifiers, especially in "non-standard" settings

Next we adapted these ideas to **binary** or **multiclass** outputs

Recommender Systems
- Collaborative filtering
- Latent factor models and matrix factorization
- Recommender Systems Evaluation

Content and Structure in Recommender Systems
- Recommendation with complex features
- Recommendation in non-standard settings
- Advertising
- Maybe discuss some tools/libraries

Tools and Libraries
- Crawling and parsing data from the Web
- Plotting data
- Tensorflow

Later: More "specialized" material

Temporal & Sequence Data
- Sliding windows & autoregression
- Temporal dynamics in recommender systems
- Temporal dynamics in text & social networks

Text Mining
- Sentiment analysis
- Bag-of-words representations
- TF-IDF
- Stopwords, stemming
- Personalized text models and natural-language explanations

Personalized Visual Models

Ethics

Personalized Machine Learning - McAuley, Julian

[PML Website (Free)](https://cseweb.ucsd.edu/~jmcauley/pml)

Other references from
– Bishop: Pattewrn Recognition and Machine Learning
- [Charles Elkan's Notes](http://cseweb.ucsd.edu/classes/fa18/cse258-a/files/elkan_dm.pdf)

Python Data Products (Coursera)

New Classes
- Fairness & Interpretability of ML (WI25)
- ML for Music (SP25)

## Supervised Learning - Regression

> [!definition] What is Supervised Learning?
> **Supervised learning** is the process of trying to infer from **labeled data** the underlying function that produced the labels associated with the data

Given **labeled training data** of the form  
$$\{(\text{data}_1,\text{label}_{1},\dots,(\text{data}_{n},\text{label}_{n})\}$$  
Infer the function  
$$f(\text{data})\rightarrow \text{labels}$$

Solution 1: Design a system based on **prior knowledge**  

Disadvantages:
- Depends on possibly false **assumptions** about how users relate to items
- Cannot adapt to new data/information

Advantages:
- Requires no data

Solution 2: Identify words that I frequently mention in my social media posts, and recommend movies whose plot synopses use **similar** types of language  

Disadvantages:
- Depends on possibly false **asumptions** about how users relate to items
- May not be adaptable to new settings

Advantages:
- Requires data, but does not required **labeled** data

Solution 3: Identify which attributes are associated with positive ratings. Recommend movies that exhibit those attributes.

Disadvantages:
- Requires a (possibly large) dataset of movies with labeled ratings

Advantages
- Directly optimizes a measure we care about (prediction ratings)
- Easy to adapt to new settings and data

## Supervised versus unsupervised learning

**Learning** approaches attempt to **model data** in order to solve a problem

**Unsupervised learning** approaches find patterns/relationships/structure in data, but **are not** optimized to solve a particular predictive task

**Supervised learning** aims to directly model the relationship between input and output variables, so that the output variables can be predicted accurately given the input
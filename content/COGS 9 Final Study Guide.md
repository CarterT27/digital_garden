---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/COGS_9"
date:
- 2024-03-17
---
# Winter 2024 Final Exam Study Guide  

## What is Data Science?  
What are the arguments for and against Data Science existing as a discipline?  
What is Data Science?  
What do data scientists do?  
- [[COGS 9 Lecture 1]]  
- [[50 Years of Data Science]]  

## Ethics & Privacy  
What question was the Facebook Study trying to answer?  
What were the ethical arguments for/against the Facebook Study?  
What is The Belmont Report?  
What is the Common Rule?  
What is Informed Consent?  
What ethical considerations should be made for each data science project?  
- [[COGS 9 Lecture 2]]  
- [[COGS 9 Lecture 3]]  

## Data Science & Reproducibility  
What is the scientific method?  
How does the scientific process fit into data science?  
What makes a project reproducible?  
What makes a project replicable?  
What is the replicability crisis?  
What is the unicorn test?  
What is cognitive bias?  
Why did we discuss the example about Amy Cuddy?  
- [[COGS 9 Lecture 4]]  

## Version Control & File Management  
Why use version control?  
What tools are used for version control?  
What problem does version control help solve?  
Why do we care about file structure?  
What considerations should we make when naming individual files?  
What are some of the main commands in git (clone, push, pull, commit) and when are they used?  
- [[COGS 9 Lecture 9]]  
- [[COGS 9 Lecture 10]]  

## Programming  
Why Learn to code?  
What languages are most common in data science? Why?  
Who uses the most common programming languages?  
What differs between how software engineers and data scientists use code?  
What is end-user programming? (Note: this is the type of programming data scientists tend to do)  
- [[COGS 9 Lecture 9]]  

## Data & Data Types  
What counts as data?  
How do we categorize data?  
What file formats are common for each data structure category?  
What are the characteristics of each type of data structure?  
How are tables handled and merged in relational data?  
- [[COGS 9 Lecture 5]]  
- [[COGS 9 Lecture 6]]  

## Getting Data  
Where does one find data to use for data science projects?  
If data are not already in usable format, what options do you have?  
How does an API work generally?  
When would someone use web scraping?  
What are the ethics of acquiring data?  
- [[COGS 9 Lecture 7]]  

## Data Wrangling  
What are the principles of tidy data?  
What are typical steps taken during data wrangling?  
What are some common pitfalls of data in spreadsheets?  
What does each of the common wrangling verbs accomplish?  
- [[COGS 9 Lecture 8]]  


## Data Visualization  
Which graphs are appropriate for various types of data (i.e. when would you make a histogram? A scatterplot? etc.)  
What are important things to keep in mind when generating visualizations (including graphs and tables)?  
When interpreting visualizations, what do you do? (think: look for general pattern and things that are outliers/weird/odd)  
What colors are good to use? Which colors and color combinations to avoid?  
What’s the difference between an exploratory and an explanatory visualization?  
What is the “data to ink ratio” and how does changing that ratio aid in understanding data visualization?  
What does it mean to iteratively improve a visualization?  
What makes a good exploratory visualization? What takes a visualization from exploratory to explanatory?  
What differs between visualizations on paper and those presented using slides?  
What does visualization have to do with storytelling and/or effective communication?  
- [[COGS 9 Lecture 11]]  
- [[COGS 9 Lecture 12]]  

## Descriptive Analysis  
What is a descriptive analysis?  
What are the best practices for sampling from a population?  
How do we describe a dataset? What measurements do we use? (size, missingness, shape, central tendency, variability)  
What are the differences between the mean and the median? In what situations would you favor one over the other?  
- [[COGS 9 Lecture 12]]  
- [[COGS 9 Lecture 13]]  

## Exploratory Data Analysis (EDA)  
What is EDA? Why do EDA?  
What does it mean that EDA is an iterative process?  
What are the general steps in an exploratory analysis?  
What types of plots are helpful during EDA?  
When is EDA helpful? When is it not the right approach?  
- [[COGS 9 Lecture 12]]  
- [[COGS 9 Lecture 13]]  

## Inference  
What is inferential analysis? What types of questions are appropriate for inference?  
What does sampling have to do with inference?  
What is Anscombe’s Quartet? What is interesting about Anscombe’s quartet? Note here that these four sets of X,Y pairs have very similar, if not identical, summary statistics: means and variances for both X and Y, the X,Y correlation, as well as the equation for the regression line. Yet they are clearly very different upon cursory visual inspection.  
Why is setting a p-value—the probability of observing a result assuming that the null hypothesis is true—at an arbitrary threshold such as 0.05 (1-in-20) problematic? If you run 20 (independent) tests, you’re likely to get one that results in a “significant” effect!  
What does correlation demonstrate? What does it mean when people say correlation does not equal causation?  
What does a comparison of means demonstrate? What statistical test could you use for this? What assumptions must be met for this statistical test?  
What is regression? What are the assumptions of linear regression?  
What are confounders?  
- [[COGS 9 Lecture 17]]  
- [[COGS 9 Lecture 18]]  

## Machine Learning  
What is Machine Learning (ML)?  
What are the four basic steps to prediction? What does each of them mean?  
What are the differences between supervised and unsupervised learning?  
What are the differences between regression and classification?  
What are decision trees? When would you use them?  
What does it mean to assess machine learning models?  
What metrics would you use to assess classification models?  
What metrics would you use to assess regression models?  
How are deep learning and machine learning related?  
How are machine learning and data science related?  
What is overfitting?  
What is underfitting?  
What are neural networks?  
- [[COGS 9 Lecture 18]]  
- [[COGS 9 Lecture 19]]  
- [[COGS 9 Lecture 20]]  
- [[COGS 9 Lecture 21]]  

## Geospatial Analysis  
What are map projections? What criteria might be used while creating a map projection?  
What is wrong with plotting raw count histogram-type distributions of many real-world geospatial features, such as population, economic activity, number of website users, etc.?  
How can plotting certain features, such as disease prevalence rates by geographic region, help scientists form new hypotheses about disease causes (or cures)?  
What is a choropleth map?  
Why do we need cartograms?  
What are isarithmic maps?  
In what ways do spatial data violate conventional statistics?  
What is spatial autocorrelation, and in what way are many real-world geospatial features highly spatially autocorrelated?  
The modifiable areal unit problem (MAUP) is important for things such as Gerrymandering: how we divide features across space influences aggregate statistics within those subdivisions! Be sure you understand this.  
What is the ecological fallacy?  
What does nonuniformity in space mean and how does that complicate the analysis of geospatial data?  
- [[COGS 9 Lecture 22]]  

## Text Analysis  
What is the “TF” in TF-IDF? What is the “IDF”?  
What is a “token”?  
What is sentiment analysis? What is a lexicon?  
What are some limitations of sentiment analysis?  
What are word clouds?  
How can we analyze text in novels?  
What are a few ways you can deal with the issue of context in text data?  
What is the main difference between structured and distributional learning?  
What is the distributional hypothesis?  
What is the main principle behind language models?  
- [[COGS 9 Lecture 24]]  
- [[COGS 9 Lecture 25]]  

## Algorithms & Computability  
What is the definition of an algorithm?  
How can the performance of an algorithm be measured?  
At Stitch Fix, at what points in the process are algorithms used?  
What is meant by “What the average user thinks they are doing is what is actually being done?”  
What does it mean for an algorithm to be FAT?  
- [[COGS 9 Lecture 27]]  

## Data Science Jobs Lecture  
What were the two personas of people who search for data science jobs?  
What positions would you look for if searching for a data science internship/job?  
What are the barriers to entry for someone searching for a data science job?  
Other than an internship, what can undergraduates do to increase their chances of employment?  
- [[COGS 9 Lecture 28]]  

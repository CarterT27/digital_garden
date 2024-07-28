---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/COGS_9"
date:
- 2024-02-23
---
Source: https://drive.google.com/file/d/1kiISfUk70piO42XPdPw_gc858DLeDh3Q/view?usp=sharing  

# Machine Learning  

## First Steps to Supervised Prediction  
1. Data Partitioning  
2. Feature Selection  
3. Model Selection  
4. Testing the Model  

> [!note] Data Partitioning  
> Full Dataset  
> Training and Testing set  
> Training Set, Validation Set, Testing Set  
>  
> Training set is the data used to build your predictive model  
> Testing set is new and independent data set used to assess if prediction model is generalizable  
> Validation set is data from original dataset that was held out and not used in training the model; helpful in fine-tuning prediction accuracy  

> [!definition] Feature Selection  
> **feature selection** determines which variables are most predictive and includes them in the model  
> Note, whatever you do to your training data (removing, transforming, etc.), you will eventually do to your test data as well  
> variables that can be used for accurate prediction exploit the relationship between the variables but do NOT mean that one causes the other.  

> [!note] Model Selection  
> What variable are you trying to predict?  
> - Regression: predicting continuous variables (i.e. Age)  
> - Classification: predicting categorical variables (i.e. education level)  

## Supervised machine learning: Tree-based algorithms  

> [!note] Decision tree  
> A decision tree is just a function that is displayed as a tree  
> Decision trees compromise of the following components:  
> A. Internal nodes: Test one feature of the input (e.g. height)  
> B. Branches: Possible values of the feature being tested  
> C. Leaf nodes: The label of input whose features correspond to the root-to-leaf path  

> [!note] How do we grow decision tree from data?  
> Before considering decision trees, let's consider decision stumps.  
> Stumps are trees where only one splitting is allowed (decision trees of depth 1).  
>  
> What would be the parameters for defining a stump?  
>  
> How do we decide the optimal 'rule' for splitting?  
> A rule consists of 3 things:  
> - Feature  
> - Threshold value for the feature if continuous  
> - Labels at the leaf nodes after splitting  
>  
> First, we have to define a 'score' or 'metric' for evaluating the split:  
> - We want to learn decision stumps by finding the rule with the best 'score'  
> - 'score' defines what is considered 'best'  

> [!note] How do we grow a decision stump from data?  
> The prediction should improve after the split  
> Most intuitive score: "accuracy"  
> - Find the rule that maximizes the number of training examples that are classified correctly  
> - Several issues with accuracy:  
>   - Often, it's difficult to find decision rules that improve accuracy  
>   - Decision stumps divide input space by horizontal/vertical lines  
>       - It could happen that no horizontal or vertical line improves accuracy  
> - In practice, more complex score measures like 'information gain' are used  

> [!note] Summary of Decision Trees  
> Good:  
> - Very interpretable ('Rules')  
> - Very fast (learning and classification)  
> - No data preprocessing  
> Bad:  
> - Have to rely on a greedy strategy - not optimal  
> - Often not very accurate - we can use a simple trick  

> [!note] Training the Model  
> Several examples of a cost function  
>  
> | Measurement | Purpose | Commonly Used Variable Type |  
> | ----------- | ------- | --------------------------- |  
> | RMSE | Root Mean Squared Error: summarize distance b/w prediction and actual value; sensitive to outliers (lower = better) | Continuous |  
> | Accuracy | What % where predicted correctly? (higher = better) | Categorical |  
> | Sensitivity or Recall | Of those that were positives, what % were predicted to be positive? (higher = better) | Categorical |  
> | Specificity | Of those that were negative, what % were predicted to be negative? (higher = better) | Categorical |  
> | Precision of PPV | Of those that should have been positives, what % were predicted to be positive? (higher = better) | Categorical |  
> | F1 Score | Considers Precision and Recall (0 = poor; 1 = best) | Categorical |  
>  
> Type I Error (false positive) vs. Type II Error (false negative)  
>  
> Confusion Matrix  

## Final Steps to Supervised Prediction  

5. Training & Testing Final Model  
6. Deploying Final Model  

---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/COGS_9"
date:
- 2024-03-08
---
Source: https://drive.google.com/file/d/1YmR9Na-so1Y_m3yRA0jNqZbIqvleg3HA/view  

> [!note] Types of Text Analysis  
> Structured (supervised)  
> - Specify features/labels using linguistic theory  
> - Train classifiers using explicit labels to learn text features (i.e. spam classifier, sentiment classifier)  
> Distributional (unsupervised/semi-supervised)  
> - Learn features in an unsupervised way  
> - Know a word by the company it keeps  
> - Learn to predict and cluster language based on these features  

## How does distributional learning work?  

> [!note] What is the last word in each sentence?  
> - Roses are red and violets are **blue**.  
> - I like my coffee with cream and **sugar**.  
> - Can you put cream cheese on my **bagel**?  

> [!note] What does the word *dax* mean in this context?  
> - A new **dax** costs less than you might expect.  
> - You can fit five people in a **dax**.  
> - The **dax** made a right at the junction and got stuck in traffic.  

> [!note] The distributional hypothesis  
> "You shall know a word by the company it keeps." - J.R. Firth (1957)  
> "The meaning of a word is determined by how it is used." - Ludwig Wittgenstein (1953)  

> [!note] Computational models take advantage of these patterns  
> From data like this:  
> - There is a lovely house on that street.  
> - My house is on that road.  
> - I drove my car down the road.  
> - Did you park on the street?  
> - There are some kids playing soccer on the road.  
> Models can learn:  
> - "House" and "street" are more likely to appear in the same sentences.  
> - "House" and "road" appear in the same sentences.  
> - "Street" and "road" follow the words "the" or "that".  
> - "Street" and "road" are similar words.  

> [!note] Early computational models: Latent Semantic Analysis  
> Bag of words  
> Dimensionality reduction  

> [!note] Bag of words drawbacks  
> 1. No representation of word order  
>   - Man bites dog = dog bites man  
> 2. Dependent on document size  

> [!note] Skip-Gram Models: Word2Vec  
> Skip-gram models  
> Train neural networks to predict contexts  
> Vector spaces  
> Word Vectors  

> [!note] Large Language Models  
> Principles  
> - Similar to Word2Vec  
> - Neural network trained to predict the next word  
> - Contextualised representations  
>   - That dog has a loud bark.  
>   - That tree has a brown bark.  
> - Learns to pay attention to the right words.  
> - Much larger (billions of parameters vs. thousands for Word2Vec)  
> - Bigger is better  
> - Few-shot learning vs. training on many examples  

> [!note] Using LLMs to do Data Science  
> - Writing code  
> - Critiquing code  
> - Learning about new paradigms  
> - Writing documentation  
> - Cleaning messy data  
> - Generating data  
> - The future (automating your own job?)  

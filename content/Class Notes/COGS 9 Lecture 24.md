---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/COGS_9"
date:
- 2024-03-06
---
Source: https://drive.google.com/file/d/10O8pMwSy9209mP4a9pCctCYIVXa8oGpL/view?usp=sharing  

# Text Analysis  

> [!definition] Text Analysis  
> To determine structure, insight, and relationship within and between textual data, e.g. articles, tweets, books, music, web page content, code, etc.  

> [!note] Approaches To: Text Analysis  
> 1. Sentiment Analysis  
> 2. TF-IDF  
> 3. Visualizations - Word Clouds & Networks  
> 4. + Much more!  

> [!definition] Sentiment Analysis  
> Programatically infer emotional content of text  

> [!definition] Sentiment Lexicon  
> Dataset containing words classified by their sentiment  

## When doing sentiment analysis...  

> [!definition] Token  
> A meaningful unit of text  
> - what you use for analysis  
> - *tokenization* takes corpus of text and splits it into tokens (words, bigrams, etc.)  

> [!definition] Stop words  
> Words not helpful for analysis  
> - extremely common words such as "the", "of", "to"  
> - are typically removed from analysis  

## TF-IDF  

> [!definiiton] Term Frequency - Inverse Document Frequency (TF-IDF)  
> TF-IDF is a measure of originality of a word in a document obtained by comparing the number of times a word appears in a document with the number of documents the word appears in  
> $$w_{x,y}=tf_{x,y}\times log\left(\frac{N}{df_x}\right)$$  
> Term $x$ within document $y$  
> $tf_{x,y}$: frequency of $x$ in $y$  
> $df_x$: number of documents containing $x$  
> $N$: total number of documents  

Word clouds display the words proportional to their frequency within the textual dataset  

What if you don't want to remove words from their context?  

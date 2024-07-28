---
tags:
- "Type/Definition"
- "Topic/Data_Science"
- "Class/DSC_10"
---
> [!definition] Simple Random Sample (SRS)  
> A **simple random sample** is a [[Sample|sample]] drawn **uniformly** at random **without replacement**.  
> - "Uniformly" means every individual has the same chance of being selected.  
> - "Without replacement" means we won't pick the same individual more than once.  

To perform an SRS from a [[List]] or [[Array]] `options`, we use `np.random.choice(options, n, replace=False)`.  
```python  
staff = ['Oren Ciolli', 'Nate Del Rosario', 'Jack Determan', 'Sophia Fang', 'Charlie Gillet',  
'Ashley Ho', 'Henry Ho', 'Vanessa Hu', 'Leena Kang', 'Norah Kerendian', 'Anthony Li', 'Weiyue Li',  
'Jasmine Lo', 'Arjun Malleswaran', 'Mert Ozer', 'Baby Panda', 'Arya Rahnama', 'Aaron Rasin', 'Chandiner Rishi', 'Gina Roberg',  
'Harshi Saha', 'Keenan Serrao', 'Abel Seyoum', 'Suhani Sharma', 'Yutian Shi', 'Ester Tsai',  
'Bill Wang', 'Ylesia Wu', 'Jason Xu', 'Diego Zavalza', 'Ciro Zhang']  

# Simple random sample of 4 course staff members.  
np.random.choice(staff, 4, replace=False)  
# array(['Yutian Shi', 'Oren Ciolli', 'Ylesia Wu', 'Sophia Fang'],  
# dtype='<U17')  
```  
If we use `replace=True`, then we're sampling uniformly at random with replacement – there's no simpler term for this.  

---  

If we want to sample rows from a DataFrame, we can use the `.sample` method on a DataFrame. That is,  

```python  
df.sample(n)  
```  

returns a random subset of `n` rows of `df`, drawn **without replacement** (i.e. the default is `replace=False`, unlike `np.random.choice`).  

---  

**The effect of sample size**  
- The law of large numbers states that when we repeat a chance experiment more and more times, the empirical distribution will look more and more like the true probability distribution.  
- **Similarly, if we take a large simple random sample, then the sample distribution is likely to be a good approximation of the true population distribution.**  
- **In general**, [[Statistic|statistics]] computed on **larger** [[Sample|samples]] tend to be **better** estimates of the [[Population]] [[Parameter|parameters]] than [[Statistic|statistics]] computed on smaller samples.  

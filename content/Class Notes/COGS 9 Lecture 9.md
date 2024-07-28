---
tags:
- Type/Note
- Topic/Data_Science
- Class/COGS_9
date:
- 2024-01-29
---
# Programming  

> [!note] Why Learn to Program? (as a data scientist)  
> - Manually editing data sucks  
> 	- Increased error rate  
> 	- Time consuming  
> - Allows the computer to do the work for you  
> 	- Routine tasks  
> 	- Simulations, permutations, etc.  
> - Makes analyses reproducible  
> 	- Particularly important as things increase in complexity  
> - It teaches persistence  
> - It can improve your life  
> 	- Data aren't going anywhere  

> [!note] Programming Workflow  
> Think-Try-Read-Refactor  
> 1. Think about what it is you want to do  
> 2. Try it out  
> 	1. If you succeed, awesome  
> 	2. If not, continue on  
> 3. Read to try to figure out the answer  
> 4. Refactor your code to improve and learn  

> [!note] Why are R and Python the languages data scientists use?  
> Easy to learn: clear, simple syntax and structure  
> Rapid development & prototyping: get more done with less, and in less time  
> Huge support: cross-platform compatible (OS X, Windows, Linux/Unix). Tons of libraries for analytics, visualization, machine learning, data wrangling...  

> [!note] Python vs. R  
> R  
> - Statistical programming language  
> 	- 1st functional programming  
> 	- 2nd object oriented  
> - Most commonly used  
> 	- Data wrangling  
> 		- tidyverse  
> 	- Data visualization  
> 		- ggplot2  
> 	- Statistical analysis  
> 	- Machine learning  
> 		- caret/tidymodels  
> 	- By people with a statistical background  
> Python  
> - General programming language  
> 	- 1st object oriented  
> 	- 2nd functional programming  
> - Most commonly used  
> 	- Data Wrangling  
> 		- Pandas  
> 		- NumPy  
> 	- Machine Learning  
> 		- Scikit-learn  
> 		- TensorFlow, PyTorch  
> 	- Deploying models in production  
> 	- By people with CS background  

> [!note] Data Science is constantly changing  
> This makes data science fun and challenging.  
> Start somewhere: Either Python or R are good places to start  
> Technology changes: You'll learn more than one language in your career  
> Good data scientists adapt quickly  

## CS programming vs. DS programming  

> [!note] Computer Science  
> **Computer science** is the study of the theory and practice of how computers work.  
> Typical job duties:  
> - Testing, documenting, and debugging code  
> - Creating or modifying software and mobile apps  
> - Designing components of an application and integrating them into a larger overall product  
> - Collaborating with a team of programmers to build and optimize code  

> [!note] Data Science  
> **Data science** is the scientific process of extracting value from data.  
> Typical job duties:  
> - Collecting, "cleaning", and organizing data sets  
> - Building data models  
> - Asking and answering questions with large scale data analysis  
> - Creating data visualizations and presenting findings to stakeholders  
> Data is the emphasis: programming skills should focus on **working with data**  

> [!note] Data Scientists  
> - excel at getting the data they need (SQL)  
> - explore & clean the data (R, Python)  
> - are very comfortable working with tabular data (R, Python)  
> - prioritize reproducibility  
> - program to accomplish a task/answer a question  

> [!definition] Version Control  
> How to work collaboratively and track your code-centric projects  
> - Enables multiple people to simultaneously work on a single project  
> - Each person edits their own copy of the files and chooses when to share those changes with the rest of the team  
> - Thus, temporary or partial edits by one person do not interfere with another person's work  

> [!note] What is version control?  
> A way to manage the evolution of a set of files  
> When using a version control system, you have one copy of each file and the version control system tracks the changes that have occurred over time  

> [!note] git & GitHub  
> git: the version control system  
> GitHub is the home where your git-based projects live on the Internet  

> [!note] Why version control with git and GitHub?  
> - Collaboration  
> 	- Each person is making changes locally (on their computer)  
> - Returning to a safe state  
> 	- You're free and safe to try things out locally. You'll only send changes to the repo when you're at a stable point  
> - Exposure for your work  
> 	- Your public GitHub repos are your coding social media  
> - Tracking others' work  
> 	- As a social platform, you can see others' work too  

> [!note] GitHub  
> A remote host, which stores files geographically distant from any files on your computer.  

> [!note] GitHub repo  
> Contains all the files and folders for your project.  

> [!note] Clone  
> The action of getting the files and folders from a remote repository onto your laptop for the first time.  

> [!note] Staging  
> The process of telling git which files you want to keep track of using `add`.  
> `git add file`: stages specified file (or folder)  
> `git add .`: stages **new and modified** files  
> `git add -u`: stages **modified and deleted** files  
> `git add -A`: stages **new, modified, and deleted** files  
> `git add *.csv`: stages any files with .csv extension  
> `git add *`: stages everything  

> [!note] Commit  
> A snapshot or your files at a certain point, which tracks who, what, and when.  
> You can make commits more informative by adding a **commit message**: `git commit -m "changed colors for animal icons"`  

> [!note] Push  
> The action of uploading changes back to the remote for others to access.  

> [!note] Pull  
> The action of downloading changes from the remote (GitHub).  

## Definition Recap  

> [!definition] repo  
> set of files and folders for a project  

> [!definition] remote  
> where the repo lives  

> [!definition] clone  
> get the repo from the remote for the first time  

> [!definition] add  
> specify which files you want to stage (add to repo)  

> [!definition] commit  
> snapshot of your files at a point in time  

> [!definition] pull  
> get new commits to the repo from the remote  

> [!definition] push  
> send your new commits to the remote  

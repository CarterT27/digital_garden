---  
tags:  
- Type/Note  
- Topic/Data_Science  
- Class/COGS_9  
date:  
- 2024-01-26  
---  
  
Source: https://drive.google.com/file/d/1efATrW7wpnBsTycfj29xohyOkkR0VFD1/view  
  
# Data Wrangling  
  
> [!definition] Data Science  
> The scientific process of extracting value from data  
  
## Data Vocabulary/Fluency  
  
> [!definition] Variables/Features  
> Variables are stored in columns on spreadsheets.  
  
> [!definition] Observations  
> Observations are stored in rows on spreadsheets.  
  
> [!note] Tidy Data  
> 1. Each variable you measure should be in a single column.  
> 2. Every observation of a variable should be in a different row.  
> 3. There should be one table for each type of data.  
> 4. If you have multiple tables, they should include a column in each with the same column label that allows them to be joined.  
> Tidy data `==` rectangular data  
  
> [!note] Benefits of Tidy Data  
> 1. Consistent data structure  
> 2. Foster tool development  
> 3. Require only a small set of tools to be learned  
> 4. Allow for datasets to be combined (much like in an RDB!)  
  
## Good Spreadsheets  
  
> [!note] Rules for Tidy Spreadsheets  
> 1. Be consistent  
> 2. Choose good names for things  
> 3. Write dates as YYYY-MM-DD (ISO-8601)  
> 4. No empty cells  
> 5. Put just one thing in a cell  
> 6. Don't use font color or highlighting as data  
> 7. Save the data as plain text files (i.e. CSV)  
  
> [!note] Be consistent  
> - Keep exactly the same variable names across spreadsheets.  
> - Pick a way to code your variables and stick to it.  
  
> [!note] Choose good names for things  
> - Avoid extra spaces  
> - Use underscores not spaces  
> - Choose meaningful names  
  
> [!note] Write dates as YYYY-MM-DD  
> Use 'ISO 8601' standard  
  
> [!note] No empty cells  
  
> [!note] Put just one thing in a cell  
  
> [!note] Don't use font color or highlighting as data  
  
> [!note] Common Problems with Messy Data Sets  
> 1. Column headers are values but should be variable names  
> 2. A single column has multiple variables  
> 3. Variables have been entered in both rows and columns  
> 4. Multiple "types" of data are in the same spreadsheet  
> 5. A single observation is stored across multiple spreadsheets  
  
> [!note] Tidy data is also relevant for unstructured data  
  
> [!note] Common data wrangling tasks (and verbs)  
> - subset dataset  
> 	- filter: filter rows  
> 	- select: select columns  
> - change order  
> 	- arrange: reorder rows  
> 	- reorder: reorder columns  
> - add a column: mutate  
> - summarize data:  
> 	- group by: group by other variables  
> 	- summarize: reduce multiple values down to a single value  

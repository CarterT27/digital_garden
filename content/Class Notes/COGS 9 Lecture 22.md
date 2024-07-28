---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/COGS_9"
date:
- 2024-03-01
---
Source: https://drive.google.com/file/d/1ueNGxlTiVnVweovyJJdLpbFit-ddNY2h/view  

# Geospatial Analysis  

> [!note] Why Geospatial Analysis?  
> "Everything is related to everything else, but near things are more related than distant things." - Tobler 1979  
> "...the purpose of geographic inquiry is to examine relationshiops between geographic features collectively and to use the relationships to describe the real-world phenomena that map features represent" - Clarke 2001  

> [!note] Map Projections  
> Never all 4 at once  
> - True directions  
> - True distances  
> - True areas  
> - True shapes  

> [!note] When looking at a map always ask  
> - What is the purpose for this map and who made it?  
> - What facets of data have been included/excluded?  
> - Where did the data come from? Is there a source?  
> - How has this map been modified and what principles were applied and for what purpose?  

## Visualizing Geospatial Data  

> [!note] Chloropleth maps  
> **Chloropleth** maps are useful for visualizing *clear regional patterns* in the data  
> Use light colors for low values, dark colors for high values  
> Shine when displaying a single variable  
> Excel at displaying the big picture, but not subtle differences  
> Should display relative differences, not absolute numbers  
> Can be misleading - geographic maps can just be population maps  
> Consider using the smallest unit possible  
> Sometimes summarizing at the state level is ok  

> [!note] Cartograms  
> Cartograms should be considered when displaying how many people were affected (vs. area affected in chloropleths)  
> If geographic space and population were correlated, this wouldn't be an issue  
> Tradeoffs should be carefully considered  

| Comparison of Cartogram Types | Contiguous Cartograms | Grid/Tile Cartograms | Dorling Cartograms | Geographical Map |  
| --- | --- | --- | --- | --- |  
| Easy recognition by position? | 2/3 | 1/3 | 0/3 | 3/3 |  
| Easy recognition by size? | 0/3 | 0/3 | 0/3 | 3/3 |  
| Easy recognition by shape? | 1/3 | 1/3 | 0/3 | 3/3|  
| Easy to compare the shape sizes? | 1/3 | 2/3 | 3/3 | |  
| Accurate? | 2/3 | 2/3 | 3/3 | |  

> [!note] Isarithmic Maps  
> **Isarithmic maps** demonstrate smooth, continuous phenomena (temperature, elevation, rainfall, etc.)  

## Spatial Statistics  

The statistical techniques we've discussed so far won't work well when visualizing spatial distributions...  
...Which means we have a chance to look at data and the relationship between the data in new and interesting ways (distance, adjacency, interaction, and neighbor)  

> [!note] Spatial data violate conventional statistics  
> Violations:  
> - Spatial autocorrelation  
> - Modifiable areal unit problem (MAUP)  
> - Edge effects (Boundary problem)  
> - Ecology fallacy  
> - Nonuniformity of space  

> [!note] Spatial Autocorrelation  
> Data from locations near one another in space are more likely to be similar than data from locations remote from one another  
> - Housing market  
> - Elevation change  
> - Temperature  

> [!note] Modifiable Areal Unit Problem (MAUP)  
> The aggregation units used are arbitrary with respect to the phenomena under investigation, yet the aggregation units used will affect statistics determined on the basis of data reported in this way.  
> If the spatial units in a particular study were specified differently, we might observe very different patterns and relationships.  
> MAUP: Units are arbitrarily defined and different organization of the units may create different analytical results (i.e. gerrymandering)  

> [!note] Edge Effects (The Boundary Problem)  
> Analyzing A vs. B ignores similarities between the two based on their shared boundary  

> [!note] Ecological Fallacy  
> The ecological Fallacy is a situation that can occur when a researcher or analyst makes an inference about an individual based on aggregate data for a group.  
> Issues:  
> Inferences drawn about associations between the characteristics of an aggregate population and the characteristics of sub-units within the population are wrong. That is: results from aggregated data (e.g. counties) cannot be applied to individual people  
> What should we do?  
> Be aware of the process of aggregating or disaggregating data may conceal the variations that are not visible at the larger aggregate level  

> [!note] Nonuniformity  

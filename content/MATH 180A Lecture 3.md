---
tags:
- "Type/Note"
- "Topic/Probability"
- "Class/MATH_180A"
date:
- 2024-04-05
---
Source: https://canvas.ucsd.edu/courses/55106/pages/lecture-notes-and-videos  

**Example: w/ replacement, order matters:** I flip a fair coin 6 times.  

> [!question] Describe the sample space  
> $\Omega=\{H,T\}^6=\{(c_1,c_2,c_3,c_4,c_5,c_6):c_i\in\{H,T\}\}$  

> [!question] Calculate $\mathbb{P}(\text{every even flip is heads})$  
> $=\frac{\#\text{"every even flip is H"}}{\#\Omega}=\frac{\#\{(c_1,H,c_2,H,c_5,H):c_i\in\{H,T\}\}}{\#\Omega}$  
> $=\frac{2^3}{2^6}=\frac{1}{8}$  

**Example: w/o replacement, order matters**  

There are 6 numbered balls in an urn. 3 are removed w/o replacement and lined up in order.  

> [!question] Calculate the probability that the 1st tow numbers removed are (3,6) (in that order).  
> $=\frac{\#\text{"1st 2 removed are (3,6"}}{\#\Omega}$  
> $=\frac{\#\{(3,6,b_3):b_3\in\{1,2,4,5\}\}}{\#\Omega}=\frac{4}{(6)_3}=\frac{4}{6\cdot5\cdot4}=\frac{1}{30}$  

> [!question] Suppose 5 balls are removed instead of 3. Now what is the probability that the 1st two numbers removed are (3,6)?  
> $\frac{\#\{(3,6,b_3,b_4,b_5):b_3\in\{1,2,4,5\},b_4\in\{1,2,4,5\}\setminus\{b_3\},b_5\in\{1,2,4,5\}\setminus\{b_3,b_4\}\}}{\#\Omega}$  
> $=\frac{4\cdot3\cdot2}{6\cdot5\cdot4\cdot3\cdot2}=\frac{(4)_3}{(6)_5}=\frac{1}{30}$  

An urn contains 10 marbles: 5 are red, 2 are white, 3 are blue. Three are chosen uniformly at random and taken out.  

> [!question] Calculate the probability that we drew 2 blue and 1 red.  
> $\frac{\begin{pmatrix}5\\1\end{pmatrix}\cdot\begin{pmatrix}3\\2\end{pmatrix}}{\begin{pmatrix}10\\3\end{pmatrix}}=\frac{5\cdot3}{\begin{pmatrix}10\\3\end{pmatrix}}=\frac{1}{8}$  

> [!question] Instead, suppose that the urn contained 6 red, 4 white, and 7 blue marbles and that we drew three uniformly at random. Now calculate the probability that we drew 2 blue and 1 red.  
> $\frac{\begin{pmatrix}7\\2\end{pmatrix}\cdot\begin{pmatrix}6\\1\end{pmatrix}}{\begin{pmatrix}17\\3\end{pmatrix}}=\frac{7\cdot6\cdot6\cdot3\cdot2\cdot1}{2\cdot1\cdot1\cdot17\cdot16\cdot15}$  

# Section 1.3  

**Infinitely Many Outcomes**  

**Example.** A number $X$ is chosen "uniformly at random" from the interval $[0,2]$.  

> [!question] Describe the probability space modeling this experiment  
> $\Omega=[0,2]$  
> $\mathbb{P}(A)=\frac{length(A)}{length([0,2])}=\frac{length(A)}{2}$  
> $A\subseteq[0,2]$ subset  
> $\mathcal{F}=$ all subsets of [0,2] which "can be reasonably assigned a length"  
> e.g. length([a,b]) = b-a  
> length([1/3,1/2]U[1,1.3]))=(1/2-1/3)+(1.3-1)  

> [!question] What is $\mathbb{P}(X\geq0.5)$?  
> $\frac{2-0.5}{2}=\frac{3}{4}$  
> $\mathbb{P}(X\geq0.5)=\mathbb{P}([0.5,2])=\frac{length([0.5,2])}{length([0,2])}=\frac{2-0.5}{2}=\frac{3}{4}$  

> [!question] What is $\mathbb{P}(X=1)$?  
> $\mathbb{P}(X=1)=\mathbb{P}([1,1])=\frac{1-1}{2}=0$  
> $\mathbb{P}(X=1.2020202020)=0$  
> $\mathbb{P}(X=a)=0$ doesn't mean X=a is impossible  
> $\mathbb{P}([0,2])\neq\sum_{0\leq a\leq2}\mathbb{P}(X=a)=0$ because [0,2] is uncountable  

**Example.** An archery target is a 50cm diameter disk containing a middle disk of 25cm and a bullseye of 5cm. You shoot an arrow which hits a point uniformly at random on the target.  

> [!question] Describe the probability space modeling this experiment  
> $\Omega=target=\{(x,y)\in\mathbb{R}^2:x^2+y^2\leq25\}$  
> $\mathcal{F}=$ all subsets of $\Omega$ which we can "reasonably assign an area"  
> $\mathbb{P}(A)=\frac{area(A)}{area(\Omega)}=\frac{area(A)}{\pi(25)^2}$  
> $A\subseteq\Omega$  

> [!question] Calculate the probability that the arrow hits the middle disk but misses the bullseye.  
> $\mathbb{P}(\text{middle disk not bullseye})=\frac{\frac{\pi(25)^2}{4}-\frac{\pi(5)^2}{4}}{\pi(25)^2}=\frac{24}{100}$  

> [!question] Calculate the probability that the arrow hits the bullseye.  
> $\mathbb{P}(bullseye)=\frac{Area(bullseye)}{\pi(25)^2}=\frac{\frac{5(5)^2}{4}}{\pi(25)^2}=\frac{1}{100}$  

---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/COGS_9"
date:
- 2024-03-11
---
# How to Train Your Vicuna - Finetuning, Evaluating, and Serving LLMs in the Wild - Hao Zhang  

alpa.ai  
lmsys.org  
vllm.ai  

> [!note] Background: LLMs and Open Source LLMs  

> [!note] Topics  
> - How we trained Vicuna  
> - One core problem after Vicuna: Evaluation  
> - Evaluation  
>   - LLM-as-judge  
>   - Chatbot arena  

> [!note] Background  
> Meta Llama weights  
> Used ShareGPT to collect conversations from API and train Vicuna  

> [!note] Why is ShareGPT small yet effective?  
> ShareGPT data contains the user preferences implicit in the ChatGPT conversations that were trained using RLHF (Reinforcement Learning with Human Feedback)  

> [!note] Llama + ShareGPT = Vicuna  
> Strongly preferred by users than base models  
> Does not improve, sometimes decreases academic NLP metrics  

"For better or worse, benchmarks shape a field" - David Patterson, Turing Award 2017  

> [!note] LLMs are extremely hard to evaluate  
> Unreliable: Benchmarks cannot tell human preference  
>   - Requires expertise to evaluate  
>   - Data contamination  
> Cost: Very expensive to evaluate  

> [!note] How to evaluate human preferences?  
> Use humans to rate chatbots  

> [!note] Human Evaluation  
> Chatbot answers interpreted by humans, so it makes sense for humans to be ultimate arbiters  
> Ideally, for every question we want to rank all LLMs  
> Ranking N choices is hard:  
> - Easier to pick best of N  
> - Even easier to pick best of two!  

> [!note] How to scale human evaluation  
> Tournament  
> ELO rating  

> [!note] [Chatbot Arena](https://arena.lmsys.org)  
> Benchmark platform for LLMs that features anonymous, randomized battles in a crowdsourced manner  

---  

> [!note] How to evaluate it?  
> - Humans take long and are expensive  
> - How about we use the strongest LLM to evaluate?  

> [!note] Evaluation: MT-Bench  
> Our initial method: LLM Exams and LLM-as-a-Judge  
> - Let two chatbots generate responses to the same set of questions  
> - Use GPT-4 to assess the model responses  
> - Simultaneously, let human raters assess the model responses  
> - Study the alignment between GPT-4 and human raters  

> [!note] Can we really trust LLM as judge?  

> [!note] Limitations: not unlike humans  
> Position bias: prefer first position  
> Verbosity bias: prefer long answers  
> Self-enhancement bias: prefer answers from itself  
> Limited reasoning: not good at grading math questions  

> [!note] High agreement despite limitations  
> Agreement between GPT-4 and humans over 80%: same/better as human-human agreement  

> [!note] Summary  
> - LLM evaluation is extremely hard  
> - Cracking this problem requires new techniques  
>   - LLMs as judges  
>   - Scalable human evaluation  
> - Many challlenges remain  
>   - Contamination: generating unique exams difficult  
>   - Diversity: most questions are easy; need hard questions to differentiate between LLMs  

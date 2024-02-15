---
tags:
- "Type/Note"
- "Topic/Data_Science"
- "Class/COGS_9"
date:
- 2024-02-14
---
Source: https://drive.google.com/file/d/1Pou5InOgSZiEYtRofYpRd13sRL40C9cs/view  

# Adversarial Examples for Human Vision - Vijay Veerabadran  

> [!note] Adversarial Examples  
> - Perturbations designed by an adversary to misalign predictions made by machine learning models  
> - In computer vision: Perturbations added to images that cause an image classifier to make wrong predictions  

> [!note] Security Concerns Caused by Adversarial Images  
> - Deep learning models deployed in critical applications such as autonomous driving, ATS, etc. are exposed to security concerns.  

Adversarial examples have been assumed to uniquely plague machine perception. Do they also influence human perception?  

> [!note] Generating adversarial examples  
> - Adversarial attacks often generated through an optimization process requiring access to the victim model's parameters, gradients, and classification decisions  
> - These details are inaccessible from the human vision system  

> [!note] Hints suggesting effect on human perception  
> - "Blackbox" adversarial images are capable of affecting predictions of deep learning models  
>   - Without access to the model's learned parameters  
>   - Without access to the model's architecture  
>   - Without requiring to run inference on the model (or access to classification decisions)  

> [!note] Hypothesis  
> H: Adversarial examples that transfer strongly across deep learning models target semantic features that may also influence human visual perception  
> Aim: Identify conditions wherein we can detect adversarial examples influencing human perception  

## Study 1: Adversarial examples that fool both computer vision models and time-limited humans  

> [!note] Experiment 1 setup  
> - Subjects performed a time-limited classification task  
> - Dynamic mask used to reduce influence from feedback connections  
> - Subjects responded with one of two options using a response time box  

> [!note] Experiment 1 conditions  
> - Conditions  
>   - image: Clean image which is classified as class T  
>   - A$\uparrow$Adversarial image corresponding to "image" that is classified as A  
>   - control: Perturbed (non-adversarial) image with the same amount of noise as A  

> [!note] Experiment 1 results  
> A$\uparrow$ has an increased error rate over the control group  

> [!note] Limitations of Experiment 1  
> - Adversarial perturbations were large in magnitude ($\pm32/256$ intensity levels)  
> - Effect demonstrated only for time-limited stimulus viewing  

## Current study: Subtle adversarial image manipulations influence both human and machine perception  

> [!note] Image-pair assessment experiment setup  
> - Task: Choose which image looks more \<A\>-like  
> - Number of subjects: n=100  
> - Data collected:  
>   - Participant choice  
>   - Response time  

> [!note] Experiment 4 conditions (A$\uparrow$ vs A'$\uparrow$)  
> - image: Unperturbed image classified as T  
> - A$\uparrow$: targeted adversarial image, target = A  
> - A'$\uparrow$: targeted adversarial image, target = A'  
> - $\epsilon$: L-$\infty$ norm of perturbation magnitude ($\Vert T\uparrow-x\Vert_\infty==\Vert T\uparrow-x\Vert_\infty$)  

> [!note] Experiment 4 results  
> A$\uparrow$ image perceived more A-like than A'$\uparrow$ images (and vice-versa)  

> [!note] Summary so far  
> - Subtle adversarial image manipulations influence human perception  
> - We identify three conditions where the effect can be robustly detected for human vision  
> - What ANN properties are crucial for influencing human perception?  

> [!note] ANN properties crucial for transfer to humans  
> - Are there certain factors about certain ANNs perturbations that appeal more to humans?  
> - We designed an experiment to test for differences as a function of model architectures in producing perturbations that transfer better to humans  

> [!note] Self-attention models vs. convolution models  
> Alignment between humans and self-attention models was higher than the alignment between humans and convolutional models  

> [!note] Self-attention vs. Convolution Perturbations  
> - Visualizing adversarial perturbations (delta images) obtained from self-attention and convolutional models  
> - Self-attention perturbation images contain relatively more evidence for edges  

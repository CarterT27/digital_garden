---
tags:
- "Type/Note"
- "Topic/Quantitative_Finance"
- "Club/Triton_Quantitative_Trading"
date:
- 2024-10-04
---

Source: https://docs.google.com/presentation/d/18zOOAOMr46qcWH_mLTa0QuzmMMRyr6c-/edit?usp=sharing&ouid=102562506046996324732&rtpof=true&sd=true

# Overview of Markov Decision Process

> [!definition] MDP
> a mathematical framework for modeling decision-making situations where outcomes are partly random and partly under the control of a decision-maker, characterized by states, actions, and rewards

> [!definition] Markov Property

1. States in trading - market conditions
2. Actions available - buying, selling, or holding a stock
3. Reward structure - profit or loss resulting from the actions taken

> [!definition] Reinforcement Learning

Reinforcement derived from MDP Process

RL vs. Other Learning Paradigms

Pros:
- handles complex environments
- learns from delayed rewards
- adapts to dynamic markets
- balances exploration and exploitation
- scalable with deep learning
- provides robust decision-making

Cons:
- Requires extensive data
- High computational cost
- Difficult to tune hyperparameters
- Risk of overfitting
- Limited interpretability
- Insensitive to market changes

# Q-Learning and Bellman Equation

> [!definition] Q-Learning
> Q-Learning is a **model-free** reinforcement learning algorithm that enables an agent to learn the value of actions in a given state by using a **Q-table**
> Q-values: expected reward of taking a specific action when in a specific state
> Iteratively updated based on the Bellman equation and observed rewards

Bellman Equation
![[Pasted image 20241004172646.png]]

Discount Factor Gamma ($\gamma$)
- determines the present value of future rewards
- higher discount factor encourages the agent to prioritize long-term rewards, and vice-versa
- want the Q-value to converge, discount factor plays an important role

State Transition Probabilities: only applies to defined environments with defined rules

# Action Selection Strategies

Exploration: discover new actions and states
Exploitation: taking actions that the agent already knows has high Q values to maximize the reward

Epsilon-Greedy Strategy: random actions for probability $\epsilon$ and greedy actions for probability $(1-\epsilon)$ where $\epsilon$ decreases over iterations
- Epsilon decay factor can be linear or exponential

Other Strategies
- Boltzmann Exploration: Q-values and temperature
- Upper Confidence Bound
- Thompson Sampling
- Entropy-Based Exploration
- Exploration with Noise: Noisy Networks

# Experience Buffer

Deep learning to approximate Q-value function allows to handle larger state spaces and more complex environments

Experience replay allows us to store pass experiences and sample during training to break correlation between consecutive experiences
- Makes data IID

Target Network: Copy weights to increase stability

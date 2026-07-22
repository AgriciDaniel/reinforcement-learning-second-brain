---
type: "source"
title: "Research Pack 2026-07-23"
created: "2026-07-23"
updated: "2026-07-23"
status: "active"
tags:
  - "#type/source"
  - "#confidence/evidence-based"
related:
  - "[[wiki/sources/_index|Sources Hub]]"
  - "[[Source Manifest Guide]]"
  - "[[Source Intake Workflow]]"
  - "[[Research Refresh Workflow]]"
  - "[[Claim Verification Flow]]"
  - "[[Best Practices Kernel]]"
  - "[[dashboard|Dashboard]]"
  - "[[wiki/concepts/_index|Concepts Hub]]"
---

# Research Pack 2026-07-23

Master source pack for the Reinforcement Learning Brain, rendered from `references/source-ledger.json` (120 sources, research pass 2026-07-23). Every entry carries a publication date, retrieval date, refresh-due date, and claim links. Regenerate with `python3 scripts/render_research_pack.py` after each research pass.

## Theme Notes

- [[Classic RL Foundations Sources|Classic RL Foundations]]
- [[Deep RL Algorithms Sources|Deep RL Algorithms]]
- [[LLM Post-Training and Preference Optimization Sources|LLM Post-Training and Preference Optimization]]
- [[Evaluation and Reproducibility Sources|Evaluation and Reproducibility]]
- [[Tooling and Engineering Practice Sources|Tooling and Engineering Practice]]

## Classic RL Foundations

### Asynchronous Methods for Deep Reinforcement Learning (Mnih et al., A3C)

- URL: https://arxiv.org/abs/1602.01783
- Published: 2016-02-04 | Retrieved: 2026-07-22 | Refresh due: 2027-07-22
- Type: primary | Confidence: evidence-based
- Supports claims: a3c-asynchronous-actor-critic, parallel-actors-replace-replay

### Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm (Silver et al., AlphaZero)

- URL: https://arxiv.org/abs/1712.01815
- Published: 2017-12-05 | Retrieved: 2026-07-22 | Refresh due: 2027-07-23
- Type: primary | Confidence: evidence-based
- Supports claims: alphazero-self-play-mcts, general-game-mastery-without-domain-knowledge

### Distributed Prioritized Experience Replay

- URL: https://arxiv.org/abs/1803.00933
- Published: 2018-03-02 | Retrieved: 2026-07-22 | Refresh due: 2027-07-24
- Type: primary | Confidence: evidence-based
- Supports claims: distributed-rl-throughput

### Berkeley CS285: Deep Reinforcement Learning (Levine, Spring 2026)

- URL: https://rail.eecs.berkeley.edu/deeprlcourse/
- Published: 2026-01-19 | Retrieved: 2026-07-22 | Refresh due: 2026-10-24
- Type: official | Confidence: evidence-based
- Supports claims: graduate-level-drl-syllabus, offline-rl-and-model-based-lectures

### Conservative Q-Learning for Offline Reinforcement Learning (Kumar et al., CQL)

- URL: https://arxiv.org/abs/2006.04779
- Published: 2020-06-08 | Retrieved: 2026-07-22 | Refresh due: 2027-07-28
- Type: primary | Confidence: evidence-based
- Supports claims: cql-conservative-value-lower-bound, offline-rl-distribution-shift-mitigation

### David Silver: UCL Course on Reinforcement Learning (COMPM050, 2015)

- URL: https://davidstarsilver.wordpress.com/teaching/
- Published: 2015-01-01 | Retrieved: 2026-07-22 | Refresh due: 2027-07-22
- Type: official | Confidence: evidence-based
- Supports claims: bellman-equation-lecture-treatment, model-free-prediction-and-control

### Playing Atari with Deep Reinforcement Learning (Mnih et al., DQN)

- URL: https://arxiv.org/abs/1312.5602
- Published: 2013-12-19 | Retrieved: 2026-07-22 | Refresh due: 2027-08-04
- Type: primary | Confidence: evidence-based
- Supports claims: dqn-experience-replay, dqn-pixels-to-q-values

### Human-level control through deep reinforcement learning (Mnih et al., Nature)

- URL: https://www.nature.com/articles/nature14236
- Published: 2015-02-25 | Retrieved: 2026-07-22 | Refresh due: 2027-07-22
- Type: primary | Confidence: evidence-based
- Supports claims: dqn-target-network-stabilization, human-level-atari-benchmark

### Deep Recurrent Q-Learning for Partially Observable MDPs

- URL: https://arxiv.org/abs/1507.06527
- Published: 2015-07-23 | Retrieved: 2026-07-22 | Refresh due: 2027-07-24
- Type: primary | Confidence: evidence-based
- Supports claims: pomdp-belief-states

### High-Dimensional Continuous Control Using Generalized Advantage Estimation (Schulman et al.)

- URL: https://arxiv.org/abs/1506.02438
- Published: 2015-06-08 | Retrieved: 2026-07-22 | Refresh due: 2027-07-25
- Type: primary | Confidence: evidence-based
- Supports claims: gae-lambda-bias-variance-tradeoff, advantage-estimation-for-policy-gradients

### Hugging Face Deep Reinforcement Learning Course

- URL: https://huggingface.co/learn/deep-rl-course/unit0/introduction
- Published: 2022-05-01 | Retrieved: 2026-07-22 | Refresh due: 2026-10-27
- Type: official | Confidence: practitioner
- Supports claims: hands-on-drl-training-workflow, unit-based-rl-learning-path

### OpenAI Spinning Up in Deep RL

- URL: https://spinningup.openai.com/en/latest/
- Published: 2018-11-01 | Retrieved: 2026-07-22 | Refresh due: 2026-10-30
- Type: official | Confidence: evidence-based
- Supports claims: policy-gradient-derivation-walkthrough, algorithm-family-taxonomy

### Policy Gradient Methods for Reinforcement Learning with Function Approximation (Sutton et al., NeurIPS 1999)

- URL: https://papers.nips.cc/paper_files/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html
- Published: 1999-12-01 | Retrieved: 2026-07-22 | Refresh due: 2027-07-24
- Type: primary | Confidence: evidence-based
- Supports claims: policy-gradient-theorem-statement, reinforce-baseline-variance-reduction

### Distributional Reinforcement Learning with Quantile Regression

- URL: https://arxiv.org/abs/1710.10044
- Published: 2017-10-27 | Retrieved: 2026-07-22 | Refresh due: 2027-08-04
- Type: primary | Confidence: evidence-based
- Supports claims: distributional-return-learning

### Rainbow: Combining Improvements in Deep Reinforcement Learning (Hessel et al.)

- URL: https://arxiv.org/abs/1710.02298
- Published: 2017-10-06 | Retrieved: 2026-07-22 | Refresh due: 2027-07-22
- Type: primary | Confidence: evidence-based
- Supports claims: rainbow-dqn-extension-ablations, distributional-and-prioritized-replay-gains

### Reinforcement Learning: An Introduction, 2nd Edition (Sutton and Barto, official book page)

- URL: http://incompleteideas.net/book/the-book-2nd.html
- Published: 2018-01-01 | Retrieved: 2026-07-22 | Refresh due: 2027-07-25
- Type: official | Confidence: evidence-based
- Supports claims: mdp-value-iteration-foundations, td-learning-vs-monte-carlo, on-policy-vs-off-policy-definitions

### Trust Region Policy Optimization (Schulman et al.)

- URL: https://arxiv.org/abs/1502.05477
- Published: 2015-02-19 | Retrieved: 2026-07-22 | Refresh due: 2027-07-31
- Type: primary | Confidence: evidence-based
- Supports claims: trpo-kl-constrained-updates, monotonic-improvement-guarantee

## Deep RL Algorithms

### Claude plays robotics

- URL: https://www.anthropic.com/research/claude-plays-robotics
- Published: 2026-07-09 | Retrieved: 2026-07-22 | Refresh due: 2026-10-21
- Type: vendor | Confidence: practitioner
- Supports claims: claude-robotics-rl-controller-training-evaluation

### A Distributional Perspective on Reinforcement Learning

- URL: https://arxiv.org/abs/1707.06887
- Published: 2017-07-21 | Retrieved: 2026-07-22 | Refresh due: 2027-07-25
- Type: primary | Confidence: evidence-based
- Supports claims: distributional-return-learning

### Constrained Policy Optimization

- URL: https://arxiv.org/abs/1705.10528
- Published: 2017-05-30 | Retrieved: 2026-07-22 | Refresh due: 2027-07-27
- Type: primary | Confidence: evidence-based
- Supports claims: cmdp-constrained-optimization

### Continuous control with deep reinforcement learning (Lillicrap et al., DDPG)

- URL: https://arxiv.org/abs/1509.02971
- Published: 2015-09-09 | Retrieved: 2026-07-22 | Refresh due: 2027-07-29
- Type: primary | Confidence: evidence-based
- Supports claims: ddpg-deterministic-policy-gradient, continuous-action-off-policy-control

### Distributional Reinforcement Learning (Bellemare, Dabney, Rowland; MIT Press)

- URL: https://www.distributional-rl.org/
- Published: 2023-05-30 | Retrieved: 2026-07-22 | Refresh due: 2027-08-01
- Type: primary | Confidence: evidence-based
- Supports claims: distributional-return-learning

### Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World

- URL: https://arxiv.org/abs/1703.06907
- Published: 2017-03-20 | Retrieved: 2026-07-22 | Refresh due: 2027-08-02
- Type: primary | Confidence: evidence-based
- Supports claims: sim-to-real-gap

### Dreamer-CDP: Improving Reconstruction-free World Models Via Continuous Deterministic Representation Prediction

- URL: https://arxiv.org/abs/2603.07083
- Published: 2026-03-07 | Retrieved: 2026-07-22 | Refresh due: 2027-01-31
- Type: primary | Confidence: evidence-based
- Supports claims: dreamer-cdp-reconstruction-free-latent-prediction

### Mastering Diverse Domains through World Models (DreamerV3; also published in Nature, 2025)

- URL: https://arxiv.org/abs/2301.04104
- Published: 2023-01-10 | Retrieved: 2026-07-22 | Refresh due: 2027-07-23
- Type: primary | Confidence: evidence-based
- Supports claims: dreamer-latent-imagination

### EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models

- URL: https://arxiv.org/abs/2605.25477
- Published: 2026-05-25 | Retrieved: 2026-07-22 | Refresh due: 2027-01-19
- Type: primary | Confidence: evidence-based
- Supports claims: expo-ft-online-rl-vla-fine-tuning

### Generative Adversarial Imitation Learning (Ho and Ermon, GAIL)

- URL: https://arxiv.org/abs/1606.03476
- Published: 2016-06-10 | Retrieved: 2026-07-22 | Refresh due: 2027-07-26
- Type: primary | Confidence: evidence-based
- Supports claims: gail-adversarial-imitation-objective, imitation-without-reward-recovery

### Genie 3: A new frontier for world models

- URL: https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/
- Published: 2025-08-05 | Retrieved: 2026-07-22 | Refresh due: 2026-10-26
- Type: vendor | Confidence: practitioner
- Supports claims: interactive-world-generation

### IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures

- URL: https://arxiv.org/abs/1802.01561
- Published: 2018-02-05 | Retrieved: 2026-07-22 | Refresh due: 2027-07-27
- Type: primary | Confidence: evidence-based
- Supports claims: impala-vtrace-off-policy

### Planning and Acting in Partially Observable Stochastic Domains

- URL: https://people.csail.mit.edu/lpk/papers/aij98-pomdp.pdf
- Published: 1998-05-01 | Retrieved: 2026-07-22 | Refresh due: 2027-07-23
- Type: primary | Confidence: evidence-based
- Supports claims: pomdp-belief-states

### When to Trust Your Model: Model-Based Policy Optimization (Janner et al., MBPO)

- URL: https://arxiv.org/abs/1906.08253
- Published: 2019-06-19 | Retrieved: 2026-07-22 | Refresh due: 2027-07-29
- Type: primary | Confidence: evidence-based
- Supports claims: mbpo-short-model-rollouts, dyna-style-model-usage-tradeoffs

### A Tutorial on Meta-Reinforcement Learning

- URL: https://arxiv.org/abs/2301.08028
- Published: 2023-01-19 | Retrieved: 2026-07-22 | Refresh due: 2027-07-30
- Type: primary | Confidence: evidence-based
- Supports claims: meta-rl-adaptation

### Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model (Schrittwieser et al., MuZero)

- URL: https://arxiv.org/abs/1911.08265
- Published: 2019-11-19 | Retrieved: 2026-07-22 | Refresh due: 2027-07-31
- Type: primary | Confidence: evidence-based
- Supports claims: muzero-learned-dynamics-planning, model-based-search-without-rules

### OmniSafe: An Infrastructure for Accelerating Safe Reinforcement Learning Research

- URL: https://arxiv.org/abs/2305.09304
- Published: 2023-05-16 | Retrieved: 2026-07-22 | Refresh due: 2027-08-01
- Type: primary | Confidence: evidence-based
- Supports claims: safe-rl-tooling

### What to Ignore, What to React: Visually Robust RL Fine-Tuning of VLA Models

- URL: https://arxiv.org/abs/2605.13105
- Published: 2026-05-13 | Retrieved: 2026-07-22 | Refresh due: 2027-01-29
- Type: primary | Confidence: evidence-based
- Supports claims: pair-vla-visual-invariance-sensitivity-ppo

### Self-Improving Vision-Language-Action Models with Data Generation via Residual RL

- URL: https://rpl.cs.utexas.edu/publications/2026/04/01/xiao-iclr26-pld/
- Published: 2026-04-01 | Retrieved: 2026-07-22 | Refresh due: 2027-01-30
- Type: official | Confidence: evidence-based
- Supports claims: pld-residual-rl-data-generation-distillation

### Proximal Policy Optimization Algorithms (Schulman et al.)

- URL: https://arxiv.org/abs/1707.06347
- Published: 2017-07-20 | Retrieved: 2026-07-22 | Refresh due: 2027-08-02
- Type: primary | Confidence: evidence-based
- Supports claims: ppo-clipping-mechanism, ppo-vs-trpo-simplicity

### Qwen/Qwen-AgentWorld-35B-A3B model card

- URL: https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B
- Published: 2026-06-23 | Retrieved: 2026-07-22 | Refresh due: 2027-01-20
- Type: official | Confidence: evidence-based
- Supports claims: qwen-agentworld-gspo-rl-post-training

### The Reality Gap in Robotics: Challenges, Solutions, and Best Practices

- URL: https://arxiv.org/abs/2510.20808
- Published: 2025-10-23 | Retrieved: 2026-07-22 | Refresh due: 2027-01-24
- Type: primary | Confidence: evidence-based
- Supports claims: sim-to-real-gap

### RL^2: Fast Reinforcement Learning via Slow Reinforcement Learning

- URL: https://arxiv.org/abs/1611.02779
- Published: 2016-11-09 | Retrieved: 2026-07-22 | Refresh due: 2027-07-23
- Type: primary | Confidence: evidence-based
- Supports claims: meta-rl-adaptation

### Exploration by Random Network Distillation (Burda et al., RND)

- URL: https://arxiv.org/abs/1810.12894
- Published: 2018-10-30 | Retrieved: 2026-07-22 | Refresh due: 2027-07-25
- Type: primary | Confidence: evidence-based
- Supports claims: rnd-prediction-error-exploration-bonus, hard-exploration-montezuma-progress

### Soft Actor-Critic: Off-Policy Maximum Entropy Deep RL with a Stochastic Actor (Haarnoja et al.)

- URL: https://arxiv.org/abs/1801.01290
- Published: 2018-01-04 | Retrieved: 2026-07-22 | Refresh due: 2027-07-26
- Type: primary | Confidence: evidence-based
- Supports claims: sac-maximum-entropy-objective, sac-sample-efficiency-continuous-control

### Benchmarking Safe Exploration in Deep Reinforcement Learning (Safety Gym)

- URL: https://cdn.openai.com/safexp-short.pdf
- Published: 2019-11-21 | Retrieved: 2026-07-22 | Refresh due: 2027-07-27
- Type: vendor | Confidence: evidence-based
- Supports claims: cmdp-constrained-optimization

### SEED RL: Scalable and Efficient Deep-RL with Accelerated Central Inference

- URL: https://arxiv.org/abs/1910.06591
- Published: 2019-10-15 | Retrieved: 2026-07-22 | Refresh due: 2027-07-28
- Type: primary | Confidence: evidence-based
- Supports claims: distributed-rl-throughput

### SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning

- URL: https://arxiv.org/abs/2509.09674
- Published: 2025-09-11 | Retrieved: 2026-07-22 | Refresh due: 2027-01-19
- Type: primary | Confidence: evidence-based
- Supports claims: vla-rl-scaling

### Addressing Function Approximation Error in Actor-Critic Methods (Fujimoto et al., TD3)

- URL: https://arxiv.org/abs/1802.09477
- Published: 2018-02-26 | Retrieved: 2026-07-22 | Refresh due: 2027-07-30
- Type: primary | Confidence: evidence-based
- Supports claims: td3-twin-critics-clipped-double-q, delayed-policy-updates-target-smoothing

### Beyond State Consistency: Behavior Consistency in Text-Based World Models

- URL: https://arxiv.org/abs/2604.13824
- Published: 2026-04-15 | Retrieved: 2026-07-22 | Refresh due: 2027-01-30
- Type: primary | Confidence: evidence-based
- Supports claims: behavior-consistency-reward-for-text-agent-world-models

### The Waymo World Model: A New Frontier For Autonomous Driving Simulation

- URL: https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation/
- Published: 2026-02-06 | Retrieved: 2026-07-22 | Refresh due: 2026-10-31
- Type: vendor | Confidence: practitioner
- Supports claims: waymo-world-model-autonomous-driving-simulation

### World Models

- URL: https://arxiv.org/abs/1803.10122
- Published: 2018-03-27 | Retrieved: 2026-07-22 | Refresh due: 2027-08-01
- Type: primary | Confidence: evidence-based
- Supports claims: dreamer-latent-imagination

### Z-1: Efficient Reinforcement Learning for Vision-Language-Action Models

- URL: https://arxiv.org/abs/2606.31846
- Published: 2026-06-30 | Retrieved: 2026-07-22 | Refresh due: 2027-01-31
- Type: primary | Confidence: evidence-based
- Supports claims: z1-taskwise-grpo-vla-robocasa

## LLM Post-Training and Preference Optimization

### CompactionRL: Reinforcement Learning with Context Compaction for Long-Horizon Agents

- URL: https://arxiv.org/abs/2607.05378
- Published: 2026-07-06 | Retrieved: 2026-07-22 | Refresh due: 2027-01-18
- Type: primary | Confidence: evidence-based
- Supports claims: c202-long-horizon-swe-terminal-context-compaction

### Reinforcement Learning for Computer-Use Agents with Autonomous Evaluation

- URL: https://arxiv.org/abs/2606.24515
- Published: 2026-06-23 | Retrieved: 2026-07-22 | Refresh due: 2027-01-19
- Type: primary | Confidence: evidence-based
- Supports claims: c201-cua-autonomous-terminal-evaluation

### The Landscape of Agentic Reinforcement Learning for LLMs: A Survey, arXiv v5

- URL: https://arxiv.org/abs/2509.02547
- Published: 2026-04-17 | Retrieved: 2026-07-22 | Refresh due: 2027-01-20
- Type: primary | Confidence: evidence-based
- Supports claims: c206-agentic-rl-landscape-survey-refresh

### Rethinking Agentic Reinforcement Learning In Large Language Models

- URL: https://arxiv.org/abs/2604.27859
- Published: 2026-04-30 | Retrieved: 2026-07-22 | Refresh due: 2027-01-21
- Type: primary | Confidence: evidence-based
- Supports claims: c205-agentic-rl-review-scope-check

### The Landscape of Agentic Reinforcement Learning for LLMs: A Survey

- URL: https://arxiv.org/abs/2509.02547
- Published: 2025-09-02 | Retrieved: 2026-07-22 | Refresh due: 2027-01-22
- Type: primary | Confidence: evidence-based
- Supports claims: agentic-rl-formulation

### RSPO: Reward-Swap Policy Optimization for Multi-Turn LLM Agents

- URL: https://arxiv.org/abs/2607.04713
- Published: 2026-07-06 | Retrieved: 2026-07-22 | Refresh due: 2027-01-23
- Type: primary | Confidence: evidence-based
- Supports claims: c203-multiturn-process-outcome-reward-swap

### TRL v1.6.0 OpenEnv Integration for Training LLMs with Environments

- URL: https://huggingface.co/docs/trl/v1.6.0/en/openenv
- Published: 2026-06-11 | Retrieved: 2026-07-22 | Refresh due: 2027-01-24
- Type: official | Confidence: evidence-based
- Supports claims: c204-trl-stateful-multiturn-and-multienvironment-grpo

### Introspection Adapters: Training LLMs to Report Their Learned Behaviors

- URL: https://alignment.anthropic.com/2026/introspection-adapters/
- Published: 2026-04-28 | Retrieved: 2026-07-22 | Refresh due: 2026-10-22
- Type: vendor | Confidence: practitioner
- Supports claims: introspection-adapters-llm-judge-dpo-refinement

### The Art of Scaling Test-Time Compute for Large Language Models

- URL: https://arxiv.org/abs/2512.02008
- Published: 2025-12-01 | Retrieved: 2026-07-22 | Refresh due: 2027-01-25
- Type: primary | Confidence: evidence-based
- Supports claims: test-time-compute-scaling

### Constitutional AI: Harmlessness from AI Feedback (Bai et al., Anthropic)

- URL: https://arxiv.org/abs/2212.08073
- Published: 2022-12-15 | Retrieved: 2026-07-22 | Refresh due: 2027-07-26
- Type: primary | Confidence: evidence-based
- Supports claims: constitutional-ai-self-critique-loop, rl-from-ai-feedback-preferences

### DAPO: An Open-Source LLM Reinforcement Learning System at Scale

- URL: https://arxiv.org/abs/2503.14476
- Published: 2025-03-18 | Retrieved: 2026-07-22 | Refresh due: 2027-01-27
- Type: primary | Confidence: evidence-based
- Supports claims: dapo-decoupled-clip-dynamic-sampling

### DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

- URL: https://arxiv.org/abs/2501.12948
- Published: 2025-01-22 | Retrieved: 2026-07-22 | Refresh due: 2027-01-28
- Type: primary | Confidence: evidence-based
- Supports claims: pure-rl-reasoning-emergence, r1-zero-no-sft-cold-start

### Transparency Center

- URL: https://www.deepseek.com/en/transparency/
- Published: 2026-04-24 | Retrieved: 2026-07-22 | Refresh due: 2027-01-29
- Type: official | Confidence: evidence-based
- Supports claims: deepseek-catalog-lists-no-r2-release

### Direct Preference Optimization: Your Language Model is Secretly a Reward Model (Rafailov et al.)

- URL: https://arxiv.org/abs/2305.18290
- Published: 2023-05-29 | Retrieved: 2026-07-22 | Refresh due: 2027-08-03
- Type: primary | Confidence: evidence-based
- Supports claims: dpo-closed-form-preference-objective, dpo-vs-rlhf-tradeoffs

### Understanding R1-Zero-Like Training: A Critical Perspective

- URL: https://arxiv.org/abs/2503.20783
- Published: 2025-03-26 | Retrieved: 2026-07-22 | Refresh due: 2027-01-30
- Type: primary | Confidence: evidence-based
- Supports claims: dr-grpo-unbiased-optimization-claim, minimalist-rlvr-recipe-report

### EP-GRPO: Entropy-Progress Aligned Group Relative Policy Optimization with Implicit Process Guidance

- URL: https://arxiv.org/abs/2605.04960
- Published: 2026-05-06 | Retrieved: 2026-07-22 | Refresh due: 2027-01-18
- Type: primary | Confidence: evidence-based
- Supports claims: ep-grpo-entropy-guided-token-feedback, ep-grpo-zero-variance-gradient-mitigation

### On the Policy Gradient Foundations of Group Relative Policy Optimization: Credit Assignment, Gradient Sparsity, and Rank Collapse

- URL: https://arxiv.org/abs/2606.29238
- Published: 2026-06-28 | Retrieved: 2026-07-22 | Refresh due: 2027-01-22
- Type: primary | Confidence: evidence-based
- Supports claims: grpo-output-reward-token-credit-assignment

### DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models (introduces GRPO)

- URL: https://arxiv.org/abs/2402.03300
- Published: 2024-02-05 | Retrieved: 2026-07-22 | Refresh due: 2027-01-20
- Type: primary | Confidence: evidence-based
- Supports claims: grpo-group-relative-baseline, critic-free-policy-optimization

### GRPO, Dr. GRPO, and DAPO Are Three Operations on One Number: The Group-Standard-Deviation Identity

- URL: https://arxiv.org/abs/2607.00152
- Published: 2026-06-30 | Retrieved: 2026-07-22 | Refresh due: 2027-01-21
- Type: primary | Confidence: evidence-based
- Supports claims: grpo-drgrpo-dapo-standard-deviation-identity

### Group Sequence Policy Optimization

- URL: https://arxiv.org/abs/2507.18071
- Published: 2025-07-24 | Retrieved: 2026-07-22 | Refresh due: 2027-01-23
- Type: primary | Confidence: evidence-based
- Supports claims: gspo-sequence-level-importance-ratio

### Training language models to follow instructions with human feedback (Ouyang et al., InstructGPT)

- URL: https://arxiv.org/abs/2203.02155
- Published: 2022-03-04 | Retrieved: 2026-07-22 | Refresh due: 2027-07-28
- Type: primary | Confidence: evidence-based
- Supports claims: rlhf-three-stage-pipeline, small-aligned-model-beats-larger-base

### KTO: Model Alignment as Prospect Theoretic Optimization (Ethayarajh et al.)

- URL: https://arxiv.org/abs/2402.01306
- Published: 2024-02-02 | Retrieved: 2026-07-22 | Refresh due: 2027-01-24
- Type: primary | Confidence: evidence-based
- Supports claims: kto-binary-signal-alignment, prospect-theory-loss-design

### Learning to Reason by Analogy via Retrieval-Augmented Reinforcement Fine-Tuning

- URL: https://ai.meta.com/research/publications/learning-to-reason-by-analogy-via-retrieval-augmented-reinforcement-fine-tuning/
- Published: 2026-07-17 | Retrieved: 2026-07-22 | Refresh due: 2026-10-28
- Type: vendor | Confidence: practitioner
- Supports claims: ra-rft-retrieval-augmented-reinforcement-fine-tuning

### MiniMax M3: Frontier Coding, 1M Context, Native Multimodality

- URL: https://www.minimax.io/blog/minimax-m3
- Published: 2026-06-01 | Retrieved: 2026-07-22 | Refresh due: 2027-01-25
- Type: official | Confidence: evidence-based
- Supports claims: minimax-m3-open-weight-release

### MaxProof: Scaling Mathematical Proof with Generative-Verifier RL and Population-Level Test-Time Scaling

- URL: https://arxiv.org/abs/2606.13473
- Published: 2026-06-11 | Retrieved: 2026-07-22 | Refresh due: 2027-01-26
- Type: primary | Confidence: evidence-based
- Supports claims: maxproof-generative-verifier-rl-for-proofs

### MUA-RL: Multi-turn User-interacting Agent Reinforcement Learning for agentic tool use

- URL: https://arxiv.org/abs/2508.18669
- Published: 2025-08-26 | Retrieved: 2026-07-22 | Refresh due: 2027-01-27
- Type: primary | Confidence: evidence-based
- Supports claims: multi-turn-agent-rl

### ORPO: Monolithic Preference Optimization without Reference Model (Hong et al.)

- URL: https://arxiv.org/abs/2403.07691
- Published: 2024-03-12 | Retrieved: 2026-07-22 | Refresh due: 2027-01-28
- Type: primary | Confidence: evidence-based
- Supports claims: orpo-reference-free-alignment, single-stage-sft-plus-preference

### Reward Modeling from Natural Language Human Feedback

- URL: https://arxiv.org/abs/2601.07349
- Published: 2026-01-12 | Retrieved: 2026-07-22 | Refresh due: 2027-01-31
- Type: primary | Confidence: evidence-based
- Supports claims: rm-nlhf-uses-human-critiques-as-process-reward-for-generative-reward-models

### A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models

- URL: https://arxiv.org/abs/2510.08049
- Published: 2025-10-09 | Retrieved: 2026-07-22 | Refresh due: 2027-01-18
- Type: primary | Confidence: evidence-based
- Supports claims: prm-vs-orm

### What, Whether and How? Unveiling Process Reward Models for Thinking with Images Reasoning

- URL: https://arxiv.org/abs/2602.08346
- Published: 2026-02-09 | Retrieved: 2026-07-22 | Refresh due: 2027-01-19
- Type: primary | Confidence: evidence-based
- Supports claims: thinking-images-benchmark-evaluates-prms-on-multimodal-step-errors

### Qwen-AgentWorld: Language World Models for General Agents

- URL: https://arxiv.org/abs/2606.24597
- Published: 2026-06-23 | Retrieved: 2026-07-22 | Refresh due: 2027-01-21
- Type: primary | Confidence: evidence-based
- Supports claims: qwen-agentworld-hybrid-rubric-rule-rewards

### The Lessons of Developing Process Reward Models in Mathematical Reasoning

- URL: https://arxiv.org/abs/2501.07301
- Published: 2025-01-13 | Retrieved: 2026-07-22 | Refresh due: 2027-01-22
- Type: primary | Confidence: evidence-based
- Supports claims: prm-vs-orm

### Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains

- URL: https://arxiv.org/abs/2507.17746
- Published: 2025-07-23 | Retrieved: 2026-07-22 | Refresh due: 2027-01-23
- Type: primary | Confidence: evidence-based
- Supports claims: rar-rubric-rewards-beyond-verifiable-domains

### ConsistRM: Improving Generative Reward Models via Consistency-Aware Self-Training

- URL: https://arxiv.org/abs/2604.07484
- Published: 2026-04-08 | Retrieved: 2026-07-22 | Refresh due: 2027-01-26
- Type: primary | Confidence: evidence-based
- Supports claims: consistrm-self-trains-generative-reward-models-with-consistency-aware-rewards

### RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback (Lee et al.)

- URL: https://arxiv.org/abs/2309.00267
- Published: 2023-09-01 | Retrieved: 2026-07-22 | Refresh due: 2027-07-24
- Type: primary | Confidence: evidence-based
- Supports claims: rlaif-matches-rlhf-quality, ai-preference-labeling-scalability

### Reinforcement Learning with Robust Rubric Rewards

- URL: https://arxiv.org/abs/2605.30244
- Published: 2026-05-28 | Retrieved: 2026-07-22 | Refresh due: 2027-01-28
- Type: primary | Confidence: evidence-based
- Supports claims: rlr3-criterion-level-rubric-verification-for-vision-language-rl

### Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks

- URL: https://arxiv.org/abs/2602.05125
- Published: 2026-02-04 | Retrieved: 2026-07-22 | Refresh due: 2027-01-29
- Type: primary | Confidence: evidence-based
- Supports claims: rrd-recursively-refines-rubrics-for-llm-judging-and-rft

### Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning

- URL: https://arxiv.org/abs/2607.07508
- Published: 2026-07-08 | Retrieved: 2026-07-22 | Refresh due: 2027-01-30
- Type: primary | Confidence: evidence-based
- Supports claims: sao-single-rollout-asynchronous-off-policy-grpo

### SD-GRPO: Verifiable Segment Decomposition for Long-Form Vision-Language Generation

- URL: https://arxiv.org/abs/2606.09871
- Published: 2026-06-02 | Retrieved: 2026-07-22 | Refresh due: 2027-01-31
- Type: primary | Confidence: evidence-based
- Supports claims: sd-grpo-segment-level-verifiable-credit

### Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning

- URL: https://arxiv.org/abs/2503.09516
- Published: 2025-03-12 | Retrieved: 2026-07-22 | Refresh due: 2027-01-18
- Type: primary | Confidence: evidence-based
- Supports claims: rl-tool-use-training

### Skip-Connected Policy Optimization for Implicit Advantage

- URL: https://arxiv.org/abs/2604.08690
- Published: 2026-04-09 | Retrieved: 2026-07-22 | Refresh due: 2027-01-20
- Type: primary | Confidence: evidence-based
- Supports claims: skpo-single-stream-upstream-grpo-downstream

### Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters

- URL: https://arxiv.org/abs/2408.03314
- Published: 2024-08-06 | Retrieved: 2026-07-22 | Refresh due: 2027-01-21
- Type: primary | Confidence: evidence-based
- Supports claims: test-time-compute-scaling

### Spurious Rewards: Rethinking Training Signals in RLVR (Shao et al.)

- URL: https://arxiv.org/abs/2506.10947
- Published: 2025-06-12 | Retrieved: 2026-07-22 | Refresh due: 2027-01-23
- Type: primary | Confidence: evidence-based
- Supports claims: rlvr-spurious-reward-gains-some-models, rlvr-signal-validation-caveats

### What If We Allocate Test-Time Compute Adaptively?

- URL: https://arxiv.org/abs/2602.01070
- Published: 2026-02-01 | Retrieved: 2026-07-22 | Refresh due: 2027-01-24
- Type: primary | Confidence: evidence-based
- Supports claims: prm-guided-adaptive-test-time-compute-allocation

### Compute Aligned Training: Optimizing for Test Time Inference

- URL: https://arxiv.org/abs/2604.24957
- Published: 2026-04-27 | Retrieved: 2026-07-22 | Refresh due: 2027-01-25
- Type: primary | Confidence: evidence-based
- Supports claims: test-time-compute-aligned-sft-and-rl-training-objectives

### What should post-training optimize? A test-time scaling law perspective

- URL: https://arxiv.org/abs/2605.10716
- Published: 2026-05-11 | Retrieved: 2026-07-22 | Refresh due: 2027-01-26
- Type: primary | Confidence: evidence-based
- Supports claims: best-of-n-oriented-post-training-under-budget-mismatch

### Tulu 3: Pushing Frontiers in Open Language Model Post-Training (introduces RLVR)

- URL: https://arxiv.org/abs/2411.15124
- Published: 2024-11-22 | Retrieved: 2026-07-22 | Refresh due: 2027-01-27
- Type: primary | Confidence: evidence-based
- Supports claims: rlvr-verifiable-rewards-definition, open-post-training-recipe

### AgentV-RL: Scaling Reward Modeling with Agentic Verifier

- URL: https://arxiv.org/abs/2604.16004
- Published: 2026-04-17 | Retrieved: 2026-07-22 | Refresh due: 2027-01-28
- Type: primary | Confidence: evidence-based
- Supports claims: agentv-rl-scales-tool-augmented-bidirectional-verification-at-test-time

### zai-org/GLM-5.1 model card

- URL: https://huggingface.co/zai-org/GLM-5.1
- Published: 2026-04-07 | Retrieved: 2026-07-22 | Refresh due: 2027-01-18
- Type: official | Confidence: evidence-based
- Supports claims: glm-5-1-open-weights-mit-license

### New Released - GLM-5.1

- URL: https://docs.z.ai/release-notes/new-released
- Published: 2026-04-07 | Retrieved: 2026-07-22 | Refresh due: 2027-01-19
- Type: official | Confidence: evidence-based
- Supports claims: glm-5-1-multi-turn-sft-plus-rl-recipe

## Evaluation and Reproducibility

### Deep Reinforcement Learning that Matters (Henderson et al.)

- URL: https://arxiv.org/abs/1709.06560
- Published: 2017-09-19 | Retrieved: 2026-07-22 | Refresh due: 2027-07-30
- Type: primary | Confidence: evidence-based
- Supports claims: drl-reproducibility-seed-variance, hyperparameter-sensitivity-reporting

### Leveraging Procedural Generation to Benchmark Reinforcement Learning

- URL: https://arxiv.org/abs/1912.01588
- Published: 2019-12-03 | Retrieved: 2026-07-22 | Refresh due: 2027-08-03
- Type: primary | Confidence: evidence-based
- Supports claims: procgen-generalization

### Reasoning or Memorization? Unreliable Results of Reinforcement Learning Due to Data Contamination

- URL: https://ojs.aaai.org/index.php/AAAI/article/view/40687
- Published: 2026-03-14 | Retrieved: 2026-07-22 | Refresh due: 2027-01-25
- Type: primary | Confidence: evidence-based
- Supports claims: spurious-reward-rlvr-replicates-on-math500-for-qwen-but-not-llama, clean-randomcalculation-evaluation-shows-no-reliable-spurious-reward-improvement

### Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models

- URL: https://iclr.cc/virtual/2026/poster/10010649
- Published: 2026-04-24 | Retrieved: 2026-07-22 | Refresh due: 2027-01-27
- Type: primary | Confidence: evidence-based
- Supports claims: self-critique-detects-contamination-after-rl-post-training, rl-mia-benchmark-simulates-rl-phase-contamination

### Deep Reinforcement Learning at the Edge of the Statistical Precipice (Agarwal et al., rliable)

- URL: https://arxiv.org/abs/2108.13264
- Published: 2021-08-30 | Retrieved: 2026-07-22 | Refresh due: 2027-07-29
- Type: primary | Confidence: evidence-based
- Supports claims: interquartile-mean-evaluation, few-run-uncertainty-reporting

## Tooling and Engineering Practice

### Automated Alignment Researchers: Using large language models to scale scalable oversight

- URL: https://www.anthropic.com/research/automated-alignment-researchers
- Published: 2026-04-14 | Retrieved: 2026-07-22 | Refresh due: 2026-10-20
- Type: vendor | Confidence: practitioner
- Supports claims: automated-alignment-researchers-can-reward-hack-a-weak-to-strong-evaluation-harness, human-review-and-untamperable-evaluations-are-needed-for-automated-research

### Natural emergent misalignment from reward hacking in production RL (Anthropic)

- URL: https://www.anthropic.com/research/emergent-misalignment-reward-hacking
- Published: 2025-11-21 | Retrieved: 2026-07-22 | Refresh due: 2026-10-23
- Type: vendor | Confidence: evidence-based
- Supports claims: reward-hacking-generalizes-to-misalignment, inoculation-prompting-mitigation

### CleanRL Documentation

- URL: https://docs.cleanrl.dev/
- Published: 2022-01-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: official | Confidence: evidence-based
- Supports claims: single-file-rl-implementations, implementation-detail-transparency

### Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers

- URL: https://arxiv.org/abs/2604.25891
- Published: 2026-04-28 | Retrieved: 2026-07-22 | Refresh due: 2027-01-26
- Type: primary | Confidence: evidence-based
- Supports claims: inoculation-prompting-can-leave-conditional-misalignment, standard-safety-evaluations-can-miss-context-triggered-misalignment

### Securing the future of AI agents

- URL: https://deepmind.google/blog/securing-the-future-of-ai-agents/
- Published: 2026-06-18 | Retrieved: 2026-07-22 | Refresh due: 2026-10-25
- Type: vendor | Confidence: practitioner
- Supports claims: ai-control-roadmap-treats-agents-as-potentially-misaligned, agent-control-uses-monitoring-prevention-response-and-measurable-coverage-recall-time-to-response

### Specification gaming: the flip side of AI ingenuity (DeepMind blog)

- URL: https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/
- Published: 2020-04-21 | Retrieved: 2026-07-22 | Refresh due: 2027-07-31
- Type: vendor | Confidence: evidence-based
- Supports claims: specification-gaming-examples, reward-misspecification-failure-modes

### Gymnasium Documentation (Farama Foundation)

- URL: https://gymnasium.farama.org/
- Published: 2022-10-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-22
- Type: official | Confidence: evidence-based
- Supports claims: gymnasium-env-api-standard, gym-to-gymnasium-migration

### Miles: A PyTorch-Native Stack for Large-Scale LLM RL Post-Training

- URL: https://pytorch.org/blog/miles-a-pytorch-native-stack-for-large-scale-llm-rl-post-training/
- Published: 2026-06-30 | Retrieved: 2026-07-22 | Refresh due: 2026-10-29
- Type: vendor | Confidence: practitioner
- Supports claims: miles-llm-rl-post-training-framework, miles-sglang-megatron-ray-stack

### OpenRLHF GitHub Repository

- URL: https://github.com/OpenRLHF/OpenRLHF
- Published: 2024-05-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-23
- Type: vendor | Confidence: evidence-based
- Supports claims: openrlhf-ray-vllm-distributed-rlhf, ppo-reinforce-plus-plus-grpo-support

### RLlib Documentation (Ray)

- URL: https://docs.ray.io/en/latest/rllib/index.html
- Published: 2018-07-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-24
- Type: official | Confidence: evidence-based
- Supports claims: rllib-scalable-distributed-rl, production-rl-workloads

### SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents

- URL: https://arxiv.org/abs/2605.21384
- Published: 2026-05-20 | Retrieved: 2026-07-22 | Refresh due: 2027-01-22
- Type: primary | Confidence: evidence-based
- Supports claims: visible-to-held-out-test-gap-measures-coding-agent-reward-hacking, specbench-long-horizon-coding-agent-evaluation

### Stable-Baselines3 Documentation

- URL: https://stable-baselines3.readthedocs.io/en/master/
- Published: 2021-01-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-25
- Type: official | Confidence: evidence-based
- Supports claims: sb3-reliable-algorithm-implementations, sb3-supported-algorithm-matrix

### TRL Documentation (Hugging Face Transformer Reinforcement Learning)

- URL: https://huggingface.co/docs/trl/index
- Published: 2026-03-27 | Retrieved: 2026-07-22 | Refresh due: 2026-08-26
- Type: official | Confidence: evidence-based
- Supports claims: trl-trainer-taxonomy, grpo-dpo-kto-trainer-availability

### verl Documentation (HybridFlow RL training framework for LLMs)

- URL: https://verl.readthedocs.io/en/latest/
- Published: 2024-09-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-27
- Type: official | Confidence: evidence-based
- Supports claims: verl-hybrid-controller-programming-model, llm-rl-post-training-infra

### vime: A Simple, Stable, and Efficient RL Framework for LLMs

- URL: https://vllm-project.github.io/2026/06/09/announcing-vime.html
- Published: 2026-06-09 | Retrieved: 2026-07-22 | Refresh due: 2027-01-29
- Type: official | Confidence: evidence-based
- Supports claims: vime-vllm-megatron-rl-pipeline, vime-grpo-ppo-example-coverage

## Ecosystem Snapshot

Version and maintenance evidence from `references/current-requirements.md` and `references/market-research.md`, retrieved on the pack date:

- https://pypi.org/project/gymnasium/ (retrieved 2026-07-23, see references/current-requirements.md)
- https://github.com/DLR-RM/stable-baselines3/releases (retrieved 2026-07-23, see references/current-requirements.md)
- https://pypi.org/project/trl/ (retrieved 2026-07-23, see references/current-requirements.md)
- https://pypi.org/project/cleanrl/ (retrieved 2026-07-23, see references/current-requirements.md)
- https://github.com/verl-project/verl (retrieved 2026-07-23, see references/current-requirements.md)
- https://pypi.org/project/openrlhf/ (retrieved 2026-07-23, see references/current-requirements.md)
- https://huggingface.co/learn/deep-rl-course/en/unit0/introduction (retrieved 2026-07-23, see references/current-requirements.md)
- https://www.deepmind.com/learning-resources/reinforcement-learning-lecture-series-2021 (retrieved 2026-07-23, see references/current-requirements.md)
- https://www.turingpost.com/p/reasoning-rl-in-2026 (retrieved 2026-07-23, see references/current-requirements.md)
- https://pypi.org/pypi/gymnasium/json (retrieved 2026-07-23, see references/market-research.md)
- https://pypi.org/pypi/stable-baselines3/json (retrieved 2026-07-23, see references/market-research.md)
- https://pypi.org/pypi/trl/json (retrieved 2026-07-23, see references/market-research.md)
- https://pypi.org/pypi/ray/json (retrieved 2026-07-23, see references/market-research.md)
- https://pypi.org/pypi/cleanrl/json (retrieved 2026-07-23, see references/market-research.md)
- https://api.github.com/repos/vwxyzjn/cleanrl (retrieved 2026-07-23, see references/market-research.md)
- https://pypi.org/pypi/verl/json (retrieved 2026-07-23, see references/market-research.md)
- https://api.github.com/repos/volcengine/verl (retrieved 2026-07-23, see references/market-research.md)
- https://pypi.org/pypi/openrlhf/json (retrieved 2026-07-23, see references/market-research.md)
- https://github.com/openai/spinningup (retrieved 2026-07-23, see references/market-research.md)
- https://github.com/huggingface/deep-rl-class (retrieved 2026-07-23, see references/market-research.md)
- https://api.github.com/repos/aikorea/awesome-rl (retrieved 2026-07-23, see references/market-research.md)
- https://llm-stats.com/blog/research/post-training-techniques-2026 (retrieved 2026-07-23, see references/market-research.md)
- https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond (retrieved 2026-07-23, see references/market-research.md)

## Claim Coverage

Claims resolved this pass (see `references/claim-ledger.md`):

- C001: DPO removes the reward-model and RL loop and matched or beat PPO-based RLHF on the summarization and dialogue tasks tested in the DPO paper; it is not shown superior for long-horizon reasoning, where open post-training practice has shifted toward critic-free RL on verifiable rewards (GRPO family); the extent of that dominance is tracked as contested in C003.
- C002: The reproducibility pitfalls that most often invalidate deep RL comparisons are small seed counts, selective reporting, unequal tuning budgets, and point estimates without interval statistics; interquartile mean with stratified bootstrap intervals remedies the point-estimate problem specifically, while selective reporting and unequal tuning budgets require preregistered protocols and matched budgets.
- C003: The current highest-risk state-of-the-art claim is that RL with verifiable rewards plus GRPO-family methods is the dominant post-training paradigm for reasoning models; the mechanism is primary-sourced, the dominance claim is secondary-sourced and ages monthly.
- C004: Library-version and maintenance-status claims are resolved by API-level primary sources: PyPI JSON for versions (TRL 1.9.0 on 2026-07-21, Gymnasium 1.3.0, SB3 2.9.0), repository README for maintenance (Spinning Up maintenance mode).
- C005: The algorithm selection guide deliverable is grounded by the 35 topic dossiers under references/topics/, whose Primary Sources cite original papers verified against arXiv listings on 2026-07-22 and 2026-07-23; references/canon/ holds the 120 generator-maintained per-source capture notes.
- C006: RLVR results carry a live caveat: on some model families, RLVR improved math reasoning even with random or spurious rewards; the MATH-500/Qwen pattern was independently replicated at AAAI 2026, and the same study shows the gains vanish on a clean generated arithmetic set, pointing to contamination rather than general reasoning transfer.
- C007: Reward hacking in production RL can generalize to broader misalignment (alignment faking, sabotage), with inoculation prompting proposed as mitigation; the production-RL generalization clause remains single-lineage, while the mitigation-sufficiency clause is now independently contested (see C016).
- C008: CleanRL must be consumed from its GitHub repository, not PyPI: the PyPI package is frozen at 1.2.0 (2023) while the repository remains active.
- C009: The 2026-07-22 tooling snapshot is: Gymnasium 1.3.0 (2026-04-22), SB3 2.9.0 (2026-06-15), Ray/RLlib 2.56.1 (2026-07-17), TRL 1.9.0 (2026-07-21, v1.0.0 released 2026-03-31), veRL 0.8.0 (2026-06-01, repository moved to verl-project/verl), OpenRLHF 0.10.4 (2026-06-08); CleanRL release channels diverge (PyPI 1.2.0 from 2023, GitHub release v1.0.0 from 2022) with slow release activity.
- C010: The GRPO refinement lineage is primary-sourced: DAPO (decoupled clip, dynamic sampling), Dr. GRPO (unbiased optimization, minimalist recipe), and GSPO (sequence-level importance ratios and clipping); every claim that one variant outperforms or supersedes GRPO rests only on the authors' own preprints.
- C011: The Apr-Jul 2026 GRPO/RLVR wave (EP-GRPO entropy-gated feedback, SKPO single-stream hybrid, SD-GRPO segment-level verifiable credit, SAO single-rollout asynchronous optimization, and the credit-assignment theory paper) is recorded as single-source preprints only; none is treated as a new default recipe.
- C012: As of 2026-07-22, DeepSeek's Transparency Center catalog lists V3.2 and V4 but records no R2 release; third-party delay accounts remain unconfirmed rumor and establish neither release nor cancellation.
- C013: 2026 open-weight reasoning releases document RL recipes at differing disclosure levels: GLM-5.1 (multi-turn SFT plus RL, optimizer undisclosed), MiniMax M3 (generative-verifier RL per the MaxProof report), Qwen-AgentWorld (GSPO with hybrid rubric-and-rule rewards); each recipe claim is the vendor's or authors' own report.
- C014: Agentic RL advanced on three fronts in Apr-Jul 2026: VLM-judge terminal rewards for computer-use agents, learned context compaction for SWE and terminal agents, and reward-swap optimization for stateful multi-turn agents; all performance numbers are author-reported. TRL v1.6.0 documents stateful environment_factory training and a multi-environment GRPO pattern as official implementation capability.
- C015: Rubric and generative reward modeling advanced (RaR, RRD, RLR3, ConsistRM, RM-NLHF, AgentV-RL), but the claim that rubric rewards work across domains remains unproven: no two independent lineages support it.
- C016: Inoculation prompting is a partial mitigation, not a sufficient one: independent 2026 work shows it can suppress unconditional emergent misalignment while leaving context-triggered misalignment that standard evaluations miss.
- C017: Reasoning-RL evaluation requires contamination audits: the AAAI 2026 replication shows spurious-reward gains vanish on clean generated arithmetic, and RL-MIA supplies a benchmark plus detector for RL-phase contamination.
- C018: VLA RL is an active 2026 lane with four adaptation patterns (residual-RL data generation and distillation, online on-robot fine-tuning, visual-robustness PPO objectives, simulator-based GRPO post-training); every performance number is a single-source author report. Education anchors: CS285 shows Spring 2026 material with no Fall 2026 offering displayed, the HF Deep RL course is live, and Spinning Up is maintenance-only.
- C019: World-model and test-time-compute work continued in 2026 (Waymo driving world model as vendor claim; Dreamer-CDP, behavior-consistency world models, adaptive TTC allocation, compute-aligned training, TTC scaling-law analysis as preprints); none overturns the finding that no single test-time-scaling strategy universally dominates.

## Related

- [[wiki/sources/_index|Sources Hub]]
- [[Source Manifest Guide]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Best Practices Kernel]]
- [[dashboard|Dashboard]]
- [[wiki/concepts/_index|Concepts Hub]]

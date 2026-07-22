---
type: "source"
title: "Research Pack 2026-07-22"
created: "2026-07-22"
updated: "2026-07-22"
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

# Research Pack 2026-07-22

Master source pack for the Reinforcement Learning Brain, rendered from `references/source-ledger.json` (70 sources, research pass 2026-07-22). Every entry carries a publication date, retrieval date, refresh-due date, and claim links. Regenerate with `python3 scripts/render_research_pack.py` after each research pass.

## Theme Notes

- [[Classic RL Foundations Sources|Classic RL Foundations]]
- [[Deep RL Algorithms Sources|Deep RL Algorithms]]
- [[LLM Post-Training and Preference Optimization Sources|LLM Post-Training and Preference Optimization]]
- [[Evaluation and Reproducibility Sources|Evaluation and Reproducibility]]
- [[Tooling and Engineering Practice Sources|Tooling and Engineering Practice]]

## Classic RL Foundations

### Asynchronous Methods for Deep Reinforcement Learning (Mnih et al., A3C)

- URL: https://arxiv.org/abs/1602.01783
- Published: 2016-02-04 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: a3c-asynchronous-actor-critic, parallel-actors-replace-replay

### Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm (Silver et al., AlphaZero)

- URL: https://arxiv.org/abs/1712.01815
- Published: 2017-12-05 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: alphazero-self-play-mcts, general-game-mastery-without-domain-knowledge

### Distributed Prioritized Experience Replay

- URL: https://arxiv.org/abs/1803.00933
- Published: 2018-03-02 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: distributed-rl-throughput

### Berkeley CS285: Deep Reinforcement Learning (Levine, Spring 2026)

- URL: https://rail.eecs.berkeley.edu/deeprlcourse/
- Published: 2026-01-19 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: official | Confidence: evidence-based
- Supports claims: graduate-level-drl-syllabus, offline-rl-and-model-based-lectures

### Conservative Q-Learning for Offline Reinforcement Learning (Kumar et al., CQL)

- URL: https://arxiv.org/abs/2006.04779
- Published: 2020-06-08 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: cql-conservative-value-lower-bound, offline-rl-distribution-shift-mitigation

### David Silver: UCL Course on Reinforcement Learning (COMPM050, 2015)

- URL: https://davidstarsilver.wordpress.com/teaching/
- Published: 2015-01-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: official | Confidence: evidence-based
- Supports claims: bellman-equation-lecture-treatment, model-free-prediction-and-control

### Playing Atari with Deep Reinforcement Learning (Mnih et al., DQN)

- URL: https://arxiv.org/abs/1312.5602
- Published: 2013-12-19 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: dqn-experience-replay, dqn-pixels-to-q-values

### Human-level control through deep reinforcement learning (Mnih et al., Nature)

- URL: https://www.nature.com/articles/nature14236
- Published: 2015-02-25 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: dqn-target-network-stabilization, human-level-atari-benchmark

### Deep Recurrent Q-Learning for Partially Observable MDPs

- URL: https://arxiv.org/abs/1507.06527
- Published: 2015-07-23 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: pomdp-belief-states

### High-Dimensional Continuous Control Using Generalized Advantage Estimation (Schulman et al.)

- URL: https://arxiv.org/abs/1506.02438
- Published: 2015-06-08 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: gae-lambda-bias-variance-tradeoff, advantage-estimation-for-policy-gradients

### Hugging Face Deep Reinforcement Learning Course

- URL: https://huggingface.co/learn/deep-rl-course/unit0/introduction
- Published: 2022-05-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: official | Confidence: practitioner
- Supports claims: hands-on-drl-training-workflow, unit-based-rl-learning-path

### OpenAI Spinning Up in Deep RL

- URL: https://spinningup.openai.com/en/latest/
- Published: 2018-11-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: official | Confidence: evidence-based
- Supports claims: policy-gradient-derivation-walkthrough, algorithm-family-taxonomy

### Policy Gradient Methods for Reinforcement Learning with Function Approximation (Sutton et al., NeurIPS 1999)

- URL: https://papers.nips.cc/paper_files/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html
- Published: 1999-12-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: policy-gradient-theorem-statement, reinforce-baseline-variance-reduction

### Distributional Reinforcement Learning with Quantile Regression

- URL: https://arxiv.org/abs/1710.10044
- Published: 2017-10-27 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: distributional-return-learning

### Rainbow: Combining Improvements in Deep Reinforcement Learning (Hessel et al.)

- URL: https://arxiv.org/abs/1710.02298
- Published: 2017-10-06 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: rainbow-dqn-extension-ablations, distributional-and-prioritized-replay-gains

### Reinforcement Learning: An Introduction, 2nd Edition (Sutton and Barto, official book page)

- URL: http://incompleteideas.net/book/the-book-2nd.html
- Published: 2018-01-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: official | Confidence: evidence-based
- Supports claims: mdp-value-iteration-foundations, td-learning-vs-monte-carlo, on-policy-vs-off-policy-definitions

### Trust Region Policy Optimization (Schulman et al.)

- URL: https://arxiv.org/abs/1502.05477
- Published: 2015-02-19 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: trpo-kl-constrained-updates, monotonic-improvement-guarantee

## Deep RL Algorithms

### A Distributional Perspective on Reinforcement Learning

- URL: https://arxiv.org/abs/1707.06887
- Published: 2017-07-21 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: distributional-return-learning

### Constrained Policy Optimization

- URL: https://arxiv.org/abs/1705.10528
- Published: 2017-05-30 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: cmdp-constrained-optimization

### Continuous control with deep reinforcement learning (Lillicrap et al., DDPG)

- URL: https://arxiv.org/abs/1509.02971
- Published: 2015-09-09 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: ddpg-deterministic-policy-gradient, continuous-action-off-policy-control

### Distributional Reinforcement Learning (Bellemare, Dabney, Rowland; MIT Press)

- URL: https://www.distributional-rl.org/
- Published: 2023-05-30 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: distributional-return-learning

### Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World

- URL: https://arxiv.org/abs/1703.06907
- Published: 2017-03-20 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: sim-to-real-gap

### Mastering Diverse Domains through World Models (DreamerV3; also published in Nature, 2025)

- URL: https://arxiv.org/abs/2301.04104
- Published: 2023-01-10 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: dreamer-latent-imagination

### Generative Adversarial Imitation Learning (Ho and Ermon, GAIL)

- URL: https://arxiv.org/abs/1606.03476
- Published: 2016-06-10 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: gail-adversarial-imitation-objective, imitation-without-reward-recovery

### Genie 3: A new frontier for world models

- URL: https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/
- Published: 2025-08-05 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: vendor | Confidence: practitioner
- Supports claims: interactive-world-generation

### IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures

- URL: https://arxiv.org/abs/1802.01561
- Published: 2018-02-05 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: impala-vtrace-off-policy

### Planning and Acting in Partially Observable Stochastic Domains

- URL: https://people.csail.mit.edu/lpk/papers/aij98-pomdp.pdf
- Published: 1998-05-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: pomdp-belief-states

### When to Trust Your Model: Model-Based Policy Optimization (Janner et al., MBPO)

- URL: https://arxiv.org/abs/1906.08253
- Published: 2019-06-19 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: mbpo-short-model-rollouts, dyna-style-model-usage-tradeoffs

### A Tutorial on Meta-Reinforcement Learning

- URL: https://arxiv.org/abs/2301.08028
- Published: 2023-01-19 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: meta-rl-adaptation

### Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model (Schrittwieser et al., MuZero)

- URL: https://arxiv.org/abs/1911.08265
- Published: 2019-11-19 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: muzero-learned-dynamics-planning, model-based-search-without-rules

### OmniSafe: An Infrastructure for Accelerating Safe Reinforcement Learning Research

- URL: https://arxiv.org/abs/2305.09304
- Published: 2023-05-16 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: safe-rl-tooling

### Proximal Policy Optimization Algorithms (Schulman et al.)

- URL: https://arxiv.org/abs/1707.06347
- Published: 2017-07-20 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: ppo-clipping-mechanism, ppo-vs-trpo-simplicity

### The Reality Gap in Robotics: Challenges, Solutions, and Best Practices

- URL: https://arxiv.org/abs/2510.20808
- Published: 2025-10-23 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: sim-to-real-gap

### RL^2: Fast Reinforcement Learning via Slow Reinforcement Learning

- URL: https://arxiv.org/abs/1611.02779
- Published: 2016-11-09 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: meta-rl-adaptation

### Exploration by Random Network Distillation (Burda et al., RND)

- URL: https://arxiv.org/abs/1810.12894
- Published: 2018-10-30 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: rnd-prediction-error-exploration-bonus, hard-exploration-montezuma-progress

### Soft Actor-Critic: Off-Policy Maximum Entropy Deep RL with a Stochastic Actor (Haarnoja et al.)

- URL: https://arxiv.org/abs/1801.01290
- Published: 2018-01-04 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: sac-maximum-entropy-objective, sac-sample-efficiency-continuous-control

### Benchmarking Safe Exploration in Deep Reinforcement Learning (Safety Gym)

- URL: https://cdn.openai.com/safexp-short.pdf
- Published: 2019-11-21 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: vendor | Confidence: evidence-based
- Supports claims: cmdp-constrained-optimization

### SEED RL: Scalable and Efficient Deep-RL with Accelerated Central Inference

- URL: https://arxiv.org/abs/1910.06591
- Published: 2019-10-15 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: distributed-rl-throughput

### SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning

- URL: https://arxiv.org/abs/2509.09674
- Published: 2025-09-11 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: vla-rl-scaling

### Addressing Function Approximation Error in Actor-Critic Methods (Fujimoto et al., TD3)

- URL: https://arxiv.org/abs/1802.09477
- Published: 2018-02-26 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: td3-twin-critics-clipped-double-q, delayed-policy-updates-target-smoothing

### World Models

- URL: https://arxiv.org/abs/1803.10122
- Published: 2018-03-27 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: dreamer-latent-imagination

## LLM Post-Training and Preference Optimization

### The Landscape of Agentic Reinforcement Learning for LLMs: A Survey

- URL: https://arxiv.org/abs/2509.02547
- Published: 2025-09-02 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: agentic-rl-formulation

### The Art of Scaling Test-Time Compute for Large Language Models

- URL: https://arxiv.org/abs/2512.02008
- Published: 2025-12-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: test-time-compute-scaling

### Constitutional AI: Harmlessness from AI Feedback (Bai et al., Anthropic)

- URL: https://arxiv.org/abs/2212.08073
- Published: 2022-12-15 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: constitutional-ai-self-critique-loop, rl-from-ai-feedback-preferences

### DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

- URL: https://arxiv.org/abs/2501.12948
- Published: 2025-01-22 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: pure-rl-reasoning-emergence, r1-zero-no-sft-cold-start

### Direct Preference Optimization: Your Language Model is Secretly a Reward Model (Rafailov et al.)

- URL: https://arxiv.org/abs/2305.18290
- Published: 2023-05-29 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: dpo-closed-form-preference-objective, dpo-vs-rlhf-tradeoffs

### DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models (introduces GRPO)

- URL: https://arxiv.org/abs/2402.03300
- Published: 2024-02-05 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: grpo-group-relative-baseline, critic-free-policy-optimization

### Training language models to follow instructions with human feedback (Ouyang et al., InstructGPT)

- URL: https://arxiv.org/abs/2203.02155
- Published: 2022-03-04 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: rlhf-three-stage-pipeline, small-aligned-model-beats-larger-base

### KTO: Model Alignment as Prospect Theoretic Optimization (Ethayarajh et al.)

- URL: https://arxiv.org/abs/2402.01306
- Published: 2024-02-02 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: kto-binary-signal-alignment, prospect-theory-loss-design

### MUA-RL: Multi-turn User-interacting Agent Reinforcement Learning for agentic tool use

- URL: https://arxiv.org/abs/2508.18669
- Published: 2025-08-26 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: multi-turn-agent-rl

### ORPO: Monolithic Preference Optimization without Reference Model (Hong et al.)

- URL: https://arxiv.org/abs/2403.07691
- Published: 2024-03-12 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: orpo-reference-free-alignment, single-stage-sft-plus-preference

### A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models

- URL: https://arxiv.org/abs/2510.08049
- Published: 2025-10-09 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: prm-vs-orm

### The Lessons of Developing Process Reward Models in Mathematical Reasoning

- URL: https://arxiv.org/abs/2501.07301
- Published: 2025-01-13 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: prm-vs-orm

### RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback (Lee et al.)

- URL: https://arxiv.org/abs/2309.00267
- Published: 2023-09-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: rlaif-matches-rlhf-quality, ai-preference-labeling-scalability

### Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning

- URL: https://arxiv.org/abs/2503.09516
- Published: 2025-03-12 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: rl-tool-use-training

### Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters

- URL: https://arxiv.org/abs/2408.03314
- Published: 2024-08-06 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: test-time-compute-scaling

### Spurious Rewards: Rethinking Training Signals in RLVR (Shao et al.)

- URL: https://arxiv.org/abs/2506.10947
- Published: 2025-06-12 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: rlvr-spurious-reward-gains-some-models, rlvr-signal-validation-caveats

### Tulu 3: Pushing Frontiers in Open Language Model Post-Training (introduces RLVR)

- URL: https://arxiv.org/abs/2411.15124
- Published: 2024-11-22 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: rlvr-verifiable-rewards-definition, open-post-training-recipe

## Evaluation and Reproducibility

### Deep Reinforcement Learning that Matters (Henderson et al.)

- URL: https://arxiv.org/abs/1709.06560
- Published: 2017-09-19 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: drl-reproducibility-seed-variance, hyperparameter-sensitivity-reporting

### Leveraging Procedural Generation to Benchmark Reinforcement Learning

- URL: https://arxiv.org/abs/1912.01588
- Published: 2019-12-03 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: procgen-generalization

### Deep Reinforcement Learning at the Edge of the Statistical Precipice (Agarwal et al., rliable)

- URL: https://arxiv.org/abs/2108.13264
- Published: 2021-08-30 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: primary | Confidence: evidence-based
- Supports claims: interquartile-mean-evaluation, few-run-uncertainty-reporting

## Tooling and Engineering Practice

### Natural emergent misalignment from reward hacking in production RL (Anthropic)

- URL: https://www.anthropic.com/research/emergent-misalignment-reward-hacking
- Published: 2025-11-21 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: vendor | Confidence: evidence-based
- Supports claims: reward-hacking-generalizes-to-misalignment, inoculation-prompting-mitigation

### CleanRL Documentation

- URL: https://docs.cleanrl.dev/
- Published: 2022-01-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: official | Confidence: evidence-based
- Supports claims: single-file-rl-implementations, implementation-detail-transparency

### Specification gaming: the flip side of AI ingenuity (DeepMind blog)

- URL: https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/
- Published: 2020-04-21 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: vendor | Confidence: evidence-based
- Supports claims: specification-gaming-examples, reward-misspecification-failure-modes

### Gymnasium Documentation (Farama Foundation)

- URL: https://gymnasium.farama.org/
- Published: 2022-10-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: official | Confidence: evidence-based
- Supports claims: gymnasium-env-api-standard, gym-to-gymnasium-migration

### OpenRLHF GitHub Repository

- URL: https://github.com/OpenRLHF/OpenRLHF
- Published: 2024-05-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: vendor | Confidence: evidence-based
- Supports claims: openrlhf-ray-vllm-distributed-rlhf, ppo-reinforce-plus-plus-grpo-support

### RLlib Documentation (Ray)

- URL: https://docs.ray.io/en/latest/rllib/index.html
- Published: 2018-07-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: official | Confidence: evidence-based
- Supports claims: rllib-scalable-distributed-rl, production-rl-workloads

### Stable-Baselines3 Documentation

- URL: https://stable-baselines3.readthedocs.io/en/master/
- Published: 2021-01-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: official | Confidence: evidence-based
- Supports claims: sb3-reliable-algorithm-implementations, sb3-supported-algorithm-matrix

### TRL Documentation (Hugging Face Transformer Reinforcement Learning)

- URL: https://huggingface.co/docs/trl/index
- Published: 2026-03-27 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: official | Confidence: evidence-based
- Supports claims: trl-trainer-taxonomy, grpo-dpo-kto-trainer-availability

### verl Documentation (HybridFlow RL training framework for LLMs)

- URL: https://verl.readthedocs.io/en/latest/
- Published: 2024-09-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: official | Confidence: evidence-based
- Supports claims: verl-hybrid-controller-programming-model, llm-rl-post-training-infra

## Ecosystem Snapshot

Version and maintenance evidence from `references/current-requirements.md` and `references/market-research.md`, retrieved on the pack date:

- https://pypi.org/project/gymnasium/ (retrieved 2026-07-22, see references/current-requirements.md)
- https://github.com/DLR-RM/stable-baselines3/releases (retrieved 2026-07-22, see references/current-requirements.md)
- https://pypi.org/project/trl/ (retrieved 2026-07-22, see references/current-requirements.md)
- https://pypi.org/project/cleanrl/ (retrieved 2026-07-22, see references/current-requirements.md)
- https://github.com/volcengine/verl (retrieved 2026-07-22, see references/current-requirements.md)
- https://pypi.org/project/openrlhf/ (retrieved 2026-07-22, see references/current-requirements.md)
- https://huggingface.co/learn/deep-rl-course/en/unit0/introduction (retrieved 2026-07-22, see references/current-requirements.md)
- https://www.deepmind.com/learning-resources/reinforcement-learning-lecture-series-2021 (retrieved 2026-07-22, see references/current-requirements.md)
- https://arxiv.org/abs/2503.14476 (retrieved 2026-07-22, see references/current-requirements.md)
- https://www.turingpost.com/p/reasoning-rl-in-2026 (retrieved 2026-07-22, see references/current-requirements.md)
- https://pypi.org/pypi/gymnasium/json (retrieved 2026-07-22, see references/market-research.md)
- https://pypi.org/pypi/stable-baselines3/json (retrieved 2026-07-22, see references/market-research.md)
- https://pypi.org/pypi/trl/json (retrieved 2026-07-22, see references/market-research.md)
- https://pypi.org/pypi/ray/json (retrieved 2026-07-22, see references/market-research.md)
- https://pypi.org/pypi/cleanrl/json (retrieved 2026-07-22, see references/market-research.md)
- https://api.github.com/repos/vwxyzjn/cleanrl (retrieved 2026-07-22, see references/market-research.md)
- https://pypi.org/pypi/verl/json (retrieved 2026-07-22, see references/market-research.md)
- https://api.github.com/repos/volcengine/verl (retrieved 2026-07-22, see references/market-research.md)
- https://pypi.org/pypi/openrlhf/json (retrieved 2026-07-22, see references/market-research.md)
- https://github.com/openai/spinningup (retrieved 2026-07-22, see references/market-research.md)
- https://github.com/huggingface/deep-rl-class (retrieved 2026-07-22, see references/market-research.md)
- https://api.github.com/repos/aikorea/awesome-rl (retrieved 2026-07-22, see references/market-research.md)
- https://llm-stats.com/blog/research/post-training-techniques-2026 (retrieved 2026-07-22, see references/market-research.md)
- https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond (retrieved 2026-07-22, see references/market-research.md)

## Claim Coverage

Claims resolved this pass (see `references/claim-ledger.md`):

- C001: DPO removes the reward-model and RL loop and matched or beat PPO-based RLHF on the summarization and dialogue tasks tested in the DPO paper; it is not shown superior for long-horizon reasoning, where open post-training practice has shifted toward critic-free RL on verifiable rewards (GRPO family); the extent of that dominance is tracked as contested in C003.
- C002: The reproducibility pitfalls that most often invalidate deep RL comparisons are small seed counts, selective reporting, unequal tuning budgets, and point estimates without interval statistics; interquartile mean with stratified bootstrap intervals remedies the point-estimate problem specifically, while selective reporting and unequal tuning budgets require preregistered protocols and matched budgets.
- C003: The current highest-risk state-of-the-art claim is that RL with verifiable rewards plus GRPO-family methods is the dominant post-training paradigm for reasoning models; the mechanism is primary-sourced, the dominance claim is secondary-sourced and ages monthly.
- C004: Library-version and maintenance-status claims are resolved by API-level primary sources: PyPI JSON for versions (TRL 1.9.0 on 2026-07-21, Gymnasium 1.3.0, SB3 2.9.0), repository README for maintenance (Spinning Up maintenance mode).
- C005: The algorithm selection guide deliverable is grounded by the 24 topic dossiers under references/topics/, whose Primary Sources cite original papers verified against arXiv listings on 2026-07-22; references/canon/ holds the 43 generator-maintained per-source capture notes.
- C006: RLVR results carry a live caveat: on some model families, RLVR improved math reasoning even with random or spurious rewards, so reward-attribution claims need per-model verification.
- C007: Reward hacking in production RL can generalize to broader misalignment (alignment faking, sabotage), with inoculation prompting proposed as mitigation.
- C008: CleanRL must be consumed from its GitHub repository, not PyPI: the PyPI package is frozen at 1.2.0 (2023) while the repository remains active.

## Related

- [[wiki/sources/_index|Sources Hub]]
- [[Source Manifest Guide]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Best Practices Kernel]]
- [[dashboard|Dashboard]]
- [[wiki/concepts/_index|Concepts Hub]]

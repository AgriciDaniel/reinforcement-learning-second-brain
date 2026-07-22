---
type: "canon"
title: "029. POMDPs and partial observability"
created: "2026-07-22"
updated: "2026-07-22"
status: "active"
---

# 029. POMDPs and partial observability

Ledger: 029 | target: POMDPs and partial observability | confidence: evidence-based | fold: [[POMDPs and partial observability]] | status: active.

## Core Thesis

A partially observable Markov decision process, or POMDP, separates the environment's latent Markov state from the observation available to the agent. Optimal action can therefore depend on history rather than on the current observation alone. [evidence-based]

A belief state is a posterior distribution over latent states conditioned on action-observation history. With a known model it supplies a sufficient statistic for control, but learned memories are only approximations to that ideal. [evidence-based]

Frame stacking, recurrence, external memory, and asymmetric actor-critic training address different parts of partial observability; none guarantees recovery of the true hidden state. [evidence-based]

## How It Works

A POMDP specifies latent states, actions, state transitions, rewards, observations, an observation process, and a horizon or discount. The latent state is Markov even when a single observation is not. [evidence-based]

After an action, the environment transitions to a new hidden state and emits an observation. Distinct latent states can produce the same observation even when they require different actions, a condition called perceptual aliasing. [evidence-based]

A memoryless policy cannot distinguish histories that end in the same observation. A history-dependent policy can condition on earlier observations, actions, rewards, and termination signals to infer missing information. [evidence-based]

For a known model, Bayesian filtering updates the belief by predicting the next-state distribution under the chosen action and conditioning that prediction on the new observation. [evidence-based]

The belief converts the problem into a fully observed belief-state MDP under the model assumptions. Its state space is continuous even for a finite latent-state POMDP, and exact planning can become computationally expensive. [evidence-based]

Most deep RL agents do not know the transition and observation models. Their recurrent hidden states or external memories are learned representations of history rather than explicit, calibrated probability distributions over latent state. [evidence-based]

Frame stacking concatenates a fixed window of recent observations. It can reveal short-term motion or delays, but cannot resolve dependencies longer than the window or facts that were never observed. [evidence-based]

A recurrent policy updates memory from its previous hidden state and new inputs. Deep Recurrent Q-Learning replaces a feed-forward component of DQN with an LSTM so action values can depend on a learned summary of earlier frames. [evidence-based]

Training recurrent agents from replay requires contiguous sequences, correct episode boundaries, and an initialization or burn-in scheme for hidden state. Isolated transitions discard the context the network is supposed to use. [practitioner]

An LLM agent faces partial observability when user intent, application state, tool side effects, external changes, or future responses are not fully represented in its visible transcript. A long context window cannot reveal state that the environment never exposes. [evidence-based]

Conversation, retrieval, and tool history can support an approximate belief, while truncation, lossy summaries, missing events, and stale observations can make similar visible contexts correspond to different situations. [practitioner]

Asymmetric actor-critic training gives the deployable actor partial observations while allowing the training critic to use privileged state. This can improve target estimation in simulation, but the actor still has the same information constraint at deployment. [evidence-based]

A state-only critic is not automatically unbiased for every history-based policy under partial observability. The value definition and conditioning variables must preserve the intended policy-gradient estimator. [evidence-based]

## Key Principles

- Partial observability is an information problem because distinct hidden states can produce the same visible input. [evidence-based]
- The Markov property belongs to the selected latent state, not necessarily to a raw observation or short observation window. [evidence-based]
- A model-based belief state is sufficient under the POMDP assumptions, while a neural hidden vector is not automatically a calibrated belief. [evidence-based]
- Frame stacking addresses bounded recent-history dependence and is not a general solution to hidden state. [evidence-based]
- Recurrent policies require sequence sampling, reset semantics, and unroll lengths aligned with the dependencies they must learn. [evidence-based]
- Privileged critic inputs can assist training without changing the actor interface, but their benefits and estimator validity are design-dependent. [evidence-based]
- Agentic LLM interaction remains partially observed when the transcript omits consequential user, tool, or world state. [evidence-based]
- Claims that recurrence or asymmetric critics universally outperform simpler memory baselines exceed the cited task-specific evidence. [contested]

## Best Practices

- Write down the latent state, observation function, hidden variables, action-observation timing, and deployment information before choosing an architecture. [practitioner]
- Start with memoryless and fixed-window baselines, then add recurrence when controlled tests demonstrate history dependence. [practitioner]
- Sample contiguous replay sequences, preserve episode boundaries, and reset recurrent state only at true environment resets. [practitioner]
- Use a documented burn-in prefix or stored recurrent state before scoring a training unroll. [practitioner]
- Include previous actions, rewards, termination flags, and tool results in memory updates when they carry otherwise missing state information. [practitioner]
- Test observation dropout, delay, corruption, longer occlusion, context truncation, and changed history length. [practitioner]
- Keep privileged fields confined to the critic and add deployment-path tests that fail if the actor reads them. [practitioner]
- Report performance by observability and memory-demand slice with multiple seeds and matched model capacity. [evidence-based]

## Primary Sources

- Leslie Pack Kaelbling, Michael L. Littman, and Anthony R. Cassandra, 1998, "Planning and acting in partially observable stochastic domains," Artificial Intelligence 101(1-2), 99-134, [DOI record](https://doi.org/10.1016/S0004-3702(98)00023-X).
- Matthew Hausknecht and Peter Stone, 2015, "Deep Recurrent Q-Learning for Partially Observable MDPs," arXiv:1507.06527, [paper](https://arxiv.org/abs/1507.06527).
- Lerrel Pinto, Marcin Andrychowicz, Peter Welinder, Wojciech Zaremba, and Pieter Abbeel, 2017, "Asymmetric Actor Critic for Image-Based Robot Learning," arXiv:1710.06542, [paper](https://arxiv.org/abs/1710.06542).
- Andrea Baisero and Christopher Amato, 2021, "Unbiased Asymmetric Reinforcement Learning under Partial Observability," arXiv:2105.11674, [paper](https://arxiv.org/abs/2105.11674).

## Evidence Caveats

- The standard formalism assumes a suitable latent Markov state and stationary transition and observation processes, which may only approximate open-world systems. [evidence-based]
- Exact belief updates require a known model and tractable inference, conditions that usually fail in high-dimensional learned environments. [evidence-based]
- A recurrent hidden vector can encode useful history without representing the true state, a sufficient statistic, or calibrated uncertainty. [evidence-based]
- Truncated backpropagation, finite context, replay initialization, and sparse rewards can prevent learning dependencies the architecture could represent. [evidence-based]
- DRQN evidence comes from standard and artificially flickering Atari settings, so its comparison does not establish general superiority over stacking. [contested]
- Asymmetric actor-critic results depend on selected simulations, privileged signals, value definitions, and actor observations. [contested]
- Real LLM tool environments may be nonstationary or multi-agent in addition to being partially observable, which exceeds a simple fixed POMDP model. [practitioner]

## Brain Hooks

- Folded concept: [[POMDPs and partial observability]]
- Related canon: [[Markov decision processes and the RL problem formulation]]
- Related canon: [[Deep Q-Networks and value-based deep RL (DQN, Rainbow)]]
- Related canon: [[Actor-critic methods (A2C A3C, GAE)]]
- Related canon: [[Agentic multi-turn RL for LLM agents]]
- Related canon: [[World models and latent imagination (Dreamer, Genie)]]
- Related canon: [[Multi-agent RL]]
- Related canon: [[Model-based RL and planning (Dyna, MBPO, AlphaZero, MuZero)]]
- Related canon: [[Hierarchical RL and options]]
- Related canon: [[Evaluation, benchmarks, and reproducibility in deep RL]]
- Source intake path: [[Source Intake Workflow]]
- Verification path: [[Claim Verification Flow]]

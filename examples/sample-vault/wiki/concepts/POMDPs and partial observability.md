---
type: "concept"
title: "POMDPs and partial observability"
domain: "reinforcement learning: fundamentals, deep RL, RLHF/RLAIF and preference optimization, evaluation, tooling, and applied best practices"
status: "active"
created: "2026-07-22"
updated: "2026-07-22"
tags:
  - "#domain/reinforcement-learning-fundamentals-deep-rl-rlhf-rlaif-and-prefe"
  - "#type/concept"
  - "#confidence/evidence-based"
confidence: "evidence-based"
related:
  - "[[Index]]"
  - "[[CONVENTIONS]]"
  - "[[Best Practices Kernel]]"
  - "[[Source Intake Workflow]]"
  - "[[Research Refresh Workflow]]"
  - "[[Synthesis Workflow]]"
  - "[[wiki/concepts/_index|Concepts Hub]]"
  - "[[Dashboard]]"
  - "[[Tag Taxonomy]]"
  - "[[Claim Verification Flow]]"
  - "[[Reporting Workflow]]"
  - "[[Source Manifest Guide]]"
  - "[[Health Scorecard]]"
  - "[[Action Roadmap]]"
  - "[[Weekly Report]]"
  - "[[Approval Queue]]"
  - "[[wiki/flows/_index|Flows Hub]]"
  - "[[wiki/sources/_index|Sources Hub]]"
  - "[[wiki/decisions/_index|Decisions Hub]]"
  - "[[wiki/deliverables/_index|Deliverables Hub]]"
  - "[[wiki/reports/_index|Reports Hub]]"
  - "[[wiki/questions/_index|Questions Hub]]"
  - "[[wiki/gaps/_index|Gaps Hub]]"
  - "[[wiki/experiments/_index|Experiments Hub]]"
source_urls:
  - "https://doi.org/10.1016/S0004-3702(98"
  - "https://arxiv.org/abs/1507.06527"
  - "https://arxiv.org/abs/1710.06542"
  - "https://arxiv.org/abs/2105.11674"
---

# POMDPs and partial observability

Confidence tag: evidence-based. Folded from canon `029-pomdps-and-partial-observability.md` on the date in `updated`.

## Sourced Takeaways

A partially observable Markov decision process, or POMDP, separates the environment's latent Markov state from the observation available to the agent. Optimal action can therefore depend on history rather than on the current observation alone. [evidence-based]

A belief state is a posterior distribution over latent states conditioned on action-observation history. With a known model it supplies a sufficient statistic for control, but learned memories are only approximations to that ideal. [evidence-based]

Frame stacking, recurrence, external memory, and asymmetric actor-critic training address different parts of partial observability; none guarantees recovery of the true hidden state. [evidence-based]

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

## Evidence Caveats

- The standard formalism assumes a suitable latent Markov state and stationary transition and observation processes, which may only approximate open-world systems. [evidence-based]
- Exact belief updates require a known model and tractable inference, conditions that usually fail in high-dimensional learned environments. [evidence-based]
- A recurrent hidden vector can encode useful history without representing the true state, a sufficient statistic, or calibrated uncertainty. [evidence-based]
- Truncated backpropagation, finite context, replay initialization, and sparse rewards can prevent learning dependencies the architecture could represent. [evidence-based]
- DRQN evidence comes from standard and artificially flickering Atari settings, so its comparison does not establish general superiority over stacking. [contested]
- Asymmetric actor-critic results depend on selected simulations, privileged signals, value definitions, and actor observations. [contested]
- Real LLM tool environments may be nonstationary or multi-agent in addition to being partially observable, which exceeds a simple fixed POMDP model. [practitioner]

## Sources

- Canon evidence file: `references/topics/029-pomdps-and-partial-observability.md`
- Leslie Pack Kaelbling, Michael L. Littman, and Anthony R. Cassandra, 1998, "Planning and acting in partially observable stochastic domains," Artificial Intelligence 101(1-2), 99-134, [DOI record](https://doi.org/10.1016/S0004-3702(98)00023-X).
- Matthew Hausknecht and Peter Stone, 2015, "Deep Recurrent Q-Learning for Partially Observable MDPs," arXiv:1507.06527, [paper](https://arxiv.org/abs/1507.06527).
- Lerrel Pinto, Marcin Andrychowicz, Peter Welinder, Wojciech Zaremba, and Pieter Abbeel, 2017, "Asymmetric Actor Critic for Image-Based Robot Learning," arXiv:1710.06542, [paper](https://arxiv.org/abs/1710.06542).
- Andrea Baisero and Christopher Amato, 2021, "Unbiased Asymmetric Reinforcement Learning under Partial Observability," arXiv:2105.11674, [paper](https://arxiv.org/abs/2105.11674).
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]

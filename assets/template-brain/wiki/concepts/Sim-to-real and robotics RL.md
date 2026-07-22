---
type: "concept"
title: "Sim-to-real and robotics RL"
domain: "reinforcement learning"
status: "active"
created: "2026-07-22"
updated: "2026-07-22"
tags:
  - "#domain/reinforcement-learning"
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
  - "https://arxiv.org/abs/1703.06907"
  - "https://arxiv.org/abs/1710.06537"
  - "https://arxiv.org/abs/1810.05687"
  - "https://arxiv.org/abs/1801.08757"
  - "https://arxiv.org/abs/2403.03949"
  - "https://arxiv.org/abs/2509.09674"
  - "https://arxiv.org/abs/2510.20808"
---

# Sim-to-real and robotics RL

Confidence tag: evidence-based. Folded from canon `033-sim-to-real-and-robotics-rl.md` on the date in `updated`.

## Sourced Takeaways

Sim-to-real robot learning uses simulation to develop or refine a policy before physical deployment, while explicitly managing discrepancies in dynamics, sensing, actuation, and system design that form the reality gap. [evidence-based]

Transfer is an engineering and learning loop rather than a property conferred by simulation alone: the simulator distribution, real-world measurements, policy architecture, safety controls, and evaluation protocol jointly determine what can transfer. [evidence-based]

Domain randomization, system identification, real-to-sim-to-real reconstruction, and reinforcement learning fine-tuning of vision-language-action policies solve different parts of this loop; no cited evidence establishes one universally superior recipe across robots and tasks. [contested]

- A simulator is a task model with deliberate abstractions, not a ground-truth copy of the physical world. [evidence-based]
- Transfer depends on whether training variation covers the target conditions that materially affect policy behavior, not on visual realism alone. [evidence-based]
- Domain randomization trains robustness across a distribution, while system identification uses measurements to calibrate or infer a target model. [evidence-based]
- Real data can improve simulation without requiring unconstrained policy optimization on the robot. [practitioner]
- Structural model error cannot always be repaired by tuning the parameters of an inadequate simulator. [evidence-based]
- VLA reinforcement learning is closed-loop control: every action changes the next visual and proprioceptive observation. [evidence-based]
- A high simulated success rate is not evidence of physical safety or transfer until the policy is tested under a declared real-world protocol. [evidence-based]
- Claims that one sim-to-real method or VLA fine-tuning recipe is generally state of the art remain protocol-dependent and short-lived. [contested]

## Best Practices

- Write a gap inventory before training that covers dynamics, contacts, sensing, actuation, latency, low-level control, resets, safety mechanisms, and system design. [practitioner]
- Use measured hardware ranges and uncertainty where available, version every randomization distribution, and record the sampled parameters for each rollout. [practitioner]
- Validate system-identification trajectories for safe excitation and held-out predictive behavior before using fitted parameters to guide policy training. [practitioner]
- Combine calibrated nominal models with randomized residual uncertainty when both real measurements and substantial unmodeled variation are present. [practitioner]
- Start VLA RL from a policy with demonstrated task competence, inspect successful and failed trajectories, and keep reward components and termination causes separate. [practitioner]
- Stage deployment through offline replay, simulation stress tests, bounded hardware trials, and progressively broader operating conditions with explicit promotion criteria. [practitioner]
- Put physical interlocks, action projection, watchdogs, workspace limits, and emergency stopping outside the learned policy, then test them independently. [practitioner]
- Report simulation and real-world results separately with task definitions, hardware, controller stack, randomization, trial protocol, failures, interventions, and uncertainty. [evidence-based]
- Keep residual-RL data generation, online on-robot fine-tuning, visual-robustness objectives, and simulator-based GRPO post-training as separate VLA adaptation patterns with their own action representations, safety constraints, and evaluation protocols. [practitioner]
- Recheck education-source page state before using it as a schedule or maintenance claim, especially when no page-visible update date is provided. [practitioner]

## Evidence Caveats

- The domain-randomization demonstrations study particular perception and control tasks, simulators, robots, parameter ranges, and target conditions; they do not establish zero-shot transfer for arbitrary hardware. [evidence-based]
- Survey taxonomies organize a broad literature but do not by themselves provide controlled comparative evidence among domain randomization, system identification, adaptation, and real-to-sim methods. [evidence-based]
- System identification can fit observed trajectories while remaining wrong under contacts, loads, speeds, wear, or disturbances absent from the identification data. [evidence-based]
- Randomization ranges are design assumptions, and successful transfer does not prove that the learned policy will remain safe outside the tested support. [evidence-based]
- SimpleVLA-RL is a single technical report whose comparisons combine a specific VLA implementation, supervised initialization, reward, exploration changes, simulator assets, and evaluation protocol. [contested]
- Binary task success can conceal collisions, excessive force, unsafe shortcuts, intervention dependence, or fragile recovery behavior unless those outcomes are measured separately. [practitioner]
- A safety layer depends on its constraint model, state estimates, action authority, and runtime reliability; citing one does not turn physical exploration into a formal end-to-end safety guarantee. [evidence-based]
- PLD, EXPO-FT, PAIR-VLA, and Z-1 are distinct adaptation patterns with single-source method or performance evidence. Their reported benchmark and real-robot outcomes must remain protocol-specific and are not an independently replicated ranking. [contested]
- pi-star 0.6 is contextual 2025 evidence, Alpamayo is a workflow guide, and SPARR is adjacent non-VLA evidence; none should be misdated or treated as a directly comparable Apr-Jun 2026 VLA result. [evidence-based]
- The CS285 observation is a fetched landing-page state, not evidence that Berkeley will not offer Fall 2026. The Hugging Face course page exposes no update date, and Spinning Up's maintenance mode does not make it a current-library or current-benchmark authority. [evidence-based]

## Sources

- Canon evidence file: `references/topics/033-sim-to-real-and-robotics-rl.md`
- Josh Tobin, Rachel Fong, Alex Ray, Jonas Schneider, Wojciech Zaremba, and Pieter Abbeel, 2017, "Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World," arXiv:1703.06907, [paper](https://arxiv.org/abs/1703.06907).
- Xue Bin Peng, Marcin Andrychowicz, Wojciech Zaremba, and Pieter Abbeel, 2018, "Sim-to-Real Transfer of Robotic Control with Dynamics Randomization," arXiv:1710.06537, [paper](https://arxiv.org/abs/1710.06537).
- Yevgen Chebotar, Ankur Handa, Viktor Makoviychuk, Miles Macklin, Jan Issac, Nathan Ratliff, and Dieter Fox, 2019, "Closing the Sim-to-Real Loop: Adapting Simulation Randomization with Real World Experience," arXiv:1810.05687, [paper](https://arxiv.org/abs/1810.05687).
- Gal Dalal, Krishnamurthy Dvijotham, Matej Vecerik, Todd Hester, Cosmin Paduraru, and Yuval Tassa, 2018, "Safe Exploration in Continuous Action Spaces," arXiv:1801.08757, [paper](https://arxiv.org/abs/1801.08757).
- Marcel Torne, Anthony Simeonov, Zechu Li, April Chan, Tao Chen, Abhishek Gupta, and Pulkit Agrawal, 2024, "Reconciling Reality through Simulation: A Real-to-Sim-to-Real Approach for Robust Manipulation," arXiv:2403.03949, [paper](https://arxiv.org/abs/2403.03949).
- Haozhan Li et al., 2025, "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning," arXiv:2509.09674, [paper](https://arxiv.org/abs/2509.09674).
- Elie Aljalbout et al., 2025, "The Reality Gap in Robotics: Challenges, Solutions, and Best Practices," arXiv:2510.20808, [paper](https://arxiv.org/abs/2510.20808).
- "Self-Improving Vision-Language-Action Models with Data Generation via Residual RL," [UT Austin publication](https://rpl.cs.utexas.edu/publications/2026/04/01/xiao-iclr26-pld/), 2026-04-01. SINGLE-SOURCE for its method description.
- "EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models," [arXiv:2605.25477](https://arxiv.org/abs/2605.25477), 2026-05-25. SINGLE-SOURCE for author-reported results.
- "What to Ignore, What to React: Visually Robust RL Fine-Tuning of VLA Models," [arXiv:2605.13105](https://arxiv.org/abs/2605.13105), 2026-05-13. SINGLE-SOURCE for author-reported results.
- "Z-1: Efficient Reinforcement Learning for Vision-Language-Action Models," [arXiv:2606.31846](https://arxiv.org/abs/2606.31846), 2026-06-30. SINGLE-SOURCE for author-reported results.
- "pi-star 0.6," [arXiv:2511.14759](https://arxiv.org/abs/2511.14759), 2025-11-18; NVIDIA, [Alpamayo post-training guide](https://developer.nvidia.com/blog/how-to-post-train-autonomous-vehicle-models-in-closed-loop-with-nvidia-alpamayo/), 2026-05-31; and NVIDIA, [SPARR project page](https://research.nvidia.com/labs/srl/projects/sparr/), 2026. Context and workflow sources only.
- Berkeley, [CS 185/285 course page](https://rail.eecs.berkeley.edu/deeprlcourse/), Spring 2026 page state; Hugging Face, [Deep RL Course](https://huggingface.co/learn/deep-rl-course/unit0/introduction), live with no page-visible update date; and OpenAI, [Spinning Up](https://spinningup.openai.com/en/latest/), maintenance-only status from its [official README](https://github.com/openai/spinningup), retrieved 2026-07-22.
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]

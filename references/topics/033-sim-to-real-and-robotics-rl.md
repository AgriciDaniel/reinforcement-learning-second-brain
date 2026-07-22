---
type: "canon"
title: "033. Sim-to-real and robotics RL"
created: "2026-07-22"
updated: "2026-07-23"
status: "active"
---

# 033. Sim-to-real and robotics RL

Ledger: 033 | target: Sim-to-real and robotics RL | confidence: evidence-based | fold: [[Sim-to-real and robotics RL]] | status: active.

## Core Thesis

Sim-to-real robot learning uses simulation to develop or refine a policy before physical deployment, while explicitly managing discrepancies in dynamics, sensing, actuation, and system design that form the reality gap. [evidence-based]

Transfer is an engineering and learning loop rather than a property conferred by simulation alone: the simulator distribution, real-world measurements, policy architecture, safety controls, and evaluation protocol jointly determine what can transfer. [evidence-based]

Domain randomization, system identification, real-to-sim-to-real reconstruction, and reinforcement learning fine-tuning of vision-language-action policies solve different parts of this loop; no cited evidence establishes one universally superior recipe across robots and tasks. [contested]

## How It Works

A simulator exposes the policy to observations, actions, transitions, rewards, resets, and termination rules that approximate the physical task. Its interfaces should also represent control frequency, latency, sensor noise, actuator limits, and safety interventions that will exist on hardware. [practitioner]

The reality gap is the mismatch between simulated and physical environments. It can arise from visual appearance, geometry, contact and friction, mass and inertia, deformability, sensor characteristics, communication delays, low-level controllers, and mechanisms omitted from the simulator. [evidence-based]

Domain randomization samples training environments from a distribution over selected visual, physical, sensing, and actuation parameters. The goal is a policy that remains effective across variation broad enough to include relevant physical conditions. [evidence-based]

Tobin et al. demonstrated visual domain randomization by training on simulated images with varied rendering and transferring an object localizer into a robotic grasping setup. This is evidence for that task and perception pipeline, not a general transfer guarantee. [evidence-based]

Dynamics randomization applies the same idea to quantities such as mass, friction, damping, delays, and controller gains. A range that is too narrow can omit the target system, while an excessively broad or implausible range can make learning unnecessarily difficult. [practitioner]

System identification instead uses real input-output traces to estimate simulator parameters or dynamics. It aims to reduce mismatch around the measured system, but its result depends on excitation, sensor quality, parameter identifiability, operating regime, and whether the simulator contains the right model structure. [evidence-based]

The approaches are complementary: system identification can center or shape a plausible simulator distribution, and domain randomization can train robustness to residual uncertainty and drift around that estimate. Which allocation works better is task-dependent and must be evaluated on the target hardware. [contested]

Adaptive variants close the loop by collecting bounded real rollouts, comparing real and simulated behavior, updating the simulator parameter distribution, retraining the policy, and repeating under a fixed safety protocol. [evidence-based]

Real-to-sim starts from physical observations or trajectories to reconstruct geometry, appearance, object placement, sensor behavior, or dynamics in a digital environment. Training then occurs in the reconstructed and randomized simulator before the policy returns to the robot for staged validation. [evidence-based]

In a published real-to-sim-to-real example, RialTo constructs a digital twin from limited real data, transfers demonstrations into simulation, uses reinforcement learning there to robustify an imitation policy, and deploys the result back to the physical task. Its findings remain specific to the studied manipulation setup. [evidence-based]

A vision-language-action, or VLA, policy maps visual and proprioceptive observations plus a language instruction to robot actions or action chunks. Supervised pretraining and task demonstrations can provide an initial policy before reinforcement learning. [evidence-based]

SimpleVLA-RL samples closed-loop VLA trajectories in parallel simulation environments, assigns an outcome reward from task completion, and updates action-token probabilities with a group-relative policy objective after supervised fine-tuning. [evidence-based]

The paper reports that simulation-only RL fine-tuning improved its VLA baseline in its simulation suites and in a limited real-robot evaluation. Those comparative findings use the authors' models, tasks, randomization, and protocol and are not an independently reproduced general ranking. [contested]

Sparse task-completion rewards require the current policy to generate some successful rollouts. SimpleVLA-RL reports that outcome-only RL did not improve a starting policy with no task success in its studied setting, making initialization and exploration central design variables. [contested]

Real-world learning adds hazards that simulation does not reproduce. A deployment loop should place learned actions beneath independently tested limits, workspace boundaries, collision checks, rate and force limits, emergency stops, and a human-approved abort path. [practitioner]

Safety filters and low-level controllers also change the deployed transition dynamics. They should therefore be represented during simulation where feasible and logged as part of the real-world trajectory rather than treated as invisible infrastructure. [practitioner]

Evaluation should separate simulator return from physical task success and report real-world failures, constraint violations, safety interventions, recovery behavior, and performance across declared operating conditions. [practitioner]

### Apr-Jun 2026 VLA adaptation patterns

PLD describes residual-RL probing, distribution-aware hybrid rollout collection, and distillation back into a VLA generalist. This is a residual-RL data-generation and distillation pattern. [evidence-based]

EXPO-FT reports online reinforcement-learning fine-tuning of pretrained VLA policies on real manipulation tasks. Its real-robot outcomes are single-source author reports tied to its hardware, tasks, and protocol. [contested]

PAIR-VLA reports PPO fine-tuning with paired visual-invariance and sensitivity objectives for visual shifts. Its comparative gains remain author-reported and do not establish a generally preferred robustness objective. [contested]

Z-1 reports task-wise GRPO post-training of a pi-0.5-based flow VLA in RoboCasa. Its benchmark outcomes are single-source author reports, so simulator-based GRPO post-training is recorded as one adaptation pattern rather than a general ranking. [contested]

Physical Intelligence's pi-star 0.6 is relevant real-world VLA RL context, but its arXiv v1 date is 2025-11-18, not an Apr-Jun 2026 result. NVIDIA's Alpamayo material is a 2026 closed-loop VLA post-training workflow guide, while SPARR is adjacent non-VLA sim-to-real residual-RL evidence. [evidence-based]

### Education-source status

The fetched CS 185/285 landing page shows Spring 2026 material and no Fall 2026 offering text. The Hugging Face Deep RL Course is live with no page-visible update date. Spinning Up is maintenance-only and remains useful for fundamentals rather than current-library or current-benchmark guidance. [evidence-based]

## Key Principles

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

## Primary Sources

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

## Brain Hooks

- Folded concept: [[Sim-to-real and robotics RL]]
- Problem formulation under hidden physical state: [[POMDPs and partial observability]]
- Continuous robot control: [[Continuous control (DDPG, TD3, SAC)]]
- Learned simulators and planning: [[Model-based RL and planning (Dyna, MBPO, AlphaZero, MuZero)]]
- Learning from fixed robot data: [[Offline batch RL and conservatism]]
- Demonstration initialization: [[Imitation learning and inverse RL]]
- Safe physical interaction: [[Safe and constrained RL]]
- Reward and shortcut analysis: [[Reward design, reward hacking, and specification gaming]]
- Robust exploration: [[Exploration strategies and intrinsic motivation]]
- Transfer evaluation: [[Evaluation, benchmarks, and reproducibility in deep RL]]
- Run diagnosis: [[Debugging RL training runs in practice]]
- Source intake path: [[Source Intake Workflow]]
- Verification path: [[Claim Verification Flow]]

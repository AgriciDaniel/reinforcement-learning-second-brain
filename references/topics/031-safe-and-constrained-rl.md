---
type: "canon"
title: "031. Safe and constrained RL"
created: "2026-07-22"
updated: "2026-07-22"
status: "active"
---

# 031. Safe and constrained RL

Ledger: 031 | target: Safe and constrained RL | confidence: evidence-based | fold: [[Safe and constrained RL]] | status: active.

## Core Thesis

Safe and constrained reinforcement learning separates task reward from explicit cost, risk, or behavioral constraints instead of expecting one scalar reward to encode every requirement. [evidence-based]
A constrained Markov decision process, or CMDP, supports policies that maximize expected return subject to cost budgets, but expected constraints alone do not guarantee that every training or deployment trajectory is safe. [evidence-based]
Practical safety therefore combines objective design, constrained optimization, risk-sensitive evaluation, exploration controls, and independent enforcement where consequences demand it. [practitioner]
RLHF safety training can shape behavior through preferences or learned rewards, but it does not by itself provide the formal constraint guarantees assumed by CMDP or shielding methods. [evidence-based]

## How It Works

A CMDP augments an MDP with one or more cost signals and corresponding limits. The usual objective maximizes expected discounted reward while requiring each expected discounted cost to remain within its budget. [evidence-based]

A Lagrangian method introduces a nonnegative multiplier for each constraint and optimizes a reward-minus-penalized-cost objective. Policy parameters and multipliers are updated in coupled primal and dual steps so violations increase their effective penalty. [evidence-based]

An adaptive Lagrange multiplier responds to observed violations, while a fixed penalty requires the operator to choose the tradeoff in advance. The adaptive design is easier to add to common policy-gradient code, but it can oscillate or lag when estimates are noisy. [practitioner]

Constrained Policy Optimization, or CPO, derives a trust-region policy step with a local reward objective and local constraint approximations. Its analysis provides a bound used to motivate near-constraint satisfaction across updates under the paper's assumptions. [evidence-based]

CPO and Lagrangian methods encode constraints differently: CPO solves an approximate constrained update, while Lagrangian methods learn penalty multipliers through optimization. Neither design is universally preferable across tasks and implementations. [contested]

Safe exploration asks whether the behavior used to collect training data also respects safety requirements. Measuring only the final policy misses costs accumulated by earlier exploratory policies. [evidence-based]

Safety Gym formalizes benchmark tasks with separate reward and cost functions and evaluates task performance, final constraint satisfaction, and safety costs during training. Its simulated hazards are test instruments, not evidence of deployment safety. [evidence-based]

Risk-sensitive objectives change what part of the return or cost distribution matters. Conditional value at risk, or CVaR, can constrain the expected cost within a specified tail rather than only the overall mean. [evidence-based]

A shield uses a model and formal specification to identify unsafe actions before execution or to correct a proposed action that would violate the specification. Its protection is limited by the completeness of that model and specification. [evidence-based]

OmniSafe packages safe-RL algorithms and experiment infrastructure so implementations can be studied under shared interfaces. Library availability does not validate a method for a particular operational hazard. [evidence-based]

For RLHF or RLAIF, a safety preference model, rule-based signal, or constitutional critique can be one feedback channel. Hard operational limits still need explicit monitoring, access controls, or enforcement outside the learned policy where appropriate. [practitioner]

## Key Principles

- Reward and safety costs should remain separately observable even when an optimizer combines them internally. [evidence-based]
- Expected-cost feasibility can coexist with rare catastrophic trajectories, so tail and worst-case diagnostics matter. [evidence-based]
- A constraint threshold is a normative and operational choice, not a hyperparameter that optimization can justify on its own. [practitioner]
- Safety during learning and safety of the final policy are distinct evaluation targets. [evidence-based]
- Lagrangian multipliers are learned tradeoff prices, not proof that constraints will hold on every rollout. [evidence-based]
- A shield can block specified unsafe actions, but unspecified hazards remain outside its guarantee. [evidence-based]
- Reward hacking can affect cost functions, learned safety critics, and preference models as well as the primary reward. [evidence-based]
- Claims that one constrained optimizer is safest require matched tasks, budgets, implementation details, and uncertainty reporting. [contested]

## Best Practices

- Define each hazard, cost event, aggregation rule, time horizon, and threshold with a domain owner before training. [practitioner]
- Log raw reward and every raw cost channel separately from shaped rewards, penalties, and multiplier values. [practitioner]
- Evaluate cumulative training cost, final-policy feasibility, violation frequency, violation severity, and return under multiple seeds. [evidence-based]
- Stress-test tail behavior with targeted scenarios and report CVaR or another named risk statistic together with its confidence level. [practitioner]
- Start in a validated simulator or offline dataset, then gate any real-world exploration behind explicit review and rollback procedures. [practitioner]
- Unit-test shield interventions, fallback actions, model mismatch, delayed observations, and states for which no safe action is known. [practitioner]
- Sweep constraint thresholds and optimization settings to expose the reward-safety frontier instead of reporting a single operating point. [practitioner]
- Keep an independent evaluator and immutable incident traces so the learned policy cannot control all safety evidence. [practitioner]

## Primary Sources

- Joshua Achiam, David Held, Aviv Tamar, and Pieter Abbeel, 2017, "Constrained Policy Optimization," arXiv:1705.10528, [paper](https://arxiv.org/abs/1705.10528).
- Alex Ray, Joshua Achiam, and Dario Amodei, 2019, "Benchmarking Safe Exploration in Deep Reinforcement Learning," [Safety Gym paper](https://cdn.openai.com/safexp-short.pdf).
- Jiaming Ji et al., 2023, "OmniSafe: An Infrastructure for Accelerating Safe Reinforcement Learning Research," arXiv:2305.09304, [paper](https://arxiv.org/abs/2305.09304).
- Yinlam Chow, Mohammad Ghavamzadeh, Lucas Janson, and Marco Pavone, 2015, "Risk-Constrained Reinforcement Learning with Percentile Risk Criteria," arXiv:1512.01629, [paper](https://arxiv.org/abs/1512.01629).
- Mohammed Alshiekh, Roderick Bloem, Ruediger Ehlers, Bettina Könighofer, Scott Niekum, and Ufuk Topcu, 2017, "Safe Reinforcement Learning via Shielding," arXiv:1708.08611, [paper](https://arxiv.org/abs/1708.08611).

## Evidence Caveats

- CMDP feasibility is defined relative to chosen cost signals and budgets; omitted or misspecified hazards are not controlled. [evidence-based]
- Constraints in expectation allow individual episodes to exceed a cost limit, which may be unacceptable for irreversible harms. [evidence-based]
- CPO's theoretical statements depend on approximations and assumptions that finite-sample neural-network implementations do not satisfy exactly. [evidence-based]
- Lagrangian training can be sensitive to multiplier initialization, step sizes, estimator variance, and delayed cost feedback. [practitioner]
- CVaR estimation is difficult when harmful events are rare and the available data contain little tail coverage. [evidence-based]
- A shield depends on a sufficiently accurate transition abstraction and a complete formal safety specification. [evidence-based]
- Safety Gym and OmniSafe support research comparisons, but success in their supported simulations does not certify a deployed system. [evidence-based]
- Preference-based safety signals can inherit annotator disagreement, reward-model error, distribution shift, and optimization pressure. [evidence-based]
- Comparative safe-RL results are protocol-dependent and should remain contested until reproduced with matched budgets and hazard definitions. [contested]

## Brain Hooks

- Folded concept: [[Safe and constrained RL]]
- Related canon: [[Markov decision processes and the RL problem formulation]]
- Related canon: [[Trust-region and proximal methods (TRPO, PPO)]]
- Related canon: [[Exploration strategies and intrinsic motivation]]
- Related canon: [[Reward design, reward hacking, and specification gaming]]
- Related canon: [[RLHF reward models and PPO post-training (InstructGPT lineage)]]
- Related canon: [[RLAIF and Constitutional AI]]
- Related canon: [[Evaluation, benchmarks, and reproducibility in deep RL]]
- Related canon: [[Distributional RL]]
- Related canon: [[Sim-to-real and robotics RL]]
- Related canon: [[RL tooling landscape (Gymnasium, SB3, CleanRL, RLlib, TRL, veRL, OpenRLHF)]]
- Source intake path: [[Source Intake Workflow]]
- Verification path: [[Claim Verification Flow]]

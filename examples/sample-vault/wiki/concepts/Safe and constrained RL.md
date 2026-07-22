---
type: "concept"
title: "Safe and constrained RL"
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
  - "https://arxiv.org/abs/1705.10528"
  - "https://cdn.openai.com/safexp-short.pdf"
  - "https://arxiv.org/abs/2305.09304"
  - "https://arxiv.org/abs/1512.01629"
  - "https://arxiv.org/abs/1708.08611"
---

# Safe and constrained RL

Confidence tag: evidence-based. Folded from canon `031-safe-and-constrained-rl.md` on the date in `updated`.

## Sourced Takeaways

Safe and constrained reinforcement learning separates task reward from explicit cost, risk, or behavioral constraints instead of expecting one scalar reward to encode every requirement. [evidence-based]
A constrained Markov decision process, or CMDP, supports policies that maximize expected return subject to cost budgets, but expected constraints alone do not guarantee that every training or deployment trajectory is safe. [evidence-based]
Practical safety therefore combines objective design, constrained optimization, risk-sensitive evaluation, exploration controls, and independent enforcement where consequences demand it. [practitioner]
RLHF safety training can shape behavior through preferences or learned rewards, but it does not by itself provide the formal constraint guarantees assumed by CMDP or shielding methods. [evidence-based]

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

## Sources

- Canon evidence file: `references/topics/031-safe-and-constrained-rl.md`
- Joshua Achiam, David Held, Aviv Tamar, and Pieter Abbeel, 2017, "Constrained Policy Optimization," arXiv:1705.10528, [paper](https://arxiv.org/abs/1705.10528).
- Alex Ray, Joshua Achiam, and Dario Amodei, 2019, "Benchmarking Safe Exploration in Deep Reinforcement Learning," [Safety Gym paper](https://cdn.openai.com/safexp-short.pdf).
- Jiaming Ji et al., 2023, "OmniSafe: An Infrastructure for Accelerating Safe Reinforcement Learning Research," arXiv:2305.09304, [paper](https://arxiv.org/abs/2305.09304).
- Yinlam Chow, Mohammad Ghavamzadeh, Lucas Janson, and Marco Pavone, 2015, "Risk-Constrained Reinforcement Learning with Percentile Risk Criteria," arXiv:1512.01629, [paper](https://arxiv.org/abs/1512.01629).
- Mohammed Alshiekh, Roderick Bloem, Ruediger Ehlers, Bettina Könighofer, Scott Niekum, and Ufuk Topcu, 2017, "Safe Reinforcement Learning via Shielding," arXiv:1708.08611, [paper](https://arxiv.org/abs/1708.08611).
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]

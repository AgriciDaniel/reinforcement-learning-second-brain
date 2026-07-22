---
type: "concept"
title: "Model-based RL and planning (Dyna, MBPO, AlphaZero, MuZero)"
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
  - "https://doi.org/10.1016/B978-1-55860-141-3.50030-4"
  - "http://incompleteideas.net/book/the-book-2nd.html"
  - "https://arxiv.org/abs/1906.08253"
  - "https://arxiv.org/abs/1712.01815"
  - "https://arxiv.org/abs/1911.08265"
---

# Model-based RL and planning (Dyna, MBPO, AlphaZero, MuZero)

Confidence tag: evidence-based. Folded from canon `011-model-based-rl-and-planning-dyna-mbpo-alphazero-muzero.md` on the date in `updated`.

## Sourced Takeaways

Model-based reinforcement learning uses a known or learned account of consequences to improve decisions with computation, while direct reinforcement learning improves from experienced transitions alone.
Dyna, MBPO, AlphaZero, and MuZero instantiate this idea at different levels: replaying learned one-step transitions, generating short synthetic rollouts, searching a known simulator, and searching a learned latent dynamics model.
The central tradeoff is that planning can reuse data and look ahead, but errors in the model, value function, or search procedure can be amplified by repeated imagined steps.

- Planning is computation applied to a model, and learning from simulated experience can use the same update rule as learning from real experience. [evidence-based]
- Dyna treats real and simulated transitions as inputs to a common value-learning process while learning the model online. [evidence-based]
- MBPO controls compounding model error by branching short rollouts from states in the real replay distribution. [evidence-based]
- AlphaZero's search has access to exact game dynamics, whereas MuZero learns latent dynamics that predict reward, policy, and value information useful for search. [evidence-based]
- MuZero's latent state is not required to reconstruct observations, so predictive usefulness for planning does not imply a human-interpretable or causally correct world model. [evidence-based]
- More model rollouts or deeper search are not automatically better because error, distribution shift, and compute cost can increase with planning depth. [practitioner]
- Model accuracy averaged over a dataset is insufficient by itself, because errors along policy-selected and search-selected trajectories determine control quality. [practitioner]

## Best Practices

- Start model-generated rollouts from real replay states and validate short horizons before increasing rollout length. [evidence-based]
- Hold out real transitions for one-step and multi-step model validation, and stratify errors by state region instead of relying only on a global mean. [practitioner]
- Track real-data return, model-predicted return, rollout disagreement, and policy performance separately so exploitation of model error is visible. [practitioner]
- Use model ensembles or another explicit uncertainty diagnostic to identify where synthetic rollouts leave supported data, without treating ensemble spread as calibrated certainty. [practitioner]
- For tree-search agents, report simulations per decision, network evaluations, training compute, and evaluation search settings because these are part of the method. [practitioner]
- Preserve terminal semantics, reward scaling, discounting, and legal-action masks consistently between the real environment, learned model, replay targets, and planner. [practitioner]
- Refit and revalidate a learned model as the policy distribution changes, since a model accurate for old behavior may be poor on newly visited trajectories. [practitioner]
- Compare against strong direct-learning baselines at matched real interaction and disclose when planning receives substantially more computation. [practitioner]

## Evidence Caveats

Sutton's original Dyna results establish an architecture and illustrative tabular behavior, not a guarantee that learned neural simulators improve every high-dimensional control task.
The Dyna-Q planning update is only as reliable as its value-learning conditions, state-action sampling, and model; function approximation and off-policy bootstrapping introduce additional stability concerns.

MBPO's empirical evidence comes from a particular family of continuous-control tasks, model ensembles, rollout schedules, and an off-policy learner.
It does not establish one universally optimal synthetic-to-real ratio or rollout horizon, and its monotonic-improvement analysis uses assumptions and bounds that are more conservative than the practical algorithm.

AlphaZero's evidence concerns deterministic, fully observed, two-player board games with exact rules and terminal outcomes.
It does not show that the same search-training loop is practical under unsafe exploration, partial observability, costly real actions, or a misspecified learned simulator.

MuZero shows that task-relevant latent predictions can support planning in the evaluated games, but it does not prove that the learned dynamics identify true physical state, transfer causally, or remain reliable under arbitrary distribution shift.
Reported comparisons across Dyna, MBPO, AlphaZero, and MuZero would conflate different domains, data budgets, simulators, planners, and compute regimes.
For all four families, conclusions should include multiple seeds or independent runs where feasible, uncertainty intervals, ablations, and exact train-versus-evaluation planning budgets.

## Sources

- Canon evidence file: `references/topics/011-model-based-rl-and-planning-dyna-mbpo-alphazero-muzero.md`
- Richard S. Sutton (1990), "Integrated Architectures for Learning, Planning, and Reacting Based on Approximating Dynamic Programming," Proceedings of the Seventh International Conference on Machine Learning, [publisher record and DOI](https://doi.org/10.1016/B978-1-55860-141-3.50030-4).
- Richard S. Sutton and Andrew G. Barto (2018), *Reinforcement Learning: An Introduction*, second edition, Chapter 8, "Planning and Learning with Tabular Methods," [official book site](https://incompleteideas.net/book/the-book-2nd.html).
- Michael Janner, Justin Fu, Marvin Zhang, and Sergey Levine (2019), "When to Trust Your Model: Model-Based Policy Optimization," NeurIPS 2019, [arXiv:1906.08253](https://arxiv.org/abs/1906.08253).
- David Silver et al. (2017), "Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm," [arXiv:1712.01815](https://arxiv.org/abs/1712.01815).
- Julian Schrittwieser et al. (2019), "Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model," [arXiv:1911.08265](https://arxiv.org/abs/1911.08265), later published in *Nature*.
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]

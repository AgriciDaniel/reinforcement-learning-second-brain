---
type: "concept"
title: "Trust-region and proximal methods (TRPO, PPO)"
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
  - "https://proceedings.mlr.press/v37/schulman15.html"
  - "https://arxiv.org/abs/1707.06347"
  - "https://arxiv.org/abs/1506.02438"
  - "https://mitpress.mit.edu/9780262039246/reinforcement-learning/"
---

# Trust-region and proximal methods (TRPO, PPO)

Confidence tag: evidence-based. Folded from canon `009-trust-region-and-proximal-methods-trpo-ppo.md` on the date in `updated`.

## Sourced Takeaways

Trust-region policy optimization (TRPO) and proximal policy optimization (PPO) are on-policy policy-gradient methods that limit how aggressively a policy is changed using data collected by an older policy. TRPO expresses proximity as an average Kullback-Leibler (KL) divergence constraint and approximately solves a constrained second-order problem. PPO trades that machinery for first-order surrogate objectives that are easier to optimize, while providing no hard trust-region guarantee.

- The policy ratio corrects action probabilities under the old policy, but it does not correct the rollout state distribution after a large update. [evidence-based]
- TRPO's practical trust region is an average sampled KL constraint, while its strongest theoretical bound uses a stricter divergence quantity. [evidence-based]
- PPO clipping changes the optimization objective but does not guarantee that realized KL divergence or all probability ratios remain small. [evidence-based]
- Reusing a rollout for multiple PPO epochs improves data use relative to a single policy-gradient step, but the batch becomes progressively less on-policy as optimization proceeds. [evidence-based]
- Advantage quality matters because sign errors determine which side of the PPO clipping rule is active and can misdirect either algorithm. [evidence-based]
- The critic is a variance-reduction device for the policy update, so value loss is a diagnostic rather than the task objective itself. [evidence-based]
- TRPO and PPO optimize local surrogates and do not remove nonconvexity, partial observability, reward misspecification, or exploration failure. [evidence-based]

## Best Practices

- Log approximate KL, clip fraction, policy entropy, value error, explained variance, episodic return, and the number of accepted or rejected updates. [practitioner]
- For PPO, stop minibatch epochs early when measured KL materially exceeds a chosen target, since clipping alone does not enforce proximity. [practitioner]
- Treat the clip range, learning rate, rollout length, number of epochs, minibatch size, discount, and GAE \(\lambda\) as coupled controls rather than independent defaults. [practitioner]
- Preserve old log probabilities exactly for the sampled actions and test ratio computation, masking, termination handling, and advantage construction before tuning. [practitioner]
- Normalize advantages per training batch only as an implementation choice, and document it because it changes gradient scale and interactions with optimization. [practitioner]
- Keep policy and value losses separately observable, and consider separate optimizers or capacity when a shared network creates destructive interference. [practitioner]
- Compare algorithms across multiple seeds with identical environment steps, preprocessing, evaluation policy, and termination semantics. [evidence-based]

## Evidence Caveats

TRPO's theorem does not prove monotonic improvement for the exact neural-network implementation under finite sampling. The practical algorithm substitutes an average KL, approximate curvature, estimated advantages, and an acceptance heuristic for quantities in the bound.

The PPO paper reports favorable benchmark evidence for the tested objectives and settings, but it does not establish that clipping dominates TRPO, the KL-penalty form, or other policy optimizers across tasks. The clip range is not a universal safe step size, and implementation details can materially alter results.

Results from a small number of simulated-control or Atari seeds should not be treated as a universal ranking. Environment versions, time-limit handling, observation and reward normalization, network initialization, evaluation stochasticity, and total interaction budget can all change a comparison.

## Sources

- Canon evidence file: `references/topics/009-trust-region-and-proximal-methods-trpo-ppo.md`
- John Schulman, Sergey Levine, Pieter Abbeel, Michael I. Jordan, and Philipp Moritz (2015), [Trust Region Policy Optimization](https://proceedings.mlr.press/v37/schulman15.html), ICML, PMLR 37, arXiv:1502.05477.
- John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov (2017), [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347), arXiv:1707.06347.
- John Schulman, Philipp Moritz, Sergey Levine, Michael I. Jordan, and Pieter Abbeel (2015), [High-Dimensional Continuous Control Using Generalized Advantage Estimation](https://arxiv.org/abs/1506.02438), arXiv:1506.02438.
- Richard S. Sutton and Andrew G. Barto (2018), [Reinforcement Learning: An Introduction, second edition](http://incompleteideas.net/book/the-book-2nd.html), Chapter 13 on policy-gradient methods.
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]

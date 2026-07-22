---
type: "concept"
title: "Policy gradient methods and REINFORCE"
domain: "reinforcement learning: fundamentals, deep RL, RLHF/RLAIF and preference optimization, evaluation, tooling, and applied best practices"
status: "active"
created: "{{date}}"
updated: "{{date}}"
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
  - "https://doi.org/10.1007/BF00992696"
  - "https://proceedings.neurips.cc/paper_files/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html"
  - "https://mitpress.mit.edu/9780262039246/reinforcement-learning/"
---

# Policy gradient methods and REINFORCE

Confidence tag: evidence-based. Folded from canon `007-policy-gradient-methods-and-reinforce.md` on the date in `updated`.

## Sourced Takeaways

Policy gradient methods directly adjust a differentiable policy to increase an expected-return objective, rather than deriving the policy only by maximizing an estimated value function.
REINFORCE applies the likelihood-ratio, or score-function, identity to sampled actions and weights their log-probability gradients by observed returns.
This gives a broadly applicable, model-free gradient estimator, but its Monte Carlo targets can have high variance and its optimization problem is generally nonconvex.

- The score-function identity estimates a distribution gradient without differentiating rewards or environment dynamics. [evidence-based]
- Reward-to-go removes rewards that occurred before an action from that action's credit signal and preserves the on-policy expectation. [evidence-based]
- The policy gradient theorem expresses the gradient using policy derivatives and action values under the policy's own occupancy distribution. [evidence-based]
- Any baseline that depends on state but not on the sampled action has zero expected score-function contribution. [evidence-based]
- REINFORCE uses sampled Monte Carlo returns, so correct on-policy sampling can yield an unbiased estimator for the chosen finite-horizon objective while still producing high variance. [evidence-based]
- Direct policy parameterization naturally represents stochastic policies and common continuous-action distributions. [evidence-based]
- A valid gradient direction does not imply monotonic improvement after a finite optimizer step or convergence to a global optimum. [evidence-based]

## Best Practices

- Define the return objective, discount convention, horizon, and treatment of truncation before implementing the loss. [evidence-based]
- Compute reward-to-go backward through each trajectory and mask only true environmental terminations when deciding whether bootstrapping is valid. [practitioner]
- Use a learned value baseline or another demonstrably action-independent control variate, and keep its regression target separate from the actor objective. [evidence-based]
- Detach sampled return or advantage targets from the actor loss unless a separately derived differentiable objective requires otherwise. [practitioner]
- Check that stored log probabilities correspond to the policy that generated each action; stale or replayed samples require an explicit off-policy correction. [evidence-based]
- Track gradient norms, policy entropy, approximate policy change, episodic return distributions, and multiple random seeds rather than trusting one learning curve. [practitioner]
- Treat advantage normalization, entropy bonuses, gradient clipping, and optimizer settings as implementation choices to ablate, not as consequences of the REINFORCE theorem. [practitioner]

## Evidence Caveats

Williams establishes a family of stochastic gradient-following rules under stated formulations; it does not show that modern neural REINFORCE is sample-efficient or stable across deep-RL benchmarks.
The Sutton et al. convergence result uses specific assumptions and compatible function-approximation structure, so it is not a blanket convergence guarantee for arbitrary nonlinear policy networks.
Unbiasedness claims depend on the precise objective, on-policy data, horizon handling, and baseline construction.
Finite batches, reward scaling, optimizer state, shared representations, and advantage normalization can materially alter empirical behavior.
Reported success on one task or seed does not establish superiority over value-based, actor-critic, or proximal alternatives.

## Sources

- Canon evidence file: `references/topics/007-policy-gradient-methods-and-reinforce.md`
- Ronald J. Williams (1992), "Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning," *Machine Learning* 8, 229-256, DOI: https://doi.org/10.1007/BF00992696
- Richard S. Sutton, David A. McAllester, Satinder P. Singh, and Yishay Mansour (2000; NeurIPS 12 conference proceedings), "Policy Gradient Methods for Reinforcement Learning with Function Approximation": https://proceedings.neurips.cc/paper_files/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html
- Richard S. Sutton and Andrew G. Barto (2018), *Reinforcement Learning: An Introduction*, second edition, Chapter 13, MIT Press: https://mitpress.mit.edu/9780262039246/reinforcement-learning/
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]

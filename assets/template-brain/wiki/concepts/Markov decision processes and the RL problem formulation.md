---
type: "concept"
title: "Markov decision processes and the RL problem formulation"
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
  - "https://mitpress.mit.edu/9780262039246/reinforcement-learning/>"
  - "http://incompleteideas.net/book/RLbook2020.pdf>"
---

# Markov decision processes and the RL problem formulation

Confidence tag: evidence-based. Folded from canon `001-markov-decision-processes-and-the-rl-problem-formulation.md` on the date in `updated`.

## Sourced Takeaways

A Markov decision process (MDP) formalizes sequential decision making as interaction between an agent and an environment through states, actions, and scalar rewards.
The formulation matters because it separates the objective, encoded by reward and return, from the solution method, encoded by a policy and a learning or planning algorithm.
Value functions and Bellman equations then turn long-horizon consequences into one-step recursive relationships that most classical reinforcement-learning methods estimate or improve.

- The agent-environment boundary determines which signals are actions, states, and rewards, so moving the boundary changes the formal problem. [evidence-based]
- A state is Markov when it carries the information needed for the conditional distribution of the next reward and state, even if it is not a complete description of the world. [evidence-based]
- Rewards define immediate goal signals, while value functions summarize their expected long-term accumulation under a policy. [evidence-based]
- A stochastic policy maps each state to action probabilities, and a deterministic policy is the special case that assigns all probability to one action. [evidence-based]
- Bellman equations are consistency relationships for value functions, not standalone learning algorithms. [evidence-based]
- The distinction between episodic and continuing tasks affects return definitions, terminal handling, and suitable discounting. [evidence-based]
- Optimality is defined relative to the supplied state, action, reward, dynamics, and return objective, so a mathematically optimal policy can still solve the wrong practical problem. [practitioner]
- Known dynamics permit planning, but reinforcement-learning methods can instead approximate values or policies from experience without an explicit transition model. [evidence-based]

## Best Practices

- Write down the time step, agent-environment boundary, action set, observation or state, reward timing, and terminal condition before choosing an algorithm. [practitioner]
- Test state sufficiency by looking for histories with the same represented state but materially different next-outcome distributions; augment the state or use a partial-observability treatment when they differ. [practitioner]
- Treat discounting as part of the task objective, and report \(\gamma\) with results because changing it changes the policy being optimized. [evidence-based]
- Distinguish true termination from administrative truncation so that bootstrapped targets do not silently discard continuation value at a time limit. [practitioner]
- Validate reward semantics with trajectory-level examples, including edge cases where maximizing accumulated reward could diverge from the intended goal. [practitioner]
- Specify the initial-state distribution and evaluation distribution, since performance can vary even when the transition and reward functions are unchanged. [practitioner]
- Use tabular exact methods as a diagnostic baseline when the state-action space is small enough, before introducing approximation error. [practitioner]

## Evidence Caveats

The finite MDP model assumes that a useful Markov state is available and that interaction can be represented at discrete time steps.
Real systems may expose observations that alias latent states, may change over time, or may depend on other adapting agents.

Discounted return is one objective, not a proof that a chosen discount rate captures the real decision horizon or stakeholder utility.
Average-reward continuing formulations and partially observable models require additional machinery not developed in this note.

Bellman optimality establishes mathematical relationships under the specified model.
It does not guarantee that a learning algorithm will reach the optimal solution with finite data, approximation, off-policy sampling, or unstable optimization.

The textbook develops general theory and illustrative examples.
It does not establish that any one state representation, reward design, or algorithm is adequate for a new application without task-specific validation, multiple runs, and failure analysis.

## Sources

- Canon evidence file: `references/topics/001-markov-decision-processes-and-the-rl-problem-formulation.md`
- Richard S. Sutton and Andrew G. Barto, 2018, *Reinforcement Learning: An Introduction*, second edition, Chapter 3, "Finite Markov Decision Processes," MIT Press. Author-hosted book page: <http://incompleteideas.net/book/the-book-2nd.html>
- Richard S. Sutton and Andrew G. Barto, *Reinforcement Learning: An Introduction*, second-edition complete text, including the Chapter 3 equations and notation used here. Author-hosted PDF: <http://incompleteideas.net/book/RLbook2020.pdf>
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]

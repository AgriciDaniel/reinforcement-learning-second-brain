---
type: "canon"
title: "001. Markov decision processes and the RL problem formulation"
created: "2026-07-22"
updated: "2026-07-22"
status: "active"
---

# 001. Markov decision processes and the RL problem formulation

Ledger: 001 | target: Markov decision processes and the RL problem formulation | confidence: evidence-based | fold: [[Markov decision processes and the RL problem formulation]] | status: active.

## Core Thesis

A Markov decision process (MDP) formalizes sequential decision making as interaction between an agent and an environment through states, actions, and scalar rewards.
The formulation matters because it separates the objective, encoded by reward and return, from the solution method, encoded by a policy and a learning or planning algorithm.
Value functions and Bellman equations then turn long-horizon consequences into one-step recursive relationships that most classical reinforcement-learning methods estimate or improve.

## How It Works

At discrete time step \(t\), the agent observes state \(S_t\), selects action \(A_t\), and receives reward \(R_{t+1}\) together with the next state \(S_{t+1}\).

For a finite MDP, the environment dynamics are captured by the one-step joint distribution

\[
p(s',r\mid s,a) = \Pr\{S_{t+1}=s', R_{t+1}=r \mid S_t=s, A_t=a\}.
\]

The Markov property says that this distribution depends on the current state and action, not on earlier observations and actions once the current state is given.
Thus, state design is a predictive sufficiency claim, not merely a choice of feature names.

A policy \(\pi(a\mid s)\) is a probability distribution over actions conditional on state.
The agent's objective is expressed through the return, the discounted sum of future rewards,

\[
G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \cdots
    = R_{t+1} + \gamma G_{t+1},
\]

where \(0 \leq \gamma \leq 1\) is the discount rate under the usual episodic or discounted continuing formulation.
Episodic tasks end in a terminal state and may use \(\gamma=1\) when returns remain finite.
Continuing tasks have no natural terminal event and commonly use \(\gamma<1\) for the discounted objective.

The state-value function under policy \(\pi\) is the expected return from a state,

\[
v_\pi(s) = \mathbb{E}_\pi[G_t \mid S_t=s],
\]

and the action-value function is the expected return after taking an action and then following \(\pi\),

\[
q_\pi(s,a) = \mathbb{E}_\pi[G_t \mid S_t=s, A_t=a].
\]

The Bellman expectation equation for \(v_\pi\) expands value into expected immediate reward plus discounted successor value,

\[
v_\pi(s) = \sum_a \pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)
            [r + \gamma v_\pi(s')].
\]

Optimal value functions use maximization instead of a policy-weighted action average.
For example, the Bellman optimality equation for action values is

\[
q_*(s,a) = \sum_{s',r}p(s',r\mid s,a)
            [r + \gamma \max_{a'} q_*(s',a')].
\]

A policy greedy with respect to \(q_*\) is optimal under the finite-MDP assumptions.
Planning methods apply these recursions with a known model, while model-free methods estimate their solutions from sampled transitions.

The canonical interaction loop is: initialize policy or value estimates, observe a state, choose an action, collect \((S_t,A_t,R_{t+1},S_{t+1})\), update estimates or the policy, handle termination, and repeat.
The initial-state distribution, transition timing, terminal convention, and evaluation objective are therefore part of the problem definition, not incidental implementation details.

## Key Principles

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

## Primary Sources

- Richard S. Sutton and Andrew G. Barto, 2018, *Reinforcement Learning: An Introduction*, second edition, Chapter 3, "Finite Markov Decision Processes," MIT Press. Author-hosted book page: <http://incompleteideas.net/book/the-book-2nd.html>
- Richard S. Sutton and Andrew G. Barto, *Reinforcement Learning: An Introduction*, second-edition complete text, including the Chapter 3 equations and notation used here. Author-hosted PDF: <http://incompleteideas.net/book/RLbook2020.pdf>

## Evidence Caveats

The finite MDP model assumes that a useful Markov state is available and that interaction can be represented at discrete time steps.
Real systems may expose observations that alias latent states, may change over time, or may depend on other adapting agents.

Discounted return is one objective, not a proof that a chosen discount rate captures the real decision horizon or stakeholder utility.
Average-reward continuing formulations and partially observable models require additional machinery not developed in this note.

Bellman optimality establishes mathematical relationships under the specified model.
It does not guarantee that a learning algorithm will reach the optimal solution with finite data, approximation, off-policy sampling, or unstable optimization.

The textbook develops general theory and illustrative examples.
It does not establish that any one state representation, reward design, or algorithm is adequate for a new application without task-specific validation, multiple runs, and failure analysis.

## Brain Hooks

- Folded concept: [[Markov decision processes and the RL problem formulation]]
- Immediate-action abstraction: [[Bandits and exploration-exploitation]]
- Classical solution families: [[Dynamic programming, Monte Carlo, and temporal-difference learning]]
- Tabular control methods: [[Q-learning, SARSA, and tabular methods]]
- Approximate value representations: [[Function approximation and the deadly triad]]
- Learned or supplied models: [[Model-based RL and planning (Dyna, MBPO, AlphaZero, MuZero)]]
- Objective failure modes: [[Reward design, reward hacking, and specification gaming]]
- Dataset-constrained interaction: [[Offline batch RL and conservatism]]
- Nonstationary interacting learners: [[Multi-agent RL]]
- Source intake path: [[Source Intake Workflow]]
- Verification path: [[Claim Verification Flow]]

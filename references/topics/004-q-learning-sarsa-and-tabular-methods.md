---
type: "canon"
title: "004. Q-learning, SARSA, and tabular methods"
created: "2026-07-22"
updated: "2026-07-22"
status: "active"
---

# 004. Q-learning, SARSA, and tabular methods

Ledger: 004 | target: Q-learning, SARSA, and tabular methods | confidence: evidence-based | fold: [[Q-learning, SARSA, and tabular methods]] | status: active.

## Core Thesis

Q-learning and SARSA are one-step temporal-difference control algorithms that learn tabular action values from experience without requiring a transition model. SARSA evaluates and improves the policy that generates its next action, while Q-learning learns toward a greedy target independently of a potentially exploratory behavior policy. This on-policy versus off-policy distinction determines the update target, the policy whose value is learned, and the conditions needed for reliable control.

## How It Works

For a finite state and action space, store one estimate \(Q(s,a)\) for every state-action pair.

An action-selection rule, often \(\epsilon\)-greedy, converts the current table into a behavior policy.

With probability \(1-\epsilon\), an \(\epsilon\)-greedy policy selects a maximizing action, and with probability \(\epsilon\) it selects uniformly from all actions, including maximizing actions.

Tie handling is part of the policy definition and should be randomized among maximizing actions unless the application requires a fixed deterministic convention.

### SARSA

SARSA is named for the transition tuple \(S_t,A_t,R_{t+1},S_{t+1},A_{t+1}\).

After selecting \(A_{t+1}\) from the same policy used for behavior, compute

\[
\delta_t^{\text{SARSA}}=R_{t+1}+\gamma Q(S_{t+1},A_{t+1})-Q(S_t,A_t).
\]

Then update

\[
Q(S_t,A_t) \leftarrow Q(S_t,A_t)+\alpha\delta_t^{\text{SARSA}}.
\]

Because the next sampled action appears in the target, persistent exploration is reflected in the learned action values.

A standard episodic loop selects an initial action, steps the environment, selects the next action unless the transition terminated, updates the previous pair, and shifts \((S,A)\) to \((S',A')\).

### Q-learning

Q-learning replaces the sampled next action with a greedy target:

\[
\delta_t^{Q}=R_{t+1}+\gamma\max_a Q(S_{t+1},a)-Q(S_t,A_t).
\]

The table update is

\[
Q(S_t,A_t) \leftarrow Q(S_t,A_t)+\alpha\delta_t^{Q}.
\]

The behavior policy may remain exploratory, but the target policy represented by the maximum is greedy with respect to the current action values.

In the finite tabular setting, Q-learning converges to optimal action values under standard stochastic-approximation conditions, including repeated sampling of every state-action pair and suitable diminishing step sizes.

### Expected SARSA and Double Q-learning

Expected SARSA uses the expectation under the target policy instead of a sampled next action:

\[
R_{t+1}+\gamma\sum_a\pi(a\mid S_{t+1})Q(S_{t+1},a).
\]

For the same target policy, replacing the sampled action with its expectation removes variance due solely to that action sample.

Expected SARSA can be on-policy or off-policy depending on whether its target policy equals the behavior policy.

The maximization in ordinary Q-learning can favor noisy overestimates because selection and evaluation use the same estimates.

Double Q-learning maintains two action-value tables, uses one table to select a maximizing action, and uses the other to evaluate it, alternating which table is updated.

### Tabular control pattern

All these methods instantiate generalized policy iteration: action-value estimates move toward a policy-dependent target while action selection changes in response to the estimates.

For terminal transitions, the target is the observed reward with no bootstrap term.

For continuing tasks, the same updates require a continuing-task objective such as discounted return or an explicitly formulated average-reward method.

## Key Principles

- SARSA is on-policy when its behavior and target policies are the same, because its update uses the action actually selected by that policy. [evidence-based]
- Q-learning is off-policy because its greedy target can differ from the policy that generated the transition. [evidence-based]
- The policy used to collect data and the policy represented in the update target must be documented separately. [practitioner]
- A constant nonzero exploration rate means on-policy SARSA learns the value of an exploratory policy, not the value of the corresponding fully greedy policy. [evidence-based]
- The tabular Q-learning convergence theorem does not justify arbitrary constant step sizes, insufficient visitation, nonstationary dynamics, or nonlinear approximators. [evidence-based]
- Expected SARSA removes next-action sampling variance but still inherits randomness from transitions, rewards, and earlier estimates. [evidence-based]
- Maximization bias arises when noisy estimates are both compared and used to evaluate the selected maximum. [evidence-based]
- Optimistic initial values can induce exploration in stationary tasks, but their influence fades and they do not solve general nonstationary exploration. [evidence-based]

## Best Practices

- Initialize terminal-state action values consistently and omit the bootstrap term whenever the environment reports true termination. [evidence-based]
- Distinguish termination from an external time limit, because treating every truncation as terminal changes the value target. [practitioner]
- Randomize greedy ties to prevent table order from silently imposing a behavioral preference. [practitioner]
- Use a decaying exploration schedule only when it preserves enough visitation for the intended convergence claim, and report the complete schedule. [evidence-based]
- Tune the step size jointly with exploration and reward scale, then compare learning curves across several seeds rather than selecting one favorable run. [practitioner]
- Use SARSA when the value of exploratory behavior itself is the control object, and use Q-learning when a distinct greedy target policy matches the objective. [practitioner]
- Consider Expected SARSA when next-action noise is undesirable and the target-policy expectation is cheap to compute. [practitioner]
- Add Double Q-learning when maximization bias is visible, but verify its effect empirically rather than assuming every positive value error comes from maximization. [practitioner]

## Primary Sources

- Richard S. Sutton and Andrew G. Barto (2018), *Reinforcement Learning: An Introduction*, second edition, Chapter 6, The MIT Press: https://mitpress.mit.edu/9780262039246/reinforcement-learning/
- Richard S. Sutton and Andrew G. Barto (2020), complete second-edition author-hosted text: http://incompleteideas.net/book/RLbook2020.pdf
- Christopher J. C. H. Watkins and Peter Dayan (1992), “Q-learning,” *Machine Learning* 8, DOI: https://doi.org/10.1007/BF00992698
- Gavin A. Rummery and Mahesan Niranjan (1994), *On-line Q-learning Using Connectionist Systems*, Cambridge University Engineering Department Technical Report CUED/F-INFENG/TR 166: http://mi.eng.cam.ac.uk/reports/svr-ftp/auto-pdf/rummery_tr166.pdf

## Evidence Caveats

- Classical convergence guarantees are asymptotic and assumption-dependent, so they do not specify useful finite-sample performance or a practical stopping time. [evidence-based]
- The textbook's cliff-walking examples explain a policy distinction but do not establish that SARSA is generally safer or that Q-learning is generally more reward-efficient. [evidence-based]
- Seed variance can arise from exploratory action choices, stochastic transitions and rewards, initialization, and random tie breaking, even with a small table. [practitioner]
- A single final greedy evaluation can conceal unstable learning, poor state-action coverage, or sensitivity to the exploration schedule. [practitioner]
- Tabular guarantees do not transfer unchanged to replay buffers, target networks, deep function approximation, or offline data. [evidence-based]
- The cited sources do not prove a universal advantage for Q-learning, SARSA, Expected SARSA, or Double Q-learning across tasks. [evidence-based]

## Brain Hooks

- Folded concept: [[Q-learning, SARSA, and tabular methods]]
- Formal foundation: [[Markov decision processes and the RL problem formulation]]
- Exploration foundation: [[Bandits and exploration-exploitation]]
- Backup-method context: [[Dynamic programming, Monte Carlo, and temporal-difference learning]]
- Approximation boundary: [[Function approximation and the deadly triad]]
- Deep value extension: [[Deep Q-Networks and value-based deep RL (DQN, Rainbow)]]
- Planning extension: [[Model-based RL and planning (Dyna, MBPO, AlphaZero, MuZero)]]
- Exploration extensions: [[Exploration strategies and intrinsic motivation]]
- Offline-data boundary: [[Offline batch RL and conservatism]]
- Evaluation discipline: [[Evaluation, benchmarks, and reproducibility in deep RL]]
- Debugging practice: [[Debugging RL training runs in practice]]
- Source intake path: [[Source Intake Workflow]]
- Verification path: [[Claim Verification Flow]]

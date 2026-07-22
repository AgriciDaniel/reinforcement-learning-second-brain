---
type: "canon"
title: "015. Hierarchical RL and options"
created: "2026-07-22"
updated: "2026-07-22"
status: "active"
---

# 015. Hierarchical RL and options

Ledger: 015 | target: Hierarchical RL and options | confidence: evidence-based | fold: [[Hierarchical RL and options]] | status: active.

## Core Thesis

Hierarchical reinforcement learning organizes control across time scales, so a policy can choose a temporally extended course of action while a lower-level policy chooses primitive actions. The options framework makes this precise by extending an MDP with closed-loop actions that have explicit initiation and termination rules. It matters because the same representation supports planning, learning, and execution while retaining a formal connection to semi-Markov decision processes.

## How It Works

An option \(o\) is a triple:

\[
o = (I_o,\pi_o,\beta_o).
\]

The initiation set \(I_o \subseteq \mathcal S\) says where the option is available. The internal policy \(\pi_o(a\mid s)\) selects primitive actions while the option runs. The termination function \(\beta_o(s)\in[0,1]\) gives the probability of terminating after arrival in state \(s\).

Under call-and-return execution, a policy over options \(\mu(o\mid s)\) selects an eligible option, commits control to \(\pi_o\), and selects again only after termination. If the option lasts a random \(K\) primitive steps, its discounted reward is

\[
G_t^{(K)}=\sum_{j=0}^{K-1}\gamma^j R_{t+j+1}.
\]

The semi-Markov option-value Bellman equation is

\[
Q^\mu(s,o)=
\mathbb E\!\left[
G_t^{(K)}
+\gamma^K\sum_{o'}\mu(o'\mid S_{t+K})Q^\mu(S_{t+K},o')
\mid S_t=s,o
\right].
\]

Control replaces the policy-weighted continuation with the best available next option:

\[
Q_*^{\mathcal O}(s,o)=
\mathbb E\!\left[
G_t^{(K)}+\gamma^K\max_{o'\in\mathcal O(S_{t+K})}
Q_*^{\mathcal O}(S_{t+K},o')
\mid s,o
\right].
\]

SMDP Q-learning applies one update when an option ends:

\[
Q(s,o)\leftarrow Q(s,o)+\alpha
\left[
G_t^{(K)}+\gamma^K\max_{o'}Q(S_{t+K},o')-Q(s,o)
\right].
\]

For Markov options, one-step intra-option learning can update from transitions inside an option. Its continuation target mixes continuing the current option with terminating and choosing again:

\[
U(s',o)=(1-\beta_o(s'))Q(s',o)
+\beta_o(s')\max_{o'}Q(s',o'),
\]

\[
Q(s,o)\leftarrow Q(s,o)+\alpha
\left[R_{t+1}+\gamma U(S_{t+1},o)-Q(s,o)\right].
\]

Model-based planning uses a multi-time option model. The reward component predicts \(G_t^{(K)}\), while the transition component weights termination in \(s'\) by \(\gamma^K\):

\[
r_o(s)=\mathbb E[G_t^{(K)}\mid s,o],
\qquad
p_o(s,s')=\mathbb E[\gamma^K\mathbf 1\{S_{t+K}=s'\}\mid s,o].
\]

A practical call-and-return loop has four stages:

1. Select an option from the options whose initiation sets contain the current state.
2. Sample primitive actions from that option's internal policy.
3. Accumulate rewards and test the termination function after each transition.
4. On termination, update the option value and let the policy over options select again.

Primitive actions are representable as one-step options. A hierarchy arises from policies choosing among options, but the formalism can mix primitive actions and options at the same decision level.

## Key Principles

- An MDP plus a fixed set of options, with each selected option executed to termination, induces an SMDP whose action durations may be random. [evidence-based]
- Option values must discount both rewards within the option and the value after termination by the realized duration \(K\). [evidence-based]
- The optimum \(Q_*^{\mathcal O}\) is relative to the available option set; it need not equal the unrestricted primitive-action optimum when useful primitive choices are omitted. [evidence-based]
- Primitive actions are a special case of options, so retaining them can preserve the original MDP's action-level expressivity. [evidence-based]
- A Markov policy over multi-step options can induce a semi-Markov primitive-action policy because the active option carries memory not contained in the environment state alone. [evidence-based]
- Intra-option methods reuse action-level fragments for Markov options instead of waiting for every option to finish, subject to stronger consistency and convergence assumptions. [evidence-based]
- Temporal abstraction does not by itself solve state abstraction, subgoal discovery, transfer, or representation learning. [evidence-based]
- Interrupting an option when its continuation value is below the policy's state value has a non-degradation result under the paper's exact-value assumptions, not a blanket guarantee under approximation. [evidence-based]

## Best Practices

- Keep primitive actions or a safe short-horizon fallback available unless restricting the option set is an intentional part of the task definition. [practitioner]
- Specify each initiation set, internal policy, and termination function independently, then test unreachable starts, accidental nontermination, and termination immediately after initiation. [practitioner]
- Log primitive-step return, option duration, initiation state, termination state, termination cause, and policy-over-options decisions so failures can be localized by time scale. [practitioner]
- Use the realized \(\gamma^K\) in SMDP targets; replacing it with a fixed one-step discount changes the Bellman target for variable-duration options. [evidence-based]
- Apply intra-option updates only when the observed primitive action is compatible with the option policy and the Markov assumptions needed by the update are explicit. [evidence-based]
- Evaluate a hierarchy against a primitive-action baseline under the same interaction and compute budget, including multiple seeds and task variants. [practitioner]
- Prefer option boundaries tied to reusable and observable control events, then stress-test whether the same boundaries remain useful when goals or dynamics change. [practitioner]
- Monitor option collapse, one-step chattering, and excessively long commitments; there is no source-backed universal target duration or option count. [practitioner]

## Primary Sources

- Richard S. Sutton, Doina Precup, and Satinder Singh (1999), "Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning," *Artificial Intelligence* 112(1-2). [Publisher record and DOI](https://doi.org/10.1016/S0004-3702(99)00052-1)
- Richard S. Sutton, Doina Precup, and Satinder Singh (1999), author-paper copy of the same article, including the options tuple, SMDP Bellman equations, interruption result, and intra-option methods. [Primary paper PDF](https://people.cs.umass.edu/~barto/courses/cs687/Sutton-Precup-Singh-AIJ99.pdf)

## Evidence Caveats

- The 1999 article establishes a general framework, but many formal convergence statements are tabular and assume finite MDPs, sufficient exploration, and prescribed options.
- The stated convergence result for one-step intra-option Q-learning is for Markov options with deterministic internal policies and requires every primitive action in every state to be executed infinitely often.
- The interruption theorem reasons with the relevant true values. Approximation error can reverse a comparison and trigger a harmful interruption.
- The rooms experiments illustrate favorable planning and learning cases; they do not establish a universal advantage for hierarchy across domains.
- A restricted option set can accelerate coarse planning yet exclude actions needed to solve a changed task, so reuse and optimality can conflict.
- The source leaves option discovery, state abstraction, subtask transfer, and integration with function approximation incompletely resolved.
- Deep learned options add optimization and representation failure modes that the 1999 tabular results do not validate.

## Brain Hooks

- Folded concept: [[Hierarchical RL and options]]
- Formal foundation: [[Markov decision processes and the RL problem formulation]]
- Backup mechanics: [[Dynamic programming, Monte Carlo, and temporal-difference learning]]
- Tabular control link: [[Q-learning, SARSA, and tabular methods]]
- Approximation risks: [[Function approximation and the deadly triad]]
- Planning connection: [[Model-based RL and planning (Dyna, MBPO, AlphaZero, MuZero)]]
- Skill discovery connection: [[Exploration strategies and intrinsic motivation]]
- Evaluation discipline: [[Evaluation, benchmarks, and reproducibility in deep RL]]
- Run diagnosis: [[Debugging RL training runs in practice]]
- Source intake path: [[Source Intake Workflow]]
- Verification path: [[Claim Verification Flow]]

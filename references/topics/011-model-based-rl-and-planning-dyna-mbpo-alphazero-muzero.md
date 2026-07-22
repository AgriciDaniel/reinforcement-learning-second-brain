---
type: "canon"
title: "011. Model-based RL and planning (Dyna, MBPO, AlphaZero, MuZero)"
created: "2026-07-22"
updated: "2026-07-22"
status: "active"
---

# 011. Model-based RL and planning (Dyna, MBPO, AlphaZero, MuZero)

Ledger: 011 | target: Model-based RL and planning (Dyna, MBPO, AlphaZero, MuZero) | confidence: evidence-based | fold: [[Model-based RL and planning (Dyna, MBPO, AlphaZero, MuZero)]] | status: active.

## Core Thesis

Model-based reinforcement learning uses a known or learned account of consequences to improve decisions with computation, while direct reinforcement learning improves from experienced transitions alone.
Dyna, MBPO, AlphaZero, and MuZero instantiate this idea at different levels: replaying learned one-step transitions, generating short synthetic rollouts, searching a known simulator, and searching a learned latent dynamics model.
The central tradeoff is that planning can reuse data and look ahead, but errors in the model, value function, or search procedure can be amplified by repeated imagined steps.

## How It Works

### Dyna: direct learning and planning share an update

Dyna interleaves acting, model learning, direct reinforcement learning, and planning.
After a real transition `(S, A, R, S')`, a Dyna-Q agent applies the one-step Q-learning target and updates a model of the reward and next state for `(S, A)`.
The named Q-learning update is:

$$
Q(S,A) \leftarrow Q(S,A) + \alpha\left[R + \gamma\max_a Q(S',a) - Q(S,A)\right].
$$

For each planning step, the agent samples a previously observed state-action pair, queries the learned model for a hypothetical reward and successor, and applies the same value update to that simulated transition.
The number and distribution of planning backups determine how much computation is spent propagating information beyond the latest real transition.
A sample model generates a possible transition, while a distribution model can support expected backups or sampled outcomes.

### MBPO: constrain the horizon of learned-model rollouts

Model-Based Policy Optimization, or MBPO, trains a probabilistic ensemble dynamics model on real transitions and retains a real-data replay buffer.
Synthetic rollouts begin from states sampled from real experience, then follow the current policy inside a sampled learned model for a short horizon.
The resulting model transitions enter a model-data buffer, and an off-policy policy optimizer trains on batches drawn from real and synthetic experience.
The policy objective itself can remain model-free in form because the learned model is used as a transition generator rather than differentiated through.
MBPO's analysis and experiments center on the model-usage tradeoff: longer rollouts expose the policy to more imagined data but accumulate more model bias.
Its practical training loop alternates among collecting real transitions, refitting the model, branching short rollouts from real states, and updating the policy.

### AlphaZero: search a known environment model

AlphaZero assumes exact game rules that can advance a state and identify terminal outcomes.
A neural network maps a position `s` to a policy prior `p` and scalar value estimate `v`:

$$
(p,v) = f_\theta(s).
$$

Monte Carlo tree search uses the known rules to expand successor positions, the network policy to prioritize actions, and backed-up value estimates to update edge statistics.
The normalized root visit counts form an improved search policy `\pi`, which guides self-play action selection.
Each completed self-play game yields position targets `(s, \pi, z)`, where `z` is the terminal outcome from the current player's perspective.
The named joint policy-value loss is:

$$
\ell(\theta) = (z-v)^2 - \pi^\top\log p + c\lVert\theta\rVert^2.
$$

Training repeatedly generates self-play with the current network and search, then fits the network to search policies and game outcomes.
Search improves the targets used for learning, and the learned network in turn focuses and evaluates later searches.

### MuZero: search a task-relevant latent model

MuZero removes the requirement that planning use externally supplied transition rules.
An initial representation function maps the observation history to a hidden state, a recurrent dynamics function maps a hidden state and action to a predicted reward and next hidden state, and a prediction function maps a hidden state to policy and value predictions.
Using conventional names, these components are:

$$
s^0 = h_\theta(o_{1:t}), \qquad (r^{k+1},s^{k+1}) = g_\theta(s^k,a^{k+1}), \qquad (p^k,v^k) = f_\theta(s^k).
$$

Monte Carlo tree search unfolds `g_\theta` in latent space and uses the predicted policies, values, and rewards to select and back up simulated trajectories.
The agent acts from the search policy, stores trajectories in replay, and trains over recurrent unrolls.
At each unrolled step, the loss compares predicted rewards with observed rewards, predicted policies with search policies, and predicted values with bootstrapped return targets.
The model is therefore optimized for quantities needed by planning, not for reconstructing observations or reproducing every detail of environment dynamics.

### Shared control loop

Across these methods, model learning or simulator access supplies imagined consequences, a planner or learner converts those consequences into improved action values or policies, and real interaction corrects the system.
The meaningful unit of comparison is not simply model-based versus model-free.
It is the full allocation of real samples, model updates, planning depth, search breadth, policy updates, and evaluation compute.

## Key Principles

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

## Primary Sources

- Richard S. Sutton (1990), "Integrated Architectures for Learning, Planning, and Reacting Based on Approximating Dynamic Programming," Proceedings of the Seventh International Conference on Machine Learning, [publisher record and DOI](https://doi.org/10.1016/B978-1-55860-141-3.50030-4).
- Richard S. Sutton and Andrew G. Barto (2018), *Reinforcement Learning: An Introduction*, second edition, Chapter 8, "Planning and Learning with Tabular Methods," [official book site](https://incompleteideas.net/book/the-book-2nd.html).
- Michael Janner, Justin Fu, Marvin Zhang, and Sergey Levine (2019), "When to Trust Your Model: Model-Based Policy Optimization," NeurIPS 2019, [arXiv:1906.08253](https://arxiv.org/abs/1906.08253).
- David Silver et al. (2017), "Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm," [arXiv:1712.01815](https://arxiv.org/abs/1712.01815).
- Julian Schrittwieser et al. (2019), "Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model," [arXiv:1911.08265](https://arxiv.org/abs/1911.08265), later published in *Nature*.

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

## Brain Hooks

- Folded concept: [[Model-based RL and planning (Dyna, MBPO, AlphaZero, MuZero)]]
- Problem formulation: [[Markov decision processes and the RL problem formulation]]
- Planning foundations: [[Dynamic programming, Monte Carlo, and temporal-difference learning]]
- Dyna-Q substrate: [[Q-learning, SARSA, and tabular methods]]
- Approximation risk: [[Function approximation and the deadly triad]]
- Deep value baseline: [[Deep Q-Networks and value-based deep RL (DQN, Rainbow)]]
- Data-coverage link: [[Exploration strategies and intrinsic motivation]]
- Temporal abstraction: [[Hierarchical RL and options]]
- Evaluation discipline: [[Evaluation, benchmarks, and reproducibility in deep RL]]
- Operational diagnostics: [[Debugging RL training runs in practice]]
- Source intake path: [[Source Intake Workflow]]
- Verification path: [[Claim Verification Flow]]

---
type: "canon"
title: "022. Evaluation, benchmarks, and reproducibility in deep RL"
created: "2026-07-22"
updated: "2026-07-22"
status: "active"
---

# 022. Evaluation, benchmarks, and reproducibility in deep RL

Ledger: 022 | target: Evaluation, benchmarks, and reproducibility in deep RL | confidence: evidence-based | fold: [[Evaluation, benchmarks, and reproducibility in deep RL]] | status: active.

## Core Thesis

A deep RL result is meaningful only relative to a fully specified algorithm, task distribution, training budget, evaluation protocol, and uncertainty estimate. [evidence-based]
Random seeds, implementation details, hyperparameter selection, and environment semantics can change conclusions enough that a single learning curve or aggregate point estimate is weak evidence. [evidence-based]
Reproducible evaluation therefore joins protocol control, raw run-level reporting, statistical intervals, behavior inspection, and artifacts that let others repeat and challenge the experiment. [evidence-based]

## How It Works

Evaluation starts by defining the scientific question and the estimand, such as final policy return, return at a fixed interaction budget, or area under a learning curve. [evidence-based]

### Protocol and score matrix

1. Fully specify each algorithm, including code revision, architecture, optimizer, hyperparameters, preprocessing, and tuning budget.
2. Freeze the task set, environment versions, wrappers, observation and action transformations, interaction budget, and evaluation schedule before the confirmatory comparison.
3. Run independent training trials under documented random seeds and sources of nondeterminism.
4. Store a run-level score matrix with algorithm, task, run, and evaluation checkpoint as separate dimensions.
5. Define whether evaluation uses a frozen policy or online training behavior, how actions are sampled, how many episodes are used, and how termination and truncation are handled.
6. Preserve returns, episode lengths, wall-clock cost, environment steps, failures, and configuration metadata for every run rather than only a plotted average.

### Aggregation and uncertainty

1. If scores are normalized across tasks, declare the per-task anchors and formula before looking at comparative results.
2. Compute multiple aggregate views because the mean, median, and interquartile mean answer different questions and respond differently to outliers.
3. The interquartile mean averages the middle half of pooled run-level normalized scores, trading some outlier resistance for greater statistical efficiency than the sample median in the setting studied by Agarwal et al.
4. A stratified bootstrap resamples runs within each task, recomputes the aggregate statistic for each bootstrap replicate, and uses the resulting distribution to form an interval estimate.
5. A performance profile plots the fraction of run-task scores exceeding each threshold, exposing more of the distribution than a single scalar.
6. A probability-of-improvement estimate summarizes how often one algorithm's score exceeds another's across the benchmark, with uncertainty reported alongside it.
7. Sample-efficiency curves repeat the chosen aggregate and interval at prespecified interaction budgets instead of reporting only the final checkpoint.

### Reproduction loop

A run manifest records the repository commit, dependency lock, environment build, hardware, accelerator settings, seed, command, configuration, and artifact hashes. [practitioner]

A clean runner reconstructs the environment, executes a small deterministic or tolerance-based smoke test, and then launches the preregistered run matrix. [practitioner]

The analysis consumes immutable run-level data and produces tables and figures from versioned code. A replication changes seeds and, when feasible, implementation or infrastructure so that success is not defined as replaying one favorable random state. [practitioner]

## Key Principles

- A benchmark score is conditional on the complete evaluation protocol, not an intrinsic property of an algorithm name. [evidence-based]
- Deep RL variation arises from random seeds, stochastic environments, implementation choices, network architecture, reward scale, and hyperparameter selection. [evidence-based]
- Finite-run aggregate scores are random variables, so point estimates without interval estimates conceal sampling uncertainty. [evidence-based]
- Selecting the best seeds or showing only favorable tasks introduces selection bias and cannot characterize the population of runs. [evidence-based]
- Mean, median, interquartile mean, probability of improvement, and performance profiles are complementary summaries rather than interchangeable proof of superiority. [evidence-based]
- Benchmark task choice defines the scope of the claim, and broad task counts do not by themselves establish real-world generalization. [practitioner]
- Reproducibility of code and scores is distinct from validity of the reward, environment, benchmark, or scientific conclusion. [practitioner]
- Visual or trajectory-level inspection can reveal policies that obtain return through unintended behavior hidden by the scalar metric. [evidence-based]

## Best Practices

- Write the hypothesis, primary metric, task set, step budget, tuning budget, and exclusion rules before running the final comparison. [practitioner]
- Use multiple independently seeded runs, justify the run count with precision or power goals, and publish every prespecified run including failures. [evidence-based]
- Report raw per-run values plus interval estimates, and include interquartile mean and performance profiles for multi-task few-run comparisons when their assumptions fit. [evidence-based]
- Apply identical environment versions, wrappers, action repeats, stochasticity, evaluation episodes, and termination rules to every compared method. [evidence-based]
- Separate hyperparameter tuning tasks or seeds from final evaluation, and give baselines a comparable tuning budget and implementation quality. [practitioner]
- Save exact configs, dependency locks, code commits, seeds, logs, checkpoints, and analysis scripts in a machine-readable run manifest. [practitioner]
- Inspect videos or trajectories and task-specific diagnostics in addition to return, especially when reward loopholes or local optima are plausible. [evidence-based]
- Re-run headline comparisons on fresh seeds and, for high-impact claims, seek an independent implementation or external replication before promoting them to settled canon. [practitioner]

## Primary Sources

- Peter Henderson, Riashat Islam, Philip Bachman, Joelle Pineau, Doina Precup, and David Meger, 2017 preprint and AAAI 2018, "Deep Reinforcement Learning that Matters," arXiv:1709.06560, [paper](https://arxiv.org/abs/1709.06560), [venue record](https://ojs.aaai.org/index.php/AAAI/article/view/11694).
- Rishabh Agarwal, Max Schwarzer, Pablo Samuel Castro, Aaron C. Courville, and Marc G. Bellemare, 2021, "Deep Reinforcement Learning at the Edge of the Statistical Precipice," NeurIPS 2021, arXiv:2108.13264, [paper](https://arxiv.org/abs/2108.13264), [venue record](https://proceedings.neurips.cc/paper/2021/hash/f514cec81cb148559cf475e7426eed5e-Abstract.html).
- Marlos C. Machado, Marc G. Bellemare, Erik Talvitie, Joel Veness, Matthew Hausknecht, and Michael Bowling, 2018, "Revisiting the Arcade Learning Environment: Evaluation Protocols and Open Problems for General Agents," arXiv:1709.06009, [paper](https://arxiv.org/abs/1709.06009).
- Andrew Patterson, Samuel Neumann, Martha White, and Adam White, 2024, "Empirical Design in Reinforcement Learning," Journal of Machine Learning Research 25(318), [paper](https://www.jmlr.org/papers/v25/23-0183.html).
- Agarwal et al., `rliable` companion implementation, official google-research repository, [source](https://github.com/google-research/rliable).

## Evidence Caveats

- Henderson et al. study selected continuous-control algorithms, environments, and codebases from their period, so their observed effects are not universal constants. [evidence-based]
- Agarwal et al. analyze several major benchmark suites, but the recommended summaries cannot repair a mismatched protocol, biased task selection, tuning leakage, or invalid reward. [evidence-based]
- Bootstrap intervals can under-cover with extremely few runs, a limitation shown for some small-run settings in the statistical-precipice analysis. [evidence-based]
- Interquartile mean is not universally optimal, and trimming can hide scientifically important tail failures that should be reported separately. [evidence-based]
- Task normalization can distort comparisons when anchors are unstable, close together, or semantically inappropriate. [evidence-based]
- Exact numerical reproducibility can still be affected by hardware kernels, library versions, asynchronous execution, and simulator differences. [evidence-based]
- A reproduced benchmark result does not establish causal explanation, deployment safety, robustness outside the task suite, or practical cost-effectiveness. [evidence-based]
- The original google-research `rliable` repository is archived, so its implementation is a reference artifact whose current compatibility must be verified. [evidence-based]

## Brain Hooks

- Folded concept: [[Evaluation, benchmarks, and reproducibility in deep RL]]
- Related canon: [[Debugging RL training runs in practice]]
- Related canon: [[RL tooling landscape (Gymnasium, SB3, CleanRL, RLlib, TRL, veRL, OpenRLHF)]]
- Related canon: [[Deep Q-Networks and value-based deep RL (DQN, Rainbow)]]
- Related canon: [[Trust-region and proximal methods (TRPO, PPO)]]
- Related canon: [[Continuous control (DDPG, TD3, SAC)]]
- Related canon: [[Policy gradient methods and REINFORCE]]
- Related canon: [[Reward design, reward hacking, and specification gaming]]
- Source intake path: [[Source Intake Workflow]]
- Verification path: [[Claim Verification Flow]]

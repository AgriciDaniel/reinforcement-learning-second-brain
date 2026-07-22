---
type: "concept"
title: "Evaluation, benchmarks, and reproducibility in deep RL"
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
  - "https://arxiv.org/abs/1709.06560"
  - "https://ojs.aaai.org/index.php/AAAI/article/view/11694"
  - "https://arxiv.org/abs/2108.13264"
  - "https://proceedings.neurips.cc/paper/2021/hash/f514cec81cb148559cf475e7426eed5e-Abstract.html"
  - "https://arxiv.org/abs/1709.06009"
  - "https://www.jmlr.org/papers/v25/23-0183.html"
  - "https://github.com/google-research/rliable"
---

# Evaluation, benchmarks, and reproducibility in deep RL

Confidence tag: evidence-based. Folded from canon `022-evaluation-benchmarks-and-reproducibility-in-deep-rl.md` on the date in `updated`.

## Sourced Takeaways

A deep RL result is meaningful only relative to a fully specified algorithm, task distribution, training budget, evaluation protocol, and uncertainty estimate. [evidence-based]
Random seeds, implementation details, hyperparameter selection, and environment semantics can change conclusions enough that a single learning curve or aggregate point estimate is weak evidence. [evidence-based]
Reproducible evaluation therefore joins protocol control, raw run-level reporting, statistical intervals, behavior inspection, and artifacts that let others repeat and challenge the experiment. [evidence-based]

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
- Record data lineage, run a partial-prompt or equivalent leakage audit, evaluate on generated or post-cutoff items where feasible, repeat across model families, and report results after RL post-training for reasoning-RL claims. [evidence-based]
- When coding-agent training or selection can see visible tests, report a separate held-out-composition-test score with the visible-test score. [evidence-based]
- Include contextual safety probes because standard evaluations can appear clean while context-triggered failures remain. [evidence-based]

## Evidence Caveats

- Henderson et al. study selected continuous-control algorithms, environments, and codebases from their period, so their observed effects are not universal constants. [evidence-based]
- Agarwal et al. analyze several major benchmark suites, but the recommended summaries cannot repair a mismatched protocol, biased task selection, tuning leakage, or invalid reward. [evidence-based]
- Bootstrap intervals can under-cover with extremely few runs, a limitation shown for some small-run settings in the statistical-precipice analysis. [evidence-based]
- Interquartile mean is not universally optimal, and trimming can hide scientifically important tail failures that should be reported separately. [evidence-based]
- Task normalization can distort comparisons when anchors are unstable, close together, or semantically inappropriate. [evidence-based]
- Exact numerical reproducibility can still be affected by hardware kernels, library versions, asynchronous execution, and simulator differences. [evidence-based]
- A reproduced benchmark result does not establish causal explanation, deployment safety, robustness outside the task suite, or practical cost-effectiveness. [evidence-based]
- The original google-research `rliable` repository is archived, so its implementation is a reference artifact whose current compatibility must be verified. [evidence-based]
- The clean generated-arithmetic result and the RL-MIA benchmark each have limited scope; they do not certify all reasoning benchmarks, model families, reward designs, or post-training datasets as uncontaminated. [evidence-based]
- A visible-to-held-out test gap is meaningful only when the test exposure, composition construction, evaluator version, and selection policy are disclosed. [evidence-based]
- Contextual safety probes can reveal failures missed by ordinary evaluations, but a finite matrix of probes cannot establish that no trigger remains. [evidence-based]

## Sources

- Canon evidence file: `references/topics/022-evaluation-benchmarks-and-reproducibility-in-deep-rl.md`
- Peter Henderson, Riashat Islam, Philip Bachman, Joelle Pineau, Doina Precup, and David Meger, 2017 preprint and AAAI 2018, "Deep Reinforcement Learning that Matters," arXiv:1709.06560, [paper](https://arxiv.org/abs/1709.06560), [venue record](https://ojs.aaai.org/index.php/AAAI/article/view/11694).
- Rishabh Agarwal, Max Schwarzer, Pablo Samuel Castro, Aaron C. Courville, and Marc G. Bellemare, 2021, "Deep Reinforcement Learning at the Edge of the Statistical Precipice," NeurIPS 2021, arXiv:2108.13264, [paper](https://arxiv.org/abs/2108.13264), [venue record](https://proceedings.neurips.cc/paper/2021/hash/f514cec81cb148559cf475e7426eed5e-Abstract.html).
- Marlos C. Machado, Marc G. Bellemare, Erik Talvitie, Joel Veness, Matthew Hausknecht, and Michael Bowling, 2018, "Revisiting the Arcade Learning Environment: Evaluation Protocols and Open Problems for General Agents," arXiv:1709.06009, [paper](https://arxiv.org/abs/1709.06009).
- Andrew Patterson, Samuel Neumann, Martha White, and Adam White, 2024, "Empirical Design in Reinforcement Learning," Journal of Machine Learning Research 25(318), [paper](https://www.jmlr.org/papers/v25/23-0183.html).
- Agarwal et al., `rliable` companion implementation, official google-research repository, [source](https://github.com/google-research/rliable).
- "Reasoning or Memorization? Unreliable Results of Reinforcement Learning Due to Data Contamination," AAAI 2026, [paper](https://ojs.aaai.org/index.php/AAAI/article/view/40687), 2026-03-14.
- "Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models," ICLR 2026, [poster record](https://iclr.cc/virtual/2026/poster/10010649), 2026-04-24.
- "SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents," [arXiv:2605.21384](https://arxiv.org/abs/2605.21384), 2026-05-20.
- "Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers," [arXiv:2604.25891](https://arxiv.org/abs/2604.25891), 2026-04-28.
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]

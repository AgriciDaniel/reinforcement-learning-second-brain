---
type: "concept"
title: "Distributed RL systems and self-play (IMPALA, Ape-X, league training)"
domain: "reinforcement learning: fundamentals, deep RL, RLHF/RLAIF and preference optimization, evaluation, tooling, and applied best practices"
status: "active"
created: "2026-07-22"
updated: "2026-07-22"
tags:
  - "#domain/reinforcement-learning-fundamentals-deep-rl-rlhf-rlaif-and-prefe"
  - "#type/concept"
  - "#confidence/practitioner"
confidence: "practitioner"
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
  - "https://arxiv.org/abs/1802.01561"
  - "https://arxiv.org/abs/1803.00933"
  - "https://arxiv.org/abs/1910.06591"
  - "https://doi.org/10.1038/s41586-019-1724-z"
  - "https://verl.readthedocs.io/en/latest/"
  - "https://arxiv.org/abs/2405.11143"
  - "https://openrlhf.readthedocs.io/en/latest/"
---

# Distributed RL systems and self-play (IMPALA, Ape-X, league training)

Confidence tag: practitioner. Folded from canon `032-distributed-rl-systems-and-self-play-impala-ape-x-league-training.md` on the date in `updated`.

## Sourced Takeaways

Distributed reinforcement learning separates environment interaction, policy inference, experience transport, and parameter updates so each stage can scale according to a different resource bottleneck. [evidence-based]
That separation also changes the learning problem: actors may generate data with older policy parameters, queues and replay may alter the sample distribution, and failures can arise from systems lag rather than the nominal RL objective alone. [evidence-based]
IMPALA, Ape-X, and SEED RL provide distinct reference designs for these tradeoffs, while self-play leagues add a population-management problem whose quality cannot be inferred from throughput alone. [practitioner]

- Scaling environment steps is useful only when the learner, transport path, replay service, and evaluator can absorb the resulting data without uncontrolled lag. [practitioner]
- Actor-policy staleness is an algorithmic variable because it changes the behavior distribution used by the learner. [evidence-based]
- V-trace uses clipped importance weighting to manage off-policy actor trajectories, trading some correction fidelity for bounded variance. [evidence-based]
- Prioritized replay changes which stored samples are learned from, so priority definitions, importance weights, eviction, and shard behavior are part of the method. [evidence-based]
- Centralized inference can improve batching and reduce actor-side model replication, while making latency and service availability part of the control loop. [practitioner]
- Self-play is a data-generation process, whereas league training additionally manages a population and an opponent-selection distribution. [practitioner]
- Higher samples per second does not by itself establish better sample efficiency, wall-clock convergence, reproducibility, or final policy quality. [contested]
- Modern LLM RL stacks share distributed rollout and training motifs with earlier actor-learner systems, but claims of direct inheritance require implementation-specific evidence. [practitioner]

## Best Practices

- Attach a policy-version identifier and behavior log probabilities to every trajectory or response needed by the selected correction rule. [practitioner]
- Log queue depth, sample age, inference latency, actor throughput, learner throughput, replay hit rate, and rejected or dropped data alongside returns and losses. [practitioner]
- Increase actor count, replay capacity, shard count, and learner parallelism one axis at a time while holding the evaluation protocol fixed. [practitioner]
- Test replay priority updates, shard routing, eviction, deduplication, and restart behavior with deterministic fixtures before long runs. [practitioner]
- Compare synchronous and intentionally delayed rollouts to measure the staleness range the implementation can tolerate under the named objective. [practitioner]
- Evaluate self-play policies against frozen historical checkpoints, held-out scripted opponents, and cross-play populations rather than only the latest training opponent. [practitioner]
- Record league membership, opponent-sampling probabilities, checkpoint lineage, payoff data, and retirement decisions so population drift can be audited. [practitioner]
- Pin framework and inference-engine versions, then verify weight synchronization and log-probability semantics end to end before enabling asynchronous LLM rollouts. [practitioner]

## Evidence Caveats

- IMPALA's reported results are tied to its paper's tasks, architecture, optimizer choices, and distributed setup; they do not establish universal gains from actor-learner separation. [contested]
- V-trace reduces the effect of behavior-policy mismatch under its assumptions, but clipping introduces bias and cannot repair corrupted trajectories, missing behavior probabilities, or unlimited lag. [practitioner]
- Ape-X combines distributed acting with prioritized replay and specific value-learning agents, so its empirical comparisons do not isolate every systems component. [evidence-based]
- A sharded replay implementation can approximate priorities, sample unevenly, or lose updates under concurrency; these are implementation risks rather than guarantees of the Ape-X algorithm. [practitioner]
- SEED RL's central-inference results concern the evaluated networks, environments, communication layer, and hardware; different observation sizes or latency constraints can shift the bottleneck. [contested]
- AlphaStar combines human data, multi-agent reinforcement learning, league management, and a domain-specific architecture, which prevents causal attribution of its reported outcome to league training alone. [evidence-based]
- League policies can overfit their own population, and a favorable internal rating need not predict robustness to unseen opponents or rule changes. [practitioner]
- Maintainer documentation is primary evidence for veRL and OpenRLHF interfaces, but not independent evidence of comparative speed, stability, or policy quality. [evidence-based]
- Similar role names across classic RL and LLM post-training can hide different trajectory units, objectives, synchronization rules, and off-policy corrections. [practitioner]
- Distributed benchmarks age with hardware and software stacks, so throughput or cost comparisons require a dated, reproducible configuration and should remain contested across unlike setups. [contested]

## Sources

- Canon evidence file: `references/topics/032-distributed-rl-systems-and-self-play-impala-ape-x-league-training.md`
- Lasse Espeholt et al., 2018, *IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures*, arXiv:1802.01561, [paper](https://arxiv.org/abs/1802.01561).
- Dan Horgan et al., 2018, *Distributed Prioritized Experience Replay*, arXiv:1803.00933, [paper](https://arxiv.org/abs/1803.00933).
- Lasse Espeholt, Raphaël Marinier, Piotr Stanczyk, Ke Wang, and Marcin Michalski, 2019, *SEED RL: Scalable and Efficient Deep-RL with Accelerated Central Inference*, arXiv:1910.06591, [paper](https://arxiv.org/abs/1910.06591).
- Oriol Vinyals et al., 2019, *Grandmaster level in StarCraft II using multi-agent reinforcement learning*, Nature 575, [journal record](https://doi.org/10.1038/s41586-019-1724-z).
- veRL maintainers, [veRL documentation](https://verl.readthedocs.io/en/latest/), official documentation for distributed rollout, worker, and training roles.
- Jian Hu et al., 2024, *OpenRLHF: An Easy-to-use, Scalable and High-performance RLHF Framework*, arXiv:2405.11143, [paper](https://arxiv.org/abs/2405.11143), with [official documentation](https://openrlhf.readthedocs.io/en/latest/).
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]

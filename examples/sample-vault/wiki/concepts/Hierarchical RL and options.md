---
type: "concept"
title: "Hierarchical RL and options"
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
  - "https://www.sciencedirect.com/science/article/pii/S0004370299000521"
  - "https://people.cs.umass.edu/~barto/courses/cs687/Sutton-Precup-Singh-AIJ99.pdf"
---

# Hierarchical RL and options

Confidence tag: evidence-based. Folded from canon `015-hierarchical-rl-and-options.md` on the date in `updated`.

## Sourced Takeaways

Hierarchical reinforcement learning organizes control across time scales, so a policy can choose a temporally extended course of action while a lower-level policy chooses primitive actions. The options framework makes this precise by extending an MDP with closed-loop actions that have explicit initiation and termination rules. It matters because the same representation supports planning, learning, and execution while retaining a formal connection to semi-Markov decision processes.

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

## Evidence Caveats

- The 1999 article establishes a general framework, but many formal convergence statements are tabular and assume finite MDPs, sufficient exploration, and prescribed options.
- The stated convergence result for one-step intra-option Q-learning is for Markov options with deterministic internal policies and requires every primitive action in every state to be executed infinitely often.
- The interruption theorem reasons with the relevant true values. Approximation error can reverse a comparison and trigger a harmful interruption.
- The rooms experiments illustrate favorable planning and learning cases; they do not establish a universal advantage for hierarchy across domains.
- A restricted option set can accelerate coarse planning yet exclude actions needed to solve a changed task, so reuse and optimality can conflict.
- The source leaves option discovery, state abstraction, subtask transfer, and integration with function approximation incompletely resolved.
- Deep learned options add optimization and representation failure modes that the 1999 tabular results do not validate.

## Sources

- Canon evidence file: `references/topics/015-hierarchical-rl-and-options.md`
- Richard S. Sutton, Doina Precup, and Satinder Singh (1999), "Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning," *Artificial Intelligence* 112(1-2). [Publisher record and DOI](https://doi.org/10.1016/S0004-3702(99)00052-1)
- Richard S. Sutton, Doina Precup, and Satinder Singh (1999), author-paper copy of the same article, including the options tuple, SMDP Bellman equations, interruption result, and intra-option methods. [Primary paper PDF](https://people.cs.umass.edu/~barto/courses/cs687/Sutton-Precup-Singh-AIJ99.pdf)
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]

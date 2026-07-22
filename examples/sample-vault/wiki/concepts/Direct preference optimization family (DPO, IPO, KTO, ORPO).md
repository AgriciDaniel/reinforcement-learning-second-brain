---
type: "concept"
title: "Direct preference optimization family (DPO, IPO, KTO, ORPO)"
domain: "reinforcement learning: fundamentals, deep RL, RLHF/RLAIF and preference optimization, evaluation, tooling, and applied best practices"
status: "active"
created: "2026-07-22"
updated: "2026-07-22"
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
  - "https://arxiv.org/abs/2305.18290"
  - "https://proceedings.neurips.cc/paper_files/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract-Conference.html"
  - "https://arxiv.org/abs/2310.12036"
  - "https://proceedings.mlr.press/v238/gheshlaghi-azar24a.html"
  - "https://arxiv.org/abs/2402.01306"
  - "https://proceedings.mlr.press/v235/ethayarajh24a.html"
  - "https://arxiv.org/abs/2403.07691"
  - "https://aclanthology.org/2024.emnlp-main.626/"
---

# Direct preference optimization family (DPO, IPO, KTO, ORPO)

Confidence tag: evidence-based. Folded from canon `019-direct-preference-optimization-family-dpo-ipo-kto-orpo.md` on the date in `updated`.

## Sourced Takeaways

Direct preference optimization methods fit a language-model policy from feedback without the online actor-critic loop used in PPO-based RLHF. [evidence-based]
Their objectives encode different assumptions about pairwise or binary labels, reference policies, and regularization, so DPO, IPO, KTO, and ORPO are not interchangeable names for one loss. [evidence-based]
Published comparisons are tied to particular models, datasets, judges, and training budgets, and do not establish a universal ranking among the family. [contested]

- Direct objectives remove an explicit learned reward model and online policy rollouts from this training stage, but they still encode a model of preference or utility in the loss. [evidence-based]
- DPO, IPO, and ORPO consume pairwise preferences, while KTO can learn from unpaired desirable and undesirable examples. [evidence-based]
- DPO's derivation depends on a reference policy, a KL-regularized objective, and a Bradley-Terry-style model of pairwise preference. [evidence-based]
- IPO was designed to retain a finite regularization-controlled margin when empirical preferences are deterministic or nearly deterministic. [evidence-based]
- KTO's authors explicitly argue that no single human-aware loss is universally superior because the useful inductive bias depends on the setting. [evidence-based]
- ORPO's reference-free objective couples supervised adaptation and preference separation, so its coefficient is not directly comparable with DPO's `beta`. [evidence-based]
- Offline preference coverage, label noise, prompt distribution, and response length can affect every member of the family even when the optimization code is correct. [evidence-based]
- Claims that one family member is the default winner across alignment tasks remain benchmark-dependent and fast-moving. [contested]

## Best Practices

- Define the label contract before training: pairwise winner and loser for DPO, IPO, or ORPO, or explicit desirable and undesirable classes for KTO. [practitioner]
- Apply identical prompt templates, truncation rules, token masking, and sequence aggregation to every response being compared. [practitioner]
- Start from the intended supervised checkpoint and record the exact reference checkpoint whenever the objective uses one. [practitioner]
- Sweep the regularization or preference coefficient together with learning rate, because their numerical meanings differ across objectives and implementations. [practitioner]
- Track chosen and rejected log-probabilities, preference margins, KL to the starting policy, response length, and held-out quality rather than loss alone. [practitioner]
- For KTO, report class balance and class weights, and test whether one label class dominates the effective gradient. [practitioner]
- Compare methods with matched data, initialization, token budget, decoding, evaluation prompts, and multiple random seeds. [evidence-based]
- Stop or investigate when both chosen and rejected likelihoods collapse, the policy drifts sharply, or automated preference gains disagree with human review. [practitioner]

## Evidence Caveats

- The four papers use different model scales, preference corpora, baselines, and evaluators, so their reported results are not a controlled four-way comparison. [contested]
- DPO's equivalence to the stated RLHF objective holds under its preference-model and optimization assumptions, not for arbitrary human preferences or arbitrary implementations. [evidence-based]
- IPO's original large-scale language-model evidence was limited, and its theoretical examples do not by themselves prove superiority in production post-training. [contested]
- KTO's use of a prospect-inspired value function does not prove that text preferences follow the psychology of monetary gambles. [contested]
- ORPO's efficiency and quality findings are specific to its tested setup, and later software or matched implementations can change the tradeoff. [contested]
- Automated judges, response-length effects, data leakage, and selective hyperparameter tuning can distort apparent preference gains. [evidence-based]
- Treat 2025-2026 SOTA or universal-best claims about this family as stale or contested until reproduced under a named current protocol. [contested]

## Sources

- Canon evidence file: `references/topics/019-direct-preference-optimization-family-dpo-ipo-kto-orpo.md`
- Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, and Chelsea Finn, 2023, "Direct Preference Optimization: Your Language Model is Secretly a Reward Model," NeurIPS 2023, arXiv:2305.18290, [paper](https://arxiv.org/abs/2305.18290), [venue record](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract-Conference.html).
- Mohammad Gheshlaghi Azar, Mark Rowland, Bilal Piot, Daniel Guo, Daniele Calandriello, Michal Valko, and Remi Munos, 2023, "A General Theoretical Paradigm to Understand Learning from Human Preferences," arXiv:2310.12036, published at AISTATS 2024, [paper](https://arxiv.org/abs/2310.12036), [venue record](https://proceedings.mlr.press/v238/gheshlaghi-azar24a.html).
- Kawin Ethayarajh, Winnie Xu, Niklas Muennighoff, Dan Jurafsky, and Douwe Kiela, 2024, "KTO: Model Alignment as Prospect Theoretic Optimization," ICML 2024, arXiv:2402.01306, [paper](https://arxiv.org/abs/2402.01306), [venue record](https://proceedings.mlr.press/v235/ethayarajh24a.html).
- Jiwoo Hong, Noah Lee, and James Thorne, 2024, "ORPO: Monolithic Preference Optimization without Reference Model," EMNLP 2024, arXiv:2403.07691, [paper](https://arxiv.org/abs/2403.07691), [venue record](https://aclanthology.org/2024.emnlp-main.626/).
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]

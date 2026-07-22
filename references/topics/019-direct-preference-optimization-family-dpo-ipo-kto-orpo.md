---
type: "canon"
title: "019. Direct preference optimization family (DPO, IPO, KTO, ORPO)"
created: "2026-07-22"
updated: "2026-07-22"
status: "active"
---

# 019. Direct preference optimization family (DPO, IPO, KTO, ORPO)

Ledger: 019 | target: Direct preference optimization family (DPO, IPO, KTO, ORPO) | confidence: evidence-based | fold: [[Direct preference optimization family (DPO, IPO, KTO, ORPO)]] | status: active.

## Core Thesis

Direct preference optimization methods fit a language-model policy from feedback without the online actor-critic loop used in PPO-based RLHF. [evidence-based]
Their objectives encode different assumptions about pairwise or binary labels, reference policies, and regularization, so DPO, IPO, KTO, and ORPO are not interchangeable names for one loss. [evidence-based]
Published comparisons are tied to particular models, datasets, judges, and training budgets, and do not establish a universal ranking among the family. [contested]

## How It Works

Let `x` be a prompt, `y_w` a preferred completion, `y_l` a rejected completion, `pi_theta` the trainable policy, and `pi_ref` a frozen reference policy. [evidence-based]

DPO starts from KL-regularized reward maximization and writes the implicit reward as `beta * log(pi_theta(y|x) / pi_ref(y|x))` plus a prompt-only constant. [evidence-based]

Under the Bradley-Terry preference model, that constant cancels between two responses, and DPO minimizes the binary logistic loss `-log sigmoid(beta * (Delta_theta - Delta_ref))`, where each delta is the chosen-minus-rejected sequence log-probability. [evidence-based]

IPO is the identity special case of the paper's general preference-optimization objective. Its sampled squared loss regresses the same policy-versus-reference log-ratio gap toward a finite margin determined by the regularization strength, rather than driving a separable preference margin without a finite target. [evidence-based]

KTO accepts independently labeled desirable or undesirable completions. It forms an implicit log-ratio reward against a reference policy, compares that reward with a KL-derived reference point, and applies separate logistic value terms and weights to gains and losses. [evidence-based]

KTO's prospect-theoretic framing motivates the shape of its value function, but it does not require a paired chosen and rejected response for every prompt. [evidence-based]

ORPO combines causal language-model negative log-likelihood on the chosen response with a weighted preference term. The preference term is `-log sigmoid(log odds(y_w|x) - log odds(y_l|x))`, using odds derived from average sequence likelihood. [evidence-based]

ORPO trains in one supervised-style stage without a frozen reference model, which changes the source of regularization rather than merely deleting a DPO implementation component. [evidence-based]

The common offline loop is to tokenize labeled examples, compute sequence log-probabilities, construct the method-specific loss, backpropagate through the policy, and evaluate behavior on held-out prompts. [evidence-based]

## Key Principles

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

## Primary Sources

- Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, and Chelsea Finn, 2023, "Direct Preference Optimization: Your Language Model is Secretly a Reward Model," NeurIPS 2023, arXiv:2305.18290, [paper](https://arxiv.org/abs/2305.18290), [venue record](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract-Conference.html).
- Mohammad Gheshlaghi Azar, Mark Rowland, Bilal Piot, Daniel Guo, Daniele Calandriello, Michal Valko, and Remi Munos, 2023, "A General Theoretical Paradigm to Understand Learning from Human Preferences," arXiv:2310.12036, published at AISTATS 2024, [paper](https://arxiv.org/abs/2310.12036), [venue record](https://proceedings.mlr.press/v238/gheshlaghi-azar24a.html).
- Kawin Ethayarajh, Winnie Xu, Niklas Muennighoff, Dan Jurafsky, and Douwe Kiela, 2024, "KTO: Model Alignment as Prospect Theoretic Optimization," ICML 2024, arXiv:2402.01306, [paper](https://arxiv.org/abs/2402.01306), [venue record](https://proceedings.mlr.press/v235/ethayarajh24a.html).
- Jiwoo Hong, Noah Lee, and James Thorne, 2024, "ORPO: Monolithic Preference Optimization without Reference Model," EMNLP 2024, arXiv:2403.07691, [paper](https://arxiv.org/abs/2403.07691), [venue record](https://aclanthology.org/2024.emnlp-main.626/).

## Evidence Caveats

- The four papers use different model scales, preference corpora, baselines, and evaluators, so their reported results are not a controlled four-way comparison. [contested]
- DPO's equivalence to the stated RLHF objective holds under its preference-model and optimization assumptions, not for arbitrary human preferences or arbitrary implementations. [evidence-based]
- IPO's original large-scale language-model evidence was limited, and its theoretical examples do not by themselves prove superiority in production post-training. [contested]
- KTO's use of a prospect-inspired value function does not prove that text preferences follow the psychology of monetary gambles. [contested]
- ORPO's efficiency and quality findings are specific to its tested setup, and later software or matched implementations can change the tradeoff. [contested]
- Automated judges, response-length effects, data leakage, and selective hyperparameter tuning can distort apparent preference gains. [evidence-based]
- Treat 2025-2026 SOTA or universal-best claims about this family as stale or contested until reproduced under a named current protocol. [contested]

## Brain Hooks

- Folded concept: [[Direct preference optimization family (DPO, IPO, KTO, ORPO)]]
- Related canon: [[RLHF reward models and PPO post-training (InstructGPT lineage)]]
- Related canon: [[RLAIF and Constitutional AI]]
- Related canon: [[GRPO and RL with verifiable rewards for reasoning models]]
- Related canon: [[Reward design, reward hacking, and specification gaming]]
- Related canon: [[Evaluation, benchmarks, and reproducibility in deep RL]]
- Related canon: [[Debugging RL training runs in practice]]
- Related canon: [[RL tooling landscape (Gymnasium, SB3, CleanRL, RLlib, TRL, veRL, OpenRLHF)]]
- Related canon: [[Trust-region and proximal methods (TRPO, PPO)]]
- Source intake path: [[Source Intake Workflow]]
- Verification path: [[Claim Verification Flow]]

---
type: "canon"
title: "021. RLAIF and Constitutional AI"
created: "2026-07-22"
updated: "2026-07-22"
status: "active"
---

# 021. RLAIF and Constitutional AI

Ledger: 021 | target: RLAIF and Constitutional AI | confidence: evidence-based | fold: [[RLAIF and Constitutional AI]] | status: active.

## Core Thesis

Reinforcement learning from AI feedback, or RLAIF, uses model-generated judgments as preference labels or rewards for training another policy. [evidence-based]
Constitutional AI is a specific RLAIF-centered design that makes desired behavior explicit in a written set of principles and combines self-critique, revision, supervised fine-tuning, and reinforcement learning. [evidence-based]
The approach can reduce dependence on repeated human preference labeling, but it relocates human judgment into the constitution, feedback-model setup, data distribution, and independent evaluation rather than removing it. [evidence-based]

## How It Works

The main inputs are an initial policy, a prompt distribution, a written constitution, and a model capable of applying those principles as feedback. [evidence-based]

### Constitutional supervised phase

1. Sample an initial response to a prompt, including prompts designed to expose harmful or evasive behavior.
2. Select a constitutional principle and ask a model to critique the response against that principle.
3. Ask the model to revise the response in light of the critique.
4. Repeat critique and revision when the design calls for multiple passes.
5. Fine-tune the initial policy on the revised responses, while retaining task data needed for helpful behavior.
6. Use the resulting supervised constitutional policy to initialize the later RL phase.

### AI preference and reinforcement-learning phase

1. Sample two candidate responses for a prompt from a policy snapshot.
2. Condition an AI labeler on task instructions or constitutional principles and ask it to compare the candidates.
3. Convert the labeler's probabilities for the two choices into a soft preference distribution over candidate A and candidate B.
4. Reverse candidate order and average the two distributions when counterbalancing position bias, as in Lee et al.
5. Train a reward model that scores each prompt-response pair.
6. Use soft pairwise cross-entropy to match the AI preference distribution to the softmax of the two reward scores.
7. With a hard preferred response, this becomes the usual logistic pairwise loss on the preferred-minus-rejected reward-score difference.
8. Optimize the policy for expected reward-model score minus a weighted Kullback-Leibler divergence penalty from a reference policy.
9. The cited implementations use policy-gradient training, but RLAIF is defined by the source of feedback rather than one policy optimizer.

### Direct RLAIF variant

Direct RLAIF omits the separately trained reward model. [evidence-based]

The AI labeler assigns a rating distribution to each generated response during RL, and the expected normalized rating becomes the sequence-level reward. [evidence-based]

This can reduce reward-model staleness while increasing dependence on online labeler inference and the labeler's current failure modes. [evidence-based]

## Key Principles

- Constitutional AI has both a supervised self-revision stage and an AI-feedback RL stage, so equating it only with reward-model training omits half of the proposed pipeline. [evidence-based]
- The constitution is an explicit specification artifact whose wording and coverage influence critiques, labels, and ultimately policy behavior. [evidence-based]
- RLAIF replaces some human comparison labels with AI judgments, but people still choose principles, prompts, labeler configuration, and evaluation criteria. [evidence-based]
- Soft AI preferences can be distilled into a reward model through pairwise cross-entropy instead of collapsing every judgment to a hard label. [evidence-based]
- AI labelers can exhibit candidate-position bias, and counterbalancing response order is an empirically motivated control. [evidence-based]
- Prompt detail, exemplars, labeler rationales, and labeler scale can change agreement with human preferences, with effects that vary by task. [evidence-based]
- A policy optimized against AI feedback is still optimizing a learned proxy, so agreement tests and adversarial evaluation remain necessary. [practitioner]

## Best Practices

- Version the constitution with stable identifiers, rationale, ownership, conflict-resolution rules, and an evaluation mapped to every high-risk principle. [practitioner]
- Calibrate the AI labeler on held-out human judgments before generating a large preference set, and report agreement by task and risk slice. [practitioner]
- Counterbalance candidate order, inspect ties and low-margin judgments, and preserve soft preference probabilities when the serving interface exposes them. [evidence-based]
- Sample preference pairs from multiple policy snapshots and difficult prompt slices so the reward model is not trained only on outputs from the initial policy. [practitioner]
- Evaluate the feedback model and the trained policy separately, using independent human review for final helpfulness, harmlessness, and over-refusal judgments. [evidence-based]
- Monitor reward, Kullback-Leibler divergence, response length, refusal rate, and slice-level behavior together because one aggregate score can hide proxy exploitation. [practitioner]
- Treat rationale prompting and direct RLAIF as design choices to validate per task, not as universal improvements over simpler labeling or a distilled reward model. [contested]

## Primary Sources

- Yuntao Bai et al., 2022, "Constitutional AI: Harmlessness from AI Feedback," arXiv:2212.08073, [paper](https://arxiv.org/abs/2212.08073).
- Harrison Lee et al., 2023, "RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback," arXiv:2309.00267, published at ICML 2024, [paper](https://arxiv.org/abs/2309.00267), [venue record](https://proceedings.mlr.press/v235/lee24t.html).

## Evidence Caveats

- Bai et al. study harmless assistant behavior in a particular model and data setting, not every interpretation of helpfulness, honesty, or harmlessness. [evidence-based]
- The absence of human harmlessness labels in that experiment does not mean an absence of human-authored principles, helpfulness data, prompt design, or human evaluation. [evidence-based]
- Lee et al. compare summarization and selected dialogue tasks, so the results do not establish RLAIF and RLHF equivalence across model families, languages, or deployment risks. [contested]
- Constitutional principles can be incomplete, mutually conflicting, culturally narrow, or vulnerable to a labeler's misinterpretation. [practitioner]
- High agreement with a finite human preference set does not prove that either the AI labeler or that set captures the intended specification or rare harms. [evidence-based]
- A distilled reward model can become stale as the policy distribution moves, while direct scoring can be costly and can expose training to labeler drift. [evidence-based]
- Neither source proves robustness to adaptive attacks, elimination of reward hacking, or safety in high-stakes deployment. [evidence-based]
- Comparative claims about RLAIF cost, quality, or scalability remain conditional on labeler access, inference prices, annotation protocols, and the evaluated task. [contested]

## Brain Hooks

- Folded concept: [[RLAIF and Constitutional AI]]
- Related canon: [[RLHF reward models and PPO post-training (InstructGPT lineage)]]
- Related canon: [[Direct preference optimization family (DPO, IPO, KTO, ORPO)]]
- Related canon: [[Reward design, reward hacking, and specification gaming]]
- Related canon: [[Evaluation, benchmarks, and reproducibility in deep RL]]
- Related canon: [[Policy gradient methods and REINFORCE]]
- Related canon: [[Trust-region and proximal methods (TRPO, PPO)]]
- Related canon: [[Imitation learning and inverse RL]]
- Source intake path: [[Source Intake Workflow]]
- Verification path: [[Claim Verification Flow]]

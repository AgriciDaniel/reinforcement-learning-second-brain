---
type: "concept"
title: "RLHF reward models and PPO post-training (InstructGPT lineage)"
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
  - "https://arxiv.org/abs/1706.03741"
  - "https://arxiv.org/abs/1707.06347"
  - "https://arxiv.org/abs/1909.08593"
  - "https://proceedings.neurips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html"
  - "https://proceedings.neurips.cc/paper_files/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract.html"
---

# RLHF reward models and PPO post-training (InstructGPT lineage)

Confidence tag: evidence-based. Folded from canon `018-rlhf-reward-models-and-ppo-post-training-instructgpt-lineage.md` on the date in `updated`.

## Sourced Takeaways

RLHF converts human judgments into a learned reward signal and then optimizes a policy against that signal, usually while constraining drift from a supervised reference policy.
In the InstructGPT lineage, the operational pipeline is pretrained language modeling, supervised fine-tuning on demonstrations, reward modeling from ranked completions, and PPO policy optimization with a KL control term.
The method can make model behavior better match the sampled labeler preferences, but neither the reward model nor PPO equates those preferences with a complete or universal account of human intent.

- Preference learning replaces a hand-coded reward with an estimated model of judgments from a specified data-generating process; it does not eliminate reward misspecification. [evidence-based]
- Demonstrations train the initial behavior policy, whereas comparisons train the reward model, so the two datasets play different statistical and operational roles. [evidence-based]
- Christiano et al. used A2C and TRPO in the original deep human-preference experiments; PPO entered this lineage through later policy-optimization and language-model work. [evidence-based]
- A pairwise reward model learns relative preference evidence, and its scalar outputs are not intrinsically calibrated utilities with an absolute zero. [evidence-based]
- KL control reduces departure from the reference distribution but does not guarantee factuality, harmlessness, or agreement beyond the feedback population. [evidence-based]
- Stiennon et al. observed that stronger optimization could increase predicted reward after actual human preference had begun to decline, directly demonstrating reward-model overoptimization in their setting. [evidence-based]
- InstructGPT aligned behavior to the stated preferences of its labelers and researchers, not to an unspecified aggregate called universal human values. [evidence-based]
- PPO is one optimizer for learned reward and is not conceptually required for every system described as RLHF. [evidence-based]

## Best Practices

- Define the target behavior, conflict-resolution rules, abstention policy, and labeling rubric before collecting demonstrations or comparisons. [practitioner]
- Measure labeler agreement and disagreement by task and safety category, preserve annotator provenance, and evaluate with genuinely held-out labelers when cross-rater generalization matters. [evidence-based]
- Generate comparison candidates with enough policy, checkpoint, and decoding diversity to expose meaningful quality differences without making preferences trivial. [practitioner]
- Validate reward models beyond aggregate pairwise accuracy using calibration, subgroup slices, adversarial candidates, length controls, and high-score samples from the current policy. [practitioner]
- Sweep the KL coefficient, PPO clip range, learning rate, rollout batch size, and update epochs together; monitor achieved KL and human quality rather than copying paper settings across scales. [practitioner]
- Normalize rewards and advantages deliberately, use a stable value baseline, cap gradient norms, and watch policy entropy, clip fraction, value error, and response length for optimization pathologies. [practitioner]
- Select checkpoints on blinded human evaluation and independent capability and safety suites, not reward-model score alone. [evidence-based]
- If mixing pretraining gradients to retain capabilities, treat the mix weight as a measured tradeoff and verify that it does not erase the target preference gains. [evidence-based]

## Evidence Caveats

- The cited results concern particular simulated-control, Atari, summarization, and API-prompt distributions; they do not establish universal effectiveness across tasks, languages, model families, or deployment contexts.
- Human comparisons encode the rubric, information, incentives, skill, and demographic coverage of the people providing them, and disagreement cannot be reduced to label noise by default.
- Reward-model validation on a static split can overstate reliability after PPO changes the response distribution.
- KL penalties and PPO clipping control optimization geometry, but neither is a proof that the learned objective is correct or that unsafe behavior is excluded.
- Stiennon et al.'s overoptimization analysis shows a failure can occur, but it does not identify one universal KL target or stopping rule.
- InstructGPT reported remaining instruction-following errors and limitations in bias, truthfulness, and safety, so preference wins should not be read as a complete alignment result.
- PPO-ptx reduced selected capability regressions in the InstructGPT experiments; its effect depends on the pretraining distribution, evaluation suite, and mixture strength.
- Later preference-optimization families may remove the explicit online PPO stage, but they introduce different assumptions and are outside the evidence established by this lineage.

## Sources

- Canon evidence file: `references/topics/018-rlhf-reward-models-and-ppo-post-training-instructgpt-lineage.md`
- Paul F. Christiano, Jan Leike, Tom B. Brown, Miljan Martic, Shane Legg, and Dario Amodei (2017), *Deep Reinforcement Learning from Human Preferences*, arXiv:1706.03741: https://arxiv.org/abs/1706.03741
- John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov (2017), *Proximal Policy Optimization Algorithms*, arXiv:1707.06347: https://arxiv.org/abs/1707.06347
- Daniel M. Ziegler, Nisan Stiennon, Jeffrey Wu, Tom B. Brown, Alec Radford, Dario Amodei, Paul Christiano, and Geoffrey Irving (2019), *Fine-Tuning Language Models from Human Preferences*, arXiv:1909.08593: https://arxiv.org/abs/1909.08593
- Nisan Stiennon, Long Ouyang, Jeffrey Wu, Daniel M. Ziegler, Ryan Lowe, Chelsea Voss, Alec Radford, Dario Amodei, and Paul Christiano (2020), *Learning to Summarize from Human Feedback*, NeurIPS 2020, arXiv:2009.01325: https://proceedings.neurips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html
- Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, et al. (2022), *Training Language Models to Follow Instructions with Human Feedback*, NeurIPS 2022, arXiv:2203.02155: https://proceedings.neurips.cc/paper_files/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract.html
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]

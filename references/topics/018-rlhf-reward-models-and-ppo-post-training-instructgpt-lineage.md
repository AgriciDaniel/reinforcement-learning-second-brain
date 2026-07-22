---
type: "canon"
title: "018. RLHF reward models and PPO post-training (InstructGPT lineage)"
created: "2026-07-22"
updated: "2026-07-22"
status: "active"
---

# 018. RLHF reward models and PPO post-training (InstructGPT lineage)

Ledger: 018 | target: RLHF reward models and PPO post-training (InstructGPT lineage) | confidence: evidence-based | fold: [[RLHF reward models and PPO post-training (InstructGPT lineage)]] | status: active.

## Core Thesis

RLHF converts human judgments into a learned reward signal and then optimizes a policy against that signal, usually while constraining drift from a supervised reference policy.
In the InstructGPT lineage, the operational pipeline is pretrained language modeling, supervised fine-tuning on demonstrations, reward modeling from ranked completions, and PPO policy optimization with a KL control term.
The method can make model behavior better match the sampled labeler preferences, but neither the reward model nor PPO equates those preferences with a complete or universal account of human intent.

## How It Works

The lineage contains distinct algorithmic stages that should not be collapsed into one paper.
Christiano et al. established a deep preference-learning loop for Atari and simulated control, fitting rewards from short trajectory comparisons while training policies with A2C or TRPO.
Ziegler et al. transferred learned human-preference rewards to language-model fine-tuning.
Stiennon et al. developed the supervised model, pairwise reward model, PPO, and KL-regularized policy recipe for summarization.
Ouyang et al. applied that recipe to a broad distribution of instructions and named the resulting models InstructGPT.

Given a prompt \(x\), two completions \(y_w\) and \(y_l\), and a label that \(y_w\) is preferred, a scalar reward model \(r_\phi(x,y)\) uses a Bradley-Terry-style preference probability:

$$
P_\phi(y_w \succ y_l\mid x)=\sigma\left(r_\phi(x,y_w)-r_\phi(x,y_l)\right).
$$

The pairwise negative log-likelihood is

$$
\mathcal{L}_{\mathrm{RM}}(\phi)=-\mathbb{E}_{(x,y_w,y_l)}\log\sigma\left(r_\phi(x,y_w)-r_\phi(x,y_l)\right).
$$

Only score differences enter this loss, so an additive reward offset is unidentifiable.
Implementations therefore need an explicit normalization convention before policy optimization.
Rankings among several samples can be decomposed into comparisons, but comparisons created from the same prompt are correlated and should be batched or weighted with that structure in mind.

For language generation, the prompt supplies context and each generated token is an action.
The episode ends at a stop condition, and the learned reward is usually assigned to the completed response.
A KL-controlled sequence score can be written as

$$
R(x,y)=r_\phi(x,y)-\beta\log\frac{\pi_\theta(y\mid x)}{\pi_{\mathrm{ref}}(y\mid x)},
$$

with the log-ratio implemented as token-level contributions.
In expectation, the control term penalizes divergence from the reference policy, discouraging the policy from moving rapidly into regions where the reward model has little comparison data.

PPO updates use samples from the current or recent policy.
For token step \(t\), define the importance ratio \(\rho_t(\theta)=\pi_\theta(a_t\mid s_t)/\pi_{\theta_{\mathrm{old}}}(a_t\mid s_t)\).
The clipped surrogate is

$$
L^{\mathrm{clip}}(\theta)=\mathbb{E}_t\left[\min\left(\rho_t\hat A_t,\operatorname{clip}(\rho_t,1-\epsilon,1+\epsilon)\hat A_t\right)\right].
$$

A learned value function supplies baselines for advantage estimates, while clipping limits the incentive for a single batch to induce a large likelihood-ratio update.
The KL reward penalty and PPO clipping are separate controls: the first anchors behavior to a reference model, and the second constrains optimization relative to the rollout policy.

The end-to-end training loop is:

1. Pretrain a causal language model on next-token prediction.
2. Collect high-quality demonstrations for target prompts and supervised-fine-tune a reference policy.
3. Sample multiple candidate completions from one or more policy checkpoints and ask trained labelers to rank them under a documented rubric.
4. Fit and validate the reward model on held-out prompts, users, policies, and labelers where the intended generalization requires those splits.
5. Roll out the policy on prompts, compute reward-model scores and KL penalties, estimate token-level advantages, and run multiple PPO minibatch epochs.
6. Monitor held-out human preference, KL, response statistics, reward calibration, and capability evaluations, then stop before proxy optimization outruns external quality.
7. Refresh comparison data on stronger policy outputs when the deployed training design calls for another reward-model and policy iteration.

InstructGPT's PPO-ptx variant additionally mixed gradients from the pretraining objective into PPO updates to reduce regressions on the public NLP evaluations studied in that paper.
That auxiliary objective is a retention mechanism, not part of the definition of RLHF.

## Key Principles

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

## Primary Sources

- Paul F. Christiano, Jan Leike, Tom B. Brown, Miljan Martic, Shane Legg, and Dario Amodei (2017), *Deep Reinforcement Learning from Human Preferences*, arXiv:1706.03741: https://arxiv.org/abs/1706.03741
- John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov (2017), *Proximal Policy Optimization Algorithms*, arXiv:1707.06347: https://arxiv.org/abs/1707.06347
- Daniel M. Ziegler, Nisan Stiennon, Jeffrey Wu, Tom B. Brown, Alec Radford, Dario Amodei, Paul Christiano, and Geoffrey Irving (2019), *Fine-Tuning Language Models from Human Preferences*, arXiv:1909.08593: https://arxiv.org/abs/1909.08593
- Nisan Stiennon, Long Ouyang, Jeffrey Wu, Daniel M. Ziegler, Ryan Lowe, Chelsea Voss, Alec Radford, Dario Amodei, and Paul Christiano (2020), *Learning to Summarize from Human Feedback*, NeurIPS 2020, arXiv:2009.01325: https://proceedings.neurips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html
- Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, et al. (2022), *Training Language Models to Follow Instructions with Human Feedback*, NeurIPS 2022, arXiv:2203.02155: https://proceedings.neurips.cc/paper_files/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract.html

## Evidence Caveats

- The cited results concern particular simulated-control, Atari, summarization, and API-prompt distributions; they do not establish universal effectiveness across tasks, languages, model families, or deployment contexts.
- Human comparisons encode the rubric, information, incentives, skill, and demographic coverage of the people providing them, and disagreement cannot be reduced to label noise by default.
- Reward-model validation on a static split can overstate reliability after PPO changes the response distribution.
- KL penalties and PPO clipping control optimization geometry, but neither is a proof that the learned objective is correct or that unsafe behavior is excluded.
- Stiennon et al.'s overoptimization analysis shows a failure can occur, but it does not identify one universal KL target or stopping rule.
- InstructGPT reported remaining instruction-following errors and limitations in bias, truthfulness, and safety, so preference wins should not be read as a complete alignment result.
- PPO-ptx reduced selected capability regressions in the InstructGPT experiments; its effect depends on the pretraining distribution, evaluation suite, and mixture strength.
- Later preference-optimization families may remove the explicit online PPO stage, but they introduce different assumptions and are outside the evidence established by this lineage.

## Brain Hooks

- Folded concept: [[RLHF reward models and PPO post-training (InstructGPT lineage)]]
- Objective misspecification and reward-model gaming: [[Reward design, reward hacking, and specification gaming]]
- PPO mechanics and update constraints: [[Trust-region and proximal methods (TRPO, PPO)]]
- Gradient-estimator foundation: [[Policy gradient methods and REINFORCE]]
- Value baselines and advantage estimation: [[Actor-critic methods (A2C A3C, GAE)]]
- Explicit-policy-optimization alternatives: [[Direct preference optimization family (DPO, IPO, KTO, ORPO)]]
- AI-generated feedback extension: [[RLAIF and Constitutional AI]]
- Evaluation and seed discipline: [[Evaluation, benchmarks, and reproducibility in deep RL]]
- Training-run diagnosis: [[Debugging RL training runs in practice]]
- Implementation ecosystem: [[RL tooling landscape (Gymnasium, SB3, CleanRL, RLlib, TRL, veRL, OpenRLHF)]]
- Source intake path: [[Source Intake Workflow]]
- Verification path: [[Claim Verification Flow]]

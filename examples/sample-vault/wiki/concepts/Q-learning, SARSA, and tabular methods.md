---
type: "concept"
title: "Q-learning, SARSA, and tabular methods"
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
  - "https://mitpress.mit.edu/9780262039246/reinforcement-learning/"
  - "http://incompleteideas.net/book/RLbook2020.pdf"
  - "https://doi.org/10.1007/BF00992698"
  - "http://mi.eng.cam.ac.uk/reports/svr-ftp/auto-pdf/rummery_tr166.pdf"
---

# Q-learning, SARSA, and tabular methods

Confidence tag: evidence-based. Folded from canon `004-q-learning-sarsa-and-tabular-methods.md` on the date in `updated`.

## Sourced Takeaways

Q-learning and SARSA are one-step temporal-difference control algorithms that learn tabular action values from experience without requiring a transition model. SARSA evaluates and improves the policy that generates its next action, while Q-learning learns toward a greedy target independently of a potentially exploratory behavior policy. This on-policy versus off-policy distinction determines the update target, the policy whose value is learned, and the conditions needed for reliable control.

- SARSA is on-policy when its behavior and target policies are the same, because its update uses the action actually selected by that policy. [evidence-based]
- Q-learning is off-policy because its greedy target can differ from the policy that generated the transition. [evidence-based]
- The policy used to collect data and the policy represented in the update target must be documented separately. [practitioner]
- A constant nonzero exploration rate means on-policy SARSA learns the value of an exploratory policy, not the value of the corresponding fully greedy policy. [evidence-based]
- The tabular Q-learning convergence theorem does not justify arbitrary constant step sizes, insufficient visitation, nonstationary dynamics, or nonlinear approximators. [evidence-based]
- Expected SARSA removes next-action sampling variance but still inherits randomness from transitions, rewards, and earlier estimates. [evidence-based]
- Maximization bias arises when noisy estimates are both compared and used to evaluate the selected maximum. [evidence-based]
- Optimistic initial values can induce exploration in stationary tasks, but their influence fades and they do not solve general nonstationary exploration. [evidence-based]

## Best Practices

- Initialize terminal-state action values consistently and omit the bootstrap term whenever the environment reports true termination. [evidence-based]
- Distinguish termination from an external time limit, because treating every truncation as terminal changes the value target. [practitioner]
- Randomize greedy ties to prevent table order from silently imposing a behavioral preference. [practitioner]
- Use a decaying exploration schedule only when it preserves enough visitation for the intended convergence claim, and report the complete schedule. [evidence-based]
- Tune the step size jointly with exploration and reward scale, then compare learning curves across several seeds rather than selecting one favorable run. [practitioner]
- Use SARSA when the value of exploratory behavior itself is the control object, and use Q-learning when a distinct greedy target policy matches the objective. [practitioner]
- Consider Expected SARSA when next-action noise is undesirable and the target-policy expectation is cheap to compute. [practitioner]
- Add Double Q-learning when maximization bias is visible, but verify its effect empirically rather than assuming every positive value error comes from maximization. [practitioner]

## Evidence Caveats

- Classical convergence guarantees are asymptotic and assumption-dependent, so they do not specify useful finite-sample performance or a practical stopping time. [evidence-based]
- The textbook's cliff-walking examples explain a policy distinction but do not establish that SARSA is generally safer or that Q-learning is generally more reward-efficient. [evidence-based]
- Seed variance can arise from exploratory action choices, stochastic transitions and rewards, initialization, and random tie breaking, even with a small table. [practitioner]
- A single final greedy evaluation can conceal unstable learning, poor state-action coverage, or sensitivity to the exploration schedule. [practitioner]
- Tabular guarantees do not transfer unchanged to replay buffers, target networks, deep function approximation, or offline data. [evidence-based]
- The cited sources do not prove a universal advantage for Q-learning, SARSA, Expected SARSA, or Double Q-learning across tasks. [evidence-based]

## Sources

- Canon evidence file: `references/topics/004-q-learning-sarsa-and-tabular-methods.md`
- Richard S. Sutton and Andrew G. Barto (2018), *Reinforcement Learning: An Introduction*, second edition, Chapter 6, The MIT Press: https://mitpress.mit.edu/9780262039246/reinforcement-learning/
- Richard S. Sutton and Andrew G. Barto (2020), complete second-edition author-hosted text: http://incompleteideas.net/book/RLbook2020.pdf
- Christopher J. C. H. Watkins and Peter Dayan (1992), “Q-learning,” *Machine Learning* 8, DOI: https://doi.org/10.1007/BF00992698
- Gavin A. Rummery and Mahesan Niranjan (1994), *On-line Q-learning Using Connectionist Systems*, Cambridge University Engineering Department Technical Report CUED/F-INFENG/TR 166: http://mi.eng.cam.ac.uk/reports/svr-ftp/auto-pdf/rummery_tr166.pdf
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]

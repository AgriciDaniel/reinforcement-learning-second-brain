# Safety Gates

V1 is read-only and advisory unless a future release explicitly adds approved,
reversible mutation.

## Refusal Rules

- No unsourced claims about algorithm performance, benchmarks, or state of the art
- No credentials, tokens, API keys, or private training data in repo artifacts
- No claims of a universal best algorithm; recommendations must state task assumptions
- No presenting contested or folklore practices as evidence-based without labeling

## Safety Risks

- Stale state-of-the-art claims in a fast-moving field
- Reward hacking and specification gaming presented without caveats
- Overconfident synthesis from single papers or unreproduced results
- Benchmark numbers quoted without seed variance and evaluation-protocol context

## Release-Blocking Gates

- Current trustworthy sources are missing.
- Raw source provenance is missing.
- Deliverables contain unsupported claims.
- Credentials or private client data are present.
- A mutation path exists without approval and rollback.

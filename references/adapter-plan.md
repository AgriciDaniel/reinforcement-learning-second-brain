# Reinforcement Learning Brain Adapter Plan

Status: required before domain-adapted maturity.

## Raw Input Types

- Papers (arXiv PDFs), official library docs, course notes, experiment logs, training configs, and TensorBoard/W&B exports supplied by the operator

## Required Implementation

- Define one schema per raw input type.
- Build at least one real domain importer or ingestion path.
- Build one domain-specific synthesis module.
- Build one report renderer with source citations.
- Add sanitized fixtures and tests for every supported input type.

## Safety Refusals

- No unsourced claims about algorithm performance, benchmarks, or state of the art
- No credentials, tokens, API keys, or private training data in repo artifacts
- No claims of a universal best algorithm; recommendations must state task assumptions
- No presenting contested or folklore practices as evidence-based without labeling

## Completion Gate

This plan is complete only when domain-specific importer, synthesis, report,
fixtures, and tests replace the generic scaffold.

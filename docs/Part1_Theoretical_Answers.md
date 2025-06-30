# Part 1: Theoretical Analysis (30%)

## Q1: AI-driven code generation tools

### How they reduce development time

**Context-aware autocomplete**
By analyzing surrounding code and comments, tools like Copilot can suggest whole lines or blocks, cutting boilerplate and repetitive patterns.

**Instant scaffolding**
They can spin up function stubs, tests, or common data-processing pipelines in seconds.

**Learning from vast corpora**
They encapsulate community best practices, so you get idiomatic code rather than reinventing wheels.

### Limitations

- **Accuracy & correctness:** Suggestions may compile but contain subtle bugs or security holes.
- **Context gaps:** They can't fully "understand" domain-specific logic or architecture decisions.
- **Over-reliance:** Blindly accepting suggestions can erode deep understanding and lead to technical debt.

## Q2: Supervised vs. Unsupervised in automated bug detection

| Aspect | Supervised | Unsupervised |
|--------|------------|--------------|
| **Data** | Labeled examples ("bug" vs. "no-bug") | Unlabeled code changes or issue data |
| **Approach** | Train classifiers (e.g., Random Forest) to flag bugs | Cluster or anomaly detection to surface outliers |
| **Pros** | High precision if labels are abundant | Finds novel / unknown bug patterns without labels |
| **Cons** | Requires costly labeling; may miss new bug types | Higher false-positive rate; harder to interpret clusters |

## Q3: Why bias mitigation is critical in UX personalization

**Fair access:** If your model over-recommends certain layouts/styles to one demographic, others get degraded experiences.

**Regulatory compliance:** Laws (GDPR, etc.) increasingly demand fairness and explainability in user-facing algorithms.

**Business trust:** Users notice and reject biased experiences; mitigating bias preserves brand integrity.

## Case Study: AIOps in Deployment Pipelines

### How AIOps improves efficiency

**Automated anomaly detection:** Continuously monitors logs/metrics and automatically rolls back or alerts only on actionable issues, reducing mean-time-to-repair.

**Intelligent change recommendations:** By analyzing past deployments and failures, AIOps can suggest optimal rollout strategies (canary vs. blue-green) or tuning parameters, cutting down manual tuning cycles.
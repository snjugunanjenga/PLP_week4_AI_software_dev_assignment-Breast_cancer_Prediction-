# Task 1 Performance Analysis

This analysis compares the manual sorting implementation with the AI-suggested version.

Both approaches leverage Python’s built-in `sorted()` function and custom key functions, achieving the same time complexity of O(n log n). The **AI version** uses a single lambda with an `infinity` default (`float('inf')`) so that dictionaries missing the sort key naturally fall at the end. Its lean code has minimal branching, making it slightly faster in homogeneous data sets and easier to read.

The **manual version** adds robustness through exception handling: if values of mixed types cause a `TypeError`, it falls back to converting all keys to strings before sorting. This extra layer allows it to gracefully handle lists mixing integers, strings, or other value types, at the cost of a small performance hit due to the conversion and exception overhead.

In practice, if your data is consistent (all numeric or all string for the sort key), the AI-suggested snippet will be more efficient and concise. If there’s uncertainty in data types, the manual implementation’s safety net prevents runtime errors. Choosing between them depends on your domain: for high-performance pipelines with guaranteed clean data, lean AI code wins; for heterogeneous or messy inputs, the manual approach offers greater resilience.


## Screenshot

![My screenshot](../src/code_completion/manual_vs_ai.png)

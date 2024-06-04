# Causal Inference Methods Documentation

This repository aims to provide a comprehensive collection of methods for performing causal inference, including experimental designs, statistical methods, and advanced machine learning techniques. Each method will be implemented and documented with examples.

## Table of Contents

1. [Introduction](#introduction)
2. [Methods](#methods)
    - [Experimental Methods](#experimental-methods)
    - [Quasi-Experimental Methods](#quasi-experimental-methods)
    - [Matching and Reweighting Methods](#matching-and-reweighting-methods)
    - [Graphical and Structural Methods](#graphical-and-structural-methods)
    - [Machine Learning and Advanced Statistical Methods](#machine-learning-and-advanced-statistical-methods)
    - [Time-Series and Panel Data Methods](#time-series-and-panel-data-methods)
    - [Mediation and Moderation Analysis](#mediation-and-moderation-analysis)
    - [Sensitivity Analysis and Robustness Checks](#sensitivity-analysis-and-robustness-checks)
    - [Advanced Reweighting and Balancing Methods](#advanced-reweighting-and-balancing-methods)
    - [Instrumental Variable Extensions](#instrumental-variable-extensions)
    - [Subgroup Analysis and Heterogeneity](#subgroup-analysis-and-heterogeneity)
    - [Other Methods](#other-methods)
    - [Emerging and Hybrid Methods](#emerging-and-hybrid-methods)
    - [Causal Inference Software Tools](#causal-inference-software-tools)
3. [Development Plan](#development-plan)
4. [Contributing](#contributing)
5. [License](#license)

## Introduction

Causal inference aims to identify causal relationships between variables, going beyond simple correlations. This repository contains implementations of various causal inference methods, with examples and documentation for each method.

## Methods

### Experimental Methods
1. **Randomized Controlled Trials (RCTs)**
2. **Field Experiments**
3. **Lab Experiments**
4. **Natural Experiments**

### Quasi-Experimental Methods
5. **Instrumental Variables (IV)**
6. **Difference-in-Differences (DiD)**
7. **Regression Discontinuity Design (RDD)**
8. **Interrupted Time Series Analysis**

### Matching and Reweighting Methods
9. **Propensity Score Matching (PSM)**
10. **Covariate Matching**
11. **Inverse Probability Weighting (IPW)**
12. **Genetic Matching**
13. **Entropy Balancing**
14. **Mahalanobis Distance Matching**
15. **Coarsened Exact Matching (CEM)**
16. **Nearest Neighbor Matching**

### Graphical and Structural Methods
17. **Causal Diagrams (Directed Acyclic Graphs - DAGs)**
18. **Structural Equation Modeling (SEM)**
19. **Path Analysis**

### Machine Learning and Advanced Statistical Methods
20. **Causal Forests**
21. **Bayesian Causal Inference**
22. **Double Machine Learning (DML)**
23. **Targeted Maximum Likelihood Estimation (TMLE)**
24. **Synthetic Control Method**
25. **G-computation**
26. **Marginal Structural Models (MSM)**
27. **Causal Bayesian Networks**
28. **Causal Discovery Algorithms (e.g., PC Algorithm, FCI Algorithm)**

### Time-Series and Panel Data Methods
29. **Fixed Effects Models**
30. **Random Effects Models**
31. **Dynamic Panel Models**
32. **Panel Data Matching**

### Mediation and Moderation Analysis
33. **Mediation Analysis**
34. **Moderation Analysis**
35. **Moderated Mediation Analysis**

### Sensitivity Analysis and Robustness Checks
36. **Sensitivity Analysis**
37. **Bounds Analysis**
38. **Placebo Tests**
39. **Permutation Tests**

### Advanced Reweighting and Balancing Methods
40. **Inverse Probability of Treatment Weighting (IPTW)**
41. **Standardized Mortality Ratio Weighting (SMRW)**
42. **Calibration Weighting**

### Instrumental Variable Extensions
43. **Two-Stage Least Squares (2SLS)**
44. **Generalized Method of Moments (GMM)**
45. **Limited Information Maximum Likelihood (LIML)**
46. **Control Function Approach**

### Subgroup Analysis and Heterogeneity
47. **Subgroup Analysis**
48. **Quantile Treatment Effects (QTE)**
49. **Heterogeneous Treatment Effects Analysis**

### Other Methods
50. **Matching with Multiple Controls**
51. **Propensity Score Stratification**
52. **Propensity Score Regression Adjustment**
53. **Cross-Over Designs**
54. **Regression Kink Design**
55. **Fuzzy Regression Discontinuity Design**
56. **Sharp Regression Discontinuity Design**

### Emerging and Hybrid Methods
57. **Network Causal Inference**
58. **Spatial Causal Inference**
59. **Integrative Causal Inference (combining multiple methods)**

### Causal Inference Software Tools
60. **Epidemiological Software (e.g., DAGitty)**
61. **Statistical Packages (e.g., R's `MatchIt`, `twang` for IPW, `Zelig`, Python's `causalml`, `DoWhy`)**
62. **Machine Learning Libraries (e.g., `econML`, `causalForest` in R)**

## Development Plan

The development plan involves implementing each method step-by-step, providing detailed documentation and examples for each. Here is a proposed plan:

1. **Initial Setup**
    - Set up the repository structure.
    - Define coding standards and guidelines.

2. **Phase 1: Basic Methods**
    - Implement and document basic methods such as RCTs, IV, and DiD.
    - Provide examples and use cases for each method.

3. **Phase 2: Intermediate Methods**
    - Implement matching and reweighting methods.
    - Include detailed documentation and examples.

4. **Phase 3: Advanced Methods**
    - Implement graphical and structural methods, machine learning methods, and time-series methods.
    - Provide complex examples and case studies.

5. **Phase 4: Robustness and Sensitivity Analysis**
    - Implement sensitivity analysis and robustness checks.
    - Document common pitfalls and how to address them.

6. **Phase 5: Emerging Methods**
    - Implement and document emerging and hybrid methods.
    - Include innovative applications and case studies.

7. **Final Phase: Integration and Testing**
    - Integrate all methods into a cohesive framework.
    - Conduct comprehensive testing and validation.
    - Prepare final documentation and examples.

## Contributing

We welcome contributions from the community. Please follow our [contributing guidelines](CONTRIBUTING.md) to get started.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
number: 12 # leave as-is, maintainers will adjust
title: Robust GPs for Sustainable Concrete via Bayesian Optimization
topic: tutorial
team_leads:
  - Jakob Zeitler (<a href=http://matterhorn.studio/>Matterhorn Studio</a>) @jakobzeitler

# Comment these lines to hide these elements
contributors:
  - Matias Altamirano (<a href=http://matterhorn.studio/>Matterhorn Studio</a>) @maltamiranomontero

github: jakobzeitler/sustainable-concrete

youtube_video: jSPGCgH31Hc

---

We will provide a tutorial on how to use Robust GPs ([https://arxiv.org/abs/2311.00463](https://arxiv.org/abs/2311.00463)) for the Sustainable Concrete via Bayesian Optimization.

Meta at the end of 2023 published their research on "Sustainable Concrete via Bayesian Optimization". Altamarino et al. published their work on "Robust and Conjugate Gaussian Process Regression" at the same time.

This project will introduce robust GPs to the concrete sciences for future BO campaigns. Concrete sciences experiments, like many other sciences, tend to suffer from the occassional outlier. Accounting for these outliers with robust GPs directly improves BO campaign convergence due to improved surrogate modeling. Note that this is related, but separate from the topic of robust optimization under *input noise* (see e.g., [BoTorch tutorial](https://botorch.org/tutorials/robust_multi_objective_bo)).

We hope to showcase a first PoC of robust GP use for BO for concrete sciences, possibly a notebook tutorial for others to understand the use of robust GPs, e.g. in concrete sciences.

References:
1. [https://arxiv.org/abs/2311.00463](https://arxiv.org/abs/2311.00463)
2. [https://arxiv.org/abs/2310.18288](https://arxiv.org/abs/2310.18288)

---
number: 23 # leave as-is, maintainers will adjust
title: Reliable Surrogate Models of Noisy Data
topic: general
team_leads:
  - Darby Brown (EMD Electronics)
  - Vijay Narasimhan (EMD Electroncis)

# Comment these lines by prepending the pound symbol (#) to each line to hide these elements
contributors:
  - Brenden Pelkie (University of Washington)
  - Karim Ben Hicham (RWTH Aachen)
  - Utkarsh Pratiush (University of Tennessee)
  - Joseph Manning (University of Manchester, UK) @jrhmanning

github: AC-BO-Hackathon/project-noisy-nerds
# youtube_video: <your-video-id>

---

Research and development in lab settings necessarily results in imperfect data collection. Noise is introduced into R&D-scale datasets from a number of possible factors, such as human error in measurement, equipment malfunctions, contamination, calibration errors, changing analytical methods, imperfect reproducibility between scientists, and environmental factors (e.g., temperature, humidity).

Due to the costly nature of continuous experimentation, R&D teams will ideally be able to employ Bayesian optimization (BO) as soon as possible after an initial set of noisy, early stage experiments.

This project aims to benchmark the effectiveness of BO in reaching optima despite noisy and sparse data. It should identify a threshold where BO becomes useful in terms of noise level and amount of data, and the tradeoff thereof.  Further, it should identify strategies to mitigate the impact of noise in future modeling efforts. Proposed project scope for the hackathon is modeled after formulation development where the tunable parameters are:

1. Continuous: Mole-ratio of raw material 1
2. Continuous: Mole-ration of raw material 2
3. Continuous: Mole ratio of raw material 3
4. Categorical: Molecule used for raw material 1
4. Categorical: Molecule used for raw material 2

Dataset: 

The Schwefel function is a complex, multimodal function often used as a benchmark problem for optimization algorithms. This project should use the Schwefel function to generate dummy data with a 'ground truth' for the target optimization. Then, the team will mathematically add variance to the dataset by introducing Gaussian noise.(Stein)  The X parameter set should include randomly generated data consisting of 3 continuous parameters and 2 categorical parameters. 

The Schwefel function is defined as:
f(\mathbf{x}) = 418.9829 \cdot d - \sum_{i=1}^{d} x_i \cdot \sin(\sqrt{\left| x_i \right|})f(x)=418.9829⋅d−i=1∑dxi⋅sin(∣xi∣)

What makes the Schwefel function interesting:
- Complexity: It has many local minima, making it challenging for optimization algorithms to find the global minimum.
- Input Domain: It is typically evaluated on the hypercube ( x_i \in [-500, 500] ) for all dimensions ( i ).
- Global Minimum: The function has a global minimum at ( \mathbf{x^} = (420.9687, \ldots, 420.9687) ) with ( f(\mathbf{x^}) = 0 ).

The function is deceptive because the global minimum is geometrically distant from the next best local minima, which can mislead optimization algorithms. It’s a continuous function and can be defined in an n-dimensional space, adding to its complexity. For a visual representation, imagine a landscape with many peaks and valleys. Our goal is to find the gloval optimium among many local optima.

Add-on option: 

If other project teams wish to tack-on the noise study to thier project, they may leverage their existing dataset, add gaussian noise, and re-run their algorithms to study the difference of outcome between noisy or non-noisy data. 

References:

1. J. Stein, M. Poppel, P. Adamczyk, R. Fabry, Z. Wu, M. Kolle, J. Nußlein, D. Schuman, P. Altmann, T. Ehmer, V. Narasimhan, C. Linhoff-Popien. Benchmarking Quantum Surrogate Models on Scarce and Noisy Data. Proceedings of the 16th International Conference on Agents and Artificial Intelligence - Volume 3. Jun 2023.

2. Olympus: a benchmarking framework for noisy optimization and experiment planning. Florian Häse et al 2021 Mach. Learn.: Sci. Technol. 2 035021

2. H. Bellamy, A. A. Rehim, O. I. Orhobor, and R. King, Batched Bayesian Optimization for Drug Design in Noisy Environments, J. Chem. Inf. Model., vol. 62, no. 17, pp. 3970–3981, Sep. 2022.

---
number: 36 # leave as-is, maintainers will adjust
title: Scalable Nonmyopic Bayesian Optimization in Dynamic Cost Settings
topic: general
team_leads:
  - Sang T. Truong (Stanford)
  - Duc Q. Nguyen (HCMC University of Technology - VNU-HCM)

# Comment these lines by prepending the pound symbol (#) to each line to hide these elements
contributors:

github: sangttruong/nonmyopia
# youtube_video: <your-video-id>

---
Bayesian optimization is a widely used approach for making optimal decisions in uncertain scenarios by acquiring information through costly experiments. Many real-world applications can be cast as instances of this problem, ranging from designing biological sequences to conducting ground surveys. In these contexts, the cost associated with each experiment can be dynamic and non-uniform. For instance, in cases where each experiment corresponds to a location, there exists a variable travel cost contingent on the distances between successive experiments. It becomes evident that conventional Bayesian optimization techniques, often reliant on myopic acquisition functions and assuming a fixed cost structure, yield suboptimal results in dynamic cost environments. In order to address these limitations, we introduce a nonmyopic acquisition function grounded in a decision-theoretic extension of mutual information. Our empirical evaluations demonstrate that our method outperforms numerous baseline approaches across a range of global optimization tasks.

References:
1. Shali Jiang, Daniel Jiang, Maximilian Balandat, Brian Karrer, Jacob Gardner, and Roman Garnett. Efficient nonmyopic Bayesian optimization via one-shot multi-step trees. Advances in Neural Information Processing Systems, 33:18039–18049, 2020b

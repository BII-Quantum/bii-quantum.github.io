---
title: Submit a Project
menu_title: Submission
menu_icon: cloud-arrow-up
---

Below the project topic of this year's Quantum Innovation Challenge is presented.

## Quantum Innovation Challenge 2025: Applying Algorithms to Benchmark Tasks


## Project initialization

As the three team leaders, to initialize your project[<sup>(?)</sup>][faq]{:title="Can I participate in multiple projects?"}, please follow these steps:

1. Use [this link to open up an issue in the respective challenge repository](https://github.com/BII-Quantum/quantum-challenge-2025/issues). For example, if your team name is "Bayes Bandits", the file should be named `project-bayes-bandits.md`.
The team name can be whatever you want it to be as long it aligns with our code of conduct.
Further, please also state the project name, your three team members names, GitHub usernames, and your company/institution affiliations.

You do not already have to share a link to the repository you are working on for the challenge but feel free to also shae the link with your public challenge repo if you feel comfortable doing it. But we recommend to fork the Quantum-Challenge-2025 repo because you later have to submit your project with a pull request.

By experience we know that it can also be strategic to first share your repository to the public just before submission so that nobody can copy your ideas or build on top of them. But a challenge project like this over several months will probably not win just because you were hiding your development until just before the deadline. Check out the evaluation criteria to read up on how the scientific committee of this challenge will evaluate each project.

![project submission](../assets/)

In summary:

1. Fork the Quantum-Challenge-2025 repo

2. Open op a github issue stating your team details and affilitions

3. Submit a pull request to Quantum-Challenge-2025 repo with the title "Submit project \<team-name: project-name\>" and tag your team members in the pull request description using the <code>@</code> symbol followed by their real names and affilitions. It is very important that the scientific evaluation committee can see the affilitions of the team members due to the needed academic affiliation of one team member. Make also sure that you have sent us via email the confirmation of the academic background of that team member in form of a ... .

4. Once the pull request is merged, your project will appear on [the projects page](_/../projects.md) of this portal and will also be moved into the projects folder together with all other projects in the Quantum-Challenge-2025 repo.

```yaml
---
number: 1 # leave as-is, maintainers will adjust
title: Project 1 title
topic: <topic-name>
team_leads:
  - Project lead 1 (Institution 1) @gh-username1
  - Project lead 2 (Institution 2) @gh-username2

# Comment these lines by prepending the pound symbol (#) to each line to hide these elements
contributors:
  - Contributor 1 (Institution 1) @gh-username3
  - Contributor 2 (Institution 2) @gh-username4

# github: <your-github-account>/<your-repo-name>
# youtube_video: <your-video-id>

---

Project 1 description

References:

```

Here is an example of a filled-in project file called `foobar.md` for the "Quantumpharma Lifesaver" team. Please replace any colons (`:`) with hyphens (`-`) in the title, if applicable, and ensure that the filename ends with the Markdown (`.md`) extension. Also, ensure that you include the first line with `---` (required for the webpage to build correctly). The references section is optional. Please include links in Markdown format where appropriate.

```yaml
---
number: 1 # leave as-is, maintainers will adjust
title: Quantum Graph Neural Networks for Biopharmaceutical Development
topic: general
team_leads:
  - Jane Doe (University of Invention) @jdoe
  - John Smith (Institute of Discovery) @john-smith

contributors:
  - Larry Lab (University of Invention) @labamation
  - David Data (University of Science) @data4everyone
  - Rachel Research (Institute of Discovery) @researchlife

# github: <your-github-account>/<your-repo-name>
# youtube_video: <your-video-id>

---

This project will investigate the application of quantum graph neural networks to pharmaceutical drug development involving several sub-algorithms with quantum computing simulators and quantum-inspired methods. A benchmarking study has been established and is presented in this project report.

References:

1. 

2. 


```markdown
github: <your-github-account>/<your-repo-name>
```

will be replaced with:
  
```markdown
github: <Quantum-Innovation-Challenge>/<Quantum-Challenge-2025>
```

## Project showcase and judging

You can showcase your project in multiple ways and it is up to you how you would like to communicate your project in form of a video, a pdf report, a poster, or even an prototype software tool on-boarding documentation.

It is very important that your submitted pull request with the repo content holds all the needed information and links to be able to judge your project fully.

## End of Quantum Challenge

To ensure a dynamic and engaging submission process, we ask that all challenge teams announce their final projects through social media (e.g., BlueSky, LinkedIn, YouTube etc.) and then link to their project folder within the Quantum-Challenge-2025 repo.

By sharing your work with a broader audience, you’ll help to promote groundbreaking research within pharmaceutical development while inspiring others to contribute to the field.

Here is a guideline for the optional presentation of your project:

1. Optional but recommended: Create a concise video presentation (3 minutes or less) summarizing your team’s project, highlighting its application and novelty, and presenting your project outputs.

2. Upload your video to YouTube (unlisted is fine) and post about it on social media (e.g., BlueSky, LinkedIn, etc.)

3. With the pull request, update your project file with the YouTube video ID (e.g., `IVaWl2tL06c` for `https://youtu.be/IVaWl2tL06c`) and a sentence with a link to the social media post:

```markdown
github: Quantum-Challenge-2025/<project-name>
youtube_video: <your-video-id>
```

For the social media post, you would add a sentence like `Check out our social media post on [LinkedIn](<your link here>)!` before the References section.

This pull request will be considered your final submission for phase 1 of the challenge.

## Evaluation criteria

### 1. Problem Understanding & Approach (0-5 pts)

- Comparison to state of the art: Does the team clearly define the problem and put it into context?
- Technical Feasibility: Is the approach reasonable given current or near turn quantum computational/AI hardware capacities? 
- Innovativeness: Does the solution bring a novel perspective or improvement compared to existing approaches? Has the participant demonstrated (potential) advantage over classical methods (e.g. speedup, accuracy, resource efficiency)? 
- Scalability: Can the approach be extended or scaled up? For larger PKPD datasets can this solution adapted for another use case such as drug resistance prediction?

### 2. Computational Resource Estimation (0-5 pts)
- Hardware Requirements: Did the team estimate the needed computational resources (GPUs, CPUs)? 

### 3. Technical Assessment (0-5 pts)
- Choice of Algorithms: Are the selected algorithms appropriate for the task?
- Justification of Methods: Is there a solid reasoning behind using specific architectures or techniques?
- Benchmark with existing solutions: Are existing solutions considered and benchmarked?

### 4. Structure of the Work Plan (0-5 pts)
- Step-by-Step Breakdown: Does the participant outline a clear roadmap how to approach the challenge?
- Risk Assessment & Mitigation: Are potential failure points identified with alternative solutions?

### 5. Team skills 0-5 (pts)
- Skillset: Does the team cover the necessary experience in quantum/AI techniques?

### 6. Proof of Concept / Prototype (non-mandatory; 0-5pts)
- Prototype Implementation: Has the team built a minimal working proof of concept? 
- Initial Results: Are preliminary results provided?
- Demonstration of Key Concepts: Does the proof of concept validate core ideas effectively?

[faq]: {{ site.baseurl }}{% link faq.md %}

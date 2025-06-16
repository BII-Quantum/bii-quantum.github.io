---
layout: page
title: BII Quantum Challenge 2025
menu_title: Home
menu_icon: house-door
---
{% assign current_date = 'now' | date: "%Y-%m-%d" %}
{% assign event_start_date = site.event_start_date | date: "%Y-%m-%d" %}
{% assign event_close_date = site.event_close_date | date: "%Y-%m-%d" %}
{% assign registration_opens_date = site.registration_opens_date | date: "%Y-%m-%d" %}
{% assign registration_closes_date = site.registration_closes_date | date: "%Y-%m-%d" %}

{% if current_date < registration_opens_date %}
    {% assign registration_status = 'soon' %}
{% elsif current_date >= registration_opens_date and current_date <= registration_closes_date %}
    {% assign registration_status = 'open' %}
{% else %}
    {% assign registration_status = 'closed' %}
{% endif %}

{% if current_date < event_start_date %}
    {% assign event_status = 'soon' %}
{% elsif current_date >= event_start_date and current_date <= event_close_date %}
    {% assign event_status = 'now' %}
{% else %}
    {% assign event_status = 'over' %}
{% endif %}

{:.secondary}
# {{ site.event_date }}, sponsored by the Novo Nordisk Foundation and Erhvervsstyrelsen

<div class="aside">
    <h2><i class="bi bi-calendar3"></i> Event timeline</h2>
    <dl>
        {% if registration_status == "soon" or registration_status == "open" or registration_status == "demo" %}
            <dt>{{ site.registration_opens_date }}</dt>
            <dd>
                Applications open for participants<br>
                {% if registration_status == 'open' %}
                    <a href="{{ site.baseurl }}{% link registration.md %}" class="btn">Register now</a>
                {% elsif registration_status == 'closed' %}
                    <a class="btn disabled">Registration has closed</a>
                {% elsif registration_status == 'soon' %}
                    <a class="btn disabled">Registration opens soon</a>
                {% endif %}
            </dd>
        {% endif %}

        <dt>{{ site.registration_closes_date }}</dt>
        <dd>Applications close</dd>

        <dt>{{ site.event_date }}</dt>
        <dd>Hackathon date</dd>
    </dl>
</div>

{% if event_status != "over" %}

With the emergence of near term intermediate quantum computers and quantum-inspired algorithms powered by GPUs, it is important to understand their strengths and weaknesses, reduce the barrier to use, and adapt them for pharmaceutical development apart from drug discovery (e.g. docking and binding analysis).
The Bio Innovation Institute (BII), Molecular Quantum Solutions (MQS), Novo Nordisk, QAI Ventures and Roche are hosting the virtual quantum challenge for researchers all over the world to work collaboratively in teams on projects. 

Researchers can propose projects with respect to this year's [challenge topic](_/../projects.md) applying quantum computing and quantum-inspired algorithms to existing benchmarks, developing new benchmarks involving quantum computing methods, creating sub-aglorithms based on quantum computing methods, proposing quantum computing based sampling and optimization methods, and more.
After the challenge, results will be collated and secured under open-source and free license agreements (Apache/MIT) in the dedicated Quantum-Challenge-2025 repository.

[This opportunity](_/../registration.md) is open to researchers at all levels who are interested in quantum computing for better informed pharmaceutical development in the low data regime.
Prior programming experience is required and basic familiarity with git and GitHub.
Training and orientation resources are available on the [resources page](_/../resources.md).

## Logistics

([Element](https://) for ongoing comms, especially for the participants to find other team members.

Questions via email can be sent to quantum_challenge@mqs.dk during the two weeks Q&A phase and will be collectively answered via the Q&A page.

## Outputs

By the end of the event, we hope you will have formed new connections, learned new skills, and been inspired with new ideas!

{% else %}

With the completion of the BII Quantum Challenge 2025, we thank participants for exploring, collaborating, innovating, and contributing to the advancement of quantum computing and quantum-inspired methods for pharmaceutical development.

During the hackathon, researchers had the opportunity to develop with a use-case example provided by Novo Nordisk.

Although the event has concluded, the outputs from the quantum challenge, including applied and developed algorithms, benchmarks, etc. will continue to serve as valuable resources for the research community. Outputs from teams that have participated  are available at [https://github.com/BII-Quantum/Quantum-Challenge-2025](https://github.com/BII-Quantum/Quantum-Challenge-2025).

We want to express our gratitude to all the participants for their contributions, and we look forward to future collaborations.
{% endif %}

## Prizes

{% if event_status != "over" %}

Prizes sponsored by [Matterhorn Studio](https://matterhorn.studio/) will be announced the day after the hackathon for the highest-ranked[<sup>(?)</sup>][faq]{:title="What is expected from me if I act as a judge?"} projects based on the project showcase and judging session on Day 2 of [agenda](_/../agenda.md). Tentative prize tiers are below, and submissions from any project topic are eligible. Each prize will be awarded in the form of a gift card.

| Rank | Prize |
| --- | --- |
| First-ranked | Up to CA$300 gift card per team member (max CA$1000) |
| Second-ranked | Up to CA$150 gift card per team member (max CA$500) |
| Third-ranked | Up to CA$75 gift card per team member (max CA$250) |
| 4th-10th ranked | Up to CA$35 gift card per team member (max CA$125) |

{% else %}
We'd like to congratulate the following teams for their outstanding contributions to the hackathon! The top-ranked[<sup>(?)</sup>][faq]{:title="What is expected from me if I act as a judge?"} projects from the showcase and judging session are as follows:

| Rank | Project #                                            | Team Name | Project Name |
| ---  | ---------------------------------------------------- | --------- | ------------ |
| 1st  | [Project xx](https://bii-quantum.github.io/projects) |           |              |
| 2nd  | [Project xx](https://bii-quantum.github.io/projects) |           |              |
| 3rd  | [Project xx](https://bii-quantum.github.io/projects) |           |              |
| 4th  | [Project xx](https://bii-quantum.github.io/projects) |           |              |
| 5th  | [Project xx](https://bii-quantum.github.io/projects) |           |              |

For a full list of hackathon projects, we encourage you to check out the [projects page](_/../projects.md).

{% endif %}

## Sponsors

- [Novo Nordisk Foundation](https://novonordiskfonden.dk/)
- [Danish Business Authority](https://danishbusinessauthority.dk/)
- [Danish Centre for AI Innovation - Gefion](https://dcai.dk/)

## Hosts

<div style="display: flex; align-items: center; justify-content: center;">
    <a href="https://bii.dk/">
        <img src="https://mva.org/wp-content/uploads/2019/03/BII_Logo_Petroleum_RGB.png" alt="BioInnovation Institute" style="width:400px; margin-right: 20px;">
    </a>
    <a href="https://mqs.dk">
        <img src="https://mqs.dk/Images/Logo/MQS_Logo_Text_black.png" alt="Molecular Quantum Solutions (MQS)" style="width:300px; margin-left: 20px;">
    </a>
    <a href="https://novonordisk.com/">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsYXQ2Ql2tHhxEPxX_p_wzGvDAH1B-uglemQ&s" alt="Novo Nordisk" style="width:300px; margin-left: 20px;">
    </a>
    <a href="https://qai-ventures.com/">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4yFd81seqGxOo0wpiPf_e27HXz6YQQHtZdw&s" alt="QAI Ventures" style="width:300px; margin-left: 20px;">
    </a>
    <a href="https://roche.com/">
        <img src="https://upload.wikimedia.org/wikipedia/commons/f/f4/F._Hoffmann-La_Roche_2021_logo.svg" alt="Roche" style="width:300px; margin-left: 20px;">
    </a> 
</div>

## Prize Sponsor

<div style="display: flex; align-items: center; justify-content: center;">
    <a href="https://danishbusinessauthority.dk/">
        <img src="https://stateofgreen.com/en/wp-content/uploads/2018/05/profile_logo_6283_460x160-4-240x83.png" alt="Danish Business Authority" style="width:200px;">
    </a>
</div>

[faq]: {{ site.baseurl }}{% link faq.md %}

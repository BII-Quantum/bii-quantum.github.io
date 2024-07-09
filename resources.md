---
title: Hackathon resources
menu_title: Resources
menu_icon: journal-code
---

<ul class="grid">

<li class="resource-block" markdown="1">

## Getting Started

#### [Slack](https://join.slack.com/share/enQtNjc5MjI1NTI3MDUzMy1lNjZlZWZlMGYxNzA3MTY2N2Q2MDA2ZjNlMDQxZmIyMmZkMmNhZmYyMjhhYWQyODM1NDI0Yjg0MGE4NjI3YTBl) - Join the hackathon's Slack channel to connect, ask questions, and form teams

#### [Project proposals](_/../submission.md) - team leaders should submit their project proposals using the instructions here

#### [Gather](https://app.gather.town/events/nHv-tpANR6a7kCsPCgqJ) - Add the Gather Town event to your calendar

####  [Accelerated discovery forum](https://accelerated-discovery.discourse.group/) - create an account to join the discussion forums

#### [Bayesian optimization](https://youtu.be/IVaWl2tL06c) - Watch the Accelerate '23 training workshop on Bayesian optimization below

{% include youtube.html video="IVaWl2tL06c" title="A Gentle Introduction to Bayesian Optimization" %}

</li>

<li class="resource-block" markdown="1">

## Orientation Modules

Please complete the following orientation assignments in preparation for the hackathon to familiarize the tools and concepts you'll need. You will need to [create a GitHub account](https://github.com/join) to access these resources. If you are already familiar with git and GitHub, you may skip directly to "Intro to GitHub Classroom". When prompted, please select an identifier from the list that's given. In addition to these orientation modules, we also recommend that you [familiarize yourself with Markdown syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) if this is new to you.

<table>
    <tr>
        <td><a href="https://classroom.github.com/a/2rswOlPi">📝 Intro to Git and GitHub</a></td>
        <td><a href="https://classroom.github.com/a/EaTuZ8L8">📝 Intro to GitHub Classroom</a></td>
    </tr>
</table>

For those looking for a refresher on Python programming or to implement a simple BO example, see the following GitHub Classroom assignments:

<table>
    <tr>
        <td><a href="https://classroom.github.com/a/XFCJVXYP">📝 Python Refresher</a></td>
        <td><a href="https://classroom.github.com/a/TlzXth_g">📝 Simple Bayesian optimization script</a></td>
    </tr>
</table>

{% include youtube.html video="w3jLJU7DT5E" title="What is GitHub?" %}

</li>

<li class="resource-block" markdown="1">

## Bayesian optimization

#### [Bayes Rule by 3Blue1Brown](https://youtu.be/HZGCoVF3YvM) -- explanation of the fundamental concept behind Bayesian methods

{% include youtube.html video="HZGCoVF3YvM" title="" %}

#### [A Visual Exploration of Gaussian Processes](https://distill.pub/2019/visual-exploration-gaussian-processes/) - An explanation of a commonly used predictive model in Bayesian optimization with visualizations and mathematical rigor

#### [Exploring Bayesian Optimization](https://distill.pub/2020/bayesian-optimization/) - An overview of active learning and Bayesian optimization with visualizations and mathematical rigor

#### [Bayesian Optimization Book](https://bayesoptbook.com/) - For those that REALLY want to understand BO, this is a self-contained, comprehensive deep dive that builds up basic principles from "scratch" and delves into advanced topics. The book is free and open-source.

</li>

<li class="resource-block" markdown="1">

## Python

Programming expertise is not required, but at least beginner Python programming experience is recommended for participation in code-focused projects of the hackathon. For those looking for a brief, interactive refresher on Python programming, see the GitHub Classroom assignment from the first section on this page. For those without prior Python experience, we recommend you complete an introductory Python course in preparation for the hackathon. Some resources are listed below:

<table>
    <tr>
        <td><a href="https://www.coursera.org/specializations/python">Python for Everybody by University of Michigan</a></td>
        <td><a href="https://www.codecademy.com/learn/learn-python-3">Learn Python 3 by CodeAcademy</a></td>
    </tr>
    <tr>
        <td><a href="https://youtube.com/playlist?list=PLL0SWcFqypCmkHClksnGlab3wglEVMqNN">Intro to Python Programming for Materials Engineers</a></td>
        <td><a href="https://wiki.python.org/moin/BeginnersGuide/Programmers">Python Beginners Guide for Programmers by Python Software Foundation</a></td>
    </tr>
    <tr>
        <td><a href="https://courses.packtpub.com/courses/python">The Python Workshop by Packt</a></td>
    </tr>
</table>

If you have no prior programming experience, you may wish to start with the [Python Beginners Guide for Non-programmers by Python Software Foundation](https://www.python.org/about/gettingstarted/).

{% include youtube.html video="x7X9w_GIm1s" title="What is Python?" %}

</li>

<li class="resource-block" markdown="1">

## BO Tools

Use of the tools listed on this page is not a requirement. A diverse set of packages and implementations is encouraged. Likewise, multiple teams using the same package is not a problem, in part because implementations can remain private during the course of the hackathon.[<sup>(?)</sup>][faq]{:title="Does my GitHub repository need to be public?"} If you'd like to see a specific tool listed here, please navigate to the "Improve this page" link at the bottom of the page and open a pull request. See also the [Acceleration Consortium's curated list of optimization tools](https://github.com/AccelerationConsortium/awesome-self-driving-labs#optimization).

</li>

<li class="resource-block" markdown="1">

#### [BayBE](https://github.com/emdgroup/baybe)

[![baybe](./assets/baybe.png)](https://github.com/emdgroup/baybe)

This hackathon is co-organized by Merck KGaA. You may consider using an internal Merck tool that was recently open-sourced, called the [Bayesian optimization BackEnd (BayBE)](https://github.com/emdgroup/baybe). This tool focuses on real-world experimental campaigns in the physical sciences with support for integrating domain knowledge through custom parameter encodings and built-in chemical encodings. In addition, it allows for custom surrogate models, mixed variable types, and transfer learning.

</li>

<li class="resource-block" markdown="1">

#### [Adaptive Experiment (Ax) Platform](https://ax.dev/)

[![ax](./assets/ax-black-background.png)](https://ax.dev/)

The [Ax Platform](https://ax.dev/) is a tool developed by Meta's Adaptive Experimentation team. It is a user-friendly, modular, and actively developed general-purpose Bayesian optimization platform with support for simple and advanced optimization tasks. It is a high-level wrapper to the widely used [BoTorch](https://botorch.org/) library, also developed by Meta, which is built on PyTorch.

</li>

<li class="resource-block" markdown="1">

#### [Honegumi](https://honegumi.readthedocs.io/en/latest/)

[![honegumi](./assets/honegumi.png)](https://honegumi.readthedocs.io/en/latest/)

[Honegumi](https://honegumi.readthedocs.io/en/latest/) (pronounced "ho neh goo mee", also referred to as "honey gummy"), deriving from the Japanese word for _skeletal framework_, is a package for interactively creating API tutorials with a focus on optimization packages. You use an interactive grid to select Bayesian optimization characteristics specific to your task and watch the corresponding template dynamically appear. "Open in Colab" and "Open in GitHub" links are also dynamically generated for each template. [Honegumi pairs particularly well with LLMs](https://youtu.be/rnI2BvGgP9o) to adapt the templates to real-world tasks.

</li>


<li class="resource-block" markdown="1">

## [Hugging Face Spaces](https://huggingface.co/docs/hub/spaces)

The pre-packaged benchmark functions will be available on [Hugging Face Spaces](https://huggingface.co/docs/hub/spaces), which makes it easy to deploy and use our benchmark tasks through a web GUI, or more relevant to the hackathon - programmatically via a straightforward API. For those who are planning to develop their own benchmark as a hackathon project (Topic #2), we recommend hosting the final benchmark through this same interface. Start by watching the [Hugging Face Spaces overview](https://huggingface.co/docs/hub/spaces-overview) below, which shows how you can get one running in just a few minutes.

{% include youtube.html video="3bSVKNKb_PY" title="Hugging Face Spaces Overview" %}

To make this more concrete, see [our implementation of the Branin function](https://huggingface.co/spaces/AccelerationConsortium/branin) being run via the Hugging Face Spaces interface, which can be set up in just a few minutes. To see how to use it programmatically, click on the "Use with API" button at the bottom of the page (button marked in red in the image below).

[![use with API](assets/branin-api.png)](https://huggingface.co/spaces/AccelerationConsortium/branin)

</li>

</ul>

<ul class="grid">

<li class="resource-block" markdown="1">

## Guidelines

### [Submission](_/../submission.md) - The hackathon's workflow for submissions, including project topics and proposal instructions

</li>

</ul>

[faq]: {{ site.baseurl }}{% link faq.md %}

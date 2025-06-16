---
title: Quantum Challenge Agenda 🗓️
menu_title: Agenda
menu_icon: clock
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


## Schedule
{% if event_status != "over" %}
The anticipated schedule is as follows, with all times listed in Central European Time (CET).
{% else %}
The schedule for the event was as follows, with all times listed in Central European Time (CET):
{% endif %}


## Jun 23 - Jun 30

Brainstorm, build, team up.

1. Brainstorm project ideas and form teams
   1. Read [the project description](_/../projects.md)
   2. If you'd like to solicit team members or get feedback, post your project idea via a github issue in the Quantum-Challenge-2025 repository
   3. If you would like to join a team, use the Element channel () to express your interest and describe your background.
   4. Submit your [project proposal](_/../submission.md) to get feedback and then you are ready for developing your project during phase 1.
4. Check also the resources which allow you to retrieve valuable knowledge with respect to this challenge, [complete the orientation modules](_/../resources.md)


### Phase 1: Jul 01 - Aug 31

During the first two weeks of Phase 1 we will compile an extensive Q&A summary with all your questions. From the 15th of July we will not respond to questions anymore and you will have time until the 31st of August to submit your project via a pull request to the Quantum-Challenge-2025 repository. 


### Phase 2: Sep 01 - Oct 15


### Final presentations 



### After the challenge

The Quantum-Challenge-2025 will be a documentation of all projects and a valuable resource for academia and industry.
All submitted projects have been screened to align with the necessary open-source and free license (Apache/MIT).

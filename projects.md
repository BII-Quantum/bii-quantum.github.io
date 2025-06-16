---
layout: project_list
title: Quantum Challenge 2025 projects
menu_title: Projects
menu_icon: briefcase
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

{% if event_status != "over" %}

Find below the webpages for each of the projects. This list will be updated on an ongoing basis to reflect the accepted project proposals. For details on how to submit a project, see the [submission page](_/../submission.md).

{% else %}

The BII Quantum Challenge '25 has concluded. See below for teams, project descriptions, videos, and GitHub repositories for each of the projects below.

{% endif %}

[faq]: {{ site.baseurl }}{% link faq.md %}

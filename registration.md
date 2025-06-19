---
title: Quantum Challenge registration
menu_title: Registration
menu_icon: clipboard-check
event_status: soon
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


{:.lead}
Participation is FREE and open. We can't wait to see what you build!

{% if registration_status == "soon" or registration_status == "demo" %}
Registration opens on {{ site.registration_opens_date }}.
{% endif %}
The closing date for applications is {{ site.registration_closes_date }}.

The hackathon is open to everyone, regardless of background or experience. Prior programming experience is not required, but it is recommended for coding projects[<sup>(?)</sup>][faq]{:title="Am I eligible to participate in the hackathon?"}. Please review the [project submission page](_/../submission.md) to learn more about the types of projects within the scope of the hackathon as well the [resources page](_/../resources.md) for other information you need to prepare. During the hackathon, the organizers will be available to support you. After the hackathon, if you choose to and you meet the guidelines[<sup>(?)</sup>][faq]{:title="What is required for me to participate in the scholarly article?"}, you can contribute to the scholarly article. If you are interested in acting as a judge[<sup>(?)</sup>][faq]{:title="What is expected from me if I act as a judge?"}, please indicate so in the corresponding question on the registration form.

<div class="aside" markdown="1">
This virtual event will require some commitment prior to and including the
hackathon event which will take part from {{ site.event_date }}.

{% if registration_status == "soon" or registration_status == "demo" %}
  <a class="btn disabled">Registration opens soon</a>
{% endif %}
{% if registration_status == "open" or registration_status == "demo" %}
  [Register now](https://www.eventbrite.com/...){:.btn target="_blank"}
{% endif %}
{% if registration_status == "closed" or registration_status == "demo" %}
  <a class="btn disabled">Registration has closed</a>
{% endif %}

The closing date for applications is {{ site.registration_closes_date }}.
</div>

[faq]: {{ site.baseurl }}{% link faq.md %}

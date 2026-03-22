---
layout: default
title: Incident Status
sidebar: false
permalink: /incident/
---

{% assign inc = site.data.incident %}

<div class="incident-status incident-status--{{ inc.status }}">
  <div class="incident-status__indicator"></div>
  <div class="incident-status__text">
    <strong>
      {% if inc.status == "active" %}ACTIVE INCIDENT
      {% elsif inc.status == "standby" %}STANDBY
      {% else %}NO ACTIVE INCIDENT
      {% endif %}
    </strong>
    <span>{{ inc.status_message }}</span>
  </div>
  <div class="incident-status__updated">Updated: {{ inc.status_updated }}</div>
</div>

{% if inc.incidents and inc.incidents.size > 0 %}
## Active Incidents

{% for incident in inc.incidents %}
<div class="incident-card">
  <div class="incident-card__header">
    <span class="incident-card__name">{{ incident.name }}</span>
    <span class="incident-card__badge">{{ incident.status }}</span>
  </div>
  <dl class="incident-card__details">
    <dt>Type</dt><dd>{{ incident.type }}</dd>
    <dt>Location</dt><dd>{{ incident.location }}</dd>
    <dt>Activated</dt><dd>{{ incident.date_activated }}</dd>
    {% if incident.controller_callsign %}
    <dt>Incident Controller</dt><dd>{{ incident.controller_callsign }}{% if incident.controller_name %} — {{ incident.controller_name }}{% endif %}</dd>
    {% endif %}
    {% if incident.description %}
    <dt>Notes</dt><dd>{{ incident.description }}</dd>
    {% endif %}
  </dl>
</div>
{% endfor %}
{% endif %}

## Communications Channels

<table class="incident-table">
  <thead>
    <tr><th>Layer</th><th>Detail</th></tr>
  </thead>
  <tbody>
    {% for ch in inc.comms_channels %}
    <tr><td>{{ ch.name }}</td><td>{{ ch.detail }}</td></tr>
    {% endfor %}
  </tbody>
</table>

## Resources

<ul class="incident-resources">
  {% for res in inc.resources %}
  <li><a href="{{ res.url }}">{{ res.name }}</a></li>
  {% endfor %}
</ul>

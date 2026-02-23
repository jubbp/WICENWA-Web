---
layout: default
title: Future Events
---

# Upcoming Events

This page lists posts that are tagged with `future`. To include an event here, add `tags: [future]` to the post's front matter.

{% assign events = site.tags.future %}
{% if events %}
	{% assign events = events | where_exp: "post", "post.date >= site.time" | sort: 'date' %}
{% endif %}

{% if events and events.size > 0 %}
<ul class="future-events-list">
{% for post in events %}
	<li>
		<a href="{{ post.url | relative_url }}">{{ post.title }}</a>
		<span class="event-date"> — {{ post.date | date: "%-d %b %Y" }}</span>
	</li>
{% endfor %}
</ul>
{% else %}
<p>No future events are listed. Tag posts with <strong>future</strong> to add them here.</p>
{% endif %}

---

## Requesting WICEN Support

WICEN WA is available to provide communications support for community events, government activities, and emergency response operations. For requests or enquiries, please [contact us](/contact).

## Latest News

For news and updates about recent events and activities, [visit our News page](/news).

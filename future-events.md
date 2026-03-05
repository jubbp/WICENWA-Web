---
layout: default
title: Future Events
---

# Upcoming Events

{% assign events = site.tags.future %}
{% if events %}
	{% assign events = events | where_exp: "post", "post.date >= site.time" | sort: 'date' %}
{% endif %}

{% if events and events.size > 0 %}
<ul class="future-events-list">
{% for post in events %}
	<article class="news-item">
    <h3><a href="{{ post.url }}" class="news-link">{{ post.title }}</a></h3>
    <div class="news-meta">
      <span class="news-date">{{ post.date | date: "%B %d, %Y" }}</span>
      {% if post.author %}<span class="news-author">by {{ post.author }}</span>{% endif %}
    </div>
    <p class="news-excerpt">{{ post.excerpt }}</p>
    <a href="{{ post.url }}" class="read-more">Read more →</a>
  </article>
{% endfor %}
</ul>
{% else %}
<p>No future events are listed. </p>
{% endif %}

---


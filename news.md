---
layout: default
title: News
---

# News & Updates

Latest news and updates from WICEN WA.

## Recent Posts

{% if site.posts.size > 0 %}
  {% for post in site.posts %}
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
{% else %}
  <p><em>Check back soon for news updates from WICEN WA.</em></p>
  <p>To see what's happening with WICEN WA, we share updates about:</p>
  <ul>
    <li>Event participation and support</li>
    <li>Member achievements and milestones</li>
    <li>Training programs and workshops</li>
    <li>Equipment updates and technology news</li>
    <li>Emergency response activities</li>
    <li>Community announcements</li>
  </ul>
{% endif %}

## Subscribe

Stay informed about WICEN WA news and activities. 

[Contact us](/contact) to join our mailing list.

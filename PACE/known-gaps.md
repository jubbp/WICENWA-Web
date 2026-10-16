---
layout: default
title: Known Gaps
pace_nav: true
PaceNavTitle: 14. Known Gaps
---

## Known Gaps

This plan is a draft and has known gaps. Each one has a gap ID, and wherever a gap affects a plan page, that page shows the ID next to the affected text — for example {% include gap.html id="GAP-004" %}.

Gaps are worked through by the committee in WICEN WA's PACE Gap Register, a members' working document. When a gap is resolved, the agreed change is made on the plan page and its status here is updated.

| ID | Gap | Domain | Status |
|---|---|---|---|
{% for g in site.data.gaps %}| <span id="{{ g.id | downcase }}">{{ g.id }}</span> | {{ g.title }} | {{ g.domain }} | {{ g.status }} |
{% endfor %}

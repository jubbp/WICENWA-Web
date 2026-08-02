---
layout: default
title: PACE Domain Summary
pace_nav: true
PaceNavTitle: 02. Domain Summary
---

## DRAFT ONLY

This Plan is currently only a DRAFT and has not been accepted or implemented by WICEN WA. It is largely incomplete.

## Why this page exists

The [Overview](./overview) describes PACE as a single ladder: Primary, Alternate, Contingency, Emergency, each layer assumed to only be used once the layer above it has failed.

In practice, WICEN-WA's communications cover several different jobs — alerting members, coordinating an incident, moving long-form traffic statewide, running a field team, liaising interstate — and each of those jobs has its own Primary/Alternate/Contingency/Emergency answer. Trying to describe all of them with one ladder is what caused MeshCore (and other local/tactical tools) to have nowhere to sit in the plan.

This page names those **domains** explicitly, so a reader can see the whole shape of the plan in one place instead of piecing it together from several pages. Each domain keeps its own detail page; this page is the map, not a replacement for them.

## Domains

| Domain | Scope | Primary | Alternate | Contingency | Emergency |
|---|---|---|---|---|---|
| [Activation & Alerting](./activation) | Getting members mobilised before/at the start of an incident | Internet Messaging (App/Signal/Discord) | Email Distribution | SMS Broadcast | Amateur Radio Alert Net (HF) |
| [Strategic Coordination](./operational) | Incident-level coordination and command, once activated | Internet Collaboration Platform | Amateur Radio Voice Nets | Amateur Radio Digital Messaging | Voice Relay Network |
| [Long-Haul Message Traffic](./digital-messaging-architecture) | Structured, state/regional-scale message traffic over HF | Winlink (HF) | JS8Call (HF) | *Not yet defined* | *Not yet defined* |
| Local/Tactical Field Comms | Team-level comms for a single field unit or task group | VHF/UHF Voice (simplex/repeater) | MeshCore LoRa mesh | HF Voice (if the team is remote enough to need it) | Runner / face-to-face |
| [Cross-State Coordination](./cross-state-coordination) | Liaison with interstate amateur emergency comms groups | Internet Collaboration Platform | Winlink HF Email | HF Voice Liaison | *Not yet defined* |

Local/Tactical Field Comms doctrine (node roles, standing orders, use cases) is still being drafted and does not have its own page yet — see [Deployment Model](./deployment-model) for where this domain sits organisationally in the meantime.

**Cross-cutting — not a ladder:** *Situational Awareness* (APRS position/message beacons, MeshCore adverts) runs alongside whichever tier of whichever domain is currently active, rather than sitting in any one domain's ladder.

## Cascade rule, and the one exception to it

Every domain above follows the Overview's rule — **each layer assumes the layer above it has failed** — with one deliberate exception:

**Local/Tactical Field Comms.** The Alternate tier (MeshCore) is run in parallel with the Primary tier (VHF/UHF voice) as standard practice, not held in reserve. This is a deliberate exemption from the cascade rule, for training and validation reasons: a mesh network that's only ever switched on after voice has already failed is a mesh network nobody has practised using under pressure. All other domains keep the strict cascade.

## Net discipline

Because there are now several domains instead of one ladder, net controllers and operators must name **which domain** they mean, not just the tier. "Field Comms going to Alternate, mesh" is a complete instruction; "going to Alternate" on its own is not — it's ambiguous between five different systems.

## Methodology check: is each ladder actually redundant?

CISA's guidance on PACE planning sets a **Distinguishable** test for any PACE ladder: two tiers are not genuinely redundant if they depend on the same underlying path, and "the same communications path or method should never be used more than once" as you step down a ladder — if one medium is degraded or denied, the next tier should use a different one entirely.

Run against the table above:

- **Activation & Alerting** — Primary (Internet Messaging) and Alternate (Email) both typically ride the same internet/cellular data path. If that path is down, both tiers fail together. This is a genuine gap, not just a documentation gap.
- **Strategic Coordination** — Primary (internet) to Alternate (radio) is a clean break. Contingency and Emergency are both amateur radio, but on different modes (digital vs. voice relay) — worth the committee confirming this counts as distinguishable enough, since RF conditions that degrade voice may also degrade digital.
- **Long-Haul Message Traffic** — Primary (Winlink) and Alternate (JS8Call) are both HF radio. They're genuinely different digital modes with different failure characteristics (JS8Call tolerates far weaker signals), so this likely passes the test even though the underlying medium is shared — but it's a closer call than a true medium change, and worth stating explicitly rather than assuming.
- **Local/Tactical Field Comms** — VHF/UHF, LoRa mesh, HF, and runner are four genuinely independent mediums. This domain passes cleanly.
- **Cross-State Coordination** — same internet-to-radio break as Strategic Coordination; the undefined Emergency tier means the test can't be completed yet.

CISA's methodology also calls for explicit **triggers** — defined conditions for when to move from one tier to the next (e.g. what specifically counts as "voice has failed"). None of the domains on this site currently define these. That's a gap across the whole plan, not specific to any one domain.

## Open gaps

A few cells in the table above are marked *Not yet defined* — these are genuine gaps in the current draft, not omissions from this page:

- Long-Haul Message Traffic has no defined Contingency or Emergency tier.
- Cross-State Coordination has no defined Emergency tier.
- No domain defines explicit trigger conditions for moving between tiers (see Methodology check above).
- Activation & Alerting's Primary/Alternate pair shares an underlying path and may not be truly redundant (see Methodology check above).

These need to be resolved as part of finishing the draft, not assumed.

Several of these gaps can't actually be closed until the committee has settled the organisation's aims and priorities — see [Committee Discussion — Aims & Priorities](./committee-discussion).

## References

This restructure draws on published methodology and comparable organisations' plans, for context rather than as WICEN-WA policy:

- [Leveraging the PACE Plan into the Emergency Communications Ecosystem](https://www.cisa.gov/sites/default/files/2024-10/2024_NCSWICPTE_Leveraging_PACE_Plan_Emergency_Comms_Ecosystems.pdf) — CISA/NCSWIC, 2023. Source of the Feasible/Acceptable/Suitable/Distinguishable/Complete test and the PACE-triggers concept used above. Also recommends a separate PACE plan per entity/scope rather than one universal ladder, which is the basis for this domain-based structure.
- [WICEN (Vic.) Background Procedures & Techniques Manual](https://www.vic.wicen.org.au/wp-content/uploads/2011/05/VK3KBA_ops_man.pdf) — WICEN Victoria, 1994/2000. A sister WICEN organisation's message-handling standard (serial numbers, precedence, date/time groups, prowords) — more detailed than this site's current [Message Handling](./message-handling) page, useful if that page is expanded later.
- [West Central Florida Section Emergency Communications Plan 2025](https://arrlwcf.org/download/wcfares/WCFSection_ARESPlan_040125.pdf) — ARRL ARES, West Central Florida Section. A comparable volunteer amateur emergency comms plan; notable for a four-level activation scale (Routine / Alert / Partial Activation / Full Activation) more granular than this site's current three WICEN Status levels.

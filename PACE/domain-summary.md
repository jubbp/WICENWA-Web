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

In practice, WICEN-WA's communications cover several different jobs — alerting members, coordinating an incident, moving long-form traffic statewide, running a field team, liaising interstate, supporting a planned event — and each of those jobs has its own Primary/Alternate/Contingency/Emergency answer. Trying to describe all of them with one ladder is what caused MeshCore (and other local/tactical tools) to have nowhere to sit in the plan.

This page names those **domains** explicitly, so a reader can see the whole shape of the plan in one place instead of piecing it together from several pages. Each domain keeps its own detail page; this page is the map, not a replacement for them.

## Domains

| Domain | Scope | Primary | Alternate | Contingency | Emergency |
|---|---|---|---|---|---|
| [Activation & Alerting](./activation) | Getting members mobilised before/at the start of an incident | Internet Messaging (App/Signal/Discord) | Email Distribution | SMS Broadcast | Amateur Radio Alert Net (HF) |
| [Strategic Coordination](./operational) | Incident-level coordination and command, once activated | Internet Collaboration Platform | Amateur Radio Voice Nets | Amateur Radio Digital Messaging | Voice Relay Network |
| [Long-Haul Message Traffic](./digital-messaging-architecture) | Structured, state/regional-scale message traffic over HF | Winlink (HF) | JS8Call (HF) | *Not yet defined* {% include gap.html id="GAP-001" %} | *Not yet defined* {% include gap.html id="GAP-002" %} |
| Local/Tactical Field Comms | Team-level comms for a single field unit or task group | VHF/UHF Voice (simplex/repeater) | Local digital mesh/messaging — technology not yet chosen {% include gap.html id="GAP-009" %} | HF Voice (if the team is remote enough to need it) | Runner / face-to-face {% include gap.html id="GAP-039" %} |
| [Cross-State Coordination](./cross-state-coordination) | Liaison with interstate amateur emergency comms groups | Internet Collaboration Platform | Winlink HF Email | HF Voice Liaison | *Not yet defined* {% include gap.html id="GAP-003" %} |
| [Event Support](./event-support) | Communications for a planned event, run for the organiser's race control | VHF/UHF net to race control | Simplex relay via intermediate stations | HF NVIS or the event's own UHF CB | Satellite messenger/phone, then runner or vehicle {% include gap.html id="GAP-045" %} |

Most Primary tiers depend on internet or mobile networks, which are often the first thing to fail in the incidents WICEN is called to {% include gap.html id="GAP-025" %}. Every tier also depends on power {% include gap.html id="GAP-026" %}.

Local/Tactical Field Comms doctrine (node roles, standing orders, use cases) is still being drafted and does not have its own page yet {% include gap.html id="GAP-008" %} — see [Deployment Model](./deployment-model) for where this domain sits organisationally in the meantime.

**Cross-cutting — not a ladder:** *Situational Awareness* (APRS position/message beacons, and adverts from whichever local mesh system is chosen) runs alongside whichever tier of whichever domain is currently active, rather than sitting in any one domain's ladder.

**Cross-cutting — voice procedure:** every voice tier in every domain above — the HF alert net, voice nets, the voice relay network, field VHF/UHF and HF, and interstate HF liaison — uses the same [Voice Procedure (RATEL)](./voice-procedure). The ladders say which system to use; that page says how to talk on it.

## Permanent infrastructure vs portable capability

The table above describes *what* each tier uses, not *whether it's already there or has to be brought in*. Every technology named above can exist as either **standing infrastructure**, in place all the time regardless of activation, or **portable kit**, carried to wherever a deployment needs it — and those two forms have completely different cost and maintenance profiles.

WICEN WA isn't starting from zero on standing infrastructure: South West WA's existing APRS digipeater network and an expanding MeshCore coverage area are both already real, already providing baseline coverage, and neither needed WICEN to build them. A permanently sited AREDN network in major centres, by contrast, would be genuinely new capital investment. Portable capability is a separate question again — a field go-kit could carry any of these technologies regardless of what's permanently sited nearby. These assets are not yet inventoried {% include gap.html id="GAP-015" %}.

## Cascade rule, and the one exception to it

Every domain above follows the Overview's rule — **each layer assumes the layer above it has failed** — with one deliberate exception:

**Local/Tactical Field Comms.** The Alternate tier — whichever local digital mesh/messaging system is eventually chosen — is run in parallel with the Primary tier (VHF/UHF voice) as standard practice, not held in reserve. This is a deliberate exemption from the cascade rule, for training and validation reasons: a system that's only ever switched on after voice has already failed is a system nobody has practised using under pressure. All other domains keep the strict cascade. This exemption is about *when* the Alternate tier runs, not *which* technology fills it {% include gap.html id="GAP-009" %}.

## Net discipline

Because there are now several domains instead of one ladder, net controllers and operators must name **which domain** they mean, not just the tier. "Field Comms going to Alternate, mesh" is a complete instruction; "going to Alternate" on its own is not — it's ambiguous between six different systems.

## Known gaps

Tier triggers — the defined conditions for stepping from one tier to the next — are not yet set for any domain {% include gap.html id="GAP-004" %}. Some ladders also have tiers that may share an underlying path and so may not be genuinely redundant: Activation & Alerting {% include gap.html id="GAP-005" %}, Strategic Coordination {% include gap.html id="GAP-006" %} and Long-Haul Message Traffic {% include gap.html id="GAP-007" %}. See [Known Gaps](./known-gaps) for the full list.

## References

This restructure draws on published methodology and comparable organisations' plans, for context rather than as WICEN-WA policy:

- [Leveraging the PACE Plan into the Emergency Communications Ecosystem](https://www.cisa.gov/sites/default/files/2024-10/2024_NCSWICPTE_Leveraging_PACE_Plan_Emergency_Comms_Ecosystems.pdf) — CISA/NCSWIC, 2023. Source of the Feasible/Acceptable/Suitable/Distinguishable/Complete test and the PACE-triggers concept. Also recommends a separate PACE plan per entity/scope rather than one universal ladder, which is the basis for this domain-based structure.
- [WICEN (Vic.) Background Procedures & Techniques Manual](https://www.vic.wicen.org.au/wp-content/uploads/2011/05/VK3KBA_ops_man.pdf) — WICEN Victoria, 1994/2000. A sister WICEN organisation's message-handling standard (serial numbers, precedence, date/time groups, prowords) — more detailed than this site's current [Message Handling](./message-handling) page, useful if that page is expanded later.
- [AIIMS 2025](https://www.afac.com.au/AIIMS) — AFAC. The incident management doctrine every domain here ultimately has to fit into if WICEN WA is supporting a fire, emergency, or land management agency. See [Deployment Model](./deployment-model).
- [West Central Florida Section Emergency Communications Plan 2025](https://arrlwcf.org/download/wcfares/WCFSection_ARESPlan_040125.pdf) — ARRL ARES, West Central Florida Section. A comparable volunteer amateur emergency comms plan; notable for a four-level activation scale (Routine / Alert / Partial Activation / Full Activation) more granular than this site's current three WICEN Status levels.

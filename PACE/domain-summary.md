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

## Open gaps

A few cells in the table above are marked *Not yet defined* — these are genuine gaps in the current draft, not omissions from this page:

- Long-Haul Message Traffic has no defined Contingency or Emergency tier.
- Cross-State Coordination has no defined Emergency tier.

These need to be resolved as part of finishing the draft, not assumed.

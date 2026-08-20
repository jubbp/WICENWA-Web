---
layout: default
title: Proposed Implementation Roadmap
pace_nav: true
PaceNavTitle: 15. Implementation Roadmap
---

## DRAFT ONLY

This Plan is currently only a DRAFT and has not been accepted or implemented by WICEN WA. It is largely incomplete.

## Why this page exists

[Committee Discussion](./committee-discussion) raises ten clusters of open questions — some are gaps in the plan itself, others are genuinely new capability proposals (community welfare messaging, a non-ham mobile repeater, ad-hoc satellite internet, permanent AREDN siting). Not all of it is achievable at once. WICEN WA is currently in a rebuilding phase, and most of what's been discussed assumes a membership, budget, and equipment base the organisation doesn't have yet.

This page is an assessment of relative cost and effort against that reality, and a **proposed** phased sequence — a recommendation for the committee to confirm, amend, or reject, not a decision that's already been made.

**Working assumption this roadmap depends on:** it assumes Committee Discussion Section 1 gets answered as "build reliable local/regional capability first, state-wide capability later," because that's what current membership and activity level actually supports. If the committee decides the opposite — state-wide capability is the immediate priority — this sequencing needs to be rebuilt around that instead, not just relabelled.

## Assessment

| Proposal | Capital cost | Ongoing cost | Regulatory / admin load | Nature of the work | Depends on |
|---|---|---|---|---|---|
| Inventory existing standing infrastructure (APRS digipeaters, MeshCore coverage) | None | None | None — possibly a relationship if run by another club | Documentation only; it already exists | Nothing — can start immediately |
| Close existing domain gaps (PACE triggers, distinguishability issues, undefined tiers) | None | None | None | Documentation only | Aims answered (Discussion §1, §3) |
| Local/Tactical Field Comms doctrine + Self-Assessment update | Low regardless of technology chosen (APRS messaging costs nothing new; a mesh system is cheap per node) | None | None | Mostly documentation; APRS capability already exists in members | Local/Tactical confirmed as a near-term priority; technology chosen (Discussion §8) |
| Community welfare messaging pilot | None to low — reuses existing Long-Haul HF digital skills | None | One relationship to build (Red Cross WA) | Mostly documentation + one partnership conversation | Long-Haul domain reasonably mature; Discussion §6 decision |
| Ad-hoc satellite internet — single-unit trial | Moderate (one kit) | Moderate, subscription-based, pausable | Low | Genuinely new capability | Discussion §7 identity question; a real operational trigger to test it against |
| Mobile repeater for non-ham distribution | High (repeater hardware + radios to distribute) | High (ACMA apparatus licence, ongoing) | High (spectrum licensing, plus who's accountable for community-held radios) | Genuinely new capability, significant | Larger membership/budget, likely external co-funding |
| Permanent AREDN network in major centres | High (hardware at multiple sites) | High (site agreements, ongoing maintenance per node) | Moderate (site negotiation, no spectrum licensing) | Genuinely new standing infrastructure, significant | Larger membership/budget; someone accountable for node uptime (Discussion §10) |
| Cross-State Coordination maturity | Low equipment cost | None | None | Mostly relationship-building over time | WA-internal domains stable first; larger membership |

The pattern in this table is the basis for the phasing below: **documentation-only work costs nothing and should happen regardless of capacity; genuinely new capabilities should be ordered by capital cost, ascending.**

## Proposed phases

### Phase 0 — Decisions (cost: committee time only)

Work through [Committee Discussion](./committee-discussion) Sections 1–10. Nothing below can be honestly sequenced until Section 1 (Mission & Scope) and Section 3 (Domain priority) are answered — everything here already assumes a specific answer to both, and that assumption needs to be confirmed, not inherited from this page.

### Phase 1 — Close documentation gaps, and inventory what already exists

Define the PACE triggers, resolve the Activation & Alerting distinguishability gap, and fill (or explicitly mark as "not provided, by decision") the missing Contingency/Emergency tiers in Long-Haul Message Traffic and Cross-State Coordination. Alongside that, inventory the standing infrastructure WICEN WA already has informal access to but hasn't documented — South West WA's APRS digipeater network and the expanding MeshCore coverage area (Discussion §10). Neither task needs equipment, new members, or budget; both are achievable at current capacity and shouldn't wait for anything else. Knowing what's already there also directly informs Phase 2 below.

### Phase 2 — Local/Tactical Field Comms

Discussion §8 splits this into two independent layers rather than one technology choice: a **community intake layer** (MeshCore and/or UHF CB, for non-hams to get a message in) and an **operator-to-operator layer** (APRS messaging and/or AREDN, between licensed members). They don't have to land together. The operator layer is the cheaper and more natural starting point — APRS messaging costs nothing new to acquire since members are already partly trained on it per the Capability Self-Assessment — and can proceed on its own timeline from the intake layer, which is more of a community-engagement decision than an equipment one. Once the committee has confirmed which layer(s) to build first, write the `local-tactical-comms.md` doctrine page and extend the Capability Self-Assessment to cover whichever is chosen.

### Phase 3 — Community welfare messaging pilot

Once Local/Tactical is stable, this is mostly a matter of defining an intake model (doorknock/warden vs. a public drop-off point) and having one conversation with Red Cross WA about feeding into Register.Find.Reunite. It reuses skills and infrastructure WICEN already has in the Long-Haul domain rather than requiring new equipment.

### Phase 4 — Satellite internet, single-unit trial

Don't start with a fleet. One kit, trialled at a real event or exercise, tests both the operational value and whether it belongs in WICEN's identity at all before committing further budget. Subscription-based cost is easier to pause or cancel than a fixed capital project if it doesn't prove out.

### Phase 5 — Larger standing capital investments: mobile repeater and permanent AREDN siting

The most expensive and highest-admin-load items on this list, and the two that most depend on WICEN WA no longer being in a rebuilding phase. Both are genuinely new standing commitments — not portable kit — with ongoing maintenance and accountability questions attached, so it's worth considering them together rather than in isolation. Worth exploring co-funding or partnership with a served agency (DFES, SES, local government) rather than assuming WICEN self-funds either alone — the ACMA licensing, site agreements, and ongoing uptime accountability arguably belong to whoever benefits most from the coverage, not solely to WICEN.

### Phase 6 — Cross-State Coordination maturity

Lowest equipment cost on the list but a genuinely slow one — interstate relationships take time to build regardless of budget. Only worth active investment once the WA-internal domains (Strategic Coordination, Local/Tactical) are solid; there's little point coordinating interstate before WICEN WA can reliably coordinate with itself.

## What would change this order

This sequencing isn't fixed. Some things that would reasonably reorder it:

- A served agency or local government offering to co-fund the mobile repeater or satellite kit would justify moving Phase 4 or 5 earlier — the cost assessment above assumes WICEN pays for it alone.
- If membership doesn't grow over the next 12–24 months, Phases 4–6 should be dropped from the plan rather than left "delayed" indefinitely — an aspiration with no realistic path to resourcing isn't a plan.
- If the committee's answer to Discussion §1 is state-wide capability first, this entire ordering needs to be rebuilt around Strategic Coordination and Long-Haul Message Traffic maturity instead of Local/Tactical.

## Outcome

This roadmap is a proposal, not policy. It should be brought to the committee alongside [Committee Discussion](./committee-discussion) for sign-off, amendment, or rejection — and revisited whenever the working assumption above is confirmed or overturned.

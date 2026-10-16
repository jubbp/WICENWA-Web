---
layout: default
title: Event Support
pace_nav: true
PaceNavTitle: 08a. Event Support
---

## DRAFT ONLY

This domain is a draft and has not yet been reviewed, tested or adopted {% include gap.html id="GAP-045" %}.

This is the **Event Support** domain — see the [Domain Summary](./domain-summary) for how it relates to the other domains in the plan.

## What this domain covers

Communications that WICEN WA provides **for someone else's planned event**: multi-day canoe races, car rallies, endurance rides, community walks and similar. The organiser is the customer, and the organiser's **race control** (or event control) is in charge — much as a controlling agency's incident management team is in charge during an emergency.

It differs from the other domains in three ways:

- **It's planned, not reactive.** Events are booked months ahead, so the [Activation](./activation) statuses (Stand By, On Watch, Activated) don't apply. Events follow the engagement lifecycle below instead.
- **WICEN runs the network for the organiser,** and reports to their race control, not to a WICEN coordinator.
- **The main traffic is competitor tracking** — bib numbers and times through checkpoints — rather than formal messages.

What an organiser needs from WICEN WA comes down to one thing: **knowing where every competitor is, and getting help to one fast when something goes wrong.**

## Event Support PACE

| Level | System | Use |
|------|------|------|
| PRIMARY | VHF/UHF voice net to race control (repeater, or a portable repeater on high ground) | Checkpoint reports, incidents, coordination |
| ALTERNATE | Simplex relay through intermediate stations | Same traffic, relayed — see [Voice Procedure](./voice-procedure)'s Relay section |
| CONTINGENCY | HF NVIS (40/80m), or the event's own UHF CB | Deep valleys and remote stages beyond VHF/UHF reach |
| EMERGENCY | Satellite messenger or satellite phone, then a runner or vehicle to the nearest staffed point | Incident reports when every radio path has failed |

Triggers for stepping between tiers are not yet defined {% include gap.html id="GAP-004" %}.

## Engagement lifecycle

1. **Request.** The organiser contacts WICEN WA's single point of contact.
2. **Scope.** Agree what WICEN will and won't do: which sites, which days, how many operators, what the organiser provides (access, food, shelter, power) {% include gap.html id="GAP-046" %}.
3. **Agreement.** Confirm scope, responsibilities and insurance in writing. Check what the licence conditions allow {% include gap.html id="GAP-053" %}.
4. **Coverage survey.** Visit the course and test every site and path before the event. Plan relays and portable repeaters where needed {% include gap.html id="GAP-052" %}.
5. **Communications plan.** A written plan the organiser can attach to their event safety plan: every site, every channel, every contact, and what happens when each tier fails {% include gap.html id="GAP-047" %}.
6. **Briefing.** Operators, race control and key event staff briefed together, including the escalation and missing-competitor procedures.
7. **Operate.** Run the net for race control. Over multiple days, stations move ahead of the field, and some stay out overnight {% include gap.html id="GAP-054" %}.
8. **Demobilise and report back.** See [Demobilisation](./demobilisation). Logs go to the organiser, and both sides debrief.

## Network structure

```text
Race Control
     |
Net Control (WICEN)
     |
Checkpoint, relay and sweep stations
```

Net Control sits beside race control, not in a separate location, wherever possible. The organiser's marshals and sweep crews often use their own UHF CB or hired business radios; WICEN may need to bridge between those and the WICEN net {% include gap.html id="GAP-039" %}.

## Competitor tracking

Every checkpoint reports competitors through, in order, and race control must be able to ask "where is number 214?" at any time and get an answer. Between days, the finishers of one day must reconcile with the starters of the next.

A draft checkpoint report {% include gap.html id="GAP-048" %}:

> CHECKPOINT (name), TIME (hhmm) — THROUGH: (bib numbers) — WITHDRAWN: (bib number, reason) — SWEEP PASSED: (yes/no)

Bib numbers are read digit by digit (*"Two One Four"*) and read back by Net Control. On busy checkpoints, report in batches at fixed intervals rather than one competitor at a time. Competitor names and medical details are personal information and should not be sent over the air {% include gap.html id="GAP-032" %}.

## Missing or overdue competitors

The organiser owns the decision to search. WICEN's job is to raise the alarm early and supply the facts: last checkpoint passed, time, and who passed them. A competitor is treated as overdue when they haven't reached the next checkpoint within the time agreed with race control {% include gap.html id="GAP-049" %}.

## Incidents and escalation

- **Threat to life:** anyone with a working phone calls 000 immediately. If there's no phone coverage, the operator passes the incident to race control at the highest precedence {% include gap.html id="GAP-012" %}, and race control calls 000.
- **Every incident report includes:** location (checkpoint, distance along the course, or grid reference), bib number, what happened, the competitor's condition, and the help needed.
- Who calls 000, and who meets ambulances at access points, is agreed with the organiser before the event {% include gap.html id="GAP-050" %}.

If police or ambulance take control of an incident, the event becomes, at least in part, an emergency. WICEN keeps supporting race control unless told otherwise, and takes no tasking from emergency services except through race control or a WICEN liaison {% include gap.html id="GAP-051" %}.

## Why this domain matters beyond events

Planned events are what WICEN WA does most, and they are its most realistic exercises: real, multi-day, long-distance deployments with a customer depending on the network. Each event is a chance to test the power standard {% include gap.html id="GAP-026" %}, rostering {% include gap.html id="GAP-027" %}, field safety {% include gap.html id="GAP-028" %} and tier triggers in practice. A well-run event is also the strongest evidence of reliability WICEN WA can show to a Local Emergency Management Committee or a supported agency.

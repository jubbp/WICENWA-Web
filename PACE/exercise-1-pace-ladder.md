---
layout: default
title: "Exercise Part 1 — STEPDOWN (PACE end-to-end)"
pace_nav: true
PaceNavTitle: 16. Exercise 1 — STEPDOWN
published: false
---

## DRAFT ONLY

This exercise design is a draft for committee review. It has not been approved or scheduled. Items in [SQUARE BRACKETS] are decisions still to be made.

## Purpose

Exercise STEPDOWN is Part 1 of a two-part exercise programme. It tests and trains WICEN WA's ability to **run the PACE plan from start to finish**: alert the membership, activate, coordinate, move formal traffic, step down every tier of every ladder as each one is made to fail, then recover and stand down.

It is deliberately a **home-station** exercise. Nobody deploys; members operate from wherever they normally would during a real activation. That keeps the focus on procedure, net discipline and the PACE ladders themselves rather than on field logistics, which is what [Part 2 — PARKLANDS](./exercise-2-parklands) is for.

Part 2 has different aims and should run **after** Part 1's debrief, because one of Part 1's outputs is a set of draft tier triggers that Part 2 then tests in the field.

## Aims

1. Walk the full activation sequence — Stand By → On Watch → Activated → stand-down — as written on the [Activation](./activation) page.
2. Step every defined tier of three domains, in order, under a controlled failure of the tier above:
   - [Activation & Alerting](./activation) — all four tiers
   - [Strategic Coordination](./operational) — all four tiers
   - [Long-Haul Message Traffic](./digital-messaging-architecture) — both defined tiers, and deliberately run into the undefined Contingency tier
3. Practise net discipline across domains: every tier change must name the domain as well as the tier ("Strategic Coordination going to Alternate, voice nets"), per the [Domain Summary](./domain-summary).
4. Practise the logging and reporting the plan already requires — station logs, Net Control logging with an independent Alternate NCS log, message format, and at least two SITREP cycles ([Message Handling](./message-handling)).
5. **Generate evidence for the plan's open gaps** — in particular, record what actually made each tier change necessary, so the debrief can turn that into the explicit trigger conditions the [Domain Summary](./domain-summary) says are missing everywhere.

## What this exercise is not

- Not a test of individual members. Evaluators score the plan and the procedures, not people. (Individual capability is what the [Capability Self-Assessment](/self-assessment) is for.)
- Not a Local/Tactical Field Comms exercise — that domain is Part 2.
- Not a Cross-State Coordination exercise — interstate groups aren't involved. [Optional: invite one interstate WICEN contact to receive a single 20m liaison message in Phase 4.]

## Format

| Item | Detail |
|---|---|
| Type | Functional exercise, distributed home stations, scripted injects |
| Duration | About 5 hours — suggested **[SATURDAY DATE] 1500–2030 WST**, so the HF nets cross the day/night band change (40m → 80m) during the exercise |
| Participants | [6–15] operating members, plus exercise control staff |
| Scenario | Fictional, clearly labelled — see below |
| Served agency | None real. Exercise Control plays the "served agency" and "incident command" |
| Real systems touched | WICEN's own messaging group, email list, SMS broadcast tool, [wicenwa.org/incident](/incident) (exercise banner only), HF and VHF/UHF nets |

## Scenario (fictional)

> **EXERCISE ONLY.** A fast-moving bushfire in the Perth Hills forces evacuations over an afternoon and evening. Fire damage to a telecommunications site takes out mobile data and then mobile voice across the eastern suburbs and hills. Later, mains power and the local repeater site are lost. The (simulated) incident controller asks WICEN WA to provide backup communications between an evacuation centre, the incident control centre, and a regional coordination point.

The scenario exists only to make each failure inject believable. Exercise Control decides which failure hits which stations — members don't have to guess.

## Roles

| Role | Responsibility |
|---|---|
| Exercise Director | Owns the exercise; can pause or end it; makes the call on safety and on "NO DUFF" |
| Exercise Control (EXCON), 2 people | Runs the inject timetable, plays the served agency and incident command, receives all traffic addressed to them |
| Evaluators, 1–2 | Watch against the evaluation criteria below; keep their own timeline |
| State Coordinator (exercise role) | Activation authority for the exercise, per the [Activation](./activation) page |
| Digital Information Station (DIS) | Updates the incident page and runs the information beacon (APRS / JS8Call / Winlink) |
| Net Control Station (NCS) VHF/UHF and HF | Runs the nets and logs every check-in |
| Alternate NCS | Keeps an independent duplicate log |
| Net Logger | Transcribes for the NCS on busy nets |
| Winlink station, JS8Call station | Dedicated digital messaging stations, per the [Operational Comms](./operational) station modes |
| Relay stations | Carry traffic for stations that can't reach NCS in the Emergency tier |
| Field / evacuation-centre stations (simulated) | Ordinary members at home, told by EXCON which "location" they represent |

The State Coordinator, DIS and NCS roles should **not** all be filled by the same few experienced members. Rotating these roles is part of the training value.

## Exercise conventions

- **Radio calls:** every transmission, on every band and mode, says **"exercise only"** immediately before the operator's call sign — for example, *"WICEN Net Control, this is exercise only VK6ABC, over."* This applies every time a call sign is given, including the ACMA identification schedule below.
- **Written and digital messages** (messaging app, email, SMS, Winlink, JS8Call, runner notes) start and end with **"EXERCISE ONLY"**.
- **Voice procedure** is WICEN's RATEL procedure — calls, prowords, relay and frequency changes as on the [Voice Procedure](./voice-procedure) page.
- **"NO DUFF"** marks a real emergency during the exercise (for example, a genuine injury or a real incident call-out). It overrides all exercise traffic. The Exercise Director decides whether to pause or end.
- **Simulated failures are simulated.** Nobody switches off real infrastructure. When EXCON says "your internet is down", that station stops using internet-based systems until EXCON restores them.
- Call-sign identification follows the ACMA schedule for the whole exercise: start and end of transmission, and at least every 30 minutes. This explicitly applies to training exercises ([Message Handling](./message-handling)).
- Use the frequencies in the plan: HF voice 7.110 MHz LSB (day), 7.090 MHz LSB (alternate), 3.600 MHz LSB (night); Winlink 7.095 / 3.595 MHz; JS8Call 7.078 / 3.578 MHz; VHF/UHF on [REPEATER — e.g. VK6RLM 146.750] with [SIMPLEX FALLBACK].
  [CHECK: the weekly net on Get Involved is now 3.610 MHz, but the PACE pages still say 3.600 MHz — settle which one the plan uses before the exercise.]

## Phases and inject timetable (MSEL)

Times are relative to STARTEX (T). EXCON may hold or skip injects if the exercise runs slow.

### Phase 0 — Before the day (T − 4 weeks to T − 1 day)

- Brief all participants: aims, roles, conventions, "NO DUFF", which systems are in play.
- Confirm every participant is on the messaging group, email list and SMS list, and has Winlink/JS8Call set up if they're in a digital role. **Record who isn't** — that is itself a finding for the Alerting domain.
- EXCON prepares the inject cards, the scenario map, and the pre-written "served agency" traffic.
- DIS prepares an exercise version of the incident page with a clear EXERCISE banner. [DECIDE: use the live /incident page with a banner, or a separate exercise page so the public page stays at "standby".]

### Phase 1 — Alerting ladder (T+0:00 to T+1:00)

| Time | Domain | Inject | Expected action | Measure |
|---|---|---|---|---|
| T+0:00 | Activation & Alerting | EXCON (as served agency) tells the SC a fire is threatening the hills | SC moves WICEN to **On Watch** via **Primary** (messaging app), in the standard activation message format | Time to send; % of members acknowledging within 15 min |
| T+0:15 | Activation & Alerting | "The messaging platform is unavailable" | SC re-sends via **Alternate** (email) | Time to recognise and switch; acknowledgements |
| T+0:30 | Activation & Alerting | "Mobile data is down across the hills" — affects **both** messaging and email at the same time | SC goes to **Contingency** (SMS broadcast) | Does anyone notice that Primary and Alternate failed together? (This is the known distinguishability gap) |
| T+0:40 | Activation & Alerting | "Mobile voice and SMS are now down" | SC calls the **Emergency** tier: HF alert net on 7.110 MHz | Time to first check-in; number of stations reached by HF alone |
| T+0:50 | Activation & Alerting | SC declares **Activated** | Members check in; SC nominates NCS, Alternate NCS, DIS, digital stations | Time from Activated to all roles filled |

### Phase 2 — Strategic Coordination ladder (T+1:00 to T+3:00)

| Time | Domain | Inject | Expected action | Measure |
|---|---|---|---|---|
| T+1:00 | Strategic Coordination | Internet is "restored" for coordination purposes | Coordination runs on **Primary** (collaboration platform) in the named channels: #incident-status, #operations, #field-teams, #logistics, #sitrep | Channels used as intended? |
| T+1:15 | Strategic Coordination | EXCON requests **SITREP 1** | Functional areas post their sections; compiler produces the master SITREP; reviewer approves it | Time to release; who compiled and who reviewed (both undefined in the plan today) |
| T+1:30 | Strategic Coordination | "Internet lost at the incident control centre" | Move to **Alternate**: amateur radio voice nets — VHF/UHF repeater net plus HF net | Time to establish the net; NCS log started; Alternate NCS log started |
| T+1:45 | Strategic Coordination | EXCON injects routine and priority traffic by voice | Traffic passed in the standard message format with precedence | Message format compliance; precedence respected |
| T+2:00 | Strategic Coordination | "Voice nets saturated — an evacuation centre needs to send a 40-line resource list" | Move to **Contingency**: amateur radio digital messaging (Winlink / JS8Call) for structured traffic | Time to first digital message delivered; list arrives complete |
| T+2:30 | Strategic Coordination | "Repeater site has lost power" and "[2–3 named stations] can no longer hear NCS on HF" | Move to **Emergency**: voice relay network — relay stations carry traffic for the stations cut off | Messages relayed end to end without loss or distortion (compare original and received text) |
| ~T+2:45 | All HF | Sunset band change | NCS moves the HF net from 40m to 80m using the frequency change procedure | Orderly move; no stations lost |

### Phase 3 — Long-Haul Message Traffic (T+3:00 to T+4:00)

| Time | Domain | Inject | Expected action | Measure |
|---|---|---|---|---|
| T+3:00 | Long-Haul | EXCON requests **SITREP 2** to a "regional coordination point" by formal message | Sent via **Primary**: Winlink (HF) as a structured message / form | Delivery time; received intact |
| T+3:20 | Long-Haul | "The Winlink gateway is unreachable" | Move to **Alternate**: JS8Call store-and-forward, including at least one relayed message | Delivery time; relay worked |
| T+3:40 | Long-Haul | "JS8Call is also unusable on the path to the regional point" | **Contingency tier is not defined in the plan.** Participants decide on the spot what to do | Record exactly what they did and why — this is the raw material for defining the missing tier |

### Phase 4 — Recovery and stand-down (T+4:00 to T+4:45)

- EXCON restores systems in stages. Each domain steps back **up** its ladder, one tier at a time, with the domain named each time.
- SC issues a stand-down message through the same Alerting ladder, from the highest tier that is working.
- DIS returns the incident page to its normal status.
- Every station closes its log. Logs and message copies go to the evaluators within 48 hours.
- [Optional: one 20m liaison message to an interstate contact on 14.300 MHz USB, to touch the Cross-State domain.]

### Phase 5 — Hot debrief (T+4:45 to T+5:30)

On the HF or VHF net, or online. Three questions per domain: what worked, what didn't, what would have made you change tier sooner.

## Evaluation

Evaluators score each item as **Met / Partly met / Not met**, with notes.

| # | Criterion | Evidence |
|---|---|---|
| 1 | Every Activation & Alerting tier reached members within 15 minutes of use | Acknowledgement times per tier |
| 2 | The Primary/Alternate shared-path failure in Alerting was noticed and called out | Timeline, hot debrief |
| 3 | Every tier change named both domain and tier | NCS and evaluator logs |
| 4 | All four Strategic Coordination tiers were set up and passed real traffic | Logs, message copies |
| 5 | NCS log and Alternate NCS log were kept independently and agree | Compare the two logs |
| 6 | Messages used the standard format and precedence | Message copies |
| 7 | Two SITREP cycles completed, with a named compiler and reviewer | #sitrep channel and Winlink copies |
| 8 | Relayed messages arrived word for word | Compare originals and received copies |
| 9 | The band change was handled with the frequency change procedure | NCS log |
| 10 | Call-sign ID schedule was kept throughout, with "exercise only" before every call sign | Evaluator spot checks |
| 11 | The undefined Long-Haul Contingency tier was reached, and what people improvised was recorded | Evaluator notes |
| 12 | RATEL procedure used correctly — calls, relay (RELAY TO / THROUGH ME) and frequency changes (CHANGE TO … CHANGE NOW) | Evaluator spot checks, NCS log |

## Outputs, within 2–3 weeks

1. **Cold debrief** (in person or online) and a short after-action report.
2. **Draft tier triggers.** For each tier change, what the evaluators saw that made the change necessary, turned into a proposed trigger. For example: "Strategic Coordination steps to Alternate when the collaboration platform is unreachable for [5] minutes by [2] or more stations." These go to the committee, and **are then tested in the field in Part 2**.
3. **Plan corrections.** Specific edits to the PACE pages: frequencies that didn't work, roles that were missing, the SITREP compiler and reviewer question, the activation flowchart.
4. **Evidence for Committee Discussion §5** — which tiers have now actually been exercised, as opposed to only documented.
5. Update the [Training](./training) page to record that the exercise happened and what it covered.

## Before this can run

- [ ] Committee approves the exercise and a date
- [ ] Exercise Director named
- [ ] EXCON and evaluators named (ideally people who aren't operating)
- [ ] Messaging group, email list and SMS broadcast tool confirmed working — and someone knows how to send an SMS broadcast
- [ ] Winlink and JS8Call stations confirmed, with at least one reachable gateway
- [ ] Repeater owner's agreement to use [REPEATER] for an exercise
- [ ] 80m frequency question settled (3.600 vs 3.610 MHz)
- [ ] Decision on the live incident page vs a separate exercise page
- [ ] Inject cards and scenario map written

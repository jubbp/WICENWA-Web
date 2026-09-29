---
layout: default
title: "Exercise Part 2 — PARKLANDS (local incident response)"
pace_nav: true
PaceNavTitle: 17. Exercise 2 — PARKLANDS
published: false
---
{% assign ex = site.data.exercise_parklands %}
## DRAFT ONLY

This exercise design is a draft for committee review. It has not been approved or scheduled. Items in [SQUARE BRACKETS] are decisions still to be made.

Event details — date, place, contacts, channels, triggers — live in `_data/exercise_parklands.yml` and appear both in this plan and in the printable **[Field Guide](#field-guide)** at the end, which participants carry on the day. Update them there, not here.

## Purpose

Exercise PARKLANDS is Part 2 of a two-part exercise programme. Where [Part 1 — STEPDOWN](./exercise-1-pace-ladder) tested the whole PACE plan from home stations, PARKLANDS puts members **in the field**. It tests WICEN WA's ability to deploy to a local incident, set up a Communications Unit, and keep field teams in contact across real terrain in {{ ex.park }}.

Its aims are deliberately different from Part 1's. This exercise is about the **Local/Tactical Field Comms** domain, the [Deployment Model](./deployment-model), and whether members' field kit actually works. That domain has no detail page yet, so this exercise also produces the evidence needed to write one.

It should run **after** Part 1's debrief, so it can test the draft tier triggers that Part 1 produced.

## Aims

1. Deploy to a site, and set up an Incident Command Post (ICP) and a Communications Unit, following the [Deployment Model](./deployment-model): Incident Command → Communications Unit → Field Communications Teams → Supported Agency.
2. Run the **Local/Tactical Field Comms** ladder under real field conditions:
   - **Primary:** VHF/UHF voice, simplex and/or repeater
   - **Alternate:** local digital mesh/messaging, run **in parallel with voice from the start** — the plan's one deliberate exception to the cascade rule ([Domain Summary](./domain-summary))
   - **Contingency:** HF voice, for teams that can't be reached any other way
   - **Emergency:** runners, face to face
3. **Field-test the draft tier triggers** from Part 1's debrief. For example: does "three unanswered calls over two minutes" actually work as the trigger for "voice has failed" when a team is behind a hill?
4. Run situational awareness alongside every tier, not as a tier of its own: APRS position beacons, plus mesh adverts.
5. Link the field back to Strategic Coordination: the Communications Unit passes SITREPs to a "State Net Control" home station, using the ladder practised in Part 1.
6. Validate the **standard field go-kit** (Committee Discussion §10) and members' 72-hour kits: what people actually brought, what worked, and what was missing.
7. **Map the park's radio coverage**: dead spots for VHF simplex, the repeater and mesh. This is a lasting asset the plan can reuse.

## What this exercise is not

- Not a technology decision. The Alternate tier uses [MESH SYSTEM — e.g. MeshCore, since coverage is already expanding locally] as a **trial**. Committee Discussion §8 is still open.
- Not a real search. Nobody is actually missing. EXCON plays the served agency.
- Not a public event. [DECIDE: whether to include the optional community welfare intake module below.]

## Format

| Item | Detail |
|---|---|
| Type | Field exercise, single site, scripted injects |
| Location | {{ ex.park }} — a large park with varied terrain, ideally with known dead spots |
| Duration | About 4–5 hours — suggested **{{ ex.date }}, {{ ex.start }}–{{ ex.end }}**, avoiding the heat of the day |
| Participants | [8–16] members in two-person field teams, plus the Communications Unit and exercise control |
| Served agency | Simulated: EXCON plays the incident controller of a (fictional) agency |
| Remote element | One or two members at home as "State Net Control", reached from the park by the Strategic Coordination ladder |

## Scenario (fictional)

> **EXERCISE ONLY.** An elderly bushwalker has been reported overdue in {{ ex.park }}. Mobile coverage in the park is patchy. The (simulated) incident controller has set up at {{ ex.icp }} and asks WICEN WA to provide communications for several search teams working different sectors of the park, and to keep the regional coordination point informed.

A search suits this exercise because it naturally spreads teams across the terrain, needs regular position reports, and produces sudden high-priority traffic when the "missing person" is found.

## Roles

| Role | Responsibility |
|---|---|
| Exercise Director | Owns the exercise and safety; can pause or end it; "NO DUFF" authority |
| Safety Officer | Separate from the Exercise Director; heat, hydration, snakes, terrain, team check-ins. Has a real mobile phone and first-aid kit, **outside** the exercise comms |
| EXCON, 2 people | Plays incident controller and served agency; runs injects; places the "missing person" marker |
| Evaluators, 1–2 | One at the ICP, one roving |
| Communications Unit Leader | Runs the Communications Unit at the ICP |
| Field NCS | Net Control for the field net at the ICP; logs every check-in |
| Alternate NCS / Net Logger | Independent duplicate log; transcribes on busy periods |
| Mesh operator (ICP) | Watches the mesh channel in parallel with voice; logs mesh traffic |
| HF operator (ICP) | HF link to State Net Control; HF contingency for remote teams |
| Field teams (2 people each) | One sector each; one voice radio and one mesh device per team, APRS if available |
| Runners | Emergency tier; ideally teams nominate one member, rather than dedicated people |
| State Net Control (remote) | Home station receiving SITREPs from the Communications Unit |

**Every field team is at least two people**, and every team checks in on a schedule, whatever the comms situation.

## Exercise conventions

Same as Part 1:

- **Radio calls:** every transmission, on every band and mode, says **"exercise only"** immediately before the operator's call sign — for example, *"WICEN Net Control, this is exercise only VK6ABC, over."* This applies every time a call sign is given, including the ACMA identification schedule below.
- **Written and digital messages** (messaging app, email, SMS, Winlink, JS8Call, runner notes) start and end with **"EXERCISE ONLY"**.
- **Voice procedure** is WICEN's RATEL procedure — calls, prowords, relay and frequency changes as on the [Voice Procedure](./voice-procedure) page.
- **"NO DUFF"** for any real emergency. The Safety Officer's real phone is the path to 000, not the exercise radios.
- Call-sign ID on the ACMA schedule throughout.
- Park visitors are not part of the exercise. Teams are polite, identifiable (hi-vis vests with "WICEN WA"), and don't obstruct paths.

Channels for the day (from the data file; HF tactical per the [HF Propagation Plan](./HF-propagation-plan)). The plan doesn't yet name a field simplex frequency — this exercise should pick one and record it. [DECIDE: simplex-first or repeater-first.]

| Tier | System | Channel / detail |
|---|---|---|
{% for c in ex.channels %}| {{ c.tier }} | {{ c.system }} | {{ c.detail }} |
{% endfor %}

## Phases and inject timetable (MSEL)

Times are relative to STARTEX (T).

### Phase 0 — Before the day

- Land manager permission for {{ ex.park }} and any group-activity approval or fee. [CHECK: which authority manages the park, e.g. DBCA or the local council.]
- Confirm public liability cover for a WICEN WA exercise.
- EXCON walks the park beforehand: sectors, likely dead spots, marker locations, hazards.
- Issue the go-kit checklist to every participant.
- Share the draft tier triggers from Part 1 with participants, so they know what they're testing.

### Phase 1 — Deploy and set up (T+0:00 to T+0:45)

| Time | Inject | Expected action | Measure |
|---|---|---|---|
| T+0:00 | Activation message, sent via the Activation ladder | Members travel to the ICP and sign in | Time from message to arrival; sign-in sheet completed |
| T+0:10 | Go-kit inspection | Evaluator checks each team's kit against the checklist, without fixing gaps | Checklist results |
| T+0:15 | Communications Unit sets up at the ICP | Field NCS, mesh operator and HF operator operational; logs open | Time until the Communications Unit is ready |
| T+0:30 | Communications plan briefing | Comms Unit Leader briefs the teams: channels, tiers, triggers, check-in schedule. [Optional: produce an ICS-205-style comms plan sheet] | Briefing given; every team can repeat back its channels |
| T+0:40 | Link to State Net Control | HF operator passes the "Communications Unit established" message | Delivered and acknowledged |

### Phase 2 — Search operations (T+0:45 to T+3:00)

| Time | Inject | Expected action | Measure |
|---|---|---|---|
| T+0:45 | Teams deployed to sectors | Scheduled check-ins every {{ ex.checkin_minutes }} minutes by voice; mesh and APRS running in parallel | Check-in compliance; APRS positions match the reported positions |
| T+1:00 | Coverage mapping | At each check-in, teams give a LOCSTAT and record the voice signal report (ROGER / READABLE / WEAK / UNREADABLE), whether mesh got through, and any dead spots | Coverage log per team |
| T+1:15 | A team moves into a known dead spot | The draft "voice has failed" trigger is applied; the team switches to mesh for traffic | Time until the trigger is recognised; did the trigger wording actually work? |
| T+1:30 | EXCON requests **SITREP 1** | Comms Unit compiles the field SITREP; HF operator sends it to State Net Control | Time to send; received intact |
| T+1:45 | "A team's voice radio has failed" (EXCON takes the radio for 20 min) | Team continues on mesh and APRS messaging only | Traffic handled; NCS log shows the switch |
| T+2:00 | EXCON sends a remote team to the far edge of the park | Contingency tier: HF voice to the ICP on 7.130 MHz | Contact made? If not, why not |
| T+2:15 | "Mesh and voice both unavailable to Team [X]" | Emergency tier: runner to the ICP with a written message in the standard format | Time delivered; message complete and legible |
| T+2:30 | **The missing person is found** (marker found by a team) | EMERGENCY-precedence traffic: location, condition, access. ICP relays it to the incident controller, and a SITREP flash goes to State Net Control | Time from find to incident controller informed; location accuracy |
| T+2:45 | "Incident controller needs a vehicle-access route to the find location" | Coordinated response involving several teams | Traffic kept orderly under pressure; precedence respected |

### Phase 3 — Recovery and stand-down (T+3:00 to T+3:30)

- Teams return to the ICP by {{ ex.return_by }}; the Safety Officer confirms everyone is back.
- The Communications Unit sends the final SITREP to State Net Control and closes the link.
- Logs, message copies and coverage sheets are handed to the evaluators on site.

### Phase 4 — Hot debrief (T+3:30 to T+4:15)

In person, at the ICP. What worked, what didn't, and — specifically — did each draft trigger say the right thing at the right moment?

## Optional module — community welfare intake (Committee Discussion §6)

If the committee wants to start exploring §6, one small add-on fits naturally here. Set up a "welfare desk" at the ICP where role-players (friends or family of members, not the public) hand in simple "I'm safe" messages. These are sent out as ROUTINE traffic at the **bottom** of the precedence order, never competing with search traffic. This tests whether an intake model is workable at all, without committing to anything.

## Evaluation

Evaluators score each item as **Met / Partly met / Not met**, with notes.

| # | Criterion | Evidence |
|---|---|---|
| 1 | Communications Unit ready within [30] minutes of arrival | Timeline |
| 2 | Every team made every scheduled check-in, by some tier | NCS log |
| 3 | Mesh ran in parallel with voice from the start, not only after voice failed | Mesh log |
| 4 | Each draft trigger was applied when its condition occurred, and its wording was unambiguous | Evaluator notes, hot debrief |
| 5 | All four Local/Tactical tiers passed real traffic | Logs, runner messages |
| 6 | Every tier change named the domain ("Field Comms going to Alternate, mesh") | NCS log |
| 7 | APRS positions were usable for tracking teams | APRS log compared with reported positions |
| 8 | The EMERGENCY-precedence "find" message reached the incident controller accurately, within [5] minutes | Timeline, message copy |
| 9 | Two SITREPs reached State Net Control intact | Remote station log |
| 10 | Go-kits met the checklist | Kit checklist |
| 11 | Coverage map produced | Coverage sheets |
| 12 | No safety incidents; every team accounted for at every check-in | Safety Officer log |
| 13 | "Exercise only" given before every call sign, and the call-sign ID schedule kept | Evaluator spot checks |
| 14 | RATEL procedure used correctly — calls, LOCSTAT position reports, signal reports | Evaluator spot checks |

## Outputs, within 2–3 weeks

1. **Cold debrief** and a short after-action report.
2. **Revised tier triggers** for the Local/Tactical domain, now tested in the field, going to the committee for adoption into the plan.
3. **A first draft of the Local/Tactical Field Comms page** — the domain that currently has no detail page — built from what actually worked: channels, check-in schedule, team structure and standing orders.
4. **A standard field go-kit list** (Committee Discussion §10), based on what teams brought, used and wished they had.
5. **A coverage map of {{ ex.park }}**, recorded as a reusable asset, and a note on whether the mesh trial supports or argues against the Committee Discussion §8 options.
6. **Evidence for Committee Discussion §5**: the Local/Tactical tiers have now been exercised in the field.
7. Update the [Training](./training) page to record the exercise.

## Before this can run

- [ ] Part 1 (STEPDOWN) run and debriefed, with draft triggers written
- [ ] Committee approves the exercise and a date
- [ ] Park chosen; land manager permission and any approvals obtained
- [ ] Public liability cover confirmed
- [ ] Exercise Director and a separate Safety Officer named
- [ ] EXCON, evaluators and a State Net Control station named
- [ ] Field simplex channel chosen; repeater owner's agreement if a repeater is used
- [ ] Mesh devices available for every team (borrowed if needed)
- [ ] Go-kit checklist written and issued
- [ ] Hi-vis vests, first-aid kit, water, a sign-in sheet, sector maps
- [ ] Decision on the optional welfare intake module

## Field Guide

<section class="field-guide" id="field-guide">
<p class="field-guide-print-bar"><button type="button" class="btn" onclick="document.body.classList.add('print-field-guide');window.print();">Print field guide</button> Prints only this section, on white paper. Print it from a local build, since it holds phone numbers.</p>

<header class="fg-head">
  <div class="fg-title">Exercise {{ ex.name }} — Field Guide</div>
  <div class="fg-sub">EXERCISE ONLY · {{ ex.date }} · {{ ex.start }}–{{ ex.end }} · {{ ex.park }}</div>
</header>

<div class="fg-grid">
  <div class="fg-box">
    <h3>Where and when</h3>
    <table>
      <tr><th>ICP</th><td>{{ ex.icp }}</td></tr>
      <tr><th>ICP position</th><td>{{ ex.icp_position }}</td></tr>
      <tr><th>Start / finish</th><td>{{ ex.start }} – {{ ex.end }}</td></tr>
      <tr><th>All teams back at ICP</th><td><strong>{{ ex.return_by }}</strong></td></tr>
      <tr><th>Check-in</th><td>Every <strong>{{ ex.checkin_minutes }} minutes</strong>, on any tier</td></tr>
    </table>
  </div>

  <div class="fg-box fg-alert">
    <h3>Real emergency — "NO DUFF"</h3>
    <table>
      <tr><th>Call</th><td><strong>{{ ex.emergency.call }}</strong></td></tr>
      <tr><th>Location</th><td>{{ ex.emergency.app }}</td></tr>
      <tr><th>Then tell</th><td>The Safety Officer, on any radio: <em>"NO DUFF, NO DUFF, NO DUFF"</em> — it stops all exercise traffic</td></tr>
      <tr><th>First aid kit</th><td>{{ ex.emergency.first_aid }}</td></tr>
      <tr><th>Hospital</th><td>{{ ex.emergency.hospital }}</td></tr>
      <tr><th>Land manager</th><td>{{ ex.emergency.land_manager }}</td></tr>
    </table>
  </div>
</div>

<h3>Key contacts</h3>
<table>
  <thead><tr><th>Role</th><th>Name</th><th>Call sign</th><th>Mobile</th></tr></thead>
  <tbody>
  {% for c in ex.contacts %}<tr><td>{{ c.role }}</td><td>{{ c.name }}</td><td>{{ c.callsign }}</td><td>{{ c.mobile }}</td></tr>
  {% endfor %}
  </tbody>
</table>

<h3>Channels — Local/Tactical PACE</h3>
<table>
  <thead><tr><th>Tier</th><th>System</th><th>Channel / detail</th></tr></thead>
  <tbody>
  {% for c in ex.channels %}<tr><td>{{ c.tier }}</td><td>{{ c.system }}</td><td><strong>{{ c.detail }}</strong></td></tr>
  {% endfor %}
  </tbody>
</table>
<p class="fg-note">Name the domain and the tier when you change: <em>"Field Comms going to Alternate, mesh."</em></p>

<h3>When to step down</h3>
<table>
  <thead><tr><th>Step</th><th>When</th><th>What to do</th></tr></thead>
  <tbody>
  {% for t in ex.triggers %}<tr><td>{{ t.from }}</td><td>{{ t.when }}</td><td>{{ t.action }}</td></tr>
  {% endfor %}
  </tbody>
</table>
<p class="fg-note"><strong>Lost all comms:</strong> {{ ex.lost_comms }}</p>

<div class="fg-grid">
  <div class="fg-box">
    <h3>Radio calls</h3>
    <p>Say <strong>"exercise only"</strong> before your call sign, every time:</p>
    <p class="fg-script">"WICEN Net Control, this is exercise only VK6ABC, over."</p>
    <p>Give your call sign at the start and end of each transmission, and at least every 30 minutes.</p>
  </div>
  <div class="fg-box">
    <h3>Check-in report</h3>
    <ol>
      <li>Team</li>
      <li>LOCSTAT — landmark, or GRID reference</li>
      <li>Status: OK / need help</li>
      <li>Signal here: voice ROGER / READABLE / WEAK / UNREADABLE; mesh ✓/✗</li>
      <li>Any traffic</li>
    </ol>
  </div>
</div>

<div class="fg-grid">
  <div class="fg-box">
    <h3>Message format</h3>
    <p class="fg-script">EXERCISE ONLY<br>MESSAGE NUMBER:<br>PRIORITY: EMERGENCY / PRIORITY / ROUTINE<br>FROM:<br>TO:<br>TIME:<br>DATE:<br>TEXT:<br>SIGNATURE:<br>EXERCISE ONLY</p>
  </div>
  <div class="fg-box">
    <h3>Priority</h3>
    <table>
      <tr><th>EMERGENCY</th><td>Immediate threat to life — e.g. the missing person found</td></tr>
      <tr><th>PRIORITY</th><td>Urgent operational information</td></tr>
      <tr><th>ROUTINE</th><td>Everything else</td></tr>
    </table>
    <h3>Safety</h3>
    <ul>
      <li>Stay in your pair. Never split up without telling the ICP.</li>
      <li>Hi-vis on; water, hat and sunscreen.</li>
      <li>Stay on tracks; watch for snakes.</li>
      <li>Be polite to park visitors — they're not part of the exercise.</li>
    </ul>
  </div>
</div>

<h3>Prowords (RATEL)</h3>
<table class="fg-prowords">
  <tbody>
  <tr><th>OVER</th><td>Finished — reply</td><th>OUT</th><td>Finished — no reply</td></tr>
  <tr><th>WAIT</th><td>Pause up to 5 s, nobody else talks</td><th>WAIT OUT</th><td>Longer pause; I'll call back</td></tr>
  <tr><th>ROGER</th><td>Received OK</td><th>WILCO</th><td>Received, will comply</td></tr>
  <tr><th>SAY AGAIN</th><td>Repeat (ALL AFTER / ALL BEFORE …)</td><th>READ BACK</th><td>Repeat my message back exactly</td></tr>
  <tr><th>I SPELL</th><td>Spelling phonetically</td><th>FIGURES</th><td>Numbers follow, digit by digit</td></tr>
  <tr><th>LOCSTAT</th><td>Location report</td><th>GRID</th><td>Grid reference follows</td></tr>
  <tr><th>MESSAGE</th><td>Write this down</td><th>CORRECTION</th><td>Error — correct version follows</td></tr>
  <tr><th>RELAY TO</th><td>Pass this on to …</td><th>THROUGH ME</th><td>I can reach them — send via me</td></tr>
  <tr><th>RADIO CHECK</th><td>How do you hear me?</td><th>WORDS TWICE</th><td>Poor conditions — say everything twice</td></tr>
  <tr><th>CHANGE TO</th><td>Order to change frequency — don't move yet</td><th>CHANGE NOW</th><td>Move now</td></tr>
  </tbody>
</table>

<h3>Teams</h3>
<table>
  <thead><tr><th>Team</th><th>Sector</th><th>Members</th></tr></thead>
  <tbody>
  {% for t in ex.teams %}<tr><td>{{ t.team }}</td><td>{{ t.sector }}</td><td>{{ t.members }}</td></tr>
  {% endfor %}
  </tbody>
</table>
</section>

<script>
  window.addEventListener('afterprint', function () {
    document.body.classList.remove('print-field-guide');
  });
</script>

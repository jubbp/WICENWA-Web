---
layout: default
title: Message Handling
pace_nav: true
PaceNavTitle: 06. Message Handling
---

All formal messages should follow a standard format.

This ensures clarity and traceability.

## Standard Message Format

MESSAGE NUMBER:
PRIORITY:
FROM:
TO:
TIME:
DATE:

TEXT:

SIGNATURE:

## Priority Levels

EMERGENCY  
Immediate threat to life

PRIORITY  
Urgent operational information

ROUTINE  
Normal traffic

## Call Sign Identification

The [Radiocommunications Licence Conditions (Amateur Licence) Determination 2025](https://www.acma.gov.au/amateur-radio-operating-procedures) (ACMA, commenced 30 September 2025) requires a station's call sign to be transmitted at the start and end of a transmission, and at least once every 30 minutes during any transmission or series of transmissions lasting longer than that — **explicitly including emergency services operations and training exercises**, not just routine operating. Net Control and operators on any extended net must identify on this schedule regardless of message priority.

## Station and Net Logs

A message format records one message. A log records everything a station did. This site's message format doesn't replace the need for a log — modelled on the [ICS-309 Communications Log](https://www.qsl.net/ccares/ics309.pdf) standard used across Australian and international emcomm practice.

The log stays with the station, not the operator, so it survives a shift or operator change.

Record for every transmission:

- Time
- Station worked (from/to)
- Message number, if applicable
- Summary of content

Keep entries brief — the log is a record of who did what, when, not a full transcript.

## Net Control Logging

Net Control Stations carry an additional logging responsibility, separate from the station log above:

- Log every check-in — call sign, time, and role — in real time wherever possible
- On busier nets, split the role: one operator runs the net, a separate Net Logger transcribes, so the NCS's hands stay free
- If an Alternate NCS is appointed, they keep an independent duplicate log — a second original, not a copy of the primary — so there is no single point of failure in the record

Dedicated net-logging software (e.g. [NCLog](http://nclog.org/), built specifically for ARES/RACES/public-service net logging) can export directly to ICS-214/309/205-style forms — see [Committee Discussion](./committee-discussion) §9 for the broader software discussion.

## Situation Reports (SITREP)

WICEN WA operates under [AIIMS](https://www.afac.com.au/AIIMS), not the US ICS forms culture — AIIMS's primary recurring documentation artifact is the **Situation Report (SITREP)**, not a numbered form.

A SITREP is published at a fixed interval — commonly every 24 hours for an extended incident, more often for a fast-moving one. Each functional area (Operations, Logistics, Planning, and so on) updates its own section; those sections roll up into one master SITREP, reviewed before release.

The `#sitrep` channel already named on the [Operational Comms](./operational) page exists to support this cycle — but who compiles the master SITREP, at what interval, and who reviews it before release, is not yet defined anywhere in this plan. See [Committee Discussion](./committee-discussion) for related open questions.

## Compatibility with ICS forms

Some supported agencies, and some of the software already named in this plan (Outpost's built-in ICS-213 generator, referenced in [Committee Discussion](./committee-discussion) §9), use FEMA ICS forms rather than AIIMS's SITREP cycle. WICEN WA operators should be able to produce either on request — [ICS-213](https://training.fema.gov/emiweb/is/icsresource/assets/ics%20forms/ics%20form%20213,%20general%20message%20(v3).pdf) (General Message), ICS-214 (Activity Log), and ICS-205/205A (Radio Communications Plan / Communications List) are the ones most likely to be asked for.

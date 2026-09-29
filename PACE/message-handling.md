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

**Proposed change — for committee decision ([Committee Discussion](./committee-discussion) §11):** replace EMERGENCY with **IMMEDIATE**, as used in WICEN's archived RATEL manual — ROUTINE / PRIORITY / IMMEDIATE, each sent before any lower-precedence traffic not already being transmitted. Two reasons: the RATEL manual was written for "maximum compatibility with Emergency Services", and "EMERGENCY" collides with the PACE plan's own *Emergency* tier — on a net, "going to Emergency" and "EMERGENCY traffic" mean different things. Until the committee decides, EMERGENCY remains in use.

## Types of message

From the RATEL manual — see [Voice Procedure](./voice-procedure) for how each is passed on air:

- **Conversation** — back-and-forth voice between two users.
- **Informal message** — a question or piece of information given to the operator verbally or written down, with just the text and who it's for.
- **Formal message** — written on a message form, signed by a releasing officer, given a serial number, sent, logged and filed.

## Formal messages (RATEL)

WICEN's RATEL manual defines a fuller formal message than the format above. Its message form (Annex A of the [RATEL PDF](/assets/WICENWA-RATEL-Procedures.pdf)) adds:

- **Serial number** — IN or OUT, as *message number / date*, e.g. **05/15**. Numbers run consecutively for the whole event; the date part changes at midnight. The sender gives the next OUT number from the log; a received message gets the next IN number. The serial number is separate from the originator's own reference number.
- **Date-time group** — when the message was written, filled in by the originator.
- **Info addressees** — stations that should know about the message but aren't asked to act, normally at ROUTINE.
- **Operator blocks** — at the foot of the form, *R* (received) or *D* (despatched) with date, time, system and operator. Always completed.

**Before sending,** check the message can be read, has no obvious errors, has everything needed to send it, and any abbreviations are clear.

**Sending order** — any part left blank is skipped:

1. Transmission instructions (e.g. READ BACK, RELAY TO)
2. Serial number
3. Precedence
4. Date-time group
5. Originator's number
6. FROM
7. TO
8. BREAK — the text — MESSAGE ENDS

*Example:* "VK6BB, message number zero five slant one five, routine, TIME one five one one three zero hotel, OPS one six, from Bloggs, to Jones, BREAK, PARA ONE, do you have any batteries, FULL STOP, para two nil return required, FULL STOP, MESSAGE ENDS, OVER."

**Received messages** are rewritten onto a form (in duplicate if needed), given an IN serial number, logged, and the original goes to the addressee. Sent and received copies are filed separately.

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

WICEN's own archived log sheet (Annex B of the [RATEL PDF](/assets/WICENWA-RATEL-Procedures.pdf)) records the same thing — Time, From, To, Serial No., Brief Summary — with the station call sign, location, operators, event and date at the top.

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

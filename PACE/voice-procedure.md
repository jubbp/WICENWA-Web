---
layout: default
title: Voice Procedure (RATEL)
pace_nav: true
PaceNavTitle: 06a. Voice Procedure
---

## DRAFT ONLY

This page adapts WICEN WA's archived *Radiotelephone (RATEL) Procedure for Operators in WICEN* (about 2002) for the current plan. It has not yet been formally adopted — see [Committee Discussion](./committee-discussion) §11. The original scanned manual is available on the [Members](/members) page ([PDF](/assets/WICENWA-RATEL-Procedures.pdf)).

## Where this fits in the plan

The PACE ladders on the [Domain Summary](./domain-summary) say **which system** to use. This page says **how to talk** once you're on a voice system. It applies to every voice tier in every domain:

- Activation & Alerting — the HF alert net (Emergency tier)
- Strategic Coordination — amateur radio voice nets (Alternate) and the voice relay network (Emergency)
- Local/Tactical Field Comms — VHF/UHF voice (Primary) and HF voice (Contingency)
- Cross-State Coordination — HF voice liaison (Contingency)

RATEL's stated aim was "maximum compatibility with Emergency Services", which is still the reason to use it: served-agency radio operators use the same family of procedure.

## Spelling, numbers and punctuation

- Use the standard phonetic alphabet. Spell difficult words with **I SPELL**, saying the word before and after if you can pronounce it: *"Catenary — I SPELL Charlie Alpha … — Catenary."*
- Numbers are sent digit by digit, except exact hundreds and thousands. Use **FIGURES** before numbers that could be mistaken for words.

| Number | Spoken as |
|---|---|
| 44 | Fo-wer Fo-wer |
| 90 | Niner Zero |
| 136 | Wun Thuh-ree Six |
| 500 | Fi-yiv Hundred |
| 1478 | Wun Fo-wer Seven Ate |
| 16000 | Wun Six Thousand |

- Write zero as **Ø** on message forms. A decimal point is spoken **DAY-SEE-MAL**.
- Mixed groups use both prowords: 31AB7 is *"FIGURES Three One — I SPELL Alpha Bravo — FIGURES Seven."*
- Punctuation is spoken: COMMA, FULL STOP, OPEN BRACKETS / CLOSE BRACKETS, SLANT (/), HYPHEN.

## Calls and answers

A call is: **their call sign — THIS IS — your call sign — text — ending**.

- *"VK6XX, THIS IS VK6YY, are you ready to move, OVER."* — an answer is needed.
- *"VK6XX, THIS IS VK6YY, move now, OUT."* — no answer needed.

Ending words:

| Proword | Meaning |
|---|---|
| OVER | My transmission is finished; reply. |
| OUT | My transmission is finished; no reply. Never say "over and out". |
| WAIT | I must pause for up to 5 seconds. No one else transmits. |
| WAIT OUT | I must pause for longer. Others may transmit; I will call you back. |
| OUT TO YOU | Finished with you; I'm calling another station straight away. No one else transmits. |

### Signal reports

Good strength and readability is assumed unless you say otherwise. Ask with **RADIO CHECK**; answer briefly, combining terms as needed:

| Proword | Meaning |
|---|---|
| ROGER / LOUD AND CLEAR | Loud and clear |
| READABLE | Satisfactory |
| WEAK / VERY WEAK | Readable with difficulty |
| WITH INTERFERENCE / DISTORTED / FADING | Say what the problem is |
| UNREADABLE | Can't be read |

*"VK6XX, THIS IS VK6YY, RADIO CHECK, OVER." — "VK6YY, WEAK BUT READABLE, OVER." — "READABLE, OUT."*

### Abbreviated and full procedure

- **Abbreviated procedure** is normal: after the first call and answer, drop the other station's call sign and any proword that isn't needed.
- **Full procedure** is used when conditions are poor enough that shortcuts are causing repeats. Call signs and prowords that were optional become mandatory. Net Control orders it with **USE FULL PROCEDURE**, and back again with **USE ABBREVIATED PROCEDURE**.
- If conditions get worse still, use **WORDS TWICE**: send every call sign, word and phrase twice.

These are the steps *within* a voice tier before the channel is abandoned — the first rungs of the tier triggers the plan still needs (see the [Domain Summary](./domain-summary) methodology check).

**Call-sign identification.** Whatever procedure is in use, stations must still identify as required by their licence conditions — see [Message Handling](./message-handling). [CHECK: confirm how abbreviated procedure sits with the ACMA identification rule for a series of transmissions.] During exercises, say **"exercise only"** before your call sign every time.

## Passing messages

- **Offer** a message before sending when it must be written down, when conditions are poor, or on a directed net: *"VK6AA, THIS IS VK6BB, MESSAGE, OVER." — "SEND, OVER."*
- **LONG MESSAGE** — anything taking more than about 30 seconds. Send in 30-second sections, each ending **MORE TO FOLLOW**. The receiver acknowledges each section. Pause a few seconds so urgent traffic can get in, then continue with **ALL AFTER** and the last word sent.
- **Corrections:** **CORRECTION** then the last correct word, and carry on. If the mistake is found later, identify it: *"CORRECTION, WORD BEFORE street, Blue."*
- **Repeats:** **SAY AGAIN**, alone or with ALL AFTER, ALL BEFORE, WORD AFTER, WORD BEFORE, or FROM … TO. Reply with **I SAY AGAIN**.
- **READ BACK** — when accuracy matters or conditions are poor, the receiver reads the whole message back; the sender answers **CORRECT** or **WRONG**.
- **VERIFY** — ask the originator to check a message; the reply starts **I VERIFY**.
- **SPEAK SLOWER** — you're going too fast to write down.
- **DISREGARD THIS TRANSMISSION** — cancels a transmission before OVER or OUT. A message already sent can only be cancelled by another message (**CANCEL**).
- **ACKNOWLEDGE** — the addressee (not just the operator) confirms receipt.
- **FETCH** — ask for a specific person to come to the radio: *"FETCH Ambulance Officer."* They answer *"Ambulance Officer SPEAKING."*

Formal message layout and serial numbers are on [Message Handling](./message-handling).

## Relay

When two stations can't hear each other, a third station that can hear both relays. This is how the **voice relay network** — Strategic Coordination's Emergency tier on [Operational Comms](./operational) — actually works.

- **RELAY TO** — "please pass this to …"
- **THROUGH ME** — "I can reach them; send it through me."
- **RELAY THROUGH** — "send your message through (call sign)."

*VK6BB can't raise VK6AA, but VK6XX can hear both:*

> VK6XX, THIS IS VK6BB, RELAY TO VK6AA, move now, OVER.
> VK6BB, WAIT, OUT TO YOU. VK6AA, THIS IS VK6XX, FROM VK6BB, move now, OVER.
> VK6XX, ROGER, OUT.
> VK6BB, THIS IS VK6XX, FROM VK6AA, ROGER, OVER.
> ROGER, OUT.

The relay station always reports back that the message was delivered. Relay introduces errors, so use READ BACK for anything important.

## Running a net

Net Control Station duties are listed on [Radio Frequencies](./radio-frequency-plans). The prowords:

| Proword | Meaning |
|---|---|
| THIS IS A DIRECTED NET | From now, stations call Net Control, not each other, unless given permission |
| THIS IS A FREE NET | Stations may call each other directly |
| REPORTING INTO NET | A station joining a working net: *"(NCS), THIS IS VK6AA, REPORTING INTO NET, OVER."* |
| ASSUME CONTROL | Net Control hands the net to another station, e.g. the Alternate NCS |
| I AM ASSUMING CONTROL | The new Net Control announces it has taken over |
| NOTHING HEARD | No reply from the station called |
| UNKNOWN STATION | A caller whose call sign was lost: *"UNKNOWN STATION, THIS IS VK6AA, SAY AGAIN CALLSIGN, OVER."* |
| REQUEST TIME CHECK / TIME CHECK AT | Synchronise clocks — useful at the start of any log |
| CLOSE DOWN / CLOSING DOWN | Stations called close when told / this station is closing |

### Changing frequency

A frequency change has two parts: an order, then a separate command to go. **Nobody moves on the order alone.**

> NCS: ALL STATIONS, THIS IS VK6BB, CHANGE TO 7.090, OVER.
> *(each station acknowledges: "change to 7.090, OVER")*
> NCS: CHANGE NOW, OUT.

The [HF Propagation Plan](./HF-propagation-plan)'s frequency change procedure follows this.

## Position, grid and time

- **LOCSTAT** — a location report. Ask with *"SEND LOCSTAT"*, or give one unprompted: *"LOCSTAT, turn-off to Canning Dam."*
- **GRID** — before any grid reference: *"LOCSTAT, GRID 123456."*
- **TIME** — before any time: *"returning at TIME one four hundred hours."*

## Quick proword list

The abbreviated list from the original manual. The full list, with alternative meanings, is in Annex C of the [PDF](/assets/WICENWA-RATEL-Procedures.pdf).

| Proword | Meaning |
|---|---|
| ACKNOWLEDGE | Confirm you've received this message |
| ALL AFTER / ALL BEFORE | The part of the message after / before … |
| CANCEL | Cancel a message or part of one |
| CLOSE DOWN / CLOSING DOWN | Stations called close when told / I am closing |
| CORRECT | What you sent is correct |
| CORRECTION | I made an error; the correct version follows |
| FETCH | Bring (person) to the radio |
| FIGURES | Numbers follow, digit by digit (not used for call signs, grids, times) |
| GRID | A grid reference follows |
| I SPELL | I'll spell the next word phonetically |
| LOCSTAT | Location report |
| MESSAGE / LONG MESSAGE | A message to be written down follows |
| MORE TO FOLLOW | More of this long message comes next |
| NOTHING HEARD | No reply from the station called |
| OUT / OUT TO YOU | Finished, no reply / finished with you, calling another |
| OVER | Finished; reply |
| RADIO CHECK | How do you hear me? |
| READ BACK | Repeat the message back to me exactly |
| RELAY TO | Pass this message to … |
| ROGER | Received satisfactorily |
| SAY AGAIN / I SAY AGAIN | Repeat / I am repeating |
| SEND | Ready to receive your message |
| VERIFY | Check with the originator and send the correct version |
| WAIT / WAIT OUT | Pause up to 5 seconds / pause longer, others may transmit |
| WILCO | Received, understood, will comply (never with ROGER) |
| WORD AFTER / WORD BEFORE | Identifies part of a message |
| WORDS TWICE | Conditions are poor; send everything twice |
| WRONG | That's wrong; the correct version is … |

## What changed from the original

- Gender-neutral wording, and small errors corrected (duplicate paragraph numbers, "7075 MHz" for 7.075 MHz, READBACK / READ BACK).
- Military teletype and security-classification fields left out.
- Precedence is covered on [Message Handling](./message-handling), where the original's ROUTINE / PRIORITY / IMMEDIATE is proposed for adoption.
- Linked to the PACE domains and to the call-sign identification rule, neither of which existed when the manual was written.

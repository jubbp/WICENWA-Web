---
layout: default
title: Activation Plan
pace_nav: true
PaceNavTitle: 03. Activation
---

This is the **Activation & Alerting** domain — see the [Domain Summary](./domain-summary) for how it relates to the other domains in the plan.

This section defines how members are alerted and mobilised during an incident.

Planned events don't use activation — they follow the [Event Support](./event-support) engagement lifecycle.

Activation may occur due to:

- Natural disasters
- Requests from emergency services
- Planned public safety operations
- Training exercises

## Activation Authority

Activation may be initiated by:

How a supported agency requests WICEN is not yet defined {% include gap.html id="GAP-018" %}.

- WICEN-WA State Coordinator
- Deputy Coordinator
- WICEN Incident Coordinator — the person the State Coordinator puts in charge of WICEN's part of an incident

## Activation PACE

Triggers for stepping between tiers are not yet defined {% include gap.html id="GAP-004" %}.

| Level | Method | Description |
|------|------|-------------|
| PRIMARY | Internet Messaging | Discord / Signal (a WICEN WA app is proposed but not yet built) {% include gap.html id="GAP-005" %} {% include gap.html id="GAP-044" %} |
| ALTERNATE | Email Distribution | WICEN-WA email group |
| CONTINGENCY | SMS Broadcast | Bulk SMS alert |
| EMERGENCY | Amateur Radio Alert Net | HF activation frequency |

Alerts are not yet sent on all channels at once, and acknowledgements are not tracked {% include gap.html id="GAP-040" %}.

## Activation Message Format

All activation messages should follow a consistent structure.

WICEN-WA ACTIVATION

- Event:
- Location:
- Activation Level:
- Reporting Location:
- Primary Net Frequency:
- Where to find updates:
- Next Update Time:

Example:

WICEN-WA ACTIVATION

- Event: Bushfire Communications Support
- Location: Wheatbelt
- Activation Level: Standby
- Primary Net: 7.110 MHz LSB
- Updates: [method to be decided] {% include gap.html id="GAP-059" %}
- Next Update: 1400 WST

## WICEN Status

- Stand By
  - Members are maintaining watch for activations
- On Watch
  - An emergency condition may exist. While not activated, WICEN members are at a higher level of monitoring and preparing for activation. Members should contact the SC with their current capabilities.
- Activated
  - WICEN is activated. All members should check in if not directly activated

### Standby to On Watch

In the case that WICEN becomes aware of a possible need our assistance, the State Coordinator or their delagate will place WICEN "On Watch".

On watch moves all members into a monitoring actively for activations messages. Members actively on watch should turn on and test their equipment. They should prepare their 72 hour kit.

**No self-deployment.** No member goes to an incident area, or offers WICEN's services to an agency or the public at an incident, unless tasked by the State Coordinator or the WICEN Incident Coordinator. Being On Watch or Activated means *be ready*, not *go*. A member who is already in an affected area for their own reasons stays a private person until tasked.

The State Coordinator plans WICEN's response — appoints a Response Planner, sends the availability call-out, and works out what WICEN can offer — using [Planning a Deployment](./planning).

The State Coordinator will activate a "Watch Net" on the available frequencies in the comms plan. If necessary, they will nominate a watch station who will monitor the appropriate frequencies.

Each member on watch should check in with the SC or net controller as their status (availablity, capabilities change)

The State Coordinator will activate a digital information station. The digital information station will coordinate the distribution of information in a digital form. How it gets information to members is still to be decided {% include gap.html id="GAP-059" %}. The DIS will also instigate the Information Beacon (APRS,JS8CALL,WINLINK) which will allow members to gather information as they are possible.

### "OnWatch" to Activated

As the conditions deteriorate or as requested by a served agency, the State Coordinator or their delagate will move WICEN to "activated"

The requirements of each activation will differ and the SC will need to distribute information as to the requirements for this acivation.

Details should be quickly delivered to the DIS for distribution

## Types of Activations

When activating WICEN, the SC should determine the type of activation. If the activation is in support of a third party, there will be different requirements. The SC should determine the requirements for the activation and relay this information to the members — see [Planning a Deployment](./planning) for the request intake, sizing, availability call-out and decision.

- WICEN Activation
- Served Agency Activation
- Training

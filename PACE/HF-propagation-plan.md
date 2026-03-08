---
layout: default
title: HF Frequency Plan
pace_nav: true
PaceNavTitle: 08. HF Propagation
---

This frequency plan is designed to provide reliable HF communications
across Western Australia during emergency operations.

Propagation conditions vary significantly depending on:

- Time of day
- Solar activity
- Season
- Distance between stations

For this reason multiple bands are defined for different conditions.

Operators should select the most appropriate band based on current propagation.

## HF Propagation Characteristics in Western Australia

WA operations typically involve communication distances of:

200 km – Local regional coverage  
500 km – Regional coordination  
1000–2500 km – Statewide communications

Typical propagation behaviour:

Daytime
- 40m supports medium distances
- 20m supports long distances
- 80m becomes unreliable

Night
- 80m becomes primary statewide band
- 40m works well for medium distance
- 20m often closes for domestic paths

## Primary HF Net Frequencies

These frequencies are used for statewide coordination.

| Band | Frequency | Mode | Purpose |
|-----|-----|-----|-----|
| 40m | 7.110 MHz | LSB | Primary statewide voice net |
| 80m | 3.600 MHz | LSB | Night statewide voice net |
| 20m | 14.300 MHz | USB | Interstate liaison |

## Daytime Operations (0700–1800 WST)

Primary Band: 40m

| Frequency | Mode | Purpose |
|-----------|------|---------|
| 7.110 MHz | LSB | Statewide coordination |
| 7.090 MHz | LSB | Alternate coordination |
| 7.130 MHz | LSB | Tactical operations |

Typical daytime coverage on 40m:

Perth → Kalgoorlie  
Perth → Geraldton  
Perth → Albany  
Perth → Pilbara (variable)

Range: 300–1200 km

## Night Operations (1800–0700 WST)

Primary Band: 80m

| Frequency | Mode | Purpose |
|-----------|------|---------|
| 3.600 MHz | LSB | Statewide coordination |
| 3.650 MHz | LSB | Alternate coordination |
| 3.580 MHz | LSB | Tactical operations |

Typical night coverage on 80m:

Strong NVIS coverage across most of WA.

Reliable paths:

Perth → Southwest
Perth → Wheatbelt
Perth → Goldfields
Perth → Mid West

Range: 200–800 km

## Interstate Coordination

When communicating with eastern states groups,
20m is typically the most reliable band.

| Frequency | Mode | Purpose |
|-----------|------|---------|
| 14.300 MHz | USB | Interstate liaison |
| 14.250 MHz | USB | Alternate liaison |


---

# Digital Messaging Frequencies

These are ideal for structured messages using systems like **:contentReference[oaicite:3]{index=3}**.

```markdown
## Digital Messaging Frequencies

| Band | Frequency | Mode | Use |
|-----|-----|-----|-----|
| 40m | 7.078 MHz | JS8Call / digital | Messaging |
| 40m | 7.095 MHz | Winlink VARA | Email over HF |
| 80m | 3.595 MHz | digital | Night messaging |

## Net Schedule

Regular nets ensure all stations remain informed.

Example schedule:

00 minutes past hour  
Statewide situation report

30 minutes past hour  
Operational coordination

Additional tactical nets may operate continuously.

## Frequency Change Procedure

If interference or poor propagation occurs:

1. Net Control announces frequency change
2. All stations acknowledge
3. Net moves to alternate frequency

Example:

"All stations, move to alternate frequency
7.090 MHz in five minutes."

## Quick Band Selection Guide

Distance < 300 km  
Use 80m or VHF

Distance 300–800 km  
Use 80m NVIS or 40m

Distance 800–2000 km  
Use 40m

Interstate  
Use 20m


---
layout: default
title: Digital Messaging Architecture
pace_nav: true
PaceNavTitle: 11. Digital Messaging
---

Digital messaging provides resilient, structured communications during
emergency operations.

Advantages of digital messaging:

- Messages are not lost if operators miss a voice transmission
- Messages can be stored and forwarded
- Long text messages can be transmitted reliably
- Message history can be archived
- Messages can be relayed automatically between stations

This architecture uses two complementary systems:

Winlink – structured email-style messaging  
JS8Call – low bandwidth store-and-forward messaging

## System Overview

The WICENWA digital messaging network operates in three layers.

Internet Messaging Layer
    |
HF Gateway Stations
    |
Field Radio Stations


---

# System Roles

```markdown
## Station Roles

Three station types are used.

Gateway Stations
Relay digital traffic across Western Australia.

Regional Relay Stations
Provide regional coverage and relay traffic.

Field Stations
Portable stations used by deployed teams.

## Winlink System

Winlink provides email-style messaging over radio.

Capabilities:

- Send email over HF radio
- Structured emergency forms
- Attachments
- Message routing
- Message storage

Messages can be sent to:

Other Winlink users

Internet email addresses

Emergency coordination centres

## Winlink Station Types

RMS Gateway

Permanent stations connected to the Winlink network.

RMS Relay

Stations that relay traffic across RF without internet.

Field Winlink Stations

Portable stations used by operators in the field.

## Western Australia Winlink Topology

Suggested gateway locations:

Perth
Pilbara
Goldfields
Southwest
Midwest

These stations provide overlapping coverage across the state.

## Message Flow

Field Operator

creates message

↓

Message transmitted via HF

↓

Regional Relay Station

↓

Winlink Gateway

↓

Destination

Field station  
Incident command  
Internet email

## Suggested WA Winlink Frequencies

40m Day Operations

7.095 MHz

80m Night Operations

3.595 MHz

20m Interstate Messaging

14.095 MHz

## Recommended Emergency Forms

ICS-213
General message

ICS-214
Activity log

Situation report

Resource request



## JS8Call System

JS8Call provides very resilient HF messaging.

Advantages:

Extremely weak signal capability

Store-and-forward messaging

Automatic relays

Beacon capability

Position reporting

## JS8Call Relay Network

The network uses automatic relays.

Example topology:

Pilbara Relay
     |
Goldfields Relay
     |
Perth Relay
     |
Southwest Relay

## Message Types

Direct Message

Station to station messaging.

Group Message

Message sent to a defined group.

Store and Forward

Message held until the destination station is available.

Heartbeat

Automatic signal availability reporting.

## JS8Call Frequencies

40m Primary

7.078 MHz

80m Night

3.578 MHz

20m Interstate

14.078 MHz

## Store and Forward Messaging

JS8Call allows messages to be stored until the receiving station becomes available.

Example:

Station A sends message to Station C

Station B receives message

Station B stores message

When Station C becomes available the message is delivered

## Priority Levels

EMERGENCY

Threat to life or safety

PRIORITY

Urgent operational traffic

ROUTINE

Normal communications

## Logging Requirements

All digital traffic should be logged.

Required log information:

Message number

Origin station

Destination station

Time sent

Time received

Operator

## Voice and Digital Integration

Voice nets remain the primary coordination method.

Digital messaging should be used for:

Long messages

Formal reports

Resource requests

Message archiving

Voice Net Control

requests SITREP

↓

Station sends report via Winlink

↓

Net Control receives formatted message

## Portable Digital Station

Recommended equipment:

HF transceiver

Laptop computer

Digital interface

Portable antenna

Battery power



---

# Training Requirements

```markdown
## Operator Training

Operators using digital messaging should be trained in:

Winlink message creation

JS8Call message routing

Radio propagation awareness

Message handling procedures


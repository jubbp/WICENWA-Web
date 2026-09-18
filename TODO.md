# WICEN WA Website & PACE Plan — TODO

Working task list, organised by category. This is a live tracking document, not a
published page — update checkboxes as things land, and prune items once they're
genuinely done rather than leaving them checked forever.

## Website

- [ ] Link [Discussion Paper](discussion-paper.md) and [Mission & Aims draft](mission-and-aims.md)
      from somewhere members will actually find them (homepage, header, or
      `_includes/sidebar.html`) — right now neither is referenced from `index.md`,
      `_includes/header.html`, `_includes/footer.html`, or `_includes/sidebar.html`,
      so a member has to already know the URL.
- [ ] Reconcile the live-site URL in [README.md](README.md) (`jubbp.github.io/WICENWA-Web`)
      with the custom domain in [CNAME](CNAME) — confirm which is current and fix
      whichever is stale.
- [ ] Commit or discard the pending edits to `PACE/committee-discussion.md` and
      `discussion-paper.md` (currently modified but uncommitted).

## PACE Plan — documentation gaps (no committee decision needed, can start anytime)

From [Implementation Roadmap](PACE/implementation-roadmap.md) Phase 1 — pure
documentation work, doesn't wait on any Aims decision:

- [ ] Define the PACE triggers (when a domain steps from Primary → Alternate →
      Contingency → Emergency).
- [ ] Resolve the Activation & Alerting "distinguishability" gap noted in the roadmap.
- [ ] Fill in, or explicitly mark "not provided, by decision," the missing
      Contingency/Emergency tiers in Long-Haul Message Traffic and Cross-State
      Coordination.
- [ ] Inventory standing infrastructure WICEN WA already has informal access to —
      South West WA's APRS digipeater network and the expanding MeshCore coverage
      area — and turn it into a documented asset register ([Committee Discussion §10](PACE/committee-discussion.md)).
- [ ] Add a documented net-logging practice for Net Control — currently no
      logging responsibility was written down anywhere before this review
      ([Committee Discussion §9](PACE/committee-discussion.md)); flagged as the
      cheapest, no-dependency fix in [mission-and-aims.md](mission-and-aims.md) Aim 6.

## Committee & membership decisions needed

These block the rest of the PACE plan (see [Committee Discussion](PACE/committee-discussion.md)
"Outcome" section) and are for the committee/membership, not something to resolve
in code. Tracking them here so they don't get lost, not to imply engineering can
close them out.

- [ ] **§1 Mission & scope** — which operating model (event/training club,
      served-agency auxiliary, community-resilience, or staged hybrid)? Get an
      honest headcount of members available for multi-day deployment.
- [ ] **§2 Served agencies** — which agencies does WICEN WA want a standing
      relationship with, and is pursuing formal SEMC/role-statement recognition
      (as Victoria's WICEN has) worth chasing?
- [ ] **§3 Domain priority** — which of the five PACE domains gets finished and
      drilled first? Is Cross-State Coordination near-term or aspirational?
- [ ] **§4 Capabilities & training** — extend the Capability Self-Assessment now
      or later? Define minimum always-covered roles vs. nice-to-have. Formal
      training pathway or keep current ad-hoc schedule?
- [ ] **§5 Testing what matters** — should a domain's "Contingency" tier only
      count once exercised, not just documented?
- [ ] **§6 Community welfare messaging** — does WICEN WA want this as a distinct
      aim? If so, what intake model, and is a Red Cross WA / Register.Find.Reunite
      conversation worth pursuing?
- [ ] **§7 Capability investment** — mobile repeater for non-hams (UHF CB vs.
      licensed business band) and/or ad-hoc satellite internet: near-term
      priorities or deferred?
- [ ] **§8 Local/Tactical technology choice** — community intake layer (MeshCore
      and/or UHF CB) vs. operator-to-operator layer (APRS vs. AREDN) — decide
      independently, and in what order?
- [ ] **§9 Software integration** — standardise on EmComm Tools Community for
      field/gateway stations? Adopt Outpost-style logged messaging tied to
      ICS-213? Who owns evaluating this?
- [ ] **§10 Permanent vs. portable infrastructure** — is permanent AREDN siting
      worth pursuing now? Who's accountable for a permanent node's uptime? Define
      the standard field go-kit now, independent of the permanent-siting question.

Once §1 and §3 in particular are answered, revisit and rewrite
[mission-and-aims.md](mission-and-aims.md) and [PACE/implementation-roadmap.md](PACE/implementation-roadmap.md)
to match, per their own "what would change this draft" sections.

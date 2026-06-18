---
layout: default
title: Capability Self-Assessment
sidebar: false
---

<style>
.assess-intro {
  max-width: 800px;
  margin: 0 auto 2rem;
  padding: 1.25rem 1.5rem;
  background: #f9f9f9;
  border-left: 4px solid var(--primary-yellow);
  border-radius: 0 4px 4px 0;
}
.assess-intro p { margin: 0.5rem 0; }

.assess-section {
  max-width: 800px;
  margin: 0 auto 2.5rem;
}
.assess-section h2 {
  font-size: 1.15rem;
  font-weight: 700;
  margin-bottom: 1.25rem;
  padding: 0.6rem 1rem;
  background: var(--primary-yellow);
  color: #1a1a1a;
  border-radius: 4px;
}

.assess-item {
  margin-bottom: 1.5rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid #eee;
}
.assess-item:last-child { border-bottom: none; }
.assess-item p.question { font-weight: 600; margin-bottom: 0.25rem; }
.assess-item .hint {
  font-size: 0.88rem;
  color: #666;
  margin-bottom: 0.65rem;
}
.multi-label {
  font-size: 0.8rem;
  color: #888;
  font-style: italic;
  margin-bottom: 0.5rem;
}

.option-group { display: flex; flex-direction: column; gap: 0.35rem; }
.option-group label {
  display: flex;
  align-items: flex-start;
  gap: 0.65rem;
  padding: 0.45rem 0.75rem;
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.15s;
  font-size: 0.95rem;
}
.option-group label:hover { background: #f0f0f0; }
.option-group input { margin-top: 3px; flex-shrink: 0; }

.assess-actions {
  max-width: 800px;
  margin: 0 auto 3rem;
  text-align: center;
}
.assess-actions button {
  background: var(--primary-yellow);
  color: #1a1a1a;
  border: none;
  padding: 0.9rem 2.5rem;
  font-size: 1rem;
  font-weight: 700;
  border-radius: 4px;
  cursor: pointer;
  transition: opacity 0.2s;
}
.assess-actions button:hover { opacity: 0.85; }
.assess-actions button:disabled { opacity: 0.45; cursor: default; }

/* Result styles */
#assess-result { max-width: 800px; margin: 0 auto 3rem; display: none; }

.result-banner {
  text-align: center;
  padding: 1.75rem;
  border-radius: 6px;
  margin-bottom: 1.5rem;
}
.result-banner h2 { font-size: 1.5rem; margin-bottom: 0.5rem; }
.result-banner p { max-width: 620px; margin: 0 auto; }

.area-scores {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.75rem;
  margin-bottom: 1.5rem;
}
@media (max-width: 600px) { .area-scores { grid-template-columns: 1fr; } }

.area-card {
  padding: 0.85rem 1rem;
  border-radius: 4px;
  background: #f9f9f9;
  border-left: 4px solid var(--primary-yellow);
}
.area-card .area-name { font-weight: 700; font-size: 0.9rem; margin-bottom: 0.2rem; }
.area-card .area-bar-wrap { background: #ddd; border-radius: 3px; height: 8px; margin: 0.35rem 0; }
.area-card .area-bar { background: var(--primary-yellow); height: 8px; border-radius: 3px; transition: width 0.4s; }
.area-card .area-fraction { font-size: 0.8rem; color: #666; }

.roles-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.75rem;
  margin-bottom: 1.5rem;
}
@media (max-width: 600px) { .roles-grid { grid-template-columns: 1fr; } }

.role-card {
  padding: 0.9rem 1.1rem;
  border-radius: 4px;
  border-left: 4px solid #28a745;
  background: #f9f9f9;
}
.role-card .role-title { font-weight: 700; margin-bottom: 0.25rem; font-size: 0.95rem; }
.role-card .role-desc { font-size: 0.85rem; color: #555; }

.flag-block {
  padding: 1rem 1.25rem;
  background: #fff3cd;
  border-left: 4px solid #ffc107;
  border-radius: 4px;
  margin-bottom: 0.75rem;
  font-size: 0.92rem;
}
.flag-block strong { display: block; margin-bottom: 0.3rem; }

.report-section {
  margin-bottom: 1.5rem;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  overflow: hidden;
}
.report-section-header {
  padding: 0.75rem 1.1rem;
  font-weight: 700;
  font-size: 0.95rem;
  background: #1a1a1a;
  color: #fff;
}
.report-section-body { padding: 1rem 1.25rem; }
.report-section-body ul { padding-left: 1.2rem; margin: 0; }
.report-section-body li { margin-bottom: 0.55rem; font-size: 0.92rem; line-height: 1.5; }
.report-section-body li:last-child { margin-bottom: 0; }

.resource-list { list-style: none; padding: 0; margin: 0; }
.resource-list li {
  padding: 0.5rem 0;
  border-bottom: 1px solid #eee;
  font-size: 0.92rem;
}
.resource-list li:last-child { border-bottom: none; }
.resource-list .res-title { font-weight: 600; }
.resource-list .res-desc { color: #666; font-size: 0.85rem; }

.section-heading {
  font-size: 1.05rem;
  font-weight: 700;
  margin: 1.75rem 0 0.75rem;
  padding-bottom: 0.4rem;
  border-bottom: 2px solid var(--primary-yellow);
}

.disclaimer {
  max-width: 800px;
  margin: 0 auto 2rem;
  font-size: 0.82rem;
  color: #999;
  text-align: center;
}
</style>

<div class="assess-intro">
  <p>This assessment helps you understand how you can contribute to WICEN WA based on your <strong>current physical ability, mental readiness, equipment, and availability</strong>.</p>
  <p>At the end you will receive a personalised capability report with a suggested learning plan to develop your emergency communications skills.</p>
  <p>Be honest — there is a role for almost everyone, and knowing where you stand is the first step. Nothing you enter is stored or transmitted.</p>
</div>

<div id="assess-container"></div>

<div class="assess-actions">
  <button id="submit-btn" onclick="submitAssessment()">Generate My Capability Report</button>
</div>

<div id="assess-result"></div>

<p class="disclaimer">All results are calculated in your browser. Nothing is collected or transmitted.</p>

<script>
var SECTIONS = [
  {
    id: "physical",
    title: "1. Physical Capability",
    items: [
      {
        id: "carry",
        q: "How much equipment can you comfortably carry and set up?",
        hint: "Think about a realistic field deployment — not just a handheld, but antenna masts, cables, and batteries.",
        options: [
          { label: "Full kit — radio, battery, mast, antenna, shelter. I can deploy completely independently.", value: 3 },
          { label: "Moderate kit — radio and small battery. I may need help with heavier items.", value: 2 },
          { label: "Light kit only — handheld or tablet. I have physical limitations on lifting.", value: 1 },
          { label: "I am not able to carry or move equipment unaided.", value: 0 }
        ]
      },
      {
        id: "outdoor",
        q: "How do you handle extended outdoor conditions?",
        hint: "Deployments may involve heat, cold, wind, rain, and uneven terrain — sometimes for many hours.",
        options: [
          { label: "Comfortable for a full day or more outdoors in varied weather.", value: 3 },
          { label: "Fine for several hours; I need rest breaks or access to shade/shelter.", value: 2 },
          { label: "Limited — I can manage short outdoor stints but need shelter nearby.", value: 1 },
          { label: "I need to remain indoors or in a vehicle.", value: 0 }
        ]
      },
      {
        id: "endurance",
        q: "How long can you sustain focused work without a significant break?",
        hint: "Shift lengths at events or incidents are typically 4–6 hours.",
        options: [
          { label: "6+ hours of sustained, focused activity.", value: 3 },
          { label: "3–5 hours with short breaks.", value: 2 },
          { label: "1–2 hours before I need a meaningful rest.", value: 1 },
          { label: "Less than 1 hour of sustained focus.", value: 0 }
        ]
      }
    ]
  },
  {
    id: "mental",
    title: "2. Mental Readiness & Operating Experience",
    items: [
      {
        id: "stress",
        q: "How do you typically perform under pressure or in an unplanned situation?",
        hint: "Emergency comms can involve confusion, urgency, and incomplete information — calm, methodical operators are essential.",
        options: [
          { label: "I stay calm and work through problems methodically under pressure.", value: 3 },
          { label: "I manage well but prefer some time to settle in before taking responsibility.", value: 2 },
          { label: "Stressful situations affect me — I prefer structured, predictable tasks.", value: 1 },
          { label: "High-stress environments significantly impact my ability to function.", value: 0 }
        ]
      },
      {
        id: "direction",
        q: "How comfortable are you working within a structured chain of command?",
        hint: "WICEN operates under incident management structures (AIIMS) where operators take direction from a coordinator.",
        options: [
          { label: "Very comfortable — I follow direction and escalate problems appropriately.", value: 3 },
          { label: "Generally fine — I may ask questions but I respect the structure.", value: 2 },
          { label: "I prefer to work independently; structured authority is sometimes difficult.", value: 1 },
          { label: "I find it very hard to take direction from others in the field.", value: 0 }
        ]
      },
      {
        id: "comms_clarity",
        q: "How would you describe your spoken communication under pressure?",
        hint: "Clear, concise radio communication is critical — panic, verbosity, or hesitation can cause real problems on a net.",
        options: [
          { label: "Clear and concise — I get to the point quickly and listen actively.", value: 3 },
          { label: "Generally clear, though I can over-explain when nervous.", value: 2 },
          { label: "I sometimes struggle to express myself clearly when things are stressful.", value: 1 },
          { label: "Communication under pressure is a significant challenge for me.", value: 0 }
        ]
      },
      {
        id: "netcontrol",
        q: "Have you operated as Net Control on an amateur radio net?",
        hint: "Net Control manages all traffic on a directed net — calling stations, prioritising messages, and keeping the net orderly. It is one of the most important emcomm skills you can develop.",
        options: [
          { label: "Yes — I regularly serve as Net Control on formal amateur or emcomm nets.", value: 3 },
          { label: "Yes — I have been Net Control on a few occasions.", value: 2 },
          { label: "No, but I have studied net control procedures and feel ready to try.", value: 1 },
          { label: "No experience with Net Control — I would not know where to start.", value: 0 }
        ]
      }
    ]
  },
  {
    id: "radio",
    title: "3. Radio & Equipment",
    items: [
      {
        id: "licence",
        q: "What is your current amateur radio licence status?",
        options: [
          { label: "Licensed — Standard or Advanced.", value: 3 },
          { label: "Licensed — Foundation.", value: 2 },
          { label: "No licence, but actively studying or enrolled in a course.", value: 1 },
          { label: "No licence and not currently pursuing one.", value: 0 }
        ]
      },
      {
        id: "bands_hf",
        multiSelect: true,
        q: "Which HF bands can you currently operate on?",
        hint: "Select all that apply. For WICEN, 80m and 40m are the primary bands. More bands means more flexibility for changing propagation conditions.",
        options: [
          { label: "160m (1.8 MHz) — Top Band" },
          { label: "80m (3.5 MHz) — primary WICEN state/regional net band" },
          { label: "60m (5 MHz) — newer Australian allocation, good NVIS" },
          { label: "40m (7 MHz) — secondary WICEN net, reliable daytime regional" },
          { label: "20m (14 MHz) — long-haul, interstate and international" },
          { label: "17m (18 MHz)" },
          { label: "15m (21 MHz)" },
          { label: "12m (24 MHz)" },
          { label: "10m (28 MHz)" },
          { label: "6m (50 MHz)" }
        ],
        scoreFunc: function(sel) {
          if (sel.length === 0) return 0;
          if (sel.length === 1) return 1;
          if (sel.length <= 3) return 2;
          return 3;
        }
      },
      {
        id: "bands_vhf",
        multiSelect: true,
        q: "Which VHF/UHF bands can you operate?",
        hint: "Select all that apply.",
        options: [
          { label: "2m (144 MHz) — essential for local WICEN tactical comms" },
          { label: "70cm (430 MHz)" },
          { label: "23cm (1.2 GHz)" },
          { label: "6m (50 MHz)" },
          { label: "Other (satellite, 70 MHz, microwave, etc.)" }
        ],
        scoreFunc: function(sel) {
          var has2m   = sel.indexOf(0) >= 0;
          var has70cm = sel.indexOf(1) >= 0;
          if (sel.length === 0) return 0;
          if (sel.length === 1) return 1;
          if (has2m && has70cm) return sel.length >= 3 ? 3 : 2;
          return 2;
        }
      },
      {
        id: "portable",
        q: "Can you operate portable — away from home with a battery and a self-erected antenna?",
        hint: "Portable operation is essential for field deployment. This means no mains power and an antenna you put up yourself.",
        options: [
          { label: "Yes — I regularly operate portable and have a proven, tested field setup.", value: 3 },
          { label: "Yes — I have the equipment but limited field experience with it.", value: 2 },
          { label: "Mobile only — I can operate from a vehicle but not truly pack-and-carry portable.", value: 1 },
          { label: "No — my station is fixed/home-based and mains-dependent.", value: 0 }
        ]
      },
      {
        id: "aprs_rx",
        q: "Can you receive APRS transmissions?",
        hint: "APRS (Automatic Packet Reporting System) is used at WICEN deployments for position tracking and short messages between stations.",
        options: [
          { label: "Yes — dedicated hardware (TNC, APRS-capable radio, or SDR) decoding APRS.", value: 3 },
          { label: "Yes — via software on a laptop connected to a receiver.", value: 2 },
          { label: "Yes — via a smartphone app (e.g. APRSDroid in receive mode).", value: 1 },
          { label: "No — I cannot currently receive APRS.", value: 0 }
        ]
      },
      {
        id: "aprs_tx",
        q: "Can you transmit APRS — send your position and messages over RF?",
        hint: "RF transmit capability means sending via radio (not just internet-connected apps). This enables real tracking when infrastructure is down.",
        options: [
          { label: "Yes — dedicated hardware APRS tracker or TNC connected to a radio transmitter.", value: 3 },
          { label: "Yes — radio with built-in APRS (e.g. Kenwood TH-D74, Yaesu FT3D) or Bluetooth TNC.", value: 2 },
          { label: "App-based only — my APRS transmit goes via the internet (APRS-IS), not RF.", value: 1 },
          { label: "No — I cannot transmit APRS.", value: 0 }
        ]
      },
      {
        id: "digital_hf",
        multiSelect: true,
        q: "Which HF digital modes are you set up and operational for?",
        hint: "Select all you can currently use. Winlink HF is the top priority for WICEN emcomm. FT8 and JS8Call are excellent for propagation checks and low-power messaging.",
        options: [
          { label: "Winlink via Vara HF (software TNC)" },
          { label: "Winlink via Pactor (hardware TNC)" },
          { label: "JS8Call (keyboard-to-keyboard HF messaging)" },
          { label: "FT8 / FT4 (weak-signal propagation + messaging)" },
          { label: "PSK31 / PSK63" },
          { label: "RTTY" },
          { label: "WSPR (propagation beaconing)" },
          { label: "Other HF digital mode" }
        ],
        scoreFunc: function(sel) {
          var hasWinlink = sel.indexOf(0) >= 0 || sel.indexOf(1) >= 0;
          if (sel.length === 0) return 0;
          if (!hasWinlink) return 1;
          if (hasWinlink && sel.length < 3) return 2;
          return 3;
        }
      },
      {
        id: "digital_vhf",
        multiSelect: true,
        q: "Which VHF/UHF digital modes are you set up and operational for?",
        hint: "Select all you can currently use. Winlink via VHF adds store-and-forward messaging at events. Digital voice modes extend your reach on linked repeater networks.",
        options: [
          { label: "Winlink via Vara FM (software TNC on VHF/UHF)" },
          { label: "Winlink via Packet / AX.25 (hardware or software TNC)" },
          { label: "D-STAR (digital voice and data)" },
          { label: "DMR (Digital Mobile Radio)" },
          { label: "System Fusion / C4FM (Yaesu digital)" },
          { label: "P25" },
          { label: "Other VHF/UHF digital mode" }
        ],
        scoreFunc: function(sel) {
          var hasWinlink = sel.indexOf(0) >= 0 || sel.indexOf(1) >= 0;
          if (sel.length === 0) return 0;
          if (!hasWinlink) return 1;
          if (hasWinlink && sel.length < 3) return 2;
          return 3;
        }
      },
      {
        id: "power",
        q: "How self-sufficient is your power setup?",
        hint: "Deployments may have no mains power — your station needs to sustain itself.",
        options: [
          { label: "Fully portable — battery plus solar or generator. Independent for 24+ hours.", value: 3 },
          { label: "Battery powered for several hours, with a plan for recharge.", value: 2 },
          { label: "Mains-dependent — I would need a power source at the deployment.", value: 1 },
          { label: "I don't have a station yet.", value: 0 }
        ]
      }
    ]
  },
  {
    id: "availability",
    title: "4. Availability & Commitment",
    items: [
      {
        id: "training",
        q: "Can you attend regular training and the weekly net?",
        hint: "The WICEN WA net runs weekly at 20:00 local. Training and exercises are typically quarterly.",
        options: [
          { label: "Yes — I can commit to the weekly net and quarterly exercises.", value: 3 },
          { label: "Mostly — I will miss some nets but will attend when I can.", value: 2 },
          { label: "Occasional — I can attend a few times per year.", value: 1 },
          { label: "Very limited — my schedule makes regular attendance unlikely.", value: 0 }
        ]
      },
      {
        id: "activation",
        q: "Could you respond to an activation at short notice?",
        hint: "Some events are planned weeks in advance; others require a response within hours.",
        options: [
          { label: "Yes — I can be ready to deploy within 1–2 hours for local activations.", value: 3 },
          { label: "For planned events, yes. Short-notice callouts are difficult for me.", value: 2 },
          { label: "I can support planned events only, with several days notice.", value: 1 },
          { label: "I am not in a position to deploy for activations at this stage.", value: 0 }
        ]
      },
      {
        id: "remote",
        q: "Are you able to contribute remotely (net monitoring, liaison, planning support)?",
        hint: "Not all roles require field deployment — coordination, message relay, and background support are also vital.",
        options: [
          { label: "Yes — and I am happy to take on remote coordination roles.", value: 3 },
          { label: "Yes — remote support suits me well.", value: 2 },
          { label: "Possibly — depends on the task and timeframe.", value: 1 },
          { label: "My availability is very limited even for remote support.", value: 0 }
        ]
      }
    ]
  }
];

var responses = {};

function renderAssessment() {
  var container = document.getElementById('assess-container');
  SECTIONS.forEach(function(section) {
    var sDiv = document.createElement('div');
    sDiv.className = 'assess-section';
    sDiv.innerHTML = '<h2>' + section.title + '</h2>';

    section.items.forEach(function(item) {
      var iDiv = document.createElement('div');
      iDiv.className = 'assess-item';

      var pEl = document.createElement('p');
      pEl.className = 'question';
      pEl.textContent = item.q;
      iDiv.appendChild(pEl);

      if (item.hint) {
        var hint = document.createElement('div');
        hint.className = 'hint';
        hint.textContent = item.hint;
        iDiv.appendChild(hint);
      }

      if (item.multiSelect) {
        var ml = document.createElement('div');
        ml.className = 'multi-label';
        ml.textContent = 'Select all that apply — leave unchecked if none apply.';
        iDiv.appendChild(ml);
        responses[section.id + '-' + item.id] = [];
      }

      var group = document.createElement('div');
      group.className = 'option-group';

      if (item.multiSelect) {
        item.options.forEach(function(opt, oi) {
          var label = document.createElement('label');
          var cb = document.createElement('input');
          cb.type = 'checkbox';
          cb.name = section.id + '-' + item.id;
          cb.value = oi;
          (function(index) {
            cb.addEventListener('change', function() {
              var arr = responses[section.id + '-' + item.id];
              if (cb.checked) {
                arr.push(index);
              } else {
                var pos = arr.indexOf(index);
                if (pos >= 0) arr.splice(pos, 1);
              }
            });
          })(oi);
          label.appendChild(cb);
          label.appendChild(document.createTextNode(opt.label));
          group.appendChild(label);
        });
      } else {
        item.options.forEach(function(opt) {
          var label = document.createElement('label');
          var radio = document.createElement('input');
          radio.type = 'radio';
          radio.name = section.id + '-' + item.id;
          radio.value = opt.value;
          radio.addEventListener('change', function() {
            responses[section.id + '-' + item.id] = opt.value;
          });
          label.appendChild(radio);
          label.appendChild(document.createTextNode(opt.label));
          group.appendChild(label);
        });
      }

      iDiv.appendChild(group);
      sDiv.appendChild(iDiv);
    });
    container.appendChild(sDiv);
  });
}

function getItemScore(section, item) {
  var key = section.id + '-' + item.id;
  if (item.multiSelect) {
    var sel = responses[key] || [];
    return item.scoreFunc ? item.scoreFunc(sel) : Math.min(3, sel.length);
  }
  var val = responses[key];
  return val !== undefined ? val : 0;
}

function submitAssessment() {
  // Count unanswered single-select items only
  var unanswered = 0;
  SECTIONS.forEach(function(s) {
    s.items.forEach(function(item) {
      if (!item.multiSelect && responses[s.id + '-' + item.id] === undefined) {
        unanswered++;
      }
    });
  });
  if (unanswered > 0) {
    if (!confirm(unanswered + ' question(s) are unanswered. Submit anyway?')) return;
  }

  document.getElementById('submit-btn').disabled = true;

  var scores = {};
  SECTIONS.forEach(function(section) {
    var total = 0, max = section.items.length * 3;
    section.items.forEach(function(item) {
      total += getItemScore(section, item);
    });
    scores[section.id] = { score: total, max: max, pct: total / max };
  });

  renderResult(scores);
  document.getElementById('assess-result').style.display = 'block';
  document.getElementById('assess-result').scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function r(key) {
  return responses[key] !== undefined ? responses[key] : 0;
}
function ms(key) {
  return responses[key] || [];
}

function renderResult(scores) {
  var el = document.getElementById('assess-result');

  // Shorthand response lookups
  var licenceVal    = r('radio-licence');
  var portableVal   = r('radio-portable');
  var aprsRxVal     = r('radio-aprs_rx');
  var aprsTxVal     = r('radio-aprs_tx');
  var powerVal      = r('radio-power');
  var ncVal         = r('mental-netcontrol');
  var activationVal = r('availability-activation');
  var remoteVal     = r('availability-remote');
  var physPct       = scores.physical.pct;
  var mentPct       = scores.mental.pct;
  var availPct      = scores.availability.pct;

  var bandsHf  = ms('radio-bands_hf');
  var bandsVhf = ms('radio-bands_vhf');
  var digHf    = ms('radio-digital_hf');
  var digVhf   = ms('radio-digital_vhf');

  // Key flags derived from multi-select
  var has80m      = bandsHf.indexOf(1) >= 0;
  var has40m      = bandsHf.indexOf(3) >= 0;
  var has20m      = bandsHf.some(function(i) { return i >= 4; });
  var has2m       = bandsVhf.indexOf(0) >= 0;
  var has70cm     = bandsVhf.indexOf(1) >= 0;
  var hasWinlinkHf  = digHf.indexOf(0) >= 0 || digHf.indexOf(1) >= 0;
  var hasWinlinkVhf = digVhf.indexOf(0) >= 0 || digVhf.indexOf(1) >= 0;
  var hasJS8      = digHf.indexOf(2) >= 0;
  var hasFT8      = digHf.indexOf(3) >= 0;
  var hasDstar    = digVhf.indexOf(2) >= 0;
  var hasDMR      = digVhf.indexOf(3) >= 0;
  var hasFusion   = digVhf.indexOf(4) >= 0;

  // ---- Overall summary ----
  var overallScore = scores.physical.score + scores.mental.score + scores.radio.score + scores.availability.score;
  var overallMax   = scores.physical.max   + scores.mental.max   + scores.radio.max   + scores.availability.max;
  var overallPct   = overallScore / overallMax;

  var summaryText, summaryBg;
  if (overallPct >= 0.75) {
    summaryText = "You have strong all-round capability and are well placed for active field deployment with WICEN WA.";
    summaryBg = "background:#d4edda; border:2px solid #28a745;";
  } else if (overallPct >= 0.5) {
    summaryText = "You have solid foundations. A few targeted steps will bring you to full deployment readiness.";
    summaryBg = "background:#cce5ff; border:2px solid #004085;";
  } else if (overallPct >= 0.25) {
    summaryText = "You are beginning your WICEN journey. There are roles suited to you now and a clear path to more.";
    summaryBg = "background:#fff3cd; border:2px solid #ffc107;";
  } else {
    summaryText = "Now is a great time to start building toward WICEN involvement. Support roles are available to you today.";
    summaryBg = "background:#f0f0f0; border:2px solid #aaa;";
  }

  var html = '<div class="result-banner" style="' + summaryBg + '">' +
    '<h2>Your WICEN WA Capability Report</h2>' +
    '<p>' + summaryText + '</p>' +
    '</div>';

  // ---- Area scores ----
  html += '<p class="section-heading">Capability by Area</p><div class="area-scores">';
  var areaLabels = { physical: 'Physical', mental: 'Mental & Operating', radio: 'Radio & Equipment', availability: 'Availability' };
  SECTIONS.forEach(function(s) {
    var sc = scores[s.id];
    var pctW = Math.round(sc.pct * 100);
    html += '<div class="area-card">' +
      '<div class="area-name">' + areaLabels[s.id] + '</div>' +
      '<div class="area-bar-wrap"><div class="area-bar" style="width:' + pctW + '%"></div></div>' +
      '<div class="area-fraction">' + sc.score + ' / ' + sc.max + ' (' + pctW + '%)</div>' +
      '</div>';
  });
  html += '</div>';

  // ---- Flags ----
  var flags = [];
  if (licenceVal === 0) flags.push({ h: "No amateur radio licence", b: 'A licence is required to transmit. The Foundation course is the single most impactful step you can take right now. <a href="/get-involved">Get in touch</a> and we can point you to local options.' });
  if (licenceVal === 1) flags.push({ h: "Foundation licence", b: "Foundation covers most VHF/UHF work and some HF. A Standard licence upgrade unlocks full HF access and higher power — the key next milestone." });
  if (physPct < 0.34) flags.push({ h: "Physical limitations noted", b: "Field deployment may not suit you right now — but remote support, net participation, and Winlink relay roles are equally vital and need no physical presence." });
  if (bandsHf.length === 0) flags.push({ h: "No HF capability yet", b: "HF is the backbone of WICEN long-distance comms. Even a modest second-hand transceiver with a wire antenna makes a big difference." });
  if (bandsVhf.length === 0) flags.push({ h: "No VHF/UHF capability", b: "VHF/UHF is used for local tactical comms at every WICEN event. A 2m handheld is the lowest-cost way to become immediately deployable." });

  if (flags.length > 0) {
    html += '<p class="section-heading">Things to Note</p>';
    flags.forEach(function(f) {
      html += '<div class="flag-block"><strong>' + f.h + '</strong>' + f.b + '</div>';
    });
  }

  // ---- Roles ----
  var roles = [];
  if (physPct >= 0.67 && mentPct >= 0.67 && has80m && portableVal >= 2 && licenceVal >= 2 && activationVal >= 2) {
    roles.push({ t: "Field HF Operator", d: "Deploy as a self-sufficient portable HF station at incidents and events." });
  }
  if (physPct >= 0.34 && mentPct >= 0.67 && has2m && licenceVal >= 1 && activationVal >= 1) {
    roles.push({ t: "VHF/UHF Field Support", d: "Portable VHF/UHF tactical coverage at events and incidents." });
  }
  if (aprsTxVal >= 2 && licenceVal >= 1) {
    roles.push({ t: "APRS Tracker Operator", d: "RF-based position tracking and short messaging at deployments." });
  }
  if (hasWinlinkHf || hasWinlinkVhf) {
    roles.push({ t: "Winlink / Digital Operator", d: "Store-and-forward email messaging over radio when voice or internet is unavailable." });
  }
  if (ncVal >= 2 && licenceVal >= 2) {
    roles.push({ t: "Net Control", d: "Direct net traffic, manage check-ins, and coordinate message flow on WICEN nets." });
  }
  if (mentPct >= 0.67 && licenceVal >= 2 && availPct >= 0.67) {
    roles.push({ t: "Net Participant", d: "Regular check-in on the weekly WICEN WA net and exercise nets." });
  }
  if (mentPct >= 0.67 && remoteVal >= 2) {
    roles.push({ t: "Remote Support / Liaison", d: "Off-site coordination, message relay, and background logistics support." });
  }
  if (licenceVal <= 1) {
    roles.push({ t: "Support / Observer", d: "Assist with non-radio tasks at events while working toward your licence or upgrade." });
  }
  if (roles.length === 0) {
    roles.push({ t: "Community Associate", d: "Stay connected with WICEN WA while building readiness over time." });
  }

  html += '<p class="section-heading">Roles You Can Fill Today</p><div class="roles-grid">';
  roles.forEach(function(role) {
    html += '<div class="role-card"><div class="role-title">' + role.t + '</div><div class="role-desc">' + role.d + '</div></div>';
  });
  html += '</div>';

  // ---- Learning Plan ----
  var immediate = [], shortTerm = [], longerTerm = [];

  // Immediate
  if (licenceVal === 0) {
    immediate.push('Register for a Foundation licence course — contact the WIA or a local amateur radio club for the next course date');
  }
  if (licenceVal >= 1 && bandsVhf.length === 0) {
    immediate.push('Get a 2m handheld (HT) — this is the fastest single step to becoming deployable. Budget options start around $60–80 AUD');
  }
  if (licenceVal >= 1 && aprsRxVal === 0) {
    immediate.push('Install <strong>APRSDroid</strong> on your Android phone (free) to start monitoring APRS traffic on 144.575 MHz — no hardware needed beyond your phone');
  }
  if (licenceVal >= 1 && bandsHf.length > 0 && digHf.length === 0) {
    immediate.push('Install <strong>WSJT-X</strong> (free) and try FT8 — it introduces you to computer-audio radio interfaces and weak-signal digital modes, and is a direct stepping stone to Winlink');
  }
  if (licenceVal >= 1) {
    immediate.push('Join the WICEN WA weekly net: <strong>3.600 MHz LSB</strong> at 20:00 local — or via the WA AllStar linked repeater network on 2m');
  }
  if (ncVal === 0) {
    immediate.push('Listen to several directed nets and note how Net Control manages check-ins, handles traffic, and closes the net — the WICEN WA weekly net is a good starting point');
  }
  if (!hasWinlinkHf && !hasWinlinkVhf && licenceVal >= 1) {
    immediate.push('Create a free Winlink account at <strong>winlink.org</strong> and explore the RMS gateway map to see what HF and VHF gateways are reachable from your location');
  }

  // Short-term (1–3 months)
  if (licenceVal === 1) {
    shortTerm.push('Begin studying for the <strong>Standard licence upgrade</strong> — the WIA offers a self-study guide and the upgrade exam can be sat at most radio clubs. Standard opens full HF access.');
  }
  if (bandsHf.length > 0 && portableVal < 2) {
    shortTerm.push('Practice portable HF operation — set up in a local park or reserve to get comfortable with field antennas, guying a mast, and running from battery. A SOTA or POTA activation is an excellent structured exercise.');
  }
  if (!hasWinlinkHf && licenceVal >= 2 && bandsHf.length > 0) {
    shortTerm.push('Set up <strong>Winlink via Vara HF</strong> — Vara HF (free tier is usable), a basic soundcard interface, and your HF rig is all you need. The Winlink website has setup guides for Windows and Linux.');
  }
  if (!hasWinlinkVhf && has2m && licenceVal >= 1) {
    shortTerm.push('Try <strong>Winlink via Vara FM</strong> on 2m — find local RMS gateways on the Winlink gateway map and send a test email. Vara FM is free and works with any 2m radio and a soundcard.');
  }
  if (aprsTxVal < 2 && licenceVal >= 1 && has2m) {
    shortTerm.push('Explore low-cost APRS transmit options — a <strong>Mobilinkd TNC</strong> (~$80–100 AUD) pairs via Bluetooth with your handheld and the APRSDroid app to give you RF APRS transmit capability without modifying your radio.');
  }
  if (ncVal < 2 && licenceVal >= 2) {
    shortTerm.push('Volunteer to <strong>shadow Net Control</strong> on the WICEN WA net or a local club net, then take a turn under supervision. Net Control is a skill that only develops through practice.');
  }
  if (!hasDstar && !hasDMR && !hasFusion && has2m) {
    shortTerm.push('Investigate <strong>digital voice modes</strong> (D-STAR, DMR, or System Fusion) available on WA repeaters — these extend your reach via linked networks and add redundancy to voice comms when FM congestion is an issue.');
  }
  if (!hasJS8 && !hasFT8 && bandsHf.length > 0 && licenceVal >= 2) {
    shortTerm.push('Set up <strong>JS8Call</strong> — a keyboard-to-keyboard HF messaging mode that works at very low signal levels. Useful for HF text messaging when voice and Winlink gateways are unavailable.');
  }

  // Longer-term (3–12 months)
  if (bandsHf.length === 0 && licenceVal >= 2) {
    longerTerm.push('Save toward an entry-level HF transceiver — an Icom IC-7300 or similar, paired with a simple wire dipole for 80m/40m, is the foundation of a capable WICEN field station. Second-hand options are widely available.');
  }
  if (bandsHf.length > 0 && !has80m) {
    longerTerm.push('Add <strong>80m capability</strong> — it is the primary WICEN state net band. If your rig covers it but you lack an antenna, a simple half-wave dipole is inexpensive and effective.');
  }
  if (has80m && !has40m) {
    longerTerm.push('Add <strong>40m capability</strong> — the secondary WICEN net band and the most reliable daytime HF band for regional communications in WA.');
  }
  if (bandsHf.length > 0 && !has20m) {
    longerTerm.push('Consider adding <strong>20m capability</strong> — essential for interstate coordination and useful when 80m/40m propagation is poor during the day.');
  }
  if (powerVal < 2) {
    longerTerm.push('Build out your <strong>portable power system</strong> — a 20–30 Ah lithium iron phosphate (LiFePO4) battery with a small folding solar panel gives you 12–24 hours of self-sufficient HF operation at typical WICEN duty cycles.');
  }
  if (!hasWinlinkHf && licenceVal >= 2) {
    longerTerm.push('Develop <strong>Winlink HF proficiency</strong> — practice sending and receiving formatted messages, explore the ICS-213 form template, and learn to connect to gateways via Ardop or Vara HF on different bands.');
  }
  longerTerm.push('Complete <strong>FEMA ICS-100</strong> (Introduction to ICS) — free online at training.fema.gov. This is the foundation of how WICEN interfaces with emergency management agencies.');
  longerTerm.push('Attend a WICEN WA exercise or community event to put your skills into practice in a supervised environment — see the <a href="/events">Events</a> page for upcoming activities.');

  html += '<p class="section-heading">Your Personalised Learning Plan</p>';

  if (immediate.length > 0) {
    html += '<div class="report-section">' +
      '<div class="report-section-header">Immediate — This Week</div>' +
      '<div class="report-section-body"><ul>';
    immediate.forEach(function(s) { html += '<li>' + s + '</li>'; });
    html += '</ul></div></div>';
  }

  if (shortTerm.length > 0) {
    html += '<div class="report-section">' +
      '<div class="report-section-header">Short-Term — 1 to 3 Months</div>' +
      '<div class="report-section-body"><ul>';
    shortTerm.forEach(function(s) { html += '<li>' + s + '</li>'; });
    html += '</ul></div></div>';
  }

  if (longerTerm.length > 0) {
    html += '<div class="report-section">' +
      '<div class="report-section-header">Longer-Term — 3 to 12 Months</div>' +
      '<div class="report-section-body"><ul>';
    longerTerm.forEach(function(s) { html += '<li>' + s + '</li>'; });
    html += '</ul></div></div>';
  }

  // ---- Resources ----
  var resources = [
    { t: "WICEN WA PACE Plan", d: "How WICEN WA is structured and how activations work.", url: "/PACE/overview" },
    { t: "Wireless Institute of Australia (WIA)", d: "Licence courses, study guides, and exam bookings.", url: "https://www.wia.org.au" },
    { t: "Winlink Global Radio Email", d: "Create your account, find gateways, and download Winlink Express.", url: "https://www.winlink.org" },
    { t: "WSJT-X (FT8/FT4/WSPR)", d: "Free software for weak-signal digital modes — the gateway to HF digital.", url: "https://wsjt.sourceforge.io" },
    { t: "JS8Call", d: "Keyboard-to-keyboard HF messaging at low power and weak signals.", url: "http://js8call.com" },
    { t: "APRSDroid", d: "Android APRS app for receive and internet-linked TX. Free.", url: "https://aprsdroid.org" },
    { t: "Dire Wolf (Software TNC)", d: "Free software TNC for APRS and packet on Windows/Linux — pairs with any soundcard.", url: "https://github.com/wb2osz/direwolf" },
    { t: "FEMA ICS-100 (Free Online)", d: "Introduction to the Incident Command System — essential for all WICEN operators.", url: "https://training.fema.gov/is/courseoverview.aspx?code=IS-100.c" },
    { t: "ARRL Emergency Communications Handbook", d: "The definitive reference for amateur radio emergency communications procedures.", url: "https://www.arrl.org/emergency-communications-handbook" }
  ];

  html += '<p class="section-heading">Recommended Resources</p>' +
    '<ul class="resource-list">';
  resources.forEach(function(res) {
    html += '<li><div class="res-title"><a href="' + res.url + '">' + res.t + '</a></div>' +
      '<div class="res-desc">' + res.d + '</div></li>';
  });
  html += '</ul>';

  el.innerHTML = html;
}

renderAssessment();
</script>

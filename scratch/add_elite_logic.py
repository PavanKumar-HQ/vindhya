#!/usr/bin/env python3
"""
Add elite presentation and workshop logic to app.js:
- Session Stopwatch
- Slide Navigator Modal (Hotkey G)
- One-Click Copy on all prompt boxes with Brandex Toast
- Interactive Option Voting with Web Audio chime
- High-Contrast Projector Boost mode
- Socratic AI Simulator engine
"""

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_logic = """
/* ==========================================================================
   ELITE WORKSHOP FEATURES IMPLEMENTATION
   ========================================================================== */

// 1. Session Stopwatch (120-min workshop telemetry)
let sessionTimerSeconds = 0;
let sessionTimerInterval = null;
let sessionTimerRunning = false;

function startSessionTimer() {
  if (sessionTimerRunning) return;
  sessionTimerRunning = true;
  const dot = document.querySelector('.timer-dot');
  if (dot) dot.classList.remove('paused');
  sessionTimerInterval = setInterval(() => {
    sessionTimerSeconds++;
    const mins = String(Math.floor(sessionTimerSeconds / 60)).padStart(2, '0');
    const secs = String(sessionTimerSeconds % 60).padStart(2, '0');
    const el = document.getElementById('sessionTimerText');
    if (el) el.textContent = `⏱️ ${mins}:${secs}`;
  }, 1000);
}

function pauseSessionTimer() {
  sessionTimerRunning = false;
  clearInterval(sessionTimerInterval);
  const dot = document.querySelector('.timer-dot');
  if (dot) dot.classList.add('paused');
}

function toggleSessionTimer() {
  if (sessionTimerRunning) {
    pauseSessionTimer();
    showToast('Workshop timer paused', '⏸️');
  } else {
    startSessionTimer();
    showToast('Workshop timer started', '▶️');
  }
}

// 2. Slide Navigator Modal (Hotkey: G)
function openSlideNavigator() {
  const modal = document.getElementById('slideNavModal');
  if (!modal) return;
  populateSlideNavigator();
  modal.classList.add('open');
}

function closeSlideNavigator(e) {
  if (e && e.target && e.target.closest('.nav-modal-content')) return;
  const modal = document.getElementById('slideNavModal');
  if (modal) modal.classList.remove('open');
}

function populateSlideNavigator() {
  const grid = document.getElementById('navSlidesGrid');
  if (!grid) return;
  grid.innerHTML = '';

  const slides = document.querySelectorAll('.carousel-slide');
  slides.forEach((slide, idx) => {
    const sec = slide.dataset.section || 'WORKSHOP';
    const title = slide.dataset.title || `Slide ${idx + 1}`;
    const isCurrent = idx === appState.currentSlide;

    const thumb = document.createElement('div');
    thumb.className = `nav-slide-thumb ${isCurrent ? 'current-slide' : ''}`;
    thumb.dataset.section = sec;
    thumb.innerHTML = `
      <div class="nst-top">
        <span class="nst-num">SLIDE ${String(idx + 1).padStart(2, '0')}</span>
        <span class="nst-sec">${sec.split('•')[0].trim()}</span>
      </div>
      <div class="nst-title">${title}</div>
    `;
    thumb.onclick = () => {
      goToSlide(idx);
      closeSlideNavigator();
      showToast(`Jumped to Slide ${idx + 1}: ${title.split('•')[0].trim()}`, '🧭');
    };
    grid.appendChild(thumb);
  });
}

function filterNavGrid(filter) {
  document.querySelectorAll('#navFilterChips .n-chip').forEach(c => c.classList.remove('active'));
  event.target.classList.add('active');

  const thumbs = document.querySelectorAll('.nav-slide-thumb');
  thumbs.forEach(t => {
    if (filter === 'ALL') {
      t.style.display = 'flex';
    } else {
      const match = t.dataset.section.toUpperCase().includes(filter.toUpperCase());
      t.style.display = match ? 'flex' : 'none';
    }
  });
}

// 3. High-Contrast Projector Boost Mode
function toggleProjectorBoost() {
  document.body.classList.toggle('projector-boost');
  const isBoosted = document.body.classList.contains('projector-boost');
  const btn = document.getElementById('projectorBoostBtn');
  if (btn) {
    btn.innerHTML = isBoosted ? '💡 Projector Mode: ON' : '💡 Projector Mode';
    btn.classList.toggle('btn-primary', isBoosted);
    btn.classList.toggle('btn-outline', !isBoosted);
  }
  showToast(isBoosted ? 'High-Contrast Projector Boost enabled' : 'Projector mode disabled', '💡');
}

// 4. Web Audio Harmonic Chime (Zero external dependencies)
function playHarmonicChime(freq = 587.33, duration = 0.15) {
  try {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (!AudioContext) return;
    const ctx = new AudioContext();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();

    osc.type = 'sine';
    osc.frequency.setValueAtTime(freq, ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(freq * 1.5, ctx.currentTime + duration);

    gain.gain.setValueAtTime(0.08, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);

    osc.connect(gain);
    gain.connect(ctx.destination);

    osc.start();
    osc.stop(ctx.currentTime + duration);
  } catch (err) {
    // Ignore audio restrictions
  }
}

// 5. Toast Notifications
function showToast(message, icon = '⚡') {
  const container = document.getElementById('toastContainer');
  if (!container) return;
  const toast = document.createElement('div');
  toast.className = 'toast-message';
  toast.innerHTML = `<span>${icon}</span> <span>${message}</span>`;
  container.appendChild(toast);
  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(10px)';
    toast.style.transition = 'all 0.25s ease-out';
    setTimeout(() => toast.remove(), 250);
  }, 2500);
}

// 6. Interactive Audience Voting & Option Selection
function initInteractiveAudienceVoting() {
  document.addEventListener('click', (e) => {
    const optionCard = e.target.closest('.option-card, .vote-option');
    if (!optionCard) return;

    // Toggle highlight
    const parentGrid = optionCard.parentElement;
    if (parentGrid) {
      parentGrid.querySelectorAll('.option-card, .vote-option').forEach(c => c.classList.remove('highlight', 'vo-winner'));
    }
    optionCard.classList.add(optionCard.classList.contains('vote-option') ? 'vo-winner' : 'highlight');

    // Sound chime
    playHarmonicChime(523.25, 0.12);

    const label = optionCard.innerText.split('\\n')[0].substring(0, 30);
    showToast(`Audience Choice Recorded: "${label}..."`, '🗳️');
  });
}

// 7. Click-to-Copy on All Prompts
function initClickToCopyPrompts() {
  document.addEventListener('click', (e) => {
    const promptBox = e.target.closest('.prompt-box-editorial, .prompt-terminal-card, .demo-prompt-card');
    if (!promptBox) return;

    const text = promptBox.innerText || promptBox.textContent;
    if (text && text.trim().length > 0) {
      navigator.clipboard.writeText(text.trim()).then(() => {
        playHarmonicChime(659.25, 0.15);
        showToast('Prompt copied to clipboard! Ready to paste into ChatGPT/Gemini.', '📋');
      }).catch(() => {
        showToast('Prompt selected! Press Ctrl+C to copy.', '📋');
      });
    }
  });
}

// 8. Socratic AI Tutor Simulator Modal
function openSocraticSimulator() {
  const modal = document.getElementById('socraticSimModal');
  if (modal) modal.classList.add('open');
}

function closeSocraticSimulator(e) {
  if (e && e.target && e.target.closest('.sim-modal-content')) return;
  const modal = document.getElementById('socraticSimModal');
  if (modal) modal.classList.remove('open');
}

function loadSimSample(type) {
  const input = document.getElementById('simStudentInput');
  if (!input) return;
  if (type === 'flawed') {
    input.value = "When the bus stops suddenly, the passengers fall forward because the bus pushes them forward.";
  } else if (type === 'partial') {
    input.value = "Because of inertia the passengers fall forward when the brakes are applied.";
  } else if (type === 'perfect') {
    input.value = "Due to inertia of motion, the passenger's upper body continues in forward motion while the lower body stops with the bus.";
  }
}

function clearSimInput() {
  const input = document.getElementById('simStudentInput');
  const res = document.getElementById('simFeedbackResult');
  if (input) input.value = '';
  if (res) res.style.display = 'none';
}

function runSocraticSimEvaluation() {
  const input = document.getElementById('simStudentInput');
  const res = document.getElementById('simFeedbackResult');
  if (!input || !res) return;

  const val = input.value.toLowerCase().trim();
  if (!val) {
    showToast('Please type or select a student attempt first!', '⚠️');
    return;
  }

  playHarmonicChime(783.99, 0.2);

  let marks = 0;
  let feedback = '';
  let statusBadge = '';

  if (val.includes('inertia of motion') && (val.includes('continue') || val.includes('forward') || val.includes('upper'))) {
    marks = 2;
    statusBadge = '<span class="brutal-sticker sticker-lime">FULL 2/2 MARKS • EXCELLENT</span>';
    feedback = `
      <p style="color: var(--bx-emerald); font-weight: 700; margin-bottom: 0.5rem;">🎯 Full Marks Awarded!</p>
      <p style="font-size: 0.95rem; color: #cbd5e1; line-height: 1.6;">
        <strong>Examiner Check:</strong> Identified <em>'Inertia of motion'</em> + explained that the upper body tends to resist change in its state of motion while feet come to rest with the bus.<br>
        <strong>Board Key Match:</strong> 100% compliant with Karnataka State Board evaluation guidelines.
      </p>
    `;
  } else if (val.includes('pushes') || val.includes('push')) {
    marks = 0;
    statusBadge = '<span class="brutal-sticker sticker-pink">0/2 MARKS • CRITICAL MISCONCEPTION</span>';
    feedback = `
      <p style="color: var(--bx-rose); font-weight: 700; margin-bottom: 0.5rem;">❌ Scientific Error Detected!</p>
      <p style="font-size: 0.95rem; color: #cbd5e1; line-height: 1.6;">
        <strong>The Misconception:</strong> The bus applied a <em>backward braking force</em>, not a forward push!<br>
        <strong>Socratic Prompt:</strong> Why would passengers move forward if no forward force was applied? What did Newton's First Law say about objects already in motion?
      </p>
    `;
  } else {
    marks = 1;
    statusBadge = '<span class="brutal-sticker sticker-yellow">1/2 MARKS • PARTIAL ANSWER</span>';
    feedback = `
      <p style="color: var(--bx-amber); font-weight: 700; margin-bottom: 0.5rem;">⚠️ Missing Scientific Keyword!</p>
      <p style="font-size: 0.95rem; color: #cbd5e1; line-height: 1.6;">
        <strong>The Gap:</strong> You mentioned 'inertia', but the board marking scheme strictly requires specifying <strong>'Inertia of motion'</strong> (not inertia of rest).<br>
        <strong>Try again:</strong> Rewrite specifying which type of inertia resisted the sudden stop!
      </p>
    `;
  }

  res.innerHTML = `
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
      <span style="font-family: var(--font-mono); font-size: 0.85rem; font-weight: 800; color: #fff;">SOCRATIC AI EVALUATION:</span>
      ${statusBadge}
    </div>
    ${feedback}
  `;
  res.style.display = 'block';
}

// Enhance keyboard shortcuts (G for Navigator)
const oldInitKeyNav = initKeyboardNavigation;
initKeyboardNavigation = function() {
  document.addEventListener('keydown', (e) => {
    if (['TEXTAREA', 'INPUT'].includes(document.activeElement.tagName)) return;

    if (e.key === 'g' || e.key === 'G') {
      const modal = document.getElementById('slideNavModal');
      if (modal && modal.classList.contains('open')) {
        closeSlideNavigator();
      } else {
        openSlideNavigator();
      }
      return;
    }

    if (e.key === 'Escape') {
      closeSlideNavigator();
      closeSocraticSimulator();
      return;
    }
  });

  if (typeof oldInitKeyNav === 'function') oldInitKeyNav();
};

// Auto-start session timer on first slide transition
document.addEventListener('DOMContentLoaded', () => {
  startSessionTimer();
  initInteractiveAudienceVoting();
  initClickToCopyPrompts();
});

// Expose global functions
window.toggleSessionTimer = toggleSessionTimer;
window.openSlideNavigator = openSlideNavigator;
window.closeSlideNavigator = closeSlideNavigator;
window.filterNavGrid = filterNavGrid;
window.toggleProjectorBoost = toggleProjectorBoost;
window.showToast = showToast;
window.openSocraticSimulator = openSocraticSimulator;
window.closeSocraticSimulator = closeSocraticSimulator;
window.loadSimSample = loadSimSample;
window.clearSimInput = clearSimInput;
window.runSocraticSimEvaluation = runSocraticSimEvaluation;
"""

# Append new logic right before the last line
js = js.strip() + "\n\n" + new_logic + "\n"

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js with elite workshop logic!")

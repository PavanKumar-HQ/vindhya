#!/usr/bin/env python3
"""
Add elite presentation workshop features:
1. Session Stopwatch (Live 120-min workshop telemetry)
2. Slide Navigator Modal (Press G or click counter to jump to any of 36 slides)
3. One-Click Copy on all Slide Prompts with Toast Notifications
4. Interactive Audience Voting with Web Audio chime
5. High-Contrast Projector Boost Mode
6. Live Socratic AI Tutor Simulator Modal
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Header Actions
old_header_actions = """      <!-- Utility Actions -->
      <div class="header-right-actions">
        <button type="button" class="btn btn-outline btn-xs" id="fullscreenToggleBtn" onclick="toggleFullscreen()" title="Toggle Fullscreen for Stage Projection (Hotkey: F)">
          ⛶ Fullscreen Stage [F]
        </button>
      </div>"""

new_header_actions = """      <!-- Utility Actions -->
      <div class="header-right-actions">
        <!-- Live Workshop Session Timer -->
        <div class="session-timer-pill" id="sessionTimerDisplay" onclick="toggleSessionTimer()" title="Click to Start / Pause Workshop Timer">
          <span class="timer-dot"></span>
          <span class="timer-text" id="sessionTimerText">⏱️ 00:00</span>
        </div>

        <!-- Slide Navigator Quick-Jump -->
        <button type="button" class="btn btn-outline btn-xs" onclick="openSlideNavigator()" title="Jump to any slide (Hotkey: G)">
          🧭 Navigator [G]
        </button>

        <!-- Projector Contrast Boost -->
        <button type="button" class="btn btn-outline btn-xs" id="projectorBoostBtn" onclick="toggleProjectorBoost()" title="Toggle High-Contrast for Dim Projectors">
          💡 Projector Mode
        </button>

        <!-- Fullscreen Stage Projection -->
        <button type="button" class="btn btn-primary btn-xs" id="fullscreenToggleBtn" onclick="toggleFullscreen()" title="Toggle Fullscreen Stage (Hotkey: F)">
          ⛶ Fullscreen [F]
        </button>
      </div>"""

if old_header_actions in html:
    html = html.replace(old_header_actions, new_header_actions)
    print("Updated header actions with Timer, Navigator, and Projector Boost!")

# 2. Make the deck counter clickable to open Navigator
html = html.replace('<div class="deck-counter">', '<div class="deck-counter clickable-counter" onclick="openSlideNavigator()" title="Click to open Slide Navigator (Hotkey: G)">')

# 3. Add Slide Navigator Modal, Socratic Simulator Modal, and Toast Container before </body>
modals_html = """
  <!-- ========================================================================= -->
  <!-- 🧭 SLIDE QUICK-NAVIGATOR MODAL (HOTKEY: G)                                 -->
  <!-- ========================================================================= -->
  <div class="nav-modal-backdrop" id="slideNavModal" onclick="closeSlideNavigator(event)">
    <div class="nav-modal-content" onclick="event.stopPropagation()">
      <div class="nav-modal-header">
        <div class="nav-header-left">
          <span class="nav-title-icon">🧭</span>
          <div>
            <h3 class="nav-title">SLIDE NAVIGATOR</h3>
            <p class="nav-subtitle">Click any slide to jump instantly &bull; Press <kbd>Esc</kbd> or <kbd>G</kbd> to close</p>
          </div>
        </div>
        <div class="nav-filter-chips" id="navFilterChips">
          <button type="button" class="n-chip active" onclick="filterNavGrid('ALL')">ALL (36)</button>
          <button type="button" class="n-chip" onclick="filterNavGrid('MODULE 1')">MOD 1: REALITY</button>
          <button type="button" class="n-chip" onclick="filterNavGrid('MODULE 2')">MOD 2: 6 JOBS</button>
          <button type="button" class="n-chip" onclick="filterNavGrid('MODULE 3')">MOD 3: 3 TOOLS</button>
          <button type="button" class="n-chip" onclick="filterNavGrid('MODULE 4')">MOD 4: DEMO 1</button>
          <button type="button" class="n-chip" onclick="filterNavGrid('MODULE 5')">MOD 5: EXAM PREP</button>
          <button type="button" class="n-chip" onclick="filterNavGrid('MODULE 6')">MOD 6: NOTEBOOKLM</button>
          <button type="button" class="n-chip" onclick="filterNavGrid('MODULE 7')">MOD 7: PROMPTING</button>
          <button type="button" class="n-chip" onclick="filterNavGrid('MODULE 8')">MOD 8: MISTAKES</button>
          <button type="button" class="n-chip" onclick="filterNavGrid('MODULE 9')">MOD 9: LAB</button>
        </div>
        <button type="button" class="nav-close-btn" onclick="closeSlideNavigator()" aria-label="Close Navigator">&times;</button>
      </div>
      <div class="nav-grid" id="navSlidesGrid">
        <!-- Dynamically populated by app.js -->
      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- 🤖 SOCRATIC AI TUTOR INTERACTIVE STAGE SIMULATOR MODAL                     -->
  <!-- ========================================================================= -->
  <div class="sim-modal-backdrop" id="socraticSimModal" onclick="closeSocraticSimulator(event)">
    <div class="sim-modal-content" onclick="event.stopPropagation()">
      <div class="sim-modal-header">
        <div class="sim-header-title">
          <span class="sim-sparkle">✨</span>
          <div>
            <h3>LIVE SOCRATIC AI TUTOR SIMULATOR</h3>
            <p>Auditorium Interactive Demonstration &bull; Karnataka Board Science</p>
          </div>
        </div>
        <button type="button" class="nav-close-btn" onclick="closeSocraticSimulator()">&times;</button>
      </div>
      <div class="sim-modal-body">
        <div class="sim-question-card">
          <span class="sim-badge">BOARD EXAM QUESTION (2 MARKS)</span>
          <h4>“When a moving bus suddenly stops, why do passengers fall forward?”</h4>
        </div>

        <div class="sim-interactive-area">
          <label for="simStudentInput" class="sim-label">Type a student attempt (or click a sample):</label>
          <div class="sim-sample-chips">
            <button type="button" class="sample-chip" onclick="loadSimSample('flawed')">Sample A: “The bus pushes them forward.” (0 Marks)</button>
            <button type="button" class="sample-chip" onclick="loadSimSample('partial')">Sample B: “Because of inertia they fall.” (1 Mark)</button>
            <button type="button" class="sample-chip" onclick="loadSimSample('perfect')">Sample C: “Inertia of motion keeps upper body moving.” (2 Marks)</button>
          </div>
          <textarea id="simStudentInput" class="form-input form-textarea" placeholder="Type what a Class 9/10 student might say..."></textarea>
          <div class="sim-actions-row">
            <button type="button" class="btn btn-primary" onclick="runSocraticSimEvaluation()">⚡ Evaluate with Socratic AI</button>
            <button type="button" class="btn btn-outline" onclick="clearSimInput()">Clear</button>
          </div>
        </div>

        <div class="sim-feedback-result" id="simFeedbackResult" style="display: none;">
          <!-- Dynamically populated -->
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- 🍞 GLOBAL TOAST NOTIFICATION CONTAINER                                    -->
  <!-- ========================================================================= -->
  <div id="toastContainer" class="toast-container" aria-live="polite"></div>
"""

if '<div class="nav-modal-backdrop"' not in html:
    html = html.replace('</body>', modals_html + '\n</body>')
    print("Added Navigator Modal, Socratic Simulator Modal, and Toast Container to index.html!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully!")

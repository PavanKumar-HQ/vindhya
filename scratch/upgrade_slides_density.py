with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace Slide 2 Content
old_slide2 = '''        <!-- MERGED SLIDE 02: THE REAL QUESTION &bull; EXAM IN 7 DAYS -->
        <div class="carousel-slide" data-index="1" data-section="0–15 MIN • PART 1: AI FOR EXAMS" data-title="THE REAL QUESTION &bull; EXAM IN 7 DAYS">
          <div class="merged-slide-container">
            <div class="merged-slide-header">
              <div class="m-badge-group">
                <span class="m-badge badge-gradient">0–15 MIN • PART 1: AI FOR EXAMS</span>
                <span class="m-badge badge-navy">PART 02 OF 36</span>
              </div>
              <h2 class="m-slide-title">THE REAL QUESTION <span class="title-sep">&bull;</span> EXAM IN 7 DAYS</h2>
            </div>
            
            <div class="merged-slide-grid">
              <div class="m-panel panel-left">
                <div class="slide-content-box center-aligned">
            <h2 class="slide-title-large">
              AI CAN GIVE YOU AN ANSWER.<br>
              <span class="text-highlight">BUT CAN IT HELP YOU LEARN?</span>
            </h2>
            <div class="comparison-cards-editorial mt-3" style="max-width: 650px; margin: 1.5rem auto;">
              <div class="comp-box">
                <span class="comp-who">ANSWER</span>
                <p class="comp-quote">Appears on screen in 3s.<br>Zero brain effort.</p>
              </div>
              <div class="comp-box highlight">
                <span class="comp-who">UNDERSTANDING</span>
                <p class="comp-quote">Stays in your memory.<br>Scores in the board exam.</p>
              </div>
            </div>
            <p class="slide-quote-sub">An answer appearing on your screen doesn't mean learning happened.</p>
          </div>
              </div>
              <div class="m-panel panel-right">
                <div class="slide-content-box">
            <span class="slide-eyebrow">RELATABLE SITUATION</span>
            <h2 class="slide-heading-standard">EXAM IN 7 DAYS.</h2>
            <div class="bullet-list-editorial">
              <div class="bullet-item">• 6 chapters left to cover</div>
              <div class="bullet-item">• One chapter makes absolutely no sense</div>
              <div class="bullet-item">• You don't know what to revise</div>
              <div class="bullet-item">• You don't know if you're prepared</div>
              <div class="bullet-item highlight">• It's 10:30 PM. What are you doing?</div>
            </div>
          </div>
              </div>
            </div>
          </div>
        </div>'''

new_slide2 = '''        <!-- MERGED SLIDE 02: THE REAL QUESTION &bull; EXAM IN 7 DAYS -->
        <div class="carousel-slide" data-index="1" data-section="0–15 MIN • PART 1: AI FOR EXAMS" data-title="THE REAL QUESTION &bull; EXAM IN 7 DAYS">
          <div class="merged-slide-container">
            <div class="merged-slide-header">
              <div class="m-badge-group">
                <span class="m-badge badge-gradient">0–15 MIN • PART 1: AI FOR EXAMS</span>
                <span class="m-badge badge-navy">PART 02 OF 36</span>
              </div>
              <h2 class="m-slide-title">THE REAL QUESTION <span class="title-sep">&bull;</span> EXAM IN 7 DAYS</h2>
            </div>
            
            <div class="merged-slide-grid">
              <div class="m-panel panel-left">
                <div class="slide-content-box center-aligned">
                  <span class="slide-eyebrow">🧠 THE REAL EXAM TRUTH</span>
                  <h2 class="slide-title-large">
                    AI CAN GIVE YOU AN ANSWER.<br>
                    <span class="text-highlight">BUT CAN IT HELP YOU LEARN?</span>
                  </h2>
                  <div class="comparison-cards-editorial mt-2">
                    <div class="comp-box col-bad">
                      <span class="comp-who">❌ JUST GETTING ANSWERS</span>
                      <p class="comp-quote">Appears on screen in 3s.<br>Zero brain effort.</p>
                      <div class="contrast-tag tag-bad">Memory Retention: 0% 📉</div>
                    </div>
                    <div class="comp-box col-good highlight">
                      <span class="comp-who">⚡ ACTIVE UNDERSTANDING</span>
                      <p class="comp-quote">Stays in your long-term memory.<br>Scores in the Board Exam!</p>
                      <div class="contrast-tag tag-good">Memory Retention: 95% 🔥</div>
                    </div>
                  </div>
                  <div class="retention-meter-card">
                    <div class="meter-row">
                      <div class="meter-label"><span>Passive Copy-Paste:</span> <strong>0% In-Brain Memory</strong></div>
                      <div class="meter-track"><div class="meter-fill fill-bad" style="width: 14%;"></div></div>
                    </div>
                    <div class="meter-row mt-2">
                      <div class="meter-label"><span>Active AI Study Loop:</span> <strong>95% Exam Recall 🏆</strong></div>
                      <div class="meter-track"><div class="meter-fill fill-good" style="width: 95%;"></div></div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="m-panel panel-right">
                <div class="slide-content-box">
                  <div class="poster-badge-row">
                    <span class="slide-eyebrow">⏰ RELATABLE NIGHTMARE</span>
                    <span class="brutal-sticker sticker-pink">PANIC MODE: ON 🚨</span>
                  </div>
                  <h2 class="slide-heading-standard">EXAM IN 7 DAYS.</h2>
                  <div class="bullet-list-editorial">
                    <div class="bullet-item"><span class="b-icon">📚</span> <span>6 heavy chapters left to revise</span></div>
                    <div class="bullet-item"><span class="b-icon">🤯</span> <span>One science chapter makes zero sense</span></div>
                    <div class="bullet-item"><span class="b-icon">❓</span> <span>You don't know what questions will come for 4 marks</span></div>
                    <div class="bullet-item"><span class="b-icon">🥶</span> <span>You don't know if you're actually prepared</span></div>
                    <div class="bullet-item highlight"><span class="b-icon">🌙</span> <span><strong>It's 10:30 PM. What is your actual move?</strong></span></div>
                  </div>
                  <div class="panic-meter-strip">
                    <span class="panic-icon">⚡</span>
                    <div><strong>STUDENT CHOICE:</strong> Panic & scroll reels... OR turn AI into your private 24/7 tutor?</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>'''

# Replace Slide 3 Content
old_slide3 = '''        <!-- MERGED SLIDE 03: WHAT'S YOUR MOVE? &bull; WHAT IF D WAS DIFFERENT? -->
        <div class="carousel-slide" data-index="2" data-section="0–15 MIN • PART 1: AI FOR EXAMS" data-title="WHAT'S YOUR MOVE? &bull; WHAT IF D WAS DIFFERENT?">
          <div class="merged-slide-container">
            <div class="merged-slide-header">
              <div class="m-badge-group">
                <span class="m-badge badge-gradient">0–15 MIN • PART 1: AI FOR EXAMS</span>
                <span class="m-badge badge-navy">PART 03 OF 36</span>
              </div>
              <h2 class="m-slide-title">WHAT'S YOUR MOVE? <span class="title-sep">&bull;</span> WHAT IF D WAS DIFFERENT?</h2>
            </div>
            
            <div class="merged-slide-grid">
              <div class="m-panel panel-left">
                <div class="slide-content-box">
            <span class="slide-eyebrow">DON'T THINK. JUST SHOUT THE LETTER!</span>
            <h2 class="slide-heading-standard">WHAT'S YOUR MOVE?</h2>
            <div class="options-grid">
              <div class="option-card"><span class="opt-letter">A</span> “I'll start tomorrow at 5 AM.” (And sleep till 8)</div>
              <div class="option-card"><span class="opt-letter">B</span> Watch a 30-min YouTube video at 2x.</div>
              <div class="option-card"><span class="opt-letter">C</span> Call my friend and panic together.</div>
              <div class="option-card highlight"><span class="opt-letter">D</span> Ask AI.</div>
            </div>
            <div class="slide-bottom-note">By the end of this session, we'll see what happens when you choose D properly.</div>
          </div>
              </div>
              <div class="m-panel panel-right">
                <div class="slide-content-box center-aligned">
            <span class="slide-eyebrow">THE PARADIGM SHIFT</span>
            <h2 class="slide-title-large">WHAT IF...</h2>
            <p class="slide-statement">Instead of: <strong style="color: var(--brand-red);">“Give me the answer.”</strong></p>
            <div class="flow-sequence-box mt-2" style="max-width: 720px; margin: 1rem auto;">
              <div class="seq-step">EXPLAIN</div>
              <div class="seq-arr">→</div>
              <div class="seq-step">ASK</div>
              <div class="seq-arr">→</div>
              <div class="seq-step">PRACTISE</div>
              <div class="seq-arr">→</div>
              <div class="seq-step">CHECK</div>
              <div class="seq-arr">→</div>
              <div class="seq-step highlight">REVISE</div>
            </div>
            <p class="slide-quote-sub">From Answer Machine &rarr; to Study Partner.</p>
          </div>
              </div>
            </div>
          </div>
        </div>'''

new_slide3 = '''        <!-- MERGED SLIDE 03: WHAT'S YOUR MOVE? &bull; WHAT IF D WAS DIFFERENT? -->
        <div class="carousel-slide" data-index="2" data-section="0–15 MIN • PART 1: AI FOR EXAMS" data-title="WHAT'S YOUR MOVE? &bull; WHAT IF D WAS DIFFERENT?">
          <div class="merged-slide-container">
            <div class="merged-slide-header">
              <div class="m-badge-group">
                <span class="m-badge badge-gradient">0–15 MIN • PART 1: AI FOR EXAMS</span>
                <span class="m-badge badge-navy">PART 03 OF 36</span>
              </div>
              <h2 class="m-slide-title">WHAT'S YOUR MOVE? <span class="title-sep">&bull;</span> WHAT IF D WAS DIFFERENT?</h2>
            </div>
            
            <div class="merged-slide-grid">
              <div class="m-panel panel-left">
                <div class="slide-content-box">
                  <span class="slide-eyebrow">📢 DON'T THINK. JUST SHOUT THE LETTER!</span>
                  <h2 class="slide-heading-standard">WHAT'S YOUR MOVE?</h2>
                  <div class="options-grid">
                    <div class="option-card" onclick="castAudienceVote(this)"><span class="opt-letter">A</span> <span>“I'll start tomorrow at 5 AM.” <small style="color: var(--nb-ink-muted);">(And sleep till 8:00 AM 😴)</small></span></div>
                    <div class="option-card" onclick="castAudienceVote(this)"><span class="opt-letter">B</span> <span>Watch a 30-min YouTube video at 2x speed <small style="color: var(--nb-ink-muted);">(Learn nothing ⏩)</small></span></div>
                    <div class="option-card" onclick="castAudienceVote(this)"><span class="opt-letter">C</span> <span>Call best friend and panic together 😭</span></div>
                    <div class="option-card highlight" onclick="castAudienceVote(this)"><span class="opt-letter">D</span> <span>Make AI test me & explain like a personal coach 🔥</span></div>
                  </div>
                  <div class="slide-bottom-note">🎯 <strong>CHALLENGE:</strong> Which option sounds like you? Shout it out right now!</div>
                </div>
              </div>
              <div class="m-panel panel-right">
                <div class="slide-content-box center-aligned">
                  <span class="slide-eyebrow">🚀 THE PARADIGM SHIFT</span>
                  <h2 class="slide-title-large">WHAT IF AI WAS YOUR EXAM COACH?</h2>
                  <p class="slide-statement">Instead of lazy shortcut: <strong style="color: var(--nb-coral);">“Write my homework answer.”</strong></p>
                  <div class="flow-sequence-box">
                    <div class="seq-step"><span class="step-num">1.</span> EXPLAIN 💡</div>
                    <div class="seq-arr">➔</div>
                    <div class="seq-step"><span class="step-num">2.</span> ASK 🎯</div>
                    <div class="seq-arr">➔</div>
                    <div class="seq-step"><span class="step-num">3.</span> PRACTISE ✍️</div>
                    <div class="seq-arr">➔</div>
                    <div class="seq-step"><span class="step-num">4.</span> CHECK 🔍</div>
                    <div class="seq-arr">➔</div>
                    <div class="seq-step highlight"><span class="step-num">5.</span> REVISE 🏆</div>
                  </div>
                  <div class="poster-footer-strip">
                    <span class="strip-icon">💡</span> <strong>THE BIG SECRET:</strong> From passive "Answer Machine" ➔ to active personal Exam Coach!
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>'''

if old_slide2 in c:
    c = c.replace(old_slide2, new_slide2, 1)
    print('Slide 2 upgraded!')
else:
    print('Failed to find old_slide2')

if old_slide3 in c:
    c = c.replace(old_slide3, new_slide3, 1)
    print('Slide 3 upgraded!')
else:
    print('Failed to find old_slide3')

# Add modal tools launcher
old_modal_body = '<div class="sim-modal-body">\n        <table class="shortcuts-table">'
new_modal_body = '''<div class="sim-modal-body">
        <!-- Quick Action Launcher Tiles -->
        <div class="modal-tools-launcher-grid">
          <button type="button" class="btn btn-outline btn-sm" onclick="closeShortcutsModal(); openSlideNavigator();">🧭 Slide Navigator [G]</button>
          <button type="button" class="btn btn-outline btn-sm" onclick="closeShortcutsModal(); openSocraticSimulator();">🤖 Socratic Simulator [S]</button>
          <button type="button" class="btn btn-outline btn-sm" onclick="closeShortcutsModal(); openCheatsheetModal();">📄 Student Cheatsheet [C]</button>
          <button type="button" class="btn btn-outline btn-sm" onclick="toggleBrutalistTheme();">☀️ Toggle Theme [D]</button>
          <button type="button" class="btn btn-outline btn-sm" onclick="toggleProjectorBoost();">💡 Projector Boost [B]</button>
          <button type="button" class="btn btn-outline btn-sm" onclick="toggleAudioMute();">🔊 Audio Mute [M]</button>
          <button type="button" class="btn btn-outline btn-sm" onclick="closeShortcutsModal(); switchMainMode('overview');">📖 Workshop Guide</button>
        </div>
        <table class="shortcuts-table">'''

if old_modal_body in c:
    c = c.replace(old_modal_body, new_modal_body, 1)
    print('Modal launcher added!')
else:
    print('Failed to find modal body')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Index.html updated successfully!')

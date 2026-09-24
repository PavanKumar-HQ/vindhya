import re

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx_start = html.find('id="labContainer"')
idx_end = html.find('</main>', idx_start)

if idx_start == -1 or idx_end == -1:
    print("Error: labContainer not found in index.html")
    exit(1)

new_lab_html = '''id="labContainer" style="display: none;">

    <div class="lab-nav-bar">
      <div class="lab-meta-group">
        <span class="lab-active-badge">STUDENT LAB</span>
        <span class="lab-current-topic" id="labTopicDisplay">Topic: <strong>Newton's First Law</strong> (Class 9)</span>
      </div>

      <div class="lab-arrow-controls">
        <button type="button" class="btn btn-outline btn-xs" onclick="prevLabMission()">‹ Prev Mission</button>
        <span class="lab-step-indicator" id="labStepIndicator">Mission Setup</span>
        <button type="button" class="btn btn-outline btn-xs" onclick="nextLabMission()">Next Mission ›</button>
      </div>

      <div class="lab-right-tools">
        <div class="lab-timer-chip">
          <span>⏱️</span>
          <span class="lab-timer-digits" id="labTimerDigits">60:00</span>
          <button type="button" class="btn-timer-toggle" id="labTimerToggleBtn" onclick="toggleLabTimer()">Start</button>
        </div>
      </div>
    </div>

    <!-- 5 MISSIONS + SETUP + FINAL STEPPER DOTS -->
    <div class="lab-stepper-dots" id="labStepperDots">
      <div class="m-dot active" data-m="0" onclick="goToLabMission(0)">Setup</div>
      <div class="m-dot" data-m="1" onclick="goToLabMission(1)">M1. I Don't Get It</div>
      <div class="m-dot" data-m="2" onclick="goToLabMission(2)">M2. Two AIs</div>
      <div class="m-dot" data-m="3" onclick="goToLabMission(3)">M3. Don't Give Answer</div>
      <div class="m-dot" data-m="4" onclick="goToLabMission(4)">M4. Study My Material</div>
      <div class="m-dot" data-m="5" onclick="goToLabMission(5)">M5. Final Boss</div>
      <div class="m-dot" data-m="6" onclick="goToLabMission(6)">Final Submission</div>
    </div>

    <!-- LAB MISSIONS VIEWPORT -->
    <div class="lab-missions-viewport">
      <button type="button" class="carousel-nav-btn lab-arrow lab-prev-arrow" onclick="prevLabMission()" aria-label="Previous Mission">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>
      </button>

      <div class="lab-screens-container">

        <!-- SCREEN 0: SETUP -->
        <div class="lab-card-screen active" data-step="0">
          <div class="lab-screen-content">
            <div class="panel-header-strip">
              <span class="panel-tag tag-yellow">GENIUSPHERE AI EXAM LAB &bull; 60 MINUTES</span>
            </div>
            <h2 class="mission-title">Use AI to Solve a Real Study Problem</h2>
            <p class="mission-subtitle"><strong>The Mission:</strong> Use AI to solve a real study problem &mdash; <em>without letting AI do the learning for you.</em></p>
            
            <div class="three-pillars-strip mt-3 mb-3">
              <div class="pillar-chip bg-yellow">🤖 CHATGPT</div>
              <div class="pillar-chip bg-cyan">✨ GEMINI</div>
              <div class="pillar-chip bg-pink">📚 NOTEBOOKLM</div>
            </div>

            <form id="labSetupForm" onsubmit="event.preventDefault(); nextLabMission();">
              <div class="form-grid-editorial">
                <div class="form-group">
                  <label for="studentNameInput">Student Name / Roll No</label>
                  <input type="text" id="studentNameInput" class="form-input" placeholder="e.g. Rahul S. / Roll 14">
                </div>

                <div class="form-group">
                  <label>Your Class</label>
                  <div class="pills-row" id="classSelector">
                    <button type="button" class="pill active" data-class="Class 9">Class 9</button>
                    <button type="button" class="pill" data-class="Class 10">Class 10</button>
                  </div>
                </div>

                <div class="form-group full-width">
                  <label for="topicInput">Choose ONE Topic You Genuinely Find Difficult</label>
                  <input type="text" id="topicInput" class="form-input" placeholder="e.g. Newton's First Law of Motion, Ohm's Law, Heredity, Ray Optics" value="Newton's First Law of Motion">
                  <div class="quick-chips-row mt-2">
                    <span class="quick-label">Suggestions:</span>
                    <span class="q-chip" data-chip="Newton's First Law of Motion">Newton's First Law</span>
                    <span class="q-chip" data-chip="Electric Current & Ohm's Law">Electricity &amp; Ohm's Law</span>
                    <span class="q-chip" data-chip="Resistance in Series & Parallel">Resistors in Series/Parallel</span>
                    <span class="q-chip" data-chip="Heredity and Evolution">Heredity &amp; Evolution</span>
                  </div>
                </div>
              </div>

              <div class="screen-action-row mt-4">
                <button type="submit" class="btn btn-primary btn-lg">Start 60-Minute Lab Practical &rarr;</button>
              </div>
            </form>
          </div>
        </div>

        <!-- SCREEN 1: MISSION 1 — “I DON'T GET IT” -->
        <div class="lab-card-screen" data-step="1">
          <div class="lab-screen-content">
            <div class="panel-header-strip">
              <span class="panel-tag tag-yellow">MISSION 01 &bull; 10 MINUTES &bull; TOOL: CHATGPT</span>
            </div>
            <h2 class="mission-title">MISSION 1 &mdash; “I DON'T GET IT”</h2>
            
            <div class="story-highlight-box mb-3">
              <p>Choose <strong>one topic you genuinely find difficult</strong> from a subject you're studying.</p>
              <p class="story-punchline mt-1" style="font-size: 1.05rem !important;">Don't ask: “Give me notes on this topic.” Instead, try to make AI teach you.</p>
            </div>

            <div class="bullet-list-editorial mb-3">
              <div class="bullet-item"><div class="bullet-icon bg-yellow">1</div><div class="bullet-text"><strong>Ask ChatGPT to explain the topic simply</strong></div></div>
              <div class="bullet-item"><div class="bullet-icon bg-cyan">2</div><div class="bullet-text"><strong>Give you a real-life example</strong></div></div>
              <div class="bullet-item"><div class="bullet-icon bg-green">3</div><div class="bullet-text"><strong>Ask you one question to check your understanding</strong></div></div>
            </div>

            <div class="prompt-box">
              <div class="prompt-header">
                <span class="prompt-label">🤖 CHATGPT TUTOR PROMPT</span>
                <button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy Prompt 📋</button>
              </div>
              <div class="prompt-text">"I am a <span class="var-class">Class 9</span> student. I don't understand <span class="var-topic">Newton's First Law of Motion</span>. Explain it simply, give me a real-life example, then ask me one question to check my understanding. Don't give me the answer until I respond."</div>
            </div>

            <div class="lab-submit-card mt-3">
              <h4 class="submit-card-title">📝 Mission 1 Submission</h4>
              <div class="form-group mt-2">
                <label>Topic:</label>
                <input type="text" id="m1_topic" class="form-input var-topic-input" placeholder="Topic name">
              </div>
              <div class="form-group mt-2">
                <label>What did you understand better?</label>
                <textarea id="m1_better" class="form-textarea" rows="2" placeholder="Write 1-2 sentences on what clicked for you..."></textarea>
              </div>
              <div class="form-group mt-2">
                <label>Did AI's first explanation work for you?</label>
                <div class="pills-row" id="m1_worked">
                  <button type="button" class="pill active" onclick="setSubPill(this, 'm1_worked', 'Yes')">Yes</button>
                  <button type="button" class="pill" onclick="setSubPill(this, 'm1_worked', 'No')">No</button>
                </div>
              </div>
            </div>

            <div class="screen-action-row mt-3">
              <button type="button" class="btn btn-outline" onclick="prevLabMission()">&larr; Back</button>
              <button type="button" class="btn btn-primary" onclick="nextLabMission()">Complete Mission 1 &rarr;</button>
            </div>
          </div>
        </div>

        <!-- SCREEN 2: MISSION 2 — “TWO AIs, ONE QUESTION” -->
        <div class="lab-card-screen" data-step="2">
          <div class="lab-screen-content">
            <div class="panel-header-strip">
              <span class="panel-tag tag-cyan">MISSION 02 &bull; 10 MINUTES &bull; TOOLS: CHATGPT + GEMINI</span>
            </div>
            <h2 class="mission-title">MISSION 2 &mdash; “TWO AIs, ONE QUESTION”</h2>
            <p class="mission-subtitle">Take the <strong>same topic</strong> from Mission 1. Ask ChatGPT and Gemini to explain it using the exact same request.</p>

            <div class="comparison-card mt-2 mb-3">
              <div class="compare-col" style="background: #FFFBEB;">
                <span class="compare-badge bg-yellow" style="color:#000;">TOOL 1: CHATGPT</span>
                <p>Run your prompt in ChatGPT</p>
              </div>
              <div class="compare-versus-badge">VS</div>
              <div class="compare-col" style="background: #ECFEFF;">
                <span class="compare-badge bg-cyan" style="color:#000;">TOOL 2: GEMINI</span>
                <p>Run the exact same prompt in Gemini</p>
              </div>
            </div>

            <div class="lesson-banner mb-3" style="background: #F0FDF4; border: 1.5px solid #22C55E; padding: 0.75rem 1rem; border-radius: 8px;">
              💡 <strong>Core Lesson:</strong> Different AI response &ne; automatically wrong. Compare to find which explanation clicks for you!
            </div>

            <div class="lab-submit-card">
              <h4 class="submit-card-title">📝 Mission 2 Submission</h4>
              <div class="form-group mt-2">
                <label>Which explanation was easier for ME to understand? Why?</label>
                <textarea id="m2_easier" class="form-textarea" rows="2" placeholder="e.g. ChatGPT used a school-bus example which clicked, while Gemini used bullet points..."></textarea>
              </div>
              <div class="form-group mt-2">
                <label>Check against your textbook: Did the textbook support the explanation?</label>
                <div class="pills-row" id="m2_textbook">
                  <button type="button" class="pill active" onclick="setSubPill(this, 'm2_textbook', 'Yes')">Yes</button>
                  <button type="button" class="pill" onclick="setSubPill(this, 'm2_textbook', 'No')">No</button>
                  <button type="button" class="pill" onclick="setSubPill(this, 'm2_textbook', 'Not sure')">Not sure</button>
                </div>
              </div>
            </div>

            <div class="screen-action-row mt-3">
              <button type="button" class="btn btn-outline" onclick="prevLabMission()">&larr; Back</button>
              <button type="button" class="btn btn-primary" onclick="nextLabMission()">Complete Mission 2 &rarr;</button>
            </div>
          </div>
        </div>

        <!-- SCREEN 3: MISSION 3 — “DON'T GIVE ME THE ANSWER” -->
        <div class="lab-card-screen" data-step="3">
          <div class="lab-screen-content">
            <div class="panel-header-strip">
              <span class="panel-tag tag-pink">MISSION 03 &bull; 12 MINUTES &bull; TOOL: CHATGPT OR GEMINI</span>
            </div>
            <h2 class="mission-title">MISSION 3 &mdash; “DON'T GIVE ME THE ANSWER”</h2>

            <div class="story-highlight-box mb-3">
              <p>Choose a topic you've already studied. Ask AI to give you <strong>one exam-style question</strong>.</p>
              <p class="story-punchline mt-1" style="font-size: 1.05rem !important;">Rule: You must answer before asking AI for feedback.</p>
            </div>

            <div class="prompt-box">
              <div class="prompt-header">
                <span class="prompt-label">🥊 SPARRING &amp; CHECK PROMPT</span>
                <button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy Prompt 📋</button>
              </div>
              <div class="prompt-text">"I have studied <span class="var-topic">Newton's First Law</span>. Give me ONE exam-style question. Do not show me the answer until I respond."

[Type your own answer]

"Check my answer like a teacher. Tell me:
1. What I got right
2. What I misunderstood
3. What I should improve
Do not rewrite the complete answer for me. Give me a hint so I can improve it myself."</div>
            </div>

            <div class="lab-submit-card mt-3">
              <h4 class="submit-card-title">📝 Mission 3 Submission</h4>
              <div class="form-group mt-2">
                <label>What mistake did you discover in your answer?</label>
                <textarea id="m3_mistake" class="form-textarea" rows="2" placeholder="e.g. I forgot to mention external unbalanced force..."></textarea>
              </div>
              <div class="form-group mt-2">
                <label>What did you change in your improved answer?</label>
                <textarea id="m3_changed" class="form-textarea" rows="2" placeholder="e.g. In my second draft, I added both states of motion to score full marks..."></textarea>
              </div>
            </div>

            <div class="screen-action-row mt-3">
              <button type="button" class="btn btn-outline" onclick="prevLabMission()">&larr; Back</button>
              <button type="button" class="btn btn-primary" onclick="nextLabMission()">Complete Mission 3 &rarr;</button>
            </div>
          </div>
        </div>

        <!-- SCREEN 4: MISSION 4 — “STUDY MY MATERIAL” -->
        <div class="lab-card-screen" data-step="4">
          <div class="lab-screen-content">
            <div class="panel-header-strip">
              <span class="panel-tag tag-green">MISSION 04 &bull; 12 MINUTES &bull; TOOL: NOTEBOOKLM</span>
            </div>
            <h2 class="mission-title">MISSION 4 &mdash; “STUDY MY MATERIAL”</h2>
            <p class="mission-subtitle">Open the prepared Geniusphere NotebookLM material. Choose one section/topic.</p>

            <div class="prompt-box mt-2">
              <div class="prompt-header"><span class="prompt-label">📚 STEP 1: EXTRACT KEY CONCEPTS</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
              <div class="prompt-text">"Based only on the study material I provided, identify the key concepts I should understand for my exam. Explain them briefly in simple language."</div>
            </div>

            <div class="prompt-box mt-2">
              <div class="prompt-header"><span class="prompt-label">🔍 STEP 2: SIMPLIFY DIFFICULT CONCEPT</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
              <div class="prompt-text">"I don't understand this concept. Explain it in simpler language using an everyday example. Stay close to my study material."</div>
            </div>

            <div class="prompt-box mt-2">
              <div class="prompt-header"><span class="prompt-label">🎯 STEP 3: TEST YOURSELF</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
              <div class="prompt-text">"Using only my study material, ask me one question about this concept. Don't give me the answer until I respond."</div>
            </div>

            <div class="lab-submit-card mt-3">
              <h4 class="submit-card-title">📝 Mission 4 Submission</h4>
              <div class="form-group mt-2">
                <label>Concept I struggled with:</label>
                <input type="text" id="m4_struggled" class="form-input" placeholder="e.g. Resistance vs Resistivity">
              </div>
              <div class="form-group mt-2">
                <label>Something I understood better:</label>
                <textarea id="m4_understood" class="form-textarea" rows="2" placeholder="Explain what clicked using your textbook material..."></textarea>
              </div>
            </div>

            <div class="screen-action-row mt-3">
              <button type="button" class="btn btn-outline" onclick="prevLabMission()">&larr; Back</button>
              <button type="button" class="btn btn-primary" onclick="nextLabMission()">Complete Mission 4 &rarr;</button>
            </div>
          </div>
        </div>

        <!-- SCREEN 5: MISSION 5 — FINAL BOSS -->
        <div class="lab-card-screen" data-step="5">
          <div class="lab-screen-content">
            <div class="panel-header-strip">
              <span class="panel-tag tag-pink">MISSION 05 &bull; 10 MINUTES &bull; TOOL: YOUR CHOICE</span>
            </div>
            <h2 class="mission-title">MISSION 5 &mdash; FINAL BOSS</h2>

            <div class="story-highlight-box mb-3">
              <p>Now <strong>YOU decide which AI tool is appropriate</strong>.</p>
              <p class="story-punchline mt-1" style="font-size: 1.05rem !important;">You have a real study problem. Choose: ChatGPT / Gemini / NotebookLM.</p>
            </div>

            <div class="bullet-list-editorial mb-3">
              <div class="bullet-item"><div class="bullet-icon bg-yellow">A</div><div class="bullet-text"><strong>“I don't understand a concept.”</strong></div></div>
              <div class="bullet-item"><div class="bullet-icon bg-cyan">B</div><div class="bullet-text"><strong>“I need to practise questions.”</strong></div></div>
              <div class="bullet-item"><div class="bullet-icon bg-pink">C</div><div class="bullet-text"><strong>“I want feedback on my answer.”</strong></div></div>
              <div class="bullet-item"><div class="bullet-icon bg-green">D</div><div class="bullet-text"><strong>“I need to revise my textbook material.”</strong></div></div>
            </div>

            <div class="box-bad mb-3">
              <span class="box-tag tag-red">⚠️ MANDATORY LAB RULE:</span>
              <p class="box-note" style="color: #BE123C; font-weight: 700;">You are NOT allowed to simply copy an AI answer! You must: ASK &rarr; THINK &rarr; ANSWER &rarr; CHECK.</p>
            </div>

            <div class="lab-submit-card">
              <h4 class="submit-card-title">📝 Final Boss Submission</h4>
              <div class="form-group mt-2">
                <label>1. My study problem:</label>
                <input type="text" id="m5_problem" class="form-input" placeholder="e.g. Understanding Series and Parallel circuit calculation">
              </div>
              <div class="form-group mt-2">
                <label>2. AI tool I chose:</label>
                <div class="pills-row" id="m5_toolSelector">
                  <button type="button" class="pill active" onclick="setSubPill(this, 'm5_toolSelector', 'ChatGPT')">ChatGPT</button>
                  <button type="button" class="pill" onclick="setSubPill(this, 'm5_toolSelector', 'Gemini')">Gemini</button>
                  <button type="button" class="pill" onclick="setSubPill(this, 'm5_toolSelector', 'NotebookLM')">NotebookLM</button>
                </div>
              </div>
              <div class="form-group mt-2">
                <label>3. Why I chose it:</label>
                <textarea id="m5_why" class="form-textarea" rows="2" placeholder="e.g. I chose NotebookLM because I wanted to stay strictly within my textbook's syllabus..."></textarea>
              </div>
            </div>

            <div class="screen-action-row mt-3">
              <button type="button" class="btn btn-outline" onclick="prevLabMission()">&larr; Back</button>
              <button type="button" class="btn btn-primary" onclick="nextLabMission()">Proceed to Final Submission &rarr;</button>
            </div>
          </div>
        </div>

        <!-- SCREEN 6: FINAL SUBMISSION & CERTIFICATE -->
        <div class="lab-card-screen" data-step="6">
          <div class="lab-screen-content">
            <div class="panel-header-strip">
              <span class="panel-tag tag-green">PRACTICAL COMPLETE &bull; 60 MINUTES</span>
            </div>
            <h2 class="mission-title">FINAL SUBMISSION &bull; CERTIFICATION</h2>

            <div class="rule-of-the-lab-banner mb-3" style="background: #0B132B; color: #FFF; border-radius: 12px; padding: 1.25rem 1.5rem; text-align: center;">
              <div style="font-size: 0.85rem; font-weight: 800; color: #94A3B8; letter-spacing: 0.08em;">THE RULE OF THE LAB</div>
              <div style="font-size: 1.15rem; color: #EF4444; font-weight: 800; margin-top: 0.35rem;">❌ ASK &rarr; COPY &rarr; FORGET</div>
              <div style="font-size: 1.3rem; color: #22C55E; font-weight: 900; margin-top: 0.25rem;">✅ ASK &rarr; THINK &rarr; TRY &rarr; CHECK &rarr; IMPROVE</div>
              <p style="font-size: 1.1rem; font-weight: 800; color: #FFDE59; margin: 0.75rem 0 0 0;">YOU DON'T WIN BY GETTING THE ANSWER. YOU WIN BY UNDERSTANDING IT.</p>
            </div>

            <form id="finalSubmissionForm" onsubmit="event.preventDefault(); submitFinalLab();">
              <div class="form-grid-editorial">
                <div class="form-group">
                  <label>1. My study problem</label>
                  <input type="text" id="final_problem" class="form-input" placeholder="Your study problem">
                </div>
                <div class="form-group">
                  <label>2. AI tool I chose</label>
                  <input type="text" id="final_tool" class="form-input" placeholder="ChatGPT / Gemini / NotebookLM">
                </div>
                <div class="form-group full-width">
                  <label>3. Why I chose it</label>
                  <input type="text" id="final_why" class="form-input" placeholder="Reason for selecting this tool">
                </div>
                <div class="form-group full-width">
                  <label>4. One thing AI helped me understand</label>
                  <textarea id="final_understood" class="form-textarea" rows="2" placeholder="What key scientific concept clicked?"></textarea>
                </div>
                <div class="form-group full-width">
                  <label>5. One thing I still need to revise</label>
                  <textarea id="final_revise" class="form-textarea" rows="2" placeholder="What should you check in your textbook tonight?"></textarea>
                </div>
                <div class="form-group">
                  <label>6. My confidence BEFORE the lab (1 to 5):</label>
                  <div class="pills-row" id="final_confBefore">
                    <button type="button" class="pill" onclick="setSubPill(this, 'final_confBefore', '1')">1</button>
                    <button type="button" class="pill active" onclick="setSubPill(this, 'final_confBefore', '2')">2</button>
                    <button type="button" class="pill" onclick="setSubPill(this, 'final_confBefore', '3')">3</button>
                    <button type="button" class="pill" onclick="setSubPill(this, 'final_confBefore', '4')">4</button>
                    <button type="button" class="pill" onclick="setSubPill(this, 'final_confBefore', '5')">5</button>
                  </div>
                </div>
                <div class="form-group">
                  <label>7. My confidence AFTER the lab (1 to 5):</label>
                  <div class="pills-row" id="final_confAfter">
                    <button type="button" class="pill" onclick="setSubPill(this, 'final_confAfter', '1')">1</button>
                    <button type="button" class="pill" onclick="setSubPill(this, 'final_confAfter', '2')">2</button>
                    <button type="button" class="pill" onclick="setSubPill(this, 'final_confAfter', '3')">3</button>
                    <button type="button" class="pill" onclick="setSubPill(this, 'final_confAfter', '4')">4</button>
                    <button type="button" class="pill active" onclick="setSubPill(this, 'final_confAfter', '5')">5 🌟</button>
                  </div>
                </div>
              </div>

              <div class="screen-action-row mt-4">
                <button type="button" class="btn btn-outline" onclick="prevLabMission()">&larr; Back</button>
                <button type="submit" class="btn btn-primary btn-lg" style="background: #22C55E; color: #000; border: none; font-weight: 900;">🏆 Complete Practical &amp; Generate Certificate</button>
              </div>
            </form>
          </div>
        </div>

      </div>
    </div>
'''

updated_html = html[:idx_start] + new_lab_html + html[idx_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(updated_html)

print("Successfully replaced labContainer in index.html!")

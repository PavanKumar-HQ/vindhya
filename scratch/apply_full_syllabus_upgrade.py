#!/usr/bin/env python3
"""
Update index.html and app.js with the complete 6 Core Skills Curriculum and 7-Part Teaching Architecture.
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# ---------------------------------------------------------------------------
# 1. Update Slide 5 (data-index="5"): 6-SKILL SYLLABUS TABLE & 6 USEFUL JOBS
# ---------------------------------------------------------------------------
old_slide5_left = """            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-lime">MODULE 2 &bull; PRACTICAL VALUE</span>
              <span class="brutal-stamp stamp-tilt">NO BUZZWORDS</span>
              <span class="brutal-sticker sticker-yellow">100% BOARD SYLLABUS</span>
            </div>
            <h2 class="poster-hero-heading">SO WHAT CAN AI <mark class="poster-highlight">ACTUALLY DO FOR ME?</mark></h2>
            <p class="slide-hero-sub text-center">Forget generating generic poems. Here is the student superpower stack:</p>
            <div class="six-grid-editorial mt-2">
              <div class="sg-item"><span class="sg-num sg-yellow">01</span><strong>UNDERSTAND</strong> Dissect dense textbook sentences until click</div>
              <div class="sg-item"><span class="sg-num sg-cyan">02</span><strong>SIMPLIFY</strong> Turn abstract formulas into cricket analogies</div>
              <div class="sg-item"><span class="sg-num sg-lime">03</span><strong>EXPLORE</strong> Discover 'Why does this happen in real life?'</div>
              <div class="sg-item"><span class="sg-num sg-orange">04</span><strong>PRACTISE</strong> Command AI to quiz you, not give answers</div>
              <div class="sg-item"><span class="sg-num sg-pink">05</span><strong>CHECK</strong> Audit your hand-written answers for missing marks</div>
              <div class="sg-item"><span class="sg-num sg-purple">06</span><strong>REVISE</strong> Hunt down sneaky memory gaps before finals</div>
            </div>"""

new_slide5_left = """            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-lime">WORKSHOP SYLLABUS</span>
              <span class="brutal-stamp stamp-tilt">6 CORE SKILLS</span>
              <span class="brutal-sticker sticker-yellow">KARNATAKA BOARD</span>
            </div>
            <h2 class="poster-hero-heading" style="font-size: 1.55rem;">WHAT YOU WILL ACTUALLY LEARN TODAY</h2>
            <div class="skills-syllabus-table-wrap mt-2">
              <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem; text-align: left;">
                <thead>
                  <tr style="border-bottom: 2px solid var(--bx-navy-border); color: var(--text-muted); font-family: var(--font-display);">
                    <th style="padding: 0.4rem 0.6rem;">SKILL</th>
                    <th style="padding: 0.4rem 0.6rem;">WHAT WE TEACH YOU</th>
                    <th style="padding: 0.4rem 0.6rem;">TOOL</th>
                  </tr>
                </thead>
                <tbody style="color: #cbd5e1;">
                  <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
                    <td style="padding: 0.45rem 0.6rem; font-weight: 800; color: var(--bx-cyan);">1. UNDERSTAND</td>
                    <td style="padding: 0.45rem 0.6rem;">How to make AI explain a difficult concept at your exact level</td>
                    <td style="padding: 0.45rem 0.6rem; font-family: var(--font-mono); font-size: 0.78rem; color: #fff;">ChatGPT / Gemini</td>
                  </tr>
                  <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
                    <td style="padding: 0.45rem 0.6rem; font-weight: 800; color: var(--bx-emerald);">2. ASK</td>
                    <td style="padding: 0.45rem 0.6rem;">How to give AI useful context, constraints & instructions</td>
                    <td style="padding: 0.45rem 0.6rem; font-family: var(--font-mono); font-size: 0.78rem; color: #fff;">ChatGPT / Gemini</td>
                  </tr>
                  <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
                    <td style="padding: 0.45rem 0.6rem; font-weight: 800; color: var(--bx-amber);">3. STUDY</td>
                    <td style="padding: 0.45rem 0.6rem;">How to turn a chapter into concepts, examples and explanations</td>
                    <td style="padding: 0.45rem 0.6rem; font-family: var(--font-mono); font-size: 0.78rem; color: #fff;">ChatGPT / Gemini</td>
                  </tr>
                  <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
                    <td style="padding: 0.45rem 0.6rem; font-weight: 800; color: var(--bx-rose);">4. PRACTISE</td>
                    <td style="padding: 0.45rem 0.6rem;">How to make AI generate exam questions and conduct a quiz</td>
                    <td style="padding: 0.45rem 0.6rem; font-family: var(--font-mono); font-size: 0.78rem; color: #fff;">ChatGPT / Gemini</td>
                  </tr>
                  <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
                    <td style="padding: 0.45rem 0.6rem; font-weight: 800; color: #a78bfa;">5. CHECK</td>
                    <td style="padding: 0.45rem 0.6rem;">How to submit YOUR OWN answer and get examiner feedback</td>
                    <td style="padding: 0.45rem 0.6rem; font-family: var(--font-mono); font-size: 0.78rem; color: #fff;">ChatGPT / Gemini</td>
                  </tr>
                  <tr>
                    <td style="padding: 0.45rem 0.6rem; font-weight: 800; color: var(--bx-cobalt);">6. YOUR MATERIAL</td>
                    <td style="padding: 0.45rem 0.6rem;">How to upload your textbook/notes/PDF to NotebookLM & study</td>
                    <td style="padding: 0.45rem 0.6rem; font-family: var(--font-mono); font-size: 0.78rem; color: #fff;">NotebookLM</td>
                  </tr>
                </tbody>
              </table>
            </div>"""

if old_slide5_left in html:
    html = html.replace(old_slide5_left, new_slide5_left)
    print("Replaced Slide 5 Left Panel with 6-Skill Syllabus Table!")
else:
    print("WARNING: old_slide5_left not matched exactly.")

# Right panel of Slide 5:
old_slide5_right = """            <span class="slide-eyebrow">THE STUDENT TOOLBOX</span>
            <h2 class="slide-heading-standard">AI HAS SIX USEFUL JOBS:</h2>
            <div class="six-grid-editorial mt-2">
              <div class="sg-item"><strong>01. UNDERSTAND</strong> Break down concepts</div>
              <div class="sg-item"><strong>02. SIMPLIFY</strong> Plain language & analogies</div>
              <div class="sg-item"><strong>03. EXPLORE</strong> Why? How? Real life?</div>
              <div class="sg-item"><strong>04. PRACTISE</strong> Questions, not answers</div>
              <div class="sg-item"><strong>05. CHECK</strong> Feedback & hints</div>
              <div class="sg-item"><strong>06. REVISE</strong> Spot memory gaps</div>
            </div>"""

new_slide5_right = """            <span class="slide-eyebrow">PART 1 &bull; 0–15 MIN &bull; THE MENTAL SHIFT</span>
            <h2 class="slide-heading-standard">AI IS NOT JUST AN ANSWER GENERATOR</h2>
            <p class="slide-statement mb-2">Don't use AI to write homework. Use it as your active study partner across 6 roles:</p>
            <div class="six-grid-editorial mt-2">
              <div class="sg-item"><strong style="color: var(--bx-cyan);">01. EXPLAINER</strong> Dissects dense textbook sentences until clear</div>
              <div class="sg-item"><strong style="color: var(--bx-emerald);">02. TUTOR</strong> Guides your reasoning step-by-step</div>
              <div class="sg-item"><strong style="color: var(--bx-amber);">03. QUESTION GENERATOR</strong> Creates 2-mark & 3-mark board questions</div>
              <div class="sg-item"><strong style="color: var(--bx-rose);">04. QUIZ MASTER</strong> Tests you one question at a time</div>
              <div class="sg-item"><strong style="color: #a78bfa;">05. ANSWER CHECKER</strong> Audits your attempt for missing keywords</div>
              <div class="sg-item"><strong style="color: var(--bx-cobalt);">06. REVISION ASSISTANT</strong> Summarizes key definitions and formulas</div>
            </div>
            <div class="slide-bottom-note mt-2">💡 They don't need definitions of AI. They need: <em>“Here are 6 ways to use AI while studying.”</em></div>"""

if old_slide5_right in html:
    html = html.replace(old_slide5_right, new_slide5_right)
    print("Replaced Slide 5 Right Panel with 6 Roles!")
else:
    print("WARNING: old_slide5_right not matched.")

# ---------------------------------------------------------------------------
# 2. Update Slide 6 (data-index="6"): PART 2 — CHATGPT AS PERSONAL TUTOR: SKILL 1
# ---------------------------------------------------------------------------
old_slide6 = """        <!-- MERGED SLIDE 07: JOB 01: UNDERSTAND &bull; JOB 02: SIMPLIFY -->
        <div class="carousel-slide" data-index="6" data-section="10–20 MIN • MODULE 2" data-title="JOB 01: UNDERSTAND &bull; JOB 02: SIMPLIFY">
          <div class="merged-slide-container">
            <div class="merged-slide-header">
              <div class="m-badge-group">
                <span class="m-badge badge-gradient">10–20 MIN • MODULE 2</span>
                <span class="m-badge badge-navy">PART 07 OF 36</span>
              </div>
              <h2 class="m-slide-title">JOB 01: UNDERSTAND <span class="title-sep">&bull;</span> JOB 02: SIMPLIFY</h2>
            </div>
            
            <div class="merged-slide-grid">
              <div class="m-panel panel-left">
                <div class="slide-content-box">
            <span class="slide-eyebrow">JOB 01</span>
            <h2 class="slide-heading-standard">“I DON'T UNDERSTAND THIS.”</h2>
            <div class="bullet-list-editorial">
              <div class="bullet-item">• Explain step-by-step</div>
              <div class="bullet-item">• Break down complex theorems</div>
              <div class="bullet-item">• Dissect dense textbook sentences</div>
              <div class="bullet-item">• Provide the intuition before the formula</div>
            </div>
          </div>
              </div>
              <div class="m-panel panel-right">
                <div class="slide-content-box">
            <span class="slide-eyebrow">JOB 02</span>
            <h2 class="slide-heading-standard">“EXPLAIN IT DIFFERENTLY.”</h2>
            <p class="slide-statement">Instead of dense scientific words... ask for everyday analogies.</p>
            <div class="prompt-box-editorial mt-2">
              <code>“Explain this without difficult words, using a cricket example.”</code>
            </div>
            <div class="slide-bottom-note">Ask: What would you ask AI if the first explanation didn't make sense?</div>
          </div>
              </div>
            </div>
          </div>
        </div>"""

new_slide6 = """        <!-- MERGED SLIDE 07: CHATGPT AS PERSONAL TUTOR &bull; SKILL 1: ASK TO EXPLAIN -->
        <div class="carousel-slide" data-index="6" data-section="15–40 MIN • PART 2" data-title="CHATGPT AS PERSONAL TUTOR &bull; SKILL 1: ASK TO EXPLAIN">
          <div class="merged-slide-container">
            <div class="merged-slide-header">
              <div class="m-badge-group">
                <span class="m-badge badge-gradient">15–40 MIN • PART 2</span>
                <span class="m-badge badge-navy">PART 07 OF 36</span>
              </div>
              <h2 class="m-slide-title">CHATGPT AS PERSONAL TUTOR <span class="title-sep">&bull;</span> SKILL 1: ASK TO EXPLAIN</h2>
            </div>
            
            <div class="merged-slide-grid">
              <div class="m-panel panel-left">
                <div class="slide-content-box">
            <span class="slide-eyebrow">SKILL 1 • ASK TO EXPLAIN</span>
            <h2 class="slide-heading-standard">BAD PROMPT VS BETTER PROMPT:</h2>
            <div class="poster-contrast-grid mt-2">
              <div class="contrast-col col-bad">
                <div class="contrast-header">❌ VAGUE & LAZY</div>
                <p class="contrast-body" style="font-size: 1.15rem; font-weight: 700; color: #f43f5e;">“Explain electricity.”</p>
                <div class="contrast-tag tag-bad">Result: College-level wall of text. 0% understanding.</div>
              </div>
              <div class="contrast-col col-good">
                <div class="contrast-header">⚡ FOCUSED & CONTEXTUAL</div>
                <p class="contrast-body" style="font-size: 0.95rem; font-weight: 600; color: #10b981;">“I'm a Class 10 Karnataka State Board student. Explain electric current in simple language using an everyday example.”</p>
                <div class="contrast-tag tag-good">Result: Crystal-clear mental model tailored to your exam!</div>
              </div>
            </div>
          </div>
              </div>
              <div class="m-panel panel-right">
                <div class="poster-slide-card poster-cyan">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-pink">TEACHING FORMULA</span>
              <span class="brutal-stamp">THE 4 ANCHORS</span>
            </div>
            <h2 class="poster-hero-heading" style="font-size: 1.45rem;">ALWAYS ADD CONTEXT TO CHATGPT</h2>
            <div class="four-pill-grid mt-2">
              <div class="fp-card fp-pink">
                <span class="fp-num">WHO AM I?</span>
                <strong>Class 10 Student</strong>
                <p>Sets the cognitive level</p>
              </div>
              <div class="fp-card fp-yellow">
                <span class="fp-num">WHAT DO I WANT?</span>
                <strong>Explain Electric Current</strong>
                <p>Target concept</p>
              </div>
              <div class="fp-card fp-lime">
                <span class="fp-num">ADD THE LEVEL</span>
                <strong>Simple Language</strong>
                <p>No unnecessary jargon</p>
              </div>
              <div class="fp-card fp-white">
                <span class="fp-num">ADD THE FORMAT</span>
                <strong>Everyday Analogy</strong>
                <p>Water flowing in pipes</p>
              </div>
            </div>
          </div>
              </div>
            </div>
          </div>
        </div>"""

if old_slide6 in html:
    html = html.replace(old_slide6, new_slide6)
    print("Replaced Slide 6 with ChatGPT Skill 1: Ask to Explain + 4 Anchors!")
else:
    print("WARNING: old_slide6 not matched.")

# ---------------------------------------------------------------------------
# 3. Update Slide 7 (data-index="7"): SKILL 2: ASK FOLLOW-UP QUESTIONS (THE LEARNING CONVERSATION)
# ---------------------------------------------------------------------------
old_slide7 = """        <!-- MERGED SLIDE 08: JOB 03: EXPLORE &bull; JOB 04: PRACTISE -->
        <div class="carousel-slide" data-index="7" data-section="10–20 MIN • MODULE 2" data-title="JOB 03: EXPLORE &bull; JOB 04: PRACTISE">
          <div class="merged-slide-container">
            <div class="merged-slide-header">
              <div class="m-badge-group">
                <span class="m-badge badge-gradient">10–20 MIN • MODULE 2</span>
                <span class="m-badge badge-navy">PART 08 OF 36</span>
              </div>
              <h2 class="m-slide-title">JOB 03: EXPLORE <span class="title-sep">&bull;</span> JOB 04: PRACTISE</h2>
            </div>
            
            <div class="merged-slide-grid">
              <div class="m-panel panel-left">
                <div class="slide-content-box">
            <span class="slide-eyebrow">JOB 03</span>
            <h2 class="slide-heading-standard">DON'T STOP AT “WHAT?”</h2>
            <div class="comparison-cards-editorial mt-2">
              <div class="comp-box">
                <span class="comp-who">BORING QUESTION</span>
                <p class="comp-quote">“What is friction?”</p>
                <span class="comp-result">Abstract textbook definition.</span>
              </div>
              <div class="comp-box highlight">
                <span class="comp-who">EXPLORATION QUESTION</span>
                <p class="comp-quote">“Why do cricket players wear spikes, and why do bowlers shine one side of the ball?”</p>
                <span class="comp-result">Concept has a vivid reason to exist!</span>
              </div>
            </div>
          </div>
              </div>
              <div class="m-panel panel-right">
                <div class="slide-content-box center-aligned">
            <span class="slide-eyebrow">JOB 04</span>
            <h2 class="slide-title-large">
              DON'T ASK AI FOR THE ANSWER.<br>
              <span class="text-highlight">ASK FOR A QUESTION.</span>
            </h2>
            <div class="flow-sequence-box mt-3" style="max-width: 650px; margin: 1.5rem auto;">
              <div class="seq-step">AI</div>
              <div class="seq-arr">→</div>
              <div class="seq-step">QUESTION</div>
              <div class="seq-arr">→</div>
              <div class="seq-step highlight">YOU</div>
              <div class="seq-arr">→</div>
              <div class="seq-step">ANSWER</div>
            </div>
            <p class="slide-quote-sub">Which one makes your brain work? The question!</p>
          </div>
              </div>
            </div>
          </div>
        </div>"""

new_slide7 = """        <!-- MERGED SLIDE 08: SKILL 2: ASK FOLLOW-UP QUESTIONS &bull; THE LEARNING CONVERSATION -->
        <div class="carousel-slide" data-index="7" data-section="15–40 MIN • PART 2" data-title="SKILL 2: ASK FOLLOW-UP QUESTIONS &bull; THE LEARNING CONVERSATION">
          <div class="merged-slide-container">
            <div class="merged-slide-header">
              <div class="m-badge-group">
                <span class="m-badge badge-gradient">15–40 MIN • PART 2</span>
                <span class="m-badge badge-navy">PART 08 OF 36</span>
              </div>
              <h2 class="m-slide-title">SKILL 2: ASK FOLLOW-UP QUESTIONS <span class="title-sep">&bull;</span> THE LEARNING CONVERSATION</h2>
            </div>
            
            <div class="merged-slide-grid">
              <div class="m-panel panel-left">
                <div class="slide-content-box">
            <span class="slide-eyebrow">CRITICAL MISTAKE TO AVOID</span>
            <h2 class="slide-heading-standard">DON'T START A NEW CHAT FOR EVERY QUESTION!</h2>
            <p class="slide-statement mb-2">Have a real back-and-forth dialogue with AI:</p>
            <div class="bullet-list-editorial">
              <div class="bullet-item"><strong>1. Ask initial concept:</strong> <code>“Explain Newton's First Law.”</code></div>
              <div class="bullet-item"><strong>2. Clarify confusion:</strong> <code>“I still don't understand inertia. Explain that part again.”</code></div>
              <div class="bullet-item"><strong>3. Request example:</strong> <code>“Give me a real-life example.”</code></div>
              <div class="bullet-item"><strong>4. Ground in passion:</strong> <code>“Now explain it using cricket.”</code></div>
              <div class="bullet-item highlight"><strong>5. Diagnostic check:</strong> <code>“Ask me one question to check whether I understood.”</code></div>
            </div>
            <div class="slide-bottom-note mt-2">This is 10x more valuable than memorizing 20 complex prompt templates!</div>
          </div>
              </div>
              <div class="m-panel panel-right">
                <div class="slide-content-box center-aligned">
            <span class="slide-eyebrow">SKILL 4 PREVIEW &bull; THE RETRIEVAL LOOP</span>
            <h2 class="slide-title-large">
              DON'T ASK AI FOR THE ANSWER.<br>
              <span class="text-highlight">ASK FOR A QUESTION.</span>
            </h2>
            <div class="flow-sequence-box mt-3" style="max-width: 650px; margin: 1.5rem auto;">
              <div class="seq-step">AI</div>
              <div class="seq-arr">→</div>
              <div class="seq-step">QUESTION</div>
              <div class="seq-arr">→</div>
              <div class="seq-step highlight">YOU</div>
              <div class="seq-arr">→</div>
              <div class="seq-step">ANSWER</div>
            </div>
            <p class="slide-quote-sub">Which one builds memory for the board exam? The question you answer yourself!</p>
          </div>
              </div>
            </div>
          </div>
        </div>"""

if old_slide7 in html:
    html = html.replace(old_slide7, new_slide7)
    print("Replaced Slide 7 with Skill 2: The Learning Conversation!")
else:
    print("WARNING: old_slide7 not matched.")

# ---------------------------------------------------------------------------
# 4. Update Slide 12 (data-index="12"): PART 4 — GEMINI: COMPARE HEAD-TO-HEAD
# ---------------------------------------------------------------------------
old_slide12 = """        <!-- MERGED SLIDE 13: SAME QUESTION, DIFFERENT AI &bull; DON'T ASK THIS -->
        <div class="carousel-slide" data-index="12" data-section="20–35 MIN • MODULE 3" data-title="SAME QUESTION, DIFFERENT AI &bull; DON'T ASK THIS">
          <div class="merged-slide-container">
            <div class="merged-slide-header">
              <div class="m-badge-group">
                <span class="m-badge badge-gradient">20–35 MIN • MODULE 3</span>
                <span class="m-badge badge-navy">PART 13 OF 36</span>
              </div>
              <h2 class="m-slide-title">SAME QUESTION, DIFFERENT AI <span class="title-sep">&bull;</span> DON'T ASK THIS</h2>
            </div>
            
            <div class="merged-slide-grid">
              <div class="m-panel panel-left">
                <div class="slide-content-box">
            <span class="slide-eyebrow">LIVE HEAD-TO-HEAD COMPARISON</span>
            <h2 class="slide-heading-standard">SAME QUESTION &bull; TWO DIFFERENT AIS</h2>
            <div class="prompt-box-editorial" style="max-width: 720px; text-align: left;">
              <code>“Explain photosynthesis to a Class 9 Karnataka Board student using a simple kitchen recipe analogy.”</code>
            </div>
            <h3 class="vote-prompt mt-2">Which explanation made more sense to YOU?</h3>
            <div class="poll-options mt-2">
              <div class="vote-option" data-choice="chatgpt"><strong>A &bull; CHATGPT:</strong> More structured step-by-step</div>
              <div class="vote-option" data-choice="gemini"><strong>B &bull; GEMINI:</strong> More conversational & visual</div>
            </div>
            <div class="slide-bottom-note">Different brains like different explanations. That's why you use BOTH!</div>
          </div>
              </div>
              <div class="m-panel panel-right">
                <div class="poster-slide-card poster-pink">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-yellow">THE DANGER ZONE</span>
              <span class="brutal-stamp stamp-tilt">DO NOT DO THIS</span>
            </div>
            <h2 class="poster-hero-heading">WHAT YOU SHOULD <mark class="poster-highlight">NEVER</mark> ASK AI:</h2>
            <div class="three-tools-deck mt-2">
              <div class="deck-tool" style="background: #fff;">
                <span class="tool-badge-pill pill-pink">FATAL ERROR 01</span>
                <h3>“GIVE ME HOMEWORK ANSWERS”</h3>
                <p>AI does the thinking. You get 0 marks in the real exam.</p>
              </div>
              <div class="deck-tool" style="background: #fff;">
                <span class="tool-badge-pill pill-pink">FATAL ERROR 02</span>
                <h3>“WRITE MY LAB RECORD”</h3>
                <p>Copy-pasting formulas without understanding the physical variables.</p>
              </div>
              <div class="deck-tool" style="background: #fff;">
                <span class="tool-badge-pill pill-pink">FATAL ERROR 03</span>
                <h3>“TELL ME WHAT WILL COME IN EXAM”</h3>
                <p>AI cannot predict board question papers. Only your syllabus matters.</p>
              </div>
            </div>
          </div>
              </div>
            </div>
          </div>
        </div>"""

new_slide12 = """        <!-- MERGED SLIDE 13: PART 4: GEMINI &bull; EVALUATE, DON'T BLINDLY TRUST -->
        <div class="carousel-slide" data-index="12" data-section="65–80 MIN • PART 4" data-title="GEMINI &bull; EVALUATE, DON'T BLINDLY TRUST">
          <div class="merged-slide-container">
            <div class="merged-slide-header">
              <div class="m-badge-group">
                <span class="m-badge badge-gradient">65–80 MIN • PART 4</span>
                <span class="m-badge badge-navy">PART 13 OF 36</span>
              </div>
              <h2 class="m-slide-title">GEMINI &bull; EVALUATE, DON'T BLINDLY TRUST</h2>
            </div>
            
            <div class="merged-slide-grid">
              <div class="m-panel panel-left">
                <div class="slide-content-box">
            <span class="slide-eyebrow">PART 4 &bull; 65–80 MIN &bull; HEAD-TO-HEAD</span>
            <h2 class="slide-heading-standard">SAME PROBLEM &bull; TWO DIFFERENT AIS</h2>
            <div class="prompt-box-editorial" style="max-width: 720px; text-align: left;">
              <code>“I'm a Class 10 student preparing for my Science exam. Explain electric current in simple language using an everyday example.”</code>
            </div>
            <h3 class="vote-prompt mt-2">Compare ChatGPT vs Gemini Live:</h3>
            <div class="poll-options mt-2">
              <div class="vote-option" data-choice="chatgpt"><strong>A &bull; CHATGPT:</strong> Explains via fluid water pipe analogy & electron flow</div>
              <div class="vote-option" data-choice="gemini"><strong>B &bull; GEMINI:</strong> Connects to circuit diagrams, SI units & real components</div>
            </div>
            <div class="slide-bottom-note">The goal isn't 'which is better'. The goal is: <strong>evaluate responses rather than blindly trusting whichever tool you opened first!</strong></div>
          </div>
              </div>
              <div class="m-panel panel-right">
                <div class="poster-slide-card poster-pink">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-yellow">THE DANGER ZONE</span>
              <span class="brutal-stamp stamp-tilt">DO NOT DO THIS</span>
            </div>
            <h2 class="poster-hero-heading">WHAT YOU SHOULD <mark class="poster-highlight">NEVER</mark> ASK AI:</h2>
            <div class="three-tools-deck mt-2">
              <div class="deck-tool" style="background: #fff;">
                <span class="tool-badge-pill pill-pink">FATAL ERROR 01</span>
                <h3>“GIVE ME HOMEWORK ANSWERS”</h3>
                <p>AI does the thinking. You get 0 marks in the real exam.</p>
              </div>
              <div class="deck-tool" style="background: #fff;">
                <span class="tool-badge-pill pill-pink">FATAL ERROR 02</span>
                <h3>“WRITE MY LAB RECORD”</h3>
                <p>Copy-pasting formulas without understanding the physical variables.</p>
              </div>
              <div class="deck-tool" style="background: #fff;">
                <span class="tool-badge-pill pill-pink">FATAL ERROR 03</span>
                <h3>“TELL ME WHAT WILL COME IN EXAM”</h3>
                <p>AI cannot predict board question papers. Only your syllabus matters.</p>
              </div>
            </div>
          </div>
              </div>
            </div>
          </div>
        </div>"""

if old_slide12 in html:
    html = html.replace(old_slide12, new_slide12)
    print("Replaced Slide 12 with Gemini Part 4 Head-to-Head Evaluation!")
else:
    print("WARNING: old_slide12 not matched.")

# ---------------------------------------------------------------------------
# 5. Update Slide 31 (data-index="31"): CUT "GAME: HUMAN OR AI?", REPLACE WITH PART 7 RESPONSIBLE USE
# ---------------------------------------------------------------------------
old_slide31 = """        <!-- MERGED SLIDE 32: CATCH THE AI &bull; GAME: HUMAN OR AI? -->
        <div class="carousel-slide" data-index="31" data-section="100–110 MIN • MODULE 8" data-title="CATCH THE AI &bull; GAME: HUMAN OR AI?">
          <div class="merged-slide-container">
            <div class="merged-slide-header">
              <div class="m-badge-group">
                <span class="m-badge badge-gradient">100–110 MIN • MODULE 8</span>
                <span class="m-badge badge-navy">PART 32 OF 36</span>
              </div>
              <h2 class="m-slide-title">CATCH THE AI <span class="title-sep">&bull;</span> GAME: HUMAN OR AI?</h2>
            </div>
            
            <div class="merged-slide-grid">
              <div class="m-panel panel-left">
                <div class="poster-slide-card poster-cyan">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-pink">DETECTIVE CHALLENGE</span>
              <span class="brutal-stamp stamp-tilt">SPOT THE BLUNDER</span>
            </div>
            <h2 class="poster-hero-heading">SPOT THE SCIENTIFIC ERROR ON SCREEN:</h2>
            <div class="prompt-box-editorial mt-2">
              <code>Q: “Do desert plants take up Carbon Dioxide during daytime?”<br>AI SAYS: “Yes! Desert plants open stomata at noon to take in CO2 for photosynthesis.”</code>
            </div>
            <div class="poster-contrast-grid mt-2">
              <div class="contrast-col col-bad">
                <div class="contrast-header">❌ THE ERROR</div>
                <p class="contrast-body">If desert plants open stomata at noon, they would lose all water through transpiration and die!</p>
              </div>
              <div class="contrast-col col-good">
                <div class="contrast-header">⚡ THE REAL BIOLOGY (PAGE 96)</div>
                <p class="contrast-body">Desert plants open stomata at <strong>NIGHT</strong> to absorb CO2 and store it as an intermediate!</p>
              </div>
            </div>
          </div>
              </div>
              <div class="m-panel panel-right">
                <div class="poster-slide-card poster-yellow">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-pink">STAGE GAME</span>
              <span class="brutal-stamp">HUMAN OR AI?</span>
            </div>
            <h2 class="poster-hero-heading">READ THIS SENTENCE: HUMAN OR AI?</h2>
            <div class="prompt-box-editorial mt-2">
              <p style="font-size: 1.25rem; font-weight: 700; line-height: 1.6;">“The process by which autotrophic organisms take in substances from outside and convert them into stored forms of energy using sunlight and chlorophyll...”</p>
            </div>
            <div class="poster-contrast-grid mt-2">
              <div class="contrast-col col-white">
                <div class="contrast-header">ROOM VOTES: 80% SAY “AI!”</div>
                <p class="contrast-body">Because it sounds formal and robotic.</p>
              </div>
              <div class="contrast-col col-lime">
                <div class="contrast-header">THE BIG REVEAL! 🎉</div>
                <p class="contrast-body">It's from <strong>Page 95 of your official Karnataka State Board Science textbook!</strong></p>
              </div>
            </div>
          </div>
              </div>
            </div>
          </div>
        </div>"""

new_slide31 = """        <!-- MERGED SLIDE 32: CATCH THE AI &bull; PART 7: 5 RESPONSIBLE AI RULES -->
        <div class="carousel-slide" data-index="31" data-section="115–120 MIN • PART 7" data-title="CATCH THE AI &bull; PART 7: 5 RESPONSIBLE AI RULES">
          <div class="merged-slide-container">
            <div class="merged-slide-header">
              <div class="m-badge-group">
                <span class="m-badge badge-gradient">115–120 MIN • PART 7</span>
                <span class="m-badge badge-navy">PART 32 OF 36</span>
              </div>
              <h2 class="m-slide-title">CATCH THE AI <span class="title-sep">&bull;</span> PART 7: 5 RESPONSIBLE AI RULES</h2>
            </div>
            
            <div class="merged-slide-grid">
              <div class="m-panel panel-left">
                <div class="poster-slide-card poster-cyan">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-pink">DETECTIVE CHALLENGE</span>
              <span class="brutal-stamp stamp-tilt">SPOT THE BLUNDER</span>
            </div>
            <h2 class="poster-hero-heading">SPOT THE SCIENTIFIC ERROR ON SCREEN:</h2>
            <div class="prompt-box-editorial mt-2">
              <code>Q: “Do desert plants take up Carbon Dioxide during daytime?”<br>AI SAYS: “Yes! Desert plants open stomata at noon to take in CO2 for photosynthesis.”</code>
            </div>
            <div class="poster-contrast-grid mt-2">
              <div class="contrast-col col-bad">
                <div class="contrast-header">❌ THE ERROR</div>
                <p class="contrast-body">If desert plants open stomata at noon, they would lose all water through transpiration and die!</p>
              </div>
              <div class="contrast-col col-good">
                <div class="contrast-header">⚡ THE REAL BIOLOGY (PAGE 96)</div>
                <p class="contrast-body">Desert plants open stomata at <strong>NIGHT</strong> to absorb CO2 and store it as an intermediate!</p>
              </div>
            </div>
          </div>
              </div>
              <div class="m-panel panel-right">
                <div class="poster-slide-card poster-yellow">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-pink">PART 7 &bull; 115–120 MIN</span>
              <span class="brutal-stamp">5 RESPONSIBLE AI RULES</span>
            </div>
            <h2 class="poster-hero-heading" style="font-size: 1.35rem;">THE 5 RULES OF STUDYING WITH AI</h2>
            <div class="bullet-list-editorial mt-2">
              <div class="bullet-item"><strong style="color: var(--bx-rose);">1. AI CAN BE WRONG:</strong> It generates plausible text, not guaranteed ground truth.</div>
              <div class="bullet-item"><strong style="color: var(--bx-amber);">2. DON'T BLINDLY COPY:</strong> Copying creates zero synaptic retention for exam day.</div>
              <div class="bullet-item"><strong style="color: var(--bx-cyan);">3. VERIFY WITH TEXTBOOK:</strong> Always cross-check numbers, formulas & ray diagrams with your official board book.</div>
              <div class="bullet-item"><strong style="color: var(--bx-emerald);">4. ANSWER YOURSELF FIRST:</strong> Try answering before asking AI for hints. Effortful retrieval builds memory.</div>
              <div class="bullet-item highlight"><strong style="color: #a78bfa;">5. PRIVACY SHIELD:</strong> Never type passwords, OTPs, Aadhaar numbers, or personal secrets into AI prompts.</div>
            </div>
          </div>
              </div>
            </div>
          </div>
        </div>"""

if old_slide31 in html:
    html = html.replace(old_slide31, new_slide31)
    print("Replaced Slide 31 with Part 7: 5 Responsible AI Rules (cut Human or AI game)!")
else:
    print("WARNING: old_slide31 not matched.")

# ---------------------------------------------------------------------------
# 6. Update Slide 34 (data-index="34"): AUDITORIUM (I TEACH) -> LAB (YOU DO)
# ---------------------------------------------------------------------------
old_slide34_right = """            <span class="slide-eyebrow">ENOUGH WATCHING</span>
            <h2 class="slide-massive-quote">NOW IT'S YOUR TURN.</h2>
            <p class="slide-hero-sub">Enter the computer lab. Follow the 5 missions. Work in pairs.</p>
            <div class="slide-action-pill mt-3">👉 ENTER COMPUTER LAB NOW</div>"""

new_slide34_right = """            <span class="slide-eyebrow">THE WORKSHOP SHIFT</span>
            <h2 class="slide-massive-quote">AUDITORIUM: I TEACH.<br><span style="color: var(--bx-cyan);">LAB: YOU DO.</span></h2>
            <p class="slide-hero-sub">The auditorium taught the 6 skills. The computer lab is where you prove you can do them on your syllabus.</p>
            <div class="slide-action-pill mt-3">👉 COMMENCE 60-MINUTE COMPUTER LAB</div>"""

if old_slide34_right in html:
    html = html.replace(old_slide34_right, new_slide34_right)
    print("Replaced Slide 34 Right Panel with 'I TEACH -> YOU DO' distinction!")
else:
    print("WARNING: old_slide34_right not matched.")

# ---------------------------------------------------------------------------
# 7. Update Attention Architecture & Workshop Guide (#viewOverview)
# ---------------------------------------------------------------------------
old_overview_lead = """      <div class="section-lead">
        <span class="eyebrow">WORKSHOP ARCHITECTURE</span>
        <h1 class="section-title">120-Minute Attention Architecture</h1>
        <p class="section-text">
          No 20-minute lecture blocks. Hard rule: <strong>Every 7–10 minutes, the students must DO something</strong> (Raise hands, shout an answer, vote, guess, challenge AI, spot an error, come to the microphone).
        </p>
      </div>"""

new_overview_lead = """      <div class="section-lead">
        <span class="eyebrow">CURRICULUM ARCHITECTURE &bull; 6 SKILLS &bull; 7 TEACHING PARTS</span>
        <h1 class="section-title">Teaching Class 9 & 10 to Prepare for Board Exams</h1>
        <p class="section-text">
          The agenda is NOT to run a 2-hour AI entertainment show. <strong>The games, questions, and jokes are delivery mechanisms—the 6 AI study skills are the curriculum.</strong><br>
          Core principle: <strong>Auditorium (120 min) = I TEACH &bull; Computer Lab (60 min) = YOU DO.</strong>
        </p>
      </div>

      <!-- The 6 Core Skills Syllabus Table -->
      <div class="cheatsheet-card mb-4" style="background: var(--bx-navy); border: 2px solid var(--bx-cobalt); border-radius: 12px; padding: 1.5rem;">
        <h3 style="font-family: var(--font-display); font-size: 1.25rem; font-weight: 800; color: #fff; margin-bottom: 1rem;">
          🎯 THE 6 CORE AI EXAM PREPARATION SKILLS
        </h3>
        <table class="attention-table">
          <thead>
            <tr>
              <th>SKILL</th>
              <th>WHAT YOU TEACH THEM</th>
              <th>PRIMARY TOOL</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong style="color: var(--bx-cyan);">1. UNDERSTAND</strong></td>
              <td>How to make AI explain a difficult concept at their level</td>
              <td>ChatGPT / Gemini</td>
            </tr>
            <tr>
              <td><strong style="color: var(--bx-emerald);">2. ASK</strong></td>
              <td>How to give AI useful context and instructions</td>
              <td>ChatGPT / Gemini</td>
            </tr>
            <tr>
              <td><strong style="color: var(--bx-amber);">3. STUDY</strong></td>
              <td>How to turn a chapter into concepts, examples and explanations</td>
              <td>ChatGPT / Gemini</td>
            </tr>
            <tr>
              <td><strong style="color: var(--bx-rose);">4. PRACTISE</strong></td>
              <td>How to make AI generate exam-style questions and conduct a quiz</td>
              <td>ChatGPT / Gemini</td>
            </tr>
            <tr>
              <td><strong style="color: #a78bfa);">5. CHECK</strong></td>
              <td>How to submit <em>their own</em> answer and get feedback</td>
              <td>ChatGPT / Gemini</td>
            </tr>
            <tr>
              <td><strong style="color: var(--bx-cobalt);">6. STUDY YOUR MATERIAL</strong></td>
              <td>How to give their textbook/notes/PDF to NotebookLM and study from it</td>
              <td>NotebookLM</td>
            </tr>
          </tbody>
        </table>
      </div>"""

if old_overview_lead in html:
    html = html.replace(old_overview_lead, new_overview_lead)
    print("Updated Overview lead and added 6 Core Skills table!")
else:
    print("WARNING: old_overview_lead not matched.")

# Also update the table in #viewOverview to match the 7 Parts:
old_table_rows = """            <tr>
              <td><strong>0–3 min</strong></td>
              <td>Icebreaker</td>
              <td>Raise hands: "Be honest... who used AI to escape homework?" 😂</td>
            </tr>
            <tr>
              <td><strong>3–7 min</strong></td>
              <td>Student vote</td>
              <td>Shout A, B, C or D: "Which student are you?"</td>
            </tr>
            <tr>
              <td><strong>7–12 min</strong></td>
              <td>Story & Quote</td>
              <td>"AI won't replace students..." + Golden Rule choral call-and-response</td>
            </tr>
            <tr>
              <td><strong>12–18 min</strong></td>
              <td>Live AI demo</td>
              <td>AI vs You: "Explain why sky is blue" → "Now with cricket to 7-year-old"</td>
            </tr>
            <tr>
              <td><strong>18–22 min</strong></td>
              <td>Student interaction</td>
              <td>Mini challenge: Why does ice float? / Photosynthesis photolysis</td>
            </tr>
            <tr>
              <td><strong>22–30 min</strong></td>
              <td>ChatGPT</td>
              <td>Meet the interactive tutor ("Teach me")</td>
            </tr>
            <tr>
              <td><strong>30–35 min</strong></td>
              <td>Mini challenge</td>
              <td>Head-to-head same question on two AIs</td>
            </tr>
            <tr>
              <td><strong>35–43 min</strong></td>
              <td>Gemini</td>
              <td>Visual reasoning & diagrams exploration ("Help me explore")</td>
            </tr>
            <tr>
              <td><strong>43–48 min</strong></td>
              <td>Vote / game</td>
              <td>"Would you rather?": Read 20 pages vs Ask AI to quiz you</td>
            </tr>
            <tr>
              <td><strong>48–58 min</strong></td>
              <td>Exam workflow</td>
              <td>Board evaluator demo: Weak student answer → AI teacher grading</td>
            </tr>
            <tr>
              <td><strong>58–65 min</strong></td>
              <td>Prompting game</td>
              <td>Fix the terrible prompt: "Explain electricity" → Student to mic!</td>
            </tr>
            <tr>
              <td><strong>65–75 min</strong></td>
              <td>NotebookLM demo</td>
              <td>Upload actual Karnataka Board PDF → Grounded citations [1] [2]</td>
            </tr>
            <tr>
              <td><strong>75–82 min</strong></td>
              <td>Human vs AI</td>
              <td>Game: "Human or AI?" Shout it out! Fact-checking intro</td>
            </tr>
            <tr>
              <td><strong>82–90 min</strong></td>
              <td>Responsible AI</td>
              <td>"AI knows everything?" trap → STOP-CHECK-THINK protocol</td>
            </tr>
            <tr>
              <td><strong>90–100 min</strong></td>
              <td>Exam challenge</td>
              <td>"Beat the AI" competition: Spot the one deliberate AI mistake</td>
            </tr>
            <tr>
              <td><strong>100–110 min</strong></td>
              <td>Student questions</td>
              <td>Audience Q&A + 5-Part Formula review</td>
            </tr>
            <tr>
              <td><strong>110–120 min</strong></td>
              <td>Lab mission</td>
              <td>"Pick ONE chapter you hate. Yes. That one." → Enter Computer Lab</td>
            </tr>"""

new_table_rows = """            <tr>
              <td><strong>0–15 min</strong><br><span style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--bx-cyan);">PART 1</span></td>
              <td><strong>What AI Can Actually Do for Exam Prep</strong><br>AI is not an answer generator; 6 Study Roles</td>
              <td>Icebreaker raise hands ➔ Student persona shoutout ➔ 6 Roles demonstration</td>
            </tr>
            <tr>
              <td><strong>15–40 min</strong><br><span style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--bx-emerald);">PART 2</span></td>
              <td><strong>ChatGPT: Use It as Your Personal Tutor</strong><br>Skill 1: Ask to Explain + Context Anchors<br>Skill 2: Follow-up Questions (Learning Conversation)</td>
              <td>Bad prompt vs Better prompt ➔ Chaining questions (Newton ➔ Inertia ➔ Cricket ➔ Quiz) ➔ Students predict AI output</td>
            </tr>
            <tr>
              <td><strong>40–65 min</strong><br><span style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--bx-amber);">PART 3</span></td>
              <td><strong>ChatGPT: Exam Practice Partner</strong><br>Generate questions ➔ Answer yourself ➔ Check ➔ Improve</td>
              <td>30-Second Stage Countdown Timer ➔ Student to microphone ➔ Live Socratic AI Tutor Simulator</td>
            </tr>
            <tr>
              <td><strong>65–80 min</strong><br><span style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--bx-rose);">PART 4</span></td>
              <td><strong>Gemini: Don't Teach as "Another ChatGPT"</strong><br>Same problem to both tools; compare & evaluate</td>
              <td>Side-by-side comparison (Electric current) ➔ Audience voting on explanation clarity ➔ Visual ray diagrams & circuits</td>
            </tr>
            <tr>
              <td><strong>80–105 min</strong><br><span style="font-family: var(--font-mono); font-size: 0.72rem; color: #a78bfa);">PART 5</span></td>
              <td><strong>NotebookLM: Studying Your Actual Material</strong><br>Upload textbook/PDF ➔ Understand ➔ Revise ➔ Quiz</td>
              <td>Upload Karnataka Board chapter ➔ Workflows A–E: Concepts ➔ Difficult sections ➔ Revision ➔ Quiz me only from material</td>
            </tr>
            <tr>
              <td><strong>105–115 min</strong><br><span style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--bx-cobalt);">PART 6</span></td>
              <td><strong>Prompting in 10 Minutes</strong><br>WHO + WHAT + CONTEXT + HOW + RULE</td>
              <td>Rapid prompt overhaul: "Explain electricity" ➔ Production board command</td>
            </tr>
            <tr>
              <td><strong>115–120 min</strong><br><span style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--bx-emerald);">PART 7</span></td>
              <td><strong>Responsible AI & 60-Minute Lab Briefing</strong><br>5 Rules (AI can be wrong, verify, privacy)</td>
              <td>Auditorium: I TEACH ➔ Lab: YOU DO ➔ Briefing the 7 Hands-on Missions</td>
            </tr>"""

if old_table_rows in html:
    html = html.replace(old_table_rows, new_table_rows)
    print("Updated 120-minute table in #viewOverview to match the 7 Parts exactly!")
else:
    print("WARNING: old_table_rows not matched.")

# Write updated HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved updated index.html successfully!")

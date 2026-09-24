#!/usr/bin/env python3
"""
Enhance all plain slides in index.html with rich visual cards, Neo-Brutalist posters,
interactive voting grids, contrast pillars, and actionable visual diagrams.
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Dictionary of enhanced slide markup keyed by data-index
replacements = {}

# SLIDE 02 (Index 1): BE HONEST
replacements[1] = """        <!-- SLIDE 02: BE HONEST -->
        <div class="carousel-slide" data-index="1" data-section="00–10 MIN • MODULE 1" data-title="BE HONEST">
          <div class="poster-slide-card poster-yellow">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-pink">🚨 500 STUDENTS IN THIS HALL</span>
              <span class="brutal-stamp stamp-tilt">CONFESSION TIME</span>
              <span class="brutal-sticker sticker-cyan">CLASS 9 & 10</span>
            </div>
            <h2 class="poster-hero-heading">BE HONEST. 👀<br>HAVE YOU USED AI FOR HOMEWORK?</h2>
            <div class="poster-contrast-grid mt-2">
              <div class="contrast-col col-yellow">
                <div class="contrast-header">🙌 HANDS UP HIGH IF:</div>
                <p class="contrast-body">“You pasted a school question into ChatGPT or Gemini just to get it done fast!”</p>
                <div class="contrast-stat-tag stat-yellow">~85% OF STUDENTS IN THE ROOM</div>
              </div>
              <div class="contrast-col col-pink">
                <div class="contrast-header">🤔 KEEP HANDS UP IF:</div>
                <p class="contrast-body">“You actually UNDERSTOOD and could explain that exact answer right now on a blank paper!”</p>
                <div class="contrast-stat-tag stat-pink">DROPS TO LESS THAN 10%! 📉</div>
              </div>
            </div>
            <div class="poster-footer-strip mt-2">
              <span class="strip-icon">🎯</span> <strong>TODAY'S MISSION:</strong> We are not learning to escape homework. We are learning how to use AI to <strong>dominate board exams</strong>.
            </div>
          </div>
        </div>"""

# SLIDE 08 (Index 7): OUR RULE (The one user screenshotted!)
replacements[7] = """        <!-- SLIDE 08: OUR RULE -->
        <div class="carousel-slide" data-index="7" data-section="00–10 MIN • MODULE 1" data-title="OUR RULE">
          <div class="poster-slide-card poster-yellow">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-pink">⚡ THE #1 WORKSHOP LAW</span>
              <span class="brutal-stamp stamp-tilt">NON-NEGOTIABLE</span>
              <span class="brutal-sticker sticker-lime">BOARD EXAM SUCCESS</span>
            </div>
            <h2 class="poster-hero-heading">
              DON'T USE AI TO AVOID THINKING.<br>
              <mark class="poster-highlight">USE AI TO THINK BETTER.</mark>
            </h2>
            <div class="poster-contrast-grid mt-2">
              <div class="contrast-col col-bad">
                <div class="contrast-header">❌ THE LAZY COPY TRAP</div>
                <p class="contrast-body">“Hey ChatGPT, give me the 5-mark answer for Ohm's Law.”</p>
                <div class="contrast-tag tag-bad">Brain: 0% Effort &bull; Exam: FAILED</div>
              </div>
              <div class="contrast-col col-good">
                <div class="contrast-header">⚡ THE GENIUSPHERE METHOD</div>
                <p class="contrast-body">“Hey ChatGPT, test me on Ohm's Law. Give me a tricky situation and check my reasoning!”</p>
                <div class="contrast-tag tag-good">Brain: 100% Active &bull; Exam: TOP 1% SCORE</div>
              </div>
            </div>
            <div class="poster-footer-strip mt-2">
              <span class="strip-icon">💡</span> <strong>REALITY CHECK:</strong> In the board exam hall, you cannot bring ChatGPT. You only bring what is in your brain!
            </div>
          </div>
        </div>"""

# SLIDE 10 (Index 9): AI VS YOU
replacements[9] = """        <!-- SLIDE 10: AI VS YOU -->
        <div class="carousel-slide" data-index="9" data-section="00–10 MIN • MODULE 1" data-title="AI VS YOU">
          <div class="poster-slide-card poster-cyan">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-yellow">⏱️ 10-SECOND SPEED DRILL</span>
              <span class="brutal-stamp">HUMAN 🧠 VS AI 🤖</span>
            </div>
            <h2 class="poster-hero-heading">“WHY DOES ICE FLOAT ON WATER?”</h2>
            <div class="poster-contrast-grid mt-2">
              <div class="contrast-col col-white">
                <div class="contrast-header">🧠 YOUR TURN (10 SECONDS)</div>
                <p class="contrast-body">Formulate your explanation right now. What scientific keywords must appear?</p>
                <div class="contrast-tag tag-yellow">Density? Molecular lattice? Hydrogen bonds?</div>
              </div>
              <div class="contrast-col col-good">
                <div class="contrast-header">🤖 AI BENCHMARK ANSWER</div>
                <p class="contrast-body">“Water expands as it freezes due to hydrogen bonding creating an open hexagonal cage structure, making ice 9% less dense than liquid water.”</p>
                <div class="contrast-tag tag-good">Gold Standard Keywords Identified</div>
              </div>
            </div>
            <div class="poster-footer-strip mt-2">
              <span class="strip-icon">🔑</span> <strong>THE LESSON:</strong> AI didn't replace your thinking. It gave you an instant benchmark to compare your knowledge against!
            </div>
          </div>
        </div>"""

# SLIDE 11 (Index 10): WHAT CAN AI DO?
replacements[10] = """        <!-- SLIDE 11: WHAT CAN AI DO? -->
        <div class="carousel-slide" data-index="10" data-section="10–20 MIN • MODULE 2" data-title="WHAT CAN AI DO?">
          <div class="poster-slide-card poster-white">
            <div class="poster-badge-row">
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
            </div>
          </div>
        </div>"""

# SLIDE 18 (Index 17): JOB 06: REVISE
replacements[17] = """        <!-- SLIDE 18: JOB 06: REVISE -->
        <div class="carousel-slide" data-index="17" data-section="10–20 MIN • MODULE 2" data-title="JOB 06: REVISE">
          <div class="poster-slide-card poster-lime">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-yellow">JOB 06 &bull; ACTIVE REVISION</span>
              <span class="brutal-stamp stamp-tilt">GAP HUNTER</span>
            </div>
            <h2 class="poster-hero-heading">FIND THE GAP BEFORE THE EXAM DOES.</h2>
            <div class="poster-contrast-grid mt-2">
              <div class="contrast-col col-white">
                <div class="contrast-header">😴 PASSIVE STUDENT REVISION</div>
                <p class="contrast-body">Rereading highlighted textbook pages for the 4th time thinking: “I know this.” (Illusion of competence!)</p>
                <div class="contrast-tag tag-bad">Result: Blank out on twist questions</div>
              </div>
              <div class="contrast-col col-yellow">
                <div class="contrast-header">🎯 AI GAP REVISION PROMPT</div>
                <p class="contrast-body"><code>“Ask me 3 tricky application questions on Refraction that Class 10 students usually get wrong.”</code></p>
                <div class="contrast-tag tag-good">Result: Pinpoint blind spots in 5 minutes!</div>
              </div>
            </div>
            <div class="poster-footer-strip mt-2">
              <span class="strip-icon">💥</span> <strong>GOLDEN TRUTH:</strong> Better to feel the pain of a mistake in front of AI today than on the answer sheet tomorrow!
            </div>
          </div>
        </div>"""

# SLIDE 26 (Index 25): DON'T ASK THIS
replacements[25] = """        <!-- SLIDE 26: DON'T ASK THIS -->
        <div class="carousel-slide" data-index="25" data-section="20–35 MIN • MODULE 3" data-title="DON'T ASK THIS">
          <div class="poster-slide-card poster-yellow">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-pink">MINDSET REFRAME</span>
              <span class="brutal-stamp">THE 3-TOOL ARSENAL</span>
            </div>
            <h2 class="poster-hero-heading">STOP ASKING: <mark class="poster-highlight">“WHICH AI IS NUMBER ONE?”</mark></h2>
            <div class="three-tools-deck mt-2">
              <div class="deck-tool">
                <span class="tool-badge-pill pill-cyan">CHATGPT</span>
                <h3>“TEACH ME”</h3>
                <p>The Interactive Socratic Tutor & Evaluation Partner</p>
                <div class="tool-sub-use">Best for: Back-and-forth quizzing & answer checking</div>
              </div>
              <div class="deck-tool highlight">
                <span class="tool-badge-pill pill-lime">GEMINI</span>
                <h3>“SHOW ME”</h3>
                <p>Visual Multimodal Explorer & Diagram Master</p>
                <div class="tool-sub-use">Best for: Ray diagrams, circuits & organ systems</div>
              </div>
              <div class="deck-tool">
                <span class="tool-badge-pill pill-yellow">NOTEBOOKLM</span>
                <h3>“LOCK TO SYLLABUS”</h3>
                <p>Grounding Engine & Zero-Hallucination Book Companion</p>
                <div class="tool-sub-use">Best for: Your exact State Board PDF chapter</div>
              </div>
            </div>
            <div class="poster-footer-strip mt-2">
              <span class="strip-icon">🛠️</span> <strong>ANALOGY:</strong> A hammer isn't better than a screwdriver. Pick the right tool for the job!
            </div>
          </div>
        </div>"""

# SLIDE 30 (Index 29): TRANSITION TO LIVE DEMOS
replacements[29] = """        <!-- SLIDE 30: TRANSITION TO LIVE DEMOS -->
        <div class="carousel-slide" data-index="29" data-section="20–35 MIN • MODULE 3" data-title="TRANSITION TO LIVE DEMOS">
          <div class="poster-slide-card poster-lime">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-pink">STAGE PIVOT</span>
              <span class="brutal-stamp stamp-tilt">THE REAL ACTION</span>
              <span class="brutal-sticker sticker-cyan">LIVE ON PROJECTOR</span>
            </div>
            <h2 class="poster-hero-heading">ENOUGH TALKING ABOUT TOOLS.<br><mark class="poster-highlight">LET'S ACTUALLY STUDY ON SCREEN.</mark></h2>
            <div class="flow-sequence-box mt-3" style="max-width: 820px; margin: 1.5rem auto;">
              <div class="seq-step">1. REAL TOPIC</div>
              <div class="seq-arr">→</div>
              <div class="seq-step">2. BAD PROMPT</div>
              <div class="seq-arr">→</div>
              <div class="seq-step">3. UPGRADE PROMPT</div>
              <div class="seq-arr">→</div>
              <div class="seq-step highlight">4. EXAM LOCK</div>
            </div>
            <div class="poster-footer-strip mt-2">
              <span class="strip-icon">🔬</span> <strong>CASE STUDY TOPIC:</strong> Karnataka Board Science — <em>Force, Laws of Motion & Inertia</em>. Watch what happens!
            </div>
          </div>
        </div>"""

# SLIDE 32 (Index 31): BAD AI QUESTION
replacements[31] = """        <!-- SLIDE 32: BAD AI QUESTION -->
        <div class="carousel-slide" data-index="31" data-section="35–55 MIN • MODULE 4" data-title="BAD AI QUESTION">
          <div class="poster-slide-card poster-pink">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-yellow">THE LAZY MISTAKE</span>
              <span class="brutal-stamp stamp-tilt">DO NOT DO THIS</span>
            </div>
            <h2 class="poster-hero-heading">TYPING 5 WORDS: <mark class="poster-highlight">“EXPLAIN NEWTON'S 1ST LAW”</mark></h2>
            <div class="poster-contrast-grid mt-2">
              <div class="contrast-col col-white">
                <div class="contrast-header">🤖 WHAT AI DUMPS BACK AT YOU:</div>
                <p class="contrast-body">“An object at rest stays at rest and an object in motion stays in motion with the same speed and in the same direction unless acted upon by an unbalanced force.”</p>
                <div class="contrast-tag tag-bad">Textbook jargon overload &bull; 0% intuition gained</div>
              </div>
              <div class="contrast-col col-yellow">
                <div class="contrast-header">⚠️ WHY THIS FAILS STUDENTS AT 11 PM:</div>
                <p class="contrast-body">It's 100% factually accurate, but it didn't solve the student's confusion! If textbook words worked, you wouldn't need AI.</p>
                <div class="contrast-tag tag-yellow">Lazy Input = Lazy Output</div>
              </div>
            </div>
            <div class="poster-footer-strip mt-2">
              <span class="strip-icon">🚨</span> <strong>LESSON:</strong> When you give AI zero context, AI gives you zero teaching.
            </div>
          </div>
        </div>"""

# SLIDE 34 (Index 33): WHAT CHANGED?
replacements[33] = """        <!-- SLIDE 34: WHAT CHANGED? -->
        <div class="carousel-slide" data-index="33" data-section="35–55 MIN • MODULE 4" data-title="WHAT CHANGED?">
          <div class="poster-slide-card poster-cyan">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-yellow">PROMPT SURGERY</span>
              <span class="brutal-stamp stamp-tilt">THE SECRET</span>
            </div>
            <h2 class="poster-hero-heading">DID WE UPGRADE THE AI? <mark class="poster-highlight">NO. WE UPGRADED US.</mark></h2>
            <div class="four-pill-grid mt-2">
              <div class="fp-card fp-yellow">
                <span class="fp-num">1. WHO</span>
                <strong>Class 9 Student</strong>
                <p>Calibrates language level</p>
              </div>
              <div class="fp-card fp-lime">
                <span class="fp-num">2. GAP</span>
                <strong>Confused about Inertia</strong>
                <p>Targets the exact pain</p>
              </div>
              <div class="fp-card fp-cyan">
                <span class="fp-num">3. HOW</span>
                <strong>Cricket Bus Example</strong>
                <p>Builds concrete intuition</p>
              </div>
              <div class="fp-card fp-pink">
                <span class="fp-num">4. RULE</span>
                <strong>Quiz Me First!</strong>
                <p>Forces active recall</p>
              </div>
            </div>
            <div class="poster-footer-strip mt-2">
              <span class="strip-icon">🎯</span> <strong>TAKEAWAY:</strong> When you change how you ask, you completely change how you learn!
            </div>
          </div>
        </div>"""

# SLIDE 36 (Index 35): AI AS TUTOR
replacements[35] = """        <!-- SLIDE 36: AI AS TUTOR -->
        <div class="carousel-slide" data-index="35" data-section="35–55 MIN • MODULE 4" data-title="AI AS TUTOR">
          <div class="poster-slide-card poster-yellow">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-pink">THE COGNITIVE LOOP</span>
              <span class="brutal-stamp stamp-tilt">ACTIVE RECALL</span>
            </div>
            <h2 class="poster-hero-heading">THE ACTIVE TUTOR EQUATION</h2>
            <div class="flow-sequence-box mt-3" style="max-width: 850px; margin: 1.5rem auto;">
              <div class="seq-step">AI EXPLAINS</div>
              <div class="seq-arr">→</div>
              <div class="seq-step highlight">YOU THINK</div>
              <div class="seq-arr">→</div>
              <div class="seq-step">AI QUESTIONS</div>
              <div class="seq-arr">→</div>
              <div class="seq-step highlight">YOU ANSWER</div>
            </div>
            <div class="poster-contrast-grid mt-2">
              <div class="contrast-col col-white">
                <div class="contrast-header">WHO DID THE WORK?</div>
                <p class="contrast-body">You read, you visualized, you predicted, and you verified. Your neurons fired!</p>
              </div>
              <div class="contrast-col col-lime">
                <div class="contrast-header">WHO RETAINS THE KNOWLEDGE?</div>
                <p class="contrast-body">YOU DO. Because effortful retrieval builds long-term synaptic memory.</p>
              </div>
            </div>
          </div>
        </div>"""

# SLIDE 37 (Index 36): CATCH MY ANSWER
replacements[36] = """        <!-- SLIDE 37: CATCH MY ANSWER -->
        <div class="carousel-slide" data-index="36" data-section="35–55 MIN • MODULE 4" data-title="CATCH MY ANSWER">
          <div class="poster-slide-card poster-pink">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-yellow">AUDIENCE REFEREE TIME</span>
              <span class="brutal-stamp stamp-tilt">SPOT THE FLAW</span>
            </div>
            <h2 class="poster-hero-heading">STUDENT ANSWERS: “THE BUS PUSHES THEM.”</h2>
            <p class="slide-hero-sub text-center">Is this scientifically accurate? SHOUT YES OR NO!</p>
            <div class="poster-contrast-grid mt-2">
              <div class="contrast-col col-bad">
                <div class="contrast-header">❌ THE MISCONCEPTION</div>
                <p class="contrast-body">“The bus pushed the passengers forward when braking.” — <strong>0 MARKS!</strong> There is no forward force acting on them!</p>
              </div>
              <div class="contrast-col col-good">
                <div class="contrast-header">⚡ THE CORRECT PHYSICS</div>
                <p class="contrast-body">“Due to <strong>inertia of motion</strong>, the upper body continues moving forward while feet stop with the bus.” — <strong>FULL 2/2 MARKS!</strong></p>
              </div>
            </div>
            <div class="poster-footer-strip mt-2">
              <span class="strip-icon">🎯</span> <strong>HOW AI HELPS:</strong> AI catches this exact keyword mistake before your board examiner does!
            </div>
          </div>
        </div>"""

# SLIDE 38 (Index 37): THREE WAYS TO USE AI
replacements[37] = """        <!-- SLIDE 38: THREE WAYS TO USE AI -->
        <div class="carousel-slide" data-index="37" data-section="35–55 MIN • MODULE 4" data-title="THREE WAYS TO USE AI">
          <div class="poster-slide-card poster-white">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-lime">MATURITY MODEL</span>
              <span class="brutal-stamp">WHICH STUDENT ARE YOU?</span>
            </div>
            <h2 class="poster-hero-heading">THREE LEVELS OF USING AI</h2>
            <div class="three-tools-deck mt-2">
              <div class="deck-tool" style="background: #ffe4e6;">
                <span class="tool-badge-pill pill-pink">LEVEL 1 &bull; ❌</span>
                <h3>“GIVE ME THE ANSWER”</h3>
                <p>Copy-pasting answers</p>
                <div class="tool-sub-use">Retention: 0% &bull; Board score: Disaster</div>
              </div>
              <div class="deck-tool" style="background: #fefce8;">
                <span class="tool-badge-pill pill-yellow">LEVEL 2 &bull; ⚠️</span>
                <h3>“EXPLAIN IT TO ME”</h3>
                <p>Watching someone else work out</p>
                <div class="tool-sub-use">Retention: 25% &bull; Passive feeling of knowing</div>
              </div>
              <div class="deck-tool highlight" style="background: #dcfce7;">
                <span class="tool-badge-pill pill-lime">LEVEL 3 &bull; ⚡</span>
                <h3>“TEST ME & CHECK ME”</h3>
                <p>Active sparring partner</p>
                <div class="tool-sub-use">Retention: 90% &bull; Exam Confidence: TOP 1%</div>
              </div>
            </div>
          </div>
        </div>"""

# SLIDE 40 (Index 39): UNDERSTANDING != EXAM READY
replacements[39] = """        <!-- SLIDE 40: UNDERSTANDING ≠ EXAM READY -->
        <div class="carousel-slide" data-index="39" data-section="55–75 MIN • MODULE 5" data-title="UNDERSTANDING ≠ EXAM READY">
          <div class="poster-slide-card poster-yellow">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-pink">MODULE 5 &bull; THE EXAM GAP</span>
              <span class="brutal-stamp stamp-tilt">BRUTAL TRUTH</span>
            </div>
            <h2 class="poster-hero-heading">“I UNDERSTAND IT.”<br><mark class="poster-highlight">DOES THAT MEAN YOU GET FULL MARKS?</mark></h2>
            <div class="poster-contrast-grid mt-2">
              <div class="contrast-col col-white">
                <div class="contrast-header">🧠 IN YOUR HEAD</div>
                <p class="contrast-body">“I know what inertia is. It's when things keep going.”<br><em>(Feels good, but worth 0.5 marks!)</em></p>
              </div>
              <div class="contrast-col col-good">
                <div class="contrast-header">📝 ON THE EXAM PAPER</div>
                <p class="contrast-body">Requires 3 explicit elements: <strong>Definition + Unbalanced Force + SI Unit / Formula</strong>.<br><em>(Earns full 3/3 marks!)</em></p>
              </div>
            </div>
            <div class="poster-footer-strip mt-2">
              <span class="strip-icon">🎯</span> <strong>BOARD EXAM REALITY:</strong> Examiners don't grade what you meant. They grade the scientific keywords on paper!
            </div>
          </div>
        </div>"""

# SLIDE 42 (Index 41): STUDENT ANSWERS LIVE
replacements[41] = """        <!-- SLIDE 42: STUDENT ANSWERS LIVE -->
        <div class="carousel-slide" data-index="41" data-section="55–75 MIN • MODULE 5" data-title="STUDENT ANSWERS LIVE">
          <div class="poster-slide-card poster-cyan">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-yellow">3-MARK BOARD QUESTION</span>
              <span class="brutal-stamp">LIVE VOLUNTEER</span>
            </div>
            <h2 class="poster-hero-heading">“WHY CANNOT ATHLETES STOP IMMEDIATELY AFTER THE FINISH LINE?”</h2>
            <div class="prompt-box-editorial mt-2">
              <code>STUDENT VOLUNTEER PROMPT: “Grade this answer out of 3 marks based on Karnataka Board criteria: 'The athlete was running fast so their speed carries them across.' What marks did I lose?”</code>
            </div>
            <div class="poster-contrast-grid mt-2">
              <div class="contrast-col col-bad">
                <div class="contrast-header">LOST MARKS (-2)</div>
                <p class="contrast-body">Missing term: <strong>“Inertia of motion”</strong><br>Missing law: <strong>Newton's First Law reference</strong></p>
              </div>
              <div class="contrast-col col-good">
                <div class="contrast-header">AI COACHING INSTANT FEEDBACK</div>
                <p class="contrast-body">“1/3 Marks. You captured the idea, but board key mandates mentioning inertia of motion resisting change in velocity.”</p>
              </div>
            </div>
          </div>
        </div>"""

# SLIDE 44 (Index 43): WRONG ANSWERS ARE USEFUL
replacements[43] = """        <!-- SLIDE 44: WRONG ANSWERS ARE USEFUL -->
        <div class="carousel-slide" data-index="43" data-section="55–75 MIN • MODULE 5" data-title="WRONG ANSWERS ARE USEFUL">
          <div class="poster-slide-card poster-lime">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-pink">REFRAMING FAILURE</span>
              <span class="brutal-stamp stamp-tilt">NO SHAME</span>
            </div>
            <h2 class="poster-hero-heading">A WRONG ANSWER TODAY = FULL MARKS IN EXAM.</h2>
            <div class="four-pill-grid mt-2">
              <div class="fp-card fp-pink">
                <span class="fp-num">STEP 1</span>
                <strong>MISTAKE</strong>
                <p>Make it in private with AI</p>
              </div>
              <div class="fp-card fp-yellow">
                <span class="fp-num">STEP 2</span>
                <strong>DIAGNOSIS</strong>
                <p>AI spots the exact missing keyword</p>
              </div>
              <div class="fp-card fp-cyan">
                <span class="fp-num">STEP 3</span>
                <strong>CORRECTION</strong>
                <p>Rewrite once in your own words</p>
              </div>
              <div class="fp-card fp-lime">
                <span class="fp-num">STEP 4</span>
                <strong>100% LOCK</strong>
                <p>You will NEVER forget it on exam day</p>
              </div>
            </div>
            <div class="poster-footer-strip mt-2">
              <span class="strip-icon">🛡️</span> <strong>SAFE ZONE:</strong> AI has zero ego and never judges you. Make all your mistakes here!
            </div>
          </div>
        </div>"""

# SLIDE 47 (Index 46): EXAM TOMORROW
replacements[46] = """        <!-- SLIDE 47: EXAM TOMORROW -->
        <div class="carousel-slide" data-index="46" data-section="55–75 MIN • MODULE 5" data-title="EXAM TOMORROW">
          <div class="poster-slide-card poster-pink">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-yellow">EMERGENCY PROTOCOL</span>
              <span class="brutal-stamp stamp-tilt">PANIC NO MORE</span>
            </div>
            <h2 class="poster-hero-heading">EXAM TOMORROW. 3 CHAPTERS. 2 HOURS.</h2>
            <div class="four-pill-grid mt-2">
              <div class="fp-card fp-yellow">
                <span class="fp-num">00–30 MIN</span>
                <strong>PRIORITISE</strong>
                <p>“List the top 5 high-yield 3-mark & 5-mark topics for Karnataka Board.”</p>
              </div>
              <div class="fp-card fp-cyan">
                <span class="fp-num">30–60 MIN</span>
                <strong>ACTIVE RECALL</strong>
                <p>“Quiz me 1 question at a time. Do not reveal answer until I reply.”</p>
              </div>
              <div class="fp-card fp-lime">
                <span class="fp-num">60–90 MIN</span>
                <strong>DIAGRAM AUDIT</strong>
                <p>“Give step-by-step ray tracing checklist for convex lens.”</p>
              </div>
              <div class="fp-card fp-purple">
                <span class="fp-num">90–120 MIN</span>
                <strong>FORMULA LOCK</strong>
                <p>“Test me on units, sign conventions & definitions only.”</p>
              </div>
            </div>
          </div>
        </div>"""

# SLIDE 48 (Index 47): WHAT IF AI HAD YOUR MATERIAL?
replacements[47] = """        <!-- SLIDE 48: WHAT IF AI HAD YOUR MATERIAL? -->
        <div class="carousel-slide" data-index="47" data-section="75–90 MIN • MODULE 6" data-title="WHAT IF AI HAD YOUR MATERIAL?">
          <div class="poster-slide-card poster-cyan">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-yellow">MODULE 6 &bull; GROUNDING</span>
              <span class="brutal-stamp stamp-tilt">ENTER NOTEBOOKLM</span>
            </div>
            <h2 class="poster-hero-heading">WHAT IF AI ONLY KNEW <mark class="poster-highlight">YOUR EXACT TEXTBOOK?</mark></h2>
            <div class="poster-contrast-grid mt-2">
              <div class="contrast-col col-bad">
                <div class="contrast-header">🌐 REGULAR CHATGPT / INTERNET AI</div>
                <p class="contrast-body">Trained on the entire internet. Might bring CBSE, ICSE, or American syllabus terms you don't need!</p>
              </div>
              <div class="contrast-col col-good">
                <div class="contrast-header">🔒 NOTEBOOKLM GROUNDING</div>
                <p class="contrast-body">Locked inside your uploaded Karnataka State Board Science PDF. 100% syllabus accuracy with verifiable page citations!</p>
              </div>
            </div>
            <div class="poster-footer-strip mt-2">
              <span class="strip-icon">🎯</span> <strong>ZERO HALLUCINATIONS:</strong> It answers only from what your teacher will test you on.
            </div>
          </div>
        </div>"""

# SLIDE 55 (Index 54): PROMPT UPGRADE
replacements[54] = """        <!-- SLIDE 55: PROMPT UPGRADE -->
        <div class="carousel-slide" data-index="54" data-section="90–100 MIN • MODULE 7" data-title="PROMPT UPGRADE">
          <div class="poster-slide-card poster-yellow">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-pink">PROMPT MASTERY</span>
              <span class="brutal-stamp">THE 5-LEVEL STAIRCASE</span>
            </div>
            <h2 class="poster-hero-heading">WATCH A PROMPT GROW UP: ELECTRICITY</h2>
            <div class="staircase-grid mt-2">
              <div class="stair-step"><span class="s-level s-red">L1</span> “Explain electricity.” <em>(Too generic)</em></div>
              <div class="stair-step"><span class="s-level s-orange">L2</span> “Explain electricity for a Class 10 student.” <em>(Better)</em></div>
              <div class="stair-step"><span class="s-level s-yellow">L3</span> “...in simple words using a water pipe analogy.” <em>(Clear intuition)</em></div>
              <div class="stair-step"><span class="s-level s-cyan">L4</span> “...and give me 2 exam practice questions on Ohm's Law.” <em>(Active)</em></div>
              <div class="stair-step stair-highlight"><span class="s-level s-green">L5</span> “...ask questions ONE BY ONE and grade my answers against board criteria!” <em>(God Mode ⚡)</em></div>
            </div>
          </div>
        </div>"""

# SLIDE 56 (Index 55): THE 5-PART MASTER FORMULA
replacements[55] = """        <!-- SLIDE 56: THE 5-PART MASTER FORMULA -->
        <div class="carousel-slide" data-index="55" data-section="90–100 MIN • MODULE 7" data-title="THE 5-PART MASTER FORMULA">
          <div class="poster-slide-card poster-white">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-lime">THE GENIUSPHERE BLUEPRINT</span>
              <span class="brutal-stamp stamp-tilt">SAVE THIS</span>
            </div>
            <h2 class="poster-hero-heading">THE 5-PART PROMPT FORMULA</h2>
            <div class="five-blocks-row mt-2">
              <div class="f-block fb-yellow"><strong>1. WHO</strong> Class 10 Board Student</div>
              <div class="f-block fb-cyan"><strong>2. WHAT</strong> Specific Concept Gap</div>
              <div class="f-block fb-lime"><strong>3. CONTEXT</strong> 3-Mark Question Prep</div>
              <div class="f-block fb-orange"><strong>4. HOW</strong> Real-Life Analogy</div>
              <div class="f-block fb-pink"><strong>5. RULE</strong> Quiz Me First!</div>
            </div>
            <div class="prompt-box-editorial mt-2">
              <code>“I am a Class 10 Karnataka Board student [WHO]. I am confused about Electric Potential Difference [WHAT]. Explain with a water pump analogy [HOW] for a 3-mark question [CONTEXT]. Then quiz me one question at a time [RULE].”</code>
            </div>
          </div>
        </div>"""

# SLIDE 57 (Index 56): TEACHER ANALOGY REVISITED
replacements[56] = """        <!-- SLIDE 57: TEACHER ANALOGY REVISITED -->
        <div class="carousel-slide" data-index="56" data-section="90–100 MIN • MODULE 7" data-title="TEACHER ANALOGY REVISITED">
          <div class="poster-slide-card poster-lime">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-yellow">PROMPT WISDOM</span>
              <span class="brutal-stamp">THE GOLDEN RULE</span>
            </div>
            <h2 class="poster-hero-heading">“BETTER QUESTIONS CREATE BETTER LEARNING.”</h2>
            <div class="poster-contrast-grid mt-2">
              <div class="contrast-col col-white">
                <div class="contrast-header">STUDENT WALKS UP TO TEACHER:</div>
                <p class="contrast-body">“Sir, teach me Physics.”<br><em>Teacher has no idea where to start!</em></p>
              </div>
              <div class="contrast-col col-yellow">
                <div class="contrast-header">STUDENT ASKS PRECISELY:</div>
                <p class="contrast-body">“Sir, I understand potential difference, but why does resistance increase with wire length?”<br><em>Teacher gives a 60-second breakthrough explanation!</em></p>
              </div>
            </div>
            <div class="poster-footer-strip mt-2">
              <span class="strip-icon">🎯</span> <strong>AI IS THE SAME:</strong> Treat AI like a brilliant teacher standing in front of you. Give it context!
            </div>
          </div>
        </div>"""

# SLIDE 58 (Index 57): PROMPT BATTLE
replacements[57] = """        <!-- SLIDE 58: PROMPT BATTLE ⚔️ -->
        <div class="carousel-slide" data-index="57" data-section="90–100 MIN • MODULE 7" data-title="PROMPT BATTLE ⚔️">
          <div class="poster-slide-card poster-pink">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-yellow">AUDIENCE BATTLE &bull; 45 SECONDS</span>
              <span class="brutal-stamp stamp-tilt">ARENA TIME</span>
            </div>
            <h2 class="poster-hero-heading">PROMPT BATTLE ⚔️: LEFT WING VS RIGHT WING!</h2>
            <p class="slide-hero-sub text-center">Topic: <strong>“Refraction through a Glass Slab & Lateral Displacement”</strong></p>
            <div class="poster-contrast-grid mt-2">
              <div class="contrast-col col-white">
                <div class="contrast-header">🔵 LEFT WING AUDIENCE</div>
                <p class="contrast-body">Craft a prompt that commands AI to explain with a car-moving-from-road-to-mud analogy.</p>
              </div>
              <div class="contrast-col col-yellow">
                <div class="contrast-header">🔴 RIGHT WING AUDIENCE</div>
                <p class="contrast-body">Craft a prompt that commands AI to quiz you with ray-tracing ray angles and normal lines.</p>
              </div>
            </div>
          </div>
        </div>"""

# SLIDE 60 (Index 59): CHECK MY WORK RULE
replacements[59] = """        <!-- SLIDE 60: CHECK MY WORK RULE -->
        <div class="carousel-slide" data-index="59" data-section="90–100 MIN • MODULE 7" data-title="CHECK MY WORK RULE">
          <div class="poster-slide-card poster-yellow">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-pink">ACADEMIC INTEGRITY</span>
              <span class="brutal-stamp stamp-tilt">MANDATORY RULE</span>
            </div>
            <h2 class="poster-hero-heading">“CHECK MY REASONING, DO NOT REWRITE MY ANSWER.”</h2>
            <div class="poster-contrast-grid mt-2">
              <div class="contrast-col col-bad">
                <div class="contrast-header">❌ WHY REWRITING KILLS LEARNING:</div>
                <p class="contrast-body">When AI writes fancy 10th-grade English sentences for you, your brain feels satisfied without building any vocabulary or writing skill.</p>
              </div>
              <div class="contrast-col col-good">
                <div class="contrast-header">⚡ WHAT YOU MUST ASK INSTEAD:</div>
                <p class="contrast-body"><code>“Point out the 2 scientific keywords I missed, but let ME rewrite the sentence myself.”</code></p>
              </div>
            </div>
          </div>
        </div>"""

# SLIDE 61 (Index 60): CAN YOU TRUST AI?
replacements[60] = """        <!-- SLIDE 61: CAN YOU TRUST AI? -->
        <div class="carousel-slide" data-index="60" data-section="100–110 MIN • MODULE 8" data-title="CAN YOU TRUST AI?">
          <div class="poster-slide-card poster-white">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-lime">MODULE 8 &bull; AI MISTAKES</span>
              <span class="brutal-stamp">AUDIENCE VOTE</span>
            </div>
            <h2 class="poster-hero-heading">CAN YOU TRUST AI FOR BOARD EXAMS?</h2>
            <div class="vote-grid-large mt-3">
              <div class="vote-option vo-green">
                <span class="vo-letter">A</span>
                <span class="vo-label">YES!</span>
                <p>“It's smarter than everyone.”</p>
              </div>
              <div class="vote-option vo-red">
                <span class="vo-letter">B</span>
                <span class="vo-label">NO!</span>
                <p>“It lies all the time.”</p>
              </div>
              <div class="vote-option vo-yellow vo-winner">
                <span class="vo-letter">C</span>
                <span class="vo-label">IT DEPENDS! ⚡</span>
                <p>“Trust, but verify with your textbook!”</p>
              </div>
            </div>
          </div>
        </div>"""

# SLIDE 62 (Index 61): CONFIDENT != CORRECT
replacements[61] = """        <!-- SLIDE 62: CONFIDENT ≠ CORRECT -->
        <div class="carousel-slide" data-index="61" data-section="100–110 MIN • MODULE 8" data-title="CONFIDENT ≠ CORRECT">
          <div class="poster-slide-card poster-pink">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-yellow">CRITICAL PUNCHLINE</span>
              <span class="brutal-stamp stamp-tilt">WATCH OUT</span>
            </div>
            <h2 class="poster-hero-heading">CONFIDENT <mark class="poster-highlight">DOES NOT MEAN CORRECT.</mark></h2>
            <div class="poster-contrast-grid mt-2">
              <div class="contrast-col col-white">
                <div class="contrast-header">🎭 HOW AI SOUNDS:</div>
                <p class="contrast-body">Like a Harvard professor wearing a lab coat. Flawless grammar, perfectly confident tone, zero hesitation!</p>
              </div>
              <div class="contrast-col col-yellow">
                <div class="contrast-header">⚠️ WHAT MIGHT ACTUALLY BE HAPPENING:</div>
                <p class="contrast-body">It could be hallucinating a formula or mixing up an exception in the periodic table! You must always check.</p>
              </div>
            </div>
            <div class="poster-footer-strip mt-2">
              <span class="strip-icon">🛡️</span> <strong>REMEMBER:</strong> In board exam evaluations, writing a confident hallucination gets you 0 marks.
            </div>
          </div>
        </div>"""

# SLIDE 63 (Index 62): CATCH THE AI
replacements[62] = """        <!-- SLIDE 63: CATCH THE AI -->
        <div class="carousel-slide" data-index="62" data-section="100–110 MIN • MODULE 8" data-title="CATCH THE AI">
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
        </div>"""

# SLIDE 64 (Index 63): GAME: HUMAN OR AI?
replacements[63] = """        <!-- SLIDE 64: GAME: HUMAN OR AI? -->
        <div class="carousel-slide" data-index="63" data-section="100–110 MIN • MODULE 8" data-title="GAME: HUMAN OR AI?">
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
        </div>"""

# SLIDE 65 (Index 64): STOP. CHECK. THINK.
replacements[64] = """        <!-- SLIDE 65: STOP. CHECK. THINK. -->
        <div class="carousel-slide" data-index="64" data-section="100–110 MIN • MODULE 8" data-title="STOP. CHECK. THINK.">
          <div class="poster-slide-card poster-white">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-lime">THE 3-STEP PROTOCOL</span>
              <span class="brutal-stamp stamp-tilt">SURVIVAL KIT</span>
            </div>
            <h2 class="poster-hero-heading">THE VERIFICATION PROTOCOL</h2>
            <div class="traffic-light-grid mt-3">
              <div class="tl-card tl-red">
                <span class="tl-icon">🔴</span>
                <h3>STOP</h3>
                <p>Never blindly copy AI output directly into homework or exam prep notes.</p>
              </div>
              <div class="tl-card tl-yellow">
                <span class="tl-icon">🟡</span>
                <h3>CHECK</h3>
                <p>Cross-verify against your Karnataka State Board approved textbook & syllabus.</p>
              </div>
              <div class="tl-card tl-green">
                <span class="tl-icon">🟢</span>
                <h3>THINK</h3>
                <p>Close the laptop screen. Can you explain the concept out loud in your own words?</p>
              </div>
            </div>
          </div>
        </div>"""

# SLIDE 67 (Index 66): YOUR MISSION
replacements[66] = """        <!-- SLIDE 67: YOUR MISSION -->
        <div class="carousel-slide" data-index="66" data-section="110–120 MIN • MODULE 9" data-title="YOUR MISSION">
          <div class="poster-slide-card poster-lime">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-pink">MODULE 9 &bull; COMPUTER LAB</span>
              <span class="brutal-stamp stamp-tilt">ACTION TIME</span>
            </div>
            <h2 class="poster-hero-heading">🚨 YOUR LAB MISSION: <mark class="poster-highlight">CONQUER THE CHAPTER YOU HATE!</mark></h2>
            <p class="slide-hero-sub text-center">That one chapter you keep telling your parents you'll study tomorrow. 😂 Pick it now:</p>
            <div class="four-pill-grid mt-2">
              <div class="fp-card fp-yellow"><strong>Physics</strong> Force & Laws of Motion</div>
              <div class="fp-card fp-cyan"><strong>Physics</strong> Light & Ray Optics</div>
              <div class="fp-card fp-lime"><strong>Chemistry</strong> Chemical Reactions & Equations</div>
              <div class="fp-card fp-pink"><strong>Biology</strong> Life Processes & Respiration</div>
            </div>
          </div>
        </div>"""

# SLIDE 68 (Index 67): THE 5 LAB STEPS
replacements[67] = """        <!-- SLIDE 68: THE 5 LAB STEPS -->
        <div class="carousel-slide" data-index="67" data-section="110–120 MIN • MODULE 9" data-title="THE 5 LAB STEPS">
          <div class="poster-slide-card poster-yellow">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-cyan">WORKFLOW GUIDE</span>
              <span class="brutal-stamp">60 MINUTES</span>
            </div>
            <h2 class="poster-hero-heading">THE 5 STEPS TO LAB VICTORY:</h2>
            <div class="five-blocks-row mt-2">
              <div class="f-block fb-white"><strong>1. EXPLAIN</strong> Command AI to give an analogy</div>
              <div class="f-block fb-lime"><strong>2. QUIZ</strong> Command AI to test you 1 question</div>
              <div class="f-block fb-cyan"><strong>3. ANSWER</strong> Type answer in your own words</div>
              <div class="f-block fb-pink"><strong>4. CHECK</strong> Check keywords against board criteria</div>
              <div class="f-block fb-purple"><strong>5. LOCK</strong> Save your completed summary report</div>
            </div>
          </div>
        </div>"""

# SLIDE 70 (Index 69): ENOUGH WATCHING
replacements[69] = """        <!-- SLIDE 70: ENOUGH WATCHING -->
        <div class="carousel-slide" data-index="69" data-section="110–120 MIN • MODULE 9" data-title="ENOUGH WATCHING">
          <div class="poster-slide-card poster-pink">
            <div class="poster-badge-row">
              <span class="brutal-sticker sticker-yellow">STAGE COMPLETE</span>
              <span class="brutal-stamp stamp-tilt">HANDS ON KEYBOARD</span>
            </div>
            <h2 class="poster-hero-heading">ENOUGH WATCHING.<br><mark class="poster-highlight">NOW YOU TRY IN THE LAB!</mark></h2>
            <div class="poster-contrast-grid mt-2">
              <div class="contrast-col col-white">
                <div class="contrast-header">⏰ 60-MINUTE COUNTDOWN</div>
                <p class="contrast-body">Facilitators are circulating around the lab. Complete all 7 practical missions!</p>
              </div>
              <div class="contrast-col col-yellow">
                <div class="contrast-header">🏆 YOUR GOAL</div>
                <p class="contrast-body">Produce your personalized AI Study Dossier ready for print and revision before exams.</p>
              </div>
            </div>
            <div class="text-center mt-3">
              <button type="button" class="btn btn-large btn-primary" onclick="switchMainMode('lab')">
                🧪 LAUNCH STUDENT COMPUTER LAB WORKSPACE &rarr;
              </button>
            </div>
          </div>
        </div>"""

# Apply all replacements to index.html
pattern = r'(<!-- SLIDE \d+:[^\n]*-->\s*<div class="carousel-slide"[^>]*data-index="(\d+)"[^>]*>.*?</div>\s*)(?=<!-- SLIDE|\s*</div>\s*<!-- Carousel Controls|\s*</div>\s*<!-- PRESENTATION STAGE)'

def replacer(match):
    idx = int(match.group(2))
    if idx in replacements:
        return replacements[idx] + '\n\n'
    return match.group(0)

# Replace each slide individually
for idx, new_slide in replacements.items():
    # Look for the specific slide by data-index
    slide_regex = rf'(<!-- SLIDE 0?{idx+1}:[^\n]*-->\s*<div class="carousel-slide"[^>]*data-index="{idx}"[^>]*>.*?</div>\s*)(?=<!-- SLIDE|\s*</div>\s*<!-- Carousel Controls|\s*</div>\s*<button type="button" class="carousel-nav-btn next-arrow")'
    if re.search(slide_regex, html, re.DOTALL):
        html = re.sub(slide_regex, new_slide + '\n\n        ', html, count=1, flags=re.DOTALL)
        print(f"Replaced Slide {idx+1}")
    else:
        print(f"Could not find regex for Slide {idx+1}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Finished updating index.html!")

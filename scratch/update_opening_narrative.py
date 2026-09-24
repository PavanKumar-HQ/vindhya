import re

# Update build_curriculum_36.py slides 0 to 4
with open('scratch/build_curriculum_36.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Let's inspect where slide 0 to 4 are defined
slide0_marker = '# SLIDE 01: OPENING & ICEBREAKER'
slide6_marker = '# Slide 06: Module 1 Overview'

idx_start = code.find(slide0_marker)
idx_end = code.find(slide6_marker)

if idx_start == -1 or idx_end == -1:
    print("Markers not found in build_curriculum_36.py")
    exit(1)

new_slides_0_to_5 = '''# SLIDE 01: WALK IN WITH A QUESTION (NOT A DEFINITION)
# =========================================================================
s1_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">STUDENT REALITY</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">“I UNDERSTOOD ABSOLUTELY NOTHING.”</h3>
  </div>
  <div class="panel-body-content">
    <div class="relatable-story-card">
      <p class="story-lead">Before we start, I want to ask you something:</p>
      <div class="story-highlight-box mt-2">
        <p>“How many of you have ever been studying at night, opened a chapter, read the same paragraph two or three times…</p>
        <p class="story-punchline mt-2">and still thought: <strong>‘I understood absolutely nothing.’</strong>”</p>
      </div>
      <p class="story-caption mt-2"><em>Pause. Every single head in the room starts nodding.</em></p>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-yellow">REALITY: 100% of students have felt this</span>
  </div>
"""
s1_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">WHAT HAPPENS NEXT?</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">AND THEN WHAT DO YOU DO?</h3>
  </div>
  <div class="panel-body-content">
    <div class="bullet-list-editorial">
      <div class="bullet-item">
        <div class="bullet-icon bg-red">📺</div>
        <div class="bullet-text">
          <strong>You search YouTube</strong>
          <span class="bullet-sub">Watch a 25-minute video just to understand a 2-mark definition.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">📞</div>
        <div class="bullet-text">
          <strong>You message your friend</strong>
          <span class="bullet-sub">“Bro, what is this?! Are you studying Chapter 9?!”</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-green">🤖</div>
        <div class="bullet-text">
          <strong>And now there's one more person you can ask...</strong>
          <span class="bullet-sub"><strong>AI.</strong> (ChatGPT, Gemini, NotebookLM)</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-green">THE NEW REALITY OF 2026</span>
  </div>
"""
slides.append(make_slide(0, "0–5 MIN • OPENING", "THE REALITY &bull; “I UNDERSTOOD NOTHING”", s1_left, s1_right))

# =========================================================================
# SLIDE 02: ICEBREAKER — WHAT WOULD YOU DO?
# =========================================================================
s2_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-red">THE 10:30 PM MOMENT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">THE SCENARIO EVERY STUDENT DREADS</h3>
  </div>
  <div class="panel-body-content">
    <div class="nightmare-banner">
      <div class="banner-line">IT'S 10:30 PM.</div>
      <div class="banner-line">EXAM TOMORROW.</div>
      <div class="banner-line">ONE CHAPTER LEFT.</div>
      <div class="banner-line highlight-red">YOU DON'T UNDERSTAND IT.</div>
    </div>
    <div class="panic-meter-strip mt-3">
      <span class="strip-label">PRESSURE LEVEL:</span>
      <span class="strip-badge badge-red">🚨 MAXIMUM PANIC</span>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-red">SUNDAY NIGHT MOMENT</span>
  </div>
"""
s2_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">AUDIENCE POLL</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">BE HONEST: WHAT ARE YOU DOING?</h3>
  </div>
  <div class="panel-body-content">
    <div class="interactive-poll-grid">
      <div class="option-card" onclick="castAudienceVote(this, 22)">
        <span class="option-badge">A</span>
        <div class="option-content">
          <strong>YouTube</strong>
          <span>Search 1.5x speed video</span>
        </div>
      </div>
      <div class="option-card" onclick="castAudienceVote(this, 18)">
        <span class="option-badge">B</span>
        <div class="option-content">
          <strong>Ask a friend</strong>
          <span>Message: "Bro, help me!"</span>
        </div>
      </div>
      <div class="option-card" onclick="castAudienceVote(this, 15)">
        <span class="option-badge">C</span>
        <div class="option-content">
          <strong>Pretend tomorrow doesn't exist</strong>
          <span>Sleep &amp; hope for a miracle</span>
        </div>
      </div>
      <div class="option-card highlight-card" onclick="castAudienceVote(this, 75)">
        <span class="option-badge badge-cyan">D</span>
        <div class="option-content">
          <strong>Ask AI</strong>
          <span>Type into ChatGPT/Gemini</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-cyan">CLICK AN OPTION TO VOTE LIVE</span>
  </div>
"""
slides.append(make_slide(1, "0–5 MIN • OPENING", "IT'S 10:30 PM &bull; WHAT WOULD YOU DO?", s2_left, s2_right))

# =========================================================================
# SLIDE 03: THE BIG QUESTION (THE HOOK)
# =========================================================================
s3_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">THE BIG QUESTION</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">THE CORE HOOK OF TODAY</h3>
  </div>
  <div class="panel-body-content">
    <div class="big-hook-card">
      <blockquote class="hook-quote">
        “Are you using AI to study… or are you using AI to avoid studying?”
      </blockquote>
      <p class="hook-sub mt-2">Let that sit on screen. Because there is a <strong>huge difference</strong>.</p>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-pink">THE DEFINING QUESTION</span>
  </div>
"""
s3_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">THE HUGE DIFFERENCE</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WHO IS DOING THE THINKING?</h3>
  </div>
  <div class="panel-body-content">
    <div class="comparison-card">
      <div class="compare-col bad-col">
        <div class="compare-badge badge-bad">❌ AI DID THE THINKING</div>
        <p class="mt-1">You ask: <em>“Give me the 5-mark answer.”</em></p>
        <p>&bull; Copy it</p>
        <p>&bull; Memorize it</p>
        <p>&bull; Write it in the exam</p>
        <p class="mt-1"><strong>Result:</strong> Zero real learning.</p>
      </div>
      <div class="compare-versus-badge">VS</div>
      <div class="compare-col good-col">
        <div class="compare-badge badge-good">✅ YOU ARE LEARNING</div>
        <p class="mt-1">You ask: <em>“I don't understand this. Teach it to me. Give me an example. Then test me.”</em></p>
        <p class="mt-1"><strong>Result:</strong> Real neural comprehension!</p>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-green">YOU MUST DO THE LEARNING</span>
  </div>
"""
slides.append(make_slide(2, "0–5 MIN • OPENING", "THE BIG QUESTION &bull; STUDY OR AVOID STUDYING?", s3_left, s3_right))

# =========================================================================
# SLIDE 04: INTRODUCE THE WORKSHOP
# =========================================================================
s4_left = """
  <div class="slide-content-box center-aligned">
    <span class="slide-eyebrow">GENIUSPHERE PRESENTS</span>
    <h1 class="slide-hero-title">AI EXAM LAB</h1>
    <p class="slide-hero-sub">Learn with AI. Don't let AI learn for you.</p>
    <div class="slide-visual-media mt-2">
      <img src="assets/hero_learning_loop.jpg" alt="AI & Human Cognitive Loop" class="slide-presentation-img" style="max-height: 220px; object-fit: contain;">
    </div>
    <div class="slide-footer-tag mt-2">Karnataka State Board &bull; Classes 9 &amp; 10</div>
  </div>
"""
s4_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">WORKSHOP PROMISE</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WHAT WE ARE ACTUALLY DOING TODAY</h3>
  </div>
  <div class="panel-body-content">
    <div class="bullet-list-editorial">
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">🚫</div>
        <div class="bullet-text">
          <strong>No Boring AI History</strong>
          <span class="bullet-sub">“I'm not going to spend the next two hours explaining what artificial intelligence is. You already know AI exists. You've probably already used it.”</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-green">🎯</div>
        <div class="bullet-text">
          <strong>100% Practical Exam Preparation</strong>
          <span class="bullet-sub"><strong>“How can you actually use ChatGPT, Gemini and NotebookLM to prepare for your exams?”</strong></span>
        </div>
      </div>
    </div>
    <div class="three-pillars-strip mt-3">
      <div class="pillar-chip bg-yellow">1. UNDERSTAND</div>
      <div class="pillar-chip bg-cyan">2. PRACTISE</div>
      <div class="pillar-chip bg-pink">3. IMPROVE</div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-cyan">UNDERSTAND &bull; PRACTISE &bull; IMPROVE</span>
  </div>
"""
slides.append(make_slide(3, "0–5 MIN • OPENING", "AI EXAM LAB &bull; THE WORKSHOP PROMISE", s4_left, s4_right))

# =========================================================================
# SLIDE 05: THE PHILOSOPHY QUOTE & STUDENT INTERACTION
# =========================================================================
s5_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">GENIUSPHERE PHILOSOPHY</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">THE ONE LINE TO REMEMBER TODAY</h3>
  </div>
  <div class="panel-body-content">
    <div class="philosophy-quote-card">
      <blockquote class="slide-blockquote" style="font-size: 1.55rem; line-height: 1.35; margin: 0;">
        “The smartest use of AI isn't getting the answer faster. It's learning how to understand it better.”
      </blockquote>
      <p class="quote-sub mt-2">Remember that throughout today's session.</p>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-yellow">GENIUSPHERE ORIGINAL PRINCIPLE</span>
  </div>
"""
s5_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">STUDENT INTERACTION</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WHEN YOU DON'T UNDERSTAND, WHAT DO YOU ASK?</h3>
  </div>
  <div class="panel-body-content">
    <div class="question-ladder">
      <div class="ladder-item item-weak">
        <span class="ladder-badge">LEVEL 1</span>
        <div class="ladder-text">“What is this?”</div>
      </div>
      <div class="ladder-item item-mid">
        <span class="ladder-badge">LEVEL 2</span>
        <div class="ladder-text">“Explain this in simple language.”</div>
      </div>
      <div class="ladder-item item-good">
        <span class="ladder-badge">LEVEL 3</span>
        <div class="ladder-text">“Give me an example.”</div>
      </div>
      <div class="ladder-item item-master">
        <span class="ladder-badge badge-green">MASTER</span>
        <div class="ladder-text"><strong>“Ask me a question to see if I understood.”</strong></div>
      </div>
    </div>
    <p class="ladder-ask mt-2"><strong>Audience Question:</strong> “Which one of these is actually helping you learn?”</p>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-pink">BRIDGE TO MODULE 1</span>
  </div>
"""
slides.append(make_slide(4, "0–5 MIN • OPENING", "THE CORE PHILOSOPHY &bull; WHAT DO YOU ASK?", s5_left, s5_right))

'''

new_code = code[:idx_start] + new_slides_0_to_5 + code[idx_end:]

with open('scratch/build_curriculum_36.py', 'w', encoding='utf-8') as f:
    f.write(new_code)

print("Updated scratch/build_curriculum_36.py successfully!")

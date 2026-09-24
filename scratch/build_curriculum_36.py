import os
import re

def make_slide(idx, section, title, left_html, right_html, is_single=False, single_html=""):
    num_str = f"{idx+1:02d}"
    active_cls = " active" if idx == 0 else ""
    
    if is_single:
        return f"""
        <!-- MERGED SLIDE {num_str}: {title} -->
        <div class="carousel-slide{active_cls}" data-index="{idx}" data-section="{section}" data-title="{title}">
          <div class="merged-slide-container">
            <div class="merged-slide-header">
              <div class="m-badge-group">
                <span class="m-badge badge-gradient">{section}</span>
                <span class="m-badge badge-navy">PART {num_str} OF 36</span>
              </div>
              <h2 class="m-slide-title">{title}</h2>
            </div>
            <div class="merged-slide-single">
              {single_html}
            </div>
          </div>
        </div>"""
    else:
        return f"""
        <!-- MERGED SLIDE {num_str}: {title} -->
        <div class="carousel-slide{active_cls}" data-index="{idx}" data-section="{section}" data-title="{title}">
          <div class="merged-slide-container">
            <div class="merged-slide-header">
              <div class="m-badge-group">
                <span class="m-badge badge-gradient">{section}</span>
                <span class="m-badge badge-navy">PART {num_str} OF 36</span>
              </div>
              <h2 class="m-slide-title">{title}</h2>
            </div>
            
            <div class="merged-slide-grid">
              <div class="m-panel panel-left">
                {left_html}
              </div>
              <div class="m-panel panel-right">
                {right_html}
              </div>
            </div>
          </div>
        </div>"""

slides = []

# =========================================================================
# SLIDE 01: WALK IN WITH A QUESTION (NOT A DEFINITION)
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

# Slide 06: Module 1 Overview
s6_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">MODULE 1 &bull; PURPOSE</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">CHATGPT: UNDERSTAND DIFFICULT CONCEPTS</h3>
  </div>
  <div class="panel-body-content">
    <div class="purpose-card">
      <span class="purpose-label">CORE PURPOSE:</span>
      <p class="purpose-text">Help a student when they are <strong>completely stuck</strong> on a difficult chapter or textbook topic at home.</p>
    </div>
    <div class="bullet-list-editorial mt-3">
      <div class="bullet-item">
        <div class="bullet-icon bg-red">📖</div>
        <div class="bullet-text">
          <strong>The Textbook Bottleneck</strong>
          <span class="bullet-sub">Textbooks explain things in formal academic English. If you don't understand paragraph 1, you can't understand paragraph 2.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-green">🤖</div>
        <div class="bullet-text">
          <strong>AI as Interactive Tutor</strong>
          <span class="bullet-sub">ChatGPT can rewrite ANY difficult law into simple language, analogies, and everyday stories until it clicks.</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-yellow">SKILL 1: Concept Decoding</span>
  </div>
"""
s6_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">MODULE 1 CHECKLIST</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WHAT WE TOUCH IN THIS MODULE</h3>
  </div>
  <div class="panel-body-content">
    <div class="bullet-list-editorial">
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">1️⃣</div>
        <div class="bullet-text">
          <strong>How to ask ChatGPT to explain a concept</strong>
          <span class="bullet-sub">Setting grade level and subject context.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-cyan">2️⃣</div>
        <div class="bullet-text">
          <strong>How to ask for simpler language</strong>
          <span class="bullet-sub">Stripping away unnecessary Latin roots and confusing jargon.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-pink">3️⃣</div>
        <div class="bullet-text">
          <strong>How to ask for examples &amp; analogies</strong>
          <span class="bullet-sub">Connecting physics to school buses, cricket, and bicycles.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-green">4️⃣</div>
        <div class="bullet-text">
          <strong>How to ask follow-up questions</strong>
          <span class="bullet-sub">Having a real conversation instead of accepting one reply.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">5️⃣</div>
        <div class="bullet-text">
          <strong>How to ask AI to check whether YOU understood</strong>
          <span class="bullet-sub">The golden rule: AI must test you before moving on!</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-cyan">5 CONCRETE DRILLS</span>
  </div>
"""
slides.append(make_slide(5, "15–30 MIN • MODULE 1: UNDERSTAND", "MODULE 1 OVERVIEW &bull; STUCK ON A CHAPTER?", s6_left, s6_right))

# Slide 07: Newton's Bus Example & Prompt
s7_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">PROMPT TRANSFORMATION</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">CASE STUDY: STRUGGLING WITH NEWTON'S FIRST LAW</h3>
  </div>
  <div class="panel-body-content">
    <div class="compare-box-vertical">
      <div class="box-bad mb-2">
        <span class="box-tag tag-red">❌ INSTEAD OF LAZY PROMPTING:</span>
        <div class="code-preview">"Explain Newton's First Law."</div>
        <p class="box-note">Result: 400 words of dry textbook language that leaves you just as confused as before.</p>
      </div>
      <div class="box-good">
        <span class="box-tag tag-green">✅ TEACH THEM TO SAY THIS:</span>
        <div class="prompt-box">
          <div class="prompt-header">
            <span class="prompt-label">🎯 MASTER TUTOR PROMPT</span>
            <button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button>
          </div>
          <div class="prompt-text">"I'm a Class 9 student. I don't understand Newton's First Law. Explain it in simple language using a school-bus example. Then ask me one question to check if I understood."</div>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-green">NOTICE: Role + Analogy + Test Rule</span>
  </div>
"""
s7_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">LIVE DEMONSTRATION</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">THE SCHOOL BUS BREAKTHROUGH</h3>
  </div>
  <div class="panel-body-content">
    <div class="chat-simulation-card">
      <div class="chat-msg msg-ai">
        <div class="chat-avatar">🤖</div>
        <div class="chat-bubble">
          <p><strong>ChatGPT:</strong> Imagine you are standing in a school bus moving at 40 km/h. Your whole body is moving forward at 40 km/h.</p>
          <p class="mt-1">Suddenly, a dog runs across the road. The driver slams on the brakes! The bus floor stops instantly.</p>
          <p class="mt-1"><strong>What happens to you?</strong> Your feet stop because they touch the bus floor. But your upper body? It still wants to keep moving at 40 km/h! So you fly forward!</p>
          <p class="mt-1"><em>That is Newton's First Law: Things keep doing what they are doing unless a force stops them!</em></p>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-yellow">CONCEPT CLICKS IN 10 SECONDS!</span>
  </div>
"""
slides.append(make_slide(6, "15–30 MIN • MODULE 1: UNDERSTAND", "THE NEWTON'S BUS BREAKTHROUGH &bull; THE EXACT PROMPT", s7_left, s7_right))

# Slide 08: Follow-up Learning Conversation
s8_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">CONVERSATION FLOW</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">DON'T STOP AT ONE PROMPT: ASK FOLLOW-UPS</h3>
  </div>
  <div class="panel-body-content">
    <p>A single prompt gives an answer. A <strong>follow-up conversation</strong> builds deep understanding.</p>
    <div class="bullet-list-editorial mt-2">
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">💬</div>
        <div class="bullet-text">
          <strong>Follow-up 1: Test Opposite Scenarios</strong>
          <span class="bullet-sub">"What if the bus is standing still at a traffic light and suddenly zooms forward? Why do I fall backward?"</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-pink">🏏</div>
        <div class="bullet-text">
          <strong>Follow-up 2: Change the Analogy</strong>
          <span class="bullet-sub">"Can you explain the same law using a cricket ball or a bicycle?"</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-cyan">🔍</div>
        <div class="bullet-text">
          <strong>Follow-up 3: Clarify Confusing Keywords</strong>
          <span class="bullet-sub">"What does 'unbalanced external force' mean without using textbook jargon?"</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-cyan">POWER MOVE: Keep asking until 100% clear</span>
  </div>
"""
s8_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">AI CHECK QUESTION</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">THE CHECK QUESTION &bull; LIVE STUDENT TEST</h3>
  </div>
  <div class="panel-body-content">
    <div class="chat-simulation-card">
      <div class="chat-msg msg-ai">
        <div class="chat-avatar">🤖</div>
        <div class="chat-bubble">
          <p><strong>ChatGPT's Check Question to Student:</strong></p>
          <p class="mt-1">“Now let's check your understanding:</p>
          <p class="highlight-quote mt-1">If you throw an apple straight up inside a school bus that is moving smoothly at constant speed in a straight line, will the apple land back in your hand, behind you, or in front of you? Explain why using inertia.”</p>
        </div>
      </div>
    </div>
    <div class="callout-interactive mt-3">
      <strong>Audience Challenge:</strong> Who has the answer? Raise your hand!
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-green">STUDENT MUST THINK &bull; NOT JUST NOD</span>
  </div>
"""
slides.append(make_slide(7, "15–30 MIN • MODULE 1: UNDERSTAND", "THE LEARNING CONVERSATION &bull; FOLLOW-UP DRILLS", s8_left, s8_right))

# Slide 09: What they learn & Exam Benefit
s9_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">TAKEAWAY</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WHAT STUDENTS LEARN IN MODULE 1</h3>
  </div>
  <div class="panel-body-content">
    <div class="takeaway-big-card">
      <div class="takeaway-icon">💡</div>
      <h4 class="takeaway-headline">AI CAN BECOME AN INTERACTIVE TUTORING TOOL</h4>
      <p class="takeaway-desc">AI is not just a search box to paste answers from. It is an interactive dialogue partner that meets you at YOUR exact learning level.</p>
    </div>
    <div class="bullet-list-editorial mt-3">
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">⚡</div>
        <div class="bullet-text">
          <strong>No Fear of Looking Silly</strong>
          <span class="bullet-sub">You can ask "Explain it like I am 8 years old" 5 times without feeling shy.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-green">🔄</div>
        <div class="bullet-text">
          <strong>Multi-Angle Mastery</strong>
          <span class="bullet-sub">Switch from bus analogy &rarr; cricket analogy &rarr; bicycle analogy until it clicks.</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-pink">MINDSET SHIFT: From passive to interactive</span>
  </div>
"""
s9_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">EXAM IMPACT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">HOW THIS HELPS YOUR BOARD EXAM</h3>
  </div>
  <div class="panel-body-content">
    <div class="exam-benefit-card">
      <div class="benefit-header">
        <span class="benefit-tag tag-yellow">KARNATAKA BOARD SCIENCE EXAM</span>
        <span class="marks-pill">+3 TO +4 MARKS</span>
      </div>
      <p class="benefit-body">
        Karnataka State Board question papers no longer ask just: <em>"State Newton's First Law."</em> (1 mark).<br><br>
        They ask: <em>"Why do passengers fall sideways when a car takes a sharp turn? Give reason."</em> (2 marks)<br>
        <em>"Explain why dust flies off a carpet when beaten with a stick."</em> (2 marks)
      </p>
      <div class="benefit-conclusion mt-2">
        <strong>The Exam Secret:</strong> When you understand the concept deeply via analogies, application questions become child's play. You never have to panic about memorising exact textbook wording!
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-yellow">APPLICATION QUESTIONS UNLOCKED</span>
  </div>
"""
slides.append(make_slide(8, "15–30 MIN • MODULE 1: UNDERSTAND", "THE UNDERSTANDING CHECK &bull; EXAM BENEFIT", s9_left, s9_right))

# =========================================================================
# MODULE 2: CHATGPT EXAM PRACTICE (SLIDES 10 - 13)
# =========================================================================
# Slide 10: Module 2 Overview
s10_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">MODULE 2 &bull; PURPOSE</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">CHATGPT: EXAM PRACTICE &amp; SPARRING</h3>
  </div>
  <div class="panel-body-content">
    <div class="purpose-card">
      <span class="purpose-label">CORE PURPOSE:</span>
      <p class="purpose-text">Turn AI from an explanation tool into an active <strong>practice partner &amp; sparring coach</strong>.</p>
    </div>
    <div class="bullet-list-editorial mt-3">
      <div class="bullet-item">
        <div class="bullet-icon bg-red">📖</div>
        <div class="bullet-text">
          <strong>The Passive Study Illusion</strong>
          <span class="bullet-sub">Rereading notes feels good, but your brain isn't generating answers under pressure.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-green">🥊</div>
        <div class="bullet-text">
          <strong>Active Retrieval Practice</strong>
          <span class="bullet-sub">ChatGPT throws realistic board exam questions at you, waiting for your response before revealing answers.</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-yellow">SKILL 2: Active Exam Sparring</span>
  </div>
"""
s10_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">MODULE 2 CHECKLIST</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WHAT WE TOUCH IN THIS MODULE</h3>
  </div>
  <div class="panel-body-content">
    <div class="bullet-list-editorial">
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">1️⃣</div>
        <div class="bullet-text">
          <strong>Generating exam-style questions</strong>
          <span class="bullet-sub">Calibrated to Karnataka State Board Class 9 &amp; 10 blueprint.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-cyan">2️⃣</div>
        <div class="bullet-text">
          <strong>Different difficulty levels</strong>
          <span class="bullet-sub">1-mark direct, 2-mark reasoning, 3/4-mark application problems.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-pink">3️⃣</div>
        <div class="bullet-text">
          <strong>One-question-at-a-time quizzes</strong>
          <span class="bullet-sub">Preventing your eyes from cheating and reading ahead!</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-green">4️⃣</div>
        <div class="bullet-text">
          <strong>Asking AI NOT to reveal answers immediately</strong>
          <span class="bullet-sub">The golden constraint that forces real learning.</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-cyan">ACTIVE RECALL BLUEPRINT</span>
  </div>
"""
slides.append(make_slide(9, "30–45 MIN • MODULE 2: EXAM PRACTICE", "MODULE 2 OVERVIEW &bull; FROM EXPLANATION TO PRACTICE", s10_left, s10_right))

# Slide 11: The Practice Prompt & 1-at-a-time Rule
s11_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">THE PRACTICE PROMPT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">THE EXAM SPARRING PROMPT</h3>
  </div>
  <div class="panel-body-content">
    <p>Look at this exact prompt &mdash; copy it, memorize it, use it every night:</p>
    <div class="prompt-box mt-2">
      <div class="prompt-header">
        <span class="prompt-label">🥊 SPARRING PARTNER PROMPT</span>
        <button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button>
      </div>
      <div class="prompt-text">"I have studied Newton's First Law. Give me 5 exam-style questions for Karnataka State Board Class 9. Ask me ONE AT A TIME. Do NOT give me the answer until I respond."</div>
    </div>
    <div class="callout-notice mt-3">
      <strong>The Secret Constraint:</strong> "Ask me ONE AT A TIME. Don't give me the answer until I respond."
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-green">THE MAGIC CONSTRAINT: One at a time</span>
  </div>
"""
s11_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">WHY IT MATTERS</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WHY 'ONE AT A TIME' CHANGES EVERYTHING</h3>
  </div>
  <div class="panel-body-content">
    <div class="bullet-list-editorial">
      <div class="bullet-item">
        <div class="bullet-icon bg-red">👀</div>
        <div class="bullet-text">
          <strong>The Cheating Eye Reflex</strong>
          <span class="bullet-sub">If AI prints 5 questions with answers at the bottom, your eyes instinctively glance down. You think: "Oh yeah, I knew that!" (You didn't).</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-green">🧠</div>
        <div class="bullet-text">
          <strong>Active Memory Retrieval</strong>
          <span class="bullet-sub">When you must TYPE your attempt before the next question appears, your brain is forced to search memory files under exam pressure.</span>
        </div>
      </div>
    </div>
    <div class="retention-meter-card mt-3">
      <div class="meter-header">
        <span class="meter-label">RETENTION WITH ONE-AT-A-TIME SPARRING</span>
        <span class="meter-value">76%</span>
      </div>
      <div class="meter-bar">
        <div class="meter-fill" style="width: 76%; background: var(--nb-green);"></div>
      </div>
      <p class="meter-caption">Active struggle builds 4x stronger neural memory than passive reading.</p>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-yellow">NEUROSCIENCE IN ACTION</span>
  </div>
"""
slides.append(make_slide(10, "30–45 MIN • MODULE 2: EXAM PRACTICE", "THE EXAM-STYLE PROMPT &bull; 1-AT-A-TIME RULE", s11_left, s11_right))

# Slide 12: Question Tiers & Live Demo
s12_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">BOARD QUESTION TIERS</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">1-MARK &rarr; 2-MARK &rarr; 4-MARK APPLICATION</h3>
  </div>
  <div class="panel-body-content">
    <div class="tier-card-grid">
      <div class="tier-card">
        <span class="tier-tag bg-yellow">1-MARK DIRECT</span>
        <p><strong>Recall / Definition:</strong> "Define Inertia. State its SI unit."</p>
      </div>
      <div class="tier-card">
        <span class="tier-tag bg-cyan">2-MARK REASONING</span>
        <p><strong>Scientific Explanation:</strong> "Why does an athlete run some distance before taking a long jump?"</p>
      </div>
      <div class="tier-card">
        <span class="tier-tag bg-pink">4-MARK APPLICATION</span>
        <p><strong>Comprehensive Problem:</strong> "A cardboard with a coin is placed over a glass tumbler. Cardboard is flicked sharply. Coin drops inside. Explain the physics."</p>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-cyan">BOARD BLUEPRINT ALIGNED</span>
  </div>
"""
s12_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">STAGE CHALLENGE</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">LIVE 30-SECOND MIC CHALLENGE 🎙️</h3>
  </div>
  <div class="panel-body-content">
    <div class="chat-simulation-card">
      <div class="chat-msg msg-ai">
        <div class="chat-avatar">🤖</div>
        <div class="chat-bubble">
          <p><strong>ChatGPT Question 1:</strong></p>
          <p class="highlight-quote mt-1">"Why does dust fly out of a heavy woolen carpet when it is beaten with a wooden stick? Explain in 2 sentences using Newton's First Law."</p>
        </div>
      </div>
    </div>
    <div class="mic-challenge-banner mt-3">
      <span class="mic-icon">🎤</span>
      <div class="mic-text">
        <strong>Microphone to the Audience!</strong>
        <span>30 seconds on the clock. Who can give a board-ready 2-mark answer?</span>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-pink">STAGE ACTION: Student attempts live!</span>
  </div>
"""
slides.append(make_slide(11, "30–45 MIN • MODULE 2: EXAM PRACTICE", "QUESTION TYPES & DIFFICULTY &bull; 1-MARK TO APPLICATION", s12_left, s12_right))

# Slide 13: What they learn & Exam Benefit
s13_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">TAKEAWAY</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WHAT STUDENTS LEARN IN MODULE 2</h3>
  </div>
  <div class="panel-body-content">
    <div class="takeaway-big-card">
      <div class="takeaway-icon">🎯</div>
      <h4 class="takeaway-headline">DON'T JUST ASK FOR QUESTIONS &amp; READ ANSWERS. ACTUALLY ATTEMPT THEM!</h4>
      <p class="takeaway-desc">The magic is in typing or speaking YOUR answer first. When you force your brain to retrieve knowledge, you build permanent exam pathways.</p>
    </div>
    <div class="bullet-list-editorial mt-3">
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">🥊</div>
        <div class="bullet-text">
          <strong>Daily 10-Minute Sparring</strong>
          <span class="bullet-sub">After every chapter, ask ChatGPT for 5 questions, one at a time. It takes 10 minutes and solidifies the entire lesson.</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-yellow">RULE: Attempt before reading</span>
  </div>
"""
s13_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">EXAM IMPACT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">HOW THIS HELPS YOUR BOARD EXAM</h3>
  </div>
  <div class="panel-body-content">
    <div class="exam-benefit-card">
      <div class="benefit-header">
        <span class="benefit-tag tag-green">ACTIVE RETRIEVAL SUPERPOWER</span>
        <span class="marks-pill">ZERO EXAM PANIC</span>
      </div>
      <p class="benefit-body">
        Why do students panic in the exam hall? Because they only practiced <strong>reading</strong>, but the exam asks them to <strong>write from memory</strong>!
      </p>
      <div class="bullet-list-editorial mt-2">
        <div class="bullet-item">
          <div class="bullet-icon bg-green">✅</div>
          <div class="bullet-text">
            <strong>Active Practice = Real Exam Simulation</strong>
            <span class="bullet-sub">You get active practice under pressure, rather than just rereading chapters for the 10th time.</span>
          </div>
        </div>
        <div class="bullet-item">
          <div class="bullet-icon bg-cyan">⚡</div>
          <div class="bullet-text">
            <strong>Speed &amp; Confidence</strong>
            <span class="bullet-sub">In the actual paper, questions feel familiar because you've already answered them in your AI sparring sessions!</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-green">REAL EXAM STAMINA BUILT</span>
  </div>
"""
slides.append(make_slide(12, "30–45 MIN • MODULE 2: EXAM PRACTICE", "ACTIVE ATTEMPT VS PASSIVE READING &bull; EXAM BENEFIT", s13_left, s13_right))

# =========================================================================
# MODULE 3: CHATGPT CHECK & IMPROVE YOUR ANSWERS (SLIDES 14 - 17)
# =========================================================================
# Slide 14: Module 3 Overview
s14_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">MODULE 3 &bull; THE CROWN JEWEL</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">CHATGPT: CHECK &amp; IMPROVE YOUR ANSWERS</h3>
  </div>
  <div class="panel-body-content">
    <div class="purpose-card">
      <span class="purpose-label">THE MOST VALUABLE SKILL OF ALL:</span>
      <p class="purpose-text">This is a separate skill and <strong>one of the most valuable parts of the entire workshop</strong>.</p>
    </div>
    <div class="bullet-list-editorial mt-3">
      <div class="bullet-item">
        <div class="bullet-icon bg-red">🚫</div>
        <div class="bullet-text">
          <strong>The Huge Mistake Most Students Make</strong>
          <span class="bullet-sub">"ChatGPT, write the answer for me." This makes you dependent and helpless in the exam hall.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-green">✍️</div>
        <div class="bullet-text">
          <strong>The Master Way</strong>
          <span class="bullet-sub">YOU write your own raw answer first &mdash; typos, mistakes and all &mdash; and make AI audit it like a strict teacher!</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-pink">AI AS FEEDBACK TOOL &bull; NOT ANSWER WRITER</span>
  </div>
"""
s14_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">MODULE 3 CHECKLIST</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WHAT WE TOUCH IN THIS MODULE</h3>
  </div>
  <div class="panel-body-content">
    <div class="bullet-list-editorial">
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">1️⃣</div>
        <div class="bullet-text">
          <strong>Writing their own answer first</strong>
          <span class="bullet-sub">Never letting AI write the first draft.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-cyan">2️⃣</div>
        <div class="bullet-text">
          <strong>Giving that raw answer to AI</strong>
          <span class="bullet-sub">Submitting your draft for strict pedagogical inspection.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-pink">3️⃣</div>
        <div class="bullet-text">
          <strong>Asking AI to identify: Correct, Missing, Misunderstood</strong>
          <span class="bullet-sub">The 4-part teacher evaluation matrix.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-green">4️⃣</div>
        <div class="bullet-text">
          <strong>Asking for hints instead of rewritten answers</strong>
          <span class="bullet-sub">Keeping your brain in the driver's seat.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">5️⃣</div>
        <div class="bullet-text">
          <strong>Trying the answer again (The Rewrite Step)</strong>
          <span class="bullet-sub">Closing the loop and locking in full marks!</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-yellow">5 STEP EVALUATION WORKFLOW</span>
  </div>
"""
slides.append(make_slide(13, "45–60 MIN • MODULE 3: CHECK & IMPROVE", "MODULE 3 OVERVIEW &bull; THE HIGHEST VALUE SKILL", s14_left, s14_right))

# Slide 15: Inertia Case Study & Teacher Audit Prompt
s15_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">CASE STUDY: STUDENT DRAFT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">STUDENT WRITES THEIR OWN ANSWER FIRST</h3>
  </div>
  <div class="panel-body-content">
    <p>Student is asked: <em>"Define Inertia." (2 marks)</em></p>
    <div class="student-draft-card mt-2">
      <span class="draft-tag">📝 STUDENT'S RAW ATTEMPT:</span>
      <p class="draft-text">“Inertia is the tendency of an object to keep doing what it is doing unless something stops it.”</p>
    </div>
    <p class="mt-2">Good attempt! But in a Karnataka Board exam, will this get 2/2 marks? <strong>No! It gets 1/2 marks.</strong> Why? Missing scientific terminology!</p>
    <div class="prompt-box mt-2">
      <div class="prompt-header">
        <span class="prompt-label">🧑‍🏫 THE TEACHER AUDIT PROMPT</span>
        <button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button>
      </div>
      <div class="prompt-text">"Check my answer like a teacher. Tell me what I got right, what I misunderstood, and what I should improve. Don't rewrite the complete answer."</div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-cyan">RULE: 'Don't rewrite the complete answer'</span>
  </div>
"""
s15_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">AI TEACHER EVALUATION</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">STRICT BOARD TEACHER AUDIT OUTPUT</h3>
  </div>
  <div class="panel-body-content">
    <div class="audit-result-card">
      <div class="audit-row correct-row">
        <span class="audit-badge bg-green">✅ WHAT'S RIGHT:</span>
        <p>You grasped the core concept: objects resist changing their state.</p>
      </div>
      <div class="audit-row missing-row mt-2">
        <span class="audit-badge bg-red">⚠️ WHAT'S MISSING (BOARD KEYWORDS):</span>
        <p>1. Must specify: <em>"State of rest OR uniform motion in a straight line"</em><br>
        2. Must specify: <em>"External unbalanced force"</em> (not just 'something')</p>
      </div>
      <div class="audit-row hint-row mt-2">
        <span class="audit-badge bg-yellow">💡 TEACHER HINT (DO NOT REWRITE):</span>
        <p>Include the 2 specific states of motion and the exact scientific term for the external push or pull.</p>
      </div>
      <div class="score-strip mt-2">
        <span>CURRENT SCORE: <strong>1.0 / 2.0 MARKS</strong></span>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-yellow">PRECISE DIAGNOSIS &bull; NO SPOILERS</span>
  </div>
"""
slides.append(make_slide(14, "45–60 MIN • MODULE 3: CHECK & IMPROVE", "THE TEACHER AUDIT PROMPT &bull; INERTIA CASE STUDY", s15_left, s15_right))

# Slide 16: The 4 Feedback Pillars & Live Rewrite
s16_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">THE 4 PILLARS</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">THE 4 FEEDBACK PILLARS OF EXCELLENCE</h3>
  </div>
  <div class="panel-body-content">
    <div class="pillars-grid">
      <div class="pillar-box">
        <span class="p-num bg-green">1</span>
        <strong>WHAT IS CORRECT</strong>
        <p>Builds confidence; confirms your core intuition is scientifically sound.</p>
      </div>
      <div class="pillar-box">
        <span class="p-num bg-red">2</span>
        <strong>WHAT IS MISSING</strong>
        <p>Identifies crucial board scheme keywords that examiners underline in red.</p>
      </div>
      <div class="pillar-box">
        <span class="p-num bg-pink">3</span>
        <strong>WHAT IS MISUNDERSTOOD</strong>
        <p>Catches physics misconceptions before they solidify in your long-term memory.</p>
      </div>
      <div class="pillar-box">
        <span class="p-num bg-yellow">4</span>
        <strong>ACTIONABLE HINT</strong>
        <p>Gives you a stepping stone to fix it yourself, rather than handing you the fish.</p>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-pink">THE MARK-SAVING FORMULA</span>
  </div>
"""
s16_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">THE REWRITE CYCLE</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">STUDENT TRIES AGAIN: THE 2/2 REDEMPTION</h3>
  </div>
  <div class="panel-body-content">
    <p>Using the teacher hints, the student writes <strong>Version 2</strong>:</p>
    <div class="student-draft-card draft-v2 mt-2">
      <span class="draft-tag bg-green">📝 STUDENT'S REWRITTEN ANSWER (V2):</span>
      <p class="draft-text">“Inertia is the natural tendency of an object to resist any change in its <strong>state of rest or of uniform motion in a straight line</strong>, unless acted upon by an <strong>unbalanced external force</strong>.”</p>
    </div>
    <div class="audit-result-card mt-3">
      <div class="score-strip score-perfect">
        <span>NEW BOARD SCORE: <strong>2.0 / 2.0 FULL MARKS! 🌟</strong></span>
      </div>
      <p class="mt-1">Examiner Comments: <em>"All key scientific phrases present. Textbook-standard precision!"</em></p>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-green">FROM 50% TO 100% IN 60 SECONDS</span>
  </div>
"""
slides.append(make_slide(15, "45–60 MIN • MODULE 3: CHECK & IMPROVE", "THE 4 FEEDBACK PILLARS &bull; WHAT IS MISSING?", s16_left, s16_right))

# Slide 17: What they learn & Exam Benefit
s17_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">TAKEAWAY</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WHAT STUDENTS LEARN IN MODULE 3</h3>
  </div>
  <div class="panel-body-content">
    <div class="takeaway-big-card">
      <div class="takeaway-icon">🛡️</div>
      <h4 class="takeaway-headline">AI BECOMES A FEEDBACK TOOL, NOT AN ANSWER-WRITING MACHINE</h4>
      <p class="takeaway-desc">The biggest danger of AI is turning students into copy-pasters. When you use AI as an examiner who audits YOUR work, your writing skills explode.</p>
    </div>
    <div class="bullet-list-editorial mt-3">
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">🔍</div>
        <div class="bullet-text">
          <strong>Self-Correction Discipline</strong>
          <span class="bullet-sub">You learn to spot your own keyword weaknesses and tighten your scientific vocabulary.</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-yellow">CORE LESSON: Audit, don't generate</span>
  </div>
"""
s17_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">EXAM IMPACT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">HOW THIS HELPS YOUR BOARD EXAM</h3>
  </div>
  <div class="panel-body-content">
    <div class="exam-benefit-card">
      <div class="benefit-header">
        <span class="benefit-tag tag-green">PRE-EXAM DIAGNOSIS</span>
        <span class="marks-pill">+10 TO +15 MARKS</span>
      </div>
      <p class="benefit-body">
        Karnataka State Board examiners grade against an official <strong>Key Answer Scheme</strong>. If key terms like <em>"external unbalanced force"</em> are absent, they deduct 0.5 to 1 mark per question!
      </p>
      <div class="bullet-list-editorial mt-2">
        <div class="bullet-item">
          <div class="bullet-icon bg-green">🎯</div>
          <div class="bullet-text">
            <strong>Catch Weaknesses Before the Exam</strong>
            <span class="bullet-sub">They can identify their weaknesses <strong>before the actual exam</strong>, when mistakes cost zero marks &mdash; instead of in the board exam where mistakes cost ranks!</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-green">LETHAL EXAM ADVANTAGE</span>
  </div>
"""
slides.append(make_slide(16, "45–60 MIN • MODULE 3: CHECK & IMPROVE", "RETRY & MASTER &bull; EXAM BENEFIT", s17_left, s17_right))

# =========================================================================
# MODULE 4: GEMINI A SECOND AI STUDY TOOL (SLIDES 18 - 21)
# =========================================================================
# Slide 18: Module 4 Overview
s18_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">MODULE 4 &bull; PURPOSE</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">GEMINI: A SECOND AI STUDY TOOL</h3>
  </div>
  <div class="panel-body-content">
    <div class="purpose-card">
      <span class="purpose-label">PURPOSE:</span>
      <p class="purpose-text">This shouldn't be a huge separate lecture &mdash; it's about <strong>never depending on a single tool</strong>.</p>
    </div>
    <div class="bullet-list-editorial mt-3">
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">🤖</div>
        <div class="bullet-text">
          <strong>Why Learn a Second Tool?</strong>
          <span class="bullet-sub">Just like you have a school teacher and a tuition teacher who explain differently, different AI models have different cognitive styles.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-cyan">🌐</div>
        <div class="bullet-text">
          <strong>Google Gemini's Strengths</strong>
          <span class="bullet-sub">Built by Google, grounded in live web information, excellent at structured comparisons, charts, and diagrams.</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-cyan">SKILL 4: Dual-Tool Evaluation</span>
  </div>
"""
s18_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">MODULE 4 CHECKLIST</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WHAT WE TOUCH IN THIS MODULE</h3>
  </div>
  <div class="panel-body-content">
    <div class="bullet-list-editorial">
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">1️⃣</div>
        <div class="bullet-text">
          <strong>Using Gemini to explain concepts</strong>
          <span class="bullet-sub">Alternative phrasing when ChatGPT feels slightly unclear.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-cyan">2️⃣</div>
        <div class="bullet-text">
          <strong>Asking follow-up questions in Gemini</strong>
          <span class="bullet-sub">Probing deeper into real-world applications.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-pink">3️⃣</div>
        <div class="bullet-text">
          <strong>Generating practice questions</strong>
          <span class="bullet-sub">Different question formulations from a different AI engine.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-green">4️⃣</div>
        <div class="bullet-text">
          <strong>Comparing responses from ChatGPT &amp; Gemini</strong>
          <span class="bullet-sub">Head-to-head comparison on the exact same prompt!</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">5️⃣</div>
        <div class="bullet-text">
          <strong>Evaluating which explanation is clearer/useful</strong>
          <span class="bullet-sub">Developing student agency and critical evaluation.</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-pink">TOOL EVALUATION MATRIX</span>
  </div>
"""
slides.append(make_slide(17, "60–75 MIN • MODULE 4: GEMINI", "MODULE 4 OVERVIEW &bull; WHY YOU NEED A SECOND TOOL", s18_left, s18_right))

# Slide 19: Head-to-Head Battle: Electric Current
s19_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">LIVE DEMONSTRATION</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">HEAD-TO-HEAD BATTLE: ELECTRIC CURRENT</h3>
  </div>
  <div class="panel-body-content">
    <p>We give <strong>BOTH</strong> tools the exact same prompt:</p>
    <div class="prompt-box mt-2">
      <div class="prompt-header">
        <span class="prompt-label">⚡ THE BENCHMARK PROMPT</span>
        <button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button>
      </div>
      <div class="prompt-text">"Explain electric current to a Class 10 student using an everyday example."</div>
    </div>
    <div class="chat-simulation-card mt-3">
      <div class="chat-msg msg-ai">
        <div class="chat-avatar">🟢</div>
        <div class="chat-bubble">
          <p><strong>ChatGPT's Response: The Water Pipe Analogy</strong></p>
          <p class="mt-1">“Think of a copper wire like a water pipe. The battery is a water pump pushing water. <strong>Electric current is the amount of water flowing through the pipe every second</strong> (liters per second = Coulombs per second = Amperes). Resistance is a narrow pipe narrowing the flow!”</p>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-yellow">CHATGPT: Water Pipe Model</span>
  </div>
"""
s19_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">GEMINI'S RESPONSE</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">GEMINI: THE CROWDED CORRIDOR</h3>
  </div>
  <div class="panel-body-content">
    <div class="chat-simulation-card">
      <div class="chat-msg msg-ai">
        <div class="chat-avatar">🔵</div>
        <div class="chat-bubble">
          <p><strong>Gemini's Response: The School Hallway Analogy</strong></p>
          <p class="mt-1">“Imagine a school hallway packed with students. When the recess bell rings (the battery switch is closed), everyone starts marching in one direction. <strong>Electric current is how many students pass by your classroom door each second</strong>. The teachers standing in the hallway slowing them down? That's electrical resistance!”</p>
        </div>
      </div>
    </div>
    <div class="audience-poll-box mt-3">
      <strong>Audience Vote:</strong>
      <p>Which explanation did YOU understand more easily? Raise hands!</p>
      <div class="vote-result-meter mt-2">
        <div class="meter-fill" style="width: 55%; background: var(--nb-yellow);"></div>
        <span class="meter-text">Water Pipe: 55% | School Hallway: 45%</span>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-cyan">GEMINI: School Hallway Model</span>
  </div>
"""
slides.append(make_slide(18, "60–75 MIN • MODULE 4: GEMINI", "HEAD-TO-HEAD BATTLE &bull; ELECTRIC CURRENT", s19_left, s19_right))

# Slide 20: The Real Lesson & Evaluating Explanations
s20_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">THE CORE LESSON</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">NOT 'WHO WINS' &mdash; BUT 'HOW YOU LEARN'</h3>
  </div>
  <div class="panel-body-content">
    <div class="takeaway-big-card">
      <div class="takeaway-icon">⚖️</div>
      <h4 class="takeaway-headline">THE LESSON IS NOT “CHATGPT WINS” OR “GEMINI WINS”</h4>
      <p class="takeaway-desc"><strong>Different AI tools can give different responses. Learn to evaluate and use the response that actually helps YOU learn.</strong></p>
    </div>
    <div class="bullet-list-editorial mt-3">
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">🧠</div>
        <div class="bullet-text">
          <strong>Brain Diversity</strong>
          <span class="bullet-sub">Some students are mechanical thinkers (water pipes click instantly). Other students are social thinkers (crowded school corridors click instantly).</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-pink">FIND WHAT CLICKS FOR YOU</span>
  </div>
"""
s20_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">TOOL SELECTION MATRIX</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WHEN TO USE WHICH TOOL</h3>
  </div>
  <div class="panel-body-content">
    <div class="comparison-card">
      <div class="compare-col" style="background: rgba(255, 222, 89, 0.15);">
        <div class="compare-badge bg-yellow" style="color: #000;">🤖 CHATGPT</div>
        <p><strong>Best For:</strong></p>
        <p>&bull; Socratic back-and-forth conversation</p>
        <p>&bull; Auditing and checking your written answers</p>
        <p>&bull; Step-by-step interactive quizzes</p>
        <p>&bull; Analogies tailored to your hobby</p>
      </div>
      <div class="compare-versus-badge">+</div>
      <div class="compare-col" style="background: rgba(0, 194, 203, 0.15);">
        <div class="compare-badge bg-cyan" style="color: #000;">✨ GOOGLE GEMINI</div>
        <p><strong>Best For:</strong></p>
        <p>&bull; Real-time web search and current facts</p>
        <p>&bull; Formatting comparisons into neat tables</p>
        <p>&bull; Alternative explanations when ChatGPT is dense</p>
        <p>&bull; Integrating with Google Docs &amp; Drive</p>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-green">A COMPLETE TWO-TOOL ARSENAL</span>
  </div>
"""
slides.append(make_slide(19, "60–75 MIN • MODULE 4: GEMINI", "CHATGPT VS GEMINI &bull; EVALUATING RESPONSES", s20_left, s20_right))

# Slide 21: What they learn & Exam Benefit
s21_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">TAKEAWAY</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WHAT STUDENTS LEARN IN MODULE 4</h3>
  </div>
  <div class="panel-body-content">
    <div class="takeaway-big-card">
      <div class="takeaway-icon">🔓</div>
      <h4 class="takeaway-headline">STUDENTS ARE NOT DEPENDENT ON ONE TOOL</h4>
      <p class="takeaway-desc">If you only know one AI tool, you get trapped when it servers go down or when its explanation doesn't make sense to you. Knowing two tools makes you autonomous.</p>
    </div>
    <div class="bullet-list-editorial mt-3">
      <div class="bullet-item">
        <div class="bullet-icon bg-cyan">🔄</div>
        <div class="bullet-text">
          <strong>The Second Opinion Advantage</strong>
          <span class="bullet-sub">Just like a patient asks for a second doctor's opinion, a student can ask for a second AI's perspective on tough physics or chemistry topics.</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-yellow">TOOL AGNOSTIC INDEPENDENCE</span>
  </div>
"""
s21_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">EXAM IMPACT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">HOW THIS HELPS YOUR BOARD EXAM</h3>
  </div>
  <div class="panel-body-content">
    <div class="exam-benefit-card">
      <div class="benefit-header">
        <span class="benefit-tag tag-green">NO DEAD ENDS IN STUDYING</span>
        <span class="marks-pill">100% CONCEPT RESOLUTION</span>
      </div>
      <p class="benefit-body">
        Every year, students get stuck on difficult Class 10 concepts like <em>Electromagnetic Induction, Periodic Trends, or Carbon Compounds</em>, and give up because one book explanation confused them.
      </p>
      <div class="bullet-list-editorial mt-2">
        <div class="bullet-item">
          <div class="bullet-icon bg-green">🎯</div>
          <div class="bullet-text">
            <strong>Cross-Checking Clarity</strong>
            <span class="bullet-sub">Students learn how to use another major AI assistant for explanation, practice, and exploration &mdash; eliminating mental roadblocks completely!</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-green">ELIMINATES STUDY ROADBLOCKS</span>
  </div>
"""
slides.append(make_slide(20, "60–75 MIN • MODULE 4: GEMINI", "THE TWO-TOOL ADVANTAGE &bull; EXAM BENEFIT", s21_left, s21_right))

# =========================================================================
# MODULE 5: NOTEBOOKLM STUDY YOUR ACTUAL MATERIAL (SLIDES 22 - 26)
# =========================================================================
# Slide 22: Module 5 Overview
s22_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">MODULE 5 &bull; THE SPECIALIST</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">NOTEBOOKLM: STUDY YOUR ACTUAL MATERIAL</h3>
  </div>
  <div class="panel-body-content">
    <div class="purpose-card">
      <span class="purpose-label">THE MOST DISTINCT MODULE:</span>
      <p class="purpose-text">This is the most distinct module of the workshop. It solves the #1 flaw of generic AI tools.</p>
    </div>
    <div class="bullet-list-editorial mt-3">
      <div class="bullet-item">
        <div class="bullet-icon bg-red">🌐</div>
        <div class="bullet-text">
          <strong>The Danger of Generic AI</strong>
          <span class="bullet-sub">ChatGPT knows everything in the universe, so it often cites US/UK syllabus facts that are NOT in your Karnataka Board exam!</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-green">📚</div>
        <div class="bullet-text">
          <strong>The NotebookLM Superpower</strong>
          <span class="bullet-sub">NotebookLM ONLY reads the PDFs, textbook chapters, and teacher notes YOU upload. It answers strictly from your syllabus!</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-yellow">SKILL 5: Grounded Syllabus AI</span>
  </div>
"""
s22_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">MODULE 5 CHECKLIST</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WHAT WE TOUCH IN THIS MODULE</h3>
  </div>
  <div class="panel-body-content">
    <div class="bullet-list-editorial">
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">1️⃣</div>
        <div class="bullet-text">
          <strong>What NotebookLM is</strong>
          <span class="bullet-sub">Google's source-grounded research assistant designed for students and researchers.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-cyan">2️⃣</div>
        <div class="bullet-text">
          <strong>Adding study material</strong>
          <span class="bullet-sub">Uploading Karnataka State Board textbook PDFs and teacher class notes.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-pink">3️⃣</div>
        <div class="bullet-text">
          <strong>Finding important concepts</strong>
          <span class="bullet-sub">Extracting high-yield topics directly from approved chapter text.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-green">4️⃣</div>
        <div class="bullet-text">
          <strong>Simplifying difficult sections &amp; Creating revision material</strong>
          <span class="bullet-sub">Generating 1-page summaries and formulas with SI units.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">5️⃣</div>
        <div class="bullet-text">
          <strong>Quizzing yourself using only your material</strong>
          <span class="bullet-sub">Every quiz question has clickable textbook page citations!</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-cyan">4 CORE WORKFLOWS</span>
  </div>
"""
slides.append(make_slide(21, "75–90 MIN • MODULE 5: NOTEBOOKLM", "MODULE 5 OVERVIEW &bull; GROUNDED IN YOUR TEXTBOOK", s22_left, s22_right))

# Slide 23: Workflows 1 & 2 (Extract & Simplify)
s23_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">WORKFLOW 1: EXTRACT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">IDENTIFY KEY EXAM CONCEPTS</h3>
  </div>
  <div class="panel-body-content">
    <p>Upload your approved Karnataka Board chapter PDF to NotebookLM, then ask:</p>
    <div class="prompt-box mt-2">
      <div class="prompt-header">
        <span class="prompt-label">📑 WORKFLOW 1 PROMPT</span>
        <button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button>
      </div>
      <div class="prompt-text">"Based only on this study material, identify the key concepts I should understand for my exam."</div>
    </div>
    <div class="bullet-list-editorial mt-3">
      <div class="bullet-item">
        <div class="bullet-icon bg-green">🎯</div>
        <div class="bullet-text">
          <strong>Zero Off-Syllabus Fluff</strong>
          <span class="bullet-sub">Pulls only the laws, definitions, and formulas that exist inside your actual school book!</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-pink">WORKFLOW 1: Key Concept Extraction</span>
  </div>
"""
s23_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">WORKFLOW 2: SIMPLIFY</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">SIMPLIFY DIFFICULT SECTIONS</h3>
  </div>
  <div class="panel-body-content">
    <p>When a specific section in the textbook feels impossible to understand:</p>
    <div class="prompt-box mt-2">
      <div class="prompt-header">
        <span class="prompt-label">🔍 WORKFLOW 2 PROMPT</span>
        <button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button>
      </div>
      <div class="prompt-text">"Explain this difficult section in simpler language."</div>
    </div>
    <div class="chat-simulation-card mt-3">
      <div class="chat-msg msg-ai">
        <div class="chat-avatar">📖</div>
        <div class="chat-bubble">
          <p><strong>NotebookLM Output:</strong></p>
          <p class="mt-1">“Here is Section 12.4 (Resistors in Series) simplified into 3 clear steps without changing your textbook's variables (R1, R2, R3). Total voltage divides across resistors, but the current stays identical through every single resistor!”</p>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-cyan">WORKFLOW 2: Jargon Translation</span>
  </div>
"""
slides.append(make_slide(22, "75–90 MIN • MODULE 5: NOTEBOOKLM", "WORKFLOW 1 & 2 &bull; EXTRACT CONCEPTS & SIMPLIFY SECTIONS", s23_left, s23_right))

# Slide 24: Workflow 3 (Revision Guide)
s24_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">WORKFLOW 3: REVISION</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">CREATE A 1-PAGE REVISION GUIDE</h3>
  </div>
  <div class="panel-body-content">
    <p>The night before the exam, you don't have time to re-read 40 pages of text:</p>
    <div class="prompt-box mt-2">
      <div class="prompt-header">
        <span class="prompt-label">⚡ WORKFLOW 3 PROMPT</span>
        <button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button>
      </div>
      <div class="prompt-text">"Create a concise revision guide from this material."</div>
    </div>
    <div class="bullet-list-editorial mt-3">
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">📋</div>
        <div class="bullet-text">
          <strong>Instant High-Yield Summary</strong>
          <span class="bullet-sub">Compacts formulas, SI units, diagram labels, and core laws into a single printable review page.</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-yellow">WORKFLOW 3: Cheat-Sheet Generator</span>
  </div>
"""
s24_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">REVISION SHEET PREVIEW</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">HIGH-YIELD REVISION SHEET OUTPUT</h3>
  </div>
  <div class="panel-body-content">
    <div class="revision-sheet-preview">
      <div class="sheet-header">
        <strong>CHAPTER 12: ELECTRICITY &bull; 1-PAGE BOARD SUMMARY</strong>
      </div>
      <div class="sheet-body">
        <p><strong>1. Ohm's Law:</strong> V = IR &bull; Constant temperature condition is mandatory!</p>
        <p><strong>2. Series vs Parallel:</strong></p>
        <p>&bull; Series: I is constant, V = V1 + V2. Rs = R1 + R2</p>
        <p>&bull; Parallel: V is constant, I = I1 + I2. 1/Rp = 1/R1 + 1/R2</p>
        <p><strong>3. Joule's Law of Heating:</strong> H = I&sup2;Rt (Units: Joules)</p>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-green">15-SECOND REVISION SHEET</span>
  </div>
"""
slides.append(make_slide(23, "75–90 MIN • MODULE 5: NOTEBOOKLM", "WORKFLOW 3 &bull; THE 1-PAGE REVISION GUIDE", s24_left, s24_right))

# Slide 25: Workflow 4 (Sourced Quiz with Citations)
s25_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">WORKFLOW 4: SOURCED QUIZ</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">QUIZ ME USING ONLY THIS MATERIAL</h3>
  </div>
  <div class="panel-body-content">
    <p>Now make NotebookLM conduct an official examination from your uploaded text:</p>
    <div class="prompt-box mt-2">
      <div class="prompt-header">
        <span class="prompt-label">🎯 WORKFLOW 4 PROMPT</span>
        <button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button>
      </div>
      <div class="prompt-text">"Quiz me one question at a time using only this material."</div>
    </div>
    <div class="bullet-list-editorial mt-3">
      <div class="bullet-item">
        <div class="bullet-icon bg-pink">🎯</div>
        <div class="bullet-text">
          <strong>100% In-Syllabus Questions</strong>
          <span class="bullet-sub">Every single question comes directly from your school textbook's examples, activities, and exercises!</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-pink">WORKFLOW 4: Grounded Quizzing</span>
  </div>
"""
s25_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">CITATION MAGIC</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">CLICKABLE PAGE NUMBER CITATIONS</h3>
  </div>
  <div class="panel-body-content">
    <div class="chat-simulation-card">
      <div class="chat-msg msg-ai">
        <div class="chat-avatar">📖</div>
        <div class="chat-bubble">
          <p><strong>NotebookLM:</strong> Correct! You stated that resistivity depends on temperature and material nature.</p>
          <p class="mt-1 citation-pill">Source: [Page 207, Paragraph 2 of your uploaded Science_Ch12.pdf]</p>
        </div>
      </div>
    </div>
    <div class="citation-demo-box mt-3">
      <span class="demo-icon">🔍</span>
      <div class="demo-text">
        <strong>The Clickable Citation Chip:</strong>
        <span>Click the source chip &rarr; NotebookLM instantly highlights the exact sentence in your textbook viewer! Zero hallucinations!</span>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-cyan">100% GROUNDED TRUTH</span>
  </div>
"""
slides.append(make_slide(24, "75–90 MIN • MODULE 5: NOTEBOOKLM", "WORKFLOW 4 &bull; SOURCED QUIZ WITH CITATIONS", s25_left, s25_right))

# Slide 26: What they learn & Exam Benefit (5-Step Study Flywheel)
s26_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">TAKEAWAY</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WHAT STUDENTS LEARN IN MODULE 5</h3>
  </div>
  <div class="panel-body-content">
    <div class="takeaway-big-card">
      <div class="takeaway-icon">💎</div>
      <h4 class="takeaway-headline">THEIR OWN STUDY MATERIAL BECOMES THE FOUNDATION OF THE AI INTERACTION</h4>
      <p class="takeaway-desc">Instead of asking generic questions to the open internet, you anchor the AI directly to your syllabus.</p>
    </div>
    <div class="flywheel-pill-row mt-3">
      <span class="fw-pill bg-yellow">UNDERSTAND</span> &rarr;
      <span class="fw-pill bg-cyan">EXTRACT</span> &rarr;
      <span class="fw-pill bg-pink">REVISE</span> &rarr;
      <span class="fw-pill bg-green">PRACTISE</span> &rarr;
      <span class="fw-pill bg-yellow">TEST</span>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-yellow">THE 5-STEP STUDY FLYWHEEL</span>
  </div>
"""
s26_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">EXAM IMPACT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">HOW THIS HELPS YOUR BOARD EXAM</h3>
  </div>
  <div class="panel-body-content">
    <div class="exam-benefit-card">
      <div class="benefit-header">
        <span class="benefit-tag tag-green">SYLLABUS PRECISION</span>
        <span class="marks-pill">ZERO WASTED TIME</span>
      </div>
      <p class="benefit-body">
        Instead of asking generic AI questions, they can use their <strong>actual syllabus material</strong> to:
      </p>
      <div class="bullet-list-editorial mt-2">
        <div class="bullet-item">
          <div class="bullet-icon bg-green">✅</div>
          <div class="bullet-text">
            <strong>Understand &rarr; Extract &rarr; Revise &rarr; Practise &rarr; Test</strong>
            <span class="bullet-sub">Every minute spent studying is 100% aligned with the exact questions the Board paper setters create from your textbook!</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-green">PERFECT SYLLABUS ALIGNMENT</span>
  </div>
"""
slides.append(make_slide(25, "75–90 MIN • MODULE 5: NOTEBOOKLM", "THE 5-STEP STUDY LOOP &bull; EXAM BENEFIT", s26_left, s26_right))

# =========================================================================
# MODULE 6: PROMPTING HOW TO GET BETTER RESULTS (SLIDES 27 - 30)
# =========================================================================
# Slide 27: Module 6 Overview (Why taught now)
s27_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">MODULE 6 &bull; TIMING MATTERS</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">PROMPTING: HOW TO GET BETTER RESULTS</h3>
  </div>
  <div class="panel-body-content">
    <div class="purpose-card">
      <span class="purpose-label">PEDAGOGICAL DESIGN:</span>
      <p class="purpose-text">This should be taught <strong>AFTER they have already seen the tools</strong>, not as a theoretical introduction!</p>
    </div>
    <div class="bullet-list-editorial mt-3">
      <div class="bullet-item">
        <div class="bullet-icon bg-red">🥱</div>
        <div class="bullet-text">
          <strong>Why Teaching Prompting First Fails</strong>
          <span class="bullet-sub">If you teach prompt syntax at 9:00 AM, students zone out because it feels like abstract grammar rules.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-green">💡</div>
        <div class="bullet-text">
          <strong>Why Teaching Prompting Now Works</strong>
          <span class="bullet-sub">Now that they've seen ChatGPT, Gemini, and NotebookLM in action, they understand WHY specific wording unlocks 10x better answers!</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-yellow">SKILL 6: Master Prompt Architecture</span>
  </div>
"""
s27_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">GARBAGE IN &rarr; GARBAGE OUT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">AI IS ONLY AS SMART AS YOUR INSTRUCTIONS</h3>
  </div>
  <div class="panel-body-content">
    <div class="bullet-list-editorial">
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">🎯</div>
        <div class="bullet-text">
          <strong>Vague Prompt = Generic Noise</strong>
          <span class="bullet-sub">"Tell me about electricity" gets a boring Wikipedia dump that helps no one pass an exam.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-green">⚡</div>
        <div class="bullet-text">
          <strong>Targeted Prompt = Precision Tutoring</strong>
          <span class="bullet-sub">Telling AI who you are, what you need, and what rules to follow produces board-exam gold in 3 seconds!</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-cyan">YOU ARE THE PILOT &bull; AI IS THE ENGINE</span>
  </div>
"""
slides.append(make_slide(26, "90–105 MIN • MODULE 6: PROMPTING", "MODULE 6 OVERVIEW &bull; NOW THAT YOU KNOW THE TOOLS", s27_left, s27_right))

# Slide 28: The 5-Part Master Formula
s28_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">THE 5 INGREDIENTS</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">THE 5-PART MASTER FORMULA</h3>
  </div>
  <div class="panel-body-content">
    <p>Students learn five things to include in every study prompt:</p>
    <div class="formula-stack-editorial mt-2">
      <div class="f-item">
        <span class="f-tag bg-yellow">1. WHO</span>
        <div class="f-info"><strong>Who am I?</strong> &rarr; <em>"Class 10 Karnataka State Board student"</em></div>
      </div>
      <div class="f-item">
        <span class="f-tag bg-cyan">2. WHAT</span>
        <div class="f-info"><strong>What do I want?</strong> &rarr; <em>"Explain / Practise / Check / Revise"</em></div>
      </div>
      <div class="f-item">
        <span class="f-tag bg-pink">3. CONTEXT</span>
        <div class="f-info"><strong>What am I studying?</strong> &rarr; <em>"Electricity chapter"</em></div>
      </div>
      <div class="f-item">
        <span class="f-tag bg-green">4. HOW</span>
        <div class="f-info"><strong>How should you help?</strong> &rarr; <em>"Simple language + everyday example"</em></div>
      </div>
      <div class="f-item">
        <span class="f-tag bg-red">5. RULE</span>
        <div class="f-info"><strong>What shouldn't AI do?</strong> &rarr; <em>"Don't give the answer before I try!"</em></div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-pink">WHO + WHAT + CONTEXT + HOW + RULE</span>
  </div>
"""
s28_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">VISUAL BLUEPRINT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">HOW THE PIECES SNAP TOGETHER</h3>
  </div>
  <div class="panel-body-content">
    <div class="lego-formula-card">
      <div class="lego-brick brick-who">[WHO: Class 10 State Board Student]</div>
      <div class="lego-connector">+</div>
      <div class="lego-brick brick-context">[CONTEXT: Science Exam &bull; Electric Current]</div>
      <div class="lego-connector">+</div>
      <div class="lego-brick brick-what">[WHAT: Explain &amp; Test]</div>
      <div class="lego-connector">+</div>
      <div class="lego-brick brick-how">[HOW: Simple language + everyday example]</div>
      <div class="lego-connector">+</div>
      <div class="lego-brick brick-rule">[RULE: Don't give answers until I try!]</div>
    </div>
    <p class="mt-3 text-center"><strong>Result:</strong> An unbreakable prompt that produces the exact tutoring you need!</p>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-green">THE UNIVERSAL PROMPT ARCHITECTURE</span>
  </div>
"""
slides.append(make_slide(27, "90–105 MIN • MODULE 6: PROMPTING", "THE 5-PART MASTER FORMULA &bull; WHO, WHAT, CONTEXT, HOW, RULE", s28_left, s28_right))

# Slide 29: Bad vs Better Showdown (Electricity)
s29_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-red">THE TERRIBLE PROMPT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">BAD: "EXPLAIN ELECTRICITY."</h3>
  </div>
  <div class="panel-body-content">
    <div class="bad-prompt-preview">
      <span class="bad-label">❌ WHAT 95% OF STUDENTS TYPE:</span>
      <div class="code-box-bad">"Explain electricity."</div>
    </div>
    <div class="bullet-list-editorial mt-3">
      <div class="bullet-item">
        <div class="bullet-icon bg-red">💀</div>
        <div class="bullet-text">
          <strong>The Terrible Result</strong>
          <span class="bullet-sub">AI dumps 8 paragraphs discussing Benjamin Franklin, electromagnetic field tensors, Coulomb's constant, and power plant distribution grids!</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">❌</div>
        <div class="bullet-text">
          <strong>Zero Board Value</strong>
          <span class="bullet-sub">None of it is formatted for a Karnataka State Board 2-mark or 4-mark question. Student gives up and closes laptop.</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-red">THE LAZY PROMPT DISASTER</span>
  </div>
"""
s29_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">THE MASTER PROMPT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">BETTER: THE 5-PART FORMULA IN ACTION</h3>
  </div>
  <div class="panel-body-content">
    <div class="prompt-box">
      <div class="prompt-header">
        <span class="prompt-label">🌟 5-PART MASTER PROMPT</span>
        <button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button>
      </div>
      <div class="prompt-text">"I'm a Class 10 Karnataka State Board student preparing for my Science exam. I don't understand electric current. Explain it in simple language using an everyday example. Then ask me two questions to check whether I understood. Don't give me the answers until I try."</div>
    </div>
    <div class="bullet-list-editorial mt-2">
      <div class="bullet-item">
        <div class="bullet-icon bg-green">🏆</div>
        <div class="bullet-text">
          <strong>The Perfect Result</strong>
          <span class="bullet-sub">Precise, grade-appropriate analogy (water pipe or hallway), clear formula (I = Q/t), followed by 2 check questions waiting for the student's attempt!</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-green">SAME AI &bull; 1000x BETTER TUTORING</span>
  </div>
"""
slides.append(make_slide(28, "90–105 MIN • MODULE 6: PROMPTING", "BEFORE & AFTER BATTLE &bull; ELECTRICITY PROMPT", s29_left, s29_right))

# Slide 30: What they learn & Exam Benefit
s30_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">TAKEAWAY</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WHAT STUDENTS LEARN IN MODULE 6</h3>
  </div>
  <div class="panel-body-content">
    <div class="takeaway-big-card">
      <div class="takeaway-icon">🎯</div>
      <h4 class="takeaway-headline">STUDENTS LEARN HOW TO GET USEFUL, TARGETED STUDY HELP INSTEAD OF GENERIC AI RESPONSES</h4>
      <p class="takeaway-desc">Prompting is not programming; it is communication. By setting context, expectations, and rules, you command AI to serve YOUR learning goals.</p>
    </div>
    <div class="bullet-list-editorial mt-3">
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">🛑</div>
        <div class="bullet-text">
          <strong>Negative Constraints are King</strong>
          <span class="bullet-sub">Adding rules like <em>"Don't give me the answer until I try"</em> stops AI from spoiling the learning experience!</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-yellow">COMMUNICATION MASTERY</span>
  </div>
"""
s30_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">EXAM IMPACT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">HOW THIS HELPS YOUR BOARD EXAM</h3>
  </div>
  <div class="panel-body-content">
    <div class="exam-benefit-card">
      <div class="benefit-header">
        <span class="benefit-tag tag-green">EFFICIENCY &amp; RETENTION</span>
        <span class="marks-pill">2X STUDY SPEED</span>
      </div>
      <p class="benefit-body">
        Average students spend 45 minutes sifting through confusing websites and long videos trying to understand one concept.
      </p>
      <div class="bullet-list-editorial mt-2">
        <div class="bullet-item">
          <div class="bullet-icon bg-green">⚡</div>
          <div class="bullet-text">
            <strong>Targeted Help in 60 Seconds</strong>
            <span class="bullet-sub">With the 5-Part Formula, students get customized, board-level explanations and quizzes in 60 seconds flat &mdash; leaving maximum time for real practice.</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-green">HOURS OF STUDY TIME SAVED</span>
  </div>
"""
slides.append(make_slide(29, "90–105 MIN • MODULE 6: PROMPTING", "PROMPT UPGRADE &bull; EXAM BENEFIT", s30_left, s30_right))

# =========================================================================
# MODULE 7: FINAL MANDATORY MODULE - AI VERIFICATION (SLIDES 31 - 33)
# =========================================================================
# Slide 31: Module 7 Overview (AI Can Be Wrong)
s31_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-red">MANDATORY MODULE &bull; CAUTION</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">FINAL MODULE: AI VERIFICATION</h3>
  </div>
  <div class="panel-body-content">
    <div class="purpose-card" style="border-left-color: var(--nb-red);">
      <span class="purpose-label" style="color: var(--nb-red);">MANDATORY TRUTH:</span>
      <p class="purpose-text"><strong>AI CAN BE WRONG.</strong> Sometimes it speaks with 100% supreme confidence while stating complete falsehoods!</p>
    </div>
    <div class="bullet-list-editorial mt-3">
      <div class="bullet-item">
        <div class="bullet-icon bg-red">⚠️</div>
        <div class="bullet-text">
          <strong>The Hallucination Danger</strong>
          <span class="bullet-sub">AI doesn't "know" facts; it predicts plausible-sounding words. It can invent formulas, misquote history, or confuse chemical symbols.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">🛑</div>
        <div class="bullet-text">
          <strong>Never Trust Blindly</strong>
          <span class="bullet-sub">Confident tone does NOT equal correctness!</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-red">CRITICAL FACT: Confident ≠ Correct</span>
  </div>
"""
s31_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">EXAM RISK</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WHAT HAPPENS IF YOU WRITE AN AI ERROR?</h3>
  </div>
  <div class="panel-body-content">
    <div class="danger-case-box">
      <div class="danger-header">
        <span class="danger-tag bg-red">BOARD EXAM REALITY</span>
      </div>
      <p class="mt-2">If you write an incorrect AI-generated formula or explanation on your Karnataka State Board answer sheet:</p>
      <div class="audit-row mt-2" style="background: rgba(255, 51, 102, 0.15); border-left: 4px solid var(--nb-red); padding: 0.75rem;">
        <strong>The Board Examiner's Red Pen: 0 MARKS.</strong>
        <p class="mt-1">You cannot write in the margin: <em>"Sir, ChatGPT told me this!"</em></p>
      </div>
      <p class="mt-2"><strong>The Golden Lesson:</strong> You are 100% responsible for whatever you write in the exam hall. AI is just a sparring coach.</p>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-yellow">ZERO EXCUSES IN BOARD EXAMS</span>
  </div>
"""
slides.append(make_slide(30, "105–115 MIN • PART 7: AI VERIFICATION", "CAN YOU TRUST AI? &bull; CONFIDENT ≠ CORRECT", s31_left, s31_right))

# Slide 32: Stop, Check, Think Protocol
s32_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">THE PROTOCOL</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">STOP &bull; CHECK &bull; THINK</h3>
  </div>
  <div class="panel-body-content">
    <p>When using AI for your exams, follow this mandatory 3-step filter:</p>
    <div class="protocol-card-stack mt-2">
      <div class="p-card bg-red-tint">
        <div class="p-icon bg-red">🛑</div>
        <div class="p-text">
          <strong>1. STOP</strong>
          <span>Don't blindly accept any explanation, formula, or dates without testing it.</span>
        </div>
      </div>
      <div class="p-card bg-yellow-tint mt-2">
        <div class="p-icon bg-yellow">🔍</div>
        <div class="p-text">
          <strong>2. CHECK</strong>
          <span>Verify important facts against your official textbook and teacher's class notes.</span>
        </div>
      </div>
      <div class="p-card bg-green-tint mt-2">
        <div class="p-icon bg-green">🧠</div>
        <div class="p-text">
          <strong>3. THINK</strong>
          <span>Does this match your intuition and what you were taught in school?</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-yellow">THE 3-STEP SAFETY BRAKE</span>
  </div>
"""
s32_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">THE 3 VERIFICATION SOURCES</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">THE 3 GOLD STANDARDS OF TRUTH</h3>
  </div>
  <div class="panel-body-content">
    <div class="bullet-list-editorial">
      <div class="bullet-item">
        <div class="bullet-icon bg-green">📘</div>
        <div class="bullet-text">
          <strong>1. Official Textbook (Supreme Court of Exams)</strong>
          <span class="bullet-sub">Karnataka State Board textbooks are the ultimate grading authority. If AI conflicts with the book, the book WINS 100% of the time!</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">🧑‍🏫</div>
        <div class="bullet-text">
          <strong>2. Teacher's Class Notes</strong>
          <span class="bullet-sub">Your teachers know the exact marking scheme and step-allocation used by board evaluators.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-pink">📄</div>
        <div class="bullet-text">
          <strong>3. Past 5 Years Board Question Papers</strong>
          <span class="bullet-sub">The blueprint for question phrasing, mark distributions, and standard diagrams.</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-cyan">TRUTH IS IN YOUR SYLLABUS</span>
  </div>
"""
slides.append(make_slide(31, "105–115 MIN • PART 7: AI VERIFICATION", "STOP. CHECK. THINK. &bull; THE VERIFICATION PROTOCOL", s32_left, s32_right))

# Slide 33: 5 Responsible AI Rules & Exam Benefit
s33_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">CODE OF CONDUCT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">THE 5 RESPONSIBLE AI RULES FOR STUDENTS</h3>
  </div>
  <div class="panel-body-content">
    <div class="bullet-list-editorial">
      <div class="bullet-item">
        <div class="bullet-icon bg-red">1️⃣</div>
        <div class="bullet-text">
          <strong>Check against textbook</strong>
          <span class="bullet-sub">Always cross-verify formulas and definitions.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-yellow">2️⃣</div>
        <div class="bullet-text">
          <strong>Check teacher's notes</strong>
          <span class="bullet-sub">Respect the school's approved methodology and steps.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-cyan">3️⃣</div>
        <div class="bullet-text">
          <strong>Check reliable sources</strong>
          <span class="bullet-sub">Use NotebookLM grounded in approved PDFs when in doubt.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-pink">4️⃣</div>
        <div class="bullet-text">
          <strong>Don't blindly copy</strong>
          <span class="bullet-sub">Never submit AI-generated text as your own homework.</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-green">5️⃣</div>
        <div class="bullet-text">
          <strong>Don't put private information into AI</strong>
          <span class="bullet-sub">Never enter phone numbers, addresses, passwords, or personal photos!</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-green">THE 5 ETHICAL PILLARS</span>
  </div>
"""
s33_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">EXAM IMPACT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">HOW VERIFICATION PROTECTS YOUR EXAM</h3>
  </div>
  <div class="panel-body-content">
    <div class="exam-benefit-card">
      <div class="benefit-header">
        <span class="benefit-tag tag-yellow">ZERO ACCIDENTAL BLUNDERS</span>
        <span class="marks-pill">ACADEMIC HONESTY</span>
      </div>
      <p class="benefit-body">
        <strong>The Ultimate Exam Benefit:</strong> Students don't accidentally study an incorrect AI-generated explanation.
      </p>
      <div class="bullet-list-editorial mt-2">
        <div class="bullet-item">
          <div class="bullet-icon bg-green">🛡️</div>
          <div class="bullet-text">
            <strong>Critical Thinking Champion</strong>
            <span class="bullet-sub">You graduate from a passive gullible consumer into an elite, discerning student who interrogates information critically.</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-yellow">SAFETY &bull; ETHICS &bull; INTEGRITY</span>
  </div>
"""
slides.append(make_slide(32, "105–115 MIN • PART 7: AI VERIFICATION", "RESPONSIBLE AI: FIVE RULES &bull; EXAM BENEFIT", s33_left, s33_right))

# =========================================================================
# LAB BRIEFING & FINALE (SLIDES 34 - 36)
# =========================================================================
# Slide 34: Auditorium -> Lab Transition
s34_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">THE COMPLETE CURRICULUM</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">RECAP: THE COMPLETE 7-SKILL STACK</h3>
  </div>
  <div class="panel-body-content">
    <div class="bullet-list-editorial">
      <div class="bullet-item"><div class="bullet-icon bg-yellow">1</div><div class="bullet-text"><strong>UNDERSTAND:</strong> ChatGPT/Gemini &rarr; explain difficult concepts</div></div>
      <div class="bullet-item"><div class="bullet-icon bg-cyan">2</div><div class="bullet-text"><strong>PRACTISE:</strong> ChatGPT/Gemini &rarr; generate exam questions &amp; quizzes</div></div>
      <div class="bullet-item"><div class="bullet-icon bg-pink">3</div><div class="bullet-text"><strong>CHECK:</strong> ChatGPT &rarr; evaluate their own answers</div></div>
      <div class="bullet-item"><div class="bullet-icon bg-green">4</div><div class="bullet-text"><strong>IMPROVE:</strong> AI &rarr; identify mistakes &rarr; student retries</div></div>
      <div class="bullet-item"><div class="bullet-icon bg-yellow">5</div><div class="bullet-text"><strong>STUDY YOUR MATERIAL:</strong> NotebookLM &rarr; textbook &rarr; revision + quiz</div></div>
      <div class="bullet-item"><div class="bullet-icon bg-cyan">6</div><div class="bullet-text"><strong>ASK BETTER:</strong> Prompting &rarr; get useful, targeted AI responses</div></div>
      <div class="bullet-item"><div class="bullet-icon bg-red">7</div><div class="bullet-text"><strong>VERIFY:</strong> AI can be wrong &rarr; check important information</div></div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-yellow">THE 7-PILLAR FRAMEWORK</span>
  </div>
"""
s34_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">LAB TRANSITION</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">AUDITORIUM (I TEACH) &rarr; LAB (YOU DO!)</h3>
  </div>
  <div class="panel-body-content">
    <div class="takeaway-big-card">
      <div class="takeaway-icon">🚀</div>
      <h4 class="takeaway-headline">ENOUGH WATCHING. TIME TO BUILD YOUR SKILLS!</h4>
      <p class="takeaway-desc">In the auditorium, you watched me demonstrate. In the computer lab, YOU take the controls!</p>
    </div>
    <div class="bullet-list-editorial mt-3">
      <div class="bullet-item">
        <div class="bullet-icon bg-cyan">💻</div>
        <div class="bullet-text">
          <strong>Workstation Ready</strong>
          <span class="bullet-sub">Pair up or solo at your assigned terminal. Open the Student Lab mode right now!</span>
        </div>
      </div>
      <div class="bullet-item">
        <div class="bullet-icon bg-green">⏱️</div>
        <div class="bullet-text">
          <strong>60 Minutes of Hands-On Missions</strong>
          <span class="bullet-sub">Timer starts as soon as we enter the lab. Mentors will be walking around to assist!</span>
        </div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-green">PHASE 2 BEGINS!</span>
  </div>
"""
slides.append(make_slide(33, "115–120 MIN • LAB TRANSITION", "AUDITORIUM (TEACH) &rarr; COMPUTER LAB (YOU DO)", s34_left, s34_right))

# Slide 35: 7 Lab Missions Summary
s35_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">LAB MISSIONS 1 TO 4</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">YOUR 60-MINUTE LAB CHALLENGE (PART 1)</h3>
  </div>
  <div class="panel-body-content">
    <div class="mission-preview-list">
      <div class="m-card">
        <span class="m-num bg-yellow">M1</span>
        <div class="m-desc"><strong>The School Bus Prompt:</strong> Ask ChatGPT to explain Newton's First Law using the bus analogy + test question.</div>
      </div>
      <div class="m-card mt-2">
        <span class="m-num bg-cyan">M2</span>
        <div class="m-desc"><strong>The Exam Sparring Drill:</strong> Trigger a 5-question one-at-a-time quiz. Attempt Question 1 before looking!</div>
      </div>
      <div class="m-card mt-2">
        <span class="m-num bg-pink">M3</span>
        <div class="m-desc"><strong>Teacher Audit &amp; Rewrite:</strong> Submit your raw inertia answer, get evaluated, apply hints, score 2/2!</div>
      </div>
      <div class="m-card mt-2">
        <span class="m-num bg-green">M4</span>
        <div class="m-desc"><strong>ChatGPT vs Gemini Battle:</strong> Run the Electric Current prompt in both. Pick the clearer explanation!</div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-cyan">MISSIONS 1–4 OF 7</span>
  </div>
"""
s35_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">LAB MISSIONS 5 TO 7</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">YOUR 60-MINUTE LAB CHALLENGE (PART 2)</h3>
  </div>
  <div class="panel-body-content">
    <div class="mission-preview-list">
      <div class="m-card">
        <span class="m-num bg-yellow">M5</span>
        <div class="m-desc"><strong>NotebookLM Sourced Study:</strong> Upload your chapter PDF. Extract key concepts &amp; generate a 1-page revision sheet!</div>
      </div>
      <div class="m-card mt-2">
        <span class="m-num bg-cyan">M6</span>
        <div class="m-desc"><strong>5-Part Master Prompt Crafting:</strong> Write a WHO + WHAT + CONTEXT + HOW + RULE prompt for your hardest topic.</div>
      </div>
      <div class="m-card mt-2">
        <span class="m-num bg-red">M7</span>
        <div class="m-desc"><strong>Spot-the-Hallucination &amp; Certification:</strong> Detect the intentional AI flaw, verify against textbook, unlock your badge!</div>
      </div>
    </div>
  </div>
  <div class="panel-footer-meta">
    <span class="kid-badge badge-pink">MISSIONS 5–7 &bull; CERTIFICATION</span>
  </div>
"""
slides.append(make_slide(34, "115–120 MIN • LAB TRANSITION", "THE 7 HANDS-ON LAB MISSIONS &bull; SUMMARY", s35_left, s35_right))

# Slide 36: Closing Quote & Philosophy
s36_single = """
  <div class="slide-content-box center-aligned">
    <span class="slide-eyebrow">GENIUSPHERE PHILOSOPHY</span>
    <blockquote class="slide-blockquote" style="font-size: 2.2rem; max-width: 900px; margin: 1.5rem auto;">
      “The smartest student isn't the one who knows everything. It's the one who knows how to learn.”
    </blockquote>
    <p class="slide-quote-sub" style="font-size: 1.4rem; font-weight: 800; color: var(--nb-ink); margin-top: 1rem;">
      DON'T USE AI TO AVOID THINKING. USE AI TO THINK BETTER.
    </p>
    <div class="pill-group mt-3" style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
      <span class="kid-badge badge-yellow" style="font-size: 1rem; padding: 0.5rem 1.25rem;">Karnataka State Board &bull; Classes 9 &amp; 10</span>
      <span class="kid-badge badge-cyan" style="font-size: 1rem; padding: 0.5rem 1.25rem;">Bangalore AI Exam Lab</span>
      <span class="kid-badge badge-green" style="font-size: 1rem; padding: 0.5rem 1.25rem;">Geniusphere Certified</span>
    </div>
    <div class="slide-footer-tag mt-4">GENIUSPHERE AI EXAM LAB &bull; BANGALORE &bull; 2026</div>
  </div>
"""
slides.append(make_slide(35, "115–120 MIN • FINALE", "CLOSING QUOTE &bull; THE GENIUSPHERE CODE", "", "", is_single=True, single_html=s36_single))

print(f"Generated {len(slides)} slides successfully.")

with open('scratch/generated_curriculum_slides.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(slides))

print("Wrote scratch/generated_curriculum_slides.html successfully.")

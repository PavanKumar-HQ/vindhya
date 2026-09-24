import os
import re

def make_slide(idx, section, title, left_html, right_html, is_single=False, single_html=""):
    num_str = f"{idx+1:02d}"
    active_cls = " active" if idx == 0 else ""
    
    if is_single:
        return f"""
        <!-- SLIDE {num_str}: {title} -->
        <div class="carousel-slide{active_cls}" data-index="{idx}" data-section="{section}" data-title="{title}">
          <div class="merged-slide-container">
            <div class="merged-slide-header" style="display: none !important;">
              <h2 class="m-slide-title">{title}</h2>
            </div>
            <div class="merged-slide-single">
              {single_html}
            </div>
          </div>
        </div>"""
    else:
        return f"""
        <!-- SLIDE {num_str}: {title} -->
        <div class="carousel-slide{active_cls}" data-index="{idx}" data-section="{section}" data-title="{title}">
          <div class="merged-slide-container">
            <div class="merged-slide-header" style="display: none !important;">
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
presenter_scripts = []

# =========================================================================
# PART 1: OPENING & 2026 STUDENT REALITY (SLIDES 01 - 05)
# =========================================================================

# Slide 01
s1_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">STUDENT REALITY</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">YOU'RE STUDYING.</h3>
  </div>
  <div class="panel-body-content">
    <div class="story-highlight-box">
      <p>You read the same paragraph three times.</p>
      <p class="story-punchline mt-2">You still don't understand it.</p>
    </div>
    <p class="story-lead mt-3"><strong>What do you do?</strong></p>
    <div class="bullet-list-editorial mt-2">
      <div class="bullet-item"><div class="bullet-icon bg-red">📺</div><div class="bullet-text"><strong>Watch another YouTube video</strong><span class="bullet-sub">20 minutes to find a 2-mark answer</span></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-yellow">💬</div><div class="bullet-text"><strong>Ask a friend</strong><span class="bullet-sub">“Bro, what is this?! Are you studying this?”</span></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-cyan">😴</div><div class="bullet-text"><strong>Leave it for tomorrow or just memorize it</strong><span class="bullet-sub">Hoping it doesn't appear on the paper</span></div></div>
    </div>
  </div>
"""
s1_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">THE NEW REALITY</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">AND NOW THERE'S ONE MORE PERSON</h3>
  </div>
  <div class="panel-body-content">
    <div class="takeaway-big-card">
      <div class="takeaway-icon">🤖</div>
      <h4 class="takeaway-headline">AI (CHATGPT, GEMINI, NOTEBOOKLM)</h4>
      <p class="takeaway-desc">“Today I'm going to show you how ChatGPT can help in this exact situation. But there is one important difference: We're not going to use ChatGPT to give us answers. We're going to use it to <strong>learn</strong>.”</p>
    </div>
    <div class="three-pillars-strip mt-3">
      <div class="pillar-chip bg-yellow">UNDERSTAND</div>
      <div class="pillar-chip bg-cyan">PRACTISE</div>
      <div class="pillar-chip bg-pink">IMPROVE</div>
    </div>
  </div>
"""
slides.append(make_slide(0, "0–5 MIN • OPENING", "YOU'RE STUDYING &bull; WHAT DO YOU DO?", s1_left, s1_right))
presenter_scripts.append("""<strong>WALK IN WITH THE ACTUAL PROBLEM:</strong><br>“Let's start with something that actually happens.<br>You're studying Science. You reach a topic you don't understand. You read it once. Again. And somehow the paragraph becomes even more confusing.<br>What do you normally do?”<br>Take 2–3 quick responses from the room.<br>“And then what happens? You search YouTube. You ask your friend: ‘Bro, what is this?’<br>And now there's one more person you can ask: AI.<br>Today I'm going to show you how ChatGPT can help in this exact situation. But there is one important difference: We're not going to use ChatGPT to give us answers. We're going to use it to learn.”<hr class="script-divider"><strong>ACTION:</strong> Speak with natural warmth. Don't lecture; converse with the room.""")

# Slide 02
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
"""
slides.append(make_slide(1, "0–5 MIN • OPENING", "IT'S 10:30 PM &bull; WHAT WOULD YOU DO?", s2_left, s2_right))
presenter_scripts.append("""<strong>THE 10:30 PM ICEBREAKER:</strong><br>“Look at the screen: It's 10:30 PM. Exam tomorrow. One chapter left. You don't understand it.<br>Be honest: What are you doing?<br>Call out your letter or raise hands!<br>A — YouTube<br>B — Ask a friend<br>C — Pretend tomorrow doesn't exist<br>D — Ask AI<br>If anyone says C: ‘I appreciate the honesty!’<br>If most say D: ‘Okay, so AI is already part of your study life.’<br>Then transition: ‘But here's the question I actually want to answer today...’”<hr class="script-divider"><strong>ACTION:</strong> React live with humor and energy to their responses.""")

# Slide 03
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
        <p class="mt-1">You ask: <em>“Give me the five-mark answer.”</em></p>
        <p>&bull; Copy it &bull; Memorize it &bull; Write it in exam</p>
        <p class="mt-1"><strong>Result:</strong> Zero real learning.</p>
      </div>
      <div class="compare-versus-badge">VS</div>
      <div class="compare-col good-col">
        <div class="compare-badge badge-good">✅ YOU ARE LEARNING</div>
        <p class="mt-1">You ask: <em>“I don't understand this. Teach it to me. Give me an example. Then test me.”</em></p>
        <p class="mt-1"><strong>Result:</strong> Real comprehension!</p>
      </div>
    </div>
  </div>
"""
slides.append(make_slide(2, "0–5 MIN • OPENING", "THE BIG QUESTION &bull; STUDY OR AVOID STUDYING?", s3_left, s3_right))
presenter_scripts.append("""<strong>THE BIG QUESTION (THE HOOK):</strong><br>“Are you using AI to study… or are you using AI to avoid studying?<br>Let that sit in the room.<br>Because there is a huge difference.<br>If you ask AI: ‘Give me the five-mark answer’, copy it, memorize it, and write it in the exam… AI did the thinking.<br>Pause.<br>But if you ask: ‘I don't understand this. Teach it to me. Give me an example. Then test me.’—YOU are still doing the learning!”<hr class="script-divider"><strong>ACTION:</strong> Speak with conviction. This is the moral anchor of the session.""")

# Slide 04
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
          <strong>No Boring 1950s AI History</strong>
          <span class="bullet-sub">“I'm not going to spend two hours explaining what AI is. You already know AI exists. You've probably already used it.”</span>
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
"""
slides.append(make_slide(3, "0–5 MIN • OPENING", "AI EXAM LAB &bull; THE WORKSHOP PROMISE", s4_left, s4_right))
presenter_scripts.append("""<strong>INTRODUCE THE WORKSHOP:</strong><br>“That's what we're going to do today: AI EXAM LAB. Learn with AI. Don't let AI learn for you.<br>I'm not going to spend the next two hours explaining what artificial intelligence is. You already know AI exists. You've probably already used it.<br>What I want to teach you is something much more practical:<br>How can you actually use ChatGPT, Gemini and NotebookLM to prepare for your exams?<br>We're going to use them for three things: Understand. Practise. Improve.”<hr class="script-divider"><strong>ACTION:</strong> Clear, confident delivery of the workshop promise.""")

# Slide 05
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
"""
slides.append(make_slide(4, "0–5 MIN • OPENING", "THE CORE PHILOSOPHY &bull; WHAT DO YOU ASK?", s5_left, s5_right))
presenter_scripts.append("""<strong>THE ORIGINAL PHILOSOPHY & BRIDGE TO MODULE 1:</strong><br>“Remember this one line throughout today's session:<br>‘The smartest use of AI isn't getting the answer faster. It's learning how to understand it better.’<br>Now look at the right screen: When you don't understand something, what do you ask?<br>‘What is this?’ vs ‘Explain this in simple language’ vs ‘Give me an example’ vs ‘Ask me a question to see if I understood.’<br>Which one of these is actually helping you learn?<br>Exactly. And that is where we are going to start!”<hr class="script-divider"><strong>ACTION:</strong> Point to the 4 levels, get audience agreement, then transition to ChatGPT!""")

# =========================================================================
# PART 2: CHATGPT — YOUR AI STUDY PARTNER (SLIDES 06 - 17)
# =========================================================================

# Slide 06: What is ChatGPT actually doing?
s6_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">CHATGPT SECTION</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">MORE THAN AN ANSWER BOX</h3>
  </div>
  <div class="panel-body-content">
    <div class="story-highlight-box">
      <p class="story-punchline" style="font-size: 1.15rem !important;">“When most students hear ChatGPT, they think: 'Give me the answer.' That's the smallest possible use of it.”</p>
    </div>
    <p class="mt-3">The Complete Study Flow:</p>
    <div class="flywheel-pill-row mt-2" style="font-size: 0.8rem;">
      <span class="fw-pill bg-yellow">UNDERSTAND</span> &rarr;
      <span class="fw-pill bg-cyan">ASK</span> &rarr;
      <span class="fw-pill bg-pink">EXPLORE</span> &rarr;
      <span class="fw-pill bg-green">PRACTISE</span> &rarr;
      <span class="fw-pill bg-yellow">FEEDBACK</span> &rarr;
      <span class="fw-pill bg-cyan">REVISE</span>
    </div>
  </div>
"""
s6_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">THE 4 ROLES</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">4 ROLES FOR A STUDENT</h3>
  </div>
  <div class="panel-body-content">
    <div class="tier-card-grid">
      <div class="tier-card"><span class="tier-tag bg-yellow">1. TUTOR</span><p><strong>Explains concepts</strong> at your exact grade level.</p></div>
      <div class="tier-card"><span class="tier-tag bg-cyan">2. PRACTICE PARTNER</span><p><strong>Creates exam questions</strong> one at a time.</p></div>
      <div class="tier-card"><span class="tier-tag bg-pink">3. ANSWER CHECKER</span><p><strong>Gives teacher feedback</strong> on your written answers.</p></div>
      <div class="tier-card"><span class="tier-tag bg-green">4. REVISION PARTNER</span><p><strong>Finds weak areas</strong> and tests what you remember.</p></div>
    </div>
  </div>
"""
slides.append(make_slide(5, "5–10 MIN • CHATGPT AS STUDY PARTNER", "CHATGPT CAN BE MORE THAN AN ANSWER BOX", s6_left, s6_right))
presenter_scripts.append("""<strong>WHAT CHATGPT IS ACTUALLY DOING:</strong><br>“When most students hear ChatGPT, they think: ‘Give me the answer.’<br>That's the smallest possible use of it.<br>We're going to use it differently. Think of ChatGPT as someone you can study with.<br>You don't understand something? Ask. Need another explanation? Ask. Want a question? Ask. Want feedback on your answer? Ask. Want to test yourself? Ask.<br>Let's actually do it!”<hr class="script-divider"><strong>ACTION:</strong> Point to the 4 roles on screen: Tutor, Practice Partner, Answer Checker, Revision Partner.""")

# Slide 07: Demo 1 - The Lazy Prompt
s7_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-red">DEMO 1: THE LAZY PROMPT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">TRY THIS IN CHATGPT LIVE</h3>
  </div>
  <div class="panel-body-content">
    <div class="bad-prompt-preview">
      <span class="bad-label">❌ THE TYPICAL LAZY PROMPT:</span>
      <div class="code-box-bad">"Explain Newton's First Law of Motion."</div>
    </div>
    <p class="mt-3">Type it live. Let students see the response.</p>
    <div class="bullet-list-editorial mt-2">
      <div class="bullet-item"><div class="bullet-icon bg-yellow">❓</div><div class="bullet-text"><strong>“Did ChatGPT give us an answer?”</strong><span class="bullet-sub">Students: Yes!</span></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-red">⚠️</div><div class="bullet-text"><strong>“Is the answer necessarily useful?”</strong><span class="bullet-sub">This is the critical teaching point!</span></div></div>
    </div>
  </div>
"""
s7_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">WHY IT FAILS</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WHAT CHATGPT DOESN'T KNOW</h3>
  </div>
  <div class="panel-body-content">
    <div class="bullet-list-editorial">
      <div class="bullet-item"><div class="bullet-icon bg-red">1</div><div class="bullet-text"><strong>It doesn't know your class</strong><span class="bullet-sub">Are you Class 6, Class 9, or in college?</span></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-yellow">2</div><div class="bullet-text"><strong>It doesn't know what you already understand</strong><span class="bullet-sub">What part is confusing to you?</span></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-cyan">3</div><div class="bullet-text"><strong>It doesn't know your syllabus</strong><span class="bullet-sub">Do you need Karnataka State Board exam-style or generic wiki?</span></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-green">4</div><div class="bullet-text"><strong>So we must GIVE IT CONTEXT!</strong><span class="bullet-sub">Never just ask; tell it who you are!</span></div></div>
    </div>
  </div>
"""
slides.append(make_slide(6, "10–15 MIN • CHATGPT AS TUTOR", "CHATGPT AS A TUTOR &bull; THE LAZY PROMPT", s7_left, s7_right))
presenter_scripts.append("""<strong>DEMO 1: THE LAZY PROMPT:</strong><br>“Let's type this in ChatGPT live: ‘Explain Newton's First Law of Motion.’<br>Look at the screen. Did ChatGPT give us an answer? Yes.<br>Is the answer necessarily useful? Not really.<br>Why? Because ChatGPT doesn't automatically know: your class, what you already understand, what you're struggling with, or whether you want an exam explanation or a basic one.<br>So we need to give it context!”<hr class="script-divider"><strong>ACTION:</strong> Type the lazy prompt live on screen, show the wall of text, then turn to audience.""")

# Slide 08: Teach Them to Give Context
s8_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">UPGRADED PROMPT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">DON'T JUST ASK. GIVE CONTEXT.</h3>
  </div>
  <div class="panel-body-content">
    <div class="compare-box-vertical">
      <div class="box-bad mb-2">
        <span class="box-tag tag-red">❌ INSTEAD OF:</span>
        <div class="code-preview">Explain Newton's First Law.</div>
      </div>
      <div class="box-good">
        <span class="box-tag tag-green">✅ TRY THIS:</span>
        <div class="prompt-box">
          <div class="prompt-header">
            <span class="prompt-label">🎯 CONTEXT PROMPT</span>
            <button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button>
          </div>
          <div class="prompt-text">"I am a Class 9 student. I don't understand Newton's First Law of Motion. Explain it in simple language suitable for my class."</div>
        </div>
      </div>
    </div>
  </div>
"""
s8_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">THE MINDSET SHIFT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">A LEARNING CONVERSATION</h3>
  </div>
  <div class="panel-body-content">
    <div class="takeaway-big-card">
      <div class="takeaway-icon">💬</div>
      <h4 class="takeaway-headline">TELL AI WHO YOU ARE &amp; WHAT YOU NEED</h4>
      <p class="takeaway-desc">“The first improvement is incredibly simple. You're not asking a search engine for a link. You're having a learning conversation with a private tutor.”</p>
    </div>
    <div class="bullet-list-editorial mt-3">
      <div class="bullet-item"><div class="bullet-icon bg-yellow">🎯</div><div class="bullet-text"><strong>Calibrated Language:</strong> Explains using vocabulary appropriate for Class 9.</div></div>
    </div>
  </div>
"""
slides.append(make_slide(7, "10–15 MIN • CHATGPT AS TUTOR", "DON'T JUST ASK &bull; GIVE CONTEXT", s8_left, s8_right))
presenter_scripts.append("""<strong>TEACH THEM TO GIVE CONTEXT:</strong><br>“The first improvement is incredibly simple. Tell AI who you are and what you need.<br>‘I am a Class 9 student. I don't understand Newton's First Law of Motion. Explain it in simple language suitable for my class.’<br>You're not asking a search engine. You're having a learning conversation.<br>Watch the screen as we run this live.”<hr class="script-divider"><strong>ACTION:</strong> Run the context prompt live, highlight the sudden drop in jargon.""")

# Slide 09: Make ChatGPT Change the Explanation
s9_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">NEVER GIVE UP</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">FIRST EXPLANATION ≠ LAST ONE</h3>
  </div>
  <div class="panel-body-content">
    <p>“If the first explanation doesn't make sense, <strong>don't give up. Ask for another explanation!</strong>”</p>
    <div class="prompt-box mt-2">
      <div class="prompt-header"><span class="prompt-label">🚌 SCHOOL BUS ANALOGY</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
      <div class="prompt-text">"I still don't understand it. Explain it using a school-bus example."</div>
    </div>
    <div class="prompt-box mt-2">
      <div class="prompt-header"><span class="prompt-label">🏏 REAL-LIFE INERTIA</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
      <div class="prompt-text">"Now explain inertia separately using a real-life example."</div>
    </div>
  </div>
"""
s9_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">THE CONCEPT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">SAME CONCEPT &rarr; DIFFERENT EXPLANATION</h3>
  </div>
  <div class="panel-body-content">
    <p>ChatGPT can instantly change:</p>
    <div class="pillars-grid">
      <div class="pillar-box"><span class="p-num bg-yellow">1</span><strong>DIFFICULTY</strong><p>Simpler or advanced</p></div>
      <div class="pillar-box"><span class="p-num bg-cyan">2</span><strong>EXAMPLE</strong><p>Bus, cricket, cycling</p></div>
      <div class="pillar-box"><span class="p-num bg-pink">3</span><strong>ANALOGY</strong><p>Everyday situations</p></div>
      <div class="pillar-box"><span class="p-num bg-green">4</span><strong>STRUCTURE</strong><p>Steps, bullet points</p></div>
    </div>
    <p class="mt-2 text-center"><strong>Prompt:</strong> <em>“Explain it as if you were teaching a student who has never learned this before.”</em></p>
  </div>
"""
slides.append(make_slide(8, "10–15 MIN • CHATGPT AS TUTOR", "CHANGE THE EXPLANATION &bull; FIRST ISN'T LAST", s9_left, s9_right))
presenter_scripts.append("""<strong>MAKE CHATGPT CHANGE THE EXPLANATION:</strong><br>“This is something I really want you to remember: If the first explanation doesn't make sense, don't give up!<br>Ask for another explanation.<br>‘Explain it using a school-bus example.’<br>‘Now explain inertia separately using a real-life example.’<br>‘Explain it as if you were teaching a student who has never learned this before.’<br>AI can change difficulty, analogies, length, and perspective until it clicks!”<hr class="script-divider"><strong>ACTION:</strong> Demonstrate the school-bus prompt live. Let students see the analogy unfold.""")

# Slide 10: Follow-up Questions (Turn it into a conversation)
s10_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">CONTINUING THE DIALOGUE</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">TURN IT INTO A CONVERSATION</h3>
  </div>
  <div class="panel-body-content">
    <div class="bullet-list-editorial">
      <div class="bullet-item"><div class="bullet-icon bg-yellow">1</div><div class="bullet-text"><strong>Student:</strong> “I still don't understand inertia.” (ChatGPT explains)</div></div>
      <div class="bullet-item"><div class="bullet-icon bg-cyan">2</div><div class="bullet-text"><strong>Student:</strong> “Give me another example.”</div></div>
      <div class="bullet-item"><div class="bullet-icon bg-pink">3</div><div class="bullet-text"><strong>Student:</strong> “What's the difference between inertia and force?”</div></div>
      <div class="bullet-item"><div class="bullet-icon bg-green">4</div><div class="bullet-text"><strong>Student:</strong> “Give me a simple example where I can identify inertia myself.”</div></div>
    </div>
  </div>
"""
s10_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">THE STUDY HABIT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">DON'T OPEN 10 TABS &bull; STAY IN THE CHAT</h3>
  </div>
  <div class="panel-body-content">
    <div class="takeaway-big-card">
      <div class="takeaway-icon">🔄</div>
      <h4 class="takeaway-headline">CONTINUE THE CONVERSATION</h4>
      <p class="takeaway-desc">“Notice what's happening: We're not opening a new website every time we have a doubt. We're continuing the conversation. That's how you should use AI while studying.”</p>
    </div>
  </div>
"""
slides.append(make_slide(9, "15–20 MIN • CHATGPT CONVERSATION", "FOLLOW-UP QUESTIONS &bull; TURN IT INTO A CONVERSATION", s10_left, s10_right))
presenter_scripts.append("""<strong>FOLLOW-UP QUESTIONS:</strong><br>“Notice what's happening. We're not opening a new website every time we have a doubt.<br>We're continuing the conversation.<br>‘Give me another example.’ ‘What's the difference between inertia and force?’ ‘Give me a simple example where I can identify inertia myself.’<br>That's how you should use AI while studying alone at night!”<hr class="script-divider"><strong>ACTION:</strong> Show the conversational thread in ChatGPT.""")

# Slide 11: Flip the Role (Ask AI to check understanding)
s11_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">THE MOST IMPORTANT SHIFT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">NOW FLIP THE ROLE</h3>
  </div>
  <div class="panel-body-content">
    <div class="comparison-card">
      <div class="compare-col" style="background: #F1F5F9;">
        <span class="compare-badge bg-yellow" style="color: #000;">UNTIL NOW:</span>
        <p><strong>ChatGPT &rarr; teaches student</strong></p>
        <p>(Passive listening)</p>
      </div>
      <div class="compare-versus-badge">&rarr;</div>
      <div class="compare-col" style="background: #ECFDF5;">
        <span class="compare-badge bg-green" style="color: #000;">NOW:</span>
        <p><strong>ChatGPT &rarr; tests student!</strong></p>
        <p>(Active recall)</p>
      </div>
    </div>
  </div>
"""
s11_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">THE TEST PROMPT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">DON'T JUST ASK TO EXPLAIN &bull; ASK TO CHECK</h3>
  </div>
  <div class="panel-body-content">
    <div class="prompt-box">
      <div class="prompt-header"><span class="prompt-label">🎯 ROLE FLIP PROMPT</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
      <div class="prompt-text">"Now ask me one question to check whether I understood Newton's First Law. Don't give me the answer until I respond."</div>
    </div>
    <div class="chat-simulation-card mt-2">
      <div class="chat-msg"><div class="chat-avatar">🤖</div><div class="chat-bubble"><p><strong>ChatGPT:</strong> “If a book is resting on a table, why doesn't it move by itself? What would be required to make it move?”</p></div></div>
    </div>
  </div>
"""
slides.append(make_slide(10, "15–20 MIN • CHATGPT ROLE FLIP", "DON'T JUST ASK TO EXPLAIN &bull; ASK IT TO CHECK", s11_left, s11_right))
presenter_scripts.append("""<strong>NOW FLIP THE ROLE:</strong><br>“This is the most important part. Until now: ChatGPT teaches student. Now: ChatGPT tests student!<br>Prompt: ‘Now ask me one question to check whether I understood Newton's First Law. Don't give me the answer until I respond.’<br>Look at the screen: ChatGPT asks a question. Let's answer it live!”<hr class="script-divider"><strong>ACTION:</strong> Run prompt live. Ask a student in the audience to answer ChatGPT's question.""")

# Slide 12: Student Explains It Back (The Real Test)
s12_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">THE REAL TEST</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">CAN YOU EXPLAIN IT?</h3>
  </div>
  <div class="panel-body-content">
    <div class="prompt-box">
      <div class="prompt-header"><span class="prompt-label">📝 EXPLAIN-BACK PROMPT</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
      <div class="prompt-text">"Ask me to explain Newton's First Law in my own words. After I answer, tell me:
1. What I understood correctly
2. What I misunderstood
3. What I should improve
Don't rewrite the complete answer for me."</div>
    </div>
  </div>
"""
s12_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">LIVE DEMONSTRATION</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">DELIBERATELY IMPERFECT ANSWER</h3>
  </div>
  <div class="panel-body-content">
    <div class="student-draft-card">
      <span class="draft-tag">STUDENT TYPES:</span>
      <p class="draft-text">“Things keep doing what they are doing unless something hits them.”</p>
    </div>
    <div class="audit-result-card mt-2">
      <span class="audit-badge bg-yellow">CHATGPT FEEDBACK:</span>
      <p>1. Correct: You got the core concept of resistance to change.<br>
      2. Misunderstood: 'Something hits them' &rarr; Scientific term is <strong>external unbalanced force</strong>!<br>
      3. Improve: Mention both rest AND motion.</p>
    </div>
  </div>
"""
slides.append(make_slide(11, "15–20 MIN • CHATGPT ROLE FLIP", "THE REAL TEST &bull; CAN YOU EXPLAIN IT?", s12_left, s12_right))
presenter_scripts.append("""<strong>STUDENT EXPLAINS IT BACK:</strong><br>“Look at what just happened. ChatGPT didn't do my learning for me. I had to think! I had to explain.<br>Then AI gave me feedback.<br>‘Tell me what I understood correctly, what I misunderstood, and what I should improve. Don't rewrite the complete answer for me.’<br>This is the real test of whether you're ready for your exam.”<hr class="script-divider"><strong>ACTION:</strong> Highlight the 3-part feedback structure on screen.""")

# Slide 13: ChatGPT as a Practice Partner (Exam Questions)
s13_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">PRACTICE PARTNER</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">UNDERSTOOD THE TOPIC? NOW PRACTISE.</h3>
  </div>
  <div class="panel-body-content">
    <div class="prompt-box">
      <div class="prompt-header"><span class="prompt-label">🥊 PRACTICE PARTNER PROMPT</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
      <div class="prompt-text">"I am preparing for my Class 9 exam. I have just studied Newton's First Law of Motion. Give me 3 exam-style questions about this topic. Ask me one question at a time. Start with an easy question and gradually make the questions harder. Do not show me the answer before I respond."</div>
    </div>
  </div>
"""
s13_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">PROGRESSIVE TIERS</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">FROM EASY RECALL TO APPLICATION</h3>
  </div>
  <div class="panel-body-content">
    <div class="tier-card-grid">
      <div class="tier-card"><span class="tier-tag bg-yellow">QUESTION 1 (EASY)</span><p>Direct recall / definition: State Newton's First Law.</p></div>
      <div class="tier-card"><span class="tier-tag bg-cyan">QUESTION 2 (MEDIUM)</span><p>Reasoning: Why does a passenger lean forward when a bus stops?</p></div>
      <div class="tier-card"><span class="tier-tag bg-pink">QUESTION 3 (HARD)</span><p>Application: Explain why a coin drops into the glass when the card is flicked.</p></div>
    </div>
  </div>
"""
slides.append(make_slide(12, "20–25 MIN • CHATGPT PRACTICE PARTNER", "UNDERSTOOD THE TOPIC? &bull; NOW PRACTISE", s13_left, s13_right))
presenter_scripts.append("""<strong>CHATGPT AS A PRACTICE PARTNER:</strong><br>“Now ChatGPT changes roles. First it was my tutor. Now it becomes my practice partner.<br>Prompt: ‘Give me 3 exam-style questions. Ask me one question at a time. Start easy, make them harder. Do not show me the answer before I respond.’<br>Let it ask Question 1. Answer it. Then Question 2.”<hr class="script-divider"><strong>ACTION:</strong> Walk through Question 1, wait for student reply, then show Question 2.""")

# Slide 14: Teach Them Not to Look at the Answer (The Temptation)
s14_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-red">THE TRAP</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">THE TEMPTATION TRAP</h3>
  </div>
  <div class="panel-body-content">
    <div class="bullet-list-editorial">
      <div class="bullet-item"><div class="bullet-icon bg-yellow">1</div><div class="bullet-text"><strong>Question appears on screen</strong></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-cyan">2</div><div class="bullet-text"><strong>AI gives the answer immediately</strong></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-pink">3</div><div class="bullet-text"><strong>Student reads answer: “Yeah, I knew that.”</strong></div></div>
    </div>
    <div class="nightmare-banner mt-3" style="background: #FFF1F2; border: 1px solid #FECDD3; box-shadow: none;">
      <div class="banner-line" style="color: #BE123C; font-size: 1.3rem;">DID YOU REALLY KNOW IT?</div>
    </div>
  </div>
"""
s14_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">LEARNING PRINCIPLE</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">TRY FIRST &bull; THEN GET FEEDBACK</h3>
  </div>
  <div class="panel-body-content">
    <div class="takeaway-big-card">
      <div class="takeaway-icon">🧠</div>
      <h4 class="takeaway-headline">READING ≠ KNOWING</h4>
      <p class="takeaway-desc">“This is one of the biggest traps in student life. Reading an answer feels like knowing the answer. It isn't the same thing! If you're practising, <strong>TRY FIRST.</strong> Then get feedback.”</p>
    </div>
  </div>
"""
slides.append(make_slide(13, "20–25 MIN • CHATGPT PRACTICE PARTNER", "THE TEMPTATION TRAP &bull; DID YOU REALLY KNOW IT?", s14_left, s14_right))
presenter_scripts.append("""<strong>TEACH THEM NOT TO LOOK AT THE ANSWER:</strong><br>“This is one of the biggest traps. Reading an answer feels like knowing the answer. It isn't the same thing.<br>If AI shows you the answer right away, your brain goes: ‘Yeah, I knew that.’<br>Did you really know it? No! If you're practising, try first. Then get feedback.”<hr class="script-divider"><strong>ACTION:</strong> Speak with urgency. Ask students if they have fallen into this trap.""")

# Slide 15: ChatGPT as an Answer Checker (Write Your Own First)
s15_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">ANSWER CHECKER</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WRITE YOUR OWN ANSWER FIRST</h3>
  </div>
  <div class="panel-body-content">
    <p>Never ask AI to write the draft. Write yours, then paste it:</p>
    <div class="prompt-box mt-2">
      <div class="prompt-header"><span class="prompt-label">🧑‍🏫 TEACHER CHECK PROMPT</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
      <div class="prompt-text">"Here is my answer:
[student's answer]

Check my answer like a teacher. Tell me:
1. What I got right
2. What I misunderstood
3. What I should improve
Do not rewrite the complete answer for me. Give me a hint so I can improve it myself."</div>
    </div>
  </div>
"""
s15_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">WHY THIS RULE?</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">“DON'T REWRITE IT FOR ME”</h3>
  </div>
  <div class="panel-body-content">
    <div class="takeaway-big-card">
      <div class="takeaway-icon">💡</div>
      <h4 class="takeaway-headline">WHY HINTS BEAT REWRITING</h4>
      <p class="takeaway-desc">“Notice that last line: <em>'Don't rewrite it for me.'</em> Why? Because if AI writes the perfect answer and I simply copy it, I haven't improved. The struggle to improve is where marks are made!”</p>
    </div>
  </div>
"""
slides.append(make_slide(14, "25–30 MIN • CHATGPT ANSWER CHECKER", "WRITE YOUR OWN ANSWER FIRST &bull; ANSWER CHECKER", s15_left, s15_right))
presenter_scripts.append("""<strong>CHATGPT AS AN ANSWER CHECKER:</strong><br>“Notice that last line: Don't rewrite it for me.<br>Why?<br>Because if AI writes the perfect answer and I simply copy it, I haven't improved.<br>Tell it: ‘Check my answer like a teacher. What I got right, what I misunderstood, what I should improve. Give me a hint so I can improve it myself.’”<hr class="script-divider"><strong>ACTION:</strong> Point to the word 'hint' in the prompt box.""")

# Slide 16: The Improvement Loop & Finding Weaknesses
s16_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">THE LOOP</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WRITE &rarr; CHECK &rarr; IMPROVE</h3>
  </div>
  <div class="panel-body-content">
    <div class="comparison-card">
      <div class="compare-col bad-col">
        <div class="compare-badge badge-bad">❌ WRONG WORKFLOW</div>
        <p>ASK &rarr; COPY &rarr; FORGET</p>
      </div>
      <div class="compare-versus-badge">&rarr;</div>
      <div class="compare-col good-col">
        <div class="compare-badge badge-good">✅ GENIUSPHERE WORKFLOW</div>
        <p>Question &rarr; I think &rarr; I write &rarr; AI feedback &rarr; I identify mistake &rarr; I improve</p>
      </div>
    </div>
  </div>
"""
s16_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">FIND YOUR WEAKNESS</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WHAT AM I STRUGGLING WITH?</h3>
  </div>
  <div class="panel-body-content">
    <p>Make ChatGPT find your knowledge gaps:</p>
    <div class="prompt-box mt-2">
      <div class="prompt-header"><span class="prompt-label">🔍 DIAGNOSTIC PROMPT</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
      <div class="prompt-text">"Based on my answers so far, identify the concept I seem to be struggling with. Don't teach it yet. Just tell me what I should revise."</div>
    </div>
    <p class="mt-2 text-center">Then: <em>“Now explain that concept in simple language and give me one example.”</em></p>
  </div>
"""
slides.append(make_slide(15, "25–30 MIN • CHATGPT REVISION & WEAKNESS", "WRITE &bull; CHECK &bull; IMPROVE &bull; FIND WEAKNESS", s16_left, s16_right))
presenter_scripts.append("""<strong>THE IMPROVEMENT LOOP & FINDING WEAKNESSES:</strong><br>“The correct workflow is: Question &rarr; I think &rarr; I write &rarr; AI gives feedback &rarr; I identify my mistake &rarr; I improve.<br>Not: Ask &rarr; Copy &rarr; Forget.<br>And look at how you find weaknesses: ‘Based on my answers so far, identify the concept I seem to be struggling with. Don't teach it yet. Just tell me what I should revise.’<br>This teaches AI to diagnose your gaps!”<hr class="script-divider"><strong>ACTION:</strong> Draw the loop with hand gestures.""")

# Slide 17: The Complete ChatGPT Study Loop (11 Steps)
s17_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">MASTER FLYWHEEL</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">THE CHATGPT STUDY LOOP (1–6)</h3>
  </div>
  <div class="panel-body-content">
    <div class="bullet-list-editorial">
      <div class="bullet-item"><div class="bullet-icon bg-yellow">1</div><div class="bullet-text"><strong>DON'T UNDERSTAND</strong><span class="bullet-sub">Stuck on chapter paragraph</span></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-cyan">2</div><div class="bullet-text"><strong>ASK CHATGPT</strong><span class="bullet-sub">With class &amp; context</span></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-pink">3</div><div class="bullet-text"><strong>GET AN EXPLANATION</strong><span class="bullet-sub">Simple language</span></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-green">4</div><div class="bullet-text"><strong>ASK FOLLOW-UP QUESTIONS</strong><span class="bullet-sub">Clarify confusing words</span></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-yellow">5</div><div class="bullet-text"><strong>GET AN EXAMPLE</strong><span class="bullet-sub">School bus / cricket</span></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-cyan">6</div><div class="bullet-text"><strong>TEST YOURSELF</strong><span class="bullet-sub">AI asks you a check question</span></div></div>
    </div>
  </div>
"""
s17_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">MASTER FLYWHEEL</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">THE CHATGPT STUDY LOOP (7–11)</h3>
  </div>
  <div class="panel-body-content">
    <div class="bullet-list-editorial">
      <div class="bullet-item"><div class="bullet-icon bg-pink">7</div><div class="bullet-text"><strong>WRITE YOUR OWN ANSWER</strong><span class="bullet-sub">In your own words</span></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-green">8</div><div class="bullet-text"><strong>GET TEACHER FEEDBACK</strong><span class="bullet-sub">Right, missing, hints</span></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-yellow">9</div><div class="bullet-text"><strong>FIND YOUR WEAKNESS</strong><span class="bullet-sub">Spot the concept gap</span></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-cyan">10</div><div class="bullet-text"><strong>REVISE</strong><span class="bullet-sub">Focus on weak section</span></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-red">11</div><div class="bullet-text"><strong>TEST AGAIN!</strong><span class="bullet-sub">Lock in exam readiness</span></div></div>
    </div>
  </div>
"""
slides.append(make_slide(16, "25–30 MIN • CHATGPT STUDY LOOP", "THE COMPLETE CHATGPT STUDY LOOP &bull; 11 STEPS", s17_left, s17_right))
presenter_scripts.append("""<strong>THE COMPLETE CHATGPT STUDY LOOP:</strong><br>“This is what I want you to remember from everything we've done with ChatGPT.<br>ChatGPT isn't just: Question &rarr; Answer.<br>It can become a complete study conversation: Don't understand &rarr; Ask &rarr; Explanation &rarr; Follow-up &rarr; Example &rarr; Test yourself &rarr; Write own answer &rarr; Feedback &rarr; Find weakness &rarr; Revise &rarr; Test again.<br>Memorize this loop!”<hr class="script-divider"><strong>ACTION:</strong> Step back and let students absorb the 11-step framework.""")

# =========================================================================
# PART 3: PROMPTING & RESPONSIBLE USE (SLIDES 18 - 20)
# =========================================================================

# Slide 18: Prompting with Context (WHO, WHAT, PROBLEM, HOW, RULE)
s18_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">PROMPT ARCHITECTURE</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">A GOOD PROMPT HAS CONTEXT</h3>
  </div>
  <div class="panel-body-content">
    <div class="formula-stack-editorial">
      <div class="f-item"><span class="f-tag bg-yellow">WHO</span><div class="f-info"><strong>Who are you?</strong> &rarr; <em>“Class 10 State Board student”</em></div></div>
      <div class="f-item"><span class="f-tag bg-cyan">WHAT</span><div class="f-info"><strong>What are you studying?</strong> &rarr; <em>“Science exam &bull; Electricity”</em></div></div>
      <div class="f-item"><span class="f-tag bg-pink">PROBLEM</span><div class="f-info"><strong>What don't you understand?</strong> &rarr; <em>“Electric potential difference”</em></div></div>
      <div class="f-item"><span class="f-tag bg-green">HOW</span><div class="f-info"><strong>How should AI explain?</strong> &rarr; <em>“Simple language + everyday example”</em></div></div>
      <div class="f-item"><span class="f-tag bg-red">RULE</span><div class="f-info"><strong>What shouldn't AI do?</strong> &rarr; <em>“Don't give answer until I try!”</em></div></div>
    </div>
  </div>
"""
s18_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">BEFORE &amp; AFTER</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">ELECTRICITY PROMPT SHOWDOWN</h3>
  </div>
  <div class="panel-body-content">
    <div class="box-bad mb-2">
      <span class="box-tag tag-red">❌ BAD:</span>
      <div class="code-preview">Explain electricity.</div>
    </div>
    <div class="box-good">
      <span class="box-tag tag-green">✅ MASTER PROMPT:</span>
      <div class="prompt-box">
        <div class="prompt-header"><span class="prompt-label">⚡ 5-PART MASTER PROMPT</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
        <div class="prompt-text">"I am a Class 10 Karnataka State Board student preparing for my Science exam. I don't understand the concept of electric potential difference. Explain it in simple language, use one everyday example, then ask me one question to check whether I understood it. Don't give me the answer until I try."</div>
      </div>
    </div>
  </div>
"""
slides.append(make_slide(17, "30–35 MIN • PROMPTING & RULES", "A GOOD PROMPT HAS CONTEXT &bull; 5 INGREDIENTS", s18_left, s18_right))
presenter_scripts.append("""<strong>A GOOD PROMPT HAS CONTEXT:</strong><br>“You don't need to write giant complicated prompts. You just need to give AI enough information to understand what you're trying to accomplish.<br>WHO: Class 10 State Board student.<br>WHAT: Science exam.<br>PROBLEM: Electric potential difference.<br>HOW: Simple language + everyday example.<br>RULE: Don't give the answer until I try!”<hr class="script-divider"><strong>ACTION:</strong> Show the bad vs better prompt contrast.""")

# Slide 19: How to Correct AI
s19_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">DIRECTING AI</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">AI DIDN'T EXPLAIN IT WELL?</h3>
  </div>
  <div class="panel-body-content">
    <p>Don't stop or close the window! Use these quick directing phrases:</p>
    <div class="bullet-list-editorial mt-2">
      <div class="bullet-item"><div class="bullet-icon bg-yellow">⚡</div><div class="bullet-text"><strong>“Too difficult. Simplify it.”</strong></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-cyan">🌍</div><div class="bullet-text"><strong>“Give me a real-life example.”</strong></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-pink">🎯</div><div class="bullet-text"><strong>“Explain only this part.”</strong></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-green">⚖️</div><div class="bullet-text"><strong>“Compare these two concepts.”</strong></div></div>
    </div>
  </div>
"""
s19_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">COMMAND VOCABULARY</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">PRACTICAL STEERING COMMANDS</h3>
  </div>
  <div class="panel-body-content">
    <div class="bullet-list-editorial">
      <div class="bullet-item"><div class="bullet-icon bg-yellow">🪜</div><div class="bullet-text"><strong>“Explain it step by step.”</strong></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-pink">❓</div><div class="bullet-text"><strong>“Ask me a question instead.”</strong></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-red">🛑</div><div class="bullet-text"><strong>“Don't give me the answer yet.”</strong></div></div>
    </div>
    <div class="takeaway-big-card mt-3">
      <p class="takeaway-desc">“You are the pilot. AI is the engine. Steering AI is an active skill!”</p>
    </div>
  </div>
"""
slides.append(make_slide(18, "30–35 MIN • PROMPTING & RULES", "AI DIDN'T EXPLAIN IT WELL? &bull; STEER THE AI", s19_left, s19_right))
presenter_scripts.append("""<strong>TEACH THEM HOW TO CORRECT AI:</strong><br>“AI didn't explain it well? Don't stop.<br>Try: ‘Too difficult. Simplify it.’ ‘Give me a real-life example.’ ‘Explain only this part.’ ‘Compare these two concepts.’ ‘Explain it step by step.’ ‘Ask me a question instead.’ ‘Don't give me the answer yet.’<br>This gives you a practical vocabulary for interacting with AI!”<hr class="script-divider"><strong>ACTION:</strong> Encourage students to write down these 7 steering phrases.""")

# Slide 20: Responsible Use & The Golden Rule
s20_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-red">RESPONSIBLE USE</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">CHATGPT CAN BE WRONG.</h3>
  </div>
  <div class="panel-body-content">
    <div class="danger-case-box">
      <p style="font-size: 1.15rem; font-weight: 800; color: #BE123C; margin: 0;">AI &ne; textbook &bull; AI &ne; teacher &bull; AI &ne; your brain</p>
      <p class="mt-2">“ChatGPT can give information that sounds extremely confident and still be wrong. Check important facts against your textbook or teacher.”</p>
    </div>
    <div class="protocol-card-stack mt-2">
      <div class="p-card bg-red-tint"><div class="p-icon bg-red">🛑</div><div class="p-text"><strong>STOP</strong><span>Don't blindly trust</span></div></div>
      <div class="p-card bg-yellow-tint"><div class="p-icon bg-yellow">🔍</div><div class="p-text"><strong>CHECK</strong><span>Compare with textbook</span></div></div>
      <div class="p-card bg-green-tint"><div class="p-icon bg-green">🧠</div><div class="p-text"><strong>THINK</strong><span>Make sure you understand</span></div></div>
    </div>
  </div>
"""
s20_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">THE GOLDEN RULE</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">DON'T ASK AI TO DO THE LEARNING</h3>
  </div>
  <div class="panel-body-content">
    <div class="big-hook-card">
      <blockquote class="hook-quote" style="font-size: 1.35rem;">
        “Don't ask AI to do the learning. Ask AI to HELP YOU do the learning.”
      </blockquote>
    </div>
    <div class="comparison-card mt-3">
      <div class="compare-col bad-col"><div class="compare-badge badge-bad">❌ WRONG</div><p>Give me the 5-mark answer.</p></div>
      <div class="compare-versus-badge">&rarr;</div>
      <div class="compare-col good-col"><div class="compare-badge badge-good">✅ RIGHT</div><p>Teach me &rarr; example &rarr; ask question &rarr; let me answer &rarr; feedback.</p></div>
    </div>
  </div>
"""
slides.append(make_slide(19, "30–35 MIN • PROMPTING & RULES", "RESPONSIBLE USE &bull; THE GOLDEN RULE", s20_left, s20_right))
presenter_scripts.append("""<strong>RESPONSIBLE USE & THE GOLDEN RULE:</strong><br>“One important warning: ChatGPT can give you information that sounds extremely confident and still be wrong.<br>AI &ne; textbook. AI &ne; teacher. AI &ne; your brain.<br>STOP &rarr; CHECK &rarr; THINK.<br>And remember the Golden Rule: Don't ask AI to do the learning. Ask AI to HELP YOU do the learning!”<hr class="script-divider"><strong>ACTION:</strong> Speak with authority. Emphasize textbook checking.""")

# =========================================================================
# PART 4: GEMINI — EXPLORE, COMPARE & PRACTISE (SLIDES 21 - 27)
# =========================================================================

# Slide 21: Transition to Gemini (What if you asked another AI?)
s21_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">GEMINI SECTION</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WHAT IF YOU ASKED ANOTHER AI?</h3>
  </div>
  <div class="panel-body-content">
    <p class="story-lead">You've asked ChatGPT to explain something. But...</p>
    <div class="story-highlight-box mt-2">
      <p class="story-punchline" style="font-size: 1.25rem !important;">Would another AI explain it differently?</p>
    </div>
    <p class="mt-3">There are different AI systems, and they can produce different responses to the exact same question.</p>
  </div>
"""
s21_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">MEET GOOGLE GEMINI</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">EXPLORE, COMPARE &amp; EVALUATE</h3>
  </div>
  <div class="panel-body-content">
    <div class="comparison-card">
      <div class="compare-col" style="background: #FFFBEB;">
        <span class="compare-badge bg-yellow" style="color: #000;">CHATGPT SECTION</span>
        <p><strong>“How can AI tutor me?”</strong></p>
        <p>Tutor, sparring, auditing</p>
      </div>
      <div class="compare-versus-badge">&amp;</div>
      <div class="compare-col" style="background: #ECFEFF;">
        <span class="compare-badge bg-cyan" style="color: #000;">GEMINI SECTION</span>
        <p><strong>“How can I explore &amp; compare?”</strong></p>
        <p>Alternative perspectives &amp; evaluation</p>
      </div>
    </div>
  </div>
"""
slides.append(make_slide(20, "35–40 MIN • GEMINI AS SECOND TOOL", "WHAT IF YOU ASKED ANOTHER AI? &bull; MEET GEMINI", s21_left, s21_right))
presenter_scripts.append("""<strong>TRANSITION TO GEMINI:</strong><br>“We've just learned how to turn ChatGPT into a study partner. But ChatGPT isn't the only AI tool available to you.<br>There are different AI systems, and they can produce different responses to the same question.<br>So let's try something: We're going to give the same learning problem to another AI.<br>That AI is Gemini.”<hr class="script-divider"><strong>ACTION:</strong> Open Gemini in browser or show on screen.""")

# Slide 22: Gemini as Study Assistant & First Live Demo
s22_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">STUDY ASSISTANT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">GEMINI AS A STUDY ASSISTANT</h3>
  </div>
  <div class="panel-body-content">
    <div class="tier-card-grid">
      <div class="tier-card"><span class="tier-tag bg-yellow">UNDERSTAND</span><p>Difficult concepts with fresh angles.</p></div>
      <div class="tier-card"><span class="tier-tag bg-cyan">EXPLORE</span><p>Ask follow-up questions &amp; visual examples.</p></div>
      <div class="tier-card"><span class="tier-tag bg-pink">PRACTISE</span><p>Generate diverse exam-style questions.</p></div>
      <div class="tier-card"><span class="tier-tag bg-green">REVIEW</span><p>Work through what you've learned.</p></div>
    </div>
  </div>
"""
s22_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">LIVE DEMONSTRATION</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">SAME PROBLEM IN GEMINI</h3>
  </div>
  <div class="panel-body-content">
    <div class="prompt-box">
      <div class="prompt-header"><span class="prompt-label">⚡ EXACT SAME PROMPT</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
      <div class="prompt-text">"I am a Class 9 student. I don't understand Newton's First Law of Motion. Explain it in simple language suitable for my class. Use one real-life example."</div>
    </div>
    <div class="bullet-list-editorial mt-2">
      <div class="bullet-item"><div class="bullet-icon bg-cyan">👀</div><div class="bullet-text"><strong>What did you notice?</strong><span class="bullet-sub">Different wording, different example, different structure!</span></div></div>
    </div>
  </div>
"""
slides.append(make_slide(21, "40–45 MIN • GEMINI STUDY ASSISTANT", "GEMINI AS A STUDY ASSISTANT &bull; FIRST LIVE DEMO", s22_left, s22_right))
presenter_scripts.append("""<strong>FIRST LIVE DEMO IN GEMINI:</strong><br>“We give Gemini the exact same problem: ‘I am a Class 9 student. I don't understand Newton's First Law. Explain in simple language suitable for my class. Use one real-life example.’<br>Run it in Gemini. What did you notice?<br>Different wording? Different example? Different structure?<br>Let's compare them!”<hr class="script-divider"><strong>ACTION:</strong> Run prompt live in Gemini, invite audience observations.""")

# Slide 23: Same Question != Same Answer & Evaluation
s23_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">AI EVALUATION</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">SAME QUESTION &ne; SAME ANSWER</h3>
  </div>
  <div class="panel-body-content">
    <div class="takeaway-big-card">
      <div class="takeaway-icon">⚖️</div>
      <h4 class="takeaway-headline">SAME QUESTION &rarr; DIFFERENT AI &rarr; DIFFERENT RESPONSE</h4>
      <p class="takeaway-desc">“That doesn't automatically mean one is correct and the other is wrong. And it definitely doesn't mean: 'The answer I like more must be correct.'”</p>
    </div>
  </div>
"""
s23_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">COMPARE, DON'T CHOOSE</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">DON'T ASK: “WHICH AI IS BETTER?”</h3>
  </div>
  <div class="panel-body-content">
    <p>Ask: <strong>“Which explanation helps ME understand this particular topic?”</strong></p>
    <div class="audit-result-card mt-2">
      <div class="audit-row"><span class="audit-badge bg-green">1. UNDERSTANDABLE?</span> &bull; Does the language click with you?</div>
      <div class="audit-row mt-1"><span class="audit-badge bg-cyan">2. EXAMPLE USEFUL?</span> &bull; Is the analogy clear (water pipe vs hallway)?</div>
      <div class="audit-row mt-1"><span class="audit-badge bg-yellow">3. APPROPRIATE LEVEL?</span> &bull; Does it fit your Class 9/10 exam?</div>
      <div class="audit-row mt-1"><span class="audit-badge bg-red">4. MATCHES TEXTBOOK?</span> &bull; <strong>CHECK with your school book!</strong></div>
    </div>
  </div>
"""
slides.append(make_slide(22, "40–45 MIN • GEMINI EVALUATION", "SAME QUESTION &ne; SAME ANSWER &bull; COMPARE, DON'T CHOOSE", s23_left, s23_right))
presenter_scripts.append("""<strong>COMPARE, DON'T BLINDLY CHOOSE:</strong><br>“We're not running a competition here. Your goal isn't to become a ChatGPT fan or a Gemini fan.<br>Your goal is to learn!<br>Don't ask: ‘Which AI is better?’ Ask: ‘Which explanation helps me understand this particular topic?’<br>Use whichever explanation helps you understand—and verify important information.”<hr class="script-divider"><strong>ACTION:</strong> Review the 4-point comparison checklist.""")

# Slide 24: Gemini as an Exploration Tool & Change Style
s24_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">EXPLORATION</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">DON'T STOP AT THE FIRST ANSWER</h3>
  </div>
  <div class="panel-body-content">
    <p>Keep exploring in Gemini:</p>
    <div class="bullet-list-editorial mt-2">
      <div class="bullet-item"><div class="bullet-icon bg-yellow">1</div><div class="bullet-text"><strong>“Why does this happen?”</strong></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-cyan">2</div><div class="bullet-text"><strong>“Give me a real-life example.”</strong></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-pink">3</div><div class="bullet-text"><strong>“Explain the difference between inertia and force.”</strong></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-green">4</div><div class="bullet-text"><strong>“Give me a situation where I can identify inertia myself.”</strong></div></div>
    </div>
  </div>
"""
s24_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">STYLE DIRECTING</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">CAN GEMINI EXPLAIN IT ANOTHER WAY?</h3>
  </div>
  <div class="panel-body-content">
    <div class="prompt-box">
      <div class="prompt-header"><span class="prompt-label">🏏 CRICKET EXAMPLE</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
      <div class="prompt-text">"Explain this using a cricket example."</div>
    </div>
    <div class="prompt-box mt-2">
      <div class="prompt-header"><span class="prompt-label">📋 5 SIMPLE POINTS</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
      <div class="prompt-text">"Explain it in five simple points."</div>
    </div>
  </div>
"""
slides.append(make_slide(23, "45–50 MIN • GEMINI EXPLORATION", "GEMINI AS AN EXPLORATION TOOL &bull; CHANGE STYLE", s24_left, s24_right))
presenter_scripts.append("""<strong>GEMINI AS AN EXPLORATION TOOL:</strong><br>“The real power isn't asking one question. It's being able to keep exploring until the concept makes sense.<br>‘Why does this happen?’ ‘Explain the difference between inertia and force.’<br>‘Explain this using a cricket example.’ ‘Explain it in five simple points.’<br>You direct the explanation, rather than accepting whatever appears first!”<hr class="script-divider"><strong>ACTION:</strong> Prompt Gemini for the cricket analogy live.""")

# Slide 25: Gemini for Exam Practice & Progressive Difficulty
s25_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">EXAM PRACTICE</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">UNDERSTOOD IT? NOW TEST YOURSELF</h3>
  </div>
  <div class="panel-body-content">
    <div class="prompt-box">
      <div class="prompt-header"><span class="prompt-label">🎯 GEMINI EXAM PRACTICE PROMPT</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
      <div class="prompt-text">"I am preparing for my Class 9 Science exam. I have studied Newton's First Law of Motion. Give me 3 exam-style questions. Ask me one at a time. Don't show me the answer until I respond."</div>
    </div>
    <p class="mt-2">Gemini asks Question 1. Student answers. Then continue!</p>
  </div>
"""
s25_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">PROGRESSIVE DIFFICULTY</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">MAKE QUESTIONS PROGRESSIVELY HARDER</h3>
  </div>
  <div class="panel-body-content">
    <div class="prompt-box">
      <div class="prompt-header"><span class="prompt-label">📈 TIERED DIFFICULTY PROMPT</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
      <div class="prompt-text">"Start with an easy conceptual question. Then give me a medium question. Finally give me an application-based question. Ask one at a time and wait for my answer before continuing."</div>
    </div>
    <div class="takeaway-big-card mt-2">
      <p class="takeaway-desc">“Tell AI how you want to practise. Easy first. Then harder. Then application. That's true exam coaching!”</p>
    </div>
  </div>
"""
slides.append(make_slide(24, "50–55 MIN • GEMINI EXAM PRACTICE", "GEMINI FOR EXAM PRACTICE &bull; PROGRESSIVE DIFFICULTY", s25_left, s25_right))
presenter_scripts.append("""<strong>PROGRESSIVE DIFFICULTY IN GEMINI:</strong><br>“You can tell AI how you want to practise.<br>Prompt: ‘Start with an easy conceptual question. Then give me a medium question. Finally give me an application-based question. Ask one at a time and wait for my answer before continuing.’<br>Easy first. Then harder. Then application. That's much more useful than simply asking: ‘Give me questions.’”<hr class="script-divider"><strong>ACTION:</strong> Trigger the 3-tier question sequence in Gemini.""")

# Slide 26: Gemini as a Second Opinion & Verification
s26_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">SECOND OPINION</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">NOT SURE ABOUT AN EXPLANATION?</h3>
  </div>
  <div class="panel-body-content">
    <p>Ask another AI for a cross-check:</p>
    <div class="prompt-box mt-2">
      <div class="prompt-header"><span class="prompt-label">🔍 SECOND OPINION PROMPT</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
      <div class="prompt-text">"I received this explanation of Newton's First Law: [paste explanation]. Explain it in simpler language and point out anything I should verify with my textbook."</div>
    </div>
  </div>
"""
s26_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-red">VERIFICATION RULE</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">AI CAN SOUND CONFIDENT &amp; BE WRONG</h3>
  </div>
  <div class="panel-body-content">
    <div class="danger-case-box">
      <p style="font-size: 1.1rem; font-weight: 800; color: #BE123C; margin: 0;">TWO AIS AGREEING DOES NOT MAKE SOMETHING TRUE!</p>
      <p class="mt-2">“Don't use an AI response as your final authority just because it sounds confident. For your exams, your textbook and teacher matter. AI &rarr; CHECK &rarr; TEXTBOOK / TEACHER.”</p>
    </div>
  </div>
"""
slides.append(make_slide(25, "50–55 MIN • GEMINI SECOND OPINION", "NOT SURE ABOUT AN EXPLANATION? &bull; SECOND OPINION", s26_left, s26_right))
presenter_scripts.append("""<strong>GEMINI AS A SECOND OPINION:</strong><br>“If something seems confusing, you can ask another AI to explain it differently.<br>‘Explain it in simpler language and point out anything I should verify with my textbook.’<br>But remember this crucial sentence: Two AIs agreeing does not automatically make something true!<br>If an important fact, definition, or formula doesn't match your textbook, stop and check it.”<hr class="script-divider"><strong>ACTION:</strong> Reiterate the 'Two AIs agreeing &ne; True' principle.""")

# Slide 27: The Gemini Study Loop & Two Tools Together
s27_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">GEMINI STUDY LOOP</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">THE GEMINI STUDY WORKFLOW</h3>
  </div>
  <div class="panel-body-content">
    <div class="flywheel-pill-row" style="font-size: 0.8rem;">
      <span class="fw-pill bg-yellow">TOPIC</span> &rarr;
      <span class="fw-pill bg-cyan">ASK GEMINI</span> &rarr;
      <span class="fw-pill bg-pink">UNDERSTAND</span> &rarr;
      <span class="fw-pill bg-green">FOLLOW-UP</span> &rarr;
      <span class="fw-pill bg-yellow">PRACTISE</span> &rarr;
      <span class="fw-pill bg-cyan">ANSWER</span> &rarr;
      <span class="fw-pill bg-red">VERIFY</span>
    </div>
    <div class="box-bad mt-3">
      <span class="box-tag tag-red">⚠️ ONE IMPORTANT RULE:</span>
      <p class="box-note" style="font-size: 0.95rem; color: #BE123C;"><strong>NEVER COPY BOTH ANSWERS AND CALL IT STUDYING! 😂</strong><br>Read &rarr; Think &rarr; Answer &rarr; Check</p>
    </div>
  </div>
"""
s27_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">60-SECOND CHALLENGE</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">YOUR 60-SECOND GEMINI CHALLENGE</h3>
  </div>
  <div class="panel-body-content">
    <div class="prompt-box">
      <div class="prompt-header"><span class="prompt-label">⏱️ 60-SEC CHALLENGE PROMPT</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
      <div class="prompt-text">"Explain [topic] to me in simple language using a real-life example. Then ask me one question to test whether I understood it. Don't give me the answer until I respond."</div>
    </div>
    <p class="mt-2 text-center"><strong>Show of hands:</strong> How many could now use Gemini without asking it to simply give the answer?</p>
  </div>
"""
slides.append(make_slide(26, "55–60 MIN • GEMINI SUMMARY", "TWO AI TOOLS &bull; ONE STUDY METHOD &bull; 60-SEC CHALLENGE", s27_left, s27_right))
presenter_scripts.append("""<strong>TWO AI TOOLS, ONE STUDY METHOD:</strong><br>“You don't have to choose one AI and use it for everything.<br>ChatGPT: Tutor (Understand &rarr; Explain &rarr; Feedback).<br>Gemini: Explorer + Practice Partner (Explore &rarr; Compare &rarr; Practise).<br>And remember: Never copy both answers and call it studying! Read them. Understand them. Close the AI. Try explaining it yourself.”<hr class="script-divider"><strong>ACTION:</strong> Ask room for a quick show of hands for the 60-second challenge.""")

# =========================================================================
# PART 5: NOTEBOOKLM — STUDY WITH YOUR OWN MATERIAL (SLIDES 28 - 33)
# =========================================================================

# Slide 28: Transition to NotebookLM (Study with your own material)
s28_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">NOTEBOOKLM SECTION</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">YOU HAVE 40 PAGES TO STUDY.</h3>
  </div>
  <div class="panel-body-content">
    <div class="nightmare-banner" style="background: #1E1B4B;">
      <div class="banner-line">TEXTBOOK.</div>
      <div class="banner-line">TEACHER NOTES.</div>
      <div class="banner-line">PDF CHAPTERS.</div>
      <div class="banner-line highlight-red">WHERE DO YOU START?</div>
    </div>
    <p class="mt-2">“Imagine your exam is next week. You're sitting in front of 50 pages thinking: What exactly am I supposed to study first?”</p>
  </div>
"""
s28_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">THE BIG DIFFERENCE</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WHAT IF AI STUDIED YOUR MATERIAL?</h3>
  </div>
  <div class="panel-body-content">
    <div class="comparison-card">
      <div class="compare-col" style="background: #F1F5F9;">
        <span class="compare-badge bg-yellow" style="color: #000;">CHATGPT &amp; GEMINI</span>
        <p><strong>“Tell me about this topic.”</strong></p>
        <p>(Knows whole internet)</p>
      </div>
      <div class="compare-versus-badge">&rarr;</div>
      <div class="compare-col" style="background: #EEF2FF;">
        <span class="compare-badge bg-pink" style="color: #000;">NOTEBOOKLM</span>
        <p><strong>“Help me understand the material I am actually studying.”</strong></p>
        <p>(Grounded strictly in your PDF)</p>
      </div>
    </div>
  </div>
"""
slides.append(make_slide(27, "60–65 MIN • NOTEBOOKLM INTRODUCTION", "YOU HAVE 40 PAGES TO STUDY &bull; MEET NOTEBOOKLM", s28_left, s28_right))
presenter_scripts.append("""<strong>TRANSITION TO NOTEBOOKLM:</strong><br>“So far, we've been asking AI about subjects. But there's a problem: What if I don't want AI to give me info from everywhere? What if I want it to work specifically with my textbook, my notes, my study material?<br>Imagine uploading your study material and asking questions about that material.<br>ChatGPT/Gemini: ‘Tell me about this topic.’<br>NotebookLM: ‘Help me understand the material I am actually studying.’<br>Let's meet NotebookLM!”<hr class="script-divider"><strong>ACTION:</strong> Open NotebookLM interface on screen.""")

# Slide 29: Live Demo - Upload Material & What Should I Study?
s29_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">LIVE DEMONSTRATION</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">GIVE IT THE MATERIAL</h3>
  </div>
  <div class="panel-body-content">
    <p>Open NotebookLM. Create notebook: <strong>Class 10 Science &mdash; Electricity</strong>. Upload approved school PDF.</p>
    <div class="takeaway-big-card mt-2">
      <div class="takeaway-icon">📄</div>
      <h4 class="takeaway-headline">ONE CLEAN SOURCE</h4>
      <p class="takeaway-desc">“This is the material we're actually going to study. Not random web pages &mdash; your actual syllabus chapter!”</p>
    </div>
  </div>
"""
s29_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">FIRST QUESTION</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WHAT SHOULD I STUDY?</h3>
  </div>
  <div class="panel-body-content">
    <p>Don't read everything blindly:</p>
    <div class="prompt-box mt-2">
      <div class="prompt-header"><span class="prompt-label">📑 WORKFLOW 1 PROMPT</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
      <div class="prompt-text">"Based only on the study material I provided, identify the key concepts I should understand before my exam. Explain each one briefly in simple language."</div>
    </div>
    <p class="mt-2">Then: <em>“Organise the important concepts from this chapter in a logical order for studying.”</em></p>
  </div>
"""
slides.append(make_slide(28, "65–70 MIN • NOTEBOOKLM WORKFLOW", "LIVE DEMO: GIVE IT THE MATERIAL &bull; EXTRACT CONCEPTS", s29_left, s29_right))
presenter_scripts.append("""<strong>LIVE DEMO: GIVE IT THE MATERIAL:</strong><br>“We upload our approved Class 10 Electricity chapter PDF to NotebookLM.<br>Look at our first prompt: ‘Based only on the study material I provided, identify the key concepts I should understand before my exam. Explain each one briefly in simple language.’<br>Look at what just happened: We're not asking ‘Tell me everything about electricity.’ We're asking NotebookLM to help us understand the material we've actually provided!”<hr class="script-divider"><strong>ACTION:</strong> Upload PDF live and execute Workflow 1 prompt.""")

# Slide 30: Difficult Sections & Questions with Citations
s30_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">SIMPLIFY SECTIONS</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">FOUND A DIFFICULT SECTION?</h3>
  </div>
  <div class="panel-body-content">
    <div class="prompt-box">
      <div class="prompt-header"><span class="prompt-label">🔍 SIMPLIFY PROMPT</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
      <div class="prompt-text">"I don't understand Section 12.4 on Resistance. Explain it in simpler language using an everyday example. Stay close to the information in my study material."</div>
    </div>
    <p class="mt-2">Notice the instruction: <em>'Stay close to the information in my study material.'</em></p>
  </div>
"""
s30_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">CLICKABLE CITATIONS</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">QUESTIONS ABOUT YOUR MATERIAL</h3>
  </div>
  <div class="panel-body-content">
    <div class="prompt-box">
      <div class="prompt-header"><span class="prompt-label">📖 CITATION PROMPT</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
      <div class="prompt-text">"According to my study material, what is the difference between resistance and resistivity? Which section supports this?"</div>
    </div>
    <div class="citation-demo-box mt-2">
      <span class="demo-icon">📌</span>
      <div class="demo-text"><strong>Clickable Source Chips:</strong> <span>Click citation [1] &rarr; NotebookLM highlights the exact paragraph in your textbook!</span></div>
    </div>
  </div>
"""
slides.append(make_slide(29, "65–70 MIN • NOTEBOOKLM WORKFLOW", "DIFFICULT SECTIONS &bull; QUESTIONS WITH CITATIONS", s30_left, s30_right))
presenter_scripts.append("""<strong>DIFFICULT SECTIONS & CITATIONS:</strong><br>“Notice the difference from what we did with ChatGPT. We're not saying ‘Explain electricity.’ We're saying: ‘Here's the material I'm studying. Help me understand this part of it.’<br>And look at the citations: NotebookLM tells you exactly which page and paragraph supports the answer. True grounded verification!”<hr class="script-divider"><strong>ACTION:</strong> Click on a citation chip live in NotebookLM to show the viewer highlight.""")

# Slide 31: Turn Material into a Revision Guide
s31_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">REVISION GUIDE</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">MAKE YOUR NOTES WORK FOR YOU</h3>
  </div>
  <div class="panel-body-content">
    <p>Before an exam, you don't have time to re-read 40 pages:</p>
    <div class="prompt-box mt-2">
      <div class="prompt-header"><span class="prompt-label">📋 REVISION GUIDE PROMPT</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
      <div class="prompt-text">"Based only on the study material I provided, create a concise revision guide for this chapter. Include the key concepts, important definitions, formulas and points I should revise."</div>
    </div>
  </div>
"""
s31_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">HIGH-YIELD OUTPUT</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">CONCISE 1-PAGE SUMMARY</h3>
  </div>
  <div class="panel-body-content">
    <div class="revision-sheet-preview">
      <div class="sheet-header"><strong>CHAPTER 12: ELECTRICITY &bull; HIGH-YIELD REVISION</strong></div>
      <div class="sheet-body">
        <p><strong>Ohm's Law:</strong> V = IR (At constant temperature)</p>
        <p><strong>Series:</strong> I is constant, Rs = R1 + R2 + R3</p>
        <p><strong>Parallel:</strong> V is constant, 1/Rp = 1/R1 + 1/R2 + 1/R3</p>
        <p><strong>Joule's Heating:</strong> H = I&sup2;Rt</p>
      </div>
    </div>
  </div>
"""
slides.append(make_slide(30, "70–75 MIN • NOTEBOOKLM REVISION", "MAKE YOUR NOTES WORK FOR YOU &bull; REVISION GUIDE", s31_left, s31_right))
presenter_scripts.append("""<strong>TURN MATERIAL INTO A REVISION GUIDE:</strong><br>“This is where NotebookLM becomes unbeatable before an exam. You've already got the material.<br>Now you tell it: ‘Based only on the study material I provided, create a concise revision guide for this chapter.’<br>In 15 seconds, you have a 1-page summary of every formula and definition in your book!”<hr class="script-divider"><strong>ACTION:</strong> Show the clean generated revision guide on screen.""")

# Slide 32: Sourced Quiz & Finding Weaknesses in Notes
s32_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">SOURCED QUIZ</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">DON'T JUST READ. TEST YOURSELF.</h3>
  </div>
  <div class="panel-body-content">
    <div class="prompt-box">
      <div class="prompt-header"><span class="prompt-label">🎯 SOURCED QUIZ PROMPT</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
      <div class="prompt-text">"Using only the study material I provided, quiz me on this topic. Ask one question at a time. Do not reveal the answer until I respond. Include both conceptual and application-based questions."</div>
    </div>
    <p class="mt-2">Then: <em>“Give me a more difficult question that tests whether I understand rather than remember definitions.”</em></p>
  </div>
"""
s32_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-cyan">DIAGNOSTIC LOOP</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">WHAT AM I STILL WEAK AT?</h3>
  </div>
  <div class="panel-body-content">
    <div class="prompt-box">
      <div class="prompt-header"><span class="prompt-label">🔍 GAP FINDER PROMPT</span><button type="button" class="btn-copy-prompt" onclick="copyPromptText(this)">Copy 📋</button></div>
      <div class="prompt-text">"Based on my answers to the questions so far, identify the concepts I should revise again. Do not give me a complete lesson yet. Just identify my weak areas."</div>
    </div>
    <p class="mt-2 text-center">Then: <em>“Now help me revise the first weak area using only my study material.”</em></p>
  </div>
"""
slides.append(make_slide(31, "70–75 MIN • NOTEBOOKLM QUIZ & WEAKNESS", "SOURCED QUIZ &bull; WHAT AM I STILL WEAK AT?", s32_left, s32_right))
presenter_scripts.append("""<strong>SOURCED QUIZ & GAP FINDER:</strong><br>“Again, the objective isn't to get AI to answer for us. We're making AI test us on our own textbook!<br>‘Quiz me one question at a time. Do not reveal the answer until I respond.’<br>And look at the gap finder: ‘Based on my answers, identify the concepts I should revise again.’<br>Study &rarr; Test &rarr; Find weakness &rarr; Revise &rarr; Test again.”<hr class="script-divider"><strong>ACTION:</strong> Execute one quiz question from the uploaded PDF.""")

# Slide 33: The Source Boundary & NotebookLM Study Loop
s33_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">SOURCE BOUNDARY</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">USE THE SOURCE BOUNDARY</h3>
  </div>
  <div class="panel-body-content">
    <p>Always build this habit in NotebookLM:</p>
    <div class="bullet-list-editorial mt-2">
      <div class="bullet-item"><div class="bullet-icon bg-yellow">📌</div><div class="bullet-text"><strong>“Based on my study material...”</strong></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-cyan">📖</div><div class="bullet-text"><strong>“According to the chapter...”</strong></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-pink">📑</div><div class="bullet-text"><strong>“From the notes I uploaded...”</strong></div></div>
    </div>
    <div class="danger-case-box mt-2">
      <p style="font-size: 0.85rem; color: #BE123C; margin: 0;"><strong>Caution:</strong> If your notes contain an error, AI repeats it! Always verify official formulas with teachers.</p>
    </div>
  </div>
"""
s33_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">MASTER LOOP</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">THE NOTEBOOKLM STUDY LOOP</h3>
  </div>
  <div class="panel-body-content">
    <div class="bullet-list-editorial">
      <div class="bullet-item"><div class="bullet-icon bg-yellow">1</div><div class="bullet-text"><strong>UPLOAD STUDY MATERIAL</strong></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-cyan">2</div><div class="bullet-text"><strong>UNDERSTAND CHAPTER &amp; FIND KEY CONCEPTS</strong></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-pink">3</div><div class="bullet-text"><strong>CLARIFY DIFFICULT SECTIONS</strong></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-green">4</div><div class="bullet-text"><strong>CREATE REVISION MATERIAL &amp; TEST YOURSELF</strong></div></div>
      <div class="bullet-item"><div class="bullet-icon bg-red">5</div><div class="bullet-text"><strong>FIND WEAK AREAS &rarr; REVISE &rarr; TEST AGAIN!</strong></div></div>
    </div>
  </div>
"""
slides.append(make_slide(32, "75–80 MIN • NOTEBOOKLM STUDY LOOP", "THE SOURCE BOUNDARY &bull; NOTEBOOKLM STUDY LOOP", s33_left, s33_right))
presenter_scripts.append("""<strong>THE SOURCE BOUNDARY & NOTEBOOKLM LOOP:</strong><br>“Get into this habit: Tell AI what source you want it to work from: ‘Based on my study material...’ ‘According to the chapter...’<br>And remember: If your notes contain an error, AI doesn't magically fix them. So important exam formulas must still be verified with your teacher!<br>Memorize the NotebookLM loop: Upload &rarr; Understand &rarr; Concepts &rarr; Clarify &rarr; Revise &rarr; Test!”<hr class="script-divider"><strong>ACTION:</strong> Review the NotebookLM loop on screen.""")

# =========================================================================
# PART 6: SYNTHESIS & LAB MISSION BRIEFING (SLIDES 34 - 36)
# =========================================================================

# Slide 34: Three Tools Synthesis
s34_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-pink">THE FULL ARSENAL</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">THREE TOOLS. THREE USE CASES.</h3>
  </div>
  <div class="panel-body-content">
    <div class="tier-card-grid">
      <div class="tier-card">
        <span class="tier-tag bg-yellow">1. CHATGPT: “TEACH ME.”</span>
        <p>Difficult concepts &bull; Explanations &bull; Feedback &bull; Sparring practice</p>
      </div>
      <div class="tier-card">
        <span class="tier-tag bg-cyan">2. GEMINI: “HELP ME EXPLORE.”</span>
        <p>Alternative explanations &bull; Real-life examples &bull; Progressive practice &bull; Comparison</p>
      </div>
      <div class="tier-card">
        <span class="tier-tag bg-pink">3. NOTEBOOKLM: “HELP ME STUDY THIS MATERIAL.”</span>
        <p>Textbook &bull; Teacher notes &bull; PDFs &bull; Source-based questions &bull; Sourced quiz</p>
      </div>
    </div>
  </div>
"""
s34_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">UNIFIED STRATEGY</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">NOW THE WORKSHOP MAKES SENSE</h3>
  </div>
  <div class="panel-body-content">
    <div class="takeaway-big-card">
      <div class="takeaway-icon">🏆</div>
      <h4 class="takeaway-headline">YOU HAVE A COMPLETE STUDY ARSENAL</h4>
      <p class="takeaway-desc">“You don't have to pick one app. You now know which tool to reach for when you're stuck, when you need to explore, and when you need to revise your exact school textbook.”</p>
    </div>
  </div>
"""
slides.append(make_slide(33, "80–85 MIN • THREE TOOLS SYNTHESIS", "THREE TOOLS &bull; THREE USE CASES", s34_left, s34_right))
presenter_scripts.append("""<strong>THREE TOOLS, THREE USE CASES:</strong><br>“Look at how the entire workshop connects together:<br>CHATGPT: ‘Teach me.’ (Difficult concepts, explanations, feedback, practice).<br>GEMINI: ‘Help me explore.’ (Alternative explanations, examples, comparison).<br>NOTEBOOKLM: ‘Help me study this material.’ (Textbook, notes, source-based quiz).<br>Three distinct tools. One complete study arsenal!”<hr class="script-divider"><strong>ACTION:</strong> Point to each tool banner proudly.""")

# Slide 35: The Geniusphere Method
s35_left = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-yellow">CORE PRINCIPLE</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">THE TOOL IS NOT THE METHOD</h3>
  </div>
  <div class="panel-body-content">
    <p>“Tomorrow tools will change. New models will come. New versions will launch. But <strong>THE METHOD</strong> is what I want you to remember forever.”</p>
    <div class="flywheel-pill-row mt-3" style="font-size: 0.85rem;">
      <span class="fw-pill bg-yellow">UNDERSTAND</span> &rarr;
      <span class="fw-pill bg-cyan">ASK</span> &rarr;
      <span class="fw-pill bg-pink">THINK</span> &rarr;
      <span class="fw-pill bg-green">PRACTISE</span> &rarr;
      <span class="fw-pill bg-yellow">ANSWER</span> &rarr;
      <span class="fw-pill bg-cyan">FEEDBACK</span> &rarr;
      <span class="fw-pill bg-pink">REVISE</span> &rarr;
      <span class="fw-pill bg-green">TEST AGAIN</span>
    </div>
  </div>
"""
s35_right = """
  <div class="panel-header-strip">
    <span class="panel-tag tag-green">YOUR LAB CHALLENGE</span>
  </div>
  <div class="panel-title-area">
    <h3 class="panel-heading">THE NOTEBOOKLM CHALLENGE</h3>
  </div>
  <div class="panel-body-content">
    <div class="bullet-list-editorial">
      <div class="bullet-item"><div class="bullet-icon bg-yellow">1</div><div class="bullet-text">Find 3 key concepts from provided chapter</div></div>
      <div class="bullet-item"><div class="bullet-icon bg-cyan">2</div><div class="bullet-text">Choose 1 concept you don't understand</div></div>
      <div class="bullet-item"><div class="bullet-icon bg-pink">3</div><div class="bullet-text">Ask NotebookLM to explain it with an example</div></div>
      <div class="bullet-item"><div class="bullet-icon bg-green">4</div><div class="bullet-text">Ask it one question &bull; answer yourself &bull; get feedback!</div></div>
    </div>
  </div>
"""
slides.append(make_slide(34, "85–90 MIN • THE GENIUSPHERE METHOD", "THE TOOL IS NOT THE METHOD &bull; GENIUSPHERE CODE", s35_left, s35_right))
presenter_scripts.append("""<strong>THE TOOL IS NOT THE METHOD:</strong><br>“Tomorrow these AI tools will change. New tools will come. New versions will launch.<br>But this method is what I want you to remember:<br>UNDERSTAND &rarr; ASK &rarr; THINK &rarr; PRACTISE &rarr; ANSWER &rarr; GET FEEDBACK &rarr; FIND WEAKNESSES &rarr; REVISE &rarr; TEST AGAIN.<br>The tool is not the method. You are the student.”<hr class="script-divider"><strong>ACTION:</strong> Speak with great passion and clarity.""")

# Slide 36: Transition to Hands-On Computer Lab
s36_single = """
  <div class="slide-content-box center-aligned">
    <span class="slide-eyebrow">PHASE 2 &bull; COMPUTER LAB</span>
    <h2 class="slide-hero-title" style="font-size: 2.2rem; margin: 0.5rem 0;">YOU NOW HAVE THREE WAYS TO STUDY WITH AI</h2>
    <div class="pill-group mt-3" style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
      <span class="kid-badge badge-yellow" style="font-size: 1.15rem; padding: 0.65rem 1.4rem;">CHATGPT: “Teach me.”</span>
      <span class="kid-badge badge-cyan" style="font-size: 1.15rem; padding: 0.65rem 1.4rem;">GEMINI: “Help me explore.”</span>
      <span class="kid-badge badge-pink" style="font-size: 1.15rem; padding: 0.65rem 1.4rem;">NOTEBOOKLM: “Study my material.”</span>
    </div>
    <blockquote class="slide-blockquote mt-4" style="font-size: 1.45rem; max-width: 920px; margin: 1.5rem auto;">
      “You've only seen me do it. Now it's your turn. We're going to the computer lab. And I'm not going to tell you what to type. I'm going to give you a problem &mdash; you have to make the AI help you solve it.”
    </blockquote>
    <div class="slide-footer-tag mt-3">GENIUSPHERE AI EXAM LAB &bull; BANGALORE &bull; 2026</div>
  </div>
"""
slides.append(make_slide(35, "90 MIN • FINALE & LAB KICKOFF", "AUDITORIUM (I TEACH) &rarr; COMPUTER LAB (YOU DO!)", "", "", is_single=True, single_html=s36_single))
presenter_scripts.append("""<strong>FINAL LINE BEFORE THE COMPUTER LAB:</strong><br>“You now have three ways to study with AI.<br>ChatGPT: Teach me.<br>Gemini: Help me explore.<br>NotebookLM: Help me work through my study material.<br>But you've only seen me do it.<br>Now it's your turn.<br>We're going to the computer lab. And I'm not going to tell you what to type.<br>I'm going to give you a problem—you have to make the AI help you solve it.<br>Let's go!”<hr class="script-divider"><strong>ACTION:</strong> Massive enthusiastic energy! Cue applause, transition to Student Lab workstations.""")

print(f"Generated {len(slides)} slides and {len(presenter_scripts)} presenter scripts successfully.")

# Write generated slides HTML
with open('scratch/generated_three_tools_slides.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(slides))

print("Wrote scratch/generated_three_tools_slides.html successfully.")

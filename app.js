/**
 * GENIUSPHERE AI EXAM LAB — CAROUSEL ENGINE & LAB WORKSPACE
 * Full slide carousel navigation, keyboard arrows, presenter script drawer,
 * student mission stepper, 60-min timer, formula inspector, and autosave.
 */

// Application State
const appState = {
  currentMode: 'deck', // 'deck', 'lab', 'overview'
  currentSlide: 0,
  totalSlides: 36,
  
  labStep: 0,
  totalLabSteps: 6,
  
  // Timer State
  timerSeconds: 60 * 60,
  timerRunning: false,
  timerInterval: null,
  isMuted: false,
  
  // Student Lab Data
  labData: {
    studentName: '',
    classVal: '9',
    subject: 'Science (Physics)',
    topic: "Newton's First Law of Motion",
    confidenceBefore: '2',
    confidenceAfter: '4',
    aiMindset: 'Help me learn',
    m1_answer: '',
    m2_tool: 'Both',
    m2_reason: '',
    m3_q1: '',
    m3_q2: '',
    m3_q3: '',
    m4_right: '',
    m4_wrong: '',
    m4_improved: '',
    m5_concept: '',
    m5_question: '',
    m6_prompt_input: '',
    m7_boss_q: '',
    m7_boss_attempt: '',
    m7_boss_eval: '',
    refl_learned: '',
    refl_revise: ''
  }
};

// Word-for-Word Presenter Scripts for all 30 Slides
const presenterScripts = [
  `<strong>WALK IN WITH THE ACTUAL PROBLEM:</strong><br>“Let's start with something that actually happens.<br>You're studying Science. You reach a topic you don't understand. You read it once. Again. And somehow the paragraph becomes even more confusing.<br>What do you normally do?”<br>Take 2–3 quick responses from the room.<br>“And then what happens? You search YouTube. You ask your friend: ‘Bro, what is this?’<br>And now there's one more person you can ask: AI.<br>Today I'm going to show you how ChatGPT can help in this exact situation. But there is one important difference: We're not going to use ChatGPT to give us answers. We're going to use it to learn.”<hr class="script-divider"><strong>ACTION:</strong> Speak with natural warmth. Don't lecture; converse with the room.`,

  `<strong>THE 10:30 PM ICEBREAKER:</strong><br>“Look at the screen: It's 10:30 PM. Exam tomorrow. One chapter left. You don't understand it.<br>Be honest: What are you doing?<br>Call out your letter or raise hands!<br>A — YouTube<br>B — Ask a friend<br>C — Pretend tomorrow doesn't exist<br>D — Ask AI<br>If anyone says C: ‘I appreciate the honesty!’<br>If most say D: ‘Okay, so AI is already part of your study life.’<br>Then transition: ‘But here's the question I actually want to answer today...’”<hr class="script-divider"><strong>ACTION:</strong> React live with humor and energy to their responses.`,

  `<strong>THE BIG QUESTION (THE HOOK):</strong><br>“Are you using AI to study… or are you using AI to avoid studying?<br>Let that sit in the room.<br>Because there is a huge difference.<br>If you ask AI: ‘Give me the five-mark answer’, copy it, memorize it, and write it in the exam… AI did the thinking.<br>Pause.<br>But if you ask: ‘I don't understand this. Teach it to me. Give me an example. Then test me.’—YOU are still doing the learning!”<hr class="script-divider"><strong>ACTION:</strong> Speak with conviction. This is the moral anchor of the session.`,

  `<strong>INTRODUCE THE WORKSHOP:</strong><br>“That's what we're going to do today: AI EXAM LAB. Learn with AI. Don't let AI learn for you.<br>I'm not going to spend the next two hours explaining what artificial intelligence is. You already know AI exists. You've probably already used it.<br>What I want to teach you is something much more practical:<br>How can you actually use ChatGPT, Gemini and NotebookLM to prepare for your exams?<br>We're going to use them for three things: Understand. Practise. Improve.”<hr class="script-divider"><strong>ACTION:</strong> Clear, confident delivery of the workshop promise.`,

  `<strong>THE ORIGINAL PHILOSOPHY & BRIDGE TO MODULE 1:</strong><br>“Remember this one line throughout today's session:<br>‘The smartest use of AI isn't getting the answer faster. It's learning how to understand it better.’<br>Now look at the right screen: When you don't understand something, what do you ask?<br>‘What is this?’ vs ‘Explain this in simple language’ vs ‘Give me an example’ vs ‘Ask me a question to see if I understood.’<br>Which one of these is actually helping you learn?<br>Exactly. And that is where we are going to start!”<hr class="script-divider"><strong>ACTION:</strong> Point to the 4 levels, get audience agreement, then transition to ChatGPT!`,

  `<strong>WHAT CHATGPT IS ACTUALLY DOING:</strong><br>“When most students hear ChatGPT, they think: ‘Give me the answer.’<br>That's the smallest possible use of it.<br>We're going to use it differently. Think of ChatGPT as someone you can study with.<br>You don't understand something? Ask. Need another explanation? Ask. Want a question? Ask. Want feedback on your answer? Ask. Want to test yourself? Ask.<br>Let's actually do it!”<hr class="script-divider"><strong>ACTION:</strong> Point to the 4 roles on screen: Tutor, Practice Partner, Answer Checker, Revision Partner.`,

  `<strong>DEMO 1: THE LAZY PROMPT:</strong><br>“Let's type this in ChatGPT live: ‘Explain Newton's First Law of Motion.’<br>Look at the screen. Did ChatGPT give us an answer? Yes.<br>Is the answer necessarily useful? Not really.<br>Why? Because ChatGPT doesn't automatically know: your class, what you already understand, what you're struggling with, or whether you want an exam explanation or a basic one.<br>So we need to give it context!”<hr class="script-divider"><strong>ACTION:</strong> Type the lazy prompt live on screen, show the wall of text, then turn to audience.`,

  `<strong>TEACH THEM TO GIVE CONTEXT:</strong><br>“The first improvement is incredibly simple. Tell AI who you are and what you need.<br>‘I am a Class 9 student. I don't understand Newton's First Law of Motion. Explain it in simple language suitable for my class.’<br>You're not asking a search engine. You're having a learning conversation.<br>Watch the screen as we run this live.”<hr class="script-divider"><strong>ACTION:</strong> Run the context prompt live, highlight the sudden drop in jargon.`,

  `<strong>MAKE CHATGPT CHANGE THE EXPLANATION:</strong><br>“This is something I really want you to remember: If the first explanation doesn't make sense, don't give up!<br>Ask for another explanation.<br>‘Explain it using a school-bus example.’<br>‘Now explain inertia separately using a real-life example.’<br>‘Explain it as if you were teaching a student who has never learned this before.’<br>AI can change difficulty, analogies, length, and perspective until it clicks!”<hr class="script-divider"><strong>ACTION:</strong> Demonstrate the school-bus prompt live. Let students see the analogy unfold.`,

  `<strong>FOLLOW-UP QUESTIONS:</strong><br>“Notice what's happening. We're not opening a new website every time we have a doubt.<br>We're continuing the conversation.<br>‘Give me another example.’ ‘What's the difference between inertia and force?’ ‘Give me a simple example where I can identify inertia myself.’<br>That's how you should use AI while studying alone at night!”<hr class="script-divider"><strong>ACTION:</strong> Show the conversational thread in ChatGPT.`,

  `<strong>NOW FLIP THE ROLE:</strong><br>“This is the most important part. Until now: ChatGPT teaches student. Now: ChatGPT tests student!<br>Prompt: ‘Now ask me one question to check whether I understood Newton's First Law. Don't give me the answer until I respond.’<br>Look at the screen: ChatGPT asks a question. Let's answer it live!”<hr class="script-divider"><strong>ACTION:</strong> Run prompt live. Ask a student in the audience to answer ChatGPT's question.`,

  `<strong>STUDENT EXPLAINS IT BACK:</strong><br>“Look at what just happened. ChatGPT didn't do my learning for me. I had to think! I had to explain.<br>Then AI gave me feedback.<br>‘Tell me what I understood correctly, what I misunderstood, and what I should improve. Don't rewrite the complete answer for me.’<br>This is the real test of whether you're ready for your exam.”<hr class="script-divider"><strong>ACTION:</strong> Highlight the 3-part feedback structure on screen.`,

  `<strong>CHATGPT AS A PRACTICE PARTNER:</strong><br>“Now ChatGPT changes roles. First it was my tutor. Now it becomes my practice partner.<br>Prompt: ‘Give me 3 exam-style questions. Ask me one question at a time. Start easy, make them harder. Do not show me the answer before I respond.’<br>Let it ask Question 1. Answer it. Then Question 2.”<hr class="script-divider"><strong>ACTION:</strong> Walk through Question 1, wait for student reply, then show Question 2.`,

  `<strong>TEACH THEM NOT TO LOOK AT THE ANSWER:</strong><br>“This is one of the biggest traps. Reading an answer feels like knowing the answer. It isn't the same thing.<br>If AI shows you the answer right away, your brain goes: ‘Yeah, I knew that.’<br>Did you really know it? No! If you're practising, try first. Then get feedback.”<hr class="script-divider"><strong>ACTION:</strong> Speak with urgency. Ask students if they have fallen into this trap.`,

  `<strong>CHATGPT AS AN ANSWER CHECKER:</strong><br>“Notice that last line: Don't rewrite it for me.<br>Why?<br>Because if AI writes the perfect answer and I simply copy it, I haven't improved.<br>Tell it: ‘Check my answer like a teacher. What I got right, what I misunderstood, what I should improve. Give me a hint so I can improve it myself.’”<hr class="script-divider"><strong>ACTION:</strong> Point to the word 'hint' in the prompt box.`,

  `<strong>THE IMPROVEMENT LOOP & FINDING WEAKNESSES:</strong><br>“The correct workflow is: Question &rarr; I think &rarr; I write &rarr; AI gives feedback &rarr; I identify my mistake &rarr; I improve.<br>Not: Ask &rarr; Copy &rarr; Forget.<br>And look at how you find weaknesses: ‘Based on my answers so far, identify the concept I seem to be struggling with. Don't teach it yet. Just tell me what I should revise.’<br>This teaches AI to diagnose your gaps!”<hr class="script-divider"><strong>ACTION:</strong> Draw the loop with hand gestures.`,

  `<strong>THE COMPLETE CHATGPT STUDY LOOP:</strong><br>“This is what I want you to remember from everything we've done with ChatGPT.<br>ChatGPT isn't just: Question &rarr; Answer.<br>It can become a complete study conversation: Don't understand &rarr; Ask &rarr; Explanation &rarr; Follow-up &rarr; Example &rarr; Test yourself &rarr; Write own answer &rarr; Feedback &rarr; Find weakness &rarr; Revise &rarr; Test again.<br>Memorize this loop!”<hr class="script-divider"><strong>ACTION:</strong> Step back and let students absorb the 11-step framework.`,

  `<strong>A GOOD PROMPT HAS CONTEXT:</strong><br>“You don't need to write giant complicated prompts. You just need to give AI enough information to understand what you're trying to accomplish.<br>WHO: Class 10 State Board student.<br>WHAT: Science exam.<br>PROBLEM: Electric potential difference.<br>HOW: Simple language + everyday example.<br>RULE: Don't give the answer until I try!”<hr class="script-divider"><strong>ACTION:</strong> Show the bad vs better prompt contrast.`,

  `<strong>TEACH THEM HOW TO CORRECT AI:</strong><br>“AI didn't explain it well? Don't stop.<br>Try: ‘Too difficult. Simplify it.’ ‘Give me a real-life example.’ ‘Explain only this part.’ ‘Compare these two concepts.’ ‘Explain it step by step.’ ‘Ask me a question instead.’ ‘Don't give me the answer yet.’<br>This gives you a practical vocabulary for interacting with AI!”<hr class="script-divider"><strong>ACTION:</strong> Encourage students to write down these 7 steering phrases.`,

  `<strong>RESPONSIBLE USE & THE GOLDEN RULE:</strong><br>“One important warning: ChatGPT can give you information that sounds extremely confident and still be wrong.<br>AI &ne; textbook. AI &ne; teacher. AI &ne; your brain.<br>STOP &rarr; CHECK &rarr; THINK.<br>And remember the Golden Rule: Don't ask AI to do the learning. Ask AI to HELP YOU do the learning!”<hr class="script-divider"><strong>ACTION:</strong> Speak with authority. Emphasize textbook checking.`,

  `<strong>TRANSITION TO GEMINI:</strong><br>“We've just learned how to turn ChatGPT into a study partner. But ChatGPT isn't the only AI tool available to you.<br>There are different AI systems, and they can produce different responses to the same question.<br>So let's try something: We're going to give the same learning problem to another AI.<br>That AI is Gemini.”<hr class="script-divider"><strong>ACTION:</strong> Open Gemini in browser or show on screen.`,

  `<strong>FIRST LIVE DEMO IN GEMINI:</strong><br>“We give Gemini the exact same problem: ‘I am a Class 9 student. I don't understand Newton's First Law. Explain in simple language suitable for my class. Use one real-life example.’<br>Run it in Gemini. What did you notice?<br>Different wording? Different example? Different structure?<br>Let's compare them!”<hr class="script-divider"><strong>ACTION:</strong> Run prompt live in Gemini, invite audience observations.`,

  `<strong>COMPARE, DON'T BLINDLY CHOOSE:</strong><br>“We're not running a competition here. Your goal isn't to become a ChatGPT fan or a Gemini fan.<br>Your goal is to learn!<br>Don't ask: ‘Which AI is better?’ Ask: ‘Which explanation helps me understand this particular topic?’<br>Use whichever explanation helps you understand—and verify important information.”<hr class="script-divider"><strong>ACTION:</strong> Review the 4-point comparison checklist.`,

  `<strong>GEMINI AS AN EXPLORATION TOOL:</strong><br>“The real power isn't asking one question. It's being able to keep exploring until the concept makes sense.<br>‘Why does this happen?’ ‘Explain the difference between inertia and force.’<br>‘Explain this using a cricket example.’ ‘Explain it in five simple points.’<br>You direct the explanation, rather than accepting whatever appears first!”<hr class="script-divider"><strong>ACTION:</strong> Prompt Gemini for the cricket analogy live.`,

  `<strong>PROGRESSIVE DIFFICULTY IN GEMINI:</strong><br>“You can tell AI how you want to practise.<br>Prompt: ‘Start with an easy conceptual question. Then give me a medium question. Finally give me an application-based question. Ask one at a time and wait for my answer before continuing.’<br>Easy first. Then harder. Then application. That's much more useful than simply asking: ‘Give me questions.’”<hr class="script-divider"><strong>ACTION:</strong> Trigger the 3-tier question sequence in Gemini.`,

  `<strong>GEMINI AS A SECOND OPINION:</strong><br>“If something seems confusing, you can ask another AI to explain it differently.<br>‘Explain it in simpler language and point out anything I should verify with my textbook.’<br>But remember this crucial sentence: Two AIs agreeing does not automatically make something true!<br>If an important fact, definition, or formula doesn't match your textbook, stop and check it.”<hr class="script-divider"><strong>ACTION:</strong> Reiterate the 'Two AIs agreeing &ne; True' principle.`,

  `<strong>TWO AI TOOLS, ONE STUDY METHOD:</strong><br>“You don't have to choose one AI and use it for everything.<br>ChatGPT: Tutor (Understand &rarr; Explain &rarr; Feedback).<br>Gemini: Explorer + Practice Partner (Explore &rarr; Compare &rarr; Practise).<br>And remember: Never copy both answers and call it studying! Read them. Understand them. Close the AI. Try explaining it yourself.”<hr class="script-divider"><strong>ACTION:</strong> Ask room for a quick show of hands for the 60-second challenge.`,

  `<strong>TRANSITION TO NOTEBOOKLM:</strong><br>“So far, we've been asking AI about subjects. But there's a problem: What if I don't want AI to give me info from everywhere? What if I want it to work specifically with my textbook, my notes, my study material?<br>Imagine uploading your study material and asking questions about that material.<br>ChatGPT/Gemini: ‘Tell me about this topic.’<br>NotebookLM: ‘Help me understand the material I am actually studying.’<br>Let's meet NotebookLM!”<hr class="script-divider"><strong>ACTION:</strong> Open NotebookLM interface on screen.`,

  `<strong>LIVE DEMO: GIVE IT THE MATERIAL:</strong><br>“We upload our approved Class 10 Electricity chapter PDF to NotebookLM.<br>Look at our first prompt: ‘Based only on the study material I provided, identify the key concepts I should understand before my exam. Explain each one briefly in simple language.’<br>Look at what just happened: We're not asking ‘Tell me everything about electricity.’ We're asking NotebookLM to help us understand the material we've actually provided!”<hr class="script-divider"><strong>ACTION:</strong> Upload PDF live and execute Workflow 1 prompt.`,

  `<strong>DIFFICULT SECTIONS & CITATIONS:</strong><br>“Notice the difference from what we did with ChatGPT. We're not saying ‘Explain electricity.’ We're saying: ‘Here's the material I'm studying. Help me understand this part of it.’<br>And look at the citations: NotebookLM tells you exactly which page and paragraph supports the answer. True grounded verification!”<hr class="script-divider"><strong>ACTION:</strong> Click on a citation chip live in NotebookLM to show the viewer highlight.`,

  `<strong>TURN MATERIAL INTO A REVISION GUIDE:</strong><br>“This is where NotebookLM becomes unbeatable before an exam. You've already got the material.<br>Now you tell it: ‘Based only on the study material I provided, create a concise revision guide for this chapter.’<br>In 15 seconds, you have a 1-page summary of every formula and definition in your book!”<hr class="script-divider"><strong>ACTION:</strong> Show the clean generated revision guide on screen.`,

  `<strong>SOURCED QUIZ & GAP FINDER:</strong><br>“Again, the objective isn't to get AI to answer for us. We're making AI test us on our own textbook!<br>‘Quiz me one question at a time. Do not reveal the answer until I respond.’<br>And look at the gap finder: ‘Based on my answers, identify the concepts I should revise again.’<br>Study &rarr; Test &rarr; Find weakness &rarr; Revise &rarr; Test again.”<hr class="script-divider"><strong>ACTION:</strong> Execute one quiz question from the uploaded PDF.`,

  `<strong>THE SOURCE BOUNDARY & NOTEBOOKLM LOOP:</strong><br>“Get into this habit: Tell AI what source you want it to work from: ‘Based on my study material...’ ‘According to the chapter...’<br>And remember: If your notes contain an error, AI doesn't magically fix them. So important exam formulas must still be verified with your teacher!<br>Memorize the NotebookLM loop: Upload &rarr; Understand &rarr; Concepts &rarr; Clarify &rarr; Revise &rarr; Test!”<hr class="script-divider"><strong>ACTION:</strong> Review the NotebookLM loop on screen.`,

  `<strong>THREE TOOLS, THREE USE CASES:</strong><br>“Look at how the entire workshop connects together:<br>CHATGPT: ‘Teach me.’ (Difficult concepts, explanations, feedback, practice).<br>GEMINI: ‘Help me explore.’ (Alternative explanations, examples, comparison).<br>NOTEBOOKLM: ‘Help me study this material.’ (Textbook, notes, source-based quiz).<br>Three distinct tools. One complete study arsenal!”<hr class="script-divider"><strong>ACTION:</strong> Point to each tool banner proudly.`,

  `<strong>THE TOOL IS NOT THE METHOD:</strong><br>“Tomorrow these AI tools will change. New tools will come. New versions will launch.<br>But this method is what I want you to remember:<br>UNDERSTAND &rarr; ASK &rarr; THINK &rarr; PRACTISE &rarr; ANSWER &rarr; GET FEEDBACK &rarr; FIND WEAKNESSES &rarr; REVISE &rarr; TEST AGAIN.<br>The tool is not the method. You are the student.”<hr class="script-divider"><strong>ACTION:</strong> Speak with great passion and clarity.`,

  `<strong>FINAL LINE BEFORE THE COMPUTER LAB:</strong><br>“You now have three ways to study with AI.<br>ChatGPT: Teach me.<br>Gemini: Help me explore.<br>NotebookLM: Help me work through my study material.<br>But you've only seen me do it.<br>Now it's your turn.<br>We're going to the computer lab. And I'm not going to tell you what to type.<br>I'm going to give you a problem—you have to make the AI help you solve it.<br>Let's go!”<hr class="script-divider"><strong>ACTION:</strong> Massive enthusiastic energy! Cue applause, transition to Student Lab workstations.`
];

// Document Ready
document.addEventListener('DOMContentLoaded', () => {
  initCarouselDots();
  updateSlideView();
  initLabInteractions();
  initKeyboardNavigation();
  loadSavedLabData();
  updateDynamicPrompts();
});

/* ==========================================================================
   1. AUDITORIUM SLIDE CAROUSEL LOGIC
   ========================================================================== */
function nextSlide() {
  if (appState.currentSlide < appState.totalSlides - 1) {
    appState.currentSlide++;
    updateSlideView();
  }
}

function prevSlide() {
  if (appState.currentSlide > 0) {
    appState.currentSlide--;
    updateSlideView();
  }
}

function goToSlide(index) {
  if (index >= 0 && index < appState.totalSlides) {
    appState.currentSlide = index;
    updateSlideView();
  }
}

function updateSlideView() {
  const slides = document.querySelectorAll('.carousel-slide');
  slides.forEach((slide, idx) => {
    slide.classList.toggle('active', idx === appState.currentSlide);
  });

  
  // Update Module Navigation Pills on Deck Header
  const modPills = document.querySelectorAll('#deckModuleNav .mod-pill');
  if (modPills.length > 0) {
    let activeMod = 0;
    const cur = appState.currentSlide;
    if (cur >= 0 && cur <= 4) activeMod = 0;
    else if (cur >= 5 && cur <= 16) activeMod = 1;
    else if (cur >= 17 && cur <= 19) activeMod = 2;
    else if (cur >= 20 && cur <= 26) activeMod = 3;
    else if (cur >= 27 && cur <= 32) activeMod = 4;
    else if (cur >= 33) activeMod = 5;

    modPills.forEach((p, idx) => {
      p.classList.toggle('active', idx === activeMod);
    });
  }

  // Update counters
  const curDisplay = document.getElementById('currentSlideDisplay');
  if (curDisplay) curDisplay.textContent = String(appState.currentSlide + 1).padStart(2, '0');

  // Update section badge & title from active slide dataset
  const activeSlide = slides[appState.currentSlide];
  if (activeSlide) {
    const secTag = document.getElementById('deckSectionTag');
    const titleTag = document.getElementById('deckTimingBadge');
    if (secTag && activeSlide.dataset.section) secTag.textContent = activeSlide.dataset.section;
    if (titleTag && activeSlide.dataset.title) titleTag.textContent = activeSlide.dataset.title;
  }

  // Update bottom dots
  document.querySelectorAll('.c-dot').forEach((dot, idx) => {
    dot.classList.toggle('active', idx === appState.currentSlide);
  });

  // Update progress bar
  const progressFill = document.getElementById('deckProgressFill');
  if (progressFill) {
    progressFill.style.width = `${((appState.currentSlide + 1) / appState.totalSlides) * 100}%`;
  }

  // Update presenter drawer if open
  updatePresenterDrawer();
}

function initCarouselDots() {
  const tracker = document.getElementById('carouselDotsTracker');
  if (!tracker) return;
  tracker.innerHTML = '';
  for (let i = 0; i < appState.totalSlides; i++) {
    const dot = document.createElement('div');
    dot.className = `c-dot ${i === 0 ? 'active' : ''}`;
    dot.title = `Jump to Slide ${i + 1}`;
    dot.onclick = () => goToSlide(i);
    tracker.appendChild(dot);
  }
}

function togglePresenterScript() {
  const drawer = document.getElementById('presenterDrawer');
  const label = document.getElementById('scriptToggleLabel');
  if (!drawer) return;

  const isHidden = drawer.style.display === 'none';
  drawer.style.display = isHidden ? 'flex' : 'none';
  if (label) label.textContent = isHidden ? 'Hide Presenter Script' : 'Show Presenter Script';
  if (isHidden) updatePresenterDrawer();
}

function updatePresenterDrawer() {
  const content = document.getElementById('drawerScriptContent');
  if (content && presenterScripts[appState.currentSlide]) {
    content.innerHTML = `<div><strong>[Slide ${appState.currentSlide + 1} of ${appState.totalSlides}]</strong><br>${presenterScripts[appState.currentSlide]}</div>`;
  }
}

/* Keyboard Arrow Controls */
function initKeyboardNavigation() {
  document.addEventListener('keydown', (e) => {
    // Avoid hijacking inside textarea/input
    if (['TEXTAREA', 'INPUT'].includes(document.activeElement.tagName)) return;

    if (e.key === 'f' || e.key === 'F') {
      toggleFullscreen();
      return;
    }
    if (e.key === 'p' || e.key === 'P') {
      togglePresenterScript();
      return;
    }

    if (appState.currentMode === 'deck') {
      if (e.key === 'ArrowRight' || e.key === ' ') {
        nextSlide();
      } else if (e.key === 'ArrowLeft') {
        prevSlide();
      }
    } else if (appState.currentMode === 'lab') {
      if (e.key === 'ArrowRight') nextLabMission();
      if (e.key === 'ArrowLeft') prevLabMission();
    }
  });
}

function toggleFullscreen() {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen().catch(err => {
      console.warn('Fullscreen request failed:', err);
    });
  } else {
    document.exitFullscreen();
  }
}

/* ==========================================================================
   2. MODE SWITCHER
   ========================================================================== */
function switchMainMode(modeName) {
  appState.currentMode = modeName;

  const deckEl = document.getElementById('deckContainer');
  const labEl = document.getElementById('labContainer');
  const overviewEl = document.getElementById('overviewContainer');

  const tabDeck = document.getElementById('tabDeck');
  const tabLab = document.getElementById('tabLab');
  const tabOverview = document.getElementById('tabOverview');

  if (deckEl) deckEl.style.display = (modeName === 'deck') ? 'flex' : 'none';
  if (labEl) labEl.style.display = (modeName === 'lab') ? 'block' : 'none';
  if (overviewEl) overviewEl.style.display = (modeName === 'overview') ? 'block' : 'none';

  if (tabDeck) tabDeck.classList.toggle('active', modeName === 'deck');
  if (tabLab) tabLab.classList.toggle('active', modeName === 'lab');
  if (tabOverview) tabOverview.classList.toggle('active', modeName === 'overview');

  window.scrollTo({ top: 0, behavior: 'smooth' });
}

/* ==========================================================================
   3. STUDENT LAB CAROUSEL & STEPPER
   ========================================================================== */
function nextLabMission() {
  if (appState.labStep < appState.totalLabSteps) {
    goToLabMission(appState.labStep + 1);
  }
}

function prevLabMission() {
  if (appState.labStep > 0) {
    goToLabMission(appState.labStep - 1);
  }
}

function goToLabMission(stepIdx) {
  if (stepIdx < 0 || stepIdx > appState.totalLabSteps) return;

  appState.labStep = stepIdx;

  if (stepIdx === 1 && !appState.timerRunning) {
    startLabTimer();
  }

  // Toggle active screen
  document.querySelectorAll('.lab-card-screen').forEach((screen, idx) => {
    screen.classList.toggle('active', idx === stepIdx);
  });

  // Update Stepper dots
  document.querySelectorAll('.m-dot').forEach((dot, idx) => {
    dot.classList.toggle('active', idx === stepIdx);
  });

  // Update header text
  const stepLabel = document.getElementById('labStepIndicator');
  if (stepLabel) {
    if (stepIdx === 0) stepLabel.textContent = 'Mission Setup';
    else if (stepIdx === 6) stepLabel.textContent = 'Final Submission';
    else stepLabel.textContent = `Mission 0${stepIdx} / 05`;
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });
  saveLabData();
}

function initLabInteractions() {
  // Topic input change
  const topicInput = document.getElementById('topicInput');
  if (topicInput) {
    topicInput.addEventListener('input', (e) => {
      appState.labData.topic = e.target.value.trim() || "Newton's First Law of Motion";
      updateDynamicPrompts();
      saveLabData();
    });
  }

  // Student Name
  const nameInput = document.getElementById('studentNameInput');
  if (nameInput) {
    nameInput.addEventListener('input', (e) => {
      appState.labData.studentName = e.target.value.trim();
      saveLabData();
    });
  }

  // Subject Select
  const subjectSelect = document.getElementById('subjectSelect');
  if (subjectSelect) {
    subjectSelect.addEventListener('change', (e) => {
      appState.labData.subject = e.target.value;
      saveLabData();
    });
  }

  // Quick Chips
  document.querySelectorAll('.q-chip').forEach(chip => {
    chip.addEventListener('click', () => {
      const val = chip.dataset.chip;
      appState.labData.topic = val;
      if (topicInput) topicInput.value = val;
      updateDynamicPrompts();
      saveLabData();
    });
  });

  // Class Selector Pills
  document.querySelectorAll('#classSelector .pill').forEach(pill => {
    pill.addEventListener('click', () => {
      document.querySelectorAll('#classSelector .pill').forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      appState.labData.classVal = pill.dataset.class;
      updateDynamicPrompts();
      saveLabData();
    });
  });

  // Confidence Before Pills
  document.querySelectorAll('#confBeforeSelector .pill').forEach(pill => {
    pill.addEventListener('click', () => {
      document.querySelectorAll('#confBeforeSelector .pill').forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      appState.labData.confidenceBefore = pill.dataset.conf;
      saveLabData();
    });
  });

  // Confidence After Pills
  document.querySelectorAll('#confAfterSelector .pill').forEach(pill => {
    pill.addEventListener('click', () => {
      document.querySelectorAll('#confAfterSelector .pill').forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      appState.labData.confidenceAfter = pill.dataset.conf;
      saveLabData();
    });
  });

  // AI Mindset Pills
  document.querySelectorAll('#mindsetSelector .pill').forEach(pill => {
    pill.addEventListener('click', () => {
      document.querySelectorAll('#mindsetSelector .pill').forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      appState.labData.aiMindset = pill.dataset.val;
      saveLabData();
    });
  });

  // Tool choice
  document.querySelectorAll('#m2ToolChoice .pill').forEach(pill => {
    pill.addEventListener('click', () => {
      document.querySelectorAll('#m2ToolChoice .pill').forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      appState.labData.m2_tool = pill.dataset.tool;
      saveLabData();
    });
  });

  // Autosave text fields
  const autoFields = [
    'm1_answer', 'm2_reason', 'm3_q1', 'm3_q2', 'm3_q3',
    'm4_right', 'm4_wrong', 'm4_improved', 'm5_concept', 'm5_question',
    'm6_prompt_input', 'm7_boss_q', 'm7_boss_attempt', 'm7_boss_eval',
    'refl_learned', 'refl_revise'
  ];

  autoFields.forEach(id => {
    const el = document.getElementById(id);
    if (el) {
      el.addEventListener('input', (e) => {
        appState.labData[id] = e.target.value;
        saveLabData();
      });
    }
  });

  // Copy Buttons
  document.querySelectorAll('.copy-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.dataset.target;
      const targetEl = document.getElementById(targetId);
      if (targetEl) {
        const text = targetEl.innerText || targetEl.textContent;
        navigator.clipboard.writeText(text).then(() => {
          const orig = btn.textContent;
          btn.textContent = '✓ Copied!';
          setTimeout(() => btn.textContent = orig, 2000);
        }).catch(() => alert('Prompt copied to clipboard!'));
      }
    });
  });

  // Formula Inspector for Mission 6
  const promptInput = document.getElementById('m6_prompt_input');
  if (promptInput) {
    promptInput.addEventListener('input', () => {
      const val = promptInput.value.toLowerCase();
      toggleFormulaBadge('fp-who', /(student|class|grade|i am|i'm|9|10)/i.test(val), 'WHO');
      toggleFormulaBadge('fp-what', /(current|electricity|force|motion|law|concept|chapter|topic|reaction|photosynthesis|light)/i.test(val), 'WHAT');
      toggleFormulaBadge('fp-context', /(exam|board|prepare|preparing|revision|test|study|karnataka)/i.test(val), 'CONTEXT');
      toggleFormulaBadge('fp-how', /(simple|example|analogy|real-life|cricket|pipe|bus|step-by-step|kitchen|easy)/i.test(val), 'HOW');
      toggleFormulaBadge('fp-rule', /(question|quiz|check|test|don't give|wait|one by one|one question)/i.test(val), 'RULE');
    });
  }
}

function toggleFormulaBadge(id, isMatch, label) {
  const el = document.getElementById(id);
  if (!el) return;
  el.classList.toggle('checked', isMatch);
  el.textContent = isMatch ? `✓ ${label}` : `⚪ ${label}`;
}

function updateDynamicPrompts() {
  const topic = appState.labData.topic || "Newton's First Law of Motion";
  const classVal = appState.labData.classVal || "9";

  document.querySelectorAll('.var-topic').forEach(el => el.textContent = topic);
  document.querySelectorAll('.var-class').forEach(el => el.textContent = classVal);

  const labHeaderTopic = document.getElementById('labTopicDisplay');
  if (labHeaderTopic) {
    labHeaderTopic.innerHTML = `Topic: <strong>${topic}</strong> (Class ${classVal})`;
  }
}

/* ==========================================================================
   4. LAB TIMER & BACKUP
   ========================================================================== */
function toggleLabTimer() {
  if (appState.timerRunning) {
    pauseLabTimer();
  } else {
    startLabTimer();
  }
}

function startLabTimer() {
  if (appState.timerRunning) return;
  appState.timerRunning = true;
  const btn = document.getElementById('labTimerToggleBtn');
  if (btn) btn.textContent = 'Pause';

  appState.timerInterval = setInterval(() => {
    if (appState.timerSeconds > 0) {
      appState.timerSeconds--;
      renderLabTimer();
    } else {
      pauseLabTimer();
      alert("⏱️ 60 Minutes Completed! Please wrap up and submit your mission reflection.");
    }
  }, 1000);
}

function pauseLabTimer() {
  appState.timerRunning = false;
  clearInterval(appState.timerInterval);
  const btn = document.getElementById('labTimerToggleBtn');
  if (btn) btn.textContent = 'Start';
}

function renderLabTimer() {
  const m = Math.floor(appState.timerSeconds / 60);
  const s = appState.timerSeconds % 60;
  const display = `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
  const el = document.getElementById('labTimerDigits');
  if (el) el.textContent = display;
}

function toggleBackupMode() {
  const bodies = document.querySelectorAll('.backup-body');
  if (bodies.length === 0) return;
  const isAnyHidden = Array.from(bodies).some(b => b.style.display === 'none');
  bodies.forEach(b => {
    b.style.display = isAnyHidden ? 'block' : 'none';
  });
  if (typeof showToast === 'function') {
    showToast(isAnyHidden ? 'Offline Backup Mode: ALL AI Responses Revealed' : 'Offline Backup Mode: Collapsed', '💡');
  }
}

function toggleBackupContent(id) {
  const el = document.getElementById(id);
  if (el) {
    el.style.display = (el.style.display === 'none') ? 'block' : 'none';
  }
}

function downloadStudentDossier() {
  const d = appState.labData;
  const timestamp = new Date().toLocaleString();
  const content = `=====================================================
GENIUSPHERE AI EXAM LAB — STUDENT STUDY DOSSIER
Karnataka State Board (Classes 9–10)
=====================================================
Student Name : ${d.studentName || 'Class Student'}
Class        : Class ${d.classVal || '9/10'} (${d.subject || 'Science'})
Topic        : ${d.topic || "Newton's First Law of Motion"}
Date & Time  : ${timestamp}
Confidence   : ${d.confidenceBefore || '2'}/5 (Before) ➔ ${d.confidenceAfter || '4'}/5 (After)
AI Mindset   : ${d.aiMindset || 'Help me learn'}

-----------------------------------------------------
MISSION 01: CONCEPT EXPLANATION & CHECK QUESTION
-----------------------------------------------------
Student's Understanding in Own Words:
${d.m1_answer || '(No response recorded)'}

-----------------------------------------------------
MISSION 02: AI COMPARISON (ChatGPT vs Gemini)
-----------------------------------------------------
Preferred Tool : ${d.m2_tool || 'Both'}
Reason         : ${d.m2_reason || '(No reason recorded)'}

-----------------------------------------------------
MISSION 03: SELF-TEST (EXAMINER QUESTIONS)
-----------------------------------------------------
Q1 (Easy Recall)   : ${d.m3_q1 || '(No answer)'}
Q2 (Medium Concept): ${d.m3_q2 || '(No answer)'}
Q3 (Hard Apply)    : ${d.m3_q3 || '(No answer)'}

-----------------------------------------------------
MISSION 04: CATCH MY MISTAKE (TEACHER EVALUATION)
-----------------------------------------------------
What was right : ${d.m4_right || '(None recorded)'}
What was missed: ${d.m4_wrong || '(None recorded)'}
Improved Answer:
${d.m4_improved || '(No improved answer recorded)'}

-----------------------------------------------------
MISSION 05: NOTEBOOKLM GROUNDED STUDY
-----------------------------------------------------
Key Concept Identified: ${d.m5_concept || '(None recorded)'}
Tricky Exam Question  : ${d.m5_question || '(None recorded)'}

-----------------------------------------------------
MISSION 06: UPGRADED PROMPT (5-PART FORMULA)
-----------------------------------------------------
${d.m6_prompt_input || '(No prompt crafted)'}

-----------------------------------------------------
MISSION 07: FINAL BOSS CHALLENGE
-----------------------------------------------------
Boss Question : ${d.m7_boss_q || '(None recorded)'}
My Attempt    : ${d.m7_boss_attempt || '(None recorded)'}
AI Evaluation : ${d.m7_boss_eval || '(None recorded)'}

-----------------------------------------------------
FINAL REFLECTION & BOARD EXAM PREPARATION
-----------------------------------------------------
What I understand now:
${d.refl_learned || '(None recorded)'}

What to revise from textbook:
${d.refl_revise || '(None recorded)'}

=====================================================
Rule: AI helps you prepare. YOU write the exam!
=====================================================`;

  const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  const safeTopic = (d.topic || 'science').toLowerCase().replace(/[^a-z0-9]/g, '_');
  a.download = `Geniusphere_AI_Dossier_${safeTopic}.txt`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
  if (typeof showToast === 'function') {
    showToast('📥 Study Dossier downloaded as text file!', '💾');
  }
}

/* ==========================================================================
   5. STORAGE & MISSION SUBMISSION
   ========================================================================== */
const LAB_STORAGE_KEY = 'geniusphere_lab_v3';

function saveLabData() {
  try {
    localStorage.setItem(LAB_STORAGE_KEY, JSON.stringify({
      labStep: appState.labStep,
      labData: appState.labData
    }));
  } catch (e) {
    console.warn('Storage save failed:', e);
  }
}

function loadSavedLabData() {
  try {
    const raw = localStorage.getItem(LAB_STORAGE_KEY);
    if (raw) {
      const parsed = JSON.parse(raw);
      if (parsed.labData) {
        appState.labData = { ...appState.labData, ...parsed.labData };
        populateLabInputs();
      }
      if (typeof parsed.labStep === 'number' && parsed.labStep > 0) {
        goToLabMission(parsed.labStep);
      }
    }
  } catch (e) {
    console.warn('Storage load failed:', e);
  }
}

function populateLabInputs() {
  const d = appState.labData;
  if (d.studentName) document.getElementById('studentNameInput').value = d.studentName;
  if (d.topic) document.getElementById('topicInput').value = d.topic;
  if (d.subject) document.getElementById('subjectSelect').value = d.subject;

  document.querySelectorAll('#classSelector .pill').forEach(p => {
    p.classList.toggle('active', p.dataset.class === d.classVal);
  });
  document.querySelectorAll('#confBeforeSelector .pill').forEach(p => {
    p.classList.toggle('active', p.dataset.conf === d.confidenceBefore);
  });

  const fields = [
    'm1_answer', 'm2_reason', 'm3_q1', 'm3_q2', 'm3_q3',
    'm4_right', 'm4_wrong', 'm4_improved', 'm5_concept', 'm5_question',
    'm6_prompt_input', 'm7_boss_q', 'm7_boss_attempt', 'm7_boss_eval',
    'refl_learned', 'refl_revise'
  ];

  fields.forEach(f => {
    const el = document.getElementById(f);
    if (el && d[f]) el.value = d[f];
  });
}

function submitMissionReport() {
  const d = appState.labData;
  const reportCard = document.getElementById('finalReportCard');
  const reportContent = document.getElementById('finalReportContent');
  if (!reportCard || !reportContent) return;

  const confBefore = d.confidenceBefore || '2';
  const confAfter = d.confidenceAfter || '4';
  const delta = parseInt(confAfter, 10) - parseInt(confBefore, 10);
  const deltaText = delta > 0 ? `+${delta} Levels Higher` : 'Maintained';

  reportContent.innerHTML = `
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1rem;">
      <div><strong>Student Name:</strong> ${d.studentName || 'Anonymous Student'}</div>
      <div><strong>Class:</strong> Class ${d.classVal} (${d.subject})</div>
      <div><strong>Topic Mastered:</strong> ${d.topic}</div>
      <div><strong>Confidence Shift:</strong> ${confBefore} / 5 → ${confAfter} / 5 (<strong>${deltaText}</strong>)</div>
      <div><strong>Tool Evaluated:</strong> ${d.m2_tool || 'Both'}</div>
      <div><strong>AI Role:</strong> ${d.aiMindset}</div>
    </div>
    <hr style="border: 0; border-top: 1px solid var(--border-light); margin: 0.75rem 0;">
    <p><strong>💡 What was learned:</strong> ${d.refl_learned || 'Built conceptual clarity using real-world analogies and self-questioning.'}</p>
    <p><strong>📌 Textbook gap to revise:</strong> ${d.refl_revise || 'Revise board definitions and numerical problems from textbook.'}</p>
    <p><strong>🛡️ Upgraded Prompt Created:</strong> <code style="font-family: var(--font-mono); color: var(--brand-blue);">${d.m6_prompt_input || 'I am a Class 10 student preparing for exams. Explain with an analogy and ask me 2 check questions.'}</code></p>
  `;

  reportCard.style.display = 'block';
  reportCard.scrollIntoView({ behavior: 'smooth' });
}

// Global functions for inline HTML events
window.nextSlide = nextSlide;
window.prevSlide = prevSlide;
window.goToSlide = goToSlide;
window.switchMainMode = switchMainMode;
window.togglePresenterScript = togglePresenterScript;
window.toggleFullscreen = toggleFullscreen;
window.nextLabMission = nextLabMission;
window.prevLabMission = prevLabMission;
window.goToLabMission = goToLabMission;
window.toggleLabTimer = toggleLabTimer;
window.downloadStudentDossier = downloadStudentDossier;
window.toggleAudioMute = toggleAudioMute;
window.toggleBrutalistTheme = toggleBrutalistTheme;
window.toggleBackupMode = toggleBackupMode;
window.toggleBackupContent = toggleBackupContent;
window.submitMissionReport = submitMissionReport;


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

// 2.5 Theme Switcher (Modern Clean Light / Dark)
function toggleBrutalistTheme() {
  const isDark = document.body.classList.toggle('dark-mode');
  const btn = document.getElementById('themeToggleBtn');
  if (btn) {
    btn.innerHTML = isDark ? '🌙 Dark' : '☀️ Light';
  }
  if (typeof showToast === 'function') {
    showToast(isDark ? 'Dark Mode enabled' : 'Light Mode enabled', isDark ? '🌙' : '☀️');
  }
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

// 4. Audio Control & Web Audio Harmonic Chime (Zero external dependencies)
function toggleAudioMute() {
  appState.isMuted = !appState.isMuted;
  const btn = document.getElementById('audioMuteBtn');
  if (btn) {
    btn.innerHTML = appState.isMuted ? '🔇 Muted' : '🔊 Audio';
    btn.classList.toggle('btn-primary', appState.isMuted);
    btn.classList.toggle('btn-outline', !appState.isMuted);
  }
  showToast(appState.isMuted ? 'Audio sound effects muted' : 'Audio sound effects enabled', appState.isMuted ? '🔇' : '🔊');
}

function playHarmonicChime(freq = 587.33, duration = 0.15) {
  if (appState && appState.isMuted) return;
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

// 6. Interactive Audience Voting & Option Selection with Animated Meters
function initInteractiveAudienceVoting() {
  document.addEventListener('click', (e) => {
    const optionCard = e.target.closest('.option-card, .vote-option');
    if (!optionCard) return;

    // Toggle highlight
    const parentGrid = optionCard.parentElement;
    if (parentGrid) {
      const allCards = Array.from(parentGrid.querySelectorAll('.option-card, .vote-option'));
      allCards.forEach(c => c.classList.remove('highlight', 'vo-winner'));
      optionCard.classList.add(optionCard.classList.contains('vote-option') ? 'vo-winner' : 'highlight');

      // Animate percentage bars across options in this poll
      const totalCards = allCards.length;
      allCards.forEach((c) => {
        let meter = c.querySelector('.vote-result-meter');
        if (!meter) {
          meter = document.createElement('div');
          meter.className = 'vote-result-meter';
          meter.innerHTML = `
            <div class="vote-meter-label">
              <span>Audience Vote</span>
              <span class="vote-pct-text">0%</span>
            </div>
            <div class="vote-meter-bar">
              <div class="vote-meter-fill"></div>
            </div>
          `;
          c.appendChild(meter);
        }
        const isSelected = (c === optionCard);
        const targetPct = isSelected 
          ? (totalCards === 2 ? 74 : (totalCards === 3 ? 62 : 56))
          : Math.round((100 - (totalCards === 2 ? 74 : (totalCards === 3 ? 62 : 56))) / (totalCards - 1));
        
        setTimeout(() => {
          const fill = meter.querySelector('.vote-meter-fill');
          const txt = meter.querySelector('.vote-pct-text');
          if (fill) fill.style.width = `${targetPct}%`;
          if (txt) txt.innerText = `${targetPct}%`;
        }, 50);
      });
    }

    // Sound chime
    playHarmonicChime(523.25, 0.12);

    const label = optionCard.innerText.split('\n')[0].substring(0, 30);
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

// 9. Stage 30-Second Countdown Timer
let countdownTimerId = null;
let countdownRemaining = 30;
let isCountdownRunning = false;

function toggleStageCountdown(duration = 30) {
  const btn = document.getElementById('countdownStartBtn');
  const digital = document.getElementById('countdownDigital');
  const bar = document.getElementById('countdownProgressBar');

  if (isCountdownRunning) {
    clearInterval(countdownTimerId);
    isCountdownRunning = false;
    if (btn) btn.innerText = '▶️ Resume';
    showToast('30s Stage Timer Paused', '⏸️');
    return;
  }

  if (countdownRemaining <= 0) {
    countdownRemaining = duration;
  }

  isCountdownRunning = true;
  if (btn) btn.innerText = '⏸️ Pause';
  showToast('30s Stage Challenge Started! Student to the mic!', '⚡');

  countdownTimerId = setInterval(() => {
    countdownRemaining--;
    if (digital) digital.innerText = `⏱️ ${countdownRemaining}s`;

    if (bar) {
      const pct = Math.max(0, (countdownRemaining / duration) * 100);
      bar.style.width = `${pct}%`;
      if (countdownRemaining <= 5) {
        bar.className = 'countdown-progress-bar danger';
        if (digital) digital.className = 'countdown-digital flash';
      } else if (countdownRemaining <= 12) {
        bar.className = 'countdown-progress-bar warning';
      } else {
        bar.className = 'countdown-progress-bar';
      }
    }

    if (countdownRemaining > 0 && countdownRemaining <= 5) {
      playHarmonicChime(880, 0.08);
    }

    if (countdownRemaining <= 0) {
      clearInterval(countdownTimerId);
      isCountdownRunning = false;
      if (btn) btn.innerText = '↺ Restart';
      if (digital) digital.innerText = '🔔 TIME UP!';
      playHarmonicChime(523.25, 0.3);
      setTimeout(() => playHarmonicChime(659.25, 0.3), 150);
      setTimeout(() => playHarmonicChime(783.99, 0.5), 300);
      showToast('🔔 TIME UP! Student at the microphone, reveal your prompt!', '🎯');
    }
  }, 1000);
}

function resetStageCountdown(duration = 30) {
  if (countdownTimerId) clearInterval(countdownTimerId);
  isCountdownRunning = false;
  countdownRemaining = duration;
  const btn = document.getElementById('countdownStartBtn');
  const digital = document.getElementById('countdownDigital');
  const bar = document.getElementById('countdownProgressBar');

  if (btn) btn.innerText = '▶️ Start Timer';
  if (digital) {
    digital.innerText = `⏱️ ${duration}s`;
    digital.className = 'countdown-digital';
  }
  if (bar) {
    bar.style.width = '100%';
    bar.className = 'countdown-progress-bar';
  }
  showToast('Stage Countdown Reset', '↺');
}

// 10. Student Cheatsheet Modal
function openCheatsheetModal() {
  const modal = document.getElementById('cheatsheetModal');
  if (modal) modal.classList.add('open');
}

function closeCheatsheetModal(e) {
  if (e && e.target && e.target.closest('.cheatsheet-modal-content')) return;
  const modal = document.getElementById('cheatsheetModal');
  if (modal) modal.classList.remove('open');
}

// 11. Keyboard Shortcuts Modal
function openShortcutsModal() {
  const modal = document.getElementById('shortcutsModal');
  if (modal) modal.classList.add('open');
}

function closeShortcutsModal(e) {
  if (e && e.target && e.target.closest('.sim-modal-content')) return;
  const modal = document.getElementById('shortcutsModal');
  if (modal) modal.classList.remove('open');
}

// 12. Master Keyboard Navigation
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

    if (e.key === 's' || e.key === 'S') {
      const modal = document.getElementById('socraticSimModal');
      if (modal && modal.classList.contains('open')) {
        closeSocraticSimulator();
      } else {
        openSocraticSimulator();
      }
      return;
    }

    if (e.key === 'c' || e.key === 'C') {
      const modal = document.getElementById('cheatsheetModal');
      if (modal && modal.classList.contains('open')) {
        closeCheatsheetModal();
      } else {
        openCheatsheetModal();
      }
      return;
    }

    if (e.key === 't' || e.key === 'T') {
      toggleSessionTimer();
      return;
    }

    if (e.key === 'b' || e.key === 'B') {
      toggleProjectorBoost();
      return;
    }

    if (e.key === 'd' || e.key === 'D') {
      toggleBrutalistTheme();
      return;
    }

    if (e.key === 'm' || e.key === 'M') {
      toggleAudioMute();
      return;
    }

    if (e.key === '?' || (e.shiftKey && e.key === '/')) {
      const modal = document.getElementById('shortcutsModal');
      if (modal && modal.classList.contains('open')) {
        closeShortcutsModal();
      } else {
        openShortcutsModal();
      }
      return;
    }

    if (e.key === 'Escape') {
      closeSlideNavigator();
      closeSocraticSimulator();
      closeCheatsheetModal();
      closeShortcutsModal();
      return;
    }
  });

  if (typeof oldInitKeyNav === 'function') oldInitKeyNav();
};

// Auto-start session timer on initial page load
document.addEventListener('DOMContentLoaded', () => {
  startSessionTimer();
  initInteractiveAudienceVoting();
  initClickToCopyPrompts();
});

// Expose global functions to window
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
window.toggleStageCountdown = toggleStageCountdown;
window.resetStageCountdown = resetStageCountdown;
window.openCheatsheetModal = openCheatsheetModal;
window.closeCheatsheetModal = closeCheatsheetModal;
window.openShortcutsModal = openShortcutsModal;
window.closeShortcutsModal = closeShortcutsModal;


function setSubPill(btn, containerId, val) {
  const container = document.getElementById(containerId);
  if (!container) return;
  container.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
  btn.classList.add('active');
  saveLabData();
}

function submitFinalLab() {
  const student = document.getElementById('studentNameInput')?.value.trim() || 'Student';
  const topic = document.getElementById('topicInput')?.value.trim() || "Newton's First Law of Motion";
  const problem = document.getElementById('final_problem')?.value.trim() || topic;
  const tool = document.getElementById('final_tool')?.value.trim() || 'ChatGPT / Gemini / NotebookLM';
  
  alert(`🎉 CONGRATULATIONS, ${student.toUpperCase()}!\n\nYou have completed the Geniusphere AI Exam Lab Practical (60 Minutes)!\n\nProblem Solved: ${problem}\nAI Tool Mastered: ${tool}\n\nTHE RULE OF THE LAB:\n✅ ASK → THINK → TRY → CHECK → IMPROVE\nYou didn't win by getting the answer. You won by understanding it!`);
  saveLabData();
}


// ==========================================================================
// INTERACTIVE ENHANCEMENTS: CLICK-TO-COPY, AUDIENCE VOTES, CERTIFICATE & SIM
// ==========================================================================

function copyPromptText(btn) {
  if (!btn) return;
  const box = btn.closest('.prompt-box, .prompt-terminal-card, .demo-prompt-card');
  if (!box) return;
  const textEl = box.querySelector('.prompt-text, pre code, code') || box;
  const text = (textEl.innerText || textEl.textContent || '').trim();
  
  if (text) {
    navigator.clipboard.writeText(text).then(() => {
      const origText = btn.innerHTML;
      btn.innerHTML = 'Copied! ✓';
      btn.style.backgroundColor = '#10b981';
      btn.style.color = '#ffffff';
      playHarmonicChime(659.25, 0.15);
      showToast('Prompt copied to clipboard! Ready to paste into ChatGPT/Gemini.', '📋');
      setTimeout(() => {
        btn.innerHTML = origText;
        btn.style.backgroundColor = '';
        btn.style.color = '';
      }, 2000);
    }).catch(() => {
      showToast('Prompt selected! Press Ctrl+C to copy.', '📋');
    });
  }
}

function castAudienceVote(el, pct) {
  if (!el) return;
  const grid = el.closest('.interactive-poll-grid, .options-grid');
  if (!grid) return;

  const cards = Array.from(grid.querySelectorAll('.option-card, .vote-option'));
  cards.forEach(c => c.classList.remove('highlight', 'highlight-card', 'vo-winner'));
  el.classList.add('highlight-card');

  const totalCards = cards.length;
  cards.forEach(c => {
    let meter = c.querySelector('.vote-result-meter');
    if (!meter) {
      meter = document.createElement('div');
      meter.className = 'vote-result-meter';
      meter.innerHTML = `
        <div class="vote-meter-label">
          <span>Audience Vote</span>
          <span class="vote-pct-text">0%</span>
        </div>
        <div class="vote-meter-bar">
          <div class="vote-meter-fill"></div>
        </div>
      `;
      c.appendChild(meter);
    }
    const isSelected = (c === el);
    const targetPct = isSelected ? pct : Math.max(5, Math.round((100 - pct) / (totalCards - 1)));
    
    setTimeout(() => {
      const fill = meter.querySelector('.vote-meter-fill');
      const txt = meter.querySelector('.vote-pct-text');
      if (fill) fill.style.width = `${targetPct}%`;
      if (txt) txt.innerText = `${targetPct}%`;
    }, 50);
  });

  playHarmonicChime(523.25, 0.12);
  const title = el.querySelector('strong')?.innerText || 'Option';
  showToast(`Audience Vote Recorded: ${title} (${pct}%)`, '🗳️');
}

function toggleSimResponse(boxId) {
  const box = document.getElementById(boxId);
  if (!box) return;
  const isOpen = box.classList.toggle('open');
  if (isOpen) {
    playHarmonicChime(440, 0.12);
    box.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
}

function submitFinalLab() {
  const student = document.getElementById('studentNameInput')?.value.trim() || 'Class 9/10 Student';
  const topic = document.getElementById('topicInput')?.value.trim() || "Newton's First Law of Motion";
  const problem = document.getElementById('final_problem')?.value.trim() || topic;
  const tool = document.getElementById('final_tool')?.value.trim() || 'ChatGPT, Gemini & NotebookLM';
  
  const classVal = document.querySelector('#classSelector .pill.active')?.getAttribute('data-class') || 'Class 9';
  
  // Update certificate modal elements
  const certModal = document.getElementById('studentCertModal');
  const certName = document.getElementById('certStudentName');
  const certClass = document.getElementById('certStudentClass');
  const certTopic = document.getElementById('certStudentTopic');
  const certDate = document.getElementById('certDateDisplay');
  const certGrowth = document.getElementById('certConfidenceGrowth');

  if (certName) certName.innerText = student;
  if (certClass) certClass.innerText = classVal;
  if (certTopic) certTopic.innerText = problem;
  if (certDate) {
    const today = new Date();
    certDate.innerText = today.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' });
  }
  if (certGrowth) {
    const confBefore = document.querySelector('#final_confBefore .pill.active')?.innerText || '2';
    const confAfter = document.querySelector('#final_confAfter .pill.active')?.innerText.split(' ')[0] || '5';
    const delta = Math.max(1, parseInt(confAfter, 10) - parseInt(confBefore, 10));
    certGrowth.innerText = `Confidence Growth: +${delta} Levels (${confBefore} → ${confAfter}/5)`;
  }

  // Play 3-tone celebration chime
  playHarmonicChime(523.25, 0.2);
  setTimeout(() => playHarmonicChime(659.25, 0.2), 120);
  setTimeout(() => playHarmonicChime(783.99, 0.4), 240);

  if (certModal) {
    certModal.classList.add('open');
  }

  showToast(`🎉 Congratulations, ${student}! Practical Certified.`, '🎓');
  saveLabData();
}

function closeCertModal(e) {
  if (e && e.target && e.target.closest('.cert-container')) return;
  const modal = document.getElementById('studentCertModal');
  if (modal) modal.classList.remove('open');
}

function copyCertSummary() {
  const student = document.getElementById('certStudentName')?.innerText || 'Student';
  const topic = document.getElementById('certStudentTopic')?.innerText || "Newton's First Law";
  const classVal = document.getElementById('certStudentClass')?.innerText || 'Class 9';
  const growth = document.getElementById('certConfidenceGrowth')?.innerText || 'Confidence Growth: +3 Levels';
  
  const text = `🎓 GENIUSPHERE AI EXAM LAB — PRACTICAL DOSSIER
Student: ${student} (${classVal})
Topic Mastered: ${topic}
${growth}
Core Skills Validated:
1. Formulating Persona & Context-Rich Prompts (ChatGPT)
2. Socratic Sparring & Self-Testing before Answering
3. Cross-Checking Alternative Explanations (Gemini)
4. Textbook Grounding & Sourced Verification (NotebookLM)
The Golden Rule: "You didn't win by getting the answer. You won by understanding it."`;

  navigator.clipboard.writeText(text).then(() => {
    playHarmonicChime(659.25, 0.15);
    showToast('Student dossier summary copied to clipboard!', '📋');
  });
}

window.copyPromptText = copyPromptText;
window.castAudienceVote = castAudienceVote;
window.toggleSimResponse = toggleSimResponse;
window.closeCertModal = closeCertModal;
window.copyCertSummary = copyCertSummary;
window.submitFinalLab = submitFinalLab;

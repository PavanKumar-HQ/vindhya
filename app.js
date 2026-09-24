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
  totalLabSteps: 8,
  
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
  `<strong>WALK IN WITH A QUESTION (NOT A DEFINITION):</strong><br>“Before we start, I want to ask you something.<br>How many of you have ever been studying at night, opened a chapter, read the same paragraph two or three times… and still thought: ‘I understood absolutely nothing.’<br>Pause. Let them react.<br>And then what happens? You search YouTube. You ask your friend. You message someone: ‘Bro, what is this?!’<br>Small laugh.<br>And now there's one more person you can ask... AI.”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Walk in with calm energy. Do not introduce definitions. Pause after 'absolutely nothing'.`,

  `<strong>THE 10:30 PM ICEBREAKER:</strong><br>“Look at the screen right now:<br>IT'S 10:30 PM. EXAM TOMORROW. ONE CHAPTER LEFT. YOU DON'T UNDERSTAND IT.<br>Be honest: What are you doing?<br>A — YouTube<br>B — Ask a friend<br>C — Pretend tomorrow doesn't exist<br>D — Ask AI<br>Call out your letter or raise hands!<br>If C gets votes: ‘I appreciate the honesty!’<br>If D gets most: ‘Okay, so AI is already part of your study life.’<br>Then transition: ‘But here's the question I actually want to answer today...’”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> React live to their shouted letters with humour and warmth.`,

  `<strong>THE BIG QUESTION (THE HOOK):</strong><br>“Are you using AI to study… or are you using AI to avoid studying?<br>Let that sit on screen for a moment.<br>Because there is a huge difference.<br>If you ask AI: ‘Give me the five-mark answer’, copy it, memorize it, and write it in the exam… AI did the thinking.<br>Pause.<br>But if you ask: ‘I don't understand this. Teach it to me. Give me an example. Then test me.’—YOU are still doing the learning!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Let silence sit after the hook question. This frames the entire 2 hours.`,

  `<strong>INTRODUCE THE WORKSHOP:</strong><br>“That's what we're going to do today: AI EXAM LAB. Learn with AI. Don't let AI learn for you.<br>I'm not going to spend the next two hours explaining what artificial intelligence is. You already know AI exists. You've probably already used it.<br>What I want to teach you is something much more practical:<br>How can you actually use ChatGPT, Gemini and NotebookLM to prepare for your exams?<br>We're going to use them for three things: Understand. Practise. Improve.”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Clear, confident delivery of the workshop promise.`,

  `<strong>THE ORIGINAL PHILOSOPHY & WHAT DO YOU ASK?:</strong><br>“Remember this one line throughout today's session:<br>‘The smartest use of AI isn't getting the answer faster. It's learning how to understand it better.’<br>Now look at the question on screen: When you don't understand something, what do you ask?<br>‘What is this?’ vs ‘Explain this in simple language’ vs ‘Give me an example’ vs ‘Ask me a question to see if I understood.’<br>Which one of these is actually helping you learn?<br>Exactly. And that is where we are going to start!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Point to the 4 levels, get audience agreement, then transition to Module 1!`,

  `<strong>MODULE 1: CHATGPT AS YOUR AI TUTOR:</strong><br>“Module 1: ChatGPT as your AI Tutor.<br>Purpose: Help a student when they are stuck on a chapter/topic.<br>We touch: how to ask to explain, simpler language, examples, analogies, follow-up questions, and asking AI to check whether you understood!<br>Let's look at a student struggling with Newton's First Law!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Begin the Newton's bus demonstration!`,

  `<strong>MODULE 1 PROMPT: NEWTON'S BUS ANALOGY:</strong><br>“Look at the screen. A student is struggling with Newton's First Law.<br>A weak student types: 'Explain Newton's First Law.' AI gives you a 400-word Wikipedia essay that puts you to sleep.<br>Instead, look at our Master Tutor Prompt: 'I'm a Class 9 student. I don't understand Newton's First Law. Explain it in simple language using a school-bus example. Then ask me one question to check if I understood.'<br>Look at the output: Why you fly forward when the bus brakes! Your feet stop with the bus floor, but your upper body wants to keep moving at 40 km/h! Boom—concept understood in 10 seconds!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Act out flying forward when the bus brakes! Audience will laugh.`,

  `<strong>MODULE 1: THE LEARNING CONVERSATION:</strong><br>“Never stop at one prompt! AI is not Google search where you click one link. It is an infinitely patient conversation.<br>Ask follow-ups: 'What if the bus accelerates forward?' 'Can you give me an example from cricket?' 'What does unbalanced external force mean in plain English?'<br>And look at the bottom: AI asks US a check question: 'If you throw an apple straight up inside a moving bus, does it land in your hand or behind you?'<br>Who in the audience can answer that right now? Raise your hand!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Point to an engaged student to answer the apple question!`,

  `<strong>MODULE 1: TAKEAWAY & EXAM BENEFIT:</strong><br>“What did you learn here? AI can become your interactive tutor.<br>And how does this help your board exam? In Karnataka State Board Science papers, examiners don't just ask you to state definitions for 1 mark.<br>They ask: 'Why does dust fly off a carpet when beaten with a stick?' or 'Why do passengers lean outward on sharp turns?'<br>When you truly understand via analogies, you answer 3-mark and 4-mark application questions effortlessly!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Emphasize the +3 to +4 marks leap on board papers.`,

  `<strong>MODULE 2 OVERVIEW: EXAM PRACTICE:</strong><br>“Now we move to Module 2: ChatGPT for Exam Practice.<br>The purpose: Turn AI from an explanation tool into an active practice partner.<br>Most students spend 90% of their time rereading notes. That gives you an illusion of competence.<br>Real exam success comes from active retrieval practice. In this module, we teach AI to generate board-style questions and drill us under pressure!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Transition voice from tutor tone to coach/sparring partner tone.`,

  `<strong>MODULE 2 PROMPT: THE 1-AT-A-TIME RULE:</strong><br>“Here is the sparring prompt: 'I have studied Newton's First Law. Give me 5 exam-style questions for Karnataka State Board Class 9. Ask me ONE AT A TIME. Don't give me the answer until I respond.'<br>Notice those last two sentences: Ask me one at a time. Don't give me the answer until I respond.<br>Why? Because if AI shows 5 questions with answers below, your eyes cheat automatically. One-at-a-time forces your brain to generate the answer from memory!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Emphasize the words 'ONE AT A TIME' with hands.`,

  `<strong>MODULE 2: QUESTION TIERS & MIC CHALLENGE:</strong><br>“AI can generate all 3 tiers of Karnataka Board questions:<br>Tier 1: 1-mark direct recall—Define Inertia.<br>Tier 2: 2-mark reasoning—Why does an athlete run before a long jump?<br>Tier 3: 4-mark application problems.<br>Look at Question 1 on screen: 'Why does dust fly out of a carpet when beaten with a stick?'<br>Microphone check! Handing the mic to row 2—you have 30 seconds to give a board-ready answer!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Walk towards audience with mic, let a student attempt live.`,

  `<strong>MODULE 2: TAKEAWAY & EXAM BENEFIT:</strong><br>“What did you learn? Don't just ask AI for questions and read the answers. Actually ATTEMPT them!<br>How does this help your exam? You build active practice and real exam stamina.<br>When you walk into the exam hall next week, writing answers feels completely natural because you've already answered dozens of questions under simulated pressure!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Highlight the 76% active recall retention on screen.`,

  `<strong>MODULE 3 OVERVIEW: CHECK & IMPROVE ANSWERS:</strong><br>“Now we enter Module 3: Check and Improve Your Answers.<br>In my opinion, this is the single most valuable part of today's workshop.<br>Most students ask AI: 'Write an answer for me.' That is a trap.<br>The master skill is: YOU write your own raw answer first, submit it to AI, and tell AI to act like a strict Karnataka Board examiner!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Pause for dramatic effect. 'This skill alone is worth 10 marks.'`,

  `<strong>MODULE 3 PROMPT: INERTIA AUDIT:</strong><br>“Look at what a student wrote: 'Inertia is the tendency of an object to keep doing what it is doing unless something stops it.'<br>Is that true? Yes! But will it get full marks on a Karnataka Board paper? No! It gets 1 out of 2 marks.<br>Now look at our Teacher Audit prompt: 'Check my answer like a teacher. Tell me what I got right, what I misunderstood, and what I should improve. Don't rewrite the complete answer.'<br>Look at AI's audit: It tells the student: You missed 'state of rest or uniform motion in a straight line' and 'external unbalanced force'!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Point to the missing keywords highlighted in red on screen.`,

  `<strong>MODULE 3: THE 4 PILLARS & LIVE REWRITE:</strong><br>“AI gives you feedback across 4 pillars: What is correct, What is missing, What is misunderstood, and an Actionable Hint.<br>Notice: It gave a hint, but it did NOT give the final answer!<br>The student thinks, applies the hint, and writes Version 2: 'Inertia is the inherent property of an object to resist any change in its state of rest or uniform motion in a straight line, unless acted upon by an external unbalanced force.'<br>New score: 2 out of 2 full marks!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Celebrate the 2/2 score jump on screen.`,

  `<strong>MODULE 3: TAKEAWAY & EXAM BENEFIT:</strong><br>“What did you learn? AI becomes a feedback tool, not an answer-writing machine.<br>And the exam benefit? Karnataka Board evaluators grade strictly against an official answer scheme with specific keywords.<br>By having AI audit your drafts during preparation, you catch your keyword weaknesses BEFORE the actual exam, when mistakes cost zero marks!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Emphasize: 'Catch mistakes in practice, not on report cards.'`,

  `<strong>MODULE 4 OVERVIEW: GEMINI AS SECOND TOOL:</strong><br>“Next is Module 4: Google Gemini as a Second AI Study Tool.<br>This isn't a long lecture—it's about learning never to be dependent on just one tool.<br>If you only know one AI, you get stuck when its servers go down or when its explanation doesn't make sense to your brain.<br>Gemini is built by Google, connects directly to real-time search, and structures comparisons beautifully.”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Introduce Gemini as the multi-tool companion to ChatGPT.`,

  `<strong>MODULE 4: HEAD-TO-HEAD BATTLE:</strong><br>“Let's do a live demonstration! We give both tools the exact same prompt: 'Explain electric current to a Class 10 student using an everyday example.'<br>ChatGPT gave us the Water Pipe and Pump Analogy: Voltage is water pressure, current is liters of water flowing per second.<br>Gemini gave us the Crowded School Hallway Analogy: Students marching down a corridor, teachers creating resistance.<br>Audience vote: Raise your hand if the Water Pipe made more sense? Now raise your hand if the School Hallway made more sense?”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Count hands quickly, show the 55% / 45% split on screen.`,

  `<strong>MODULE 4: THE LESSON & EVALUATION:</strong><br>“Look at the split: 55% liked water pipes, 45% liked school hallways.<br>The lesson isn't 'ChatGPT wins' or 'Gemini wins.'<br>The lesson is: Different AI tools can give different responses. Learn to evaluate and use the response that actually helps YOU learn.<br>Use ChatGPT for conversational tutoring and checking answers. Use Gemini for search grounding, tables, and alternative visual perspectives!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Point to the comparison matrix on screen.`,

  `<strong>MODULE 4: TAKEAWAY & EXAM BENEFIT:</strong><br>“What did you learn? You are not locked into one tool. You have multiple assistants.<br>And the exam benefit? Students aren't dependent on one tool. When studying complex Class 10 topics like Electricity or Heredity, you can cross-check explanations until you achieve 100% clarity.”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Affirm: 'Never let a difficult textbook chapter defeat you.'`,

  `<strong>MODULE 5 OVERVIEW: NOTEBOOKLM:</strong><br>“Now we come to Module 5: NotebookLM—Study YOUR Actual Material.<br>This is the most distinct module of the entire workshop.<br>What is the biggest flaw of ChatGPT and Gemini? They know the whole internet, so they can talk about things outside your syllabus!<br>NotebookLM is completely different: It ONLY reads the textbook PDF, notes, and chapters YOU upload. It has zero knowledge of anything else!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Hold up a physical textbook or point to PDF icon on screen.`,

  `<strong>NOTEBOOKLM WORKFLOW 1 & 2:</strong><br>“We teach 4 exact workflows in NotebookLM:<br>Workflow 1: Extract Key Concepts. You ask: 'Based only on this study material, identify the key concepts I should understand for my exam.' It pulls the exact board laws and formulas.<br>Workflow 2: Simplify Difficult Sections. You ask: 'Explain this difficult section on resistors in series in simpler language.' It breaks down the math without adding foreign concepts!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Demonstrate Workflow 1 & 2 on screen.`,

  `<strong>NOTEBOOKLM WORKFLOW 3: REVISION GUIDE:</strong><br>“Workflow 3: The 1-Page Revision Guide.<br>The night before an exam, you don't have time to re-read 40 pages of text.<br>You tell NotebookLM: 'Create a concise revision guide from this material.'<br>Look at the output: In 15 seconds, you have a clean summary of Chapter 12: Ohm's Law, series and parallel formulas, Joule's law of heating, and common examiner traps!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Highlight the 1-page summary on screen.`,

  `<strong>NOTEBOOKLM WORKFLOW 4: SOURCED QUIZ:</strong><br>“Workflow 4: The Sourced Textbook Quiz.<br>You ask: 'Quiz me one question at a time using only this material.'<br>And look at the magic: Next to every answer, NotebookLM provides a clickable citation chip: [Page 207, Paragraph 2 of your uploaded textbook].<br>Click that chip, and it highlights the exact sentence in your book! Zero hallucinations, 100% textbook truth.”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Point to citation pill [Page 207].`,

  `<strong>NOTEBOOKLM: TAKEAWAY & FLYWHEEL:</strong><br>“What did you learn? Your own study material becomes the foundation of the AI interaction.<br>And the exam benefit? Instead of asking generic AI questions, you use your actual syllabus material in a 5-step loop:<br>UNDERSTAND &rarr; EXTRACT &rarr; REVISE &rarr; PRACTISE &rarr; TEST.<br>100% of your prep time is focused on the exact text the Board examiner uses!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Chant the 5-step flywheel with the students.`,

  `<strong>MODULE 6 OVERVIEW: PROMPTING:</strong><br>“Now we reach Module 6: Prompting—How to Get Better Results.<br>Notice why we teach prompting NOW, after you've already seen the tools in action.<br>If I taught you prompting at 9:00 AM, it would have felt like boring grammar rules.<br>Now you know that AI is only as smart as your instructions. Garbage in, garbage out. Master prompt in, board-ready gold out!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Connect prompting to real tools seen in Modules 1–5.`,

  `<strong>THE 5-PART MASTER FORMULA:</strong><br>“Memorize these five ingredients for every study prompt:<br>1. WHO: Class 10 Karnataka State Board student<br>2. WHAT: Explain / Practise / Check / Revise<br>3. CONTEXT: Electricity chapter<br>4. HOW: Simple language + everyday example<br>5. RULE: Don't give the answer before I try!<br>These 5 pieces snap together like Lego blocks!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Count the 5 fingers on hand: WHO, WHAT, CONTEXT, HOW, RULE.`,

  `<strong>PROMPT SHOWDOWN: ELECTRICITY:</strong><br>“Look at the showdown on screen.<br>Bad Prompt: 'Explain electricity.' AI gives you 8 paragraphs about power grids, Maxwell equations, and Benjamin Franklin. Zero exam value!<br>Better Prompt: 'I'm a Class 10 Karnataka State Board student preparing for my Science exam. I don't understand electric current. Explain it in simple language using an everyday example. Then ask me two questions to check whether I understood. Don't give me the answers until I try.'<br>Look at that difference. Precision tutoring tailored to your exact syllabus!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Contrast the red box with the green box on screen.`,

  `<strong>MODULE 6: TAKEAWAY & EXAM BENEFIT:</strong><br>“What did you learn? Students learn how to get useful, targeted study help instead of generic AI responses.<br>And the exam benefit? You save 45 minutes every study session. No more wandering through random websites or watching 30-minute YouTube intros.<br>You get straight to board-level mastery in 60 seconds!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Snap fingers to illustrate 60-second clarity.`,

  `<strong>MODULE 7: AI VERIFICATION (MANDATORY):</strong><br>“Our final module is short, but it is 100% mandatory: AI Verification.<br>Students, listen carefully: AI CAN BE WRONG.<br>AI does not think like a human. It predicts the most likely next word. When it doesn't know, it will invent false formulas with 100% supreme confidence!<br>If you write a hallucinated AI answer on your Karnataka Board paper, the examiner gives you ZERO marks. You cannot blame ChatGPT!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Use serious, protective tone. 'You are the captain of your exam paper.'`,

  `<strong>THE STOP ➔ CHECK ➔ THINK PROTOCOL:</strong><br>“Whenever you use AI, follow this 3-step filter:<br>STOP: Don't blindly accept any explanation.<br>CHECK: Cross-check against the 3 Gold Standards: 1. Official Karnataka Board Textbook, 2. Teacher's Class Notes, 3. Past 5 Years Board Papers.<br>THINK: Does this make logical scientific sense?<br>If AI contradicts your textbook, the textbook wins 100% of the time!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Point to the 3 gold standards on screen.`,

  `<strong>THE 5 RESPONSIBLE AI RULES & EXAM BENEFIT:</strong><br>“Here are our 5 Responsible AI Rules:<br>1. Check against textbook<br>2. Check teacher's notes<br>3. Check reliable sources<br>4. Don't blindly copy<br>5. Don't put private information into AI.<br>Exam benefit: You never accidentally study an incorrect AI-generated explanation. You protect your marks, your academic integrity, and your future!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Review the 5 rules clearly.`,

  `<strong>LAB BRIEFING: TRANSITION TIME:</strong><br>“Let's recap our complete curriculum:<br>1. UNDERSTAND concepts<br>2. PRACTISE exam questions<br>3. CHECK own answers<br>4. IMPROVE and retry<br>5. STUDY YOUR MATERIAL with NotebookLM<br>6. ASK BETTER with 5-Part Prompts<br>7. VERIFY with Stop-Check-Think.<br>The auditorium phase is complete: I TAUGHT. Now we enter the computer lab: YOU DO!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Lead the energy surge! 'Time to touch the keyboards!'`,

  `<strong>THE 7 LAB MISSIONS SUMMARY:</strong><br>“In the lab, you will complete 7 hands-on missions:<br>M1: The School Bus Prompt (Newton's First Law)<br>M2: The Exam Sparring Quiz (Active recall)<br>M3: Teacher Audit & Rewrite (Inertia 2/2 marks)<br>M4: ChatGPT vs Gemini Electric Current Battle<br>M5: NotebookLM Sourced Study & 1-page summary<br>M6: 5-Part Master Prompt Challenge<br>M7: Spot-the-Hallucination & Certification!<br>Mentors are ready. 60 minutes on the clock!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Point towards the lab doors or switch to Student Lab mode.`,

  `<strong>CLOSING FINALE & THE GENIUSPHERE CODE:</strong><br>“As we conclude our auditorium session, remember the core philosophy of Geniusphere:<br>'The smartest student isn't the one who knows everything. It's the one who knows how to learn.'<br>Don't use AI to avoid thinking. Use AI to think better.<br>Thank you everyone—now let's conquer the Computer Lab!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Final applause cue! Transition directly to Student Lab tab.`
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
    else if (stepIdx === 8) stepLabel.textContent = 'Mission Complete';
    else stepLabel.textContent = `Mission 0${stepIdx} / 07`;
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

// 2.5 Theme Switcher (Neo-Brutalist Light / Dark)
function toggleBrutalistTheme() {
  const isDark = document.body.classList.toggle('dark-mode');
  const btn = document.getElementById('themeToggleBtn');
  if (btn) {
    btn.innerHTML = isDark ? '🌙 Dark' : '☀️ Light';
  }
  if (typeof showToast === 'function') {
    showToast(isDark ? 'Neo-Brutalist Dark Ink enabled' : 'Neo-Brutalist Light Paper enabled', isDark ? '🌙' : '☀️');
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


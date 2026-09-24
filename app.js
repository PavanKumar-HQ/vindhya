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
  `<strong>STAGE ENTRANCE:</strong><br>“Good morning everyone! Walk to center stage. Look out across the room.<br>Before we start today, I want to make one thing completely clear: I am not going to lecture you on what AI stands for. I’m not going to bore you with history from 1950.<br>I am going to ask you something much more real. Because right now, every single one of you has a superpower in your pocket—and almost nobody is using it right.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>HANDS UP & ICEBREAKER:</strong><br>“Look at the screen: Be honest... How many of you have already used ChatGPT, Google Gemini, or some other AI on your phone or laptop? Raise your hands high! Don't look at your teachers—nobody is taking notes!”<br><em>[Wait 3 seconds for 90% of hands to shoot up].</em><br>“Okay, keep your hands up if you've ever used AI to quickly help with homework or an assignment!” <em>[Laughter].</em><br>“Now... keep your hand up if you COMPLETELY understood 100% of whatever the AI gave you.”<br><em>[Pause. Watch 95% of hands drop down].</em><br><strong>Joke #1:</strong> “Okay, you can put your hands down. I'm not taking attendance!” <em>[Laughter].</em>`,

  `<strong>THE CORE PROBLEM:</strong><br>“Because getting an answer in 2026 is dead easy. You type three words, hit enter, and an algorithm spits out four paragraphs in three seconds.<br>But if that exact question appears on your board exam paper next month... ChatGPT isn't sitting on your desk.<br>An answer appearing on your phone screen does NOT mean learning happened in your brain.<br>Today is not about getting AI to do your work. It's about making AI help you actually study.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>EXAM CRISIS HOOK:</strong><br>“Picture a situation every single person in this auditorium has lived through:<br>Your board exam is in 7 days. You have 6 chapters left. And there's one chapter—maybe Optics, maybe Organic Chemistry, maybe Quadratic Equations—that you’ve read four times, and it still makes zero sense.<br>It's 10:30 at night. Your parents think you're studying. You're staring at the page.<br>What do you do?”`,

  `<strong>AUDIENCE SHOUT OUT:</strong><br>“Don't think. Look at the four letters. On the count of three, shout the letter that represents your real life! One, two, three—SHOUT!”<br><em>[Audience shouts loud chorus of A and B].</em><br>“I heard A very confidently! 'I'll wake up at 5:00 AM'—and then you wake up at 8:15 AM!<br>And I heard B: watching YouTube videos at 2x speed where someone explains it in 10 minutes and you feel like a genius for 20 minutes until you close the tab.<br>But notice Option D. What if Option D isn't just 'cheat on homework'?”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>THE SHIFT:</strong><br>“What if Option D wasn't an answer machine?<br>What if instead of you asking: 'Give me the answer to question 4', AI became an active sparring partner?<br>It explains. Then it asks you a question. It gives you practice. It checks your handwritten answer. And it tells you what to revise before the exam.”`,

  `<strong>THE STUDY PARTNER:</strong><br>“Imagine having a personal tutor who never gets tired, never gets frustrated, never judges you for asking the same question seven times, and is ready at 11:30 PM the night before your exam.<br>You say: 'Explain differently.' It adapts. You say: 'Test me.' It quizzes you.<br>That is what we are building today.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>THE GOLDEN RULE:</strong><br>“If you remember only one sentence from this entire two-hour masterclass, let it be this one:<br><strong>Don't use AI to avoid thinking. Use AI to think better.</strong><br>Say it with me in your head: Don't use AI to avoid thinking... use AI to think better.”`,

  `<strong>THE TEACHER ANALOGY:</strong><br>“Think about school right now.<br>Student A walks up to the staffroom: 'Sir, explain this.' What does the teacher do? They repeat the textbook lecture.<br>Student B walks up: 'Sir, I understood the first half, but I'm confused about this specific part. Can you explain using a cricket example?'<br>Which student gets the 10x better explanation? Student B!<br>You already know how to prompt. Prompting is just giving context to a teacher.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>FIRST MINI CHALLENGE:</strong><br>“Let's do our first battle: Human vs AI.<br>Question on screen: Why does ice float on water?<br>You have 10 seconds. Who wants to give their 1-sentence answer? Raise your hand!”<br><em>[Take 2 quick student answers from the microphone].</em><br>“Now let's ask AI live on the projector. Look at AI's answer: It talks about density, anomalous expansion, and open hexagonal crystal structure.<br>Look what happened: AI didn't make your thinking unnecessary. It gave you something to compare your brain against!”`,

  `<strong>THE 6 CONCRETE SKILLS SYLLABUS:</strong><br>“Look at the table on screen. This is our exact syllabus today across 6 core skills:<br>1. Understand: How to make AI explain a difficult concept at your level.<br>2. Ask: How to give AI useful context and instructions.<br>3. Study: How to turn a chapter into concepts, examples and explanations.<br>4. Practise: How to make AI generate exam questions and conduct a quiz.<br>5. Check: How to submit your own answer and get strict feedback.<br>6. Study Your Material: How to upload your textbook/notes/PDF to NotebookLM.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>AI IS NOT JUST AN ANSWER GENERATOR:</strong><br>“They don't need definitions of Artificial Intelligence. You need to know: AI can act as your Explainer, Tutor, Question Generator, Quiz Master, Answer Checker, and Revision Assistant. That is what we will master today.”`,

  `<strong>PART 2: CHATGPT AS PERSONAL TUTOR:</strong><br>“Now we enter Part 2. This is how you use ChatGPT to study.<br>Look at the difference on screen: If you type 'Explain electricity', you get college-level paragraphs that confuse you more.<br>Look at the better prompt: 'I am a Class 10 Karnataka State Board student. Explain electric current in simple language using an everyday example.'”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>THE 4 CONTEXT ANCHORS:</strong><br>“Always give ChatGPT 4 anchors:<br>1. WHO am I? Class 10 student.<br>2. WHAT do I want? Explain the concept.<br>3. LEVEL: Simple language.<br>4. FORMAT: Everyday analogy like water flowing in pipes.”`,

  `<strong>SKILL 2: ASK FOLLOW-UP QUESTIONS:</strong><br>“Here is the biggest secret students miss: DON'T START A NEW CHAT FOR EVERY QUESTION!<br>Have a real learning conversation: Start with 'Explain Newton's First Law'. When it answers, reply: 'I still don't understand inertia. Explain that part again.' Then: 'Give me a real-life example.' Then: 'Explain using cricket.' Then: 'Ask me one question to check whether I understood.' That chain is how real learning happens!”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>THE RETRIEVAL LOOP:</strong><br>“Never ask AI for answers. When AI gives you an answer, your brain relaxes into an illusion of competence. When AI asks YOU a question, your brain sweats. In the exam hall, only the sweat counts!”`,

  `<strong>JOB 05: CHECK:</strong><br>“Job 5 is Check. You write your answer down. You feed it to AI. But you give it a rule: 'Do not rewrite my answer. Tell me what keywords I missed and give me a hint so I can fix it myself.'”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>JOB 06: REVISE:</strong><br>“Job 6 is Revise. The most dangerous feeling before an exam is false confidence. You reread notes and nod along thinking you know it. AI is the sparring partner that punches through your blind spots.”`,

  `<strong>THE METHOD:</strong><br>“This is the Geniusphere Method. Memorize this loop: Understand. Practise. Answer. Check. Revise. Test again. That is how toppers prepare.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>THE TRAP & JOKE #2:</strong><br>“AI can make studying too easy. Look at the bottom line: <strong>Ctrl+C is not a study technique!</strong> If you just copy and paste, the only thing that got smarter was your clipboard, not your brain!”`,

  `<strong>TOOLKIT INTRO:</strong><br>“We don't use AI randomly. We have three distinct tools in our exam arsenal: ChatGPT, Gemini, and NotebookLM. Each has a specific superpower.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>CHATGPT PROFILE:</strong><br>“When you open ChatGPT, your mental model should be: 'Teach me.' It is your conversational tutor for back-and-forth questioning and essay/marking evaluation.”`,

  `<strong>AUDIENCE VOTE:</strong><br>“AI just gave us an explanation. What do we do next? Shout C or D! We never ask for answers—we command AI to challenge us!”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>GEMINI PROFILE:</strong><br>“When you open Google Gemini, your mental model is: 'Help me see and explore.' In Karnataka Board Science, over 35% of marks are diagrams! Gemini excels at visual reasoning and step-by-step drawing instructions.”`,

  `<strong>PART 4: GEMINI HEAD-TO-HEAD:</strong><br>“Don't treat Gemini as just 'another ChatGPT'. Let's give ChatGPT and Gemini the exact same study problem live: 'I'm a Class 10 student preparing for my Science exam. Explain electric current in simple language using an everyday example.'<br>Compare the outputs: ChatGPT uses a water pipe analogy; Gemini highlights circuit components and SI units.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>EVALUATE, DON'T BLINDLY TRUST:</strong><br>“The takeaway isn't 'which AI is number one'. The takeaway is: Different AI tools produce different responses. You must learn to evaluate the response rather than blindly trusting whichever tool you opened first!”`,

  `<strong>NOTEBOOKLM INTRO:</strong><br>“Now meet NotebookLM. This is your secret weapon. Instead of searching the wild internet, you upload your actual Karnataka Board textbook chapter PDF. AI is locked inside your syllabus with zero hallucinations!”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>THE DIVIDE:</strong><br>“Understand the divide: ChatGPT and Gemini say 'Teach me about the world'. NotebookLM says: 'Study THIS exact PDF with me for tomorrow's exam.' Both are powerful, but they serve different moments.”`,

  `<strong>RAPID DRILL:</strong><br>“Situation 1: Light bending in prism—Gemini!<br>Situation 2: 25 pages of textbook notes—NotebookLM!<br>Situation 3: Grade my 3-mark answer—ChatGPT!<br>You now know the toolbox.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>TRANSITION:</strong><br>“Enough talking about tools. Let's open our laptops, put a real chapter on screen, and actually study.”`,

  `<strong>LIVE DEMO 1 ANCHOR:</strong><br>“We anchor on one core topic: Force and Laws of Motion. Let's see what happens when a student tries to study this using AI.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>THE BAD PROMPT:</strong><br>“Look at what happens when you type two words. Is this output factually correct? Yes. Would a student struggling at 11:00 PM understand it? No! It just dumps textbook jargon right back at you.”`,

  `<strong>THE UPGRADE:</strong><br>“Now look at our upgraded prompt. We gave it who we are, what we're confused about, what example to use, and a strict rule: do not spoil the answer until I try.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>WHAT CHANGED:</strong><br>“Ask the room: Did we magically upgrade the AI algorithm? No! We simply gave it clearer constraints. When you change how you ask, you change how you learn.”`,

  `<strong>CRICKET TEST:</strong><br>“Look at the screen: AI asks US: If a cricket ball is rolling on an infinite frictionless glass pitch, when will it stop?<br>Shout out your answers! Someone says 'Never!' Exactly—until an unbalanced force acts on it.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>THE ACTIVE EQUATION:</strong><br>“Look at what is happening on stage: AI explains, YOU think. AI questions, YOU answer. Who is doing the heavy lifting? YOU are.”`,

  `<strong>CATCH MY ANSWER:</strong><br>“Look at this student answer: 'Passengers fall forward because the bus pushed them.' Did the bus push them? Shout YES or NO!<br>NO! The bus stopped; their upper body simply continued moving! Now watch AI critique this answer live without giving the full solution.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>THREE LEVELS:</strong><br>“Level 1 is cheating. Level 2 is watching someone else lift weights. Level 3 is lifting the weights yourself with a coach standing over you.”`,

  `<strong>STAGE CHALLENGE:</strong><br>“You have 30 seconds. Turn this terrible 2-word prompt 'Explain electricity' into a master study prompt. Who wants to come to the mic?” <em>[Bring 1 student up to read their prompt].</em><hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>EXAM READINESS CHECK:</strong><br>“You understand the concept. Great! Does that mean you will score full marks in your Karnataka Board exam next week?<br>Absolutely not! Because exams don't test what you vaguely understand in your head—exams grade what you write with a pen on paper under time pressure.”`,

  `<strong>EXAMINER MODE:</strong><br>“We now switch AI from tutor mode to strict examiner mode. Watch how it generates board-pattern questions.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>KEYWORD DRILL:</strong><br>“Look at the question AI gave us. What is the exact scientific keyword? Shout it out!<br>INERTIA OF MOTION! Perfect!”`,

  `<strong>STRICT EVALUATION:</strong><br>“Watch the screen: We entered a sloppy answer. AI gives us 1 out of 2 marks. Why? Because we explained the idea, but forgot the formal term 'inertia of motion'. It highlights the missing keyword in red.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>REFRAMING MISTAKES:</strong><br>“In school, getting an answer wrong feels embarrassing. In AI Exam Lab, a wrong answer is gold! Because every mistake you make in front of AI today is a mistake you will NOT make in your board exam next month.”`,

  `<strong>THE REVISION LOOP:</strong><br>“Study, try, get feedback, fix, try again. Do this three times per chapter, and your exam anxiety disappears.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>AUDIENCE SHOUT OUT:</strong><br>“Don't think—shout the letter! Who is actually training their brain?<br>Student C! Student A has an optical illusion; Student B is a printer; Student D is doomed. Be Student C!”`,

  `<strong>EMERGENCY WORKFLOW:</strong><br>“When you have 2 hours left before bed, you don't read 60 pages. You upload your chapter, ask AI for the 5 highest-yield exam questions, attempt them, check your keyword gaps, and sleep with confidence.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>NOTEBOOKLM HOOK:</strong><br>“Now we enter the most powerful section of this workshop. What if you didn't have to trust the open internet? What if AI only knew YOUR textbook?”`,

  `<strong>NOTEBOOKLM ARCHITECTURE:</strong><br>“Look at NotebookLM: You upload the PDF. It creates a private knowledge brain. It will not quote American textbooks, it will not quote CBSE if you're State Board. It speaks only your syllabus.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>LIVE DEMO NOTEBOOKLM:</strong><br>“Watch the screen: In 4 seconds, NotebookLM extracts the 3 core pillars of the chapter with page citations. What would normally take 45 minutes of skimming happens in seconds.”`,

  `<strong>TARGETING CONFUSION:</strong><br>“Notice the instruction: 'Stay 100% faithful to my textbook.' It gives an analogy, but uses the exact terminology our board examiners require.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>REVISION SHEET:</strong><br>“Look at this output: Formulas, SI units, and the exact traps where students lose marks. That is your night-before summary sheet.”`,

  `<strong>WOULD YOU RATHER & JOKE #3:</strong><br>“Shout it out! Would you rather read 20 pages again or have NotebookLM quiz you on those 20 pages?” <em>[Audience shouts QUIZ].</em><br>“Good. Your textbook just became an examiner! And unlike your teacher, it doesn't get tired of asking you the same question four times!” <em>[Laughter].</em><hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>PROMPT AUDIT:</strong><br>“Look at this prompt: 'Explain electricity.' What is wrong with this? Shout out!<br>Too broad! No class! No exam context! No format! If you ask a broad question, you get a boring essay.”`,

  `<strong>PROMPT EVOLUTION:</strong><br>“Look at how we evolve the prompt: Add grade &rarr; add analogy &rarr; add topic focus &rarr; add testing rule. Prompting is just clear communication.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>THE 5-PART FORMULA:</strong><br>“Remember these five letters: WHO, WHAT, CONTEXT, HOW, RULE. If you include these five, your AI study sessions will be 10x more effective than anyone else's.”`,

  `<strong>TEACHER ANALOGY:</strong><br>“Remember: Better questions create better learning. Garbage in, garbage out. Quality in, distinction out.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>PROMPT BATTLE:</strong><br>“Left side of auditorium vs Right side! You have 45 seconds with the person sitting next to you. Construct the ultimate prompt for Refraction through a Glass Slab using our 5-part formula. Go!” <em>[Pick 1 student from each side].</em>`,

  `<strong>CONTROL THE CONVERSATION:</strong><br>“Look at this prompt: You aren't just asking a question—you are designing your own adaptive learning algorithm! You control the AI, AI does not control you.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>NON-NEGOTIABLE RULE:</strong><br>“Why is 'do not rewrite my answer' non-negotiable? Because the moment AI writes it for you, you stop thinking. You must be the one holding the pen.”`,

  `<strong>CAN YOU TRUST AI?:</strong><br>“Look at the screen: Can you trust AI 100% for your board exams? Shout YES, NO, or IT DEPENDS!<br>The room shouted IT DEPENDS and NO! You are 100% correct.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>CONFIDENT != CORRECT:</strong><br>“Remember this punchline: Confident does not mean correct! AI is a language prediction engine. It predicts words that sound convincing. It has no idea if an answer is true or false unless grounded.”`,

  `<strong>CATCH THE AI:</strong><br>“Look at what AI claimed: It says desert plants open stomata during peak daytime sunlight!<br>Who spots the flaw? Hands up!<br>If they open stomata in the midday desert sun, all their water evaporates through transpiration! They open stomata at NIGHT to take in CO2 and store it as an intermediate acid!<br>If you wrote AI's answer in your board exam, you would get zero marks!”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>PART 7: 5 RESPONSIBLE AI RULES:</strong><br>“Five simple, non-negotiable rules for your exam prep:<br>1. AI can be wrong.<br>2. Don't blindly copy.<br>3. Always verify against your Karnataka Board textbook.<br>4. Try answering yourself before asking AI.<br>5. Never paste passwords, OTPs, or private personal data into AI prompts!”`,

  `<strong>THE PROTOCOL:</strong><br>“Whenever AI gives you an answer, follow our protocol: STOP. CHECK. THINK. Stop before writing. Check against your approved syllabus. Think with your own logic.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>RESPONSIBLE RULES:</strong><br>“Five simple ethical rules. Follow these, and AI becomes the greatest academic accelerator of your life.”`,

  `<strong>YOUR MISSION:</strong><br>“We are done with theory. Now you enter the computer lab.<br>🚨 YOUR MISSION: Pick ONE chapter you hate.<br><em>[Pause. Room laughs].</em><br>Yes. That one! The chapter you keep telling your parents you'll study tomorrow. That is the one we are conquering today.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>5 LAB STEPS:</strong><br>“Five practical missions in the lab. You explain, you quiz, you answer, you check, you eliminate the gap.”`,

  `<strong>THE CORE SHIFT:</strong><br>“The auditorium was: I TEACH. The computer lab is: YOU DO!<br>We just taught you the 6 skills across ChatGPT, Gemini, and NotebookLM. Now you have 60 minutes in the lab to prove you can do them on your own Karnataka Board syllabus!”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>LAUNCH CALL:</strong><br>“No more slides. No more watching.<br>Head to your computers, open Mission 1, and conquer your toughest chapter!”`,

  `<strong>CLOSING QUOTE:</strong><br>“Remember: The smartest student isn't the one who knows everything. It's the one who knows how to learn.<br>Let's make AI work for our exams. Thank you everyone!”`
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


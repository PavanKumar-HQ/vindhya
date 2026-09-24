import re

new_scripts = [
    # 01
    """<strong>STAGE ENTRANCE & ICEBREAKER:</strong><br>“Good morning everyone! Walk to center stage. Look out across the room.<br>Before we start today, I want to make one thing completely clear: I am not here to lecture you on what AI stands for, and I am not going to bore you with history from 1950.<br>Let's do an honest reality check right now: Hands in the air if you have ever used ChatGPT to finish your homework in 30 seconds! Be honest, we won't tell your teachers.<br>Now... keep your hands UP if you actually understood what you submitted and could write it in an exam right now? Look around the room—almost every hand drops! Today, we fix that forever.”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Smile, observe the dropping hands, point to the 8% meter on screen.""",

    # 02
    """<strong>THE RELATABLE NIGHTMARE:</strong><br>“Picture this scenario: It's Sunday night, 10:30 PM. Your Science exam is in 7 days. You have 4 huge chapters left. You open the textbook and read: 'The rate of change of momentum is proportional to the impressed force...'<br>You read it 5 times. Your eyes are moving across the page, but your brain is completely asleep.<br>Here is the scientific truth: Rereading gives you a fake sense of security. Recognition is NOT recall. When you sit in the exam hall, the question is twisted slightly, and your mind goes blank.”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Gesture tiredness, point to the 18% retention meter.""",

    # 03
    """<strong>WHAT'S YOUR MOVE? AUDIENCE POLL:</strong><br>“So when you hit that wall at night, what do you do? Shout your letter!<br>A: Reread it 10 times and pray?<br>B: Copy an answer guide blindly without understanding?<br>C: Panic, open Instagram reels, and feel guilty at 1 AM?<br>Or D: Use AI the right way as a 24/7 personal study partner sitting right next to you?<br>Look at the screen—84% of smart students pick D, but only if you know the exact method!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Click Option D on the screen to trigger the live audience vote chime!""",

    # 04
    """<strong>THE #1 WORKSHOP LAW:</strong><br>“Before we touch a single AI tool, memorize this golden law: AI is a bicycle for your brain—NOT a wheelchair.<br>If you ask AI to pedal for you, your mental muscles become weak. When you enter the Board exam hall, there is no WiFi and no ChatGPT. You are on your own.<br>Today, you will not learn how to make AI think FOR you. You will learn how to make AI coach you to think faster, clearer, and deeper than ever before.”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Speak with conviction. Point to the Passive vs Active comparison.""",

    # 05
    """<strong>THE 7-SKILL CURRICULUM ROADMAP:</strong><br>“Here is our complete roadmap for today. We have divided our master curriculum into 7 concrete skills:<br>1. UNDERSTAND with ChatGPT & Gemini<br>2. PRACTISE with board-level exam quizzes<br>3. CHECK by evaluating your own answers<br>4. IMPROVE by identifying mistakes and rewriting<br>5. STUDY YOUR MATERIAL with NotebookLM<br>6. ASK BETTER with our 5-Part Master Prompt Formula<br>7. VERIFY with the Stop, Check, Think protocol.<br>45 minutes on stage, followed by 60 minutes in the computer lab where YOU execute every single one!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Walk through the 7 pills on screen briskly.""",

    # 06
    """<strong>MODULE 1 OVERVIEW: UNDERSTAND CONCEPTS:</strong><br>“Let's begin with Module 1: ChatGPT for Understanding Difficult Concepts.<br>The purpose here is simple: What do you do when you are stuck on a difficult chapter at home?<br>Textbooks explain things in formal academic jargon. If you don't understand paragraph 1, you can't understand paragraph 2.<br>In this module, you will learn 5 skills: asking for explanations, simpler language, everyday analogies, follow-up questions, and the understanding check!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Emphasize that textbooks are static, but AI is interactive.""",

    # 07
    """<strong>MODULE 1 PROMPT: NEWTON'S BUS ANALOGY:</strong><br>“Look at the screen. A student is struggling with Newton's First Law.<br>A weak student types: 'Explain Newton's First Law.' AI gives you a 400-word Wikipedia essay that puts you to sleep.<br>Instead, look at our Master Tutor Prompt: 'I'm a Class 9 student. I don't understand Newton's First Law. Explain it in simple language using a school-bus example. Then ask me one question to check if I understood.'<br>Look at the output: Why you fly forward when the bus brakes! Your feet stop with the bus floor, but your upper body wants to keep moving at 40 km/h! Boom—concept understood in 10 seconds!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Act out flying forward when the bus brakes! Audience will laugh.""",

    # 08
    """<strong>MODULE 1: THE LEARNING CONVERSATION:</strong><br>“Never stop at one prompt! AI is not Google search where you click one link. It is an infinitely patient conversation.<br>Ask follow-ups: 'What if the bus accelerates forward?' 'Can you give me an example from cricket?' 'What does unbalanced external force mean in plain English?'<br>And look at the bottom: AI asks US a check question: 'If you throw an apple straight up inside a moving bus, does it land in your hand or behind you?'<br>Who in the audience can answer that right now? Raise your hand!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Point to an engaged student to answer the apple question!""",

    # 09
    """<strong>MODULE 1: TAKEAWAY & EXAM BENEFIT:</strong><br>“What did you learn here? AI can become your interactive tutor.<br>And how does this help your board exam? In Karnataka State Board Science papers, examiners don't just ask you to state definitions for 1 mark.<br>They ask: 'Why does dust fly off a carpet when beaten with a stick?' or 'Why do passengers lean outward on sharp turns?'<br>When you truly understand via analogies, you answer 3-mark and 4-mark application questions effortlessly!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Emphasize the +3 to +4 marks leap on board papers.""",

    # 10
    """<strong>MODULE 2 OVERVIEW: EXAM PRACTICE:</strong><br>“Now we move to Module 2: ChatGPT for Exam Practice.<br>The purpose: Turn AI from an explanation tool into an active practice partner.<br>Most students spend 90% of their time rereading notes. That gives you an illusion of competence.<br>Real exam success comes from active retrieval practice. In this module, we teach AI to generate board-style questions and drill us under pressure!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Transition voice from tutor tone to coach/sparring partner tone.""",

    # 11
    """<strong>MODULE 2 PROMPT: THE 1-AT-A-TIME RULE:</strong><br>“Here is the sparring prompt: 'I have studied Newton's First Law. Give me 5 exam-style questions for Karnataka State Board Class 9. Ask me ONE AT A TIME. Don't give me the answer until I respond.'<br>Notice those last two sentences: Ask me one at a time. Don't give me the answer until I respond.<br>Why? Because if AI shows 5 questions with answers below, your eyes cheat automatically. One-at-a-time forces your brain to generate the answer from memory!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Emphasize the words 'ONE AT A TIME' with hands.""",

    # 12
    """<strong>MODULE 2: QUESTION TIERS & MIC CHALLENGE:</strong><br>“AI can generate all 3 tiers of Karnataka Board questions:<br>Tier 1: 1-mark direct recall—Define Inertia.<br>Tier 2: 2-mark reasoning—Why does an athlete run before a long jump?<br>Tier 3: 4-mark application problems.<br>Look at Question 1 on screen: 'Why does dust fly out of a carpet when beaten with a stick?'<br>Microphone check! Handing the mic to row 2—you have 30 seconds to give a board-ready answer!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Walk towards audience with mic, let a student attempt live.""",

    # 13
    """<strong>MODULE 2: TAKEAWAY & EXAM BENEFIT:</strong><br>“What did you learn? Don't just ask AI for questions and read the answers. Actually ATTEMPT them!<br>How does this help your exam? You build active practice and real exam stamina.<br>When you walk into the exam hall next week, writing answers feels completely natural because you've already answered dozens of questions under simulated pressure!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Highlight the 76% active recall retention on screen.""",

    # 14
    """<strong>MODULE 3 OVERVIEW: CHECK & IMPROVE ANSWERS:</strong><br>“Now we enter Module 3: Check and Improve Your Answers.<br>In my opinion, this is the single most valuable part of today's workshop.<br>Most students ask AI: 'Write an answer for me.' That is a trap.<br>The master skill is: YOU write your own raw answer first, submit it to AI, and tell AI to act like a strict Karnataka Board examiner!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Pause for dramatic effect. 'This skill alone is worth 10 marks.'""",

    # 15
    """<strong>MODULE 3 PROMPT: INERTIA AUDIT:</strong><br>“Look at what a student wrote: 'Inertia is the tendency of an object to keep doing what it is doing unless something stops it.'<br>Is that true? Yes! But will it get full marks on a Karnataka Board paper? No! It gets 1 out of 2 marks.<br>Now look at our Teacher Audit prompt: 'Check my answer like a teacher. Tell me what I got right, what I misunderstood, and what I should improve. Don't rewrite the complete answer.'<br>Look at AI's audit: It tells the student: You missed 'state of rest or uniform motion in a straight line' and 'external unbalanced force'!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Point to the missing keywords highlighted in red on screen.""",

    # 16
    """<strong>MODULE 3: THE 4 PILLARS & LIVE REWRITE:</strong><br>“AI gives you feedback across 4 pillars: What is correct, What is missing, What is misunderstood, and an Actionable Hint.<br>Notice: It gave a hint, but it did NOT give the final answer!<br>The student thinks, applies the hint, and writes Version 2: 'Inertia is the inherent property of an object to resist any change in its state of rest or uniform motion in a straight line, unless acted upon by an external unbalanced force.'<br>New score: 2 out of 2 full marks!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Celebrate the 2/2 score jump on screen.""",

    # 17
    """<strong>MODULE 3: TAKEAWAY & EXAM BENEFIT:</strong><br>“What did you learn? AI becomes a feedback tool, not an answer-writing machine.<br>And the exam benefit? Karnataka Board evaluators grade strictly against an official answer scheme with specific keywords.<br>By having AI audit your drafts during preparation, you catch your keyword weaknesses BEFORE the actual exam, when mistakes cost zero marks!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Emphasize: 'Catch mistakes in practice, not on report cards.'""",

    # 18
    """<strong>MODULE 4 OVERVIEW: GEMINI AS SECOND TOOL:</strong><br>“Next is Module 4: Google Gemini as a Second AI Study Tool.<br>This isn't a long lecture—it's about learning never to be dependent on just one tool.<br>If you only know one AI, you get stuck when its servers go down or when its explanation doesn't make sense to your brain.<br>Gemini is built by Google, connects directly to real-time search, and structures comparisons beautifully.”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Introduce Gemini as the multi-tool companion to ChatGPT.""",

    # 19
    """<strong>MODULE 4: HEAD-TO-HEAD BATTLE:</strong><br>“Let's do a live demonstration! We give both tools the exact same prompt: 'Explain electric current to a Class 10 student using an everyday example.'<br>ChatGPT gave us the Water Pipe and Pump Analogy: Voltage is water pressure, current is liters of water flowing per second.<br>Gemini gave us the Crowded School Hallway Analogy: Students marching down a corridor, teachers creating resistance.<br>Audience vote: Raise your hand if the Water Pipe made more sense? Now raise your hand if the School Hallway made more sense?”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Count hands quickly, show the 55% / 45% split on screen.""",

    # 20
    """<strong>MODULE 4: THE LESSON & EVALUATION:</strong><br>“Look at the split: 55% liked water pipes, 45% liked school hallways.<br>The lesson isn't 'ChatGPT wins' or 'Gemini wins.'<br>The lesson is: Different AI tools can give different responses. Learn to evaluate and use the response that actually helps YOU learn.<br>Use ChatGPT for conversational tutoring and checking answers. Use Gemini for search grounding, tables, and alternative visual perspectives!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Point to the comparison matrix on screen.""",

    # 21
    """<strong>MODULE 4: TAKEAWAY & EXAM BENEFIT:</strong><br>“What did you learn? You are not locked into one tool. You have multiple assistants.<br>And the exam benefit? Students aren't dependent on one tool. When studying complex Class 10 topics like Electricity or Heredity, you can cross-check explanations until you achieve 100% clarity.”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Affirm: 'Never let a difficult textbook chapter defeat you.'""",

    # 22
    """<strong>MODULE 5 OVERVIEW: NOTEBOOKLM:</strong><br>“Now we come to Module 5: NotebookLM—Study YOUR Actual Material.<br>This is the most distinct module of the entire workshop.<br>What is the biggest flaw of ChatGPT and Gemini? They know the whole internet, so they can talk about things outside your syllabus!<br>NotebookLM is completely different: It ONLY reads the textbook PDF, notes, and chapters YOU upload. It has zero knowledge of anything else!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Hold up a physical textbook or point to PDF icon on screen.""",

    # 23
    """<strong>NOTEBOOKLM WORKFLOW 1 & 2:</strong><br>“We teach 4 exact workflows in NotebookLM:<br>Workflow 1: Extract Key Concepts. You ask: 'Based only on this study material, identify the key concepts I should understand for my exam.' It pulls the exact board laws and formulas.<br>Workflow 2: Simplify Difficult Sections. You ask: 'Explain this difficult section on resistors in series in simpler language.' It breaks down the math without adding foreign concepts!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Demonstrate Workflow 1 & 2 on screen.""",

    # 24
    """<strong>NOTEBOOKLM WORKFLOW 3: REVISION GUIDE:</strong><br>“Workflow 3: The 1-Page Revision Guide.<br>The night before an exam, you don't have time to re-read 40 pages of text.<br>You tell NotebookLM: 'Create a concise revision guide from this material.'<br>Look at the output: In 15 seconds, you have a clean summary of Chapter 12: Ohm's Law, series and parallel formulas, Joule's law of heating, and common examiner traps!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Highlight the 1-page summary on screen.""",

    # 25
    """<strong>NOTEBOOKLM WORKFLOW 4: SOURCED QUIZ:</strong><br>“Workflow 4: The Sourced Textbook Quiz.<br>You ask: 'Quiz me one question at a time using only this material.'<br>And look at the magic: Next to every answer, NotebookLM provides a clickable citation chip: [Page 207, Paragraph 2 of your uploaded textbook].<br>Click that chip, and it highlights the exact sentence in your book! Zero hallucinations, 100% textbook truth.”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Point to citation pill [Page 207].""",

    # 26
    """<strong>NOTEBOOKLM: TAKEAWAY & FLYWHEEL:</strong><br>“What did you learn? Your own study material becomes the foundation of the AI interaction.<br>And the exam benefit? Instead of asking generic AI questions, you use your actual syllabus material in a 5-step loop:<br>UNDERSTAND &rarr; EXTRACT &rarr; REVISE &rarr; PRACTISE &rarr; TEST.<br>100% of your prep time is focused on the exact text the Board examiner uses!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Chant the 5-step flywheel with the students.""",

    # 27
    """<strong>MODULE 6 OVERVIEW: PROMPTING:</strong><br>“Now we reach Module 6: Prompting—How to Get Better Results.<br>Notice why we teach prompting NOW, after you've already seen the tools in action.<br>If I taught you prompting at 9:00 AM, it would have felt like boring grammar rules.<br>Now you know that AI is only as smart as your instructions. Garbage in, garbage out. Master prompt in, board-ready gold out!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Connect prompting to real tools seen in Modules 1–5.""",

    # 28
    """<strong>THE 5-PART MASTER FORMULA:</strong><br>“Memorize these five ingredients for every study prompt:<br>1. WHO: Class 10 Karnataka State Board student<br>2. WHAT: Explain / Practise / Check / Revise<br>3. CONTEXT: Electricity chapter<br>4. HOW: Simple language + everyday example<br>5. RULE: Don't give the answer before I try!<br>These 5 pieces snap together like Lego blocks!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Count the 5 fingers on hand: WHO, WHAT, CONTEXT, HOW, RULE.""",

    # 29
    """<strong>PROMPT SHOWDOWN: ELECTRICITY:</strong><br>“Look at the showdown on screen.<br>Bad Prompt: 'Explain electricity.' AI gives you 8 paragraphs about power grids, Maxwell equations, and Benjamin Franklin. Zero exam value!<br>Better Prompt: 'I'm a Class 10 Karnataka State Board student preparing for my Science exam. I don't understand electric current. Explain it in simple language using an everyday example. Then ask me two questions to check whether I understood. Don't give me the answers until I try.'<br>Look at that difference. Precision tutoring tailored to your exact syllabus!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Contrast the red box with the green box on screen.""",

    # 30
    """<strong>MODULE 6: TAKEAWAY & EXAM BENEFIT:</strong><br>“What did you learn? Students learn how to get useful, targeted study help instead of generic AI responses.<br>And the exam benefit? You save 45 minutes every study session. No more wandering through random websites or watching 30-minute YouTube intros.<br>You get straight to board-level mastery in 60 seconds!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Snap fingers to illustrate 60-second clarity.""",

    # 31
    """<strong>MODULE 7: AI VERIFICATION (MANDATORY):</strong><br>“Our final module is short, but it is 100% mandatory: AI Verification.<br>Students, listen carefully: AI CAN BE WRONG.<br>AI does not think like a human. It predicts the most likely next word. When it doesn't know, it will invent false formulas with 100% supreme confidence!<br>If you write a hallucinated AI answer on your Karnataka Board paper, the examiner gives you ZERO marks. You cannot blame ChatGPT!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Use serious, protective tone. 'You are the captain of your exam paper.'""",

    # 32
    """<strong>THE STOP ➔ CHECK ➔ THINK PROTOCOL:</strong><br>“Whenever you use AI, follow this 3-step filter:<br>STOP: Don't blindly accept any explanation.<br>CHECK: Cross-check against the 3 Gold Standards: 1. Official Karnataka Board Textbook, 2. Teacher's Class Notes, 3. Past 5 Years Board Papers.<br>THINK: Does this make logical scientific sense?<br>If AI contradicts your textbook, the textbook wins 100% of the time!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Point to the 3 gold standards on screen.""",

    # 33
    """<strong>THE 5 RESPONSIBLE AI RULES & EXAM BENEFIT:</strong><br>“Here are our 5 Responsible AI Rules:<br>1. Check against textbook<br>2. Check teacher's notes<br>3. Check reliable sources<br>4. Don't blindly copy<br>5. Don't put private information into AI.<br>Exam benefit: You never accidentally study an incorrect AI-generated explanation. You protect your marks, your academic integrity, and your future!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Review the 5 rules clearly.""",

    # 34
    """<strong>LAB BRIEFING: TRANSITION TIME:</strong><br>“Let's recap our complete curriculum:<br>1. UNDERSTAND concepts<br>2. PRACTISE exam questions<br>3. CHECK own answers<br>4. IMPROVE and retry<br>5. STUDY YOUR MATERIAL with NotebookLM<br>6. ASK BETTER with 5-Part Prompts<br>7. VERIFY with Stop-Check-Think.<br>The auditorium phase is complete: I TAUGHT. Now we enter the computer lab: YOU DO!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Lead the energy surge! 'Time to touch the keyboards!'""",

    # 35
    """<strong>THE 7 LAB MISSIONS SUMMARY:</strong><br>“In the lab, you will complete 7 hands-on missions:<br>M1: The School Bus Prompt (Newton's First Law)<br>M2: The Exam Sparring Quiz (Active recall)<br>M3: Teacher Audit & Rewrite (Inertia 2/2 marks)<br>M4: ChatGPT vs Gemini Electric Current Battle<br>M5: NotebookLM Sourced Study & 1-page summary<br>M6: 5-Part Master Prompt Challenge<br>M7: Spot-the-Hallucination & Certification!<br>Mentors are ready. 60 minutes on the clock!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Point towards the lab doors or switch to Student Lab mode.""",

    # 36
    """<strong>CLOSING FINALE & THE GENIUSPHERE CODE:</strong><br>“As we conclude our auditorium session, remember the core philosophy of Geniusphere:<br>'The smartest student isn't the one who knows everything. It's the one who knows how to learn.'<br>Don't use AI to avoid thinking. Use AI to think better.<br>Thank you everyone—now let's conquer the Computer Lab!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Final applause cue! Transition directly to Student Lab tab."""
]

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx = js.find('const presenterScripts = [')
end_idx = js.find('];', idx)

if idx == -1 or end_idx == -1:
    print('Error: presenterScripts not found in app.js')
    exit(1)

formatted_scripts = 'const presenterScripts = [\n' + ',\n\n'.join(f'  `{s}`' for s in new_scripts) + '\n];'

updated_js = js[:idx] + formatted_scripts + js[end_idx+2:]

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(updated_js)

print(f'Successfully updated app.js with {len(new_scripts)} synced presenter scripts!')

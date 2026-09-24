#!/usr/bin/env python3
"""
Synchronize presenterScripts in app.js with the updated 6 Core Skills and 7-Part Teaching Architecture.
"""
import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Slide 5 script (index 4 or index 5)
old_script5 = """  `<strong>SECTION 2 INTRO:</strong><br>“So let's move past the hype. What can AI actually do for a Class 9 or 10 student facing board exams?”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>SIX JOBS OVERVIEW:</strong><br>“AI has six clear jobs for your study routine. Notice what is NOT on this list: 'Write my essay for me' or 'Do my homework'. Let's walk through them.”`,"""

new_script5 = """  `<strong>THE 6 CONCRETE SKILLS SYLLABUS:</strong><br>“Look at the table on screen. This is our exact syllabus today across 6 core skills:<br>1. Understand: How to make AI explain a difficult concept at your level.<br>2. Ask: How to give AI useful context and instructions.<br>3. Study: How to turn a chapter into concepts, examples and explanations.<br>4. Practise: How to make AI generate exam questions and conduct a quiz.<br>5. Check: How to submit your own answer and get strict feedback.<br>6. Study Your Material: How to upload your textbook/notes/PDF to NotebookLM.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>AI IS NOT JUST AN ANSWER GENERATOR:</strong><br>“They don't need definitions of Artificial Intelligence. You need to know: AI can act as your Explainer, Tutor, Question Generator, Quiz Master, Answer Checker, and Revision Assistant. That is what we will master today.”`,"""

if old_script5 in js:
    js = js.replace(old_script5, new_script5)
    print("Updated Slide 5 script in app.js!")
else:
    print("WARNING: old_script5 not found.")

# 2. Slide 6 script (index 6)
old_script6 = """  `<strong>JOB 01: UNDERSTAND:</strong><br>“Job 1 is Understand. When a textbook paragraph feels like reading ancient Greek, AI can break down the logic sentence by sentence without jargon.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>JOB 02: SIMPLIFY:</strong><br>“Job 2 is Simplify. If an explanation doesn't click, you don't give up. You tell AI: 'Explain it like I am 12 years old' or 'Explain using cricket bowling variations'. What would you ask if the first explanation failed?”`,"""

new_script6 = """  `<strong>PART 2: CHATGPT AS PERSONAL TUTOR:</strong><br>“Now we enter Part 2. This is how you use ChatGPT to study.<br>Look at the difference on screen: If you type 'Explain electricity', you get college-level paragraphs that confuse you more.<br>Look at the better prompt: 'I am a Class 10 Karnataka State Board student. Explain electric current in simple language using an everyday example.'”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>THE 4 CONTEXT ANCHORS:</strong><br>“Always give ChatGPT 4 anchors:<br>1. WHO am I? Class 10 student.<br>2. WHAT do I want? Explain the concept.<br>3. LEVEL: Simple language.<br>4. FORMAT: Everyday analogy like water flowing in pipes.”`,"""

if old_script6 in js:
    js = js.replace(old_script6, new_script6)
    print("Updated Slide 6 script in app.js!")
else:
    print("WARNING: old_script6 not found.")

# 3. Slide 7 script (index 7)
old_script7 = """  `<strong>JOB 03: EXPLORE:</strong><br>“Job 3 is Explore. Don't just ask 'What is Newton's law?' Ask: 'Why do cricket fielders pull their hands back when catching a ball?' Suddenly, impulse has a reason to exist in your memory!”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>JOB 04: PRACTISE:</strong><br>“Job 4 is Practise. The biggest mistake students make is asking AI for answers. When AI gives you an answer, your brain relaxes. When AI gives you a question, your brain sweats. Which one helps you in the exam hall? The sweat!”`,"""

new_script7 = """  `<strong>SKILL 2: ASK FOLLOW-UP QUESTIONS:</strong><br>“Here is the biggest secret students miss: DON'T START A NEW CHAT FOR EVERY QUESTION!<br>Have a real learning conversation: Start with 'Explain Newton's First Law'. When it answers, reply: 'I still don't understand inertia. Explain that part again.' Then: 'Give me a real-life example.' Then: 'Explain using cricket.' Then: 'Ask me one question to check whether I understood.' That chain is how real learning happens!”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>THE RETRIEVAL LOOP:</strong><br>“Never ask AI for answers. When AI gives you an answer, your brain relaxes into an illusion of competence. When AI asks YOU a question, your brain sweats. In the exam hall, only the sweat counts!”`,"""

if old_script7 in js:
    js = js.replace(old_script7, new_script7)
    print("Updated Slide 7 script in app.js!")
else:
    print("WARNING: old_script7 not found.")

# 4. Slide 12 script (index 12)
old_script12 = """  `<strong>HEAD-TO-HEAD:</strong><br>“Look at both outputs on screen. One gave a batsman playing a forward defensive shot; the other talked about a ball rolling across a grass outfield.<br>Which explanation made more sense to YOUR brain? AI models think differently. Don't be afraid to try both.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>MINDSET REFRAME:</strong><br>“Stop asking which AI is number one. A screwdriver isn't better than a hammer. It depends on whether you have a screw or a nail!”`,"""

new_script12 = """  `<strong>PART 4: GEMINI HEAD-TO-HEAD:</strong><br>“Don't treat Gemini as just 'another ChatGPT'. Let's give ChatGPT and Gemini the exact same study problem live: 'I'm a Class 10 student preparing for my Science exam. Explain electric current in simple language using an everyday example.'<br>Compare the outputs: ChatGPT uses a water pipe analogy; Gemini highlights circuit components and SI units.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>EVALUATE, DON'T BLINDLY TRUST:</strong><br>“The takeaway isn't 'which AI is number one'. The takeaway is: Different AI tools produce different responses. You must learn to evaluate the response rather than blindly trusting whichever tool you opened first!”`,"""

if old_script12 in js:
    js = js.replace(old_script12, new_script12)
    print("Updated Slide 12 script in app.js!")
else:
    print("WARNING: old_script12 not found.")

# 5. Slide 31 script (index 31)
old_script31 = """<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>HUMAN OR AI?:</strong><br>“Read this sentence: Human or AI? Vote!<br>The reveal: It's from Page 95 of your official Karnataka State Board textbook!<br>Lesson: You cannot judge accuracy just because something sounds intelligent. Always verify.”`,"""

new_script31 = """<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>PART 7: 5 RESPONSIBLE AI RULES:</strong><br>“Five simple, non-negotiable rules for your exam prep:<br>1. AI can be wrong.<br>2. Don't blindly copy.<br>3. Always verify against your Karnataka Board textbook.<br>4. Try answering yourself before asking AI.<br>5. Never paste passwords, OTPs, or private personal data into AI prompts!”`,"""

if old_script31 in js:
    js = js.replace(old_script31, new_script31)
    print("Updated Slide 31 script in app.js!")
else:
    print("WARNING: old_script31 not found.")

# 6. Slide 34 script (index 34)
old_script34 = """  `<strong>LAB INTEGRITY:</strong><br>“In the lab, facilitators are walking around. If we catch you simply copying text, your score resets. Be the thinker.”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>LAUNCH CALL:</strong><br>“No more slides. No more lectures.<br>Enough watching. Now you try. Head to your computers!”`,"""

new_script34 = """  `<strong>THE CORE SHIFT:</strong><br>“The auditorium was: I TEACH. The computer lab is: YOU DO!<br>We just taught you the 6 skills across ChatGPT, Gemini, and NotebookLM. Now you have 60 minutes in the lab to prove you can do them on your own Karnataka Board syllabus!”<hr class="script-divider" style="margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);"><strong>LAUNCH CALL:</strong><br>“No more slides. No more watching.<br>Head to your computers, open Mission 1, and conquer your toughest chapter!”`,"""

if old_script34 in js:
    js = js.replace(old_script34, new_script34)
    print("Updated Slide 34 script in app.js!")
else:
    print("WARNING: old_script34 not found.")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Saved updated app.js successfully!")

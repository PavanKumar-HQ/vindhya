#!/usr/bin/env python3
"""
Merge 71 micro-slides into 36 rich, full-page panoramic presentation slides (2-column split),
utilizing the full viewport space, styled with the Brandex logo color system (#111D36, #4071E5 -> #7C5CE9 gradient).
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Let's extract existing presenter scripts from app.js
scripts_match = re.search(r'const presenterScripts = \[(.*?)\];\s*// Document Ready', js, re.DOTALL)
old_scripts = []
if scripts_match:
    raw_scripts = scripts_match.group(1)
    # Extract strings enclosed in backticks
    old_scripts = re.findall(r'`(.*?)`', raw_scripts, re.DOTALL)
    print(f'Extracted {len(old_scripts)} existing presenter scripts')

# Pairing plan: 71 slides into 36 merged slides
# Slide 1: 0, 1 (Opening + Be Honest)
# Slide 2: 2, 3 (Real Question + Exam in 7 Days)
# Slide 3: 4, 5 (What's Your Move + What if D was Different)
# Slide 4: 6, 7 (AI Study Partner + Our Rule)
# Slide 5: 8, 9 (You Already Know This + AI vs You)
# Slide 6: 10, 11 (What Can AI Do + 6 Useful Jobs)
# Slide 7: 12, 13 (Job 01 Understand + Job 02 Simplify)
# Slide 8: 14, 15 (Job 03 Explore + Job 04 Practise)
# Slide 9: 16, 17 (Job 05 Check + Job 06 Revise)
# Slide 10: 18, 19 (Geniusphere Loop + The Trap)
# Slide 11: 20, 21 (Three Tools + ChatGPT)
# Slide 12: 22, 23 (ChatGPT Interaction + Gemini)
# Slide 13: 24, 25 (Same Question Different AI + Don't Ask This)
# Slide 14: 26, 27 (NotebookLM + Crucial Difference)
# Slide 15: 28, 29 (Quick Game Which Tool + Transition Live Demos)
# Slide 16: 30, 31 (The Problem + Bad AI Question)
# Slide 17: 32, 33 (Better Question + What Changed)
# Slide 18: 34, 35 (Cricket Test + AI as Tutor)
# Slide 19: 36, 37 (Catch My Answer + Three Ways to Use AI)
# Slide 20: 38, 39 (Mini Challenge Photosynthesis + Understanding != Exam Ready)
# Slide 21: 40, 41 (Build a Test + Student Answers Live)
# Slide 22: 42, 43 (Check My Answer + Wrong Answers are Useful)
# Slide 23: 44, 45 (Revision Flywheel + Spotting Blind Spots)
# Slide 24: 46, 47 (Emergency Protocol 2 Hours + What if AI had Textbook)
# Slide 25: 48, 49 (NotebookLM Setup + Syllabus Locked Questioning)
# Slide 26: 50, 51 (Citation Superpower + Audio Overview)
# Slide 27: 52, 53 (When to use Which + Art of Student Prompting)
# Slide 28: 54, 55 (Prompt Staircase 5 Levels + 5-Part Formula)
# Slide 29: 56, 57 (Teacher Analogy + Prompt Battle)
# Slide 30: 58, 59 (5 Master Prompts + Check My Work Rule)
# Slide 31: 60, 61 (Can You Trust AI + Confident != Correct)
# Slide 32: 62, 63 (Catch the AI Stomata + Game Human or AI)
# Slide 33: 64, 65 (Stop Check Think + Responsible AI 5 Rules)
# Slide 34: 66, 67 (Your Mission Pick Chapter + 5 Lab Steps)
# Slide 35: 68, 69 (Lab Rules + Enough Watching Launch)
# Slide 36: 70 (Closing Quote Outro)

pairings = [
    (0, 1, "00–10 MIN • MODULE 1", "THE REALITY CHECK & ICEBREAKER"),
    (2, 3, "00–10 MIN • MODULE 1", "THE REAL QUESTION & 7-DAY PANIC"),
    (4, 5, "00–10 MIN • MODULE 1", "WHAT'S YOUR MOVE & THE SHIFT"),
    (6, 7, "00–10 MIN • MODULE 1", "THE STUDY PARTNER & THE #1 RULE"),
    (8, 9, "00–10 MIN • MODULE 1", "PROMPTING AS CONTEXT & AI VS YOU"),
    (10, 11, "10–20 MIN • MODULE 2", "WHAT AI CAN DO & 6 USEFUL JOBS"),
    (12, 13, "10–20 MIN • MODULE 2", "JOB 1: UNDERSTAND & JOB 2: SIMPLIFY"),
    (14, 15, "10–20 MIN • MODULE 2", "JOB 3: EXPLORE & JOB 4: PRACTISE"),
    (16, 17, "10–20 MIN • MODULE 2", "JOB 5: CHECK & JOB 6: REVISE GAPS"),
    (18, 19, "10–20 MIN • MODULE 2", "THE 5-STEP LOOP & THE COPY-PASTE TRAP"),
    (20, 21, "20–35 MIN • MODULE 3", "THREE TOOLS ARSENAL & CHATGPT"),
    (22, 23, "20–35 MIN • MODULE 3", "CHATGPT INTERACTION & GEMINI VISUALS"),
    (24, 25, "20–35 MIN • MODULE 3", "HEAD-TO-HEAD COMPARISON & TOOL MINDSET"),
    (26, 27, "20–35 MIN • MODULE 3", "NOTEBOOKLM & THE CRUCIAL DIVIDE"),
    (28, 29, "20–35 MIN • MODULE 3", "WHICH TOOL TO USE & LIVE DEMO LAUNCH"),
    (30, 31, "35–55 MIN • MODULE 4", "NEWTON'S LAWS & THE 5-WORD BAD PROMPT"),
    (32, 33, "35–55 MIN • MODULE 4", "THE UPGRADED PROMPT & WHAT CHANGED"),
    (34, 35, "35–55 MIN • MODULE 4", "CRICKET TEST & AI AS SOCRATIC TUTOR"),
    (36, 37, "35–55 MIN • MODULE 4", "CATCH MY ANSWER & 3 LEVELS OF AI USE"),
    (38, 39, "55–75 MIN • MODULE 5", "PHOTOSYNTHESIS CHALLENGE & EXAM GAP"),
    (40, 41, "55–75 MIN • MODULE 5", "BUILD A TEST & LIVE STUDENT ATHLETE ANSWER"),
    (42, 43, "55–75 MIN • MODULE 5", "STRICT EXAMINER SCORING & ERROR FUNNEL"),
    (44, 45, "55–75 MIN • MODULE 5", "THE REVISION FLYWHEEL & BLIND SPOTS"),
    (46, 47, "55–75 MIN • MODULE 5", "2-HOUR EMERGENCY PROTOCOL & TEXTBOOK LOCK"),
    (48, 49, "75–90 MIN • MODULE 6", "NOTEBOOKLM PDF SETUP & SYLLABUS QUERIES"),
    (50, 51, "75–90 MIN • MODULE 6", "VERIFIABLE CITATIONS & AUDIO OVERVIEW"),
    (52, 53, "75–90 MIN • MODULE 6", "TOOL MATRIX & THE ART OF PROMPTING"),
    (54, 55, "90–100 MIN • MODULE 7", "PROMPT STAIRCASE & 5-PART MASTER FORMULA"),
    (56, 57, "90–100 MIN • MODULE 7", "TEACHER CONTEXT & AUDIENCE PROMPT BATTLE"),
    (58, 59, "90–100 MIN • MODULE 7", "5 MASTER PROMPTS & CHECK-MY-WORK RULE"),
    (60, 61, "100–110 MIN • MODULE 8", "CAN YOU TRUST AI & CONFIDENT != CORRECT"),
    (61, 63, "100–110 MIN • MODULE 8", "CATCH THE STOMATA ERROR & HUMAN OR AI"),
    (64, 65, "100–110 MIN • MODULE 8", "STOP CHECK THINK & RESPONSIBLE AI RULES"),
    (66, 67, "110–120 MIN • MODULE 9", "LAB MISSION: PICK HARDEST CHAPTER & 5 STEPS"),
    (68, 69, "110–120 MIN • MODULE 9", "LAB INTEGRITY RULES & LAUNCH WORKSPACE"),
    (70, -1, "120 MIN • OUTRO", "THE ULTIMATE TAKEAWAY & LAUNCH")
]

print(f"Total merged slides: {len(pairings)}")

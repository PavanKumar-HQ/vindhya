import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx_start = js.find('const presenterScripts = [')
if idx_start == -1:
    print('Error: presenterScripts not found')
    exit(1)

new_s1 = """<strong>WALK IN WITH A QUESTION (NOT A DEFINITION):</strong><br>“Before we start, I want to ask you something.<br>How many of you have ever been studying at night, opened a chapter, read the same paragraph two or three times… and still thought: ‘I understood absolutely nothing.’<br>Pause. Let them react.<br>And then what happens? You search YouTube. You ask your friend. You message someone: ‘Bro, what is this?!’<br>Small laugh.<br>And now there's one more person you can ask... AI.”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Walk in with calm energy. Do not introduce definitions. Pause after 'absolutely nothing'."""

new_s2 = """<strong>THE 10:30 PM ICEBREAKER:</strong><br>“Look at the screen right now:<br>IT'S 10:30 PM. EXAM TOMORROW. ONE CHAPTER LEFT. YOU DON'T UNDERSTAND IT.<br>Be honest: What are you doing?<br>A — YouTube<br>B — Ask a friend<br>C — Pretend tomorrow doesn't exist<br>D — Ask AI<br>Call out your letter or raise hands!<br>If C gets votes: ‘I appreciate the honesty!’<br>If D gets most: ‘Okay, so AI is already part of your study life.’<br>Then transition: ‘But here's the question I actually want to answer today...’”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> React live to their shouted letters with humour and warmth."""

new_s3 = """<strong>THE BIG QUESTION (THE HOOK):</strong><br>“Are you using AI to study… or are you using AI to avoid studying?<br>Let that sit on screen for a moment.<br>Because there is a huge difference.<br>If you ask AI: ‘Give me the five-mark answer’, copy it, memorize it, and write it in the exam… AI did the thinking.<br>Pause.<br>But if you ask: ‘I don't understand this. Teach it to me. Give me an example. Then test me.’—YOU are still doing the learning!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Let silence sit after the hook question. This frames the entire 2 hours."""

new_s4 = """<strong>INTRODUCE THE WORKSHOP:</strong><br>“That's what we're going to do today: AI EXAM LAB. Learn with AI. Don't let AI learn for you.<br>I'm not going to spend the next two hours explaining what artificial intelligence is. You already know AI exists. You've probably already used it.<br>What I want to teach you is something much more practical:<br>How can you actually use ChatGPT, Gemini and NotebookLM to prepare for your exams?<br>We're going to use them for three things: Understand. Practise. Improve.”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Clear, confident delivery of the workshop promise."""

new_s5 = """<strong>THE ORIGINAL PHILOSOPHY & WHAT DO YOU ASK?:</strong><br>“Remember this one line throughout today's session:<br>‘The smartest use of AI isn't getting the answer faster. It's learning how to understand it better.’<br>Now look at the question on screen: When you don't understand something, what do you ask?<br>‘What is this?’ vs ‘Explain this in simple language’ vs ‘Give me an example’ vs ‘Ask me a question to see if I understood.’<br>Which one of these is actually helping you learn?<br>Exactly. And that is where we are going to start!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Point to the 4 levels, get audience agreement, then transition to Module 1!"""

new_s6 = """<strong>MODULE 1: CHATGPT AS YOUR AI TUTOR:</strong><br>“Module 1: ChatGPT as your AI Tutor.<br>Purpose: Help a student when they are stuck on a chapter/topic.<br>We touch: how to ask to explain, simpler language, examples, analogies, follow-up questions, and asking AI to check whether you understood!<br>Let's look at a student struggling with Newton's First Law!”<hr class="script-divider" style="margin: 0.5rem 0; border: none; border-top: 1px dashed #ccc;"><strong>ACTION:</strong> Begin the Newton's bus demonstration!"""

idx_end = js.find('];', idx_start)
snippet = js[idx_start:idx_end+2]

items = re.findall(r'`([^`]+)`', snippet)
print('Current items count:', len(items))

items[0] = new_s1
items[1] = new_s2
items[2] = new_s3
items[3] = new_s4
items[4] = new_s5
items[5] = new_s6

formatted = 'const presenterScripts = [\n' + ',\n\n'.join(f'  `{it}`' for it in items) + '\n];'
updated_js = js[:idx_start] + formatted + js[idx_end+2:]

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(updated_js)

print('Updated app.js successfully with opening narrative presenter scripts!')

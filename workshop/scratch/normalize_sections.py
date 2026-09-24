#!/usr/bin/env python3
"""
Normalize section tags and badges across all 36 slides in index.html to match the 7 Parts.
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def get_section(idx):
    if 0 <= idx <= 4:
        return "0–15 MIN • PART 1: AI FOR EXAMS"
    elif 5 <= idx <= 10:
        return "15–40 MIN • PART 2: CHATGPT AS TUTOR"
    elif 11 <= idx <= 18:
        return "40–65 MIN • PART 3: CHATGPT EXAM PARTNER"
    elif 19 <= idx <= 22:
        return "65–80 MIN • PART 4: GEMINI STUDY WORKFLOW"
    elif 23 <= idx <= 27:
        return "80–105 MIN • PART 5: NOTEBOOKLM STUDY MATERIAL"
    elif 28 <= idx <= 30:
        return "105–115 MIN • PART 6: PROMPTING IN 10 MIN"
    else:
        return "115–120 MIN • PART 7: RESPONSIBLE AI & LAB"

# Regex to find each slide header and replace data-section and badge
def repl_slide(match):
    full = match.group(0)
    idx = int(match.group(1))
    new_sec = get_section(idx)
    # replace data-section="..."
    res = re.sub(r'data-section="[^"]+"', f'data-section="{new_sec}"', full, count=1)
    # replace badge-gradient
    res = re.sub(r'<span class="m-badge badge-gradient">[^<]+</span>', f'<span class="m-badge badge-gradient">{new_sec}</span>', res, count=1)
    return res

slide_header_regex = re.compile(r'<div class="carousel-slide[^"]*" data-index="(\d+)"[^>]*>.*?<div class="m-badge-group">.*?</div>', re.DOTALL)
new_html = slide_header_regex.sub(repl_slide, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Successfully normalized all 36 slide section headers to the 7-Part Teaching Architecture!")

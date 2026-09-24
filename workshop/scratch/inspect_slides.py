#!/usr/bin/env python3
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# -------------------------------------------------------------
# 1. Update Slide 5 (data-index="4") with the 6-Skill Syllabus Table & 6 Jobs
# -------------------------------------------------------------
slide5_pattern = r'(<div class="carousel-slide[^"]*" data-index="4"[^>]*>)(.*?)(</div>\s*</div>\s*</div>\s*</div>\s*<!-- MERGED SLIDE 06)'
slide5_match = re.search(slide5_pattern, html, re.DOTALL)
if slide5_match:
    print("Found Slide 5 (Index 4)")

# Let's inspect data-index="4" and data-index="5" in index.html to be certain of their headers and markup

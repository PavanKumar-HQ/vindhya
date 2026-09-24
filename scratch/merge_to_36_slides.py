#!/usr/bin/env python3
"""
Merge 71 micro-slides into 36 full-page panoramic presentation slides (2-column split),
utilizing the full viewport space, styled with the Brandex logo color system (#111D36, #4071E5 -> #7C5CE9 gradient).
"""
import re

# 1. Read index.html and app.js
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 2. Extract existing 71 slides
slide_pattern = r'<div class="carousel-slide[^"]*" data-index="(\d+)" [^>]*data-section="([^"]+)" data-title="([^"]+)">\s*(.*?)\s*</div>\s*(?=<!-- SLIDE|\s*</div>\s*<!-- Click Arrow|\s*<button type="button" class="carousel-nav-btn next-arrow")'
slides = re.findall(slide_pattern, html, re.DOTALL)
print(f'Parsed {len(slides)} existing slides from index.html')

# 3. Extract existing 71 presenter scripts from app.js
scripts_match = re.search(r'const presenterScripts = \[(.*?)\];\s*// Document Ready', js, re.DOTALL)
old_scripts = []
if scripts_match:
    raw_scripts = scripts_match.group(1)
    old_scripts = re.findall(r'`(.*?)`', raw_scripts, re.DOTALL)
    print(f'Extracted {len(old_scripts)} existing presenter scripts from app.js')

# 4. Generate 36 merged slides
merged_slides_html = []
merged_scripts = []

for k in range(35):
    idx1 = 2 * k
    idx2 = 2 * k + 1

    slide1 = slides[idx1]
    slide2 = slides[idx2]

    sec1 = slide1[1]
    title1 = slide1[2]
    body1 = slide1[3]

    sec2 = slide2[1]
    title2 = slide2[2]
    body2 = slide2[3]

    # Combine scripts
    script1 = old_scripts[idx1] if idx1 < len(old_scripts) else ""
    script2 = old_scripts[idx2] if idx2 < len(old_scripts) else ""
    combined_script = f"{script1}<hr class=\"script-divider\" style=\"margin: 1rem 0; border: none; border-top: 2px dashed rgba(88,107,230,0.5);\">{script2}"
    merged_scripts.append(combined_script)

    active_cls = " active" if k == 0 else ""
    merged_html = f"""        <!-- MERGED SLIDE {k+1:02d}: {title1} &bull; {title2} -->
        <div class="carousel-slide{active_cls}" data-index="{k}" data-section="{sec1}" data-title="{title1} &bull; {title2}">
          <div class="merged-slide-container">
            <div class="merged-slide-header">
              <div class="m-badge-group">
                <span class="m-badge badge-gradient">{sec1}</span>
                <span class="m-badge badge-navy">PART {k+1:02d} OF 36</span>
              </div>
              <h2 class="m-slide-title">{title1} <span class="title-sep">&bull;</span> {title2}</h2>
            </div>
            
            <div class="merged-slide-grid">
              <div class="m-panel panel-left">
                {body1}
              </div>
              <div class="m-panel panel-right">
                {body2}
              </div>
            </div>
          </div>
        </div>"""
    merged_slides_html.append(merged_html)

# 36th Slide: Slide 70 (Grand Finale Outro)
last_slide = slides[70]
sec_last = last_slide[1]
title_last = last_slide[2]
body_last = last_slide[3]
last_script = old_scripts[70] if 70 < len(old_scripts) else ""
merged_scripts.append(last_script)

merged_last_html = f"""        <!-- MERGED SLIDE 36: {title_last} -->
        <div class="carousel-slide" data-index="35" data-section="{sec_last}" data-title="{title_last}">
          <div class="merged-slide-container">
            <div class="merged-slide-header">
              <div class="m-badge-group">
                <span class="m-badge badge-gradient">{sec_last}</span>
                <span class="m-badge badge-navy">PART 36 OF 36 &bull; FINALE</span>
              </div>
              <h2 class="m-slide-title">{title_last}</h2>
            </div>
            <div class="merged-slide-single">
              {body_last}
            </div>
          </div>
        </div>"""
merged_slides_html.append(merged_last_html)

print(f"Generated {len(merged_slides_html)} merged slides and {len(merged_scripts)} merged scripts")

# 5. Replace slide section in index.html
all_merged_slides_str = "\n\n".join(merged_slides_html)

# Find the slides container
# From right after <div class="slides-viewport"> to before </div>\s*<!-- Click Arrow: Right
viewport_replace_pattern = r'(<div class="slides-viewport">\s*).*?(\s*</div>\s*<!-- Click Arrow: Right)'
if re.search(viewport_replace_pattern, html, re.DOTALL):
    html = re.sub(viewport_replace_pattern, rf'\1{all_merged_slides_str}\2', html, flags=re.DOTALL)
    print("Replaced all slides in index.html with 36 merged slides!")
else:
    print("ERROR: Could not find slides-viewport pattern in index.html")

# Update slide counter displays and tabs to 36
html = html.replace('<span class="total-slides-num" id="totalSlidesDisplay">71</span>', '<span class="total-slides-num" id="totalSlidesDisplay">36</span>')
html = re.sub(r'Auditorium Presentation \([^)]*\)', 'Auditorium Presentation (36 Merged Panoramic Slides)', html)

# Add Brandex Logo in Header
brand_header_old = """      <div class="header-brand">
        <div class="brand-badge">GS</div>
        <div class="brand-titles">
          <span class="brand-title">GENIUSPHERE</span>
          <span class="brand-subtitle">AI EXAM LAB</span>
        </div>
      </div>"""

brand_header_new = """      <div class="header-brand">
        <div class="brandex-header-pill">
          <img src="assets/brandex_logo.png" alt="Brandex" class="brandex-header-img">
        </div>
        <div class="brand-titles">
          <span class="brand-title">AI EXAM LAB</span>
          <span class="brand-subtitle">Karnataka State Board &bull; Classes 9 & 10</span>
        </div>
      </div>"""

if brand_header_old in html:
    html = html.replace(brand_header_old, brand_header_new)
    print("Updated header with Brandex Logo!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 6. Update app.js with 36 merged scripts and appState.totalSlides = 36
js = js.replace('totalSlides: 71,', 'totalSlides: 36,')

scripts_code_lines = []
for s in merged_scripts:
    scripts_code_lines.append(f"  `{s}`")

scripts_block = "const presenterScripts = [\n" + ",\n\n".join(scripts_code_lines) + "\n];\n\n// Document Ready"

js = re.sub(r'const presenterScripts = \[.*?\];\s*// Document Ready', scripts_block, js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js with 36 merged scripts and totalSlides = 36!")

import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

with open('scratch/generated_three_tools_slides.html', 'r', encoding='utf-8') as f:
    new_slides_html = f.read()

start_marker = '<div class="slides-viewport">'
end_marker = '<!-- Click Arrow: Right (Next Slide) -->'

start_pos = text.find(start_marker)
end_pos = text.find(end_marker)

if start_pos == -1 or end_pos == -1:
    print('Error: markers not found in index.html!')
    exit(1)

start_inner = start_pos + len(start_marker)
end_inner = text.rfind('</div>', 0, end_pos)

updated_html = text[:start_inner] + '\n' + new_slides_html + '\n      ' + text[end_inner:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(updated_html)

print('Successfully updated index.html! New length:', len(updated_html))

# Verify slides in index.html
slides = re.findall(r'<div class="carousel-slide[^"]*"[^>]*data-index="(\d+)"', updated_html)
print('Total slides verified in index.html:', len(slides), 'First 3:', slides[:3], 'Last 3:', slides[-3:])

# 2. Update app.js presenterScripts
# import presenter_scripts from build_complete_three_tools_system.py
import importlib.util
spec = importlib.util.spec_from_file_location("builder", "scratch/build_complete_three_tools_system.py")
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)

scripts = builder.presenter_scripts
print('Total presenter scripts loaded from builder:', len(scripts))

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx_start = js.find('const presenterScripts = [')
idx_end = js.find('];', idx_start)

if idx_start == -1 or idx_end == -1:
    print('Error: presenterScripts not found in app.js')
    exit(1)

formatted_scripts = 'const presenterScripts = [\n' + ',\n\n'.join(f'  `{s}`' for s in scripts) + '\n];'
updated_js = js[:idx_start] + formatted_scripts + js[idx_end+2:]

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(updated_js)

print('Successfully updated app.js with 36 presenter scripts!')

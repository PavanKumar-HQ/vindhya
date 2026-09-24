import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's verify start and end of carousel slides
slides_start_marker = '<div class="slides-viewport">'
slides_end_marker = '<!-- MODE 2: 🧪 STUDENT COMPUTER LAB'

start_pos = html.find(slides_start_marker)
end_pos = html.find(slides_end_marker)

if start_pos == -1 or end_pos == -1:
    print('Failed to locate markers!')
    exit(1)

print(f'Located slides section from {start_pos} to {end_pos}')

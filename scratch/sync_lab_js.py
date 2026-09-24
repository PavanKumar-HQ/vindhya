with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Update totalLabSteps to 6
js = js.replace('totalLabSteps: 8,', 'totalLabSteps: 6,')

# 2. Update goToLabMission indicator label
old_code = """  const stepLabel = document.getElementById('labStepIndicator');
  if (stepLabel) {
    if (stepIdx === 0) stepLabel.textContent = 'Mission Setup';
    else if (stepIdx === 8) stepLabel.textContent = 'Mission Complete';
    else stepLabel.textContent = `Mission 0${stepIdx} / 07`;
  }"""

new_code = """  const stepLabel = document.getElementById('labStepIndicator');
  if (stepLabel) {
    if (stepIdx === 0) stepLabel.textContent = 'Mission Setup';
    else if (stepIdx === 6) stepLabel.textContent = 'Final Submission';
    else stepLabel.textContent = `Mission 0${stepIdx} / 05`;
  }"""

if old_code in js:
    js = js.replace(old_code, new_code)
    print("Updated stepLabel logic in goToLabMission!")
else:
    print("Warning: old_code for stepLabel not matched directly")

# 3. Add setSubPill and submitFinalLab if not present
if 'function setSubPill' not in js:
    additions = """
function setSubPill(btn, containerId, val) {
  const container = document.getElementById(containerId);
  if (!container) return;
  container.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
  btn.classList.add('active');
  saveLabData();
}

function submitFinalLab() {
  const student = document.getElementById('studentNameInput')?.value.trim() || 'Student';
  const topic = document.getElementById('topicInput')?.value.trim() || "Newton's First Law of Motion";
  const problem = document.getElementById('final_problem')?.value.trim() || topic;
  const tool = document.getElementById('final_tool')?.value.trim() || 'ChatGPT / Gemini / NotebookLM';
  
  alert(`🎉 CONGRATULATIONS, ${student.toUpperCase()}!\\n\\nYou have completed the Geniusphere AI Exam Lab Practical (60 Minutes)!\\n\\nProblem Solved: ${problem}\\nAI Tool Mastered: ${tool}\\n\\nTHE RULE OF THE LAB:\\n✅ ASK → THINK → TRY → CHECK → IMPROVE\\nYou didn't win by getting the answer. You won by understanding it!`);
  saveLabData();
}
"""
    js += additions
    print("Added setSubPill and submitFinalLab to app.js!")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js successfully!")

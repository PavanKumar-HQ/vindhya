# 🚀 BRANDEX AI EXAM LAB — WORKSHOP SYSTEM (V1 LOCKED)

Welcome to the **Brandex & Geniusphere AI Exam Lab** operating system. This package contains the end-to-end assets for running the 2-Hour Auditorium Session followed by the 60-Minute Interactive Digital Student Computer Lab for Classes 9 & 10.

---

## 📂 DIRECTORY STRUCTURE & ASSETS

| File | Purpose |
|---|---|
| [`index.html`](file:///Users/pavankumars/Downloads/workshop/index.html) | **The Digital Student Lab Web Application**. Zero-paper, interactive student interface for the 60-minute computer lab session. |
| [`styles.css`](file:///Users/pavankumars/Downloads/workshop/styles.css) | Custom styling: Brandex dark navy palette, glassmorphism cards, micro-animations, responsive layout & print stylesheets. |
| [`app.js`](file:///Users/pavankumars/Downloads/workshop/app.js) | Interactive application engine: Dynamic prompt templating, 60-min countdown timer, 1-click clipboard copy, autosave (`localStorage`), prompt formula inspector, and completion report generator. |
| [`assets/brandex-logo.png`](file:///Users/pavankumars/Downloads/workshop/assets/brandex-logo.png) | High-resolution official Brandex brand asset embedded across the application. |
| [`AUDITORIUM_PLAYBOOK.md`](file:///Users/pavankumars/Downloads/workshop/AUDITORIUM_PLAYBOOK.md) | **120-Minute Auditorium Presenter Playbook & Slide Deck Content**: Word-for-word stage script, slides 1–22, audience questions, pauses, and attention-loop interactions. |
| [`DEMO_PLAYBOOK.md`](file:///Users/pavankumars/Downloads/workshop/DEMO_PLAYBOOK.md) | **Live Demo Cheatsheet**: Copy-paste prompts for ChatGPT, Gemini, and NotebookLM, including bad prompts vs. upgraded prompts and weak-answer evaluation prompts. |
| [`FACILITATOR_GUIDE.md`](file:///Users/pavankumars/Downloads/workshop/FACILITATOR_GUIDE.md) | **Lab Operations Manual**: Facilitator-to-student ratios, minute-by-minute intervention guide, 3-step unblocking rule, emergency backup protocols, and school report template. |

---

## 🏃 HOW TO RUN LOCALLY

To launch the Digital Student Lab web application locally in any browser:

```bash
# In the workshop directory:
python3 -m http.server 8089
```

Then open your browser to:
👉 **`http://localhost:8089`**

---

## 🌟 KEY CAPABILITIES OF THE DIGITAL LAB

1. **Dynamic Prompt Variable Injection**: When a student inputs their Class (9 or 10) and Topic (e.g. *Newton's First Law* or *Electricity*), every prompt across all 7 missions automatically updates in real time.
2. **1-Click Prompt Copy**: Instant copy with feedback to clipboard for seamless pasting into ChatGPT, Gemini, or NotebookLM.
3. **Prompt Inspector (Mission 6)**: Live analyzer that detects if the student included **WHO**, **WHAT**, **CONTEXT**, **HOW**, and **RULE** in their improved prompt and lights up green checkmarks.
4. **Offline / Slow-Network "Backup AI" Mode**: Header toggle reveals pre-loaded realistic AI responses so students never get blocked if school Wi-Fi is unstable.
5. **Printable / Downloadable Mission Certificate**: Summarizes baseline confidence vs post-lab confidence, key takeaways, and upgraded prompt.

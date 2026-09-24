import re

css = """/* ==========================================================================
   GENIUSPHERE AI EXAM LAB — RAW NEO-BRUTALIST PRESENTATION & LAB SYSTEM
   Authentic Editorial Brutalism:
   - 100% Solid Ink Borders (2px - 3.5px solid #000000)
   - 100% Hard Physical Offset Drop Shadows (ZERO blur: 4px 4px 0px #000000)
   - Tactile Mechanical Button States (Press depth, crisp displacement)
   - Zero AI Slop (No radial dots, no blurry neon glows, no gradient soup)
   - Pure Brandex Ink Palette: Navy #111D36, Electric Blue #2563EB, Canary Yellow #FFE600
   ========================================================================== */

:root {
  /* Surface Tokens (Default: High-Impact Neo-Brutalist Light Paper) */
  --nb-bg: #f4f5f8;
  --nb-stage: #ffffff;
  --nb-card: #ffffff;
  --nb-card-alt: #f8fafc;
  --nb-card-panel: #ffffff;
  --nb-header: #ffffff;
  
  /* Text & Inks */
  --nb-ink: #000000;
  --nb-ink-secondary: #1e293b;
  --nb-ink-muted: #64748b;
  --nb-ink-white: #ffffff;
  
  /* Solid Graphic Colors (Zero Gradient Soup) */
  --nb-navy: #111d36;
  --nb-blue: #2563eb;
  --nb-blue-light: #eff6ff;
  --nb-yellow: #ffe600;
  --nb-mint: #10b981;
  --nb-mint-light: #f0fdf4;
  --nb-coral: #ef4444;
  --nb-coral-light: #fef2f2;
  --nb-cyan: #0284c7;
  --nb-purple: #7c5ce9;

  /* Physical Borders & Hard Drop Shadows */
  --nb-border: 2px solid #000000;
  --nb-border-thick: 3px solid #000000;
  --nb-border-sm: 1.5px solid #000000;
  
  --nb-shadow: 4px 4px 0px #000000;
  --nb-shadow-sm: 2px 2px 0px #000000;
  --nb-shadow-btn: 3px 3px 0px #000000;
  --nb-shadow-lg: 6px 6px 0px #000000;
  --nb-shadow-xl: 8px 8px 0px #000000;
  --nb-shadow-hover: 4px 4px 0px #000000;
  --nb-shadow-pressed: 1px 1px 0px #000000;
  
  --nb-radius: 4px;
  --nb-radius-card: 6px;

  /* Typography */
  --font-display: 'Space Grotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  /* Backward Compatibility Aliases */
  --bx-canvas: var(--nb-bg);
  --bx-stage: var(--nb-stage);
  --bx-navy: var(--nb-card);
  --bx-navy-elevated: var(--nb-card-alt);
  --bx-navy-card: var(--nb-card);
  --bx-navy-border: #000000;
  --bx-blue: var(--nb-blue);
  --bx-cobalt: var(--nb-navy);
  --bx-indigo: var(--nb-purple);
  --bx-violet: var(--nb-purple);
  --bx-cyan: #0284c7;
  --bx-emerald: var(--nb-mint);
  --bx-amber: #b45309;
  --bx-rose: var(--nb-coral);
  --text-white: #ffffff;
  --text-primary: var(--nb-ink);
  --text-secondary: var(--nb-ink-secondary);
  --text-muted: var(--nb-ink-muted);
}

/* Dark Neo-Brutalist Theme (Crisp Charcoal, Sharp Inks, No Fuzzy Purple Glows) */
[data-theme="dark"], body.dark-mode {
  --nb-bg: #0d1117;
  --nb-stage: #161b22;
  --nb-card: #161b22;
  --nb-card-alt: #21262d;
  --nb-card-panel: #161b22;
  --nb-header: #161b22;
  
  --nb-ink: #ffffff;
  --nb-ink-secondary: #cbd5e1;
  --nb-ink-muted: #8b949e;
  
  --nb-navy: #1f293d;
  --nb-blue: #3b82f6;
  --nb-blue-light: #172554;
  --nb-yellow: #fde047;
  --nb-mint: #34d399;
  --nb-mint-light: #064e3b;
  --nb-coral: #f87171;
  --nb-coral-light: #450a0a;

  --nb-border: 2px solid #000000;
  --nb-border-thick: 3px solid #000000;
  --nb-shadow: 4px 4px 0px #000000;
  --nb-shadow-btn: 3px 3px 0px #000000;
  --nb-shadow-lg: 6px 6px 0px #000000;
  
  --bx-navy-border: #30363d;
  --text-primary: #ffffff;
  --text-secondary: #cbd5e1;
  --text-muted: #8b949e;
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html, body {
  height: 100%;
  width: 100%;
}

body.site-body {
  font-family: var(--font-sans);
  background-color: var(--nb-bg);
  color: var(--nb-ink);
  line-height: 1.55;
  display: flex;
  flex-direction: column;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}

/* ==========================================================================
   MASTER HEADER (SOLID INK, ZERO GLASSMORPHISM)
   ========================================================================== */
.master-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background-color: var(--nb-header);
  border-bottom: var(--nb-border-thick);
  box-shadow: 0 3px 0px #000000;
  height: 56px;
  min-height: 56px;
  max-height: 56px;
  display: flex;
  align-items: center;
  overflow: hidden;
}

.header-inner {
  width: 100%;
  max-width: 100%;
  padding: 0 1.25rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  white-space: nowrap;
}

.header-brand {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  flex-shrink: 0;
}

.brandex-header-pill {
  background: #ffffff;
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  border-radius: var(--nb-radius);
  padding: 2px 8px;
  display: flex;
  align-items: center;
}

.brandex-header-img {
  height: 24px;
  width: auto;
  object-fit: contain;
  display: block;
}

.brand-titles {
  display: flex;
  flex-direction: column;
  line-height: 1.15;
}

.brand-title {
  font-family: var(--font-display);
  font-weight: 900;
  font-size: 0.95rem;
  letter-spacing: -0.01em;
  color: var(--nb-ink);
}

.brand-subtitle {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  color: var(--nb-ink-muted);
}

/* Mode Selector Tabs */
.mode-tabs {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  flex-shrink: 0;
}

.mode-tab {
  font-family: var(--font-display);
  background-color: var(--nb-card);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  border-radius: var(--nb-radius);
  padding: 0 0.85rem;
  height: 32px;
  font-size: 0.82rem;
  font-weight: 800;
  color: var(--nb-ink);
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  white-space: nowrap;
  transition: transform 0.1s ease, box-shadow 0.1s ease, background 0.1s ease;
}

.mode-tab:hover {
  transform: translate(-1px, -1px);
  box-shadow: var(--nb-shadow-btn);
  background-color: var(--nb-card-alt);
}

.mode-tab:active {
  transform: translate(2px, 2px);
  box-shadow: var(--nb-shadow-pressed);
}

.mode-tab.active {
  background-color: var(--nb-yellow);
  color: #000000;
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-btn);
}

.tab-icon {
  font-size: 0.95rem;
}

/* Header Right Actions */
.header-right-actions {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  flex-shrink: 0;
}

/* Buttons (Tactile Neo-Brutalist Mechanical Feel) */
.btn {
  font-family: var(--font-display);
  font-size: 0.85rem;
  font-weight: 800;
  padding: 0.45rem 0.95rem;
  border-radius: var(--nb-radius);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-btn);
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
  text-decoration: none;
  white-space: nowrap;
  transition: transform 0.1s ease, box-shadow 0.1s ease, background 0.1s ease;
}

.btn:hover {
  transform: translate(-1px, -1px);
  box-shadow: var(--nb-shadow-hover);
}

.btn:active {
  transform: translate(2px, 2px);
  box-shadow: var(--nb-shadow-pressed);
}

.btn-primary {
  background-color: var(--nb-navy);
  color: #ffffff;
}
.btn-primary:hover {
  background-color: #1a2c4e;
}

.btn-outline {
  background-color: var(--nb-card);
  color: var(--nb-ink);
}
.btn-outline:hover {
  background-color: var(--nb-card-alt);
}

.btn-ghost {
  background: transparent;
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  color: var(--nb-ink);
}

.btn-xs {
  font-size: 0.78rem;
  padding: 0 0.65rem;
  height: 32px;
}

.btn-sm {
  font-size: 0.8rem;
  padding: 0.35rem 0.75rem;
  height: 30px;
}

.btn-large {
  font-size: 1.1rem;
  padding: 0.85rem 2rem;
  border-radius: var(--nb-radius-card);
}

/* Responsive Header */
@media (max-width: 1440px) {
  .brand-subtitle { display: none; }
  .header-inner { padding: 0 0.85rem; gap: 0.4rem; }
  .mode-tab { padding: 0 0.65rem; font-size: 0.78rem; }
  .header-right-actions .btn { padding: 0 0.5rem; font-size: 0.74rem; }
}

@media (max-width: 1180px) {
  #tabOverview { display: none; }
  #projectorBoostBtn { display: none; }
}

/* ==========================================================================
   PRESENTATION STAGE (PANORAMIC 100VW CAROUSEL DECK)
   ========================================================================== */
.deck-wrapper {
  width: 100vw;
  height: calc(100vh - 56px);
  max-width: 100%;
  padding: 0.5rem 1.25rem 0.75rem;
  margin: 0;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-sizing: border-box;
  overflow: hidden;
}

.deck-top-bar {
  width: 100%;
  height: 36px;
  min-height: 36px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.35rem;
  gap: 0.75rem;
  flex-shrink: 0;
  z-index: 10;
}

.deck-info {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: nowrap;
  overflow: hidden;
}

.section-tag {
  font-family: var(--font-display);
  font-size: 0.78rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: #000000;
  background-color: var(--nb-yellow);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  padding: 0.25rem 0.75rem;
  border-radius: var(--nb-radius);
  white-space: nowrap;
}

.deck-timing-badge {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 800;
  color: var(--nb-ink);
  background-color: var(--nb-card);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  padding: 0.25rem 0.75rem;
  border-radius: var(--nb-radius);
  white-space: nowrap;
}

.deck-counter {
  font-family: var(--font-mono);
  font-weight: 900;
  font-size: 1.05rem;
  background-color: var(--nb-card);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  border-radius: var(--nb-radius);
  padding: 0.25rem 0.85rem;
  display: flex;
  align-items: center;
  gap: 0.35rem;
}

.current-slide-num {
  color: var(--nb-ink);
  font-weight: 900;
}

.counter-slash {
  color: var(--nb-blue);
  font-weight: 900;
}

.total-slides-num {
  color: var(--nb-ink-muted);
}

.deck-progress-bar {
  width: 100%;
  height: 8px;
  background-color: var(--nb-card-alt);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  border-radius: 999px;
  overflow: hidden;
  margin-bottom: 0.65rem;
  flex-shrink: 0;
}

.deck-progress-fill {
  height: 100%;
  background-color: var(--nb-blue);
  transition: width 0.2s ease-out;
}

/* VIEWPORT & NAVIGATION ARROWS */
.carousel-stage {
  width: 100%;
  flex: 1;
  min-height: 0;
  position: relative;
  display: flex;
  align-items: stretch;
  justify-content: center;
}

.slides-viewport {
  width: 100%;
  height: 100%;
  min-height: 0;
  background-color: var(--nb-stage);
  border: var(--nb-border-thick);
  border-radius: var(--nb-radius-card);
  box-shadow: var(--nb-shadow-lg);
  padding: 1rem 1.5rem;
  overflow: hidden;
  position: relative;
  display: flex;
  align-items: stretch;
  justify-content: center;
}

.carousel-nav-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 44px;
  height: 44px;
  border-radius: var(--nb-radius);
  background-color: var(--nb-card);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-btn);
  color: var(--nb-ink);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 30;
  transition: transform 0.1s ease, box-shadow 0.1s ease, background 0.1s ease;
}

.carousel-nav-btn:hover {
  background-color: var(--nb-yellow);
  transform: translateY(-50%) translate(-1px, -1px);
  box-shadow: var(--nb-shadow-hover);
}

.carousel-nav-btn:active {
  transform: translateY(-50%) translate(2px, 2px);
  box-shadow: var(--nb-shadow-pressed);
}

.prev-arrow { left: -18px; }
.next-arrow { right: -18px; }

/* Slide Animation */
.carousel-slide {
  display: none !important;
  width: 100%;
  height: 100%;
}

.carousel-slide.active {
  display: flex !important;
  width: 100%;
  height: 100%;
  align-items: stretch;
  justify-content: center;
}

/* ==========================================================================
   PANORAMIC DUAL-PANEL LAYOUT (PART A + PART B)
   ========================================================================== */
.merged-slide-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 0.75rem;
  overflow: hidden;
}

.merged-slide-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: var(--nb-border);
  padding-bottom: 0.5rem;
  flex-shrink: 0;
}

.m-badge-group {
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.m-badge {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 0.2rem 0.65rem;
  border-radius: var(--nb-radius);
  border: var(--nb-border-sm);
  box-shadow: var(--nb-shadow-sm);
}

.badge-gradient, .badge-yellow {
  background-color: var(--nb-yellow);
  color: #000000;
}

.badge-navy {
  background-color: var(--nb-navy);
  color: #ffffff;
}

.badge-blue {
  background-color: var(--nb-blue);
  color: #ffffff;
}

.m-slide-title {
  font-family: var(--font-display);
  font-size: 1.35rem;
  font-weight: 900;
  color: var(--nb-ink);
  letter-spacing: -0.02em;
}

.title-sep {
  color: var(--nb-blue);
  margin: 0 0.35rem;
}

/* 2-Column Grid */
.merged-slide-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.25rem;
  flex: 1;
  min-height: 0;
  align-items: stretch;
}

.m-panel {
  background-color: var(--nb-card-panel);
  border: var(--nb-border);
  border-radius: var(--nb-radius);
  padding: 1.25rem 1.5rem;
  box-shadow: var(--nb-shadow);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  overflow-y: auto;
  color: var(--nb-ink);
  position: relative;
}

.merged-slide-single {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  background-color: var(--nb-card-panel);
  border: var(--nb-border);
  border-radius: var(--nb-radius);
  padding: 2rem;
  box-shadow: var(--nb-shadow);
}

/* ==========================================================================
   EDITORIAL & SLIDE CONTENT TYPOGRAPHY
   ========================================================================== */
.poster-slide-card {
  width: 100% !important;
  max-width: 100% !important;
  background-color: transparent !important;
  border: none !important;
  box-shadow: none !important;
  padding: 0 !important;
  text-align: left !important;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}

.poster-badge-row {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-bottom: 0.75rem;
}

.brutal-sticker {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 800;
  text-transform: uppercase;
  padding: 0.2rem 0.65rem;
  border-radius: var(--nb-radius);
  border: var(--nb-border-sm);
  box-shadow: var(--nb-shadow-sm);
}

.sticker-pink { background-color: #ff5376; color: #ffffff; }
.sticker-cyan { background-color: #38bdf8; color: #000000; }
.sticker-lime { background-color: var(--nb-mint); color: #000000; }
.sticker-yellow { background-color: var(--nb-yellow); color: #000000; }

.brutal-stamp {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 800;
  background: var(--nb-card-alt);
  border: var(--nb-border-sm);
  box-shadow: var(--nb-shadow-sm);
  color: var(--nb-ink);
  padding: 0.2rem 0.6rem;
  border-radius: var(--nb-radius);
}

.poster-hero-heading, .slide-hero-title, .slide-title-large, .slide-massive-quote, .slide-heading-standard {
  font-family: var(--font-display);
  font-size: 1.75rem !important;
  font-weight: 900 !important;
  line-height: 1.25 !important;
  letter-spacing: -0.03em !important;
  color: var(--nb-ink) !important;
  margin-bottom: 0.75rem !important;
}

.poster-highlight, .text-highlight {
  background-color: var(--nb-yellow);
  color: #000000 !important;
  padding: 0.1rem 0.45rem;
  border: var(--nb-border-sm);
  border-radius: 3px;
  display: inline-block;
  font-weight: 800;
}

.slide-hero-sub, .slide-sub, .slide-quote-sub, .slide-statement {
  font-size: 1.05rem;
  font-weight: 500;
  color: var(--nb-ink-secondary);
  line-height: 1.5;
  margin-bottom: 0.85rem;
}

.slide-eyebrow, .rule-super-badge {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  background-color: var(--nb-navy);
  color: #ffffff;
  border: var(--nb-border-sm);
  box-shadow: var(--nb-shadow-sm);
  padding: 0.25rem 0.75rem;
  border-radius: var(--nb-radius);
  margin-bottom: 0.75rem;
}

/* ==========================================================================
   CONTRAST & COMPARISON BOXES (BAD VS GOOD)
   ========================================================================== */
.poster-contrast-grid, .comparison-cards-editorial, .split-comparison {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.85rem;
  margin: 0.75rem 0;
  width: 100%;
}

.contrast-col, .comp-box, .split-col {
  background-color: var(--nb-card-alt);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  border-radius: var(--nb-radius);
  padding: 1rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 0.5rem;
}

.col-bad, .split-bad {
  background-color: var(--nb-coral-light);
  border-color: var(--nb-coral);
}

.col-good, .split-good {
  background-color: var(--nb-mint-light);
  border-color: var(--nb-mint);
}

.contrast-header, .comp-who, .split-tag {
  font-family: var(--font-display);
  font-size: 0.82rem;
  font-weight: 900;
  text-transform: uppercase;
  color: var(--nb-ink);
}

.col-bad .contrast-header, .split-bad .split-tag { color: var(--nb-coral); }
.col-good .contrast-header, .split-good .split-tag { color: var(--nb-mint); }

.contrast-body, .comp-quote {
  font-size: 0.95rem;
  font-weight: 500;
  line-height: 1.45;
  color: var(--nb-ink);
}

.contrast-stat-tag, .contrast-tag, .comp-result {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 800;
  background: var(--nb-card);
  border: var(--nb-border-sm);
  padding: 0.25rem 0.6rem;
  border-radius: 3px;
  width: fit-content;
  color: var(--nb-ink);
}

.poster-footer-strip, .takeaway-strip, .slide-bottom-note {
  background-color: var(--nb-card-alt);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  border-radius: var(--nb-radius);
  padding: 0.65rem 1rem;
  font-size: 0.92rem;
  font-weight: 600;
  color: var(--nb-ink);
  display: flex;
  align-items: center;
  gap: 0.6rem;
  margin-top: 0.75rem;
}

.poster-footer-strip strong, .takeaway-strip strong {
  color: var(--nb-ink);
}

/* Option Cards (Interactive Choices) */
.options-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.75rem;
  margin: 0.75rem 0;
  width: 100%;
}

.option-card {
  background-color: var(--nb-card);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-btn);
  border-radius: var(--nb-radius);
  padding: 0.85rem 1rem;
  font-size: 0.95rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  cursor: pointer;
  transition: transform 0.1s ease, box-shadow 0.1s ease, background 0.1s ease;
  color: var(--nb-ink);
}

.option-card:hover {
  background-color: var(--nb-yellow);
  transform: translate(-1px, -1px);
  box-shadow: var(--nb-shadow-hover);
}

.option-card:active {
  transform: translate(2px, 2px);
  box-shadow: var(--nb-shadow-pressed);
}

.option-card.highlight {
  background-color: #fef08a;
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-btn);
}

.opt-letter {
  width: 30px;
  height: 30px;
  border-radius: var(--nb-radius);
  background-color: var(--nb-navy);
  border: var(--nb-border-sm);
  color: #ffffff;
  font-family: var(--font-mono);
  font-weight: 900;
  font-size: 0.95rem;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

/* ==========================================================================
   CODE & PROMPT DISPLAY (PHYSICAL TERMINAL PRINTS)
   ========================================================================== */
.prompt-box-editorial {
  background-color: var(--nb-card);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow);
  border-radius: var(--nb-radius);
  padding: 1rem;
  margin: 0.65rem 0;
}

.pb-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.5rem;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 800;
  color: var(--nb-ink);
}

.prompt-code, pre.prompt-code {
  background-color: #0b1120 !important;
  color: #38bdf8 !important;
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  border-radius: var(--nb-radius);
  padding: 0.85rem 1rem;
  font-family: var(--font-mono);
  font-size: 0.85rem;
  line-height: 1.5;
  white-space: pre-wrap;
  word-break: break-word;
  overflow-x: auto;
}

.prompt-code .var-class, .prompt-code .var-topic {
  background-color: #1e293b;
  color: #fde047;
  padding: 1px 4px;
  border-radius: 2px;
  border: 1px solid #334155;
  font-weight: 700;
}

.tool-links-editorial {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 0.65rem;
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--nb-ink);
}

.bad-prompt-banner {
  background-color: var(--nb-coral-light);
  border: var(--nb-border);
  border-color: var(--nb-coral);
  box-shadow: var(--nb-shadow-sm);
  border-radius: var(--nb-radius);
  padding: 0.75rem 1rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin: 0.65rem 0;
}

.bad-prompt-tag {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 900;
  background-color: var(--nb-coral);
  color: #ffffff;
  padding: 0.2rem 0.5rem;
  border-radius: 2px;
}

.bad-prompt-text {
  font-family: var(--font-mono);
  font-size: 1.05rem;
  font-weight: 800;
  color: #991b1b;
}

.formula-tags-editorial {
  display: flex;
  gap: 0.4rem;
  flex-wrap: wrap;
  margin: 0.5rem 0;
}

.formula-tags-editorial span {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  background-color: var(--nb-card);
  border: var(--nb-border-sm);
  box-shadow: var(--nb-shadow-sm);
  padding: 0.2rem 0.5rem;
  border-radius: 3px;
  color: var(--nb-ink);
}

/* Offline Backup Box */
.backup-box-editorial {
  background-color: #fefce8;
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  border-radius: var(--nb-radius);
  margin: 0.75rem 0;
  overflow: hidden;
}

.backup-header-btn {
  padding: 0.6rem 0.85rem;
  background-color: #fef08a;
  border-bottom: var(--nb-border-sm);
  font-family: var(--font-display);
  font-size: 0.85rem;
  font-weight: 800;
  color: #713f12;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.backup-body {
  padding: 0.85rem 1rem;
  font-size: 0.9rem;
  line-height: 1.5;
  color: #451a03;
}

/* Media embeds in panels */
.slide-presentation-img, .notebooklm-visual-mock {
  width: 100%;
  max-height: 220px;
  object-fit: cover;
  border-radius: var(--nb-radius);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  margin: 0.5rem 0;
}

.slide-media-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  align-items: center;
  margin: 0.5rem 0;
}

/* Flow sequences */
.flow-sequence-box {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin: 0.75rem 0;
  flex-wrap: wrap;
}

.seq-step {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 800;
  background-color: var(--nb-card);
  border: var(--nb-border-sm);
  box-shadow: var(--nb-shadow-sm);
  color: var(--nb-ink);
  padding: 0.35rem 0.75rem;
  border-radius: 3px;
}

.seq-step.highlight {
  background-color: var(--nb-yellow);
  color: #000000;
}

.seq-arr {
  color: var(--nb-blue);
  font-weight: 900;
  font-size: 1.1rem;
}

/* Tables */
.attention-table, .brutal-table, .skills-syllabus-table-wrap table {
  width: 100%;
  border-collapse: collapse;
  border: var(--nb-border);
  box-shadow: var(--nb-shadow);
  border-radius: var(--nb-radius);
  overflow: hidden;
  margin: 0.85rem 0;
}

.attention-table th, .brutal-table th, .skills-syllabus-table-wrap th {
  background-color: var(--nb-navy);
  color: #ffffff;
  padding: 0.75rem 1rem;
  font-family: var(--font-display);
  font-size: 0.85rem;
  font-weight: 900;
  text-transform: uppercase;
  text-align: left;
  border-bottom: var(--nb-border);
}

.attention-table td, .brutal-table td, .skills-syllabus-table-wrap td {
  padding: 0.75rem 1rem;
  font-size: 0.9rem;
  border-bottom: 1px solid #cbd5e1;
  background-color: var(--nb-card);
  color: var(--nb-ink);
}

.attention-table tr:hover td, .brutal-table tr:hover td {
  background-color: var(--nb-card-alt);
}

/* ==========================================================================
   CAROUSEL BOTTOM BAR & PRESENTER NOTES DRAWER
   ========================================================================== */
.deck-bottom-bar {
  width: 100%;
  height: 40px;
  min-height: 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 0.5rem;
  gap: 0.75rem;
  flex-shrink: 0;
  z-index: 10;
}

.deck-nav-buttons {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.deck-slide-actions {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.keyboard-hint {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--nb-ink-muted);
}

.shortcut-key-badge {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 800;
  background: var(--nb-card);
  border: var(--nb-border-sm);
  box-shadow: 1px 1px 0px #000000;
  padding: 0.15rem 0.45rem;
  border-radius: 3px;
  color: var(--nb-ink);
}

/* Presenter Script Drawer */
.presenter-script-drawer {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: var(--nb-card);
  border-top: var(--nb-border-thick);
  box-shadow: 0 -4px 0px #000000;
  z-index: 150;
  transform: translateY(100%);
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  max-height: 42vh;
  display: flex;
  flex-direction: column;
}

.presenter-script-drawer.open {
  transform: translateY(0);
}

.drawer-header {
  padding: 0.75rem 1.5rem;
  background-color: var(--nb-card-alt);
  border-bottom: var(--nb-border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.drawer-title {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  font-family: var(--font-display);
  font-size: 0.9rem;
  font-weight: 800;
  color: var(--nb-ink);
}

.drawer-cue-tag {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 800;
  background-color: var(--nb-yellow);
  color: #000000;
  border: var(--nb-border-sm);
  padding: 0.2rem 0.6rem;
  border-radius: 3px;
}

.drawer-close-btn {
  background: var(--nb-card);
  border: var(--nb-border-sm);
  box-shadow: var(--nb-shadow-sm);
  color: var(--nb-ink);
  font-size: 1.25rem;
  cursor: pointer;
  width: 28px;
  height: 28px;
  border-radius: 3px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.drawer-close-btn:hover {
  background: var(--nb-coral);
  color: #ffffff;
}

.drawer-content {
  padding: 1.25rem 1.5rem;
  overflow-y: auto;
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--nb-ink);
}

.script-text {
  font-size: 1.05rem;
  line-height: 1.65;
  color: var(--nb-ink);
}

.script-teaching-objective {
  margin-top: 1rem;
  padding: 0.75rem 1rem;
  background-color: var(--nb-card-alt);
  border-left: 4px solid var(--nb-blue);
  border: var(--nb-border-sm);
  border-left-width: 4px;
  font-size: 0.88rem;
  color: var(--nb-ink-secondary);
}

/* ==========================================================================
   STAGE 30s COUNTDOWN TIMER (FOR AUDITORIUM CHALLENGES)
   ========================================================================== */
.stage-countdown-card {
  background-color: var(--nb-card);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow);
  border-radius: var(--nb-radius);
  padding: 1rem 1.25rem;
  margin: 0.75rem 0;
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
}

.countdown-header-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.countdown-title-wrap {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.countdown-badge {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 800;
  background-color: var(--nb-yellow);
  color: #000000;
  border: var(--nb-border-sm);
  padding: 0.15rem 0.5rem;
  border-radius: 3px;
}

.countdown-title-wrap strong {
  font-family: var(--font-display);
  font-size: 0.95rem;
  font-weight: 800;
  color: var(--nb-ink);
}

.countdown-digital {
  font-family: var(--font-mono);
  font-size: 1.4rem;
  font-weight: 900;
  color: var(--nb-ink);
  background-color: var(--nb-yellow);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  padding: 0.2rem 0.85rem;
  border-radius: var(--nb-radius);
}

.countdown-digital.flash {
  animation: digitalFlash 0.5s infinite alternate;
  background-color: var(--nb-coral);
  color: #ffffff;
}

@keyframes digitalFlash {
  from { transform: scale(1); }
  to { transform: scale(1.06); }
}

.countdown-progress-track {
  width: 100%;
  height: 10px;
  background-color: var(--nb-card-alt);
  border: var(--nb-border);
  box-shadow: 1px 1px 0px #000000;
  border-radius: 999px;
  overflow: hidden;
}

.countdown-progress-bar {
  height: 100%;
  width: 100%;
  background-color: var(--nb-blue);
  transition: width 1s linear, background-color 0.3s ease;
}

.countdown-progress-bar.warning {
  background-color: var(--nb-yellow);
}

.countdown-progress-bar.danger {
  background-color: var(--nb-coral);
}

.countdown-actions-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem;
}

.countdown-hint {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--nb-ink-muted);
}

/* ==========================================================================
   STUDENT COMPUTER LAB (7 HANDS-ON MISSIONS)
   ========================================================================== */
.lab-wrapper {
  width: 100vw;
  height: calc(100vh - 56px);
  max-width: 100%;
  padding: 0.75rem 1.5rem 1rem;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.lab-nav-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-bottom: 0.65rem;
  border-bottom: var(--nb-border);
  margin-bottom: 0.75rem;
  flex-shrink: 0;
}

.lab-meta-group {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.lab-step-indicator {
  font-family: var(--font-mono);
  font-weight: 900;
  font-size: 0.95rem;
  background-color: var(--nb-yellow);
  color: #000000;
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  padding: 0.25rem 0.75rem;
  border-radius: var(--nb-radius);
}

.lab-current-topic {
  font-family: var(--font-display);
  font-size: 0.95rem;
  font-weight: 800;
  color: var(--nb-ink);
}

.lab-right-tools {
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.lab-timer-chip {
  font-family: var(--font-mono);
  font-size: 0.85rem;
  font-weight: 800;
  background-color: var(--nb-card);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  padding: 0.3rem 0.75rem;
  border-radius: var(--nb-radius);
  color: var(--nb-ink);
}

.lab-missions-viewport {
  flex: 1;
  min-height: 0;
  position: relative;
  display: flex;
  align-items: stretch;
}

.lab-screens-container {
  width: 100%;
  height: 100%;
  position: relative;
}

.lab-card-screen {
  display: none !important;
  width: 100%;
  height: 100%;
  background-color: var(--nb-stage);
  border: var(--nb-border-thick);
  border-radius: var(--nb-radius-card);
  box-shadow: var(--nb-shadow-lg);
  padding: 1.5rem 2rem;
  overflow-y: auto;
}

.lab-card-screen.active {
  display: flex !important;
  flex-direction: column;
}

.lab-screen-content {
  max-width: 900px;
  margin: 0 auto;
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.mission-tag {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 800;
  background-color: var(--nb-yellow);
  color: #000000;
  border: var(--nb-border-sm);
  box-shadow: var(--nb-shadow-sm);
  padding: 0.2rem 0.65rem;
  border-radius: 3px;
  width: fit-content;
}

.mission-title {
  font-family: var(--font-display);
  font-size: 1.6rem;
  font-weight: 900;
  color: var(--nb-ink);
  letter-spacing: -0.02em;
}

.mission-desc {
  font-size: 1rem;
  color: var(--nb-ink-secondary);
  line-height: 1.5;
}

/* Forms & Inputs in Lab */
.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.form-group label {
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--nb-ink);
}

.form-input, .form-textarea {
  width: 100%;
  background-color: var(--nb-card);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  border-radius: var(--nb-radius);
  padding: 0.65rem 0.85rem;
  font-family: var(--font-sans);
  font-size: 0.95rem;
  color: var(--nb-ink);
  transition: border-color 0.1s ease, box-shadow 0.1s ease;
}

.form-input:focus, .form-textarea:focus {
  outline: none;
  border-color: var(--nb-blue);
  box-shadow: 3px 3px 0px var(--nb-blue);
}

.form-grid-editorial {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.pills-row {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.pill {
  font-family: var(--font-display);
  font-size: 0.85rem;
  font-weight: 800;
  background-color: var(--nb-card);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  border-radius: var(--nb-radius);
  padding: 0.4rem 0.85rem;
  cursor: pointer;
  color: var(--nb-ink);
  transition: transform 0.1s ease, box-shadow 0.1s ease;
}

.pill:hover {
  transform: translate(-1px, -1px);
  box-shadow: var(--nb-shadow-btn);
}

.pill.active {
  background-color: var(--nb-yellow);
  color: #000000;
  box-shadow: var(--nb-shadow-btn);
}

.mission-footer-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 1.5rem;
  padding-top: 1rem;
  border-top: var(--nb-border);
}

/* Submission Card & Report */
.final-report-card {
  background-color: var(--nb-card);
  border: var(--nb-border-thick);
  box-shadow: var(--nb-shadow-lg);
  border-radius: var(--nb-radius-card);
  padding: 1.5rem;
  margin-top: 1rem;
}

.report-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: var(--nb-border);
  padding-bottom: 0.75rem;
  margin-bottom: 1rem;
}

.report-header h3 {
  font-family: var(--font-display);
  font-size: 1.15rem;
  font-weight: 900;
}

.report-status {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 900;
  background-color: var(--nb-mint);
  color: #000000;
  border: var(--nb-border-sm);
  padding: 0.2rem 0.6rem;
  border-radius: 3px;
}

/* ==========================================================================
   MODALS (SLIDE NAVIGATOR, SOCRATIC SIMULATOR, CHEATSHEET, SHORTCUTS)
   ========================================================================== */
.nav-modal-backdrop, .sim-modal-backdrop, .cheatsheet-modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.75);
  z-index: 200;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
}

.nav-modal-backdrop.open, .sim-modal-backdrop.open, .cheatsheet-modal-backdrop.open {
  display: flex;
}

.nav-modal-content, .sim-modal-content, .cheatsheet-modal-content {
  background-color: var(--nb-stage);
  border: var(--nb-border-thick);
  border-radius: var(--nb-radius-card);
  box-shadow: var(--nb-shadow-xl);
  width: 100%;
  max-width: 1100px;
  max-height: 85vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.nav-modal-header, .sim-modal-header, .cheatsheet-modal-header {
  padding: 1rem 1.5rem;
  background-color: var(--nb-card-alt);
  border-bottom: var(--nb-border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-header-left, .sim-header-title {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.nav-title-icon, .sim-sparkle {
  font-size: 1.5rem;
}

.nav-title, .sim-header-title h3, .cheatsheet-modal-header h3 {
  font-family: var(--font-display);
  font-size: 1.1rem;
  font-weight: 900;
  color: var(--nb-ink);
}

.nav-subtitle, .sim-header-title p {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--nb-ink-muted);
}

.nav-close-btn {
  background: var(--nb-card);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  color: var(--nb-ink);
  font-size: 1.25rem;
  font-weight: 900;
  cursor: pointer;
  width: 32px;
  height: 32px;
  border-radius: var(--nb-radius);
  display: flex;
  align-items: center;
  justify-content: center;
}

.nav-close-btn:hover {
  background-color: var(--nb-coral);
  color: #ffffff;
}

.nav-modal-toolbar {
  padding: 0.75rem 1.5rem;
  border-bottom: var(--nb-border);
  background-color: var(--nb-card);
  display: flex;
  align-items: center;
  gap: 1rem;
}

.nav-search-input {
  flex: 1;
  background: var(--nb-card-alt);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  border-radius: var(--nb-radius);
  padding: 0.5rem 0.85rem;
  font-family: var(--font-mono);
  font-size: 0.85rem;
  color: var(--nb-ink);
}

.nav-grid {
  padding: 1.25rem 1.5rem;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 0.85rem;
  overflow-y: auto;
}

.nav-card {
  background-color: var(--nb-card);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  border-radius: var(--nb-radius);
  padding: 0.85rem 1rem;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 0.5rem;
  transition: transform 0.1s ease, box-shadow 0.1s ease;
}

.nav-card:hover {
  transform: translate(-1px, -1px);
  box-shadow: var(--nb-shadow-btn);
  background-color: #fef08a;
}

.nav-card.active {
  background-color: var(--nb-yellow);
  border: var(--nb-border-thick);
}

.nav-card-num {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 900;
  color: var(--nb-blue);
}

.nav-card-title {
  font-family: var(--font-display);
  font-size: 0.92rem;
  font-weight: 800;
  color: var(--nb-ink);
}

/* Socratic Simulator Modal Body */
.sim-modal-body, .cheatsheet-modal-body {
  padding: 1.5rem;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.sim-question-card {
  background-color: var(--nb-card-alt);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  border-radius: var(--nb-radius);
  padding: 1rem;
}

.sim-badge {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 800;
  background-color: var(--nb-yellow);
  color: #000000;
  border: var(--nb-border-sm);
  padding: 0.15rem 0.5rem;
  border-radius: 3px;
  display: inline-block;
  margin-bottom: 0.5rem;
}

.sim-sample-chips {
  display: flex;
  gap: 0.4rem;
  flex-wrap: wrap;
  align-items: center;
}

.sim-chip {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 700;
  background-color: var(--nb-card);
  border: var(--nb-border-sm);
  box-shadow: 1px 1px 0px #000000;
  padding: 0.25rem 0.6rem;
  border-radius: 3px;
  cursor: pointer;
}

.sim-chip:hover {
  background-color: var(--nb-yellow);
}

.sim-feedback-result {
  background-color: var(--nb-card-alt);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  border-radius: var(--nb-radius);
  padding: 1.25rem;
  line-height: 1.55;
}

/* Cheatsheet Grid */
.cheatsheet-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1rem;
}

.cheatsheet-card {
  background-color: var(--nb-card);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  border-radius: var(--nb-radius);
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.cheatsheet-card h4 {
  font-family: var(--font-display);
  font-size: 0.95rem;
  font-weight: 900;
  color: var(--nb-ink);
}

.cheatsheet-list {
  padding-left: 1.25rem;
  font-size: 0.88rem;
  color: var(--nb-ink-secondary);
  line-height: 1.5;
}

/* Shortcuts Table */
.shortcuts-table {
  width: 100%;
  border-collapse: collapse;
  border: var(--nb-border);
}

.shortcuts-table th {
  background-color: var(--nb-navy);
  color: #ffffff;
  padding: 0.65rem 1rem;
  font-family: var(--font-display);
  font-size: 0.82rem;
  font-weight: 900;
  text-align: left;
  border-bottom: var(--nb-border);
}

.shortcuts-table td {
  padding: 0.65rem 1rem;
  font-size: 0.88rem;
  border-bottom: 1px solid #cbd5e1;
  background-color: var(--nb-card);
  color: var(--nb-ink);
}

/* ==========================================================================
   TOAST NOTIFICATIONS
   ========================================================================== */
.toast-container {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  z-index: 999;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  pointer-events: none;
}

.toast-message {
  pointer-events: auto;
  background-color: var(--nb-yellow);
  color: #000000;
  border: var(--nb-border);
  box-shadow: var(--nb-shadow);
  border-radius: var(--nb-radius);
  padding: 0.75rem 1.25rem;
  font-family: var(--font-display);
  font-size: 0.9rem;
  font-weight: 800;
  display: flex;
  align-items: center;
  gap: 0.6rem;
  animation: toastPop 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes toastPop {
  from { opacity: 0; transform: translateY(12px) scale(0.95); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}

/* ==========================================================================
   PRINT STYLES FOR CHEATSHEET & STUDENT CERTIFICATE
   ========================================================================== */
@media print {
  body {
    background: #ffffff !important;
    color: #000000 !important;
  }
  .master-header, .deck-wrapper, .lab-wrapper, .overview-wrapper,
  .nav-modal-backdrop, .sim-modal-backdrop, .toast-container, .carousel-nav-btn {
    display: none !important;
  }
  .cheatsheet-modal-backdrop {
    display: block !important;
    position: static !important;
    background: none !important;
    padding: 0 !important;
  }
  .cheatsheet-modal-content {
    border: none !important;
    box-shadow: none !important;
    max-width: 100% !important;
    background: #ffffff !important;
  }
  .cheatsheet-modal-header button {
    display: none !important;
  }
  .cheatsheet-card {
    page-break-inside: avoid;
    border: 1px solid #000000 !important;
    box-shadow: none !important;
  }
}
"""

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Wrote Neo-Brutalist styles.css successfully!')

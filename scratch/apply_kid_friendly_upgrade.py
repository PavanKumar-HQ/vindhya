import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Hide the repetitive duplicate inner slide header
css = css.replace('.merged-slide-header {', '''.merged-slide-header {
  display: none !important;''', 1)

# 2. Add rich styles for bullets, meters, panic strips, options, and kid-friendly animations
new_components = """
/* ==========================================================================
   HIGH-ENERGY KID-FRIENDLY VISUAL COMPONENTS & NEGATIVE SPACE FILLERS
   ========================================================================== */

/* Animated Slide Pop Entry */
.carousel-slide.active {
  display: flex !important;
  animation: kidSlidePop 0.28s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
}

@keyframes kidSlidePop {
  0% {
    opacity: 0;
    transform: scale(0.975) translateY(10px);
  }
  100% {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

/* Floating Badges & Stickers */
@keyframes kidFloat {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-4px) rotate(2deg); }
}

.brutal-sticker, .m-badge {
  animation: kidFloat 4s ease-in-out infinite;
}

/* Situation & Bullet Cards (Fills negative space with tactile interactive items) */
.bullet-list-editorial {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  width: 100%;
  margin: 0.85rem 0;
}

.bullet-item {
  background: var(--nb-card);
  border: 2px solid #000000;
  box-shadow: 3px 3px 0px #000000;
  border-radius: 6px;
  padding: 0.95rem 1.35rem;
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--nb-ink);
  display: flex;
  align-items: center;
  gap: 0.85rem;
  transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
  cursor: pointer;
}

.bullet-item:hover {
  transform: translateX(6px) scale(1.015);
  box-shadow: 5px 5px 0px #000000;
  background-color: #fef08a;
}

.bullet-item:active {
  transform: translate(2px, 2px);
  box-shadow: 1px 1px 0px #000000;
}

.bullet-item.highlight {
  background-color: #fee2e2;
  border-color: #dc2626;
  box-shadow: 3px 3px 0px #dc2626;
  color: #991b1b;
  font-weight: 800;
}

.b-icon {
  font-size: 1.4rem;
  flex-shrink: 0;
}

/* Retention & Memory Meters */
.retention-meter-card {
  background: var(--nb-card);
  border: 2px solid #000000;
  box-shadow: 3px 3px 0px #000000;
  border-radius: 8px;
  padding: 1rem 1.25rem;
  width: 100%;
  margin-top: 1rem;
}

.meter-row {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
}

.meter-label {
  display: flex;
  justify-content: space-between;
  font-size: 0.95rem;
  font-weight: 800;
  color: var(--nb-ink);
}

.meter-track {
  width: 100%;
  height: 12px;
  background: #e2e8f0;
  border: 2px solid #000000;
  border-radius: 999px;
  overflow: hidden;
  box-shadow: 1px 1px 0px #000000;
}

.meter-fill {
  height: 100%;
  transition: width 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.meter-fill.fill-bad { background-color: #ef4444; }
.meter-fill.fill-good { background-color: #10b981; }

/* Panic Meter / Relatable Night-Before Strip */
.panic-meter-strip {
  background: #fee2e2;
  border: 2px solid #dc2626;
  box-shadow: 3px 3px 0px #dc2626;
  border-radius: 8px;
  padding: 0.85rem 1.25rem;
  display: flex;
  align-items: center;
  gap: 0.85rem;
  margin-top: 1rem;
  color: #991b1b;
  font-size: 1.05rem;
  font-weight: 700;
}

.panic-icon {
  font-size: 1.5rem;
  flex-shrink: 0;
}

/* Quick Tools Launcher Grid inside Modal */
.modal-tools-launcher-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 0.65rem;
  margin-bottom: 1.25rem;
  padding-bottom: 1.25rem;
  border-bottom: var(--nb-border);
}

.modal-tools-launcher-grid .btn {
  justify-content: flex-start;
}
"""

css += "\n" + new_components

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated styles.css with kid-friendly components and animations!')

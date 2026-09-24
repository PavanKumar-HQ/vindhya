with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add vote result meter styles
vote_meter_css = """
/* Interactive Audience Vote Result Meter */
.vote-result-meter {
  width: 100%;
  margin-top: 0.75rem;
  padding-top: 0.5rem;
  border-top: 1.5px dashed #000000;
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  animation: fadeInVote 0.25s ease-out;
}

@keyframes fadeInVote {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

.vote-meter-label {
  display: flex;
  justify-content: space-between;
  font-family: var(--font-mono);
  font-size: 0.85rem;
  font-weight: 900;
  color: #000000;
}

.vote-meter-bar {
  width: 100%;
  height: 10px;
  background: #e2e8f0;
  border: 1.5px solid #000000;
  box-shadow: 1px 1px 0px #000000;
  border-radius: 999px;
  overflow: hidden;
}

.vote-meter-fill {
  height: 100%;
  width: 0%;
  background: #2563eb;
  transition: width 0.7s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.option-card.highlight .vote-meter-fill, .vote-option.vo-winner .vote-meter-fill {
  background: #10b981;
}
"""

css += "\n" + vote_meter_css

# Update deck-top-bar in styles.css
old_top_bar = """.deck-top-bar {
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
}"""

new_top_bar = """.deck-top-bar {
  width: 100%;
  height: 44px;
  min-height: 44px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.5rem;
  gap: 0.75rem;
  flex-shrink: 0;
  z-index: 10;
}"""

css = css.replace(old_top_bar, new_top_bar, 1)

# Update deck-timing-badge font in styles.css
old_dtb = """.deck-timing-badge {
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
}"""

new_dtb = """.deck-timing-badge {
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 900;
  color: var(--nb-ink);
  background-color: var(--nb-card);
  border: var(--nb-border);
  box-shadow: var(--nb-shadow-sm);
  padding: 0.3rem 0.85rem;
  border-radius: var(--nb-radius);
  white-space: nowrap;
}"""

css = css.replace(old_dtb, new_dtb, 1)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated styles.css with polished bar and vote meters')

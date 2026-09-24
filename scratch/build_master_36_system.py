import os
import re

def make_slide(idx, section, title, left_html, right_html, is_single=False, single_html=""):
    num_str = f"{idx+1:02d}"
    active_cls = " active" if idx == 0 else ""
    
    if is_single:
        return f"""
        <!-- SLIDE {num_str}: {title} -->
        <div class="carousel-slide{active_cls}" data-index="{idx}" data-section="{section}" data-title="{title}">
          <div class="merged-slide-container">
            <div class="merged-slide-header" style="display: none !important;">
              <h2 class="m-slide-title">{title}</h2>
            </div>
            <div class="merged-slide-single">
              {single_html}
            </div>
          </div>
        </div>"""
    else:
        return f"""
        <!-- SLIDE {num_str}: {title} -->
        <div class="carousel-slide{active_cls}" data-index="{idx}" data-section="{section}" data-title="{title}">
          <div class="merged-slide-container">
            <div class="merged-slide-header" style="display: none !important;">
              <h2 class="m-slide-title">{title}</h2>
            </div>
            
            <div class="merged-slide-grid">
              <div class="m-panel panel-left">
                {left_html}
              </div>
              <div class="m-panel panel-right">
                {right_html}
              </div>
            </div>
          </div>
        </div>"""

print("Declared slide builder function.")

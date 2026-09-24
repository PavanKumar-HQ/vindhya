import re

def build_slide(index, section, title, left_content, right_content, is_single=False, single_content=""):
    num_str = f"{index+1:02d}"
    active_cls = " active" if index == 0 else ""
    
    if is_single:
        return f'''<!-- MERGED SLIDE {num_str}: {title} -->
        <div class="carousel-slide{active_cls}" data-index="{index}" data-section="{section}" data-title="{title}">
          <div class="merged-slide-container">
            <div class="merged-slide-header">
              <div class="m-badge-group">
                <span class="m-badge badge-gradient">{section}</span>
                <span class="m-badge badge-navy">PART {num_str} OF 36</span>
              </div>
              <h2 class="m-slide-title">{title}</h2>
            </div>
            <div class="merged-slide-single">
              {single_content}
            </div>
          </div>
        </div>'''
    else:
        return f'''<!-- MERGED SLIDE {num_str}: {title} -->
        <div class="carousel-slide{active_cls}" data-index="{index}" data-section="{section}" data-title="{title}">
          <div class="merged-slide-container">
            <div class="merged-slide-header">
              <div class="m-badge-group">
                <span class="m-badge badge-gradient">{section}</span>
                <span class="m-badge badge-navy">PART {num_str} OF 36</span>
              </div>
              <h2 class="m-slide-title">{title}</h2>
            </div>
            
            <div class="merged-slide-grid">
              <div class="m-panel panel-left">
                {left_content}
              </div>
              <div class="m-panel panel-right">
                {right_content}
              </div>
            </div>
          </div>
        </div>'''

print("Helper defined successfully")

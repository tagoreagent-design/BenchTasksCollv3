# Preprocessing Script for SEO Optimizer

import sys
sys.path.append('../../groundtruth_workspace')

from seo_optimizer import SEOOptimizer

# Preprocess HTML content
def preprocess_html(raw_html):
    """Clean and normalize HTML for analysis"""
    # Remove scripts and styles
    import re
    html = re.sub(r'<script.*?</script>', '', raw_html, flags=re.DOTALL)
    html = re.sub(r'<style.*?</style>', '', html, flags=re.DOTALL)
    return html.strip()

if __name__ == '__main__':
    raw = "<html><head><title>Test</title></head><body><script>alert(1)</script><p>Content</p></body></html>"
    print(preprocess_html(raw))

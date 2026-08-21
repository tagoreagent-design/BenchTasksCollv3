# Preprocessing Script for Blog Engine

import sys
sys.path.append('../../groundtruth_workspace')

from blog_engine import BlogEngine

# Preprocess blog content
def preprocess_content(raw_content):
    """Clean and normalize blog content"""
    # Basic markdown cleanup
    lines = raw_content.split('\n')
    cleaned = []
    for line in lines:
        line = line.rstrip()
        if line or cleaned and cleaned[-1]:
            cleaned.append(line)
    return '\n'.join(cleaned).strip()

if __name__ == '__main__':
    raw = "# Title\n\n\nContent here\n\n\n"
    print(preprocess_content(raw))

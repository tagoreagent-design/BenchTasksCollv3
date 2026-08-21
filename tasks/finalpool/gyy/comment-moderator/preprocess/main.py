# Preprocessing Script for Comment Moderator

import sys
sys.path.append('../../groundtruth_workspace')

from comment_moderator import CommentModerator

# Preprocess comment text
def preprocess_comment(text):
    """Clean and normalize comment text"""
    import re
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # Remove excessive punctuation
    text = re.sub(r'[!]{3,}', '!', text)
    text = re.sub(r'[?]{3,}', '?', text)
    return text

if __name__ == '__main__':
    raw = "   Great!!!   Article???   "
    print(preprocess_comment(raw))

# Evaluation Script for Comment Moderator

import sys
sys.path.append('../../groundtruth_workspace')

from comment_moderator import CommentModerator

def test_comment_moderator():
    cm = CommentModerator()
    
    # Test 1: Clean comment
    result = cm.moderate('Great article!', user_trust=0.9)
    assert result.action == 'approve'
    
    # Test 2: Spam comment
    result = cm.moderate('Buy cheap viagra!!!', user_trust=0.1)
    assert result.action == 'reject'
    
    # Test 3: Profanity
    result = cm.moderate('This is f***ing bad', user_trust=0.5)
    assert result.action in ['flag', 'reject']
    
    # Test 4: Borderline
    result = cm.moderate('Not sure about this', user_trust=0.5)
    assert result.action in ['approve', 'flag']
    
    print('All tests passed!')

if __name__ == '__main__':
    test_comment_moderator()

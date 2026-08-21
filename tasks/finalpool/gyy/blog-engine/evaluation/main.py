# Evaluation Script for Blog Engine

import sys
sys.path.append('../../groundtruth_workspace')

from blog_engine import BlogEngine

def test_blog_engine():
    be = BlogEngine()
    
    # Test 1: Create post
    post_id = be.create_post('My First Post', '# Hello\n\nWorld!', 'user1')
    
    # Test 2: Publish
    be.publish_post(post_id)
    post = be.get_post(post_id)
    assert post.status == 'published'
    
    # Test 3: Schedule
    future_id = be.create_post('Future Post', 'Content', 'user1')
    be.schedule_post(future_id, '2025-01-01')
    assert be.get_post(future_id).status == 'scheduled'
    
    # Test 4: Categories
    be.add_category(post_id, 'tech')
    assert 'tech' in be.get_categories(post_id)
    
    print('All tests passed!')

if __name__ == '__main__':
    test_blog_engine()

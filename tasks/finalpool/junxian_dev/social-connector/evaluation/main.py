# Evaluation Script for Social Connector

import sys
sys.path.append('../../groundtruth_workspace')

from social_connector import SocialConnector

def test_social_connector():
    sc = SocialConnector()
    
    # Test 1: Connect platforms
    sc.connect('twitter', 'token1')
    sc.connect('facebook', 'token2')
    
    # Test 2: Publish post
    post_id = sc.publish('Hello world!', ['twitter', 'facebook'])
    assert post_id is not None
    
    # Test 3: Schedule post
    scheduled = sc.schedule('Future post', ['twitter'], '2025-01-01 10:00')
    assert scheduled is not None
    
    # Test 4: Get analytics
    analytics = sc.get_analytics(post_id)
    assert 'impressions' in analytics
    assert 'engagements' in analytics
    
    # Test 5: Media upload
    media_id = sc.upload_media('image.jpg')
    assert media_id is not None
    
    print('All tests passed!')

if __name__ == '__main__':
    test_social_connector()

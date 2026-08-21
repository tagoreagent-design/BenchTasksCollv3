# Preprocessing Script for Social Connector

import sys
sys.path.append('../../groundtruth_workspace')

from social_connector import SocialConnector

# Preprocess social post
def preprocess_post(post_data):
    """Clean and validate post data"""
    content = post_data.get('content', '').strip()
    if not content:
        raise ValueError('Post content cannot be empty')
    
    platforms = post_data.get('platforms', [])
    valid_platforms = ['twitter', 'facebook', 'instagram', 'linkedin']
    platforms = [p for p in platforms if p in valid_platforms]
    if not platforms:
        raise ValueError('No valid platforms')
    
    return {
        'content': content[:280],  # Twitter limit
        'platforms': platforms,
        'media': post_data.get('media', []),
        'scheduled_time': post_data.get('scheduled_time')
    }

if __name__ == '__main__':
    print(preprocess_post({'content': 'Hello world!', 'platforms': ['twitter', 'facebook']}))

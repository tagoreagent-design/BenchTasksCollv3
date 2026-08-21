# Preprocessing Script for Wishlist Manager

import sys
sys.path.append('../../groundtruth_workspace')

from wishlist_manager import WishlistManager

# Preprocess wishlist data
def preprocess_wishlist(raw_data):
    """Clean and normalize wishlist data"""
    processed = []
    for item in raw_data:
        processed.append({
            'name': item.get('name', '').strip(),
            'url': item.get('url', '').strip(),
            'category': item.get('category', 'general'),
            'priority': item.get('priority', 'medium'),
            'notes': item.get('notes', '')
        })
    return processed

if __name__ == '__main__':
    raw = [
        {'name': 'Item 1', 'url': 'https://example.com/1', 'category': 'electronics'},
        {'name': 'Item 2', 'url': 'https://example.com/2', 'category': 'books'},
    ]
    print(preprocess_wishlist(raw))

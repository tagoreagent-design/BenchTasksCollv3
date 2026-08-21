# Evaluation Script for Wishlist Manager

import sys
sys.path.append('../../groundtruth_workspace')

from wishlist_manager import WishlistManager

def test_wishlist_manager():
    wm = WishlistManager()
    
    # Test 1: Create wishlist
    list_id = wm.create_wishlist('Birthday', 'user1')
    
    # Test 2: Add items
    wm.add_item(list_id, 'product1', 'https://example.com/1')
    wm.add_item(list_id, 'product2', 'https://example.com/2')
    assert wm.get_item_count(list_id) == 2
    
    # Test 3: Set price alert
    alert_id = wm.set_price_alert(list_id, 'product1', 50.00)
    
    # Test 4: Share wishlist
    share_url = wm.share_wishlist(list_id)
    assert 'wishlist' in share_url
    
    print('All tests passed!')

if __name__ == '__main__':
    test_wishlist_manager()

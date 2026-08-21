# Evaluation Script for Price Tracker

import sys
sys.path.append('../../groundtruth_workspace')

from price_tracker import PriceTracker

def test_price_tracker():
    pt = PriceTracker()
    
    # Test 1: Add product
    product_id = pt.add_product('iPhone 15', 'apple')
    
    # Test 2: Update price
    pt.update_price(product_id, 'Amazon', 799.99)
    pt.update_price(product_id, 'BestBuy', 829.99)
    
    # Test 3: Get best price
    best = pt.get_best_price(product_id)
    assert best['retailer'] == 'Amazon'
    assert best['price'] == 799.99
    
    # Test 4: Price alert
    alert_id = pt.set_alert(product_id, 750)
    assert pt.check_alerts(product_id) == []  # Price not low enough
    
    pt.update_price(product_id, 'Amazon', 749.99)
    alerts = pt.check_alerts(product_id)
    assert len(alerts) == 1
    
    print('All tests passed!')

if __name__ == '__main__':
    test_price_tracker()

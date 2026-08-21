# Evaluation Script for Inventory Management

import sys
sys.path.append('../../groundtruth_workspace')

from inventory_management import InventoryManagement

def test_inventory_management():
    im = InventoryManagement()
    
    # Test 1: Add product
    im.add_product('SKU001', 'Widget', 100, 20)
    
    # Test 2: Update stock
    im.update_stock('SKU001', -30)
    assert im.get_stock('SKU001') == 70
    
    # Test 3: Low stock alert
    im.update_stock('SKU001', -60)
    alerts = im.get_low_stock_alerts()
    assert 'SKU001' in alerts
    
    # Test 4: Generate PO
    po = im.generate_po('SKU001', 100)
    assert po.quantity == 100
    
    print('All tests passed!')

if __name__ == '__main__':
    test_inventory_management()

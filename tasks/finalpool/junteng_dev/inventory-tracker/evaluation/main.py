# Evaluation Script for Inventory Tracker

import sys
sys.path.append('../../groundtruth_workspace')

from inventory_tracker import InventoryTracker

def test_inventory_tracker():
    it = InventoryTracker()
    
    # Test 1: Add location
    it.add_location('WAREHOUSE1')
    it.add_location('WAREHOUSE2')
    
    # Test 2: Add stock
    it.add_stock('WAREHOUSE1', 'SKU001', 100)
    assert it.get_stock('WAREHOUSE1', 'SKU001') == 100
    
    # Test 3: Transfer
    it.transfer('WAREHOUSE1', 'WAREHOUSE2', 'SKU001', 30)
    assert it.get_stock('WAREHOUSE1', 'SKU001') == 70
    assert it.get_stock('WAREHOUSE2', 'SKU001') == 30
    
    # Test 4: Cycle count
    it.record_count('WAREHOUSE1', 'SKU001', 65)  # Discrepancy
    discrepancies = it.get_discrepancies()
    assert 'SKU001' in discrepancies
    
    print('All tests passed!')

if __name__ == '__main__':
    test_inventory_tracker()

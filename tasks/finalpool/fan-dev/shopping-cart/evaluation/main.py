# Evaluation Script for Shopping Cart

import sys
sys.path.append('../../groundtruth_workspace')

from shopping_cart import ShoppingCart

def test_shopping_cart():
    cart = ShoppingCart()
    
    # Test 1: Add items
    cart.add_item('product1', 2, 10.00)
    cart.add_item('product2', 1, 25.00)
    assert cart.get_item_count() == 3
    
    # Test 2: Update quantity
    cart.update_quantity('product1', 3)
    assert cart.get_quantity('product1') == 3
    
    # Test 3: Calculate total
    total = cart.get_total()
    assert total == 55.00  # 3*10 + 1*25
    
    # Test 4: Remove item
    cart.remove_item('product2')
    assert cart.get_item_count() == 3
    
    print('All tests passed!')

if __name__ == '__main__':
    test_shopping_cart()

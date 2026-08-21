# Evaluation Script for Customer Portal

import sys
sys.path.append('../../groundtruth_workspace')

from customer_portal import CustomerPortal

def test_customer_portal():
    cp = CustomerPortal()
    
    # Test 1: Register user
    user_id = cp.register('user1', 'password123', 'user1@example.com')
    
    # Test 2: Login
    token = cp.login('user1', 'password123')
    assert token is not None
    
    # Test 3: View orders
    orders = cp.get_orders(user_id)
    assert isinstance(orders, list)
    
    # Test 4: Create ticket
    ticket_id = cp.create_ticket(user_id, 'Issue with order', 'Details')
    assert ticket_id is not None
    
    # Test 5: Knowledge base
    articles = cp.search_kb('shipping')
    assert isinstance(articles, list)
    
    print('All tests passed!')

if __name__ == '__main__':
    test_customer_portal()

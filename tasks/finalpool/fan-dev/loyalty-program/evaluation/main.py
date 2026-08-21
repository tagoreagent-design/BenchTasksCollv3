# Evaluation Script for Loyalty Program

import sys
sys.path.append('../../groundtruth_workspace')

from loyalty_program import LoyaltyProgram

def test_loyalty_program():
    lp = LoyaltyProgram()
    
    # Test 1: Add customer and earn points
    customer_id = lp.add_customer('user1')
    lp.earn_points(customer_id, 100)
    assert lp.get_points(customer_id) == 100
    
    # Test 2: Tier calculation
    lp.earn_points(customer_id, 500)
    assert lp.get_tier(customer_id) == 'Silver'
    
    # Test 3: Redeem points
    success = lp.redeem_points(customer_id, 200)
    assert success == True
    assert lp.get_points(customer_id) == 400
    
    # Test 4: Insufficient points
    success = lp.redeem_points(customer_id, 1000)
    assert success == False
    
    print('All tests passed!')

if __name__ == '__main__':
    test_loyalty_program()

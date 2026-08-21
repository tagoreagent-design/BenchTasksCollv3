# Evaluation Script for Coupon Manager

import sys
sys.path.append('../../groundtruth_workspace')

from coupon_manager import CouponManager

def test_coupon_manager():
    cm = CouponManager()
    
    # Test 1: Create a percentage coupon
    coupon = cm.create_coupon(
        code='SAVE10',
        discount_type='percentage',
        discount_value=10,
        min_order=50,
        max_uses=100
    )
    assert coupon.code == 'SAVE10'
    assert coupon.discount_type == 'percentage'
    assert coupon.discount_value == 10
    
    # Test 2: Validate coupon
    valid, msg = cm.validate_coupon('SAVE10', 75)
    assert valid == True
    
    # Test 3: Apply coupon
    discount = cm.apply_coupon('SAVE10', 100)
    assert discount == 10
    
    # Test 4: Invalid coupon (below min order)
    valid, msg = cm.validate_coupon('SAVE10', 30)
    assert valid == False
    
    # Test 5: Expired coupon
    cm.create_coupon('OLD', 'percentage', 20, max_uses=0)
    cm.coupons['OLD'].expired = True
    valid, msg = cm.validate_coupon('OLD', 100)
    assert valid == False
    
    print('All tests passed!')

if __name__ == '__main__':
    test_coupon_manager()

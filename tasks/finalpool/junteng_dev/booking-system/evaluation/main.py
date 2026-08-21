# Evaluation Script for Booking System

import sys
sys.path.append('../../groundtruth_workspace')

from booking_system import BookingSystem

def test_booking_system():
    bs = BookingSystem()
    
    # Test 1: Check availability
    slots = bs.get_available_slots('2024-01-15', 'provider1')
    assert len(slots) > 0
    
    # Test 2: Create booking
    booking_id = bs.create_booking('user1', 'provider1', '2024-01-15 10:00')
    assert booking_id is not None
    
    # Test 3: Cancel booking
    result = bs.cancel_booking(booking_id)
    assert result.success
    
    # Test 4: Waitlist
    bs.create_booking('user2', 'provider1', '2024-01-15 10:00')  # Full
    waitlist = bs.join_waitlist('user3', 'provider1', '2024-01-15 10:00')
    assert waitlist.position == 1
    
    print('All tests passed!')

if __name__ == '__main__':
    test_booking_system()

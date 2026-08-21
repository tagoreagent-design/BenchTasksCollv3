# Preprocessing Script for Booking System

import sys
sys.path.append('../../groundtruth_workspace')

from booking_system import BookingSystem

# Preprocess booking request
def preprocess_booking_request(request):
    """Validate and normalize booking request"""
    from datetime import datetime
    
    try:
        dt = datetime.strptime(request['datetime'], '%Y-%m-%d %H:%M')
        return {
            'user_id': str(request['user_id']),
            'provider_id': str(request['provider_id']),
            'datetime': dt,
            'duration': int(request.get('duration', 30))
        }
    except (ValueError, KeyError) as e:
        raise ValueError(f"Invalid booking request: {e}")

if __name__ == '__main__':
    req = {'user_id': 'u1', 'provider_id': 'p1', 'datetime': '2024-01-15 10:00'}
    print(preprocess_booking_request(req))

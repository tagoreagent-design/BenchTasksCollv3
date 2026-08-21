# Preprocessing Script for Customer Portal

import sys
sys.path.append('../../groundtruth_workspace')

from customer_portal import CustomerPortal

# Preprocess user registration
def preprocess_registration(data):
    """Validate and normalize registration data"""
    import re
    
    email = data.get('email', '').strip().lower()
    if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
        raise ValueError('Invalid email')
    
    password = data.get('password', '')
    if len(password) < 8:
        raise ValueError('Password too short')
    
    return {
        'username': data.get('username', '').strip(),
        'email': email,
        'password': password  # Should be hashed in real impl
    }

if __name__ == '__main__':
    print(preprocess_registration({'username': 'user1', 'email': 'USER@EXAMPLE.COM', 'password': 'password123'}))

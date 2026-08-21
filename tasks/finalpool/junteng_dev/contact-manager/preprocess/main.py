# Preprocessing Script for Contact Manager

import sys
sys.path.append('../../groundtruth_workspace')

from contact_manager import ContactManager

# Preprocess contact data
def preprocess_contact(raw_contact):
    """Clean and normalize contact data"""
    import re
    
    email = raw_contact.get('email', '').strip().lower()
    phone = re.sub(r'\D', '', raw_contact.get('phone', ''))
    
    return {
        'name': raw_contact.get('name', '').strip(),
        'email': email if '@' in email else '',
        'phone': phone if len(phone) >= 10 else '',
        'address': raw_contact.get('address', '').strip(),
        'tags': [t.strip().lower() for t in raw_contact.get('tags', [])]
    }

if __name__ == '__main__':
    raw = {'name': '  John  ', 'email': '  JOHN@EXAMPLE.COM  ', 'phone': '(555) 123-4567'}
    print(preprocess_contact(raw))

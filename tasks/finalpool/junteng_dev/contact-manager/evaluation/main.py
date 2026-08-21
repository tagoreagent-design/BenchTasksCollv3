# Evaluation Script for Contact Manager

import sys
sys.path.append('../../groundtruth_workspace')

from contact_manager import ContactManager

def test_contact_manager():
    cm = ContactManager()
    
    # Test 1: Add contact
    contact_id = cm.add_contact('John Doe', 'john@example.com', '555-1234')
    
    # Test 2: Find contact
    contact = cm.find_by_email('john@example.com')
    assert contact.name == 'John Doe'
    
    # Test 3: Deduplicate
    cm.add_contact('John D.', 'john@example.com', '555-5678')  # Duplicate email
    contacts = cm.get_all()
    assert len(contacts) == 1  # Merged
    
    # Test 4: Tags
    cm.add_tag(contact_id, 'vip')
    assert 'vip' in cm.get_tags(contact_id)
    
    # Test 5: Export
    csv_data = cm.export_csv()
    assert 'John Doe' in csv_data
    assert 'john@example.com' in csv_data
    
    print('All tests passed!')

if __name__ == '__main__':
    test_contact_manager()

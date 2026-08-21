# Evaluation Script for Calendar Sync

import sys
sys.path.append('../../groundtruth_workspace')

from calendar_sync import CalendarSync

def test_calendar_sync():
    cs = CalendarSync()
    
    # Test 1: Connect calendars
    cs.connect('google', 'token1')
    cs.connect('outlook', 'token2')
    
    # Test 2: Create event in Google
    event_id = cs.create_event('google', 'Meeting', '2024-01-15 10:00', '2024-01-15 11:00')
    
    # Test 3: Sync to Outlook
    cs.sync()
    outlook_events = cs.get_events('outlook', '2024-01-15')
    assert any(e['title'] == 'Meeting' for e in outlook_events)
    
    # Test 4: Conflict detection
    cs.create_event('outlook', 'Conflict', '2024-01-15 10:30', '2024-01-15 11:30')
    conflicts = cs.detect_conflicts()
    assert len(conflicts) > 0
    
    print('All tests passed!')

if __name__ == '__main__':
    test_calendar_sync()

# Preprocessing Script for Calendar Sync

import sys
sys.path.append('../../groundtruth_workspace')

from calendar_sync import CalendarSync

# Preprocess calendar event
def preprocess_event(event_data):
    """Normalize event data for sync"""
    from datetime import datetime
    
    return {
        'title': str(event_data.get('title', '')).strip(),
        'start': datetime.fromisoformat(event_data['start']) if 'start' in event_data else None,
        'end': datetime.fromisoformat(event_data['end']) if 'end' in event_data else None,
        'description': str(event_data.get('description', '')).strip(),
        'location': str(event_data.get('location', '')).strip(),
        'recurring': event_data.get('recurring', False),
        'timezone': event_data.get('timezone', 'UTC')
    }

if __name__ == '__main__':
    event = {'title': 'Meeting', 'start': '2024-01-15T10:00:00', 'end': '2024-01-15T11:00:00'}
    print(preprocess_event(event))

# Preprocessing Script for Help Desk

import sys
sys.path.append('../../groundtruth_workspace')

from help_desk import HelpDesk

# Preprocess ticket data
def preprocess_ticket(raw_ticket):
    """Clean and normalize ticket data"""
    return {
        'title': raw_ticket.get('title', '').strip()[:200],
        'description': raw_ticket.get('description', '').strip(),
        'category': raw_ticket.get('category', 'general').lower(),
        'priority': raw_ticket.get('priority', 'medium').lower(),
        'user_id': str(raw_ticket.get('user_id', '')),
        'channel': raw_ticket.get('channel', 'web')
    }

if __name__ == '__main__':
    raw = {'title': '  Login Issue  ', 'description': 'Cannot login', 'category': 'TECHNICAL'}
    print(preprocess_ticket(raw))

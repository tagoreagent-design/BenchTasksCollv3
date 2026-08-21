# Evaluation Script for Help Desk

import sys
sys.path.append('../../groundtruth_workspace')

from help_desk import HelpDesk

def test_help_desk():
    hd = HelpDesk()
    
    # Test 1: Create ticket
    ticket_id = hd.create_ticket('user1', 'Login issue', 'Cannot login', 'technical')
    
    # Test 2: Auto-route
    agent = hd.route_ticket(ticket_id)
    assert agent is not None
    
    # Test 3: SLA
    hd.set_sla('technical', hours=4)
    sla = hd.get_sla_status(ticket_id)
    assert sla['remaining_hours'] <= 4
    
    # Test 4: Respond
    hd.respond(ticket_id, agent, 'Reset your password')
    
    # Test 5: Close
    hd.close_ticket(ticket_id, agent, 'Resolved')
    
    print('All tests passed!')

if __name__ == '__main__':
    test_help_desk()

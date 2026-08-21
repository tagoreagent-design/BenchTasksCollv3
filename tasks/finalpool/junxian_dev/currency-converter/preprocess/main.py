# Preprocessing Script for Currency Converter

import sys
sys.path.append('../../groundtruth_workspace')

from currency_converter import CurrencyConverter

# Preprocess conversion request
def preprocess_conversion(request):
    """Validate and normalize conversion request"""
    amount = float(request.get('amount', 0))
    from_curr = request.get('from', '').upper()
    to_curr = request.get('to', '').upper()
    
    if amount <= 0:
        raise ValueError('Amount must be positive')
    if len(from_curr) != 3 or len(to_curr) != 3:
        raise ValueError('Currency codes must be 3 letters')
    
    return {
        'amount': amount,
        'from': from_curr,
        'to': to_curr,
        'date': request.get('date')
    }

if __name__ == '__main__':
    print(preprocess_conversion({'amount': '100', 'from': 'usd', 'to': 'eur'}))

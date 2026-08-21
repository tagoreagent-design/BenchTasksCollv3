# Evaluation Script for Currency Converter

import sys
sys.path.append('../../groundtruth_workspace')

from currency_converter import CurrencyConverter

def test_currency_converter():
    cc = CurrencyConverter()
    
    # Test 1: Convert USD to EUR
    result = cc.convert(100, 'USD', 'EUR')
    assert result.amount > 0
    assert result.to_currency == 'EUR'
    
    # Test 2: Historical rate
    rate = cc.get_rate('USD', 'EUR', '2024-01-15')
    assert rate > 0
    
    # Test 3: Batch convert
    results = cc.batch_convert([
        {'amount': 100, 'from': 'USD', 'to': 'EUR'},
        {'amount': 50, 'from': 'GBP', 'to': 'USD'},
    ])
    assert len(results) == 2
    
    # Test 4: Crypto
    btc_usd = cc.convert(1, 'BTC', 'USD')
    assert btc_usd.amount > 10000
    
    print('All tests passed!')

if __name__ == '__main__':
    test_currency_converter()

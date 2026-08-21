# Preprocessing Script for Monthly Sales Analysis

import sys
sys.path.append('../../groundtruth_workspace')

from monthly_sales_analysis import MonthlySalesAnalysis

# Preprocess sales data
def preprocess_sales(raw_data):
    """Clean and normalize sales data"""
    from datetime import datetime
    
    processed = []
    for record in raw_data:
        try:
            date = datetime.strptime(record['date'], '%Y-%m-%d')
            amount = float(record['amount'])
            product = str(record['product']).strip()
            
            if amount > 0 and product:
                processed.append({
                    'date': date,
                    'product': product,
                    'amount': amount
                })
        except (ValueError, KeyError):
            continue
    return processed

if __name__ == '__main__':
    raw = [
        {'date': '2024-01-15', 'product': 'A', 'amount': '1000'},
        {'date': 'invalid', 'product': 'B', 'amount': '500'},
    ]
    print(preprocess_sales(raw))

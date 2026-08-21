# Evaluation Script for Monthly Sales Analysis

import sys
sys.path.append('../../groundtruth_workspace')

from monthly_sales_analysis import MonthlySalesAnalysis

def test_monthly_sales_analysis():
    msa = MonthlySalesAnalysis()
    
    # Test 1: Import data
    msa.import_data([
        {'date': '2024-01-15', 'product': 'A', 'amount': 1000},
        {'date': '2024-02-20', 'product': 'A', 'amount': 1200},
        {'date': '2024-01-10', 'product': 'B', 'amount': 500},
    ])
    
    # Test 2: Monthly totals
    totals = msa.get_monthly_totals()
    assert totals['2024-01'] == 1500
    assert totals['2024-02'] == 1200
    
    # Test 3: MoM growth
    growth = msa.get_mom_growth('2024-02')
    assert growth > 0  # Feb > Jan for product A
    
    # Test 4: Top products
    top = msa.get_top_products(limit=1)
    assert top[0]['product'] == 'A'
    
    # Test 5: Forecast
    forecast = msa.forecast_next_month()
    assert 'predicted' in forecast
    
    print('All tests passed!')

if __name__ == '__main__':
    test_monthly_sales_analysis()

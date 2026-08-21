# Evaluation Script for Product Comparator

import sys
sys.path.append('../../groundtruth_workspace')

from product_comparator import ProductComparator

def test_product_comparator():
    pc = ProductComparator()
    
    # Test 1: Add products
    pc.add_product('Laptop A', {'cpu': 'i7', 'ram': '16GB', 'price': 1200})
    pc.add_product('Laptop B', {'cpu': 'i5', 'ram': '8GB', 'price': 900})
    
    # Test 2: Compare
    comparison = pc.compare(['Laptop A', 'Laptop B'])
    assert 'cpu' in comparison.differences
    assert comparison.differences['cpu'] == ['i7', 'i5']
    
    # Test 3: Best value
    best = pc.best_value(['Laptop A', 'Laptop B'])
    # Laptop B is cheaper per GB RAM
    
    print('All tests passed!')

if __name__ == '__main__':
    test_product_comparator()

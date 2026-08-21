# Evaluation Script for Product Catalog

import sys
sys.path.append('../../groundtruth_workspace')

from product_catalog import ProductCatalog

def test_product_catalog():
    pc = ProductCatalog()
    
    # Test 1: Create product
    product_id = pc.create_product('T-Shirt', 'Apparel', {'brand': 'Nike'})
    
    # Test 2: Add variants
    pc.add_variant(product_id, 'Red', 'M', {'sku': 'TS-R-M', 'price': 29.99})
    pc.add_variant(product_id, 'Blue', 'L', {'sku': 'TS-B-L', 'price': 29.99})
    
    # Test 3: Get variants
    variants = pc.get_variants(product_id)
    assert len(variants) == 2
    
    # Test 4: Category
    pc.add_to_category(product_id, 'Summer Sale')
    
    # Test 5: Publish
    result = pc.publish(product_id, 'webstore')
    assert result.success
    
    print('All tests passed!')

if __name__ == '__main__':
    test_product_catalog()

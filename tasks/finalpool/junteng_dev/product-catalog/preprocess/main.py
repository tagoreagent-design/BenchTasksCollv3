# Preprocessing Script for Product Catalog

import sys
sys.path.append('../../groundtruth_workspace')

from product_catalog import ProductCatalog

# Preprocess product data
def preprocess_product(raw_product):
    """Clean and normalize product data"""
    return {
        'name': raw_product.get('name', '').strip(),
        'description': raw_product.get('description', '').strip(),
        'category': raw_product.get('category', '').strip(),
        'attributes': {k: str(v).strip() for k, v in raw_product.get('attributes', {}).items()},
        'base_price': float(raw_product.get('base_price', 0))
    }

if __name__ == '__main__':
    raw = {'name': '  T-Shirt  ', 'description': 'Cotton tee', 'category': 'Apparel', 'attributes': {'brand': '  Nike  '}, 'base_price': '29.99'}
    print(preprocess_product(raw))

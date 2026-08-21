# Evaluation Script for SEO Optimizer

import sys
sys.path.append('../../groundtruth_workspace')

from seo_optimizer import SEOOptimizer

def test_seo_optimizer():
    seo = SEOOptimizer()
    
    # Test 1: Analyze content
    html = """<html><head><title>Test Page - Best Product</title><meta name='description' content='Buy the best product online'></head><body><h1>Best Product</h1><p>This is the best product you can buy.</p><img src='product.jpg'></body></html>"""
    result = seo.analyze(html)
    
    # Test 2: Check results
    assert 'title' in result.issues
    assert 'meta_description' in result.issues
    assert 'h1_count' in result.metrics
    assert result.metrics['h1_count'] == 1
    
    # Test 3: Keyword analysis
    keywords = seo.extract_keywords(html)
    assert 'best' in keywords
    assert 'product' in keywords
    
    # Test 4: Score
    assert 0 <= result.score <= 100
    
    print('All tests passed!')

if __name__ == '__main__':
    test_seo_optimizer()

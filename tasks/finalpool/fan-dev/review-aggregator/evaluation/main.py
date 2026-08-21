# Evaluation Script for Review Aggregator

import sys
sys.path.append('../../groundtruth_workspace')

from review_aggregator import ReviewAggregator

def test_review_aggregator():
    ra = ReviewAggregator()
    
    # Test 1: Add reviews
    ra.add_review('product1', {'rating': 5, 'text': 'Great!', 'source': 'Amazon', 'verified': True})
    ra.add_review('product1', {'rating': 4, 'text': 'Good', 'source': 'BestBuy', 'verified': True})
    ra.add_review('product1', {'rating': 1, 'text': 'Bad', 'source': 'Amazon', 'verified': False})
    
    # Test 2: Get average
    avg = ra.get_average_rating('product1')
    assert avg > 4.0  # Weighted toward verified
    
    # Test 3: Sentiment
    sentiment = ra.get_sentiment('product1')
    assert sentiment == 'positive'
    
    # Test 4: Themes
    themes = ra.get_themes('product1')
    assert 'great' in themes or 'good' in themes
    
    print('All tests passed!')

if __name__ == '__main__':
    test_review_aggregator()

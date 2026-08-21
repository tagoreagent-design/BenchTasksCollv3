# Preprocessing Script for Review Aggregator

import sys
sys.path.append('../../groundtruth_workspace')

from review_aggregator import ReviewAggregator

# Preprocess raw review data
def preprocess_reviews(raw_data):
    """Clean and normalize review data"""
    processed = []
    for review in raw_data:
        # Normalize rating
        rating = max(1, min(5, int(review.get('rating', 3))))
        
        # Clean text
        text = review.get('text', '').strip()
        if len(text) < 10:
            continue  # Skip too short reviews
        
        processed.append({
            'rating': rating,
            'text': text,
            'source': review.get('source', 'unknown'),
            'verified': review.get('verified', False),
            'date': review.get('date', '2024-01-01')
        })
    return processed

if __name__ == '__main__':
    # Example usage
    raw = [
        {'rating': 5, 'text': 'Excellent product!', 'source': 'Amazon', 'verified': True},
        {'rating': 1, 'text': 'Bad', 'source': 'Amazon', 'verified': False},
    ]
    print(preprocess_reviews(raw))

# Evaluation Script for Customer Feedback Processor

import sys
sys.path.append('../../groundtruth_workspace')

from customer_feedback_processor import CustomerFeedbackProcessor

def test_customer_feedback_processor():
    cfp = CustomerFeedbackProcessor()
    
    # Test 1: Process feedback
    cfp.add_feedback('Great feature!', 'email')
    cfp.add_feedback('App crashes on login', 'support')
    cfp.add_feedback('UI is confusing', 'survey')
    
    # Test 2: Categorize
    categories = cfp.categorize()
    assert 'feature' in categories
    assert 'bug' in categories
    assert 'usability' in categories
    
    # Test 3: Sentiment
    sentiments = cfp.analyze_sentiment()
    assert sentiments['positive'] >= 1
    assert sentiments['negative'] >= 2
    
    # Test 4: Themes
    themes = cfp.extract_themes()
    assert 'login' in themes or 'crash' in themes
    
    print('All tests passed!')

if __name__ == '__main__':
    test_customer_feedback_processor()

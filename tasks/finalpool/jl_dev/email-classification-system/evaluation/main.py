# Evaluation Script for Email Classification System

import sys
sys.path.append('../../groundtruth_workspace')

from email_classification_system import EmailClassificationSystem

def test_email_classification():
    ecs = EmailClassificationSystem()
    
    # Test 1: Classify spam
    result = ecs.classify('Buy cheap meds now!!!', {})
    assert result.category == 'spam'
    assert result.confidence > 0.8
    
    # Test 2: Classify promotional
    result = ecs.classify('50% off sale ends today!', {})
    assert result.category == 'promotional'
    
    # Test 3: Classify primary
    result = ecs.classify('Meeting tomorrow at 10am', {})
    assert result.category == 'primary'
    
    # Test 4: Train custom
    ecs.train_custom([('Project update', 'work'), ('Team lunch', 'social')])
    
    print('All tests passed!')

if __name__ == '__main__':
    test_email_classification()

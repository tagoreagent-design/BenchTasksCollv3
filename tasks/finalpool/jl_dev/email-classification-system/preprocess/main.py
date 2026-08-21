# Preprocessing Script for Email Classification

import sys
sys.path.append('../../groundtruth_workspace')

from email_classification_system import EmailClassificationSystem

# Preprocess email content
def preprocess_email(email_data):
    """Clean and normalize email for classification"""
    import re
    
    subject = email_data.get('subject', '')
    body = email_data.get('body', '')
    
    # Combine subject and body
    text = f"{subject} {body}"
    
    # Clean
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = text.strip().lower()
    
    return {
        'text': text,
        'sender': email_data.get('sender', ''),
        'headers': email_data.get('headers', {})
    }

if __name__ == '__main__':
    email = {'subject': 'Sale!', 'body': 'Check out our sale http://example.com'}
    print(preprocess_email(email))

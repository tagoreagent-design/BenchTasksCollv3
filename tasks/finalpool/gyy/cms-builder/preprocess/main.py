# Preprocessing Script for CMS Builder

import sys
sys.path.append('../../groundtruth_workspace')

from cms_builder import CMSBuilder

# Preprocess CMS data
def preprocess_content_type(raw_type):
    """Normalize content type definition"""
    return {
        'name': raw_type.get('name', '').lower().strip(),
        'fields': {k: v.lower() for k, v in raw_type.get('fields', {}).items()},
        'description': raw_type.get('description', '')
    }

if __name__ == '__main__':
    raw = {'name': 'Article', 'fields': {'Title': 'Text', 'Body': 'RichText'}}
    print(preprocess_content_type(raw))

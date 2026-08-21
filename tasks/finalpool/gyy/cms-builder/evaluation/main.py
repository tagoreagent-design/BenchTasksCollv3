# Evaluation Script for CMS Builder

import sys
sys.path.append('../../groundtruth_workspace')

from cms_builder import CMSBuilder

def test_cms_builder():
    cms = CMSBuilder()
    
    # Test 1: Define content type
    cms.define_content_type('article', {
        'title': 'text',
        'body': 'richtext',
        'author': 'reference'
    })
    
    # Test 2: Create page
    page_id = cms.create_page('article', {'title': 'Test', 'body': 'Content'})
    page = cms.get_page(page_id)
    assert page.content_type == 'article'
    
    # Test 3: Navigation
    cms.add_to_menu(page_id, 'Blog')
    menu = cms.get_menu()
    assert any(item['page_id'] == page_id for item in menu)
    
    # Test 4: Versioning
    cms.update_page(page_id, {'body': 'Updated'})
    versions = cms.get_versions(page_id)
    assert len(versions) == 2
    
    print('All tests passed!')

if __name__ == '__main__':
    test_cms_builder()

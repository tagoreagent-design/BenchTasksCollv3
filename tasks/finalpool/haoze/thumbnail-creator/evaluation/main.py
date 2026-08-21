# Evaluation Script for Thumbnail Creator

import sys
sys.path.append('../../groundtruth_workspace')

from thumbnail_creator import ThumbnailCreator

def test_thumbnail_creator():
    tc = ThumbnailCreator()
    
    # Test 1: Create from template
    thumb = tc.create_from_template('youtube', {'title': 'My Video', 'image': 'bg.jpg'})
    assert thumb.width == 1280
    assert thumb.height == 720
    
    # Test 2: Add text
    tc.add_text(thumb, 'Amazing Video!', font_size=48, color='white')
    
    # Test 3: Add branding
    tc.add_logo(thumb, 'logo.png', position='bottom-right')
    
    # Test 4: Export
    output = tc.export(thumb, 'thumbnail.jpg', quality=95)
    assert output.format == 'jpeg'
    
    # Test 5: Generate variants
    variants = tc.generate_variants(thumb, count=3)
    assert len(variants) == 3
    
    print('All tests passed!')

if __name__ == '__main__':
    test_thumbnail_creator()

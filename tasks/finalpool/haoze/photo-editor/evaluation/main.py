# Evaluation Script for Photo Editor

import sys
sys.path.append('../../groundtruth_workspace')

from photo_editor import PhotoEditor

def test_photo_editor():
    pe = PhotoEditor()
    
    # Test 1: Load image
    pe.load('input.jpg')
    
    # Test 2: Apply filter
    pe.apply_filter('vintage')
    assert pe.current_filter == 'vintage'
    
    # Test 3: Adjust
    pe.adjust(brightness=1.2, contrast=1.1)
    
    # Test 4: Crop
    pe.crop(100, 100, 500, 500)
    
    # Test 5: Save
    output = pe.save('output.jpg', quality=90)
    assert output.format == 'jpeg'
    
    print('All tests passed!')

if __name__ == '__main__':
    test_photo_editor()

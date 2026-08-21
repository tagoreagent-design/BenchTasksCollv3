# Evaluation Script for Media Organizer

import sys
sys.path.append('../../groundtruth_workspace')

from media_organizer import MediaOrganizer

def test_media_organizer():
    mo = MediaOrganizer()
    
    # Test 1: Organize by type
    mo.organize('/media', by='type')
    assert os.path.exists('/media/audio')
    assert os.path.exists('/media/video')
    assert os.path.exists('/media/images')
    
    # Test 2: Rename pattern
    mo.rename_pattern('{artist} - {title}.{ext}')
    
    # Test 3: Find duplicates
    dupes = mo.find_duplicates('/media')
    assert isinstance(dupes, list)
    
    # Test 4: Backup
    backup_path = mo.create_backup('/media')
    assert os.path.exists(backup_path)
    
    print('All tests passed!')

if __name__ == '__main__':
    test_media_organizer()

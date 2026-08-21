# Preprocessing Script for Media Organizer

import sys
sys.path.append('../../groundtruth_workspace')

from media_organizer import MediaOrganizer

# Preprocess media files
def preprocess_media(file_path):
    """Extract and normalize media metadata"""
    import os
    from pathlib import Path
    
    path = Path(file_path)
    ext = path.suffix.lower()
    
    media_type = 'unknown'
    if ext in ['.mp3', '.wav', '.flac', '.aac', '.ogg']:
        media_type = 'audio'
    elif ext in ['.mp4', '.mkv', '.avi', '.mov', '.webm']:
        media_type = 'video'
    elif ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp']:
        media_type = 'image'
    
    return {
        'path': str(path),
        'name': path.name,
        'type': media_type,
        'size': path.stat().st_size if path.exists() else 0
    }

if __name__ == '__main__':
    print(preprocess_media('test.mp3'))

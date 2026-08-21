# Preprocessing Script for Photo Editor

import sys
sys.path.append('../../groundtruth_workspace')

from photo_editor import PhotoEditor

# Preprocess image
def preprocess_image(file_path):
    """Load and validate image file"""
    import os
    from pathlib import Path
    
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Image not found: {file_path}")
    
    ext = path.suffix.lower()
    supported = ['.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff']
    if ext not in supported:
        raise ValueError(f"Unsupported image format: {ext}")
    
    return {
        'path': str(path),
        'format': ext[1:],
        'size': path.stat().st_size
    }

if __name__ == '__main__':
    print(preprocess_image('test.jpg'))

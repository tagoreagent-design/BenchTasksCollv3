# Preprocessing Script for Thumbnail Creator

import sys
sys.path.append('../../groundtruth_workspace')

from thumbnail_creator import ThumbnailCreator

# Preprocess thumbnail assets
def preprocess_assets(template, assets):
    """Validate and prepare assets for thumbnail creation"""
    validated = {}
    for key, asset in assets.items():
        if isinstance(asset, str) and asset.endswith(('.jpg', '.png', '.webp')):
            # It's an image path
            validated[key] = {'type': 'image', 'path': asset}
        elif isinstance(asset, str):
            # It's text
            validated[key] = {'type': 'text', 'content': asset}
        else:
            validated[key] = asset
    return validated

if __name__ == '__main__':
    assets = {'title': 'My Video', 'background': 'bg.jpg', 'logo': 'logo.png'}
    print(preprocess_assets('youtube', assets))

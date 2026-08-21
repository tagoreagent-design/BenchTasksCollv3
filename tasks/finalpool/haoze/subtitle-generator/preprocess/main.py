# Preprocessing Script for Subtitle Generator

import sys
sys.path.append('../../groundtruth_workspace')

from subtitle_generator import SubtitleGenerator

# Preprocess audio for transcription
def preprocess_audio(file_path):
    """Validate and prepare audio for transcription"""
    import os
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Audio not found: {file_path}")
    
    ext = path.suffix.lower()
    supported = ['.wav', '.mp3', '.flac', '.m4a', '.ogg']
    if ext not in supported:
        raise ValueError(f"Unsupported audio format: {ext}")
    
    return {'path': str(path), 'format': ext[1:], 'duration': 0}

if __name__ == '__main__':
    print(preprocess_audio('test.wav'))

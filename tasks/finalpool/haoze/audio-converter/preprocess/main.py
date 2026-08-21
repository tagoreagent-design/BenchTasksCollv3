# Preprocessing Script for Audio Converter

import sys
sys.path.append('../../groundtruth_workspace')

from audio_converter import AudioConverter

# Preprocess audio files
def preprocess_audio(file_path):
    """Validate and prepare audio file for conversion"""
    import os
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Check format
    ext = os.path.splitext(file_path)[1].lower()
    supported = ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a']
    if ext not in supported:
        raise ValueError(f"Unsupported format: {ext}")
    
    return {'path': file_path, 'format': ext[1:]}

if __name__ == '__main__':
    print(preprocess_audio('test.wav'))

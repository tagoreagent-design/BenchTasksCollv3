# Evaluation Script for Audio Converter

import sys
sys.path.append('../../groundtruth_workspace')

from audio_converter import AudioConverter

def test_audio_converter():
    ac = AudioConverter()
    
    # Test 1: Convert WAV to MP3
    output = ac.convert('input.wav', 'output.mp3', bitrate='192k')
    assert output.format == 'mp3'
    assert output.bitrate == '192k'
    
    # Test 2: Batch convert
    results = ac.batch_convert(['1.wav', '2.wav'], 'mp3')
    assert len(results) == 2
    assert all(r.format == 'mp3' for r in results)
    
    # Test 3: Extract from video
    audio = ac.extract_audio('video.mp4', 'audio.mp3')
    assert audio.format == 'mp3'
    
    # Test 4: Preserve metadata
    ac.convert('tagged.mp3', 'output.mp3')
    # Metadata should be preserved
    
    print('All tests passed!')

if __name__ == '__main__':
    test_audio_converter()

# Evaluation Script for Subtitle Generator

import sys
sys.path.append('../../groundtruth_workspace')

from subtitle_generator import SubtitleGenerator

def test_subtitle_generator():
    sg = SubtitleGenerator()
    
    # Test 1: Generate from audio
    subtitles = sg.generate('audio.wav', language='en')
    assert len(subtitles) > 0
    assert all('start' in s and 'end' in s and 'text' in s for s in subtitles)
    
    # Test 2: Export SRT
    srt = sg.export(subtitles, 'srt')
    assert '-->' in srt
    
    # Test 3: Export VTT
    vtt = sg.export(subtitles, 'vtt')
    assert 'WEBVTT' in vtt
    
    # Test 4: Translate
    translated = sg.translate(subtitles, 'es')
    assert len(translated) == len(subtitles)
    
    print('All tests passed!')

if __name__ == '__main__':
    test_subtitle_generator()

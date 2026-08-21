# Evaluation Script for QR Generator

import sys
sys.path.append('../../groundtruth_workspace')

from qr_generator import QRGenerator

def test_qr_generator():
    qr = QRGenerator()
    
    # Test 1: URL QR
    img = qr.generate('https://example.com', 'url')
    assert img is not None
    
    # Test 2: vCard QR
    vcard = qr.generate({'name': 'John', 'phone': '555-1234', 'email': 'john@example.com'}, 'vcard')
    assert vcard is not None
    
    # Test 3: WiFi QR
    wifi = qr.generate({'ssid': 'MyWiFi', 'password': 'secret', 'encryption': 'WPA'}, 'wifi')
    assert wifi is not None
    
    # Test 4: Custom colors
    colored = qr.generate('test', 'url', fg_color='#FF0000', bg_color='#FFFFFF')
    assert colored is not None
    
    # Test 5: With logo
    with_logo = qr.generate('test', 'url', logo_path='logo.png')
    assert with_logo is not None
    
    print('All tests passed!')

if __name__ == '__main__':
    test_qr_generator()

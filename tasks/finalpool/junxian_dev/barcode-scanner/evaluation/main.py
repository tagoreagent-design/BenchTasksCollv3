# Evaluation Script for Barcode Scanner

import sys
sys.path.append('../../groundtruth_workspace')

from barcode_scanner import BarcodeScanner

def test_barcode_scanner():
    bs = BarcodeScanner()
    
    # Test 1: Generate
    barcode_img = bs.generate('1234567890128', 'ean13')
    assert barcode_img is not None
    
    # Test 2: Scan
    result = bs.scan(barcode_img)
    assert result.data == '1234567890128'
    assert result.format == 'ean13'
    
    # Test 3: QR Code
    qr_img = bs.generate('https://example.com', 'qrcode')
    result = bs.scan(qr_img)
    assert result.data == 'https://example.com'
    
    # Test 4: Batch
    results = bs.batch_scan([barcode_img, qr_img])
    assert len(results) == 2
    
    print('All tests passed!')

if __name__ == '__main__':
    test_barcode_scanner()

# Preprocessing Script for QR Generator

import sys
sys.path.append('../../groundtruth_workspace')

from qr_generator import QRGenerator

# Preprocess QR data
def preprocess_qr_data(data, qr_type):
    """Validate and normalize QR data"""
    if qr_type == 'url':
        if not data.startswith(('http://', 'https://')):
            data = 'https://' + data
    elif qr_type == 'vcard':
        required = ['name', 'phone', 'email']
        for field in required:
            if field not in data:
                raise ValueError(f"Missing vCard field: {field}")
    elif qr_type == 'wifi':
        required = ['ssid', 'password', 'encryption']
        for field in required:
            if field not in data:
                raise ValueError(f"Missing WiFi field: {field}")
    return {'data': data, 'type': qr_type}

if __name__ == '__main__':
    print(preprocess_qr_data('example.com', 'url'))

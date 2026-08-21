# Preprocessing Script for PDF Report Generator

import sys
sys.path.append('../../groundtruth_workspace')

from pdf_report_generator import PDFReportGenerator

# Preprocess report data
def preprocess_report_data(raw_data):
    """Normalize data for report generation"""
    processed = {}
    for key, value in raw_data.items():
        if isinstance(value, (list, dict)):
            processed[key] = value
        elif isinstance(value, (int, float)):
            processed[key] = round(value, 2)
        else:
            processed[key] = str(value)
    return processed

if __name__ == '__main__':
    raw = {'total': 10000.123, 'items': [{'name': 'A', 'qty': 10}]}
    print(preprocess_report_data(raw))

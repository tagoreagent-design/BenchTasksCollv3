# Evaluation Script for PDF Report Generator

import sys
sys.path.append('../../groundtruth_workspace')

from pdf_report_generator import PDFReportGenerator

def test_pdf_report_generator():
    prg = PDFReportGenerator()
    
    # Test 1: Create template
    template_id = prg.create_template('sales', {
        'title': 'Monthly Sales Report',
        'sections': ['summary', 'details', 'charts']
    })
    
    # Test 2: Generate report
    data = {'summary': {'total': 10000}, 'details': []}
    pdf_path = prg.generate(template_id, data, 'report.pdf')
    
    # Test 3: Verify PDF
    import os
    assert os.path.exists(pdf_path)
    assert os.path.getsize(pdf_path) > 0
    
    # Test 4: Add chart
    prg.add_chart(template_id, 'bar', {'labels': ['Jan', 'Feb'], 'values': [100, 200]})
    
    print('All tests passed!')

if __name__ == '__main__':
    test_pdf_report_generator()

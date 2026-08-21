# Evaluation Script for Canvas Grade Automation

import sys
sys.path.append('../../groundtruth_workspace')

from canvas_grade_automation import CanvasGradeAutomation

def test_canvas_grade_automation():
    cga = CanvasGradeAutomation()
    
    # Test 1: Connect
    cga.connect('https://canvas.example.com', 'token')
    
    # Test 2: Create rubric
    rubric_id = cga.create_rubric('Essay', [
        {'criterion': 'Content', 'points': 40},
        {'criterion': 'Structure', 'points': 30},
        {'criterion': 'Grammar', 'points': 30}
    ])
    
    # Test 3: Configure assignment
    cga.configure_assignment('assignment1', rubric_id, auto_grade=True)
    
    # Test 4: Grade submissions
    grades = cga.grade_submissions('assignment1')
    assert len(grades) > 0
    
    # Test 5: Sync to Canvas
    result = cga.sync_grades('assignment1')
    assert result.success
    
    print('All tests passed!')

if __name__ == '__main__':
    test_canvas_grade_automation()

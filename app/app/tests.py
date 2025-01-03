"""
Simple tests
"""
from django.test import SimpleTestCase


from app import calc

class CalcTests(SimpleTestCase):
    "Test the class modeul"
    
    def test_add_numbers(self):
        res = calc.add(5, 3)
        
        self.assertEqual(res, 9)
        
import condition_parser as cp
import unittest

# RUN with: python -m unittest test_condition_parser.py

class TestParseCondition(unittest.TestCase):
    def test_is_valid_data(self):
        self.assertEqual(cp.is_valid_data("B04<=0 || B02<=1"), True)
        self.assertEqual(cp.is_valid_data("B06<8"), True)
        self.assertEqual(cp.is_valid_data("B06==8"), True)
        self.assertEqual(cp.is_valid_data("B06!=8 && B04>=3"), True) 
        self.assertEqual(cp.is_valid_data("PCR08>=2 && ( B04>3 || B06<=8 )"), True)
        self.assertEqual(cp.is_valid_data("PFA34>=2 && ( B04>=3 && B06>8 )"), True) 
    
    def test_is_valid_data_invalid(self):
        self.assertEqual(cp.is_valid_data("B06< 8"), False)
        self.assertEqual(cp.is_valid_data("B06"), False)
        self.assertEqual(cp.is_valid_data("B06 && B04>=3"), False) 
        self.assertEqual(cp.is_valid_data("PCR08>=2 && B04>3 || B06<=8 )"), False)
        self.assertEqual(cp.is_valid_data("1:"), False) 
        self.assertEqual(cp.is_valid_data(""), False)
        self.assertEqual(cp.is_valid_data(">="), False)
        self.assertEqual(cp.is_valid_data("B06>7 && B04>=3 ;"), False) 
        self.assertEqual(cp.is_valid_data("PCR08>=2 && ( B04>3 || B06<=8 ) ; B06"), False)
        self.assertEqual(cp.is_valid_data("PFA34>=2 && ( B04>=3 && B06>8"), False) 

    def test_simple_conditions(self):
        input_data = [
            "B04<=0 || B02<=1",
            "B06<8",
            "B06==8",
            "B06==8 && B04>=3",
        ]
        answers = {
            "B02": {"value": "1"},
            "B04": {"value": "1,2"},
            "B06": {"value": "8"},
            "PCR08": {"value": "4,Custom"},
            "PFA34": {"value": "2,Custom"}
        }
        self.assertEqual(cp.parse_condition(input_data[0], answers), True)
        self.assertEqual(cp.parse_condition(input_data[1], answers), False)
        self.assertEqual(cp.parse_condition(input_data[2], answers), True)
        self.assertEqual(cp.parse_condition(input_data[3], answers), False)

    def test_complex_conditions(self):
        input_data = [
            "PCR08>=2 && ( B04>3 || B06<=8 )",
            "PFA34>=2 && ( B04>=3 && B06>8 )"
        ]
        answers = {
            "B04": {"value": "1,2"},
            "B06": {"value": "8"},
            "PCR08": {"value": "4,Custom"},
            "PFA34": {"value": "2,Custom"}
        }
        self.assertEqual(cp.parse_condition(input_data[0], answers), True)
        self.assertEqual(cp.parse_condition(input_data[1], answers), False)

if __name__ == "__main__":
    unittest.main()
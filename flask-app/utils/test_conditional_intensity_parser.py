import conditional_intensity_parser as cip
import unittest


# RUN with: python -m unittest test_conditional_intensity_parser.py

class TestParseConditionnalIntensity(unittest.TestCase):
    def test_is_valid_data(self):
        input_data = [
            {"intensity": 2, "conditional_intensity": "1: B04<=0 ; 4: B02<=1"},
            {"intensity": 1, "conditional_intensity": "3: B06<8"},
            {"intensity": 1, "conditional_intensity": "3: B06==8"},
            {"intensity": 2, "conditional_intensity": "4: B06!=8 && B04>=3"},
            {"intensity": 1, "conditional_intensity": "3: PCR08>=2 && ( B04>3 || B06<=8 )"},
            {"intensity": 1, "conditional_intensity": "3: PFA34>=2 && ( B04>=3 && B06>8 )"}
        ]
        self.assertEqual(cip.is_valid_data(input_data[0]), True)
        self.assertEqual(cip.is_valid_data(input_data[1]), True)
        self.assertEqual(cip.is_valid_data(input_data[2]), True)
        self.assertEqual(cip.is_valid_data(input_data[3]), True) 
        self.assertEqual(cip.is_valid_data(input_data[4]), True)
        self.assertEqual(cip.is_valid_data(input_data[5]), True) 
    
    def test_is_valid_data_invalid(self):
        input_data = [
            {"intensity": 2, "conditional_intensity": "1:B04<=0 ; 4: B02<=1"},
            {"intensity": 1, "conditional_intensity": "3: B06< 8"},
            {"intensity": 1, "conditional_intensity": "3: B06"},
            {"intensity": 2, "conditional_intensity": "4: B06 && B04>=3"},
            {"intensity": 1, "conditional_intensity": "3: PCR08>=2 && B04>3 || B06<=8 )"},
            {"intensity": 1, "conditional_intensity": "3: PFA34>=2 && ( B04>=3 && B06>8"},
            {"intensity": 2, "conditional_intensity": "1:"},
            {"intensity": 1, "conditional_intensity": ""},
            {"intensity": 1, "conditional_intensity": "3: >="},
            {"intensity": 2, "conditional_intensity": "4: B06>7 && B04>=3 ;"},
            {"intensity": 1, "conditional_intensity": "3: PCR08>=2 && ( B04>3 || B06<=8 ) ; B06"},
        ]
        self.assertEqual(cip.is_valid_data(input_data[0]), False)
        self.assertEqual(cip.is_valid_data(input_data[1]), False)
        self.assertEqual(cip.is_valid_data(input_data[2]), False)
        self.assertEqual(cip.is_valid_data(input_data[3]), False) 
        self.assertEqual(cip.is_valid_data(input_data[4]), False)
        self.assertEqual(cip.is_valid_data(input_data[5]), False) 
        self.assertEqual(cip.is_valid_data(input_data[6]), False)
        self.assertEqual(cip.is_valid_data(input_data[7]), False)
        self.assertEqual(cip.is_valid_data(input_data[8]), False) 
        self.assertEqual(cip.is_valid_data(input_data[9]), False)
        self.assertEqual(cip.is_valid_data(input_data[10]), False) 

    def test_simple_conditions(self):
        input_data = [
            {"intensity": 2, "conditional_intensity": "1: B04<=0 ; 4: B02<=1"},
            {"intensity": 1, "conditional_intensity": "3: B06<8"},
            {"intensity": 1, "conditional_intensity": "3: B06==8"},
            {"intensity": 2, "conditional_intensity": "4: B06!=8 && B04>=3"},
        ]
        answers = {
            "B02": {"value": "1"},
            "B04": {"value": "1,2"},
            "B06": {"value": "8"},
            "PCR08": {"value": "4,Custom"},
            "PFA34": {"value": "2,Custom"}
        }
        self.assertEqual(cip.parse_conditional_intensity(input_data[0], answers), 4)
        self.assertEqual(cip.parse_conditional_intensity(input_data[1], answers), 1)
        self.assertEqual(cip.parse_conditional_intensity(input_data[2], answers), 3)
        self.assertEqual(cip.parse_conditional_intensity(input_data[3], answers), 2)

    def test_complex_conditions(self):
        input_data = [
            {"intensity": 1, "conditional_intensity": "3: PCR08>=2 && ( B04>3 || B06<=8 )"},
            {"intensity": 1, "conditional_intensity": "3: PFA34>=2 && ( B04>=3 && B06>8 )"}
        ]
        answers = {
            "B04": {"value": "1,2"},
            "B06": {"value": "8"},
            "PCR08": {"value": "4,Custom"},
            "PFA34": {"value": "2,Custom"}
        }
        self.assertEqual(cip.parse_conditional_intensity(input_data[0], answers), 3)
        self.assertEqual(cip.parse_conditional_intensity(input_data[1], answers), 1)

if __name__ == "__main__":
    unittest.main()
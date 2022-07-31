"""
Test cases for Bmi application
"""


import unittest
from bmi_main import BMI
import errors


class TestBmi(unittest.TestCase):

    """
    Class to test BMI Calculator, Status and category
    """

    def setUp(self):
        """
        Initial Setup
        """
        #Calulate BMI
        self.result1 = BMI(175, 93)
        self.result2 = BMI(160.0, 65.0)
        self.result3 = BMI('160', '65')
        self.result4 = BMI(' 160  ', '   65   ')
        self.result5 = BMI('175', 93)
        self.result6 = BMI(160, '65')
        self.result7 = BMI('', '65')
        self.result8 = BMI(175, '')
        self.result9 = BMI('', '')
        self.result10 = BMI('ab', '76')
        self.result11 = BMI('175.2', '76.7')
        self.result12 = BMI('178', 'a')

        #Compare BMI
        self.result13 = BMI(bmi_value=30.37)
        self.result14 = BMI(bmi_value=25.39)
        self.result15 = BMI(bmi_value="")
        self.result16 = BMI(bmi_value="ak")
        self.result17 = BMI(bmi_value=16.37)
        self.result18 = BMI(bmi_value=23.38)
        self.result19 = BMI(bmi_value=27.39)
        self.result20 = BMI(bmi_value=33.394)
        self.result21 = BMI(bmi_value=37.390624999999996)
        self.result22 = BMI(bmi_value=42.3906249)

    # def tearDown(self):
    #
    #     """
    #     Final setup, if required.
    #     """
    #     print('tearDown\n')

    def test_bmi(self):

        """
        To perform test cases for calculation of BMI
        """

        self.assertEqual(self.result1.to_calculate_bmi(), 30.37)
        self.assertEqual(self.result2.to_calculate_bmi(), 25.39)
        self.assertEqual(self.result3.to_calculate_bmi(), 25.39)
        self.assertEqual(self.result4.to_calculate_bmi(), 25.39)
        self.assertEqual(self.result5.to_calculate_bmi(), 30.37)
        self.assertEqual(self.result6.to_calculate_bmi(), 25.39)
        self.assertEqual(self.result7.to_calculate_bmi(), errors.HEIGHT_MISSING)
        self.assertEqual(self.result8.to_calculate_bmi(), errors.WEIGHT_MISSING)
        self.assertEqual(self.result9.to_calculate_bmi(), errors.HEIGHT_MISSING)
        self.assertEqual(self.result10.to_calculate_bmi(), errors.HEIGHT_MISSING)
        self.assertEqual(self.result11.to_calculate_bmi(), 24.99)
        self.assertEqual(self.result12.to_calculate_bmi(), errors.WEIGHT_MISSING)

    def test_bmi_status(self):
        """
        To perform Test cases for compare_bmi i.e Bmi status and category
        :return:
        """
        self.assertEqual(self.result13.compare_bmi(),
                         ['Moderately obese', '30 - 34.9', 'Medium risk'])
        self.assertEqual(self.result14.compare_bmi(),
                         ['Over Weight', '25 - 29.9', 'Enhanced risk'])
        self.assertEqual(self.result15.compare_bmi(),
                         "BMI is missing or wrong format please check")
        self.assertEqual(self.result16.compare_bmi(),
                         "BMI is missing or wrong format please check")
        self.assertEqual(self.result17.compare_bmi(),
                         ['Under Weight', '<18.4', 'Malnutrition risk'])
        self.assertEqual(self.result18.compare_bmi(),
                         ['Normal Weight', '18.5 - 24.9', 'Low risk'])
        self.assertEqual(self.result19.compare_bmi(),
                         ['Over Weight', '25 - 29.9', 'Enhanced risk'])
        self.assertEqual(self.result20.compare_bmi(),
                         ['Moderately obese', '30 - 34.9', 'Medium risk'])
        self.assertEqual(self.result21.compare_bmi(),
                         ['Severely obese', '35 - 39.9', 'High risk'])
        self.assertEqual(self.result22.compare_bmi(),
                         ['Very severely obese', '40+', 'Very high risk'])

    # Just for reference
    def test_both(self):
        """
        Just for reference calling both caculate and compare in a single test case.
        :return:
        """
        result = self.result1.to_calculate_bmi()
        self.assertEqual(result, 30.37)
        self.assertEqual(self.result1.compare_bmi(),
                         ['Moderately obese', ['30 - 34.9', 'Medium risk']])


if __name__ == '__main__':
    unittest.main()

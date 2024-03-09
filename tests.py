import unittest   # import test module
from conversions import *  # importing all the functions defined in conversions.py
from conversions_refactored import *
import tests





class ConversionsExpectedResult(unittest.TestCase):
    def test_celsius_to_kelvin_conversion(self):
        """Check that Celsius to Kelvin conversion is working correctly.
        Checking for expected result of 5 test cases."""
        test_values = [-200.00, -30.00, 0.00, 380.00, 500.00]  # 5 test case celsius values
        expected = [73.15, 243.15, 273.15, 653.15, 773.15]  # results for kelvin conversion for 5 test cases

        "Test for expected result when entering test values into the convert_celsius_to_kelvin function."
        for (i, n) in zip(test_values, expected):
            result = convert_celsius_to_kelvin(i)
            self.assertEqual(n, result, msg=f'For an input of {i} °C, the conversion result of {result} K matches the expected result of {n} K.')

    def test_celsius_to_fahrenheit_conversion(self):
        """Check that Celsius to Fahrenheit conversion is working correctly.
        Checking for expected result of 5 test cases."""
        test_values = [-200.00, -30.00, 0.00, 380.00, 500.00]  # 5 test case celsius values
        expected = [-328.00, -22.00, 32.00, 716.00, 932.00]  # results for fahrenheit conversion for 5 test cases

        "Test for expected result when entering test values into the convert_celsius_to_fahrenheit function."
        for (i, n) in zip(test_values, expected):
            result = convert_celsius_to_fahrenheit(i)
            self.assertEqual(n, result, msg=f'For an input of {i} °C the conversion result of {result} °F matches the expected result of {n} °F.')

    def test_fahrenheit_to_celsius_conversion(self):
        """Check that Fahrenheit to Celsius conversion is working correctly.
        Checking for expected result of 5 test cases."""
        test_values = [-200.00, -30.00, 0.00, 380.00, 500.00]  # 5 test case fahrenheit values
        expected = [-128.89, -34.44, -17.78, 193.33, 260.00]  # results for celsius conversion for 5 test cases

        "Test for expected result when entering test values into the convert_fahrenheit_to_celsius function."
        for (i, n) in zip(test_values, expected):
            result = convert_fahrenheit_to_celsius(i)
            self.assertEqual(n, result, msg=f'For an input of {i} °F the conversion result of {result} °C matches the expected result of {n} °C.')

    def test_fahrenheit_to_kelvin_conversion(self):
        """Check that Fahrenheit to Kelvin conversion is working correctly.
        Checking for expected result of 5 test cases."""
        test_values = [-200.00, -30.00, 0.00, 380.00, 500.00]  # 5 test case fahrenheit values
        expected = [144.26, 238.71, 255.37, 466.48, 533.15]  # results for kelvin conversion for 5 test cases

        "Test for expected result when entering test values into the convert_fahrenheit_to_kelvin function."
        for (i, n) in zip(test_values, expected):
            result = convert_fahrenheit_to_kelvin(i)
            self.assertEqual(n, result, msg=f'For an input of {i} °F the conversion result of {result} K matches the expected result of {n} K.')

    def test_kelvin_to_fahrenheit_conversion(self):
        """Check that Kelvin to Fahrenheit conversion is working correctly.
        Checking for expected result of 5 test cases."""
        test_values = [-200.00, -30.00, 0.00, 380.00, 500.00]  # 5 test case kelvin values
        expected = [-819.67, -513.67, -459.67, 224.33, 440.33]  # results for fahrenheit conversion for 5 test cases

        "Test for expected result when entering test values into the convert_kelvin_to_fahrenheit function."
        for (i, n) in zip(test_values, expected):
            result = convert_kelvin_to_fahrenheit(i)
            self.assertEqual(n, result, msg=f'For an input of {i} K the conversion result of {result} °F matches the expected result of {n} °F.')

    def test_kelvin_to_celsius_conversion(self):
        """Check that Kelvin to Celsius conversion is working correctly.
        Checking for expected result of 5 test cases."""
        test_values = [-200.00, -30.00, 0.00, 380.00, 500.00]  # 5 test case kelvin values
        expected = [-473.15, -303.15, -273.15, 106.85, 226.85]  # results for celsius conversion for 5 test cases

        "Test for expected result when entering test values into the convert_kelvin_to_celsius function."
        for (i, n) in zip(test_values, expected):
            result = convert_kelvin_to_celsius(i)
            self.assertEqual(n, result, msg=f'For an input of {i} K the conversion result of {result} °C matches the expected result of {n} °C.')

    def test_convert_temp_conversions(self):
        """Check that all the temperature conversions are working correctly.
        Checking for expected results of 5 test cases (-200.00, -30.00, 0.00, 380.00, 500.00) for each conversion.
        """
        test_values = [-200.00, -30.00, 0.00, 380.00, 500.00]  # 5 test case input values
        expected_celsius_to_kelvin = [73.15, 243.15, 273.15, 653.15, 773.15]  # results for celsius to kelvin conversion for 5 test cases
        expected_celsius_to_fahrenheit = [-328.00, -22.00, 32.00, 716.00, 932.00]  # results for celsius to fahrenheit conversion for 5 test cases
        expected_fahrenheit_to_celsius = [-128.89, -34.44, -17.78, 193.33, 260.00]  # results for fahrenheit to celsius conversion for 5 test cases
        expected_fahrenheit_to_kelvin = [144.26, 238.71, 255.37, 466.48, 533.15]  # results for fahrenheit to kelvin conversion for 5 test cases
        expected_kelvin_to_fahrenheit = [-819.67, -513.67, -459.67, 224.33, 440.33]  # results for kelvin to fahrenheit conversion for 5 test cases
        expected_kelvin_to_celsius = [-473.15, -303.15, -273.15, 106.85, 226.85]  # results for kelvin to celsius conversion for 5 test cases

        "Test for expected results for converting celsius to kelvin."
        for (i, n) in zip(test_values, expected_celsius_to_kelvin):
            result = convert('c', 'k', i)
            self.assertEqual(n, result, msg=f'For an input of {i} C° the conversion result of {result} K matches the expected result of {n} K.')

        "Test for expected results for converting celsius to fahrenheit."
        for (i, n) in zip(test_values, expected_celsius_to_fahrenheit):
            result = convert('c', 'f', i)
            self.assertEqual(n, result, msg=f'For an input of {i} C° the conversion result of {result} F° matches the expected result of {n} F°.')

        "Test for expected results for converting fahrenheit to celsius."
        for (i, n) in zip(test_values, expected_fahrenheit_to_celsius):
            result = convert('f', 'c', i)
            self.assertEqual(n, result, msg=f'For an input of {i} F° the conversion result of {result} C° matches the expected result of {n} C°.')

        "Test for expected results for converting fahrenheit to kelvin."
        for (i, n) in zip(test_values, expected_fahrenheit_to_kelvin):
            result = convert('f', 'k', i)
            self.assertEqual(n, result, msg=f'For an input of {i} F° the conversion result of {result} K matches the expected result of {n} K.')

        "Test for expected results for converting kelvin to fahrenheit."
        for (i, n) in zip(test_values, expected_kelvin_to_fahrenheit):
            result = convert('k', 'f', i)
            self.assertEqual(n, result, msg=f'For an input of {i} K the conversion result of {result} F° matches the expected result of {n} F°.')

        "Test for expected results for converting kelvin to celsius."
        for (i, n) in zip(test_values, expected_kelvin_to_celsius):
            result = convert('k', 'c', i)
            self.assertEqual(n, result, msg=f'For an input of {i} K the conversion result of {result} C° matches the expected result of {n} C°.')


    def test_convert_distance_conversions(self):
        """Check that all the distance conversions are working correctly.
        Checking for expected results of 5 test cases for each conversion.
        """
        test_values = [3.00, 25.00, 87.00, 100.00, 345.00]  # 5 test case input values
        expected_mile_to_yard = [5280.00, 44000.00, 153120.00, 176000.00, 607200.00]  # results for mile to yard conversion for 5 test cases
        expected_mile_to_meter = [4828.03, 40233.60, 140012.93, 160934.40, 555223.68]  # results for mile to meter conversion for 5 test cases
        expected_yard_to_mile = [0.002, 0.014, 0.049, 0.057, 0.196]  # results for yard to mile conversion for 5 test cases
        expected_yard_to_meter = [2.74, 22.85, 79.52, 91.41, 315.36]  # results for yard to meter conversion for 5 test cases
        expected_meter_to_mile = [0.002, 0.016, 0.054, 0.062, 0.214]  # results for meter to mile conversion for 5 test cases
        expected_meter_to_yard = [3.28, 27.35, 95.18, 109.40, 377.43]  # results for meter to yard conversion for 5 test cases

        "Test for expected results for converting mile to yard."
        for (i, n) in zip(test_values, expected_mile_to_yard):
            result = convert('mi', 'yd', i)
            self.assertEqual(n, result, msg=f'For an input of {i} mile(s) the conversion result of {result} yard(s) matches the expected result of {n} yard(s).')

        "Test for expected results for converting mile to meter."
        for (i, n) in zip(test_values, expected_mile_to_meter):
            result = convert('mi', 'm', i)
            self.assertEqual(n, result, msg=f'For an input of {i} mile(s) the conversion result of {result} meter(s) matches the expected result of {n} meter(s).')

        "Test for expected results for converting yard to mile."
        for (i, n) in zip(test_values, expected_yard_to_mile):
            result = convert('yd', 'mi', i)
            self.assertEqual(n, result, msg=f'For an input of {i} yard(s) the conversion result of {result} mile(s) matches the expected result of {n} mile(s).')

        "Test for expected results for converting yard to meter."
        for (i, n) in zip(test_values, expected_yard_to_meter):
            result = convert('yd', 'm', i)
            self.assertEqual(n, result, msg=f'For an input of {i} yard(s) the conversion result of {result} meter(s) matches the expected result of {n} meter(s).')

            "Test for expected results for converting meter to mile."
            for (i, n) in zip(test_values, expected_meter_to_mile):
                result = convert('m', 'mi', i)
                self.assertEqual(n, result, msg=f'For an input of {i} meter(s) the conversion result of {result} mile(s) matches the expected result of {n} mile(s).')

                "Test for expected results for converting meter to yard."
                for (i, n) in zip(test_values, expected_meter_to_yard):
                    result = convert('m', 'yd', i)
                    self.assertEqual(n, result, msg=f'For an input of {i} meter(s) the conversion result of {result} yard(s) matches the expected result of {n} yard(s).')

    def test_unit_converted_to_itself(self):
        """Check that converting from one unit to itself returns the same value for all units."""
        temperature_test_values = [-200.00, -30.00, 0.00, 380.00, 500.00]  # 5 test case temperature values
        distance_test_values = [3.00, 25.00, 87.00, 100.00, 345.00]  # 5 test case values

        "Test for expected results for converting kelvin to kelvin."
        for (i) in (temperature_test_values):
            result = convert('k', 'k', i)
            self.assertEqual(i, result, msg=f'For an input of {i} K the conversion result of {result} K matches the expected result of {i} K.')

        "Test for expected result for converting celsius to celsius."
        for (i) in (temperature_test_values):
            result = convert('c', 'c', i)
            self.assertEqual(i, result, msg=f'For an input of {i} °C the conversion result of {result} °C matches the expected result of {i} °C.')

        "Test for expected result for converting fahrenheit to fahrenheit."
        for (i) in (temperature_test_values):
            result = convert('f', 'f', i)
            self.assertEqual(i, result, msg=f'For an input of {i} °F the conversion result of {result} °F matches the expected result of {i} °F.')

        "Test for expected result for converting meter to meter."
        for (i) in (distance_test_values):
            result = convert('m', 'm', i)
            self.assertEqual(i, result, msg=f'For an input of {i} meter(s) the conversion result of {result} meter(s) matches the expected result of {i} meter(s).')

        "Test for expected result for converting yard to yard."
        for (i) in (distance_test_values):
            result = convert('yd', 'yd', i)
            self.assertEqual(i, result, msg=f'For an input of {i} yard(s) the conversion result of {result} yard(s) matches the expected result of {i} yard(s).')

        "Test for expected result for converting mile to mile."
        for (i) in (distance_test_values):
            result = convert('mi', 'mi', i)
            self.assertEqual(i, result, msg=f'For an input of {i} mile(s) the conversion result of {result} mile(s) matches the expected result of {i} mile(s).')

class ConversionsBadInput(unittest.TestCase):
    def test_incompatible_conversions(self):
        """convert should fail when trying to convert incompatible units (e.g., celsius (temperature) to yards (distance))."""
        self.assertRaises(tests.ConversionNotPossibleException, tests.convert, 'f', 'c', 25)

if __name__ == '__main__':
    unittest.main()



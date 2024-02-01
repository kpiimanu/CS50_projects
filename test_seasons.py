# Test module for DOB using class

import unittest
from datetime import date
from seasons import DOB


class DOBTestCase(unittest.TestCase):
    # Checking that this input of the function results in the following date
    def test_valid_date(self):
        self.assertEqual(DOB("1990-01-01"), date(1990, 1, 1))

    # Checking that if invalid input causes system to exit
    def test_invalid_date(self):
        with self.assertRaises(SystemExit):
            DOB("1990/01/01")


if __name__ == "__main__":
    unittest.main()
import unittest
from problem1.test.test_parser_fixedwidth_to_delimited import TestFixedWidthToCSVConverter

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFixedWidthToCSVConverter)
    unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    run_tests()
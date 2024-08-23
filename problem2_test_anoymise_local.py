import unittest
from problem2.test.test_anonymise_data import TestAnonymizeData

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAnonymizeData)
    unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    run_tests()
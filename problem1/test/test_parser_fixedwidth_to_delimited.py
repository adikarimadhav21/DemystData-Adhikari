import unittest
import os
import csv
from problem1.src.parser_fixedwidth_to_delimited import FixedWidthToDelimitedConvertor

class TestFixedWidthToCSVConverter(unittest.TestCase):
    def setUp(self):

        # Create a sample specification file for testing 
        self.spec = {
            "ColumnNames": ["c1", "c2", "c3"],
            "Offsets": ["5", "10", "7"],
            "FixedWidthEncoding": "windows-1252",
            "IncludeHeader": "True",
            "DelimitedEncoding": "utf-8"
        }

        # A sample fixed-width 
        self.fixed_width_data = "xyz  def       ghi143 \njklmn opqr      stuvwx \n"
        self.fixed_width_data_with_header = "c1    c2        c3    \nxyz  def       ghi143 \njklmn opqr      stuvwx \n"

        # Expected CSV data
        self.expected_csv_data = [
            ['c1', 'c2', 'c3'],     
            ['xyz', 'def', 'ghi143'],  
            ['jklmn', 'opqr', 'stuvwx']
        ]

        # Input and output file paths
        self.input_file = 'problem1/data/output/problem1_test_fixed_width.txt'
        self.output_file = 'problem1/data/output/problem1_test_output.csv'



    def tearDown(self):
        # Cleans up the temporary files after each test to avoid conflicts 
    
        os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def testConversion(self):
        # Write the fixed-width data to the input file
        with open(self.input_file, 'w', encoding="windows-1252") as f:
            f.write(self.fixed_width_data_with_header)
        converter = FixedWidthToDelimitedConvertor(self.spec, ",",self.input_file, self.output_file)

        # Convert fixed width to csv
        converter.convert_fixedWidth_to_delimited()

        # open the output CSV file
        with open(self.output_file, 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            output_data = [row for row in reader]

        # Check that the expected data matches the output   
        self.assertEqual(output_data, self.expected_csv_data)
     
    #case 2
    def testConversionWithoutHeader(self):
        # Write the fixed-width data to the input file
        with open(self.input_file, 'w', encoding="windows-1252") as f:
            f.write(self.fixed_width_data)
        # Modify the spec to exclude headers
        self.spec["IncludeHeader"] = "False"
        

        # Expected CSV data without headers
        expected_csv_data_no_header = [
            ['xyz', 'def', 'ghi143'],
            ['jklmn', 'opqr', 'stuvwx']
        ]

        converter = FixedWidthToDelimitedConvertor(self.spec, ",",self.input_file, self.output_file)
        # Convert fixed width to csv
        converter.convert_fixedWidth_to_delimited()

        # Read the output CSV file
        with open(self.output_file, 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            output_data = [row for row in reader]
        #test case2
        self.assertEqual(output_data, expected_csv_data_no_header)

# if __name__ == "__main__":
#     unittest.main()

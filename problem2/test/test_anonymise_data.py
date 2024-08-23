import unittest
import os
import sys
import csv
#sys.path.append("..")
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from  problem2.src.anonymise_data import AnonymizeData

class TestAnonymizeData(unittest.TestCase):
    def setUp(self):
        # Define anonymise_columns
        self.anonymise_columns=["first_name", "last_name", "address"]

        # A sample data
        self.sample_data = "first_name,last_name,address,date_of_birth\nSean,Mclean,\"09751 Elizabeth Road, Madisonland, PR 08925\",08/13/1985\n"

        # Expected  data
        self.expected_csv_data = [
            ['first_name', 'last_name', 'address','date_of_birth'],     
            ['oeaR', 'ocleaL', 'MDk3NTEgRWxpemFiZXRoIFJvYWQsIE1hZGlzb25sYW5kLCBQUiAwODkyNQ==','08/13/1985']      
        ]

        # Input and output file paths
        self.input_file = 'problem2/data/input/test_csv_file.txt'
        self.output_file = 'problem2/data/output/test_csv_file_anonymise.txt'

        # Write sample  data to the input file
        with open(self.input_file, 'w', encoding="utf-8") as f:
            f.write(self.sample_data)

    def tearDown(self):
        # Cleans up the temporary files after each test to avoid conflicts 
    
        os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def testConversion(self):
        converter = AnonymizeData(self.input_file,self.output_file,self.anonymise_columns)
        converter.anoymise_data()

        # open the output CSV file
        with open(self.output_file, 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            output_data = [row for row in reader]

        # Check that the expected data matches the output   
        self.assertEqual(output_data, self.expected_csv_data)
     
    #case 2: match with original and decode data
    def testDecode(self):

        converter = AnonymizeData(self.input_file,self.output_file,self.anonymise_columns)
        converter.anoymise_data()

    # Expected  data
        expected_csv_data = [
            ['first_name', 'last_name', 'address','date_of_birth'],
            ['Sean', 'Mclean', '09751 Elizabeth Road, Madisonland, PR 08925','08/13/1985']
        ]

        # open the output CSV file
        decode_data = []
        with open(self.output_file, 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if not 'first_name' in row: # skip header
                    row[0]=converter.unmask_string(row[0])
                    row[1]=converter.unmask_string(row[1])
                    row[2]=converter.base_64_decoding(row[2])
                decode_data.append(row)

        #test case2
        self.assertEqual(expected_csv_data, decode_data)

if __name__ == "__main__":
    unittest.main()

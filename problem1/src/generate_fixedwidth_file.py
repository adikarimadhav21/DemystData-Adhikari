import argparse
import os
import json
import random
import string
class FixedWidthFileGenerator:
    def __init__(self,spec):
        self.spec=spec
       # print(self.spec)
        self.column_names=self.spec['ColumnNames']
        self.offests=self.offset_int()
        self.fixed_width_encoding = self.spec["FixedWidthEncoding"]
        self.include_header = self.spec["IncludeHeader"].lower() == "true"
        self.delimited_encoding = self.spec["DelimitedEncoding"]
        self.num_columns = len(self.column_names)
   
    def offset_int(self):
        offsets = []
        for offset in self.spec["Offsets"]:
            offsets.append(int(offset))   
        return  offsets 
    def padding(self, data_value, width):
        """ Pad the data to fit the specified width.
            data.ljust(width):For example, if data is "abc" and width is 5,
            the result would be "abc " (2 spaces added to make the total length 5)
            [:width]:if data is "abcdefgh" and width is 5, the result would be "abcde".
        """
        return data_value.ljust(width)[:width]
    
    def random_data(self, length):
        """Generate a random string of with one to max offset length
        
        """
        leng=random.randint(1,length)
        return ''.join(random.choices(string.ascii_letters + string.digits, k=leng))

    

    def create_row(self):
        """Generate a single row of fixed-width formatted data."""
        row = []
        for i in range(self.num_columns):
            random_data = self.random_data(self.offests[i])
            padded_data = self.padding(random_data, self.offests[i])
            row.append(padded_data)
        return ''.join(row)  
   
    def generate_csv_file(self,num_rows, output_file):
        """ Write output files as fixed_width
        """ 
        try:
            with open(output_file, 'w', encoding=self.fixed_width_encoding) as file:
                if self.include_header:
                    header = ''.join([self.padding(name, self.offests[i]) for i, name in enumerate(self.column_names)])
                    file.write(header + '\n')
                
                for _ in range(num_rows):
                    row = self.create_row()
                    file.write(row + '\n')
            
            print(f"File '{output_file}' generated successfully! please check respective location")
        except Exception as e:
            print(f"Error writing to file: {e}")


def read_spec(spec_file): 
        ''' This method will read the spec file and provide spec as object

                - **Params:**
                - kwargs: spec_file
                
                - **Returns:**
                - (Python object ( dictionary)) : spec
        '''  
        if not os.path.exists(spec_file):
            raise FileNotFoundError(f"spec {spec_file} does not find")
        try:
            with open(spec_file,'r',encoding='utf-8') as file:
                spec=json.load(file)
        except json.JSONDecodeError:
            raise ValueError(f"Error parsing JSON from file '{spec_file}'.")
         
         # Validate if column names and offsets match in length
        if len(spec["ColumnNames"]) != len(spec["Offsets"]):
            raise ValueError(f"Number of 'ColumnNames' and 'Offsets' should be equal.")
        
        return spec


def main():
    
    msg="Generate a fixed-width file with random data"
    parser = argparse.ArgumentParser(description=msg)
    parser.add_argument(
        "--num_rows", 
        type=int, 
        default=100,  # Set default value to 100
        help="Number of rows (default: 100)"
    )

    # Parse arguments
    args = parser.parse_args()

    spec_file = "problem1/data/input/spec.json"  
    output_file = "problem1/data/output/fixed_width_file.txt"
    num_rows = args.num_rows  

    spec=read_spec(spec_file)
    generator = FixedWidthFileGenerator(spec)
    generator.generate_csv_file(num_rows, output_file)

if __name__=='__main__':
    main()
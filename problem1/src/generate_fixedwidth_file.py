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
   
    def generate_fixedwidth_file(self,num_rows, output_file):
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

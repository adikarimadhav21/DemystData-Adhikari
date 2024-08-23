import argparse
import os
import json
import csv
class FixedWidthToDelimitedConvertor:
    def __init__(self,spec,delimiter,input_file,output_file):
        self.spec=spec
        self.delimiter=delimiter
        self.input_file=input_file
        self.output_file=output_file
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
    
    def open_files(self):
        try:
            input_file = open(self.input_file, 'r', encoding=self.fixed_width_encoding)
            out_file = open(self.output_file, 'w', newline='', encoding=self.delimited_encoding)
            return input_file, out_file
        except FileNotFoundError as e:
            print(f"Error: {e}")
            raise
        

    def close_files(self, input_file, out_file):
        input_file.close()
        out_file.close()
    
    def convert_row(self,row):
        ''' This method will convert fixedwidth row to list of values for delimited row

                - **Params:**
                - kwargs: spec_file
                
                - **Returns:**
                - (Python object ( dictionary)) : spec
        '''  
        result_row=[]
        start=0
        for width in self.offests:
            end=start+width
            result_row.append(row[start:end].strip()) #strip: trim if space 
            start=end
        return result_row
    
   
    def convert_fixedWidth_to_delimited(self):
        """ read fixed_width and write delimited files
        """ 
        input_file, out_file=self.open_files()
        try:
          read_content=input_file.readlines()
          write_content=csv.writer(out_file,delimiter=self.delimiter)
        
        # #header write
        #   if self.include_header:
        #       write_content.writerow(self.column_names)
        #Each row
          for row in read_content:
              converted_row=self.convert_row(row)
              write_content.writerow(converted_row)   
          print(f"File '{self.output_file}' generated successfully! please check respective location")
  
        except Exception as e:
            print(f"Error writing to file: {e}")
        finally:
            self.close_files(input_file, out_file)    

#
# def read_spec(spec_file):
#         ''' This method will read the spec file and provide spec as object
#
#                 - **Params:**
#                 - kwargs: spec_file
#
#                 - **Returns:**
#                 - (Python object ( dictionary)) : spec
#         '''
#         if not os.path.exists(spec_file):
#             raise FileNotFoundError(f"spec {spec_file} does not find")
#         try:
#             with open(spec_file,'r',encoding='utf-8') as file:
#                 spec=json.load(file)
#         except json.JSONDecodeError:
#             raise ValueError(f"Error parsing JSON from file '{spec_file}'.")
#
#          # Validate if column names and offsets match in length
#         if len(spec["ColumnNames"]) != len(spec["Offsets"]):
#             raise ValueError(f"Number of 'ColumnNames' and 'Offsets' should be equal.")
#
#         return spec

#
# def main():
#
#     spec_file = "problem1/data/input/spec.json"
#     input_file="problem1/data/output/fixed_width_file.txt"
#     output_file = "problem1/data/output/delimited_file.txt"
#
#     parser = argparse.ArgumentParser(description="Convert a fixed-width file to a delimited file.")
#     parser.add_argument("--delimiter", type=str, default=",", help="Delimiter for the CSV file (default: comma).")
#     args = parser.parse_args()
#     delimiter=args.delimiter
#
#     spec=read_spec(spec_file)
#     generator = FixedWidthToDelimitedConvertor(spec,delimiter,input_file,output_file)
#     generator.convert_fixedWidth_to_delimited()
#
# if __name__=='__main__':
#     main()
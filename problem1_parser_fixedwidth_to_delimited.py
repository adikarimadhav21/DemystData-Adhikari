import argparse
import os
import json
import csv


from problem1.src.parser_fixedwidth_to_delimited import  *

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

    spec_file = "problem1/data/input/spec.json"
    input_file="problem1/data/output/problem1_fixed_width_file.txt"
    output_file = "problem1/data/output/problem1_delimited_file.txt"

    parser = argparse.ArgumentParser(description="Convert a fixed-width file to a delimited file.")
    parser.add_argument("--delimiter", type=str, default=",", help="Delimiter for the CSV file (default: comma).")
    args = parser.parse_args()
    delimiter=args.delimiter

    spec=read_spec(spec_file)
    generator = FixedWidthToDelimitedConvertor(spec,delimiter,input_file,output_file)
    generator.convert_fixedWidth_to_delimited()

if __name__=='__main__':
    main()
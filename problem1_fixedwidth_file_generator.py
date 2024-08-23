import argparse
import json
import os
from problem1.src.generate_fixedwidth_file import FixedWidthFileGenerator
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
    output_file = "problem1/data/output/problem1_fixed_width_file.txt"
    num_rows = args.num_rows

    spec=read_spec(spec_file)
    generator = FixedWidthFileGenerator(spec)
    generator.generate_fixedwidth_file(num_rows, output_file)

if __name__=='__main__':
    main()
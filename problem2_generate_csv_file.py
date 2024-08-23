import argparse
from problem2.src.generate_csv_file import CSVFileGenerator
def main():

    msg="Generate a CSV file"
    parser = argparse.ArgumentParser(description=msg)
    parser.add_argument(
        "--num_rows",
        type=int,
        default=500,  # Set default value to 100
        help="Number of rows (default: 500)"
    )

    # Parse arguments
    args = parser.parse_args()

    output_file = "problem2/data/output/problem2_csv_file.txt"
    num_rows = args.num_rows
    columns = ["first_name", "last_name", "address", "date_of_birth"]

    generator = CSVFileGenerator(num_rows, output_file,columns)
    generator.generate_csv_file()

if __name__=='__main__':
    main()
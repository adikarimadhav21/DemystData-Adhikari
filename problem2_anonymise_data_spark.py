
from problem2.src.anonymise_data_spark import *
def main():
    input_file = "problem2/data/output/problem2_csv_file.txt"
    output_file = "problem2/data/output/problem2_csv_file_anonymize"
    anonymise_columns = ["first_name", "last_name", "address"]
    anonymise_data(input_file, output_file, anonymise_columns)

if __name__ == '__main__':
    main()

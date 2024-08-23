from problem2.src.anonymise_data import AnonymizeData
def main():
    input_file="problem2/data/output/problem2_csv_file.txt"
    output_file="problem2/data/output/problem2_csv_file_anonymise.txt"
    anonymise_columns=["first_name", "last_name", "address"]
    anoymise=AnonymizeData(input_file,output_file,anonymise_columns)
    anoymise.anoymise_data()

if __name__=='__main__':
    main()
import argparse
from faker import Faker
import csv 
class CSVFileGenerator:
    def __init__(self,num_rows, output_file,columns):
        self.num_rows=num_rows
        self.output_file=output_file
        self.columns=columns
        self.fake=Faker()
    
    #Fake data generate 
    def random_first_name(self):
        return self.fake.first_name()
    def random_last_name(self):
        return self.fake.last_name()
    def random_address(self):
        return self.fake.address().replace('\n', ', ')
    def random_date_of_birth(self):
        return self.fake.date_of_birth().strftime('%m/%d/%Y')  #MM/dd/yyyy
           
    #Save fake data to output file as delimited
    def generate_csv_file(self):
        try: 
            with open(self.output_file, mode='w', newline='\n') as file:
                writer = csv.writer(file)
                writer.writerow(self.columns)  # Write the header row

                # loop for each row
                for _ in range(self.num_rows): 
                    writer.writerow([self.random_first_name(), \
                                     self.random_last_name(), self.random_address(), self.random_date_of_birth()])

            print(f"Generated CSV file in {self.output_file}")
        except Exception as e:
            print(f"Error while writing file {self.output_file}: {e}")    

#
# def main():
#
#     msg="Generate a CSV file"
#     parser = argparse.ArgumentParser(description=msg)
#     parser.add_argument(
#         "--num_rows",
#         type=int,
#         default=5,  # Set default value to 100
#         help="Number of rows (default: 100)"
#     )
#
#     # Parse arguments
#     args = parser.parse_args()
#
#     output_file = "problem2/data/input/csv_file.txt"
#     num_rows = args.num_rows
#     columns = ["first_name", "last_name", "address", "date_of_birth"]
#
#     generator = CSVFileGenerator(num_rows, output_file,columns)
#     generator.generate_csv_file()
#
# if __name__=='__main__':
#     main()
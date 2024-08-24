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

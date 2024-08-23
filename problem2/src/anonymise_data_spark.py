import base64
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType
import os
class AnonymizeData:
    def __init__(self, input_file, output_file, anonymise_columns):
        # Dynamically find the base directory of the script
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct file paths using os.path.join
        self.input_file = os.path.join(base_dir, input_file)
        print("????????????????????????",base_dir)
        print("????????????????????????",self.input_file)

        self.output_file = os.path.join(base_dir, output_file)
        self.anonymise_columns = anonymise_columns
        self.spark = SparkSession.builder.appName("Data Anonymization").getOrCreate()

    def base_64_encoding(self, text):
        return str(base64.b64encode(text.encode("utf-8")).decode("utf-8"))

    def base_64_decoding(self, text):
        return str(base64.b64decode(text.encode('utf-8')).decode('utf-8'))

    def mask_string(self, s):
        if len(s) == 0:
            return s
        if len(s) == 1:
            return chr(ord(s[0]) + 1)

        first_char = s[-1]
        last_char = s[0]

        modified_first = chr(ord(first_char) + 1)
        modified_last = chr(ord(last_char) - 1)

        return modified_first + s[1:-1] + modified_last

    def unmask_string(self, s):
        if len(s) == 0:
            return s
        if len(s) == 1:
            return chr(ord(s[0]) - 1)

        first_char = s[-1]
        last_char = s[0]

        original_last = chr(ord(last_char) - 1)
        original_first = chr(ord(first_char) + 1)

        return original_first + s[1:-1] + original_last

    def anonymize_data(self):
        # Read the CSV into a Spark DataFrame
        df = self.spark.read.csv(self.input_file, header=True)

        # Define UDFs for masking and encoding
        base64_udf = udf(self.base_64_encoding, StringType())
        mask_udf = udf(self.mask_string, StringType())

        # Apply the transformations
        for column in self.anonymise_columns:
            if column == "address":
                df = df.withColumn(column, base64_udf(col(column)))
            else:
                df = df.withColumn(column, mask_udf(col(column)))

        # Save the anonymized data back to CSV
        df.write.csv(self.output_file, header=True)
        print(f"Anonymized CSV file written to {self.output_file}")

def main():
    input_file = "../data/input/csv_file.csv"
    output_file = "../data/output/csv_file_anonymize"
    anonymise_columns = ["first_name", "last_name", "address"]

    anonymizer = AnonymizeData(input_file, output_file, anonymise_columns)
    anonymizer.anonymize_data()

if __name__ == '__main__':
    main()

import base64
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType

# Function to encode text using base64
def base_64_encoding(text):
    return base64.b64encode(text.encode("utf-8")).decode("utf-8")


"""
step 1 Swap first and last characters
step 2 first char increase assci value and last char assci decrease 

"""
def mask_string(s):
    if len(s) == 0:
        return s
    # If only one character, just increment its ASCII value by 1
    if len(s) == 1:
        return chr(ord(s[0]) + 1)

        # Step 1: Swap first and last characters
    first_char = s[-1]
    last_char = s[0]

    # Step 2: Modify the ASCII values
    # Increase ASCII of the swapped first char
    # Decrease ASCII of the swapped last char
    modified_first = chr(ord(first_char) + 1)
    modified_last = chr(ord(last_char) - 1)

    # Return the modified string with swapped and changed first/last chars
    return modified_first + s[1:-1] + modified_last

def unmask_string(s):
    if len(s) == 0:
        return s
    # Reverse the change by decrementing the ASCII value by 1
    if len(s) == 1:
        return chr(ord(s[0]) - 1)

        # Step 1: Swap first and last characters back
    first_char = s[-1]
    last_char = s[0]

    # Step 2: Reverse the ASCII modifications
    original_last = chr(ord(last_char) -1)
    original_first = chr(ord(first_char) + 1)
    return original_first + s[1:-1] + original_last


def anonymise_data(input_file, output_file, anonymise_columns):
    # Initialize Spark session
    spark = SparkSession.builder.master("local[1]").config("spark.network.timeout", "600s").appName("Data Anonymization").getOrCreate()

    # Read the CSV into a Spark DataFrame
    df = spark.read.csv(input_file, header=True)

    # Define UDFs for masking and encoding
    base64_udf = udf(lambda x:base_64_encoding(x), StringType())
    mask_udf = udf(lambda  x:mask_string(x), StringType())

    # Apply the transformations
    for column in anonymise_columns:
        if column == "address":
            df = df.withColumn(column, base64_udf(col(column)))
        else:
            df = df.withColumn(column, mask_udf(col(column)))

    # Save the anonymized data back to CSV
    df.write.csv(output_file, header=True,mode='overwrite')
    print(f"Anonymized CSV file written to {output_file}")

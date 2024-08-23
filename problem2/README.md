
## Problem2 Anonymize data
### Madhav Adhikari
### Description:
- Delimited File Generator ( problem2_generate_csv_file.py)

  This project will generate csv file using random data containing first_name, last_name, address, date_of_birth.It allow user to specify the delimiter(default 500 ).

- CSV to anonymize data convertion for small file  (problem2_anonymise_local.py)

  This project will anonymize data using a masking technique. 
  The first and last names will be masked by swapping the first and last characters, 
  then increasing the ASCII value of the swapped first character and decreasing the ASCII
  value of the swapped last character. The address column will be masked using base64 encoding. 
  The project also includes unit tests (TestAnonymizeData) to ensure the correctness of the masking logic

- CSV to anonymize data convertion for big file  (problem2_anonymise_data_spark.py)

  This project will anonymize data using a masking technique on a distributed PySpark platform, enabling efficient parallel processing for both large and small files. If memory issues or slow processing are encountered, 
  the application can be tuned for optimal performance.

### Files

|  # | File                                                                                                                                                              | Description                                        |
|:--:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------| -------------------------------------------------- |
|  1 | [ generate_csv_file.py](https://github.com/adikarimadhav21/DemystData-Adhikari/blob/main/problem2/src/generate_csv_file.py )                        | main script to generate random csv file   |
|  2 | [ problem2_csv_file.txt](https://github.com/adikarimadhav21/DemystData-Adhikari/blob/main/problem2/data/output/problem2_csv_file.txt )                              |This file will stored output as csv format   |
|  3 | [ anonymise_data.py](https://github.com/adikarimadhav21/DemystData-Adhikari/blob/main/problem2/src/anonymise_data.py)            |This file is main script to anonymize data for small files  |
|  4 | [ test_anonymise_data.py](https://github.com/adikarimadhav21/DemystData-Adhikari/blob/main/problem2/test/test_anonymise_data.py ) |This file have test cases to validate conversion   |
|  5 | [ problem2_csv_file_anonymise.txtt](https://github.com/adikarimadhav21/DemystData-Adhikari/blob/main/problem2/data/output/problem2_csv_file_anonymise.txt)                          |This file will stored output as anonymized data    |
|  6 | [ anonymise_data_spark.py](https://github.com/adikarimadhav21/DemystData-Adhikari/blob/main/problem2/src/anonymise_data_spark.py)                          |This file will anonymize data  using pyspark   |


### Instructions
- Option 1 using docker file: Example
    - git clone [repository_url](https://github.com/adikarimadhav21/DemystData-Adhikari.git)
    - docker build -f Dockerfile.problem2local -t problem2_anonymise_local .
    - docker run --name problem2 -v output:/app/problem2/data/output problem2_anonymise_local
    - docker build -f Dockerfile.problem2spark -t problem2_anonymise_spark .
    - docker run --name problem2 -v output:/app/problem2/data/output problem2_anonymise_spark



- Option 2 using python command
    - Make sure you install python3
    - git clone [repository_url](https://github.com/adikarimadhav21/DemystData-Adhikari.git)
    - install requirements.txt
    - run python problem2_generate_csv_file.py --num_rows <number_of_rows>
    - run  python problem2_anonymise_local.py
    - To run all unit tests, python problem2_test_anoymise_local.py
    - run pyspark , spark-submit --master local[*] problem2_anonymise_data_spark.py or python problem2_anonymise_data_spark.py


### Example Command:
- python  problem2_generate_csv_file.py --num_rows 300
- python problem2_anonymise_local.py
- python  python problem2_test_anoymise_local.p


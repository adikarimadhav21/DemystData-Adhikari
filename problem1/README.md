
## Problem1
### Madhav Adhikari
### Description:
- Fixed-Width File Generator ( generate_fixedwidth_file.py)
  
    This project will generate fixed-width files using random data based on spec.json specification.It allow user to specify the number of rows(default 100 ) and enconding will be windows-1252.
- Fixed-Width to CSV Converter (parser_fixedwidth_to_delimited.py)  

    This project will  convert fixed-width files into CSV format using Python(default comma (,)  delimiter and allow user to pass as well), without relying on external libraries like pandas. It includes a FixedWidthFileGenerator class that reads a fixed-width text file, based on the provided spec, and converts it to a delimited file. The project also includes unit tests (TestFixedWidthToCSVConverter) to ensure the correctness of the conversion logic.




### Files

|   #   | File            | Description                                        |
| :---: | --------------- | -------------------------------------------------- |
|   1   | [spec.json](https://github.com/adikarimadhav21/DemystData-Adhikari/blob/main/problem1/data/input/spec.json )       | A JSON file that have the column names, field offsets, and other metadata.   |
|   2  |[ generate_fixedwidth_file.py](https://github.com/adikarimadhav21/DemystData-Adhikari/blob/main/problem1/src/generate_fixedwidth_file.py )      | main script to generate fixedwidth file   |
|   3  |[ fixed_width_file.txt](https://github.com/adikarimadhav21/DemystData-Adhikari/blob/main/problem1/data/output/fixed_width_file.txt )      |This file will stored output as fixed_width   |
|   4 |[ parser_fixedwidth_to_delimited.py](https://github.com/adikarimadhav21/DemystData-Adhikari/blob/main/problem1/src/parser_fixedwidth_to_delimited.py )      |This file is main script to convert fixedwidth to csv file   |
|   5  |[ test_parser_fixedwidth_to_delimited.py](https://github.com/adikarimadhav21/DemystData-Adhikari/blob/main/problem1/test/test_parser_fixedwidth_to_delimited.py )      |This file have test cases to validate conversion   |
|   6  |[ delimited_file.txt](https://github.com/adikarimadhav21/DemystData-Adhikari/blob/main/problem1/data/output/delimited_file.txt)      |This file will stored output as delimited    |




### Instructions

- Make sure you install python3
- git clone [repository_url](https://github.com/adikarimadhav21/DemystData-Adhikari.git)
- run python generate_fixedwidth_file.py --num_rows <number_of_rows>
- run python parser_fixedwidth_to_delimited.py --delimiter <name of delimiter>
- To run all unit tests, python -m unittest test_parser_fixedwidth_to_delimited.py


### Example Command:
- python generate_fixedwidth_file.py --num_rows 300
- python parser_fixedwidth_to_delimited.py --delimiter "|"
- python -m unittest test_parser_fixedwidth_to_delimited.py



import base64
import csv
import os

class AnonymizeData:
    def __init__(self,input_file,output_file,anonymise_columns):

        self.input_file = input_file
        self.output_file = output_file
        self.anonymise_columns=anonymise_columns

    
    def base_64_encoding(self,text):
        return str(base64.b64encode(text.encode("utf-8")).decode("utf-8"))


    def base_64_decoding(self,text):
        return str(base64.b64decode(text.encode('utf-8')).decode('utf-8'))

    """
    step 1 Swap first and last characters
    step 2 first char increase assci value and last char assci decrease 

    """

    def mask_string(self,s):
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

    def unmask_string(self,s):
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
    
    def open_files(self):
        try:
            input_file = open(self.input_file, 'r',newline='\n', encoding='utf-8')
            out_file = open(self.output_file, 'w', newline='\n', encoding="utf-8")
            return input_file, out_file
        except FileNotFoundError as e:
            print(f"Error: {e}")
            raise
        

    def close_files(self, input_file, out_file):
        input_file.close()
        out_file.close()
    def masked_row(self,row_data) :
         for column in self.anonymise_columns:
             if column=="address":
                 row_data[column]=self.base_64_encoding(row_data[column])
             else:   
                 row_data[column]=self.mask_string(row_data[column])
         return  row_data  
        
    def anoymise_data(self):
        input_file, out_file=self.open_files()
        reader = csv.DictReader(input_file)
        writer = csv.DictWriter(out_file, fieldnames=reader.fieldnames)
        
        #Write Header
        writer.writeheader()  
        
        for row in reader:
            masked_row = self.masked_row(row)
            writer.writerow(masked_row)
        self.close_files(input_file, out_file) 
        print(f"Anoymized CSV file in {self.output_file}")   


# First we'll import the os module
# This will allow us to create file paths across operating systems
import os 
# Module for reading CSV files
import csv 

csvpath = os.path.join('Resources', 'budget_data.csv')

print(csvpath) 

 # Method 1: Plain Reading of CSV files

with open(csvpath, 'r') as file_handler:
     lines = file_handler.read()
     print(lines)
     print(type(lines))


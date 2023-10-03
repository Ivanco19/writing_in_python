'''
This is how you write CSV files in python
'''

import os, csv

output_path = os.path.join('.', 'new.csv')

with open(output_path, 'w', newline="") as my_file:
    my_writer = csv.writer(my_file)

    my_writer.writerow(['id', 'Name', 'SSN'])
    my_writer.writerow(['1', 'Jose', '1234'])
    my_writer.writerow(['2', 'Ana', '5678'])
    my_writer.writerow(['3', 'Andres', '9012'])
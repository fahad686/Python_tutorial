'''
here are two types of modules in python:

Built in Modules - These modules are ready to import and use and ships with the python interpreter. there is no need to install such modules explicitly.
External Modules - These modules are imported from a third party file or can be installed using a package manager like pip or conda.
'''
import pandas

# Read and work with a file named 'words.csv'
df = pandas.read_csv('words.csv')
print(df) # This will display first few rows from the words.csv file


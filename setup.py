"""The setup file for parsing and running the projects"""
import os

# Project settings
projects = ['1-BigInteger', '2-MovieDatabase', '3-StackCalculator', '4-Sorting', '5-Matching', '6-Subway']
executables = ['BigInteger', 'MovieDatabaseConsole', 'CalculatorTest', 'SortingTest', 'Matching', 'Subway']
arguments = [False, False, False, False, False, True]


# The separator used in path. For some reason, this seems to work in Windows too...
slash = '/'

# Tester settings
source_path = f"{os.getcwd()}{slash}source"
results_path = f"{os.getcwd()}{slash}results"

# Command to execute .class file
command = 'java'


# On windows, a newline character is represented by \r\n.
# Having the replace flag set as True will replace the windows_newline in input/output files to the newline char.
# This ensures that files created in different environments compare to be the same.
replace_windows_newline = True
windows_newline = '\r\n'
newline = '\n'

# Output customization
verbose = True  # When set to True, changes output style to verbose
dump_input = True  # When set to True, also dumps the input file to ./results
dump_expected_output = True  # When set to True, also dumps the expected output to ./results
dump_error = True  # When set to True, also dumps the errors to ./results
dump_output_when_error = False  # When set to True, even when you're correct, dumps the output to ./results if you have error
dump_expected_output_when_error = False  # When set to True, even when you're correct, dumps the expected output to ./results if you have error

# encoding
encoding = 'utf-8'

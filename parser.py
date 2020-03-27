import os
import sys
import pickle

projects = ['1-BigInteger', '2-MovieDatabase', '3-StackCalculator', '4-Sorting', '5-Matching', '6-Subway']

io_data = {}

for project in projects:
    path = f"{os.getcwd()}/testcases/{project}/testset/"
    input_path = path + 'input/'
    output_path = path + 'output/'

    input_filenames = []
    output_filenames = []
    for filename in os.listdir(input_path):
        assert filename.endswith('.txt')
        extensionless_filename = filename.split('.')[0]
        assert extensionless_filename.isdigit()
        input_filenames.append(filename)
    for filename in os.listdir(output_path):
        assert filename.endswith('.txt')
        extensionless_filename = filename.split('.')[0]
        try:
            assert extensionless_filename.isdigit()
        except AssertionError:
            print(output_path)
            print(filename)
            print("'" + extensionless_filename + "'")
            sys.exit(1)
        output_filenames.append(filename)
    input_filenames.sort()
    output_filenames.sort()
    assert input_filenames == output_filenames

    input_files_as_str = []
    output_files_as_str = []

    for filename in input_filenames:
        with open(input_path + filename, 'r') as f:
            input_files_as_str.append(f.read())

    for filename in output_filenames:
        with open(output_path + filename, 'r') as f:
            output_files_as_str.append(f.read())

    io_data[project] = [input_files_as_str, output_files_as_str]

for project in projects:
    with open(f'{os.getcwd()}/testsets/{project}.pickle', 'wb') as f:
        pickle.dump(io_data[project], f)


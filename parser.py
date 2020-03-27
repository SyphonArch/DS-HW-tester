import os
import sys
import pickle

projects = ['1-BigInteger', '2-MovieDatabase', '3-StackCalculator', '4-Sorting', '5-Matching', '6-Subway']


class TestSet:
    """Class for a testset of a single project"""
    def __init__(self, inputs, outputs):
        assert len(inputs) == len(outputs)
        self.inputs = inputs
        self.outputs = outputs
        self._len = len(inputs)

    def __len__(self):
        return self._len


slash = '/'
def load_testset(project):
    """Loads the testset of a single project and returns a TestSet object"""
    path = f"{os.getcwd()}{slash}testcases{slash}{project}{slash}testset{slash}"
    input_path = path + f'input{slash}'
    output_path = path + f'output{slash}'

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

    testset = TestSet(input_files_as_str, output_files_as_str)
    return testset



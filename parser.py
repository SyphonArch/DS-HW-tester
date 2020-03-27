"""Provides the class for storing a testset, as well as a function to load it from files."""
import os
import sys
import pickle
from setup import slash, arguments, projects


class TestSet:
    """Class for a testset of a single project"""
    def __init__(self, inputs, outputs, arguments=None):
        assert len(inputs) == len(outputs)
        if arguments is not None:
            assert len(inputs) == len(arguments)
        self.inputs = inputs
        self.outputs = outputs
        self._len = len(inputs)
        self.arguments = arguments

    def __len__(self):
        return self._len


def load_testset(homework_number):
    assert homework_number in range(1, 7)
    project = projects[homework_number - 1]
    """Loads the testset of a single project and returns a TestSet object"""
    path = f"{os.getcwd()}{slash}testcases{slash}{project}{slash}testset{slash}"
    input_path = path + f'input{slash}'
    output_path = path + f'output{slash}'
    argument_path = path + f'argument{slash}'

    input_filenames = []
    output_filenames = []
    argument_filenames = []
    for filename in os.listdir(input_path):
        assert filename.endswith('.txt')
        extensionless_filename = filename.split('.')[0]
        assert extensionless_filename.isdigit()
        input_filenames.append(filename)
    for filename in os.listdir(output_path):
        assert filename.endswith('.txt')
        extensionless_filename = filename.split('.')[0]
        assert extensionless_filename.isdigit()
        output_filenames.append(filename)
    input_filenames.sort()
    output_filenames.sort()
    assert input_filenames == output_filenames

    if arguments[homework_number - 1]:
        for filename in os.listdir(argument_path):
            assert filename.endswith('.txt')
            extensionless_filename = filename.split('.')[0]
            assert extensionless_filename.isdigit()
            argument_filenames.append(filename)

    input_files_as_str = []
    output_files_as_str = []
    arguments_as_str = []

    for filename in input_filenames:
        with open(input_path + filename, 'r') as f:
            input_files_as_str.append(f.read())

    for filename in output_filenames:
        with open(output_path + filename, 'r') as f:
            output_files_as_str.append(f.read())

    for filename in argument_filenames:
        with open(argument_path + filename, 'r') as f:
            arguments_as_str.append(f.read())

    proj_args = arguments_as_str if arguments[homework_number - 1] else None
    testset = TestSet(input_files_as_str, output_files_as_str, proj_args)
    return testset


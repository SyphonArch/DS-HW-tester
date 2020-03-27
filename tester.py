"""Runs the test on a java file"""
from parser import load_testset
from setup import slash, projects, executables, arguments, command
from sys import argv
import os
import subprocess


def test(hw_num, input_str, argument=None):
    executable_name = executables[hw_num - 1]

    to_execute = [command, '-cp', f'{os.getcwd()}{slash}source{slash}', executable_name]
    if argument:
        to_execute.append(argument)
    result = subprocess.run(to_execute, input=input_str.encode('utf-8'), stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')


if __name__ == '__main__':
    if len(argv) < 2:
        while True:
            homework_number = input("Input homework number: ")
            if homework_number.isdigit() and int(homework_number) in range(1, 7):
                homework_number = int(homework_number)
                break
            print("Invalid input.")
    else:
        if not argv[1].isdigit():
            raise TypeError("Homework number must be an integer")

        homework_number = int(argv[1])

        if homework_number not in range(1, 7):
            raise IndexError("Homework number must be an integer")

    testset = load_testset(homework_number)
    for i in range(len(testset)):
        inp, out, arg = testset.test_data(i)
        rslt = test(homework_number, inp, arg)
        print(i + 1, out == rslt)
    print("Done!")
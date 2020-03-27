"""Runs the test on a java file"""
from parser import load_testset
from setup import slash, projects, executables, arguments
from sys import argv
import os
import subprocess


command = 'java'
def test(homework_number, input_str):
    executable_name = executables[homework_number - 1]

    to_execute = [command, f'{os.getcwd()}{slash}{source}{slash}{executable_name}']
    if arguments[homework_number - 1]:
        pass
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

    project = projects[homework_number - 1]

    testset = load_testset(project)

    for i in range(len(testset))

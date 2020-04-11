"""Runs the test on a java file"""
from loader import load_testset
from setup import *
from sys import argv
import os
import subprocess
from time import time

__version__ = '0.2.1'
__author__ = 'SyphonArch'


def println():
    print('-----------------------------------------')


def test(hw_num, input_str, argument=None):
    executable_name = executables[hw_num - 1]

    to_execute = [command, '-cp', f'{source_path}{slash}', executable_name]
    if argument:
        to_execute.append(argument)
    result = subprocess.run(to_execute, input=input_str.encode('utf-8'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output_str = result.stdout.decode('utf-8')
    if replace_windows_newline:
        output_str = output_str.replace(windows_newline, newline)
    error_str = result.stderr.decode('utf-8')
    return output_str, error_str


if __name__ == '__main__':
    print(f"[DS-HW-tester {__version__} by {__author__}]")
    println()

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

    println()
    print(f"<HW {homework_number}>")
    print("Loading testset from file...")
    testset = load_testset(homework_number)
    print(f"Loaded testset of {len(testset)} testcases from file!\n")

    results_nonempty = False
    for filename in os.listdir(results_path):
        if filename.endswith('.txt'):
            results_nonempty = True
    if results_nonempty:
        input("** WARNING: Files found in ./results! **\nThey will be deleted once you press Enter. (Ctrl-C to abort)")
    for filename in os.listdir(results_path):
        if filename.endswith('.txt'):
            os.remove(results_path + slash + filename)
    if results_nonempty:
        print("./results has been cleared.")
        print()

    input("Press Enter to initiate testing.")
    println()
    print("Testing initiated.")
    start_time = time()

    success_cnt = 0
    fail_cnt = 0
    err_cnt = 0

    fails = []
    errors = []
    error_with_fails = []

    prev_progress = 11
    int_str_len = len(str(len(testset)))
    for i in range(len(testset)):
        inp, out, arg = testset.test_data(i)
        if replace_windows_newline:
            out = out.replace(windows_newline, newline)

        rslt, err = test(homework_number, inp, arg)

        match = out == rslt
        if err:
            verdict = 'E'
            err_cnt += 1
        elif match:
            verdict = 'O'
        else:
            verdict = 'X'

        # Output for user
        if verbose:
            print("#{{:{}d}}:".format(int_str_len).format(i + 1), verdict, end=' | ', flush=True)
            if (i + 1) % 10 == 0:
                print()
        else:
            progress = (len(testset) - i) * 10 // len(testset) + 1
            for num in range(prev_progress - 1, progress - 1, -1):
                print(f'{progress}...', flush=True, end='')
            prev_progress = progress
            if i == len(testset) - 1:
                print()

        if match:
            success_cnt += 1
            if err:
                errors.append([i, rslt, inp, out, err])
        else:
            fail_cnt += 1
            if err:
                error_with_fails.append([i, rslt, inp, out, err])
            else:
                fails.append([i, rslt, inp, out])

    finish_time = time()
    elapsed = finish_time - start_time
    println()
    print("Done!")
    print("That took {:.2f} seconds.".format(elapsed))
    print(f"Your code has passed {success_cnt}/{len(testset)} testcases.")
    if err_cnt or fail_cnt:
        if err_cnt:
            print("** WARNING: There are {} testcases with errors! **".format(err_cnt))

        println()
        if fail_cnt:
            print("Dumping outputs with differences...")
            for i in range(len(fails)):
                idx, rslt, inp, out = fails[i]
                # Input dump
                if dump_input:
                    with open(f"{results_path}{slash}{testset.filename_front(idx)}" +
                            '-input.txt', 'w', encoding=encoding) as f:
                        f.write(inp)
                # User-program output dump
                with open(f"{results_path}{slash}{testset.filename_front(idx)}" +
                        '-output.txt', 'w', encoding=encoding) as f:
                    f.write(rslt)
                # Expected output dump
                if dump_expected_output:
                    with open(f"{results_path}{slash}{testset.filename_front(idx)}" +
                            '-expected.txt', 'w', encoding=encoding) as f:
                        f.write(out)
        if dump_error:
            print("Dumping outputs with errors...")
            for i in range(len(errors)):
                idx, rslt, inp, out, err = errors[i]
                # Error dump
                with open(f"{results_path}{slash}{testset.filename_front(idx)}" +
                        '-error.txt', 'w', encoding=encoding) as f:
                    f.write(err)
                # Input dump
                if dump_input:
                    with open(f"{results_path}{slash}{testset.filename_front(idx)}" +
                            '-input.txt', 'w', encoding=encoding) as f:
                        f.write(inp)
                # User-program output dump
                if dump_output_when_error:
                    with open(f"{results_path}{slash}{testset.filename_front(idx)}" +
                            '-output.txt', 'w', encoding=encoding) as f:
                        f.write(rslt)
                # Expected output dump
                if dump_expected_output_when_error:
                    with open(f"{results_path}{slash}{testset.filename_front(idx)}" +
                            '-expected.txt', 'w', encoding=encoding) as f:
                        f.write(out)
        for i in range(len(error_with_fails)):
            idx, rslt, inp, out, err = error_with_fails[i]
            # Error dump
            if dump_error:
                with open(f"{results_path}{slash}{testset.filename_front(idx)}" +
                        '-error.txt', 'w', encoding=encoding) as f:
                    f.write(err)
            # Input dump
            if dump_input:
                with open(f"{results_path}{slash}{testset.filename_front(idx)}" +
                        '-input.txt', 'w', encoding=encoding) as f:
                    f.write(inp)
            # User-program output dump
            with open(f"{results_path}{slash}{testset.filename_front(idx)}" +
                      '-output.txt', 'w', encoding=encoding) as f:
                f.write(rslt)
            # Expected output dump
            if dump_expected_output:
                with open(f"{results_path}{slash}{testset.filename_front(idx)}" +
                        '-expected.txt', 'w', encoding=encoding) as f:
                    f.write(out)

        if dump_error:
            print(f"{fail_cnt + len(errors)} outputs with differences or errors have been dumped to ./results for your inspection.")
        elif fail_cnt:
            print(f"{fail_cnt} outputs with differences have been dumped to ./results for your inspection.")
        print("Good luck with your debugging!")
    else:
        print("You are good to go!")

    println()
    input("Press Enter to terminate.")

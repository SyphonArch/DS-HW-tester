# DS-HW-tester 0.1.5
## Python script to run automated tests on the homework tasks of the Data Structure lecture(2020).

The default testsets are the official ones, having been downloaded from ETL, with the following exception:  

>A file named '.txt' was found under the '/3-StackCalculator/testset/output/'.
>
>It was ignored in the parsing of the testsets as it did not match the input format for that project.

Note: It is known that at least one testset has faulty testcases - homework #3 has several.

### Prerequisites
* Have Python 3 installed
* Have `java` in PATH
* Have homework compiled to `.class` Java bytecode

### How to use the tester
1. Clone the repository to your environment of choice.
2. Place your compiled `.class` files of your homework task into the `./source` directory.
3. Run `tester.py` with Python 3.

   You must be CDed into the root directory of this repo.
   
   When running the tester, you may provide the homework number as an argument like below:
   
   `python3 tester.py 1`
   
   If not provided as an argument, you will be prompted upon the execution.
4. That's it! Output that doesn't match will be stored under `./results`.

   For subtle differences you may find the `diff` command useful.

### Customization
You may edit the settings in the `setup.py` file to change program behaviour.

One change you might try is settings the `verbose` flag to `False`.

### Adding testcases
1. You add your test input files to `./testcases/{PROJECT_NAME}/testset/input/`
1. You add your expected output files to `./testcases/{PROJECT_NAME}/testset/output/`
3. That's it! You can now run the tester. It will load new testcases automatically.

   Just make sure that your files end with a `.txt` extension.


### Platforms
This tester was tested on **macOS Catalina** and **Windows 10**. + And now on **Ubuntu 18.04**.

If it doesn't work on your machine, too bad. It worked on my machine. lolz.

### Changelog
* Version 0.1.2: Added input/expected output to results dumping, changed testcase ordering
* Version 0.1.3: Added test timer, results dumping moved to after testing
* Version 0.1.4: Added support for relative path inputs in HW 5, and changed verbose output
* Version 0.1.5: Fixed bug concerning arguments for HW 6, by removing newline char from argument string

### Important sidenote
This tester is just a tester.

i.e., Passing all testcases on this tester does not guarantee that your program will pass the 'official' testing.

Please use only as a testing tool and reference for debugging.

Thanks!

### Future update plans
Custom testcases and/or custom testcase generator

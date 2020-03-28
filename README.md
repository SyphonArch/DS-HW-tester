# DS-HW-tester 0.1.0
## Python script to run automated tests on the homework tasks of the Data Structure lecture(2020).

The default testsets are the official ones, having been downloaded from ETL, with the following exception:  

>A file named '.txt' was found under the '/3-StackCalculator/testset/output/'.
>
>It was ignored in the parsing of the testsets as it did not match the input format for that project.

### How to use the tester
1. Clone the repository to your environment of choice.
2. Place your compiled `.class` files into the `./source` directory.
3. Run `tester.py` with Python 3.

   You must be CDed into the root directory of this repo.
   
   When running the tester, you may provide the homework number as an argument like below:
   
   `python3 tester.py 1`
   
   If not provided as an argument, you will be prompted upon the execution.
4. That's it! Output that doesn't match will be stored under `./results`.

### Customization
You may edit the settings in the `setup.py` file to change program behaviour.

One change you might try is settings the `verbose` flag to `True`.

### Adding testcases
1. You add your test input files to `./testcases/{PROJECT_NAME}/testset/input/`
1. You add your expected output files to `./testcases/{PROJECT_NAME}/testset/output/`
3. You run the tester! It will load new testcases automatically.


### Platforms
This tester was tested on macOS and Windows.

If it doesn't work on your machine, too bad. It worked on my machine. lolz.



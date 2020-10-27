Hello! Welcome to my program analyzing program. I will explain what is included, how to use the program, 
assumptions I have made, and how this code would be integrated and extended.

1. What is included:
    - The actual program is in analyzer.py, it contains two functions:
        i. analyze: actual program.
        ii. get_identifiers: helper function to decide what characters are used to identify comments
    - 8 test cases for basic popular programming languages that are supported by default; although
      any language can be used as long as the comment identifiers are passed in by the user.
    - A test_results.txt file containing the printed output of running the tests that I wrote.
    - This readme

2. How to use:
    This program was written in Python 3.8. Python must be installed on the machine that is to run 
    this, and once that is the case, simply run analyzer.py and the included test suite will execute.
    Note that the test files must be in the same folder in order for the automated tests to run. 

    To run with your own tests, simply pass in the filename and path to that file into the analyze()
    function, and look at your results :)

    NOTE: For detailed information on both functions, please see the docstrings within analyzer.py

3. Assumptions:
    - It is okay for the program to be written in Python.
    - If the program is not in one of the default-supported languages, the user will pass in 
      comment identifiers.
    - Python multi-line comments use triple quotes like so: """, not ''' .
    - Comment enabling characters are not part of strings. 
    - A single file is given as input, if more files are to be evaluated, they can be passed in one by one.

4. How the code can be integrated and extended:
    If this were to become part of an actual system, it would be fairly platform agnostic and compatible
    since it runs independently, and prints output instead of returning. This means output can easily be 
    written to a file for later use. Moving forward, it would be good to add code quality/syntax checkers 
    to this program; i.e. making sure every opened comment is closed, ensuring there's not too much 
    whitespace or unfinished TODO's etc. 
    
    If you have any questions or concerns, please reach out to me @ erichasegawa1@gmail.com
